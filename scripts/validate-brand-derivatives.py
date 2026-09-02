#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JOBS_PATH = ROOT / "brand/manifests/digital-derivative-jobs.json"
OMNI_PATH = ROOT / "brand/manifests/omnichannel-brand-manifest.json"
errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def load_json(path: Path):
    if not path.exists():
        fail(f"missing required file: {path.relative_to(ROOT)}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON {path.relative_to(ROOT)}: {exc}")
        return {}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def png_size(path: Path):
    data = path.read_bytes()
    if len(data) < 24 or not data.startswith(b"\x89PNG\r\n\x1a\n") or data[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", data[16:24])


def valid_webp(path: Path) -> bool:
    data = path.read_bytes()
    return len(data) >= 12 and data[:4] == b"RIFF" and data[8:12] == b"WEBP"


jobs_cfg = load_json(JOBS_PATH)
omni = load_json(OMNI_PATH)
generated = omni.get("generated_derivative_batches", {})

for batch in jobs_cfg.get("batches", []):
    batch_id = batch.get("id")
    if not batch_id:
        fail("derivative batch missing id")
        continue
    record = generated.get(batch_id, {})
    if not record:
        fail(f"{batch_id}: missing generated derivative manifest record")
        continue

    approval_rel = batch.get("approval_manifest")
    approval_path = ROOT / approval_rel if approval_rel else None
    approvals = {}
    if not approval_path or not approval_path.exists():
        fail(f"{batch_id}: missing approval manifest {approval_rel!r}")
    else:
        approval_data = load_json(approval_path)
        approvals = {item.get("path"): item for item in approval_data.get("assets", [])}

    if record.get("approval_manifest") != approval_rel:
        fail(f"{batch_id}: approval manifest provenance mismatch")
    if record.get("renderer") != jobs_cfg.get("renderer"):
        fail(f"{batch_id}: renderer provenance mismatch")
    if record.get("qa_status") != "passed":
        fail(f"{batch_id}: QA status must be passed")

    qa_rel = batch.get("qa_contact_sheet")
    qa_path = ROOT / qa_rel if qa_rel else None
    if not qa_path or not qa_path.exists():
        fail(f"{batch_id}: missing QA contact sheet {qa_rel!r}")
    else:
        if record.get("qa_contact_sheet") != qa_rel:
            fail(f"{batch_id}: QA contact-sheet path mismatch")
        if record.get("qa_contact_sheet_sha256") != sha256(qa_path):
            fail(f"{batch_id}: QA contact-sheet hash mismatch")

    records = {item.get("id"): item for item in record.get("assets", [])}
    jobs = batch.get("jobs", [])
    if set(records) != {job.get("id") for job in jobs}:
        fail(f"{batch_id}: generated asset record set does not match job set")

    required_status = batch.get("publication_status_required")
    for job in jobs:
        aid = job.get("id")
        source_rel = job.get("source")
        source = ROOT / source_rel if source_rel else None
        rec = records.get(aid, {})

        if not source or not source.exists():
            fail(f"{batch_id}/{aid}: missing source {source_rel!r}")
            continue
        approval = approvals.get(source_rel, {})
        if approval.get("publication_status") != required_status:
            fail(f"{batch_id}/{aid}: source is not {required_status} in approval manifest")
        if approval.get("text_free") is not True:
            fail(f"{batch_id}/{aid}: source must remain text-free")
        if rec.get("source") != source_rel:
            fail(f"{batch_id}/{aid}: source provenance mismatch")
        if rec.get("source_sha256") != sha256(source):
            fail(f"{batch_id}/{aid}: source hash mismatch")
        if rec.get("publication_status") != required_status:
            fail(f"{batch_id}/{aid}: publication status mismatch")
        if rec.get("text_free") is not True:
            fail(f"{batch_id}/{aid}: derivative record must remain text-free")
        if rec.get("qa_status") != "passed":
            fail(f"{batch_id}/{aid}: QA status must be passed")

        width = int(job.get("width", 0))
        height = int(job.get("height", 0))
        if rec.get("width") != width or rec.get("height") != height:
            fail(f"{batch_id}/{aid}: recorded dimensions mismatch")

        files = rec.get("files", {})
        for fmt, job_key in (("png", "output_png"), ("webp", "output_webp")):
            rel = job.get(job_key)
            path = ROOT / rel if rel else None
            meta = files.get(fmt, {})
            if not path or not path.exists():
                fail(f"{batch_id}/{aid}: missing {fmt} derivative {rel!r}")
                continue
            if meta.get("path") != rel:
                fail(f"{batch_id}/{aid}: {fmt} path mismatch")
            if meta.get("bytes") != path.stat().st_size:
                fail(f"{batch_id}/{aid}: {fmt} byte count mismatch")
            if meta.get("sha256") != sha256(path):
                fail(f"{batch_id}/{aid}: {fmt} hash mismatch")
            if fmt == "png":
                if png_size(path) != (width, height):
                    fail(f"{batch_id}/{aid}: PNG signature/dimensions mismatch")
            else:
                if not valid_webp(path):
                    fail(f"{batch_id}/{aid}: invalid WebP signature")
                if meta.get("lossless") is not bool(job.get("webp_lossless", True)):
                    fail(f"{batch_id}/{aid}: WebP lossless contract mismatch")

if errors:
    print("LuxSync brand derivative validation FAILED:")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

batch_count = len(jobs_cfg.get("batches", []))
asset_count = sum(len(batch.get("jobs", [])) for batch in jobs_cfg.get("batches", []))
print("LuxSync brand derivative validation PASSED")
print(f"Batches: {batch_count}")
print(f"Assets: {asset_count}")
print("Derivatives: PNG + lossless WebP with manifest hashes and QA evidence")

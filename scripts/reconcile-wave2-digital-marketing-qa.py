#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "brand/manifests/wave2-digital-marketing-manifest.json"
APPROVAL_PATH = ROOT / "brand/audit/wave2-digital-marketing-qa-approval.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    if not MANIFEST_PATH.exists():
        raise SystemExit("Wave 2 manifest is missing")
    if not APPROVAL_PATH.exists():
        print("Wave 2 QA approval record not present; leaving manifest pending manual review")
        return

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    approval = json.loads(APPROVAL_PATH.read_text(encoding="utf-8"))

    if approval.get("result") != "passed":
        raise SystemExit("Wave 2 QA approval result is not passed")
    if approval.get("reviewed_asset_count") != manifest.get("static_asset_count"):
        raise SystemExit("Wave 2 QA approval asset count does not match manifest")

    qa = manifest.get("qa", {})
    qa_rel = qa.get("contact_sheet")
    if not qa_rel:
        raise SystemExit("Wave 2 manifest is missing QA contact sheet path")
    qa_path = ROOT / qa_rel
    if not qa_path.exists():
        raise SystemExit(f"Wave 2 QA contact sheet missing: {qa_rel}")

    actual_sha = sha256(qa_path)
    manifest_sha = qa.get("sha256")
    approved_sha = approval.get("reviewed_sha256")
    if not (actual_sha == manifest_sha == approved_sha):
        raise SystemExit(
            "Wave 2 QA approval hash mismatch: "
            f"actual={actual_sha} manifest={manifest_sha} approval={approved_sha}"
        )

    approval_sheet = approval.get("reviewed_contact_sheet")
    if approval_sheet != qa_rel:
        raise SystemExit("Wave 2 QA approval contact sheet path mismatch")

    for asset in manifest.get("static_assets", []):
        asset["qa_status"] = "passed"
    qa["status"] = "passed-manual-review"
    qa["approval_record"] = str(APPROVAL_PATH.relative_to(ROOT)).replace("\\", "/")
    qa["approval_record_sha256"] = sha256(APPROVAL_PATH)
    manifest["status"] = "qa-passed"

    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print("Wave 2 manual visual QA reconciled into manifest")
    print(f"Reviewed contact sheet SHA256: {actual_sha}")


if __name__ == "__main__":
    main()

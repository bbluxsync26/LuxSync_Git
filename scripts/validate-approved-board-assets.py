#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import json
import re
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "brand/manifests/approved-board-asset-manifest.json"
EXPECTED_COUNTS = {"icons": 16, "dividers": 42}
EXPECTED_TOTAL = 58
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def png_size(path: Path):
    data = path.read_bytes()
    if len(data) < 24 or not data.startswith(b"\x89PNG\r\n\x1a\n") or data[12:16] != b"IHDR":
        fail(f"{path.relative_to(ROOT)}: invalid PNG")
        return None
    return struct.unpack(">II", data[16:24])


def webp_valid(path: Path) -> bool:
    data = path.read_bytes()
    if len(data) < 12 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        fail(f"{path.relative_to(ROOT)}: invalid WebP")
        return False
    return True


if not MANIFEST_PATH.exists():
    raise SystemExit("Missing brand/manifests/approved-board-asset-manifest.json")
manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
assets = manifest.get("assets", [])
if manifest.get("source") != "approved-reference-boards":
    fail("approved-board manifest source mismatch")
if manifest.get("status") != "wave1-board-derived-assets-qa-passed":
    fail("approved-board manifest status mismatch")
if manifest.get("asset_count") != EXPECTED_TOTAL or len(assets) != EXPECTED_TOTAL:
    fail(f"expected {EXPECTED_TOTAL} approved board-derived assets; found {len(assets)}")
if manifest.get("counts") != EXPECTED_COUNTS:
    fail(f"approved-board category counts mismatch: {manifest.get('counts')!r}")

seen: set[str] = set()
counts = {k: 0 for k in EXPECTED_COUNTS}
for item in assets:
    aid = item.get("id", "")
    category = item.get("category")
    if not aid or aid in seen:
        fail(f"duplicate or missing approved-board asset id: {aid!r}")
        continue
    seen.add(aid)
    if category not in counts:
        fail(f"{aid}: invalid category {category!r}")
        continue
    counts[category] += 1
    if item.get("master_type") != "raster-origin-board-crop":
        fail(f"{aid}: master_type must identify raster board provenance")
    if item.get("svg_type") != "embedded-raster-svg-fidelity-container":
        fail(f"{aid}: SVG must be labeled as a fidelity container")
    if item.get("publication_status") != "approved-board-derived":
        fail(f"{aid}: publication_status mismatch")
    if item.get("qa_status") != "passed":
        fail(f"{aid}: QA is not passed")

    source_rel = item.get("source_board", "")
    source = ROOT / source_rel
    if not source_rel or not source.exists():
        fail(f"{aid}: missing source board {source_rel!r}")
    elif item.get("source_board_sha256") != sha256(source):
        fail(f"{aid}: source board hash mismatch")

    width, height = int(item.get("width", 0)), int(item.get("height", 0))
    if width <= 0 or height <= 0:
        fail(f"{aid}: invalid dimensions")

    files = item.get("files", {})
    resolved = {}
    for key in ("master", "png", "webp", "svg"):
        meta = files.get(key, {})
        rel = meta.get("path", "")
        path = ROOT / rel
        resolved[key] = path
        if not rel or not path.exists():
            fail(f"{aid}: missing {key} output")
            continue
        if meta.get("bytes") != path.stat().st_size:
            fail(f"{aid}.{key}: byte count mismatch")
        if meta.get("sha256") != sha256(path):
            fail(f"{aid}.{key}: hash mismatch")

    if resolved.get("master") and resolved["master"].exists() and resolved.get("png") and resolved["png"].exists():
        if resolved["master"].read_bytes() != resolved["png"].read_bytes():
            fail(f"{aid}: master PNG and digital PNG must remain byte-identical")
        size = png_size(resolved["png"])
        if size and size != (width, height):
            fail(f"{aid}: PNG dimensions {size} != {(width, height)}")
    if resolved.get("webp") and resolved["webp"].exists():
        webp_valid(resolved["webp"])
    if resolved.get("svg") and resolved["svg"].exists():
        svg = resolved["svg"].read_text(encoding="utf-8")
        if f'viewBox="0 0 {width} {height}"' not in svg:
            fail(f"{aid}: SVG fidelity container has wrong or missing viewBox")
        if "Embedded-raster fidelity container" not in svg or "data:image/png;base64," not in svg:
            fail(f"{aid}: SVG is not explicitly documented/encoded as a fidelity container")
        match = re.search(r"data:image/png;base64,([^\"']+)", svg)
        if not match:
            fail(f"{aid}: embedded PNG payload missing from SVG")
        else:
            try:
                embedded = base64.b64decode(match.group(1), validate=True)
                if resolved.get("png") and resolved["png"].exists() and embedded != resolved["png"].read_bytes():
                    fail(f"{aid}: SVG embedded PNG differs from approved digital PNG")
            except Exception as exc:
                fail(f"{aid}: invalid SVG embedded PNG payload: {exc}")

if counts != EXPECTED_COUNTS:
    fail(f"actual approved-board category counts mismatch: {counts!r}")

for qa_key in ("icons_contact_sheet", "dividers_contact_sheet"):
    meta = manifest.get("qa", {}).get(qa_key, {})
    rel = meta.get("path", "")
    path = ROOT / rel
    if not rel or not path.exists():
        fail(f"missing QA contact sheet: {qa_key}")
    elif meta.get("sha256") != sha256(path):
        fail(f"QA contact sheet hash mismatch: {qa_key}")

reference_only = manifest.get("template_reference_only", [])
expected_families = {
    "section-separators", "buttons-and-cta-states", "smart-home-category-cards",
    "stationery-and-print-suite", "ui-controls-and-product-meta", "hero-banner-examples",
}
actual_families = {item.get("family") for item in reference_only}
if actual_families != expected_families:
    fail(f"template/reference-only family set mismatch: {sorted(actual_families ^ expected_families)}")

if errors:
    print("LuxSync approved-board asset validation FAILED:")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("LuxSync approved-board asset validation PASSED")
print("Approved board-derived assets: 58")
print("Families: 16 metallic icons + 42 dividers/accents")
print("Formats: master PNG + PNG + lossless WebP + SVG fidelity container")

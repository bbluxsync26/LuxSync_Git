#!/usr/bin/env python3
from pathlib import Path
import json, struct

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "brand/assets"
SOURCE = ROOT / "brand/source-logo"
errors = []
expected = {
    "01-logos": 3,
    "02-icons": 15,
    "03-buttons": 18,
    "04-ui-controls": 25,
    "05-dividers-accents": 24,
    "06-product-cards": 4,
    "07-heroes": 4,
    "08-sections": 3,
    "09-stationery": 4,
}
logos = ["LuxSync_Logo_Horizontal_Combo.png", "LuxSync_Logo_Horizontal_Final.png", "LuxSync_Logo_Orb.png"]
for name in logos:
    src = SOURCE / name
    dst = ASSETS / "01-logos" / name
    if not src.exists(): errors.append(f"missing authoritative logo master: {name}")
    if not dst.exists(): errors.append(f"missing production logo copy: {name}")
    elif src.read_bytes() != dst.read_bytes(): errors.append(f"production logo differs from authoritative master: {name}")
for folder, count in expected.items():
    p = ASSETS / folder
    actual = len(list(p.glob("*.png"))) if p.exists() else 0
    if actual != count: errors.append(f"brand/assets/{folder}: expected {count} PNG files; found {actual}")
if list(ASSETS.rglob("*.svg")):
    errors.append("placeholder SVG files remain under brand/assets")
for p in ASSETS.rglob("*.png"):
    data = p.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n") or data[12:16] != b"IHDR":
        errors.append(f"invalid PNG: {p.relative_to(ROOT)}")
        continue
    width, height = struct.unpack(">II", data[16:24])
    if width < 32 or height < 32: errors.append(f"implausibly small PNG: {p.relative_to(ROOT)}")
manifest_path = ASSETS / "asset-manifest.json"
if not manifest_path.exists():
    errors.append("missing brand/assets/asset-manifest.json")
else:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("version") != "5.1-production-source-of-truth": errors.append("asset manifest version mismatch")
    if manifest.get("source_of_truth") != "brand/assets": errors.append("asset manifest source_of_truth mismatch")
    if manifest.get("official_slogan") != "Where Luxury Lives Intelligently": errors.append("asset manifest slogan mismatch")
    statuses = manifest.get("status_by_folder", {})
    if statuses.get("01-logos") != "production-approved": errors.append("logo folder must be production-approved")
    for folder in expected:
        if folder != "01-logos" and statuses.get(folder) != "reference-only": errors.append(f"{folder} must be reference-only")
    files = manifest.get("files", [])
    if len(files) != sum(expected.values()): errors.append(f"asset manifest expected {sum(expected.values())} files; found {len(files)}")
    for item in files:
        path = Path(item.get("path", ""))
        status = item.get("publication_status")
        if "01-logos" in path.parts and status != "production-approved": errors.append(f"wrong publication status: {path}")
        if "01-logos" not in path.parts and status != "reference-only": errors.append(f"wrong publication status: {path}")
for rel in ("brand/README.md", "brand/assets/README.md", "brand/colors.md", "website/styles/design-system.md"):
    p = ROOT / rel
    if not p.exists(): errors.append(f"missing governing file: {rel}")
    else:
        text = p.read_text(encoding="utf-8")
        for token in ("#7B96B2", "#D6B0A0", "Brushed Dusty Steel"):
            if token not in text: errors.append(f"{rel}: missing {token}")
if errors:
    print("LuxSync production brand validation FAILED:")
    for error in errors: print("-", error)
    raise SystemExit(1)
print("LuxSync production brand validation PASSED")

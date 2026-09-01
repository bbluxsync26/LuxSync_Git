#!/usr/bin/env python3
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "brand/assets"
errors = []
required_logos = ["LuxSync_Logo_Horizontal_Combo.png","LuxSync_Logo_Horizontal_Final.png","LuxSync_Logo_Orb.png"]
for name in required_logos:
    src = ROOT / "brand/source-logo" / name
    dst = ASSETS / "01-logos" / name
    if not src.exists(): errors.append(f"missing authoritative logo master: {name}")
    if not dst.exists(): errors.append(f"missing production logo copy: {name}")
    elif src.read_bytes() != dst.read_bytes(): errors.append(f"production logo differs from authoritative master: {name}")
expected = {"01-logos":3,"02-icons":15,"03-buttons":18,"04-ui-controls":25,"05-dividers-accents":24,"06-product-cards":4,"07-heroes":4,"08-sections":3,"09-stationery":4}
for folder, count in expected.items():
    p = ASSETS / folder
    actual = len(list(p.glob("*.png"))) if p.exists() else 0
    if actual != count: errors.append(f"brand/assets/{folder}: expected {count} PNGs; found {actual}")
if list(ASSETS.rglob("*.svg")): errors.append("placeholder SVG files remain under brand/assets")
for p in ASSETS.rglob("*.png"):
    data = p.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n") or data[12:16] != b"IHDR": errors.append(f"invalid PNG: {p.relative_to(ROOT)}")
manifest_path = ASSETS / "asset-manifest.json"
if not manifest_path.exists(): errors.append("missing production asset manifest")
else:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("version") != "5.0-production-raster": errors.append("manifest version must be 5.0-production-raster")
    if manifest.get("source_of_truth") != "brand/assets": errors.append("manifest source_of_truth must be brand/assets")
for rel in ["brand/README.md","brand/assets/README.md","brand/colors.md"]:
    p = ROOT / rel
    if not p.exists(): errors.append(f"missing governing document: {rel}")
    else:
        t = p.read_text(encoding="utf-8")
        for token in ("#7B96B2","#D6B0A0","Brushed Dusty Steel"):
            if token not in t: errors.append(f"{rel}: missing {token}")
for rel,tokens in {"content/faqs.md":("Find My LuxSync Solution","info@luxsync.net","support@luxsync.net"),"website/pages/faqs.md":("FAQPage",)}.items():
    p = ROOT / rel
    if p.exists():
        text = p.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text: errors.append(f"{rel}: missing website contract token {token!r}")
if errors:
    print("LuxSync production asset validation failed:")
    for e in errors: print("-", e)
    raise SystemExit(1)
print("LuxSync production asset validation passed.")

#!/usr/bin/env python3
"""Validate the approved LuxSync atomic brand asset source of truth."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "brand" / "assets"
OLD_V3 = ROOT / "brand" / "assets-v3"

REQUIRED_LOGOS = [
    ROOT / "brand/source-logo/LuxSync_Logo_Horizontal_Combo.png",
    ROOT / "brand/source-logo/LuxSync_Logo_Horizontal_Final.png",
    ROOT / "brand/source-logo/LuxSync_Logo_Orb.png",
]
COUNTS = {
    "01-logos": 3,
    "02-icons": 15,
    "03-buttons": 18,
    "04-ui-controls": 25,
    "05-dividers-accents": 44,
    "06-product-cards": 4,
    "07-heroes": 1,
    "08-roi": 1,
    "09-stationery": 4,
    "11-marketing": 2,
    "12-palette": 9,
}
REQUIRED = [
    "brand/assets/README.md",
    "brand/assets/asset-manifest.json",
    "brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.svg",
    "brand/assets/01-logos/LuxSync_Logo_Horizontal_Final.svg",
    "brand/assets/01-logos/LuxSync_Logo_Orb.svg",
    "brand/assets/02-icons/home.svg",
    "brand/assets/02-icons/security-shield.svg",
    "brand/assets/03-buttons/primary-shop-now.svg",
    "brand/assets/03-buttons/utility-add-to-cart.svg",
    "brand/assets/04-ui-controls/toggle-on.svg",
    "brand/assets/04-ui-controls/search-bar.svg",
    "brand/assets/05-dividers-accents/brushed-dusty-steel-wide.svg",
    "brand/assets/05-dividers-accents/sparkle-12.svg",
    "brand/assets/06-product-cards/touch-panel.svg",
    "brand/assets/07-heroes/homepage-smart-living.svg",
    "brand/assets/08-roi/smart-home-roi-guide-hero.svg",
    "brand/assets/09-stationery/business-card-front.svg",
    "brand/assets/09-stationery/letterhead.svg",
    "brand/assets/11-marketing/roi-guide-promo.svg",
    "brand/assets/12-palette/brushed-dusty-steel-metallic.svg",
    "content/about.md",
    "content/faqs.md",
    "docs/leadership/bridgette-beardsley.md",
    "docs/leadership/sheldon-bardol.md",
    "website/pages/about.md",
    "website/pages/faqs.md",
]

errors = []
if OLD_V3.exists():
    errors.append("retired brand/assets-v3 directory still exists")
for path in REQUIRED_LOGOS:
    if not path.exists():
        errors.append(f"missing authoritative logo master: {path.relative_to(ROOT)}")
for rel in REQUIRED:
    if not (ROOT / rel).exists():
        errors.append(f"missing required file: {rel}")

for folder, expected in COUNTS.items():
    path = ASSETS / folder
    actual = len(list(path.glob("*.svg"))) if path.exists() else 0
    if actual != expected:
        errors.append(f"brand/assets/{folder}: expected {expected} individual SVGs; found {actual}")

manifest_path = ASSETS / "asset-manifest.json"
if manifest_path.exists():
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("version") != "4.0-atomic":
        errors.append("asset manifest version must be 4.0-atomic")
    if manifest.get("source_of_truth") != "brand/assets":
        errors.append("asset manifest source_of_truth must be brand/assets")
    if "Brushed Dusty Steel" not in manifest.get("metallic_blue", ""):
        errors.append("asset manifest must identify Brushed Dusty Steel as the approved metallic blue")
    files = manifest.get("files", [])
    if not isinstance(files, list) or len(files) < 127:
        errors.append("asset manifest does not enumerate the complete atomic library")

for rel in ["brand/README.md", "brand/assets/README.md", "brand/colors.md"]:
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing governing document: {rel}")
        continue
    text = path.read_text(encoding="utf-8")
    for token in ("#7B96B2", "#D6B0A0", "Brushed Dusty Steel"):
        if token not in text:
            errors.append(f"{rel}: missing approved-brand token {token!r}")

asset_docs = "\n".join(
    p.read_text(encoding="utf-8", errors="ignore")
    for p in [ROOT / "brand/README.md", ROOT / "brand/colors.md", ASSETS / "README.md"]
    if p.exists()
).lower()
if "icy-blue highlight tints may be used" in asset_docs:
    errors.append("retired icy-blue derivation permission remains")

for rel in ("brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.svg", "brand/assets/01-logos/LuxSync_Logo_Horizontal_Final.svg", "brand/assets/01-logos/LuxSync_Logo_Orb.svg"):
    p = ROOT / rel
    if p.exists() and "../../source-logo/" not in p.read_text(encoding="utf-8"):
        errors.append(f"{rel}: logo wrapper must reference authoritative source-logo artwork")

website_contract = {
    "content/faqs.md": ("Find My LuxSync Solution", "info@luxsync.net", "support@luxsync.net"),
    "website/pages/faqs.md": ("FAQPage",),
}
for rel, tokens in website_contract.items():
    path = ROOT / rel
    if path.exists():
        text = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                errors.append(f"{rel}: missing website contract token {token!r}")

pricing = ROOT / "docs/decisions/DEC-005-senior-service-pricing.md"
if pricing.exists() and "No senior-service price is currently approved for public display" not in pricing.read_text(encoding="utf-8"):
    errors.append("senior-service pricing publication guardrail is missing")

if errors:
    print("LuxSync atomic brand validation failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("LuxSync atomic brand validation passed.")

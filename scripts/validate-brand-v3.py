#!/usr/bin/env python3
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
V3 = ROOT / "brand" / "assets-v3"
LEGACY = ROOT / "brand" / "assets"

APPROVED = {
    "#0D1526",
    "#172036",
    "#D0BEB0",
    "#9E8B85",
    "#967878",
    "#7B96B2",
    "#D6B0A0",
}
FORBIDDEN_COLOR_HINTS = ("lavender", "purple", "electric blue", "neon blue")
REQUIRED = [
    "brand/assets-v3/README.md",
    "brand/assets-v3/00-reference/brand-board.svg",
    "brand/assets-v3/01-foundation/approved-palette.svg",
    "brand/assets-v3/02-ui/buttons-and-ctas.svg",
    "brand/assets-v3/02-ui/badges.svg",
    "brand/assets-v3/02-ui/ecommerce-controls.svg",
    "brand/assets-v3/03-icons/core-line-icons.svg",
    "brand/assets-v3/04-heroes/hero-smart-living-elevated.svg",
    "brand/assets-v3/04-heroes/hero-roi-guide.svg",
    "brand/assets-v3/05-ecommerce/product-card-template.svg",
    "brand/assets-v3/05-ecommerce/trust-bar.svg",
    "brand/assets-v3/06-stationery/letterhead.svg",
    "brand/assets-v3/06-stationery/invoice.svg",
    "brand/assets-v3/06-stationery/business-card-front.svg",
    "brand/assets-v3/06-stationery/business-card-back.svg",
    "brand/assets-v3/07-marketing/social-square.svg",
    "brand/assets-v3/07-marketing/email-header.svg",
    "brand/assets-v3/07-marketing/flyer.svg",
    "brand/assets-v3/08-docs/asset-manifest.json",
    "brand/assets-v3/08-docs/MIGRATION.md",
    "brand/assets/01-brand/luxsync-monogram-orb.png",
    "brand/assets/01-brand/luxsync-horizontal-lockup.png",
    "brand/assets/12-scenes/scene-manifest.csv",
    "content/about.md",
    "content/faqs.md",
    "docs/leadership/bridgette-beardsley.md",
    "docs/leadership/sheldon-bardol.md",
    "website/pages/about.md",
    "website/pages/faqs.md",
]

errors = []
for rel in REQUIRED:
    if not (ROOT / rel).exists():
        errors.append(f"missing required v3 asset: {rel}")

hex_re = re.compile(r"#[0-9A-Fa-f]{6}")
for path in V3.rglob("*.svg"):
    text = path.read_text(encoding="utf-8")
    colors = {c.upper() for c in hex_re.findall(text)}
    extra = colors - APPROVED
    if extra:
        errors.append(f"{path.relative_to(ROOT)}: unapproved colors {sorted(extra)}")
    if "font-family" in text:
        if "Manrope" not in text and "Inter" not in text:
            errors.append(f"{path.relative_to(ROOT)}: editable text is not Manrope/Inter")

manifest_path = V3 / "08-docs" / "asset-manifest.json"
if manifest_path.exists():
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("brand") != "LuxSync LLC":
        errors.append("v3 manifest brand must be LuxSync LLC")
    if manifest.get("slogan") != "Where Luxury Lives Intelligently":
        errors.append("v3 manifest slogan mismatch")

for rel in ["brand/README.md", "website/styles/design-system.md", "docs/master-catalog.md"]:
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing governing document: {rel}")
        continue
    text = path.read_text(encoding="utf-8")
    for token in ("LuxSync v3", "Manrope", "Inter", "Where Luxury Lives Intelligently", "#D6B0A0"):
        if token not in text:
            errors.append(f"{rel}: missing required v3 token {token!r}")

website_contract = {
    "docs/leadership/bridgette-beardsley.md": (
        "Co-Founder & Chief Technology and Strategy Officer",
        "Intelligent Calm",
    ),
    "docs/leadership/sheldon-bardol.md": (
        "Co-Founder & Chief Customer and Operations Officer",
        "Intelligent Calm",
    ),
    "content/about.md": (
        "Bridgette Beardsley",
        "Sheldon Bardol",
        "Luxury is confidence.",
    ),
    "content/faqs.md": (
        "Find My LuxSync Solution",
        "info@luxsync.net",
        "support@luxsync.net",
        "SmartThings",
    ),
    "website/pages/about.md": (
        "Co-Founder & Chief Technology and Strategy Officer",
        "Co-Founder & Chief Customer and Operations Officer",
    ),
    "website/pages/faqs.md": (
        "/guides/faqs",
        "content/faqs.md",
        "FAQPage",
    ),
}
for rel, tokens in website_contract.items():
    path = ROOT / rel
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    for token in tokens:
        if token not in text:
            errors.append(f"{rel}: missing website contract token {token!r}")

# Legacy generated graphic directories must be gone after migration.
for name in [
    "00-catalog", "02-icons-brand", "03-icons-website", "04-icons-social",
    "05-palette", "06-gradients", "07-components", "08-cards",
    "09-illustrations", "10-product-cards", "11-banners",
]:
    if (LEGACY / name).exists():
        errors.append(f"legacy generated directory still present: brand/assets/{name}")

if (LEGACY / "asset-manifest.csv").exists() or (LEGACY / "asset-manifest.json").exists():
    errors.append("legacy generated asset manifests still present")

# Keep business publication guardrail intact.
pricing = ROOT / "docs/decisions/DEC-005-senior-service-pricing.md"
if pricing.exists():
    text = pricing.read_text(encoding="utf-8")
    if "No senior-service price is currently approved for public display" not in text:
        errors.append("senior-service pricing publication guardrail is missing")

if errors:
    print("LuxSync v3 validation failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("LuxSync v3 validation passed.")

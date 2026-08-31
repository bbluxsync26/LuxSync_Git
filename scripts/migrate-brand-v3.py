#!/usr/bin/env python3
from pathlib import Path
import re
import shutil

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

# Convenience neutrals from drafting are normalized to Pale Driftwood.
REPLACEMENTS = {
    "#FFFFFF": "#D0BEB0",
    "#ffffff": "#D0BEB0",
    "#F7F5F3": "#D0BEB0",
    "#f7f5f3": "#D0BEB0",
}

for path in V3.rglob("*.svg"):
    text = path.read_text(encoding="utf-8")
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")

# Remove all generated legacy graphic groups. Keep only protected logo masters,
# curated text-free scene photography, and the compatibility README.
for name in [
    "00-catalog",
    "02-icons-brand",
    "03-icons-website",
    "04-icons-social",
    "05-palette",
    "06-gradients",
    "07-components",
    "08-cards",
    "09-illustrations",
    "10-product-cards",
    "11-banners",
]:
    target = LEGACY / name
    if target.exists():
        shutil.rmtree(target)

for name in ["asset-manifest.csv", "asset-manifest.json"]:
    target = LEGACY / name
    if target.exists():
        target.unlink()

# Remove generated derivatives in 01-brand while preserving the two approved PNG masters.
brand_dir = LEGACY / "01-brand"
if brand_dir.exists():
    keep = {"luxsync-monogram-orb.png", "luxsync-horizontal-lockup.png"}
    for path in brand_dir.iterdir():
        if path.is_file() and path.name not in keep:
            path.unlink()

# Hard palette validation for v3 vector assets.
hex_re = re.compile(r"#[0-9A-Fa-f]{6}")
errors = []
for path in V3.rglob("*.svg"):
    text = path.read_text(encoding="utf-8")
    found = {c.upper() for c in hex_re.findall(text)}
    unknown = sorted(found - APPROVED)
    if unknown:
        errors.append(f"{path.relative_to(ROOT)}: unapproved colors {unknown}")

if errors:
    raise SystemExit("\n".join(errors))

print("LuxSync v3 migration complete: palette normalized and legacy generated graphics removed.")

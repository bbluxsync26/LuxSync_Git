#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLOGAN = "Where Luxury Lives Intelligently"

for rel in ("website/navigation.md", "website/asset-map.md"):
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if SLOGAN not in text:
        text = text.rstrip() + f"\n\n**Official slogan:** {SLOGAN}\n"
        path.write_text(text, encoding="utf-8")

shop = ROOT / "website/pages/shop.md"
text = shop.read_text(encoding="utf-8")
text = text.replace("Do not use `brand/assets/06-product-cards/` as public commerce cards; those imported slices are reference-only.", "Do not use the imported product-card raster slices as public commerce cards; they are reference-only.")
shop.write_text(text, encoding="utf-8")

Path(__file__).unlink()
print("Production validation corrections applied.")

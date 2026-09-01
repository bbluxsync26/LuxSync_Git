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

# Normalize trailing whitespace so the production cutover satisfies git diff --check.
text_suffixes = {".md", ".txt", ".json", ".yml", ".yaml", ".py", ".js", ".mjs", ".css", ".html"}
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in text_suffixes:
        continue
    if any(part in {".git", "node_modules"} for part in path.parts):
        continue
    original = path.read_text(encoding="utf-8", errors="replace")
    normalized = "\n".join(line.rstrip() for line in original.splitlines()) + "\n"
    if normalized != original:
        path.write_text(normalized, encoding="utf-8")

Path(__file__).unlink()
print("Production validation corrections applied.")

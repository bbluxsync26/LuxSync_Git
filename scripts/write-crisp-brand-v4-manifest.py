#!/usr/bin/env python3
"""Write a deterministic inventory for the LuxSync Brand System 4.0 library."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "brand" / "brand-system-v4"


def main() -> None:
    files = [p.relative_to(BRAND).as_posix() for p in sorted(BRAND.rglob("*")) if p.is_file()]
    data = {
        "brand": "LuxSync LLC",
        "system": "Brand System 4.0",
        "slogan": "Where Luxury Lives Intelligently",
        "authoritative_board": "00-reference/LuxSync_Brand_Board.png",
        "protected_logos": [
            "01-logos/luxsync-monogram-approved.png",
            "01-logos/luxsync-horizontal-approved.png",
        ],
        "flat_palette": ["#0D1526", "#172036", "#D0BEB0", "#9E8B85", "#967878", "#7B96B2"],
        "metallic_treatment": "Champagne Rose Gold Metallic, derived only from approved warm palette colors",
        "fonts": {"display": "Manrope 500/600", "body_ui": "Inter 400/500"},
        "counts": {
            "svg": sum(p.endswith(".svg") for p in files),
            "png": sum(p.endswith(".png") for p in files),
            "webp": sum(p.endswith(".webp") for p in files),
            "other": sum(not p.endswith((".svg", ".png", ".webp")) for p in files),
        },
        "files": files,
    }
    out = BRAND / "asset-manifest.json"
    out.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)} with {len(files)} entries")


if __name__ == "__main__":
    main()

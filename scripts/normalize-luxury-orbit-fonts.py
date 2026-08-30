#!/usr/bin/env python3
"""Normalize generated LuxSync SVG typography to the authoritative Manrope/Inter system."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = ROOT / "brand" / "assets"

REPLACEMENTS = (
    ("Bodoni Moda,Bodoni MT,Didot,Georgia,serif", "Manrope,Arial,sans-serif"),
    ("Century Gothic,Montserrat,Arial,sans-serif", "Manrope,Arial,sans-serif"),
    ("Candara,Inter,Segoe UI,Arial,sans-serif", "Inter,Arial,sans-serif"),
    ("Century Gothic", "Manrope"),
    ("Candara", "Inter"),
    ("Bodoni Moda", "Manrope"),
    ("Bodoni MT", "Manrope"),
    ("Didot", "Manrope"),
    ("Georgia,serif", "Arial,sans-serif"),
)


def main() -> int:
    changed = 0
    for svg in sorted(ASSET_ROOT.rglob("*.svg")):
        text = svg.read_text(encoding="utf-8")
        normalized = text
        for old, new in REPLACEMENTS:
            normalized = normalized.replace(old, new)
        if normalized != text:
            svg.write_text(normalized, encoding="utf-8")
            changed += 1

    leftovers = []
    forbidden = ("Century Gothic", "Candara", "Bodoni Moda", "Bodoni MT", "Didot", "Georgia,serif")
    for svg in sorted(ASSET_ROOT.rglob("*.svg")):
        text = svg.read_text(encoding="utf-8")
        for token in forbidden:
            if token in text:
                leftovers.append(f"{svg.relative_to(ROOT)}: {token}")

    if leftovers:
        raise RuntimeError("Legacy font declarations remain:\n" + "\n".join(leftovers))

    print(f"Normalized typography in {changed} SVG files to Manrope/Inter")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

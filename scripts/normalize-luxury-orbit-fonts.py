#!/usr/bin/env python3
"""Normalize LuxSync generator/source typography to the authoritative Manrope/Inter system."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = ROOT / "brand" / "assets"
GENERATOR = ROOT / "scripts" / "generate-luxury-orbit-assets.py"

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
FORBIDDEN = tuple(old for old, _new in REPLACEMENTS[3:])


def normalize_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    normalized = text
    for old, new in REPLACEMENTS:
        normalized = normalized.replace(old, new)
    if normalized != text:
        path.write_text(normalized, encoding="utf-8")
        return True
    return False


def main() -> int:
    changed = 0

    # Keep the editable generator source aligned with the final asset standard.
    if GENERATOR.exists() and normalize_file(GENERATOR):
        changed += 1

    # Normalize every generated SVG before rasterization.
    for svg in sorted(ASSET_ROOT.rglob("*.svg")):
        if normalize_file(svg):
            changed += 1

    leftovers = []
    check_files = [GENERATOR] if GENERATOR.exists() else []
    check_files.extend(sorted(ASSET_ROOT.rglob("*.svg")))
    for path in check_files:
        text = path.read_text(encoding="utf-8")
        for token in FORBIDDEN:
            if token in text:
                leftovers.append(f"{path.relative_to(ROOT)}: {token}")

    if leftovers:
        raise RuntimeError("Legacy font declarations remain:\n" + "\n".join(leftovers))

    print(f"Normalized typography in {changed} source/SVG files to Manrope/Inter")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

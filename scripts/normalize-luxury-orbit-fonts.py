#!/usr/bin/env python3
"""Normalize Luxury Orbit outputs to the authoritative LuxSync brand system.

Authoritative typography:
- Manrope 500/600 for display and headings
- Inter 400/500 for body and UI

Authoritative Plush Drift v2.1 colors:
- Slate Navy #0D1526
- Dark Suede #172036
- Pale Driftwood #D0BEB0
- Warm Taupe Mauve #9E8B85
- Antique Rose Taupe #967878
- Dusty Steel #7B96B2
- Champagne Rose Gold Metallic #D6B0A0 (anchor)

Champagne Rose Gold Metallic uses the approved #D6B0A0 anchor with lighter
champagne and deeper copper/rose stops for metallic depth. Icy-blue orbit
treatments may use derived highlight/shadow tints from Dusty Steel.

Commerce rule:
- Category graphics must not invent prices, ratings, stock claims, or scarcity.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = ROOT / "brand" / "assets"
GENERATOR = ROOT / "scripts" / "generate-luxury-orbit-assets.py"

FONT_REPLACEMENTS = (
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

COLOR_REPLACEMENTS = (
    ("#0B1D3A", "#0D1526"),
    ("#172846", "#172036"),
    ("#F3ECE8", "#D0BEB0"),
    ("#A69A8E", "#9E8B85"),
    ("#E7B5B8", "#967878"),
    ("#A6B9CE", "#7B96B2"),
)

XML_TEXT_REPLACEMENTS = (
    ("Comfort & Lighting", "Comfort &amp; Lighting"),
    ("Energy & Control", "Energy &amp; Control"),
    ("Security & Access", "Security &amp; Access"),
)

FORBIDDEN_FONTS = (
    "Century Gothic",
    "Candara",
    "Bodoni Moda",
    "Bodoni MT",
    "Didot",
    "Georgia,serif",
)
FORBIDDEN_BASE_COLORS = tuple(old for old, _new in COLOR_REPLACEMENTS)


def normalize_text(text: str) -> str:
    normalized = text
    for old, new in FONT_REPLACEMENTS:
        normalized = normalized.replace(old, new)
    for old, new in COLOR_REPLACEMENTS:
        normalized = normalized.replace(old, new)
    for old, new in XML_TEXT_REPLACEMENTS:
        normalized = normalized.replace(old, new)

    normalized = normalized.replace('font-weight="700"', 'font-weight="600"')
    normalized = normalized.replace("font-weight='700'", "font-weight='600'")
    return normalized


def sanitize_category_card(text: str) -> str:
    """Remove invented commerce claims from generated category cards."""
    text = re.sub(
        r'<text x="90" y="790"[^>]*>.*?</text>',
        '<text x="90" y="790" font-family=\'Inter,Arial,sans-serif\' '
        'font-size="32" font-weight="500" fill="#D0BEB0">Curated collection</text>',
        text,
    )
    text = re.sub(
        r'<text x="90" y="850"[^>]*>.*?</text>',
        '<text x="90" y="850" font-family=\'Inter,Arial,sans-serif\' '
        'font-size="28" fill="#9E8B85">Compatibility-first selection</text>',
        text,
    )
    text = re.sub(
        r'<text x="400" y="980" text-anchor="middle"[^>]*>SHOP CATEGORY</text>',
        '<text x="400" y="980" text-anchor="middle" '
        'font-family=\'Inter,Arial,sans-serif\' font-size="32" font-weight="500" '
        'fill="#0D1526">SHOP CATEGORY</text>',
        text,
    )
    return text


def normalize_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    normalized = normalize_text(text)

    if path.parent.name == "10-product-cards" and path.suffix.lower() == ".svg":
        normalized = sanitize_category_card(normalized)

    if normalized != text:
        path.write_text(normalized, encoding="utf-8")
        return True
    return False


def main() -> int:
    changed = 0

    if GENERATOR.exists() and normalize_file(GENERATOR):
        changed += 1

    for svg in sorted(ASSET_ROOT.rglob("*.svg")):
        if normalize_file(svg):
            changed += 1

    leftovers: list[str] = []
    check_files = [GENERATOR] if GENERATOR.exists() else []
    check_files.extend(sorted(ASSET_ROOT.rglob("*.svg")))

    for path in check_files:
        text = path.read_text(encoding="utf-8")
        for token in FORBIDDEN_FONTS:
            if token in text:
                leftovers.append(f"{path.relative_to(ROOT)}: legacy font {token}")
        for token in FORBIDDEN_BASE_COLORS:
            if token in text:
                leftovers.append(f"{path.relative_to(ROOT)}: legacy base color {token}")
        if 'font-weight="700"' in text or "font-weight='700'" in text:
            leftovers.append(f"{path.relative_to(ROOT)}: Manrope 700 weight")

        if path.parent.name == "10-product-cards" and path.suffix.lower() == ".svg":
            if re.search(r'>\$\d', text):
                leftovers.append(f"{path.relative_to(ROOT)}: invented price")
            if "★★★★★" in text:
                leftovers.append(f"{path.relative_to(ROOT)}: invented rating")
            if re.search(r'>(?:Comfort|Energy|Security) & (?:Lighting|Control|Access)<', text):
                leftovers.append(f"{path.relative_to(ROOT)}: unescaped XML ampersand")

    if leftovers:
        raise RuntimeError("Brand normalization leftovers remain:\n" + "\n".join(leftovers))

    print(
        f"Normalized {changed} generator/SVG files to Manrope/Inter, "
        "the seven Plush Drift v2.1 colors, approved display weights, XML-safe text, "
        "and safe category copy"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

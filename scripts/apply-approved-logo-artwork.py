#!/usr/bin/env python3
"""Replace generated logo drawings with the protected approved LuxSync artwork.

The Luxury Orbit generator may create layout scaffolding, but any asset that displays
an LS brand mark must reference the approved monogram raster instead of re-drawing
letters/orbits with live SVG text and ellipses.

Champagne Rose Gold Metallic is an approved brand color anchored at #D6B0A0;
the ``m`` gradient below is its canonical metallic rendering.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "brand" / "assets"

DEFS = '''<defs>
  <linearGradient id="n" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#0D1526"/><stop offset="1" stop-color="#090E1B"/></linearGradient>
  <linearGradient id="m" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#FFF2EA"/><stop offset=".18" stop-color="#EAC8B9"/><stop offset=".42" stop-color="#D6B0A0"/><stop offset=".64" stop-color="#9C675C"/><stop offset=".82" stop-color="#F2D6C8"/><stop offset="1" stop-color="#7D4E49"/></linearGradient>
</defs>'''


def write(rel: str, text: str) -> None:
    path = ASSETS / rel
    path.write_text(text, encoding="utf-8")


def image(x: int, y: int, w: int, h: int) -> str:
    return f'<image href="../01-brand/luxsync-monogram-orb.png" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet"/>'


# Homepage hero: keep native Manrope/Inter copy, but use the exact approved LS artwork.
write(
    "11-banners/hero-technology-feels-like-home.svg",
    f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="700" viewBox="0 0 1600 700" role="img" aria-label="LuxSync Technology that feels like home hero">{DEFS}
<rect width="1600" height="700" rx="46" fill="url(#n)"/>
<path d="M690 560C930 320 1130 710 1590 330" fill="none" stroke="url(#m)" stroke-width="14" opacity=".42"/>
<path d="M760 610C980 390 1220 720 1600 410" fill="none" stroke="#D6B0A0" stroke-width="4" opacity=".35"/>
<text x="110" y="190" font-family="Manrope,Arial,sans-serif" font-size="82" fill="#D0BEB0">Technology that feels</text>
<text x="110" y="285" font-family="Manrope,Arial,sans-serif" font-size="82" fill="#D6B0A0">like home.</text>
<text x="115" y="360" font-family="Inter,Arial,sans-serif" font-size="33" fill="#7B96B2">Quiet intelligence. Beautifully integrated.</text>
{image(1050, 105, 400, 400)}
</svg>''',
)

# Primary launch hero also uses the exact approved mark.
write(
    "11-banners/hero-where-luxury-lives-intelligently.svg",
    f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="700" viewBox="0 0 1600 700" role="img" aria-label="LuxSync Smart Living Elevated hero">{DEFS}
<rect width="1600" height="700" rx="46" fill="url(#n)"/>
<path d="M690 560C930 320 1130 710 1590 330" fill="none" stroke="url(#m)" stroke-width="14" opacity=".42"/>
<path d="M760 610C980 390 1220 720 1600 410" fill="none" stroke="#D6B0A0" stroke-width="4" opacity=".35"/>
<text x="110" y="160" font-family="Manrope,Arial,sans-serif" font-size="88" font-weight="600" fill="#D6B0A0">Smart Living.</text>
<text x="110" y="258" font-family="Manrope,Arial,sans-serif" font-size="88" font-weight="600" fill="#D6B0A0">Elevated.</text>
<text x="115" y="330" font-family="Inter,Arial,sans-serif" font-size="33" fill="#D0BEB0">Luxury smart-home technology designed for modern living.</text>
<rect x="115" y="390" width="300" height="86" rx="26" fill="url(#m)"/>
<text x="265" y="446" text-anchor="middle" font-family="Manrope,Arial,sans-serif" font-size="27" fill="#0D1526">SHOP SMART HOME</text>
{image(1050, 95, 400, 400)}
</svg>''',
)

# Brand hero card: same protection rule.
write(
    "01-brand/luxsync-hero-card.svg",
    f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1200" viewBox="0 0 1200 1200" role="img" aria-label="LuxSync hero card">{DEFS}
<rect x="65" y="65" width="1070" height="1070" rx="88" fill="url(#n)" stroke="#D6B0A0" stroke-opacity=".3" stroke-width="3"/>
<image href="luxsync-monogram-orb.png" x="260" y="120" width="680" height="520" preserveAspectRatio="xMidYMid meet"/>
<text x="600" y="820" text-anchor="middle" font-family="Manrope,Arial,sans-serif" font-size="145" letter-spacing="18" fill="#D0BEB0">LUXSYNC</text>
<text x="600" y="900" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="38" fill="#967878">Where Luxury Lives Intelligently</text>
</svg>''',
)

print("Applied protected LuxSync logo artwork to logo-bearing generated assets.")

#!/usr/bin/env python3
"""Validate the authoritative LuxSync Brand System 4.0 library."""

from pathlib import Path
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "brand" / "brand-system-v4"
PALETTE = {"#0D1526", "#172036", "#D0BEB0", "#9E8B85", "#967878", "#7B96B2"}
REQUIRED = [
    "00-reference/LuxSync_Brand_Board.svg",
    "00-reference/LuxSync_Brand_Board.png",
    "01-logos/luxsync-monogram-approved.png",
    "01-logos/luxsync-horizontal-approved.png",
    "01-logos/logo-horizontal-llc.svg",
    "01-logos/favicon.ico",
    "03-ui/buttons-and-ctas.svg",
    "03-ui/forms-and-search.svg",
    "05-heroes/home-technology-feels-like-home.svg",
    "05-heroes/roi-guide.svg",
    "05-heroes/find-my-luxsync-solution.svg",
    "06-ecommerce/category-cards.svg",
    "06-ecommerce/product-card.svg",
    "07-stationery/business-card-front.svg",
    "07-stationery/letterhead.svg",
    "08-marketing/flyer.svg",
    "09-documentation/markdown-header.svg",
    "README.md",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (BRAND / rel).exists():
            errors.append(f"missing required asset: {rel}")

    pairs = 0
    for svg in BRAND.rglob("*.svg"):
        text = svg.read_text(encoding="utf-8")
        colors = {c.upper() for c in re.findall(r"#[0-9A-Fa-f]{6}", text)}
        extra = colors - PALETTE
        if extra:
            errors.append(f"{svg.relative_to(ROOT)} uses unapproved colors: {sorted(extra)}")
        if "font-family:Manrope" not in text or "font-family:Inter" not in text:
            errors.append(f"{svg.relative_to(ROOT)} missing Manrope/Inter declarations")
        for match in re.findall(r'(?:xlink:href|href)="([^"]+)"', text):
            if match.startswith(("data:", "#", "http:" ,"https:")):
                continue
            if not (svg.parent / match).resolve().exists():
                errors.append(f"{svg.relative_to(ROOT)} has broken image reference: {match}")
        png, webp = svg.with_suffix(".png"), svg.with_suffix(".webp")
        if not png.exists() or not webp.exists():
            errors.append(f"{svg.relative_to(ROOT)} missing PNG/WebP pair")
        else:
            pairs += 1

    logo_pairs = [
        (ROOT / "brand/assets/01-brand/luxsync-monogram-orb.png", BRAND / "01-logos/luxsync-monogram-approved.png"),
        (ROOT / "brand/assets/01-brand/luxsync-horizontal-lockup.png", BRAND / "01-logos/luxsync-horizontal-approved.png"),
    ]
    for original, approved in logo_pairs:
        if original.exists() and approved.exists() and digest(original) != digest(approved):
            errors.append(f"approved logo changed: {approved.relative_to(ROOT)}")

    if (ROOT / "brand/assets-v3").exists():
        errors.append("retired brand/assets-v3 still exists")

    marker = "<!-- LUXSYNC-BRAND-HEADER:START -->"
    for md in ROOT.rglob("*.md"):
        if ".git" not in md.parts and marker not in md.read_text(encoding="utf-8"):
            errors.append(f"Markdown is not branded: {md.relative_to(ROOT)}")

    if errors:
        print("LuxSync Brand System 4.0 validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("LuxSync Brand System 4.0 validation passed")
    print(f"- {pairs} SVG masters have PNG and WebP outputs")
    print("- exact approved logo artwork verified by SHA-256")
    print("- approved palette and Manrope/Inter declarations verified")
    print("- all Markdown documents carry approved LuxSync branding")
    return 0


if __name__ == "__main__":
    sys.exit(main())

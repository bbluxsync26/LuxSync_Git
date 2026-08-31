#!/usr/bin/env python3
"""Validate LuxSync source-of-truth consistency across docs, prompts, assets, and metadata."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = ROOT / "brand" / "assets"

OFFICIAL_SLOGAN = "Where Luxury Lives Intelligently"
HERO = "Smart Living. Elevated."
PRIMARY_CTA = "Shop Smart Home"
SECONDARY_CTA = "Get the ROI Guide"

BASE_COLOR_NAMES = {
    "Slate Navy": "#0D1526",
    "Dark Suede": "#172036",
    "Pale Driftwood": "#D0BEB0",
    "Warm Taupe Mauve": "#9E8B85",
    "Antique Rose Taupe": "#967878",
    "Dusty Steel": "#7B96B2",
    "Champagne Rose Gold Metallic": "#D6B0A0",
}
BASE_COLORS = set(BASE_COLOR_NAMES.values())
LEGACY_BASE_COLORS = {
    "#0B1D3A",
    "#172846",
    "#F3ECE8",
    "#A69A8E",
    "#E7B5B8",
    "#A6B9CE",
}
FORBIDDEN_GENERATED_FONTS = (
    "Century Gothic",
    "Candara",
    "Bodoni Moda",
    "Bodoni MT",
    "Didot",
    "Georgia,serif",
)

GOVERNING_FILES = [
    "brand/README.md",
    "brand/colors.md",
    "brand/typography.md",
    "website/styles/design-system.md",
    "website/pages/home.md",
    "docs/architecture/website-information-architecture.md",
    "docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md",
    "docs/runbooks/RB-008-Luxury-Orbit-Brand-Asset-Generation.md",
    "docs/runbooks/RB-009-Repository-Consistency-Validation.md",
    "docs/checklists/CL-001-Airo-First-Pass-Review.md",
    "prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md",
    "docs/master-catalog.md",
    "docs/project-runbook.md",
]

PALETTE_GOVERNING_FILES = [
    "README.md",
    "brand/README.md",
    "brand/colors.md",
    "brand/assets/README.md",
    "website/styles/design-system.md",
    "website/pages/home.md",
    "docs/architecture/website-information-architecture.md",
    "docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md",
    "docs/runbooks/RB-008-Luxury-Orbit-Brand-Asset-Generation.md",
    "docs/runbooks/RB-009-Repository-Consistency-Validation.md",
    "docs/checklists/CL-001-Airo-First-Pass-Review.md",
    "prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md",
    "docs/master-catalog.md",
    "docs/project-runbook.md",
]


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        raise RuntimeError(f"Missing governing file: {rel}")
    return path.read_text(encoding="utf-8")


def require(text: str, token: str, rel: str, errors: list[str]) -> None:
    if token not in text:
        errors.append(f"{rel}: missing required token {token!r}")


def svg_size(path: Path) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")[:2000]
    match = re.search(
        r'<svg[^>]*\bwidth="([0-9.]+)"[^>]*\bheight="([0-9.]+)"', text
    )
    if not match:
        raise RuntimeError(f"Missing explicit SVG dimensions: {path.relative_to(ROOT)}")
    return int(float(match.group(1))), int(float(match.group(2)))


def validate_governing_docs(errors: list[str]) -> None:
    for rel in GOVERNING_FILES:
        text = read(rel)
        require(text, "Manrope", rel, errors)
        require(text, "Inter", rel, errors)
        require(text, OFFICIAL_SLOGAN, rel, errors)

    for rel in (
        "website/pages/home.md",
        "docs/architecture/website-information-architecture.md",
        "docs/checklists/CL-001-Airo-First-Pass-Review.md",
        "prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md",
    ):
        text = read(rel)
        require(text, HERO, rel, errors)
        require(text, PRIMARY_CTA, rel, errors)
        require(text, SECONDARY_CTA, rel, errors)

    homepage = read("content/homepage.md")
    for token in (OFFICIAL_SLOGAN, HERO, PRIMARY_CTA, SECONDARY_CTA):
        require(homepage, token, "content/homepage.md", errors)

    src_readme = read("website/src/README.md")
    require(src_readme, "Placeholder", "website/src/README.md", errors)

    colors = read("brand/colors.md")
    for name, color in BASE_COLOR_NAMES.items():
        require(colors, name, "brand/colors.md", errors)
        require(colors, color, "brand/colors.md", errors)
    for color in LEGACY_BASE_COLORS:
        if color in colors:
            errors.append(f"brand/colors.md: legacy replacement base color remains: {color}")

    typography = read("brand/typography.md")
    require(typography, "Manrope", "brand/typography.md", errors)
    require(typography, "Inter", "brand/typography.md", errors)

    for rel in PALETTE_GOVERNING_FILES:
        text = read(rel)
        require(text, "Champagne Rose Gold Metallic", rel, errors)
        require(text, "#D6B0A0", rel, errors)


def validate_generator_and_svgs(errors: list[str]) -> None:
    generator = read("scripts/generate-luxury-orbit-assets.py")
    require(generator, "Manrope", "scripts/generate-luxury-orbit-assets.py", errors)
    require(generator, "Inter", "scripts/generate-luxury-orbit-assets.py", errors)

    for token in FORBIDDEN_GENERATED_FONTS:
        if token in generator:
            errors.append(f"scripts/generate-luxury-orbit-assets.py: forbidden generated font {token}")

    for color in LEGACY_BASE_COLORS:
        if color in generator:
            errors.append(f"scripts/generate-luxury-orbit-assets.py: legacy base color {color}")

    if "lavender-mist" in generator:
        errors.append("scripts/generate-luxury-orbit-assets.py: retired lavender-mist recipe remains")
    require(
        generator,
        "dusty-steel-mist",
        "scripts/generate-luxury-orbit-assets.py",
        errors,
    )

    svgs = [
        path
        for path in ASSET_ROOT.rglob("*.svg")
        if "00-catalog" not in path.parts and "12-scenes" not in path.parts
    ]
    if len(svgs) != 98:
        errors.append(f"brand/assets: expected 98 SVG masters; found {len(svgs)}")

    retired_assets = list(ASSET_ROOT.rglob("lavender-mist.*"))
    for path in retired_assets:
        errors.append(f"{path.relative_to(ROOT)}: retired lavender asset remains")

    palette_labels = {
        "slate-navy.svg": "SLATE NAVY",
        "dark-suede.svg": "DARK SUEDE",
        "pale-driftwood.svg": "PALE DRIFTWOOD",
        "warm-taupe-mauve.svg": "WARM TAUPE MAUVE",
        "antique-rose-taupe.svg": "ANTIQUE ROSE TAUPE",
        "dusty-steel.svg": "DUSTY STEEL",
        "champagne-rose-gold-metallic.svg": "CHAMPAGNE ROSE GOLD METALLIC",
    }
    for filename, label in palette_labels.items():
        rel = f"brand/assets/05-palette/{filename}"
        require(read(rel), label, rel, errors)

    palette_strip = read("brand/assets/05-palette/plush-drift-palette-strip.svg")
    for label in palette_labels.values():
        require(
            palette_strip,
            label,
            "brand/assets/05-palette/plush-drift-palette-strip.svg",
            errors,
        )

    for svg in svgs:
        text = svg.read_text(encoding="utf-8")
        if "<text" in text:
            for token in FORBIDDEN_GENERATED_FONTS:
                if token in text:
                    errors.append(f"{svg.relative_to(ROOT)}: forbidden editable font {token}")

    protected = {
        "01-brand/luxsync-monogram-orb.svg": "luxsync-monogram-orb.png",
        "01-brand/luxsync-horizontal-lockup.svg": "luxsync-horizontal-lockup.png",
    }
    for rel, raster in protected.items():
        text = read(f"brand/assets/{rel}")
        if raster not in text:
            errors.append(
                f"brand/assets/{rel}: protected exact logo wrapper no longer references {raster}"
            )


def validate_asset_metadata(errors: list[str]) -> None:
    data = json.loads((ASSET_ROOT / "asset-manifest.json").read_text(encoding="utf-8"))

    if data.get("brand_system") != "Plush Drift v2.1":
        errors.append("asset-manifest.json: brand_system must be Plush Drift v2.1")
    if data.get("web_visual_direction") != "Luxury Orbit":
        errors.append("asset-manifest.json: web_visual_direction must be Luxury Orbit")
    if data.get("official_slogan") != OFFICIAL_SLOGAN:
        errors.append("asset-manifest.json: official slogan mismatch")

    fonts = data.get("fonts", {})
    if fonts.get("headlines_display", {}).get("family") != "Manrope":
        errors.append("asset-manifest.json: display font must be Manrope")
    if fonts.get("body_ui", {}).get("family") != "Inter":
        errors.append("asset-manifest.json: body font must be Inter")

    palette = set(data.get("palette", {}).values())
    if palette != BASE_COLORS:
        errors.append(f"asset-manifest.json: base palette mismatch: {sorted(palette)}")

    metallic = data.get("palette_treatments", {}).get(
        "champagne_rose_gold_metallic", {}
    )
    if metallic.get("anchor") != "#D6B0A0":
        errors.append("asset-manifest.json: Champagne Rose Gold Metallic anchor mismatch")
    expected_metallic_stops = [
        "#FFF2EA",
        "#EAC8B9",
        "#D6B0A0",
        "#9C675C",
        "#F2D6C8",
        "#7D4E49",
    ]
    if metallic.get("gradient_stops") != expected_metallic_stops:
        errors.append("asset-manifest.json: Champagne Rose Gold Metallic gradient mismatch")

    inventory = data.get("inventory", {})
    if inventory.get("logical_asset_count") != 104:
        errors.append("asset-manifest.json: logical_asset_count must be 104")
    if inventory.get("svg_master_count") != 98:
        errors.append("asset-manifest.json: svg_master_count must be 98")
    if inventory.get("production_scene_count") != 6:
        errors.append("asset-manifest.json: production_scene_count must be 6")

    csv_path = ASSET_ROOT / "asset-manifest.csv"
    with csv_path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 98:
        errors.append(f"asset-manifest.csv: expected 98 rows; found {len(rows)}")
    row_names = {row.get("name", "") for row in rows}
    if "lavender-mist" in row_names:
        errors.append("asset-manifest.csv: retired lavender-mist row remains")
    if "dusty-steel-mist" not in row_names:
        errors.append("asset-manifest.csv: dusty-steel-mist row is missing")
    if "champagne-rose-gold-metallic" not in row_names:
        errors.append("asset-manifest.csv: Champagne Rose Gold Metallic swatch is missing")
    for row in rows:
        rel = row.get("svg", "")
        svg = ASSET_ROOT / rel
        if not svg.exists():
            errors.append(f"asset-manifest.csv: missing SVG {rel}")
            continue
        width, height = svg_size(svg)
        if row.get("width") != str(width) or row.get("height") != str(height):
            errors.append(
                f"asset-manifest.csv: dimensions stale for {rel}: "
                f"manifest={row.get('width')}x{row.get('height')} actual={width}x{height}"
            )

    scene_dir = ASSET_ROOT / "12-scenes"
    with (scene_dir / "scene-manifest.csv").open(newline="", encoding="utf-8-sig") as handle:
        scene_rows = list(csv.DictReader(handle))
    if len(scene_rows) != 6:
        errors.append(f"12-scenes/scene-manifest.csv: expected 6 rows; found {len(scene_rows)}")
    if len(list(scene_dir.glob("*.png"))) != 6:
        errors.append("12-scenes: expected 6 PNG scenes")
    if len(list(scene_dir.glob("*.webp"))) != 6:
        errors.append("12-scenes: expected 6 WebP scenes")

    catalog = read("brand/assets/00-catalog/LuxSync-Asset-Catalog.html")
    require(catalog, "Manrope", "brand/assets/00-catalog/LuxSync-Asset-Catalog.html", errors)
    require(catalog, "Inter", "brand/assets/00-catalog/LuxSync-Asset-Catalog.html", errors)
    require(catalog, "104 logical assets", "brand/assets/00-catalog/LuxSync-Asset-Catalog.html", errors)
    require(catalog, "Champagne Rose Gold Metallic", "brand/assets/00-catalog/LuxSync-Asset-Catalog.html", errors)
    for token in ("Century Gothic", "Candara"):
        if token in catalog:
            errors.append(
                f"brand/assets/00-catalog/LuxSync-Asset-Catalog.html: legacy font remains: {token}"
            )

    svg_list = read("brand/assets/00-catalog/SVG-ASSET-LIST.md")
    if "lavender-mist" in svg_list or "lavender-mist" in catalog:
        errors.append("asset catalogs: retired lavender-mist reference remains")
    require(svg_list, "dusty-steel-mist", "brand/assets/00-catalog/SVG-ASSET-LIST.md", errors)
    require(catalog, "dusty-steel-mist", "brand/assets/00-catalog/LuxSync-Asset-Catalog.html", errors)


def validate_business_guardrails(errors: list[str]) -> None:
    plan = read("docs/business-plan.md")
    if "Pricing status: unresolved" not in plan:
        errors.append(
            "docs/business-plan.md: senior-service pricing must be explicitly marked unresolved"
        )
    if "approximately $28,590/month" not in plan:
        errors.append(
            "docs/business-plan.md: founder transition threshold must reflect corrected Phase 2 math"
        )

    pricing = read("docs/decisions/DEC-005-senior-service-pricing.md")
    require(pricing, "Open / Decision Required", "docs/decisions/DEC-005-senior-service-pricing.md", errors)
    require(pricing, "No senior-service price is currently approved for public display", "docs/decisions/DEC-005-senior-service-pricing.md", errors)

    value = read("docs/value-proposition.md")
    for segment in (
        "Short-Term Rental",
        "Seniors",
        "Smart Office",
        "Intentional Parents",
        "Busy Professionals",
    ):
        if segment not in value:
            errors.append(f"docs/value-proposition.md: missing approved segment {segment}")
    if "Smart Sleep Nursery" not in value:
        errors.append(
            "docs/value-proposition.md: standard bundle name Smart Sleep Nursery missing"
        )


def main() -> int:
    errors: list[str] = []
    validate_governing_docs(errors)
    validate_generator_and_svgs(errors)
    validate_asset_metadata(errors)
    validate_business_guardrails(errors)

    if errors:
        print("LuxSync repository consistency validation FAILED:\n")
        for item in errors:
            print(f"- {item}")
        return 1

    print("LuxSync repository consistency validation PASSED.")
    print("- seven-color Plush Drift v2.1 palette confirmed")
    print("- Luxury Orbit web treatment confirmed")
    print("- Manrope/Inter typography confirmed")
    print("- official palette names and no lavender-mist artifact confirmed")
    print("- website hero/CTA contract confirmed")
    print("- asset metadata/dimensions/catalog confirmed")
    print("- protected exact logos confirmed")
    print("- business guardrails and open pricing decision confirmed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

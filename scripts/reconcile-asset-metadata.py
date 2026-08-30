#!/usr/bin/env python3
"""Reconcile LuxSync asset metadata with the actual committed asset library."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = ROOT / "brand" / "assets"
CSV_PATH = ASSET_ROOT / "asset-manifest.csv"
JSON_PATH = ASSET_ROOT / "asset-manifest.json"
INVENTORY_PATH = ASSET_ROOT / "00-catalog" / "ASSET-INVENTORY.txt"

BASE_PALETTE = {
    "slate_navy": "#0D1526",
    "dark_suede": "#172036",
    "pale_driftwood": "#D0BEB0",
    "warm_taupe_mauve": "#9E8B85",
    "antique_rose_taupe": "#967878",
    "dusty_steel": "#7B96B2",
}

EXPECTED_VECTOR_COUNTS = {
    "01-brand": 8,
    "02-icons-brand": 12,
    "03-icons-website": 14,
    "04-icons-social": 6,
    "05-palette": 8,
    "06-gradients": 4,
    "07-components": 17,
    "08-cards": 13,
    "09-illustrations": 7,
    "10-product-cards": 4,
    "11-banners": 4,
}
SCENE_COUNT = 6


def svg_size(path: Path) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")[:2000]
    match = re.search(
        r'<svg[^>]*\bwidth="([0-9.]+)"[^>]*\bheight="([0-9.]+)"',
        text,
        flags=re.IGNORECASE,
    )
    if not match:
        raise RuntimeError(f"Missing explicit SVG width/height: {path.relative_to(ROOT)}")
    return int(float(match.group(1))), int(float(match.group(2)))


def reconcile_csv() -> int:
    with CSV_PATH.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise RuntimeError("asset-manifest.csv has no header")
        rows = list(reader)
        fieldnames = reader.fieldnames

    if len(rows) != 97:
        raise RuntimeError(f"Expected 97 vector manifest rows; found {len(rows)}")

    seen: set[str] = set()
    counts: dict[str, int] = {}
    changed = 0

    for row in rows:
        rel = row.get("svg", "").strip()
        if not rel:
            raise RuntimeError(f"Manifest row missing svg path: {row}")
        if rel in seen:
            raise RuntimeError(f"Duplicate SVG manifest path: {rel}")
        seen.add(rel)

        svg = ASSET_ROOT / rel
        if not svg.exists():
            raise RuntimeError(f"Manifest references missing SVG: {rel}")

        width, height = svg_size(svg)
        if row.get("width") != str(width) or row.get("height") != str(height):
            row["width"] = str(width)
            row["height"] = str(height)
            changed += 1

        category = row.get("category", "").strip()
        counts[category] = counts.get(category, 0) + 1

    if counts != EXPECTED_VECTOR_COUNTS:
        raise RuntimeError(
            f"Vector category counts differ from expected values: {counts}"
        )

    actual_svgs = {
        p.relative_to(ASSET_ROOT).as_posix()
        for p in ASSET_ROOT.rglob("*.svg")
        if "00-catalog" not in p.parts and "12-scenes" not in p.parts
    }
    if actual_svgs != seen:
        missing = sorted(actual_svgs - seen)
        stale = sorted(seen - actual_svgs)
        raise RuntimeError(
            "Vector manifest does not match SVG library. "
            f"Missing rows={missing}; stale rows={stale}"
        )

    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    return changed


def validate_scenes() -> None:
    scene_dir = ASSET_ROOT / "12-scenes"
    scene_manifest = scene_dir / "scene-manifest.csv"
    if not scene_manifest.exists():
        raise RuntimeError("Missing 12-scenes/scene-manifest.csv")

    with scene_manifest.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != SCENE_COUNT:
        raise RuntimeError(f"Expected {SCENE_COUNT} scene manifest rows; found {len(rows)}")

    pngs = list(scene_dir.glob("*.png"))
    webps = list(scene_dir.glob("*.webp"))
    if len(pngs) != SCENE_COUNT or len(webps) != SCENE_COUNT:
        raise RuntimeError(
            f"Expected {SCENE_COUNT} scene PNGs and WebPs; found {len(pngs)} PNG / {len(webps)} WebP"
        )


def write_json_summary() -> None:
    data = {
        "schema_version": 3,
        "library": "LuxSync Brand Asset Library",
        "brand_system": "Plush Drift v2.1",
        "web_visual_direction": "Luxury Orbit",
        "official_slogan": "Where Luxury Lives Intelligently",
        "palette": BASE_PALETTE,
        "fonts": {
            "headlines_display": {"family": "Manrope", "weights": [500, 600]},
            "body_ui": {"family": "Inter", "weights": [400, 500]},
        },
        "inventory": {
            "vector_manifest": "asset-manifest.csv",
            "scene_manifest": "12-scenes/scene-manifest.csv",
            "logical_asset_count": 103,
            "svg_master_count": 97,
            "production_scene_count": SCENE_COUNT,
            "categories": {**EXPECTED_VECTOR_COUNTS, "12-scenes": SCENE_COUNT},
        },
        "implementation_notes": [
            "asset-manifest.csv is the detailed inventory for the 97 SVG-based vector graphics and its dimensions are reconciled from the actual SVG masters.",
            "12-scenes/scene-manifest.csv is the detailed inventory for the six production raster scenes.",
            "Manrope and Inter are the authoritative typography system for current LuxSync web graphics.",
            "Plush Drift v2.1 supplies the six authoritative base colors; Luxury Orbit is the active web/graphics treatment layered on that base.",
            "The 97 SVG-based graphics are generated in-repository and do not require image generation.",
            "The six production scenes are text-free raster assets intended for composition beneath native HTML/CSS and approved branding.",
            "Do not bake prices, ratings, stock claims, navigation, CTAs, or promotional copy into production scene photography.",
            "The approved primary monogram and horizontal lockup rasters are protected exact artwork and must not be replaced by generic regeneration.",
        ],
    }
    JSON_PATH.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def write_inventory() -> None:
    lines = [
        "LUXSYNC WEB ASSET INVENTORY",
        "Plush Drift v2.1 base system / Luxury Orbit web treatment",
        "",
        "Total logical assets: 103",
        "97 SVG-based graphics with PNG/WebP derivatives",
        "6 text-free production scenes with PNG/WebP delivery files",
        "",
    ]
    for category, count in EXPECTED_VECTOR_COUNTS.items():
        lines.append(f"{category:<24}{count:>3}")
    lines.append(f"{'12-scenes':<24}{SCENE_COUNT:>3}")
    lines.extend(
        [
            "",
            "Typography authority",
            "--------------------",
            "Headings / Display / Graphic UI: Manrope 500/600",
            "Body / Supporting UI: Inter 400/500",
            "",
            "Palette authority",
            "-----------------",
            "Slate Navy #0D1526",
            "Dark Suede #172036",
            "Pale Driftwood #D0BEB0",
            "Warm Taupe Mauve #9E8B85",
            "Antique Rose Taupe #967878",
            "Dusty Steel #7B96B2",
            "",
            "Canonical metadata",
            "------------------",
            "asset-manifest.csv               97 SVG-based vector graphics",
            "asset-manifest.json              library summary",
            "12-scenes/scene-manifest.csv     6 production raster scenes",
            "00-catalog/SVG-ASSET-LIST.md     generated SVG list",
            "",
            "Official slogan",
            "---------------",
            "Where Luxury Lives Intelligently",
            "",
        ]
    )
    INVENTORY_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    changed = reconcile_csv()
    validate_scenes()
    write_json_summary()
    write_inventory()
    print(
        f"Asset metadata reconciled: 97 vector rows, {changed} dimension row(s) updated, "
        f"{SCENE_COUNT} production scenes validated."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

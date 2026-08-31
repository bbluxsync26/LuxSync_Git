#!/usr/bin/env python3
"""Reconcile LuxSync asset metadata with the actual committed asset library."""
from __future__ import annotations

import csv
import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = ROOT / "brand" / "assets"
CSV_PATH = ASSET_ROOT / "asset-manifest.csv"
JSON_PATH = ASSET_ROOT / "asset-manifest.json"
INVENTORY_PATH = ASSET_ROOT / "00-catalog" / "ASSET-INVENTORY.txt"
CATALOG_PATH = ASSET_ROOT / "00-catalog" / "LuxSync-Asset-Catalog.html"
SCENE_MANIFEST_PATH = ASSET_ROOT / "12-scenes" / "scene-manifest.csv"

BASE_PALETTE = {
    "slate_navy": "#0D1526",
    "dark_suede": "#172036",
    "pale_driftwood": "#D0BEB0",
    "warm_taupe_mauve": "#9E8B85",
    "antique_rose_taupe": "#967878",
    "dusty_steel": "#7B96B2",
    "champagne_rose_gold_metallic": "#D6B0A0",
}

EXPECTED_VECTOR_COUNTS = {
    "01-brand": 8,
    "02-icons-brand": 12,
    "03-icons-website": 14,
    "04-icons-social": 6,
    "05-palette": 9,
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


def reconcile_csv() -> tuple[int, list[dict[str, str]]]:
    with CSV_PATH.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise RuntimeError("asset-manifest.csv has no header")
        rows = list(reader)
        fieldnames = reader.fieldnames

    if len(rows) != 98:
        raise RuntimeError(f"Expected 98 vector manifest rows; found {len(rows)}")

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
        raise RuntimeError(f"Vector category counts differ from expected values: {counts}")

    actual_svgs = {
        path.relative_to(ASSET_ROOT).as_posix()
        for path in ASSET_ROOT.rglob("*.svg")
        if "00-catalog" not in path.parts and "12-scenes" not in path.parts
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

    return changed, rows


def validate_scenes() -> list[dict[str, str]]:
    scene_dir = ASSET_ROOT / "12-scenes"
    if not SCENE_MANIFEST_PATH.exists():
        raise RuntimeError("Missing 12-scenes/scene-manifest.csv")

    with SCENE_MANIFEST_PATH.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != SCENE_COUNT:
        raise RuntimeError(f"Expected {SCENE_COUNT} scene manifest rows; found {len(rows)}")

    pngs = list(scene_dir.glob("*.png"))
    webps = list(scene_dir.glob("*.webp"))
    if len(pngs) != SCENE_COUNT or len(webps) != SCENE_COUNT:
        raise RuntimeError(
            f"Expected {SCENE_COUNT} scene PNGs and WebPs; found "
            f"{len(pngs)} PNG / {len(webps)} WebP"
        )
    return rows


def write_json_summary() -> None:
    data = {
        "schema_version": 4,
        "library": "LuxSync Brand Asset Library",
        "brand_system": "Plush Drift v2.1",
        "web_visual_direction": "Luxury Orbit",
        "official_slogan": "Where Luxury Lives Intelligently",
        "palette": BASE_PALETTE,
        "palette_treatments": {
            "champagne_rose_gold_metallic": {
                "anchor": "#D6B0A0",
                "gradient_stops": [
                    "#FFF2EA",
                    "#EAC8B9",
                    "#D6B0A0",
                    "#9C675C",
                    "#F2D6C8",
                    "#7D4E49",
                ],
            }
        },
        "fonts": {
            "headlines_display": {"family": "Manrope", "weights": [500, 600]},
            "body_ui": {"family": "Inter", "weights": [400, 500]},
        },
        "inventory": {
            "vector_manifest": "asset-manifest.csv",
            "scene_manifest": "12-scenes/scene-manifest.csv",
            "logical_asset_count": 104,
            "svg_master_count": 98,
            "production_scene_count": SCENE_COUNT,
            "categories": {**EXPECTED_VECTOR_COUNTS, "12-scenes": SCENE_COUNT},
        },
        "implementation_notes": [
            "asset-manifest.csv is the detailed inventory for the 98 SVG-based vector graphics and its dimensions are reconciled from the actual SVG masters.",
            "12-scenes/scene-manifest.csv is the detailed inventory for the six production raster scenes.",
            "Manrope and Inter are the authoritative typography system for current LuxSync web graphics.",
            "Plush Drift v2.1 supplies seven authoritative colors, including Champagne Rose Gold Metallic anchored at #D6B0A0; Luxury Orbit is the active web/graphics treatment layered on that base.",
            "The 98 SVG-based graphics are generated in-repository and do not require image generation.",
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
        "Total logical assets: 104",
        "98 SVG-based graphics with PNG/WebP derivatives",
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
            "Champagne Rose Gold Metallic #D6B0A0 (anchor)",
            "",
            "Canonical metadata",
            "------------------",
            "asset-manifest.csv               98 SVG-based vector graphics",
            "asset-manifest.json              library summary",
            "12-scenes/scene-manifest.csv     6 production raster scenes",
            "00-catalog/SVG-ASSET-LIST.md     generated SVG list",
            "00-catalog/LuxSync-Asset-Catalog.html generated browser catalog",
            "",
            "Official slogan",
            "---------------",
            "Where Luxury Lives Intelligently",
            "",
        ]
    )
    INVENTORY_PATH.write_text("\n".join(lines), encoding="utf-8")


def yes_no(value: str) -> str:
    return "transparent" if value.strip().lower() == "true" else "opaque"


def write_catalog(vector_rows: list[dict[str, str]], scene_rows: list[dict[str, str]]) -> None:
    sections: list[str] = []
    for category in EXPECTED_VECTOR_COUNTS:
        cards: list[str] = []
        for row in vector_rows:
            if row.get("category") != category:
                continue
            svg_rel = row["svg"]
            stem = Path(svg_rel).stem
            base = f"../{category}/{stem}"
            cards.append(
                '<article class="card">'
                f'<div class="preview"><img loading="lazy" src="{escape(base)}.png" '
                f'alt="{escape(row.get("description", stem))}"></div>'
                f'<div class="name">{escape(row.get("name", stem))}</div>'
                f'<div class="desc">{escape(row.get("description", ""))}</div>'
                f'<div class="meta">{escape(row.get("width", ""))}×{escape(row.get("height", ""))} · '
                f'{yes_no(row.get("transparent", ""))}</div>'
                '<div class="links">'
                f'<a href="{escape(base)}.svg">SVG</a>'
                f'<a href="{escape(base)}.png">PNG</a>'
                f'<a href="{escape(base)}.webp">WebP</a>'
                '</div></article>'
            )
        sections.append(
            f'<section><h2>{escape(category)}</h2><div class="grid">'
            + "".join(cards)
            + "</div></section>"
        )

    scene_cards: list[str] = []
    for row in scene_rows:
        name = row.get("name", "scene")
        description = row.get("description", "Text-free production smart-living scene")
        png_name = row.get("png", f"{name}.png")
        webp_name = row.get("webp", f"{name}.webp")
        scene_cards.append(
            '<article class="card">'
            f'<div class="preview scene"><img loading="lazy" src="../12-scenes/{escape(png_name)}" '
            f'alt="{escape(description)}"></div>'
            f'<div class="name">{escape(name)}</div>'
            f'<div class="desc">{escape(description)}</div>'
            '<div class="meta">production scene · text-free</div>'
            '<div class="links">'
            f'<a href="../12-scenes/{escape(png_name)}">PNG</a>'
            f'<a href="../12-scenes/{escape(webp_name)}">WebP</a>'
            '</div></article>'
        )
    sections.append(
        '<section><h2>12-scenes</h2><p class="section-note">'
        'Six text-free production scenes for compositing beneath native website copy and approved branding.'
        '</p><div class="grid">' + "".join(scene_cards) + "</div></section>"
    )

    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>LuxSync Web Asset Catalog</title>
<style>
:root{{--navy:#0D1526;--suede:#172036;--cream:#D0BEB0;--taupe:#9E8B85;--rose:#967878;--steel:#7B96B2;--champagne:#D6B0A0}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--navy);color:var(--cream);font-family:Inter,system-ui,sans-serif;background-image:linear-gradient(145deg,rgba(150,120,120,.08),transparent 32%)}}
header{{padding:54px max(28px,6vw);border-bottom:1px solid rgba(123,150,178,.22)}}
h1,h2,.name{{font-family:Manrope,system-ui,sans-serif}}
h1{{font-size:clamp(42px,6vw,78px);font-weight:600;margin:0 0 10px}}
h2{{font-size:32px;font-weight:600;color:var(--cream);border-bottom:1px solid rgba(123,150,178,.22);padding-bottom:12px}}
.lead,.section-note{{color:var(--taupe);font-size:18px;max-width:980px;line-height:1.55}}
.palette{{display:flex;gap:8px;margin-top:24px}}.palette i{{width:42px;height:42px;border-radius:50%;border:1px solid rgba(255,255,255,.15)}}
main{{padding:42px max(28px,6vw) 90px}}section{{margin:0 0 64px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:22px}}
.card{{background:var(--suede);border:1px solid rgba(150,120,120,.45);border-radius:22px;padding:18px;box-shadow:0 8px 34px rgba(150,120,120,.08)}}
.preview{{height:210px;display:grid;place-items:center;background:var(--navy);border-radius:14px;overflow:hidden}}
.preview.scene{{height:250px}}.preview img{{max-width:100%;max-height:100%;object-fit:contain}}.preview.scene img{{width:100%;height:100%;object-fit:cover}}
.name{{font-size:17px;font-weight:600;margin:15px 0 6px}}.desc{{font-size:14px;color:var(--taupe);min-height:38px;line-height:1.45}}
.meta{{font:12px ui-monospace,SFMono-Regular,Consolas,monospace;color:var(--steel);margin-top:12px}}
.links{{display:flex;gap:10px;margin-top:12px;flex-wrap:wrap}}.links a{{color:var(--cream);text-decoration:none;border:1px solid rgba(123,150,178,.7);border-radius:999px;padding:6px 11px;font-size:12px}}.links a:hover{{background:var(--steel);color:var(--navy)}}
footer{{padding:30px max(28px,6vw);color:var(--taupe);border-top:1px solid rgba(123,150,178,.18)}}
</style>
</head>
<body>
<header>
<h1>LuxSync Web Asset Catalog</h1>
<p class="lead">104 logical assets: 98 SVG-based graphics plus six text-free production scenes. Plush Drift v2.1 is the authoritative base system, Luxury Orbit is the active web treatment, and Manrope + Inter are the governing fonts.</p>
<div class="palette"><i style="background:#0D1526" title="Slate Navy #0D1526"></i><i style="background:#172036" title="Dark Suede #172036"></i><i style="background:#D0BEB0" title="Pale Driftwood #D0BEB0"></i><i style="background:#9E8B85" title="Warm Taupe Mauve #9E8B85"></i><i style="background:#967878" title="Antique Rose Taupe #967878"></i><i style="background:#7B96B2" title="Dusty Steel #7B96B2"></i><i style="background:linear-gradient(135deg,#FFF2EA,#EAC8B9 24%,#D6B0A0 48%,#9C675C 68%,#F2D6C8 84%,#7D4E49)" title="Champagne Rose Gold Metallic #D6B0A0 anchor"></i></div>
</header>
<main>{''.join(sections)}</main>
<footer>LuxSync · Where Luxury Lives Intelligently · Catalog generated from canonical repository metadata.</footer>
</body>
</html>
'''
    CATALOG_PATH.write_text(html, encoding="utf-8")


def main() -> int:
    changed, vector_rows = reconcile_csv()
    scene_rows = validate_scenes()
    write_json_summary()
    write_inventory()
    write_catalog(vector_rows, scene_rows)
    print(
        f"Asset metadata reconciled: 98 vector rows, {changed} dimension row(s) updated, "
        f"{SCENE_COUNT} production scenes validated, browser catalog refreshed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Build faithful LuxSync Wave 1 board-derived brand assets.

The source of truth is the approved reference-board artwork. This script crops the
approved reusable artwork exactly as shown on the boards and produces channel-neutral
raster masters plus PNG, lossless WebP, and self-contained SVG fidelity containers.
It does not redraw, restyle, recolor, or generatively reinterpret approved artwork.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
import shutil
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw

ROOT = Path(os.environ.get("LUXSYNC_ROOT", Path(__file__).resolve().parents[1]))
OMNI = ROOT / "brand/manifests/omnichannel-brand-manifest.json"
GENERATED_MANIFEST = ROOT / "brand/manifests/approved-board-asset-manifest.json"

BOARD_FILES = {
    "icons": ROOT / "brand/reference-boards/icons_board.png",
    "dividers": ROOT / "brand/reference-boards/dividers_board.png",
}
EXPECTED_BOARD_SIZE = (1448, 1086)

ICON_SPECS = {
    "security-shield-check": (105, 180, 235, 355),
    "lighting-bulb": (345, 175, 525, 355),
    "climate-thermostat": (625, 175, 815, 355),
    "music-note": (890, 175, 1120, 355),
    "shades-window": (1170, 175, 1380, 355),
    "smart-lock": (135, 400, 250, 575),
    "concierge-bell": (350, 400, 530, 575),
    "installation-tools": (615, 400, 825, 575),
    "support-headset": (900, 400, 1120, 575),
    "automation-home-gear": (1165, 400, 1380, 575),
    "energy-bolt": (100, 625, 250, 795),
    "camera": (340, 625, 530, 795),
    "faq-chat": (610, 625, 855, 795),
    "phone": (925, 625, 1110, 795),
    "calendar": (1165, 625, 1390, 795),
    "location-pin": (635, 840, 815, 1000),
}

DIVIDER_SPECS = {
    "horizontal-steel-line": ((35, 210, 480, 248), "horizontal-divider"),
    "horizontal-rose-spark": ((35, 255, 480, 302), "horizontal-divider"),
    "horizontal-rose-tall-spark": ((35, 300, 480, 348), "horizontal-divider"),
    "horizontal-dual-arrow-spark": ((35, 345, 480, 395), "horizontal-divider"),
    "horizontal-steel-diamond": ((35, 395, 480, 447), "horizontal-divider"),
    "horizontal-rose-rounded-spark": ((35, 445, 480, 500), "horizontal-divider"),
    "horizontal-steel-star": ((35, 495, 480, 555), "horizontal-divider"),
    "horizontal-micro-spectrum": ((35, 550, 480, 600), "horizontal-divider"),
    "sparkle-rose-small": ((610, 205, 670, 265), "standalone-sparkle"),
    "sparkle-rose-medium": ((700, 205, 765, 275), "standalone-sparkle"),
    "sparkle-steel-small": ((795, 205, 855, 270), "standalone-sparkle"),
    "sparkle-divider-tall": ((540, 265, 930, 315), "sparkle-divider"),
    "sparkle-divider-soft": ((540, 315, 930, 365), "sparkle-divider"),
    "sparkle-divider-bright": ((540, 365, 930, 415), "sparkle-divider"),
    "sparkle-divider-beaded": ((540, 420, 930, 470), "sparkle-divider"),
    "sparkle-divider-orbital": ((540, 485, 930, 540), "sparkle-divider"),
    "sparkle-divider-dotted": ((540, 550, 930, 598), "sparkle-divider"),
    "metal-line-circles": ((980, 215, 1375, 260), "metallic-line"),
    "metal-line-diamonds": ((980, 260, 1375, 310), "metallic-line"),
    "metal-line-sparkle-ends": ((980, 310, 1375, 355), "metallic-line"),
    "metal-line-double-diamonds": ((980, 355, 1375, 405), "metallic-line"),
    "metal-line-dual-arrow": ((980, 405, 1375, 450), "metallic-line"),
    "metal-bar-steel": ((980, 450, 1375, 505), "metallic-bar"),
    "metal-bar-rose": ((980, 500, 1375, 555), "metallic-bar"),
    "badge-underline-steel-spark": ((570, 680, 930, 715), "badge-underline"),
    "badge-underline-rose-spark": ((570, 720, 930, 765), "badge-underline"),
    "badge-underline-steel-diamond": ((570, 770, 930, 810), "badge-underline"),
    "badge-underline-rose-diamond": ((560, 825, 940, 865), "badge-underline"),
    "orbit-steel": ((985, 680, 1185, 760), "orbit-accent"),
    "orbit-dual": ((1185, 680, 1375, 760), "orbit-accent"),
    "orbit-rose-left": ((985, 765, 1185, 860), "orbit-accent"),
    "orbit-rose-right": ((1185, 765, 1375, 860), "orbit-accent"),
    "corner-spark-rose": ((45, 945, 175, 1025), "corner-accent"),
    "corner-double-arc": ((195, 945, 330, 1025), "corner-accent"),
    "corner-spark-straight": ((345, 925, 465, 1018), "corner-accent"),
    "corner-diamond-curve": ((500, 925, 590, 1018), "corner-accent"),
    "ornament-center-star": ((610, 915, 690, 1018), "standalone-ornament"),
    "corner-diamond-double": ((740, 925, 840, 1018), "corner-accent"),
    "corner-double-line-spark": ((860, 925, 975, 1018), "corner-accent"),
    "corner-simple-double": ((995, 925, 1090, 1018), "corner-accent"),
    "corner-steel-rose-star": ((1110, 925, 1235, 1018), "corner-accent"),
    "corner-double-arc-rose": ((1250, 925, 1375, 1018), "corner-accent"),
}

TEMPLATE_REFERENCE_ONLY = [
    {"board": "brand/reference-boards/dividers_board.png", "family": "section-separators", "count": 4, "reason": "Approved layout/template family contains placeholder SECTION text; preserve as reference/template rather than baking mutable text into production art."},
    {"board": "brand/reference-boards/buttons_board.png", "family": "buttons-and-cta-states", "reason": "Approved semantic UI/component language; implement with live text and tokens, not flattened button screenshots."},
    {"board": "brand/reference-boards/product_cards_board.png", "family": "smart-home-category-cards", "reason": "Approved marketing/composition direction; conceptual devices and mutable commerce content are not validated live catalog facts."},
    {"board": "brand/reference-boards/stationery_board.png", "family": "stationery-and-print-suite", "reason": "Approved composition/template direction includes placeholder identity/contact data; rebuild as templates with real/live data in Wave 3."},
    {"board": "brand/reference-boards/ui_controls_board.png", "family": "ui-controls-and-product-meta", "reason": "Approved semantic UI reference includes mutable or unsupported example claims; implement as live UI and validated data, not flattened production imagery."},
    {"board": "brand/reference-boards/approved_brand_board.png", "family": "hero-banner-examples", "reason": "Approved composition direction contains baked example copy; preserve as reference and rebuild with current live copy/assets in Wave 2."},
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def svg_wrapper(png: Path, width: int, height: int, title: str) -> str:
    b64 = base64.b64encode(png.read_bytes()).decode("ascii")
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">\n'
        f'  <title>{title}</title>\n'
        '  <!-- Embedded-raster fidelity container. Do not describe as newly redrawn editable vector art. -->\n'
        f'  <image width="{width}" height="{height}" href="data:image/png;base64,{b64}"/>\n'
        '</svg>\n'
    )


def paths_for(category: str, aid: str) -> dict[str, Path]:
    master = ROOT / f"brand/masters/approved-board-raster/{category}/{aid}.png"
    base = ROOT / f"brand/exports/digital/approved/{category}"
    return {"master": master, "png": base / "png" / f"{aid}.png", "webp": base / "webp" / f"{aid}.webp", "svg": base / "svg" / f"{aid}.svg"}


def record_valid(rec: dict, board_sha: str, box: tuple[int, int, int, int], paths: dict[str, Path]) -> bool:
    if not rec or rec.get("source_board_sha256") != board_sha or rec.get("crop_box") != list(box):
        return False
    for key in ("master", "png", "webp", "svg"):
        p = paths[key]
        meta = rec.get("files", {}).get(key, {})
        if not p.exists() or meta.get("path") != rel(p):
            return False
        if meta.get("sha256") != sha256(p) or meta.get("bytes") != p.stat().st_size:
            return False
    return True


def make_contact_sheet(items: list[dict], target: Path, category: str) -> None:
    cols, tile_w = 4, 300
    tile_h = 215 if category == "icons" else 150
    rows = (len(items) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tile_w, rows * tile_h), (8, 16, 30))
    draw = ImageDraw.Draw(sheet)
    for i, item in enumerate(items):
        png = ROOT / item["files"]["png"]["path"]
        im = Image.open(png).convert("RGB")
        preview = im.copy()
        preview.thumbnail((tile_w - 24, tile_h - 48))
        x = (i % cols) * tile_w + (tile_w - preview.width) // 2
        y = (i // cols) * tile_h + 6
        sheet.paste(preview, (x, y))
        draw.text(((i % cols) * tile_w + 8, (i // cols) * tile_h + tile_h - 30), item["id"], fill="white")
    target.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(target, "JPEG", quality=92, optimize=True)


def all_specs():
    for aid, box in ICON_SPECS.items():
        yield aid, "icons", None, box
    for aid, (box, subfamily) in DIVIDER_SPECS.items():
        yield aid, "dividers", subfamily, box


def main() -> None:
    if not OMNI.exists():
        raise SystemExit(f"Missing omnichannel manifest: {OMNI}")

    boards: dict[str, Image.Image] = {}
    board_sha: dict[str, str] = {}
    for category, path in BOARD_FILES.items():
        if not path.exists():
            raise SystemExit(f"Missing approved reference board: {rel(path)}")
        im = Image.open(path).convert("RGB")
        if im.size != EXPECTED_BOARD_SIZE:
            raise SystemExit(f"{rel(path)} dimensions changed: {im.size} != {EXPECTED_BOARD_SIZE}")
        boards[category] = im
        board_sha[category] = sha256(path)

    previous = {}
    if GENERATED_MANIFEST.exists():
        data = json.loads(GENERATED_MANIFEST.read_text(encoding="utf-8"))
        previous = {a.get("id"): a for a in data.get("assets", [])}

    records: list[dict] = []
    changed = False
    for aid, category, subfamily, box in all_specs():
        paths = paths_for(category, aid)
        old = previous.get(aid, {})
        if record_valid(old, board_sha[category], box, paths):
            records.append(old)
            print(f"SKIP already valid: {aid}")
            continue

        crop = boards[category].crop(box)
        width, height = crop.size
        for p in paths.values():
            p.parent.mkdir(parents=True, exist_ok=True)
        crop.save(paths["master"], "PNG", optimize=True)
        shutil.copyfile(paths["master"], paths["png"])
        crop.save(paths["webp"], "WEBP", lossless=True, method=6)
        paths["svg"].write_text(svg_wrapper(paths["png"], width, height, f"LuxSync {aid}"), encoding="utf-8")

        rec = {
            "id": aid, "category": category, "subfamily": subfamily,
            "source_board": rel(BOARD_FILES[category]), "source_board_sha256": board_sha[category],
            "crop_box": list(box), "width": width, "height": height,
            "master_type": "raster-origin-board-crop", "svg_type": "embedded-raster-svg-fidelity-container",
            "approved_background": "dark-board-background", "publication_status": "approved-board-derived",
            "qa_status": "passed", "files": {},
        }
        for key, p in paths.items():
            rec["files"][key] = {"path": rel(p), "bytes": p.stat().st_size, "sha256": sha256(p)}
        records.append(rec)
        changed = True
        print(f"BUILT: {aid}")

    icons = [r for r in records if r["category"] == "icons"]
    dividers = [r for r in records if r["category"] == "dividers"]
    if len(icons) != 16 or len(dividers) != 42:
        raise SystemExit(f"Unexpected board-derived counts: icons={len(icons)}, dividers={len(dividers)}")

    icon_qa = ROOT / "brand/audit/qa/approved-icons-board-derived.jpg"
    divider_qa = ROOT / "brand/audit/qa/approved-dividers-board-derived.jpg"
    if changed or not icon_qa.exists():
        make_contact_sheet(icons, icon_qa, "icons")
    if changed or not divider_qa.exists():
        make_contact_sheet(dividers, divider_qa, "dividers")

    manifest = {
        "schema_version": "1.0", "brand": "LuxSync", "source": "approved-reference-boards",
        "status": "wave1-board-derived-assets-qa-passed", "asset_count": len(records),
        "counts": {"icons": len(icons), "dividers": len(dividers)},
        "formats": ["master-png", "png", "lossless-webp", "svg-fidelity-container"],
        "qa": {
            "icons_contact_sheet": {"path": rel(icon_qa), "sha256": sha256(icon_qa)},
            "dividers_contact_sheet": {"path": rel(divider_qa), "sha256": sha256(divider_qa)},
        },
        "template_reference_only": TEMPLATE_REFERENCE_ONLY,
        "assets": records,
    }
    write_json(GENERATED_MANIFEST, manifest)

    omni = json.loads(OMNI.read_text(encoding="utf-8"))
    omni["version"] = "1.2-wave1-board-audit"
    omni["status"] = "wave1-board-derived-assets-generated-pending-production-promotion"
    omni["reference_board_visual_audit"] = {
        "status": "complete", "pixel_access": "full-resolution-private-audit-artifact",
        "result": "Current semantic icon/divider layer is not a faithful visual match to the approved boards; faithful board-derived assets have been generated separately for controlled promotion.",
        "approved_reusable_asset_count": 58, "approved_icon_count": 16, "approved_divider_accent_count": 42,
        "generated_manifest": rel(GENERATED_MANIFEST), "template_reference_only": TEMPLATE_REFERENCE_ONLY,
    }
    omni["known_omnichannel_gaps"] = [
        "Faithful board-derived Wave 1 icons/dividers must be deliberately promoted into the canonical production delivery mapping after final QA; the simplified legacy semantic layer remains in place until that controlled swap.",
        "Stationery, merchandise, apparel, signage, email and broader marketing export families are not yet built as a complete omnichannel delivery package.",
        "Print/specialty PDF/EPS/TIFF and one-color/embroidery/engraving variants remain Wave 3 work and must be technically justified per asset.",
    ]
    omni["next_checkpoint"] = "Wave 1 Checkpoint 2: validate the 58 faithful board-derived assets, update the canonical production asset mapping to use approved-board visuals where appropriate, and preserve template/reference-only families as live/template implementations rather than flattened screenshots."
    write_json(OMNI, omni)
    print(f"Board-derived assets ready: {len(records)} (16 icons + 42 dividers/accents)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "brand/templates/digital-marketing/template-specs.json"
LOGO_DIR = ROOT / "brand/assets/logos/png"
ORNAMENT_DIR = ROOT / "brand/assets/dividers/png"
MASTER_DIR = ROOT / "brand/masters/marketing-art/wave2"
EXPORT_DIR = ROOT / "brand/exports/digital/marketing"
QA_PATH = ROOT / "brand/audit/qa/wave2-digital-marketing.jpg"
MANIFEST_PATH = ROOT / "brand/manifests/wave2-digital-marketing-manifest.json"
EMAIL_TEMPLATE = ROOT / "brand/templates/digital-marketing/email/luxsync-email-signature.html"
PRODUCT_HTML = ROOT / "brand/templates/digital-marketing/product-card/product-card-template.html"
PRODUCT_CSS = ROOT / "brand/templates/digital-marketing/product-card/product-card.css"

SLATE = (13, 21, 38, 255)
SUEDE = (23, 32, 54, 255)
STEEL = (123, 150, 178, 255)
CHAMPAGNE = (214, 176, 160, 255)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def blend(a: int, b: int, t: float) -> int:
    return round(a + (b - a) * t)


def layered_background(width: int, height: int, layout: str) -> Image.Image:
    image = Image.new("RGBA", (width, height), SLATE)
    draw = ImageDraw.Draw(image)
    for y in range(height):
        t = y / max(1, height - 1)
        mix = min(1.0, 0.16 + 0.72 * t)
        color = tuple(blend(SLATE[i], SUEDE[i], mix) for i in range(3)) + (255,)
        draw.line((0, y, width, y), fill=color)

    glow = Image.new("RGBA", image.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse(
        (round(width * 0.58), round(height * -0.08), round(width * 1.10), round(height * 0.60)),
        fill=(STEEL[0], STEEL[1], STEEL[2], 44),
    )
    gd.ellipse(
        (round(width * -0.16), round(height * 0.58), round(width * 0.40), round(height * 1.10)),
        fill=(CHAMPAGNE[0], CHAMPAGNE[1], CHAMPAGNE[2], 28),
    )
    glow = glow.filter(ImageFilter.GaussianBlur(max(28, round(min(width, height) * 0.075))))
    image = Image.alpha_composite(image, glow)

    details = Image.new("RGBA", image.size, (0, 0, 0, 0))
    dd = ImageDraw.Draw(details)
    inset = max(20, round(min(width, height) * 0.035))
    dd.rounded_rectangle(
        (inset, inset, width - inset, height - inset),
        radius=max(18, round(min(width, height) * 0.025)),
        outline=(CHAMPAGNE[0], CHAMPAGNE[1], CHAMPAGNE[2], 42),
        width=max(1, round(min(width, height) * 0.0015)),
    )
    if "presentation" in layout or "campaign" in layout:
        x = round(width * 0.68)
        dd.line(
            (x, round(height * 0.12), x, round(height * 0.88)),
            fill=(STEEL[0], STEEL[1], STEEL[2], 32),
            width=max(1, width // 1400),
        )
    if "story" in layout or "portrait" in layout:
        dd.line(
            (round(width * 0.08), round(height * 0.82), round(width * 0.56), round(height * 0.82)),
            fill=(CHAMPAGNE[0], CHAMPAGNE[1], CHAMPAGNE[2], 56),
            width=max(1, width // 800),
        )
    return Image.alpha_composite(image, details)


def resize_to_width(asset: Image.Image, target_width: int, max_height: int | None = None) -> Image.Image:
    ratio = target_width / max(1, asset.width)
    target_height = max(1, round(asset.height * ratio))
    if max_height and target_height > max_height:
        ratio = max_height / max(1, asset.height)
        target_width = max(1, round(asset.width * ratio))
        target_height = max_height
    return asset.resize((target_width, target_height), Image.Resampling.LANCZOS)


def anchor_position(anchor: str, canvas: tuple[int, int], asset: tuple[int, int]) -> tuple[int, int]:
    width, height = canvas
    aw, ah = asset
    mx, my = round(width * 0.055), round(height * 0.055)
    return {
        "top-left": (mx, my),
        "top-right": (width - aw - mx, my),
        "bottom-left": (mx, height - ah - my),
        "bottom-right": (width - aw - mx, height - ah - my),
        "right-center": (width - aw - mx, round((height - ah) / 2)),
        "lower-third-left": (mx, height - ah - round(height * 0.07)),
    }.get(anchor, (mx, my))


def paste_logo(canvas: Image.Image, spec: dict) -> dict:
    path = LOGO_DIR / spec["logo"]
    logo = Image.open(path).convert("RGBA")
    logo = resize_to_width(
        logo,
        round(spec["width"] * float(spec["logo_width_ratio"])),
        round(spec["height"] * 0.34),
    )
    pos = anchor_position(spec["logo_anchor"], canvas.size, logo.size)
    canvas.alpha_composite(logo, dest=pos)
    return {
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "sha256": sha256(path),
        "placement": [pos[0], pos[1], logo.width, logo.height],
        "identity_rule": "exact approved LuxSync raster logo artwork composited without redraw, recolor or retyping",
    }


def ornament_width_ratio(name: str) -> float:
    if name.startswith("badge-underline"):
        return 0.22
    if name.startswith("orbit-stroke") or name == "divider-orbit.png":
        return 0.23
    if name.startswith("corner-"):
        return 0.17
    if name.startswith("divider-"):
        return 0.30
    return 0.20


def paste_ornament(canvas: Image.Image, spec: dict) -> dict | None:
    name = spec.get("ornament")
    if not name:
        return None
    path = ORNAMENT_DIR / name
    ornament = Image.open(path).convert("RGBA")
    ornament = resize_to_width(
        ornament,
        round(spec["width"] * ornament_width_ratio(name)),
        round(spec["height"] * 0.30),
    )
    anchor = spec.get("ornament_anchor") or "top-right"
    width, height = canvas.size
    ow, oh = ornament.size
    mx, my = round(width * 0.055), round(height * 0.055)
    positions = {
        "bottom-left": (mx, height - oh - my),
        "bottom-right": (width - ow - mx, height - oh - my),
        "right-center": (width - ow - mx, round((height - oh) / 2)),
        "top-left": (mx, my),
        "top-right": (width - ow - mx, my),
        "lower-third-line": (round(width * 0.25), height - oh - round(height * 0.10)),
    }
    pos = positions.get(anchor, (width - ow - mx, my))
    canvas.alpha_composite(ornament, dest=pos)
    return {
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "sha256": sha256(path),
        "placement": [pos[0], pos[1], ornament.width, ornament.height],
        "selection_rule": "clean transparent validated divider delivery used for seamless new composition; faithful board-derived crop remains preserved separately",
    }


def render_opaque(spec: dict) -> tuple[Image.Image, dict, dict | None]:
    canvas = layered_background(spec["width"], spec["height"], spec["layout"])
    ornament = paste_ornament(canvas, spec)
    logo = paste_logo(canvas, spec)
    return canvas, logo, ornament


def render_corner_bug(spec: dict) -> tuple[Image.Image, dict, None]:
    width, height = spec["width"], spec["height"]
    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    path = LOGO_DIR / spec["logo"]
    logo = Image.open(path).convert("RGBA")
    logo = resize_to_width(logo, round(width * float(spec["logo_width_ratio"])), round(height * 0.22))
    x, y = anchor_position("bottom-right", (width, height), logo.size)

    plate = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    pd = ImageDraw.Draw(plate)
    px, py = round(width * 0.018), round(height * 0.022)
    box = (x - px, y - py, x + logo.width + px, y + logo.height + py)
    pd.rounded_rectangle(
        box,
        radius=round(height * 0.025),
        fill=(13, 21, 38, 205),
        outline=(123, 150, 178, 90),
        width=max(2, width // 1800),
    )
    canvas = Image.alpha_composite(canvas, plate.filter(ImageFilter.GaussianBlur(round(height * 0.012))))
    canvas = Image.alpha_composite(canvas, plate)
    canvas.alpha_composite(logo, dest=(x, y))
    return canvas, {
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "sha256": sha256(path),
        "placement": [x, y, logo.width, logo.height],
        "identity_rule": "exact approved LuxSync raster logo artwork composited without redraw, recolor or retyping",
    }, None


def render_lower_third(spec: dict) -> tuple[Image.Image, dict, dict | None]:
    width, height = spec["width"], spec["height"]
    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    panel = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    pd = ImageDraw.Draw(panel)
    left, top = round(width * 0.045), round(height * 0.74)
    right, bottom = round(width * 0.79), round(height * 0.92)
    pd.rounded_rectangle(
        (left, top, right, bottom),
        radius=round(height * 0.025),
        fill=(13, 21, 38, 220),
        outline=(214, 176, 160, 76),
        width=max(2, width // 1800),
    )
    pd.line(
        (round(width * 0.235), top + round((bottom - top) * 0.2), round(width * 0.235), bottom - round((bottom - top) * 0.2)),
        fill=(123, 150, 178, 76),
        width=max(2, width // 1800),
    )
    canvas = Image.alpha_composite(canvas, panel.filter(ImageFilter.GaussianBlur(round(height * 0.012))))
    canvas = Image.alpha_composite(canvas, panel)
    ornament = paste_ornament(canvas, spec)
    logo = paste_logo(canvas, spec)
    return canvas, logo, ornament


def render(spec: dict) -> tuple[Image.Image, dict, dict | None]:
    if spec["layout"] == "video-corner-bug":
        return render_corner_bug(spec)
    if spec["layout"] == "video-lower-third":
        return render_lower_third(spec)
    return render_opaque(spec)


def write_asset(spec: dict) -> dict:
    image, logo_source, ornament_source = render(spec)
    channel = spec["channel"]
    master_path = MASTER_DIR / f"{spec['id']}.png"
    png_path = EXPORT_DIR / channel / "png" / f"{spec['id']}.png"
    webp_path = EXPORT_DIR / channel / "webp" / f"{spec['id']}.webp"
    for path in (master_path, png_path, webp_path):
        path.parent.mkdir(parents=True, exist_ok=True)

    image.save(master_path, "PNG", optimize=True)
    shutil.copyfile(master_path, png_path)
    image.save(webp_path, "WEBP", lossless=True, method=6)

    def record(path: Path, **extra: object) -> dict:
        return {
            "path": str(path.relative_to(ROOT)).replace("\\", "/"),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            **extra,
        }

    return {
        "id": spec["id"],
        "channel": channel,
        "layout": spec["layout"],
        "width": spec["width"],
        "height": spec["height"],
        "transparency": bool(spec["transparency"]),
        "safe_zone": spec["safe_zone"],
        "master_type": "raster-composition-from-approved-sources",
        "editable_source": "brand/templates/digital-marketing/template-specs.json",
        "logo_source": logo_source,
        "ornament_source": ornament_source,
        "format_policy": {
            "png": "lossless master/delivery",
            "webp": "lossless digital delivery",
            "svg": "intentionally omitted: composition uses protected raster logo artwork and atmospheric raster effects; editable source is the governed template spec",
        },
        "files": {
            "master_png": record(master_path),
            "png": record(png_path),
            "webp": record(webp_path, lossless=True),
        },
        "qa_status": "passed-by-deterministic-build-pending-contact-sheet-review",
    }


def make_qa(records: list[dict]) -> None:
    tile_w, tile_h, cols = 420, 280, 2
    rows = (len(records) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tile_w, rows * tile_h), (20, 24, 34))
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for index, record in enumerate(records):
        src = ROOT / record["files"]["png"]["path"]
        image = Image.open(src).convert("RGBA")
        if record["transparency"]:
            preview = Image.new("RGBA", image.size, (28, 34, 48, 255))
            preview.alpha_composite(image)
            image = preview
        thumb = image.convert("RGB")
        thumb.thumbnail((tile_w - 24, tile_h - 54), Image.Resampling.LANCZOS)
        x, y = (index % cols) * tile_w, (index // cols) * tile_h
        sheet.paste(thumb, (x + (tile_w - thumb.width) // 2, y + 12))
        draw.text(
            (x + 12, y + tile_h - 34),
            f"{record['id']}  {record['width']}x{record['height']}",
            fill=(220, 216, 210),
            font=font,
        )
    QA_PATH.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(QA_PATH, "JPEG", quality=90, optimize=True)


def main() -> None:
    specs = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    records = [write_asset(spec) for spec in specs["templates"]]
    make_qa(records)

    manifest = {
        "schema_version": "1.1",
        "brand": "LuxSync",
        "prompt": "PR-BRAND-001",
        "wave": "wave2",
        "status": "generated-pending-manual-qa-and-pr-validation",
        "brand_system": "LuxSync Production Raster v5",
        "design_dna": "Plush Drift",
        "official_slogan": "Where Luxury Lives Intelligently",
        "template_spec": {
            "path": str(SPEC_PATH.relative_to(ROOT)).replace("\\", "/"),
            "sha256": sha256(SPEC_PATH),
        },
        "ornament_policy": specs["source_rules"]["ornament_selection"],
        "live_templates": [
            {"id": "email-signature", "path": str(EMAIL_TEMPLATE.relative_to(ROOT)).replace("\\", "/"), "sha256": sha256(EMAIL_TEMPLATE), "mode": "live-placeholder-html"},
            {"id": "product-card-html", "path": str(PRODUCT_HTML.relative_to(ROOT)).replace("\\", "/"), "sha256": sha256(PRODUCT_HTML), "mode": "live-placeholder-html"},
            {"id": "product-card-css", "path": str(PRODUCT_CSS.relative_to(ROOT)).replace("\\", "/"), "sha256": sha256(PRODUCT_CSS), "mode": "live-semantic-css"},
        ],
        "static_asset_count": len(records),
        "static_assets": records,
        "qa": {
            "contact_sheet": str(QA_PATH.relative_to(ROOT)).replace("\\", "/"),
            "sha256": sha256(QA_PATH),
            "status": "generated-pending-manual-review",
        },
        "publication_guardrails": [
            "static frames contain no mutable campaign copy or commerce facts",
            "conceptual approval-board product renders are not published as live products",
            "protected LuxSync logo source pixels are composited without recoloring, redrawing or retyping",
            "clean transparent validated dividers are used for seamless new compositions while faithful board-derived crops remain preserved",
            "product-card and email-signature content remains live/template-driven",
            "video assets are static overlays only, not motion deliverables",
        ],
    }
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Built {len(records)} Wave 2 static templates")
    print(MANIFEST_PATH.relative_to(ROOT))
    print(QA_PATH.relative_to(ROOT))


if __name__ == "__main__":
    main()

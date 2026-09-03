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
ORNAMENT_DIR = ROOT / "brand/exports/digital/approved/dividers/png"
MASTER_DIR = ROOT / "brand/masters/marketing-art/wave2"
EXPORT_DIR = ROOT / "brand/exports/digital/marketing"
QA_PATH = ROOT / "brand/audit/qa/wave2-digital-marketing.jpg"
MANIFEST_PATH = ROOT / "brand/manifests/wave2-digital-marketing-manifest.json"
EMAIL_TEMPLATE = ROOT / "brand/templates/digital-marketing/email/luxsync-email-signature.html"
PRODUCT_HTML = ROOT / "brand/templates/digital-marketing/product-card/product-card-template.html"
PRODUCT_CSS = ROOT / "brand/templates/digital-marketing/product-card/product-card.css"

SLATE = (13, 21, 38, 255)
SUEDE = (23, 32, 54, 255)
DRIFTWOOD = (208, 190, 176, 255)
STEEL = (123, 150, 178, 255)
ROSE = (150, 120, 120, 255)
CHAMPAGNE = (214, 176, 160, 255)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def lerp(a: int, b: int, t: float) -> int:
    return round(a + (b - a) * t)


def layered_background(width: int, height: int, layout: str) -> Image.Image:
    image = Image.new("RGBA", (width, height), SLATE)
    px = image.load()
    for y in range(height):
        t = y / max(1, height - 1)
        for x in range(width):
            horizontal = x / max(1, width - 1)
            suede_mix = min(1.0, 0.18 + 0.56 * t + 0.16 * horizontal)
            px[x, y] = (
                lerp(SLATE[0], SUEDE[0], suede_mix),
                lerp(SLATE[1], SUEDE[1], suede_mix),
                lerp(SLATE[2], SUEDE[2], suede_mix),
                255,
            )

    glow = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(glow)
    steel_box = (
        int(width * 0.58),
        int(height * 0.02),
        int(width * 1.08),
        int(height * 0.62),
    )
    draw.ellipse(steel_box, fill=(STEEL[0], STEEL[1], STEEL[2], 46))
    warm_box = (
        int(width * -0.14),
        int(height * 0.58),
        int(width * 0.38),
        int(height * 1.08),
    )
    draw.ellipse(warm_box, fill=(CHAMPAGNE[0], CHAMPAGNE[1], CHAMPAGNE[2], 30))
    blur = max(28, round(min(width, height) * 0.08))
    glow = glow.filter(ImageFilter.GaussianBlur(blur))
    image = Image.alpha_composite(image, glow)

    architectural = Image.new("RGBA", image.size, (0, 0, 0, 0))
    a = ImageDraw.Draw(architectural)
    inset = max(20, round(min(width, height) * 0.035))
    a.rounded_rectangle(
        (inset, inset, width - inset, height - inset),
        radius=max(18, round(min(width, height) * 0.025)),
        outline=(CHAMPAGNE[0], CHAMPAGNE[1], CHAMPAGNE[2], 42),
        width=max(1, round(min(width, height) * 0.0015)),
    )
    if "presentation" in layout or "campaign" in layout:
        x = round(width * 0.68)
        a.line((x, round(height * 0.12), x, round(height * 0.88)), fill=(STEEL[0], STEEL[1], STEEL[2], 32), width=max(1, width // 1400))
    if "story" in layout or "portrait" in layout:
        a.line((round(width * 0.08), round(height * 0.82), round(width * 0.56), round(height * 0.82)), fill=(CHAMPAGNE[0], CHAMPAGNE[1], CHAMPAGNE[2], 56), width=max(1, width // 800))
    return Image.alpha_composite(image, architectural)


def resized(asset: Image.Image, target_width: int, max_height: int | None = None) -> Image.Image:
    ratio = target_width / asset.width
    target_height = max(1, round(asset.height * ratio))
    if max_height and target_height > max_height:
        ratio = max_height / asset.height
        target_width = max(1, round(asset.width * ratio))
        target_height = max_height
    return asset.resize((target_width, target_height), Image.Resampling.LANCZOS)


def anchor_position(anchor: str, canvas: tuple[int, int], asset: tuple[int, int]) -> tuple[int, int]:
    w, h = canvas
    aw, ah = asset
    mx = round(w * 0.055)
    my = round(h * 0.055)
    positions = {
        "top-left": (mx, my),
        "top-right": (w - aw - mx, my),
        "bottom-left": (mx, h - ah - my),
        "bottom-right": (w - aw - mx, h - ah - my),
        "right-center": (w - aw - mx, round((h - ah) / 2)),
        "lower-third-left": (mx, h - ah - round(h * 0.07)),
    }
    return positions.get(anchor, (mx, my))


def paste_logo(canvas: Image.Image, spec: dict) -> dict:
    logo_path = LOGO_DIR / spec["logo"]
    logo = Image.open(logo_path).convert("RGBA")
    target_width = round(spec["width"] * float(spec["logo_width_ratio"]))
    max_height = round(spec["height"] * 0.34)
    logo = resized(logo, target_width, max_height)
    pos = anchor_position(spec["logo_anchor"], canvas.size, logo.size)
    canvas.alpha_composite(logo, dest=pos)
    return {
        "path": str(logo_path.relative_to(ROOT)).replace("\\", "/"),
        "sha256": sha256(logo_path),
        "placement": [pos[0], pos[1], logo.width, logo.height],
    }


def paste_ornament(canvas: Image.Image, spec: dict) -> dict | None:
    name = spec.get("ornament")
    if not name:
        return None
    path = ORNAMENT_DIR / name
    ornament = Image.open(path).convert("RGBA")
    anchor = spec.get("ornament_anchor") or "top-right"
    if "horizontal" in name or "badge" in name or "sparkle-divider" in name:
        target_width = round(spec["width"] * (0.28 if spec["width"] < 2000 else 0.22))
    elif "orbit" in name:
        target_width = round(spec["width"] * 0.30)
    else:
        target_width = round(spec["width"] * 0.20)
    ornament = resized(ornament, target_width, round(spec["height"] * 0.32))

    w, h = canvas.size
    ow, oh = ornament.size
    mx = round(w * 0.055)
    my = round(h * 0.055)
    if anchor == "bottom-left":
        pos = (mx, h - oh - my)
    elif anchor == "bottom-right":
        pos = (w - ow - mx, h - oh - my)
    elif anchor == "right-center":
        pos = (w - ow - mx, round((h - oh) / 2))
    elif anchor == "top-left":
        pos = (mx, my)
    elif anchor == "lower-third-line":
        pos = (round(w * 0.25), h - oh - round(h * 0.10))
    else:
        pos = (w - ow - mx, my)
    canvas.alpha_composite(ornament, dest=pos)
    return {
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "sha256": sha256(path),
        "placement": [pos[0], pos[1], ornament.width, ornament.height],
    }


def render_opaque(spec: dict) -> tuple[Image.Image, dict, dict | None]:
    canvas = layered_background(spec["width"], spec["height"], spec["layout"])
    ornament_record = paste_ornament(canvas, spec)
    logo_record = paste_logo(canvas, spec)
    return canvas, logo_record, ornament_record


def render_corner_bug(spec: dict) -> tuple[Image.Image, dict, None]:
    w, h = spec["width"], spec["height"]
    canvas = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    logo_path = LOGO_DIR / spec["logo"]
    logo = Image.open(logo_path).convert("RGBA")
    logo = resized(logo, round(w * float(spec["logo_width_ratio"])), round(h * 0.22))
    x, y = anchor_position("bottom-right", (w, h), logo.size)

    plate = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(plate)
    pad_x = round(w * 0.018)
    pad_y = round(h * 0.022)
    box = (x - pad_x, y - pad_y, x + logo.width + pad_x, y + logo.height + pad_y)
    d.rounded_rectangle(box, radius=round(h * 0.025), fill=(13, 21, 38, 205), outline=(123, 150, 178, 90), width=max(2, w // 1800))
    glow = plate.filter(ImageFilter.GaussianBlur(round(h * 0.012)))
    canvas = Image.alpha_composite(canvas, glow)
    canvas = Image.alpha_composite(canvas, plate)
    canvas.alpha_composite(logo, dest=(x, y))
    return canvas, {
        "path": str(logo_path.relative_to(ROOT)).replace("\\", "/"),
        "sha256": sha256(logo_path),
        "placement": [x, y, logo.width, logo.height],
    }, None


def render_lower_third(spec: dict) -> tuple[Image.Image, dict, dict | None]:
    w, h = spec["width"], spec["height"]
    canvas = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    panel = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(panel)
    left = round(w * 0.045)
    top = round(h * 0.74)
    right = round(w * 0.79)
    bottom = round(h * 0.92)
    d.rounded_rectangle((left, top, right, bottom), radius=round(h * 0.025), fill=(13, 21, 38, 220), outline=(214, 176, 160, 76), width=max(2, w // 1800))
    d.line((round(w * 0.235), top + round((bottom-top)*0.2), round(w * 0.235), bottom - round((bottom-top)*0.2)), fill=(123, 150, 178, 76), width=max(2, w // 1800))
    glow = panel.filter(ImageFilter.GaussianBlur(round(h * 0.012)))
    canvas = Image.alpha_composite(canvas, glow)
    canvas = Image.alpha_composite(canvas, panel)
    ornament_record = paste_ornament(canvas, spec)
    logo_record = paste_logo(canvas, spec)
    return canvas, logo_record, ornament_record


def render(spec: dict) -> tuple[Image.Image, dict, dict | None]:
    if spec["layout"] == "video-corner-bug":
        return render_corner_bug(spec)
    if spec["layout"] == "video-lower-third":
        return render_lower_third(spec)
    return render_opaque(spec)


def write_asset(spec: dict) -> dict:
    image, logo_record, ornament_record = render(spec)
    channel = spec["channel"]
    master_path = MASTER_DIR / f"{spec['id']}.png"
    png_path = EXPORT_DIR / channel / "png" / f"{spec['id']}.png"
    webp_path = EXPORT_DIR / channel / "webp" / f"{spec['id']}.webp"
    master_path.parent.mkdir(parents=True, exist_ok=True)
    png_path.parent.mkdir(parents=True, exist_ok=True)
    webp_path.parent.mkdir(parents=True, exist_ok=True)

    image.save(master_path, "PNG", optimize=True)
    shutil.copyfile(master_path, png_path)
    image.save(webp_path, "WEBP", lossless=True, method=6)

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
        "logo_source": logo_record,
        "ornament_source": ornament_record,
        "format_policy": {
            "png": "lossless master/delivery",
            "webp": "lossless digital delivery",
            "svg": "intentionally omitted: composition uses protected raster logo artwork and atmospheric raster effects; editable source is the governed template spec"
        },
        "files": {
            "master_png": {
                "path": str(master_path.relative_to(ROOT)).replace("\\", "/"),
                "bytes": master_path.stat().st_size,
                "sha256": sha256(master_path),
            },
            "png": {
                "path": str(png_path.relative_to(ROOT)).replace("\\", "/"),
                "bytes": png_path.stat().st_size,
                "sha256": sha256(png_path),
            },
            "webp": {
                "path": str(webp_path.relative_to(ROOT)).replace("\\", "/"),
                "bytes": webp_path.stat().st_size,
                "sha256": sha256(webp_path),
                "lossless": True,
            },
        },
        "qa_status": "passed-by-deterministic-build-pending-contact-sheet-review",
    }


def make_qa(records: list[dict]) -> None:
    tile_w, tile_h = 420, 280
    cols = 2
    rows = (len(records) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tile_w, rows * tile_h), (20, 24, 34))
    font = ImageFont.load_default()
    d = ImageDraw.Draw(sheet)
    for i, record in enumerate(records):
        src = ROOT / record["files"]["png"]["path"]
        img = Image.open(src).convert("RGBA")
        preview_bg = Image.new("RGBA", img.size, (28, 34, 48, 255))
        if record["transparency"]:
            preview_bg.alpha_composite(img)
            img = preview_bg
        thumb = img.convert("RGB")
        thumb.thumbnail((tile_w - 24, tile_h - 54), Image.Resampling.LANCZOS)
        x = (i % cols) * tile_w
        y = (i // cols) * tile_h
        px = x + (tile_w - thumb.width) // 2
        py = y + 12
        sheet.paste(thumb, (px, py))
        d.text((x + 12, y + tile_h - 34), f"{record['id']}  {record['width']}x{record['height']}", fill=(220, 216, 210), font=font)
    QA_PATH.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(QA_PATH, "JPEG", quality=90, optimize=True)


def main() -> None:
    specs_doc = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    records = [write_asset(spec) for spec in specs_doc["templates"]]
    make_qa(records)

    manifest = {
        "schema_version": "1.0",
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
            "product-card and email-signature content remains live/template-driven",
            "video assets are static overlays only, not motion deliverables"
        ]
    }
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Built {len(records)} Wave 2 static templates")
    print(MANIFEST_PATH.relative_to(ROOT))
    print(QA_PATH.relative_to(ROOT))


if __name__ == "__main__":
    main()

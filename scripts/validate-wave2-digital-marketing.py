#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "brand/manifests/wave2-digital-marketing-manifest.json"
SPEC = ROOT / "brand/templates/digital-marketing/template-specs.json"
EMAIL = ROOT / "brand/templates/digital-marketing/email/luxsync-email-signature.html"
PRODUCT_HTML = ROOT / "brand/templates/digital-marketing/product-card/product-card-template.html"
PRODUCT_CSS = ROOT / "brand/templates/digital-marketing/product-card/product-card.css"

EXPECTED_IDS = {
    "social-square-editorial": (1080, 1080),
    "social-portrait-editorial": (1080, 1350),
    "social-story-editorial": (1080, 1920),
    "social-landscape-editorial": (1200, 628),
    "presentation-title-frame": (1920, 1080),
    "presentation-section-frame": (1920, 1080),
    "campaign-landscape-frame": (1600, 900),
    "campaign-square-frame": (1080, 1080),
    "video-corner-bug-overlay": (3840, 2160),
    "video-lower-third-overlay": (3840, 2160),
}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def fail(errors: list[str]) -> None:
    if errors:
        print("Wave 2 digital marketing validation FAILED")
        for error in errors:
            print("-", error)
        raise SystemExit(1)


def main() -> None:
    errors: list[str] = []
    for path in (MANIFEST, SPEC, EMAIL, PRODUCT_HTML, PRODUCT_CSS):
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")
    fail(errors)

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    specs = json.loads(SPEC.read_text(encoding="utf-8"))

    if manifest.get("status") != "qa-passed":
        errors.append("Wave 2 manifest must be qa-passed before PR validation")
    if manifest.get("static_asset_count") != len(EXPECTED_IDS):
        errors.append("Wave 2 manifest static_asset_count mismatch")
    if specs.get("brand_system") != "LuxSync Production Raster v5":
        errors.append("Wave 2 template spec brand system mismatch")
    if specs.get("official_slogan") != "Where Luxury Lives Intelligently":
        errors.append("Wave 2 template spec slogan mismatch")

    records = {item.get("id"): item for item in manifest.get("static_assets", [])}
    if set(records) != set(EXPECTED_IDS):
        errors.append(f"Wave 2 static asset ID mismatch: {sorted(set(records) ^ set(EXPECTED_IDS))}")

    for asset_id, dims in EXPECTED_IDS.items():
        item = records.get(asset_id)
        if not item:
            continue
        if (item.get("width"), item.get("height")) != dims:
            errors.append(f"{asset_id}: manifest dimensions mismatch")
        if item.get("qa_status") != "passed":
            errors.append(f"{asset_id}: qa_status must be passed")
        files = item.get("files", {})
        paths = {}
        for key in ("master_png", "png", "webp"):
            rec = files.get(key, {})
            rel = rec.get("path")
            if not rel:
                errors.append(f"{asset_id}: missing {key} path")
                continue
            path = ROOT / rel
            paths[key] = path
            if not path.exists():
                errors.append(f"{asset_id}: missing {key} file {rel}")
                continue
            if rec.get("sha256") != digest(path):
                errors.append(f"{asset_id}: {key} hash mismatch")
        if all(key in paths and paths[key].exists() for key in ("master_png", "png", "webp")):
            if digest(paths["master_png"]) != digest(paths["png"]):
                errors.append(f"{asset_id}: master and PNG delivery must be byte-identical")
            with Image.open(paths["png"]) as png, Image.open(paths["webp"]) as webp:
                if png.size != dims or webp.size != dims:
                    errors.append(f"{asset_id}: rendered image dimensions mismatch")
                p = png.convert("RGBA")
                w = webp.convert("RGBA")
                if ImageChops.difference(p, w).getbbox() is not None:
                    errors.append(f"{asset_id}: WebP is not pixel-identical to PNG lossless source")
                has_alpha = p.getextrema()[3][0] < 255
                if bool(item.get("transparency")) != has_alpha:
                    errors.append(f"{asset_id}: transparency declaration mismatch")

        logo = item.get("logo_source", {})
        logo_path = ROOT / logo.get("path", "")
        if not logo_path.exists() or logo.get("sha256") != digest(logo_path):
            errors.append(f"{asset_id}: protected logo source hash/path mismatch")
        ornament = item.get("ornament_source")
        if ornament:
            ornament_path = ROOT / ornament.get("path", "")
            if not ornament_path.exists() or ornament.get("sha256") != digest(ornament_path):
                errors.append(f"{asset_id}: ornament source hash/path mismatch")

    qa = manifest.get("qa", {})
    qa_path = ROOT / qa.get("contact_sheet", "")
    if not qa_path.exists():
        errors.append("Wave 2 QA contact sheet missing")
    elif qa.get("sha256") != digest(qa_path):
        errors.append("Wave 2 QA contact sheet hash mismatch")
    if qa.get("status") != "passed-manual-review":
        errors.append("Wave 2 QA contact sheet must record passed-manual-review")

    email = EMAIL.read_text(encoding="utf-8")
    for token in ("{{logo_url}}", "{{name}}", "{{title}}", "{{email}}", "{{phone}}", "{{website}}", "Where Luxury Lives Intelligently"):
        if token not in email:
            errors.append(f"email signature missing placeholder/token: {token}")

    product_html = PRODUCT_HTML.read_text(encoding="utf-8")
    for token in ("{{image_url}}", "{{title}}", "{{summary}}", "{{feature_items}}", "{{validated_price}}", "{{cta_label}}"):
        if token not in product_html:
            errors.append(f"product card template missing placeholder: {token}")
    if "$" in product_html:
        errors.append("product card template must not contain a baked price")

    css = PRODUCT_CSS.read_text(encoding="utf-8")
    for token in ("#0D1526", "#172036", "#D0BEB0", "#7B96B2", "#D6B0A0", "prefers-reduced-motion", "focus-visible"):
        if token not in css:
            errors.append(f"product card CSS missing brand/accessibility token: {token}")

    fail(errors)
    print("Wave 2 digital marketing validation PASSED")
    print(f"Static templates: {len(EXPECTED_IDS)}")
    print("Live templates: email signature + product card")


if __name__ == "__main__":
    main()

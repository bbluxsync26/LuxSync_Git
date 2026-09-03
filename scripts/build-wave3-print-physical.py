#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas as pdfcanvas

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "brand/templates/print-physical/template-specs.json"
PHYSICAL_SPEC_PATH = ROOT / "brand/templates/print-physical/physical-production-specs.json"
LOGO_DIR = ROOT / "brand/assets/logos/png"
ORNAMENT_DIR = ROOT / "brand/assets/dividers/png"
MASTER_DIR = ROOT / "brand/masters/print-physical/wave3"
EXPORT_DIR = ROOT / "brand/exports/print/wave3"
QA_PATH = ROOT / "brand/audit/qa/wave3-print-physical.jpg"
MANIFEST_PATH = ROOT / "brand/manifests/wave3-print-physical-manifest.json"

DPI = 300
PT_PER_IN = 72.0

SLATE = (13, 21, 38, 255)
SUEDE = (23, 32, 54, 255)
DRIFTWOOD = (208, 190, 176, 255)
STEEL = (123, 150, 178, 255)
CHAMPAGNE = (214, 176, 160, 255)
PAPER = (247, 245, 242, 255)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def inches_to_px(value: float) -> int:
    return round(value * DPI)


def full_size(trim: list[float], bleed: float) -> tuple[int, int]:
    return inches_to_px(trim[0] + 2 * bleed), inches_to_px(trim[1] + 2 * bleed)


def trim_box_px(trim: list[float], bleed: float) -> tuple[int, int, int, int]:
    b = inches_to_px(bleed)
    return b, b, b + inches_to_px(trim[0]), b + inches_to_px(trim[1])


def layered_dark(width: int, height: int) -> Image.Image:
    image = Image.new("RGBA", (width, height), SLATE)
    px = image.load()
    for y in range(height):
        t = y / max(1, height - 1)
        for x in range(width):
            s = min(1.0, 0.18 + 0.55 * t + 0.12 * (x / max(1, width - 1)))
            px[x, y] = (
                round(SLATE[0] + (SUEDE[0] - SLATE[0]) * s),
                round(SLATE[1] + (SUEDE[1] - SLATE[1]) * s),
                round(SLATE[2] + (SUEDE[2] - SLATE[2]) * s),
                255,
            )
    glow = Image.new("RGBA", image.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(glow)
    d.ellipse((int(width*.60), -int(height*.12), int(width*1.10), int(height*.55)), fill=(STEEL[0], STEEL[1], STEEL[2], 38))
    d.ellipse((-int(width*.18), int(height*.58), int(width*.36), int(height*1.12)), fill=(CHAMPAGNE[0], CHAMPAGNE[1], CHAMPAGNE[2], 25))
    glow = glow.filter(ImageFilter.GaussianBlur(max(24, round(min(width, height)*.055))))
    return Image.alpha_composite(image, glow)


def background(spec: dict, width: int, height: int) -> Image.Image:
    if spec["background"] == "dark-full":
        return layered_dark(width, height)
    return Image.new("RGBA", (width, height), PAPER)


def resize(asset: Image.Image, width: int, max_height: int | None = None) -> Image.Image:
    ratio = width / asset.width
    height = max(1, round(asset.height * ratio))
    if max_height and height > max_height:
        ratio = max_height / asset.height
        width = max(1, round(asset.width * ratio))
        height = max_height
    return asset.resize((width, height), Image.Resampling.LANCZOS)


def anchor_position(anchor: str, canvas: tuple[int, int], asset: tuple[int, int], trim_box: tuple[int, int, int, int]) -> tuple[int, int]:
    w, h = canvas
    aw, ah = asset
    l, t, r, b = trim_box
    tw, th = r-l, b-t
    mx = round(tw*.055)
    my = round(th*.055)
    if anchor == "center":
        return l + round((tw-aw)/2), t + round((th-ah)/2)
    if anchor == "center-top":
        return l + round((tw-aw)/2), t + round(th*.16)
    if anchor == "top-left":
        return l+mx, t+my
    if anchor == "top-right":
        return r-aw-mx, t+my
    if anchor == "right-center":
        return r-aw-mx, t+round((th-ah)/2)
    return l+mx, t+my


def paste_logo(canvas: Image.Image, spec: dict, trim_box: tuple[int, int, int, int]) -> dict:
    path = LOGO_DIR / spec["logo"]
    logo = Image.open(path).convert("RGBA")
    trim_w = trim_box[2]-trim_box[0]
    target_w = round(trim_w * float(spec["logo_width_ratio"]))
    logo = resize(logo, target_w, round((trim_box[3]-trim_box[1])*.36))
    pos = anchor_position(spec["logo_anchor"], canvas.size, logo.size, trim_box)
    canvas.alpha_composite(logo, dest=pos)
    return {"path": str(path.relative_to(ROOT)).replace("\\","/"), "sha256": sha256(path), "placement": [*pos, logo.width, logo.height]}


def paste_ornament(canvas: Image.Image, spec: dict, trim_box: tuple[int, int, int, int]) -> dict | None:
    name = spec.get("ornament")
    if not name:
        return None
    path = ORNAMENT_DIR / name
    ornament = Image.open(path).convert("RGBA")
    l,t,r,b = trim_box
    tw, th = r-l, b-t
    target_w = round(tw * (0.32 if "orbit" not in name else 0.28))
    ornament = resize(ornament, target_w, round(th*.16))
    ow, oh = ornament.size
    anchor = spec.get("ornament_anchor")
    if anchor == "bottom-center":
        pos = (l+round((tw-ow)/2), b-oh-round(th*.08))
    elif anchor == "bottom-left":
        pos = (l+round(tw*.055), b-oh-round(th*.07))
    elif anchor == "lower-left":
        pos = (l+round(tw*.06), b-oh-round(th*.14))
    elif anchor == "right-center":
        pos = (r-ow-round(tw*.05), t+round((th-oh)/2))
    elif anchor == "header-line":
        pos = (l+round(tw*.055), t+round(th*.145))
    else:
        pos = (l+round(tw*.055), b-oh-round(th*.07))
    canvas.alpha_composite(ornament, dest=pos)
    return {"path": str(path.relative_to(ROOT)).replace("\\","/"), "sha256": sha256(path), "placement": [*pos, ow, oh]}


def add_architecture(canvas: Image.Image, spec: dict, trim_box: tuple[int,int,int,int]) -> None:
    l,t,r,b = trim_box
    tw, th = r-l, b-t
    d = ImageDraw.Draw(canvas)
    if spec["background"] == "dark-full":
        d.rounded_rectangle((l+round(tw*.025), t+round(th*.025), r-round(tw*.025), b-round(th*.025)), radius=max(12, round(min(tw,th)*.025)), outline=(CHAMPAGNE[0],CHAMPAGNE[1],CHAMPAGNE[2],48), width=max(2,round(min(tw,th)*.002)))
    else:
        d.rectangle((l, t, r, t+round(th*.035)), fill=SLATE)
        d.line((l+round(tw*.055), b-round(th*.055), r-round(tw*.055), b-round(th*.055)), fill=(STEEL[0],STEEL[1],STEEL[2],120), width=max(2,round(tw*.0015)))


def render(spec: dict) -> tuple[Image.Image, dict, dict | None, tuple[int,int,int,int]]:
    trim = spec["trim_in"]
    bleed = float(spec["bleed_in"])
    w,h = full_size(trim, bleed)
    box = trim_box_px(trim, bleed)
    img = background(spec, w, h)
    add_architecture(img, spec, box)
    ornament = paste_ornament(img, spec, box)
    logo = paste_logo(img, spec, box)
    return img, logo, ornament, box


def save_pdf(image_path: Path, pdf_path: Path, trim: list[float], bleed: float) -> None:
    page_w = (trim[0] + 2*bleed) * PT_PER_IN
    page_h = (trim[1] + 2*bleed) * PT_PER_IN
    c = pdfcanvas.Canvas(str(pdf_path), pagesize=(page_w, page_h), pageCompression=1)
    c.drawImage(ImageReader(str(image_path)), 0, 0, width=page_w, height=page_h, preserveAspectRatio=False, mask='auto')
    c.showPage()
    c.save()


def live_zones_to_px(spec: dict, trim_box: tuple[int,int,int,int]) -> list[dict]:
    l,t,r,b = trim_box
    tw, th = r-l, b-t
    out=[]
    for z in spec.get("live_content_zones", []):
        x,y,w,h = z["rect_trim_ratio"]
        out.append({"id":z["id"],"rect_px":[round(l+x*tw),round(t+y*th),round(w*tw),round(h*th)],"rect_trim_ratio":z["rect_trim_ratio"]})
    return out


def write_asset(spec: dict) -> dict:
    img, logo_record, ornament_record, trim_box = render(spec)
    asset_id = spec["id"]
    family = spec["family"]
    master_png = MASTER_DIR / f"{asset_id}.png"
    png_path = EXPORT_DIR / family / "png" / f"{asset_id}.png"
    tiff_path = EXPORT_DIR / family / "tiff" / f"{asset_id}.tiff"
    pdf_path = EXPORT_DIR / family / "pdf" / f"{asset_id}.pdf"
    for p in [master_png, png_path, tiff_path, pdf_path]: p.parent.mkdir(parents=True, exist_ok=True)
    img.save(master_png, "PNG", optimize=True, dpi=(DPI,DPI))
    shutil.copyfile(master_png, png_path)
    cmyk = img.convert("RGB").convert("CMYK")
    cmyk.save(tiff_path, "TIFF", compression="tiff_lzw", dpi=(DPI,DPI))
    save_pdf(master_png, pdf_path, spec["trim_in"], float(spec["bleed_in"]))
    return {
      "id": asset_id,
      "family": family,
      "dpi": DPI,
      "trim_in": spec["trim_in"],
      "bleed_in": spec["bleed_in"],
      "full_pixel_dimensions": [img.width,img.height],
      "trim_box_px": list(trim_box),
      "background": spec["background"],
      "logo_source": {**logo_record,"identity_rule":"exact approved LuxSync raster logo artwork composited without redraw, recolor or retyping"},
      "ornament_source": ornament_record,
      "live_content_zones": live_zones_to_px(spec, trim_box),
      "master_type": "raster-print-composition-from-approved-sources",
      "editable_source": "brand/templates/print-physical/template-specs.json",
      "color_policy": {"png":"sRGB/RGBA source art","tiff":"CMYK conversion companion without vendor ICC claim","pdf":"vendor-neutral exact-page-size source PDF; printer preflight required"},
      "files": {
        "master_png":{"path":str(master_png.relative_to(ROOT)).replace("\\","/"),"sha256":sha256(master_png),"bytes":master_png.stat().st_size},
        "png":{"path":str(png_path.relative_to(ROOT)).replace("\\","/"),"sha256":sha256(png_path),"bytes":png_path.stat().st_size},
        "tiff":{"path":str(tiff_path.relative_to(ROOT)).replace("\\","/"),"sha256":sha256(tiff_path),"bytes":tiff_path.stat().st_size},
        "pdf":{"path":str(pdf_path.relative_to(ROOT)).replace("\\","/"),"sha256":sha256(pdf_path),"bytes":pdf_path.stat().st_size}
      },
      "qa_status":"generated-pending-contact-sheet-review"
    }


def make_qa(records: list[dict]) -> None:
    tile_w,tile_h=420,320
    cols=2
    rows=(len(records)+1)//2
    sheet=Image.new("RGB",(cols*tile_w,rows*tile_h),(20,24,34))
    draw=ImageDraw.Draw(sheet)
    font=ImageFont.load_default()
    for i,rec in enumerate(records):
        img=Image.open(ROOT/rec["files"]["png"]["path"]).convert("RGB")
        img.thumbnail((tile_w-32,tile_h-52),Image.Resampling.LANCZOS)
        x=(i%cols)*tile_w+(tile_w-img.width)//2
        y=(i//cols)*tile_h+12
        sheet.paste(img,(x,y))
        draw.text(((i%cols)*tile_w+12,(i//cols)*tile_h+tile_h-30),rec["id"],fill=(230,230,230),font=font)
    QA_PATH.parent.mkdir(parents=True,exist_ok=True)
    sheet.save(QA_PATH,"JPEG",quality=92,optimize=True)


def main() -> None:
    specs=json.loads(SPEC_PATH.read_text())
    physical=json.loads(PHYSICAL_SPEC_PATH.read_text())
    records=[write_asset(s) for s in specs["templates"]]
    make_qa(records)
    manifest={
      "schema_version":"1.0",
      "brand":"LuxSync",
      "prompt":"PR-BRAND-001",
      "wave":"wave3",
      "status":"generated-pending-manual-qa-and-pr-validation",
      "brand_system":specs["brand_system"],
      "design_dna":specs["design_dna"],
      "dpi":DPI,
      "template_spec":{"path":str(SPEC_PATH.relative_to(ROOT)).replace("\\","/"),"sha256":sha256(SPEC_PATH)},
      "physical_spec":{"path":str(PHYSICAL_SPEC_PATH.relative_to(ROOT)).replace("\\","/"),"sha256":sha256(PHYSICAL_SPEC_PATH),"placement_count":len(physical["placements"])},
      "static_asset_count":len(records),
      "static_assets":records,
      "qa":{"contact_sheet":str(QA_PATH.relative_to(ROOT)).replace("\\","/"),"sha256":sha256(QA_PATH),"status":"generated-pending-manual-review"},
      "specialty_production_status":"placement-guidance-complete; vendor-specific one-color/embroidery/engraving/vinyl/screen-print/foil conversions intentionally pending actual vendor constraints",
      "publication_guardrails":[
        "generated static source art contains no invented personal/contact/invoice data",
        "exact approved LuxSync raster logo artwork only",
        "CMYK TIFF companions do not claim a vendor ICC profile",
        "PDFs require selected-printer preflight before manufacture",
        "specialty-production variants must not be invented from screenshots or generative redraws"
      ]
    }
    MANIFEST_PATH.parent.mkdir(parents=True,exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(manifest,indent=2)+"\n")
    print(f"Built {len(records)} Wave 3 print assets")
    print(MANIFEST_PATH.relative_to(ROOT))
    print(QA_PATH.relative_to(ROOT))

if __name__ == "__main__":
    main()

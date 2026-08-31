#!/usr/bin/env python3
"""Render normalized LuxSync SVG masters to PNG/WebP and refresh catalog contact sheets."""
from pathlib import Path
import re
import shutil
import subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = ROOT / "brand" / "assets"
CATALOG = ASSET_ROOT / "00-catalog"
PROTECTED_EXACT_LOGOS = {
    "01-brand/luxsync-monogram-orb.svg",
    "01-brand/luxsync-horizontal-lockup.svg",
}


def run(*args: str) -> None:
    subprocess.run(list(args), check=True)


def svg_size(path: Path) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")[:1200]
    match = re.search(r'<svg[^>]*\bwidth="([0-9.]+)"[^>]*\bheight="([0-9.]+)"', text)
    if not match:
        return 1200, 800
    return int(float(match.group(1))), int(float(match.group(2)))


def render(svg: Path) -> None:
    width, height = svg_size(svg)
    png = svg.with_suffix(".png")
    webp = svg.with_suffix(".webp")
    run("inkscape", str(svg), "--export-type=png", f"--export-filename={png}", f"--export-width={width}", f"--export-height={height}", "--export-background-opacity=0")
    convert = shutil.which("magick") or shutil.which("convert")
    if not convert:
        raise RuntimeError("ImageMagick not found")
    run(convert, str(png), "-strip", "-quality", "92", str(webp))


def font(size: int, family: str = "Inter"):
    try:
        result = subprocess.run(["fc-match", "-f", "%{file}", family], check=True, capture_output=True, text=True)
        path = result.stdout.strip()
        if path and Path(path).exists():
            return ImageFont.truetype(path, size)
    except Exception:
        pass
    return ImageFont.load_default()


def contact_sheet(category: str, paths: list[Path], output: Path) -> None:
    cols = 4 if len(paths) > 6 else 3
    tile_w, tile_h = 380, 310
    rows = (len(paths) + cols - 1) // cols
    canvas = Image.new("RGB", (cols * tile_w, rows * tile_h), "#F7F4F2")
    draw = ImageDraw.Draw(canvas)
    label_font = font(17)
    for index, path in enumerate(paths):
        x = (index % cols) * tile_w
        y = (index // cols) * tile_h
        image = Image.open(path).convert("RGBA")
        image.thumbnail((tile_w - 50, tile_h - 70), Image.Resampling.LANCZOS)
        px = x + (tile_w - image.width) // 2
        py = y + 12 + (tile_h - 70 - image.height) // 2
        canvas.paste(image, (px, py), image)
        draw.text((x + 16, y + tile_h - 27), path.stem, fill="#0D1526", font=label_font)
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, optimize=True)


def rebuild_catalog(svgs: list[Path]) -> None:
    CATALOG.mkdir(parents=True, exist_ok=True)
    groups: dict[str, list[Path]] = {}
    for svg in svgs:
        category = svg.relative_to(ASSET_ROOT).parts[0]
        groups.setdefault(category, []).append(svg.with_suffix(".png"))

    sheets = []
    for category, paths in sorted(groups.items()):
        output = CATALOG / f"{category}-contact-sheet.png"
        contact_sheet(category, sorted(paths), output)
        sheets.append((category, output))

    master = Image.new("RGB", (1740, 1580), "#F7F4F2")
    draw = ImageDraw.Draw(master)
    title_font = font(22, "Manrope")
    for index, (category, path) in enumerate(sheets):
        x = 20 + (index % 3) * 570
        y = 20 + (index // 3) * 390
        image = Image.open(path).convert("RGB")
        image.thumbnail((550, 345), Image.Resampling.LANCZOS)
        master.paste(image, (x + (550 - image.width) // 2, y))
        draw.text((x + 8, y + 350), category, fill="#0D1526", font=title_font)
    master.save(CATALOG / "LuxSync-master-contact-sheet.png", optimize=True)


def write_svg_list(svgs: list[Path]) -> None:
    lines = [
        "# LuxSync Luxury Orbit SVG Asset List",
        "",
        f"Generated SVG masters: **{len(svgs)}**",
        "",
        "These SVGs are generated directly by `scripts/generate-luxury-orbit-assets.py`; they do **not** need to be sent through an image generator.",
        "",
    ]
    current = None
    for svg in svgs:
        rel = svg.relative_to(ASSET_ROOT)
        category = rel.parts[0]
        if category != current:
            current = category
            lines.extend([f"## {category}", ""])
        lines.append(f"- `{rel.as_posix()}`")
    (CATALOG / "SVG-ASSET-LIST.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


def main() -> int:
    svgs = sorted(p for p in ASSET_ROOT.rglob("*.svg") if "00-catalog" not in p.parts)
    for index, svg in enumerate(svgs, 1):
        rel = svg.relative_to(ASSET_ROOT).as_posix()
        if rel in PROTECTED_EXACT_LOGOS:
            print(f"[{index}/{len(svgs)}] preserve exact approved logo: {svg.relative_to(ROOT)}")
            continue
        print(f"[{index}/{len(svgs)}] {svg.relative_to(ROOT)}")
        render(svg)
    rebuild_catalog(svgs)
    write_svg_list(svgs)
    print(f"Rendered normalized SVG masters while preserving {len(PROTECTED_EXACT_LOGOS)} exact approved logo rasters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

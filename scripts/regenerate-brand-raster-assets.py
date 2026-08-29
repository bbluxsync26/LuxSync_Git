#!/usr/bin/env python3
"""Generate LuxSync Luxury Orbit SVG masters, PNG/WebP siblings, and contact sheets."""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = ROOT / 'brand' / 'assets'
GENERATOR = ROOT / 'scripts' / 'generate-luxury-orbit-assets.py'

CATEGORY_SHEETS = {
    '01-brand': '01-brand-contact-sheet.png',
    '02-icons-brand': '02-icons-brand-contact-sheet.png',
    '03-icons-website': '03-icons-website-contact-sheet.png',
    '04-icons-social': '04-icons-social-contact-sheet.png',
    '05-palette': '05-palette-contact-sheet.png',
    '06-gradients': '06-gradients-contact-sheet.png',
    '07-components': '07-components-contact-sheet.png',
    '08-cards': '08-cards-contact-sheet.png',
    '09-illustrations': '09-illustrations-contact-sheet.png',
    '10-product-cards': '10-product-cards-contact-sheet.png',
    '11-banners': '11-banners-contact-sheet.png',
}

def run(*args: str) -> None:
    subprocess.run(list(args), check=True)

def svg_size(svg: Path) -> tuple[int, int]:
    text = svg.read_text(encoding='utf-8')[:1000]
    m = re.search(r'<svg[^>]*\bwidth="([0-9.]+)"[^>]*\bheight="([0-9.]+)"', text)
    if not m:
        return 1200, 800
    return max(64, int(float(m.group(1)))), max(64, int(float(m.group(2))))

def render_svg(svg: Path) -> None:
    w, h = svg_size(svg)
    png = svg.with_suffix('.png')
    webp = svg.with_suffix('.webp')
    run('inkscape', str(svg), '--export-type=png', f'--export-filename={png}', f'--export-width={w}', f'--export-height={h}', '--export-background-opacity=0')
    convert = shutil.which('magick') or shutil.which('convert')
    if not convert:
        raise RuntimeError('ImageMagick convert/magick not found')
    run(convert, str(png), '-strip', '-quality', '92', str(webp))

def font(size: int, bold: bool=False):
    candidates = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def make_contact_sheet(category: str, filename: str) -> None:
    folder = ASSET_ROOT / category
    files = sorted(folder.glob('*.png'))
    if not files:
        return
    cols = 4
    tile_w, tile_h = 360, 300
    rows = (len(files) + cols - 1) // cols
    canvas = Image.new('RGB', (cols*tile_w + 60, rows*tile_h + 90), '#F7F4F2')
    draw = ImageDraw.Draw(canvas)
    draw.text((30,20), f'LuxSync Luxury Orbit • {category}', font=font(28,True), fill='#0B1D3A')
    for i, path in enumerate(files):
        im = Image.open(path).convert('RGBA')
        im.thumbnail((tile_w-50, tile_h-80), Image.Resampling.LANCZOS)
        card_x = 30 + (i % cols)*tile_w + 10
        card_y = 60 + (i // cols)*tile_h + 10
        canvas.paste('#FFFFFF', (card_x, card_y, card_x+tile_w-20, card_y+tile_h-20))
        x = 30 + (i % cols)*tile_w + (tile_w-im.width)//2
        y = 60 + (i // cols)*tile_h + 10
        canvas.paste(im, (x,y), im)
        draw.text((30+(i%cols)*tile_w+24, 60+(i//cols)*tile_h+tile_h-48), path.stem, font=font(18), fill='#172846')
    out = ASSET_ROOT / '00-catalog' / filename
    out.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out, optimize=True)

def make_master_sheet() -> None:
    selected = [
        ASSET_ROOT/'01-brand/luxsync-horizontal-lockup.png',
        ASSET_ROOT/'11-banners/str-smart-home-roi-guide.png',
        ASSET_ROOT/'03-icons-website/security.png',
        ASSET_ROOT/'07-components/button-primary.png',
        ASSET_ROOT/'10-product-cards/category-security.png',
        ASSET_ROOT/'10-product-cards/category-comfort.png',
        ASSET_ROOT/'11-banners/hero-where-luxury-lives-intelligently.png',
        ASSET_ROOT/'11-banners/shop-curated-smart-living.png',
    ]
    positions=[(50,110,820,360),(930,110,820,360),(50,520,500,330),(600,520,500,330),(1150,520,600,330),(50,900,520,430),(610,900,520,430),(1170,900,580,430)]
    canvas = Image.new('RGB',(1800,1400),'#F7F4F2')
    draw = ImageDraw.Draw(canvas)
    draw.text((50,30),'LuxSync Luxury Orbit • Master Contact Sheet',font=font(36,True),fill='#0B1D3A')
    for path,pos in zip(selected,positions):
        if not path.exists():
            continue
        x,y,w,h=pos
        im=Image.open(path).convert('RGBA')
        im.thumbnail((w,h),Image.Resampling.LANCZOS)
        canvas.paste(im,(x+(w-im.width)//2,y+(h-im.height)//2),im)
    canvas.save(ASSET_ROOT/'00-catalog/LuxSync-master-contact-sheet.png', optimize=True)

def main() -> int:
    run(sys.executable, str(GENERATOR))
    svgs=[p for p in ASSET_ROOT.rglob('*.svg') if '00-catalog' not in p.parts]
    for i, svg in enumerate(sorted(svgs),1):
        print(f'[{i}/{len(svgs)}] {svg.relative_to(ROOT)}')
        render_svg(svg)
    for cat, fn in CATEGORY_SHEETS.items():
        make_contact_sheet(cat,fn)
    make_master_sheet()
    svg_list = ASSET_ROOT / '00-catalog' / 'SVG-ASSET-LIST.md'
    lines = ['# LuxSync Luxury Orbit SVG Asset List', '', f'Generated SVG masters: **{len(svgs)}**', '', 'These SVGs are generated directly by `scripts/generate-luxury-orbit-assets.py`; they do **not** need to be sent through an image generator.', '']
    current = None
    for svg in sorted(svgs):
        rel = svg.relative_to(ASSET_ROOT)
        category = rel.parts[0]
        if category != current:
            current = category
            lines.extend([f'## {category}', ''])
        lines.append(f'- `{rel.as_posix()}`')
    svg_list.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'Regenerated {len(svgs)} SVG/PNG/WebP asset sets plus contact sheets.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())

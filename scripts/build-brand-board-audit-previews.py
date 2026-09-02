#!/usr/bin/env python3
from pathlib import Path
from PIL import Image
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'brand/reference-boards'
OUT = ROOT / 'brand/audit/tmp-board-previews'
OUT.mkdir(parents=True, exist_ok=True)
records = []
for src in sorted(SOURCE.glob('*.png')):
    im = Image.open(src).convert('RGB')
    original_size = im.size
    preview = im.copy()
    preview.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
    dest = OUT / f'{src.stem}.jpg'
    preview.save(dest, 'JPEG', quality=78, optimize=True, progressive=True)
    records.append({
        'source': src.relative_to(ROOT).as_posix(),
        'source_sha256': hashlib.sha256(src.read_bytes()).hexdigest(),
        'original_size': list(original_size),
        'preview': dest.relative_to(ROOT).as_posix(),
        'preview_size': list(preview.size),
        'preview_bytes': dest.stat().st_size,
        'preview_sha256': hashlib.sha256(dest.read_bytes()).hexdigest(),
    })
(OUT / 'manifest.json').write_text(json.dumps({'records': records}, indent=2) + '\n', encoding='utf-8')
print(f'Built {len(records)} board audit previews')

#!/usr/bin/env python3
from pathlib import Path
import base64, io, zipfile

root = Path(__file__).resolve().parents[1]
install = root / '.atomic-installer'
parts = sorted(install.glob('source-sheets.part-*.b64'))
archive = install / 'source-sheets.zip.b64'

if parts:
    encoded = ''.join(p.read_text(encoding='utf-8').strip() for p in parts)
elif archive.exists():
    encoded = archive.read_text(encoding='utf-8').strip()
else:
    encoded = ''

if encoded:
    data = base64.b64decode(encoded, validate=True)
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        names = [n for n in z.namelist() if n.endswith('.webp')]
        if len(names) != 8:
            raise SystemExit(f'Expected 8 archived source sheets; found {len(names)}')
        for name in names:
            payload = base64.b64encode(z.read(name)).decode('ascii')
            (install / f'{Path(name).name}.b64').write_text(payload, encoding='utf-8')
    print(f'Expanded {len(names)} approved source sheets from chunked archive.')
else:
    print('No source sheet archive found; using individual payloads.')

#!/usr/bin/env python3
from pathlib import Path
import base64, io, zipfile
root = Path(__file__).resolve().parents[1]
install = root / '.atomic-installer'
archive = install / 'source-sheets.zip.b64'
if archive.exists():
    data = base64.b64decode(archive.read_text(encoding='utf-8').strip())
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        for name in z.namelist():
            if not name.endswith('.webp'):
                continue
            payload = base64.b64encode(z.read(name)).decode('ascii')
            (install / f'{Path(name).name}.b64').write_text(payload, encoding='utf-8')
    print('Expanded approved source sheet archive into installer payloads.')
else:
    print('No source-sheets.zip.b64 found; using individual payloads.')

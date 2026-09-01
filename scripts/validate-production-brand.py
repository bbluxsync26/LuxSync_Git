#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, struct, xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'brand/assets'
SOURCE=ROOT/'brand/source-logo'
errors=[]
EXPECTED={'logos':3,'icons':16,'dividers':12}
FORMATS=('svg','png','webp')
OLD=('01-logos','02-icons','03-buttons','04-ui-controls','05-dividers-accents','06-product-cards','07-heroes','08-sections','09-stationery')
LOGOS={
 'luxsync-horizontal-combo':'LuxSync_Logo_Horizontal_Combo.png',
 'luxsync-horizontal':'LuxSync_Logo_Horizontal_Final.png',
 'luxsync-orb':'LuxSync_Logo_Orb.png',
}

def fail(msg): errors.append(msg)

for name in OLD:
    if (ASSETS/name).exists(): fail(f'retired grid-sliced folder remains: brand/assets/{name}')

manifest_path=ASSETS/'asset-manifest.json'
if not manifest_path.exists():
    fail('missing brand/assets/asset-manifest.json')
    manifest={'assets':[]}
else:
    manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
    if manifest.get('version')!='6.0-clean-atomic-triple-format': fail('asset manifest version mismatch')
    if manifest.get('formats')!=list(FORMATS): fail('asset manifest format contract mismatch')
items=manifest.get('assets',[])
if len(items)!=sum(EXPECTED.values()): fail(f'expected {sum(EXPECTED.values())} production assets; found {len(items)}')

bycat={k:[] for k in EXPECTED}
for item in items:
    cat=item.get('category'); aid=item.get('id','')
    if cat not in bycat: fail(f'unknown asset category: {cat}'); continue
    bycat[cat].append(aid)
    if item.get('production_status')!='approved' or item.get('qa_status')!='passed': fail(f'{aid}: asset not approved and QA-passed')
    files=item.get('files',{})
    for fmt in FORMATS:
        meta=files.get(fmt,{})
        rel=meta.get('path','')
        p=ASSETS/rel
        if not rel or not p.exists(): fail(f'{aid}: missing {fmt} file'); continue
        digest=hashlib.sha256(p.read_bytes()).hexdigest()
        if meta.get('sha256')!=digest: fail(f'{aid}.{fmt}: manifest hash mismatch')
        if meta.get('bytes')!=p.stat().st_size: fail(f'{aid}.{fmt}: manifest byte count mismatch')
        if fmt=='svg':
            try:
                root=ET.fromstring(p.read_text(encoding='utf-8'))
                if not root.attrib.get('viewBox'): fail(f'{aid}.svg: missing viewBox')
            except Exception as exc: fail(f'{aid}.svg: invalid SVG: {exc}')
        elif fmt=='png':
            data=p.read_bytes()
            if not data.startswith(b'\x89PNG\r\n\x1a\n') or data[12:16]!=b'IHDR': fail(f'{aid}.png: invalid PNG')
            elif len(data)>=26:
                color_type=data[25]
                if cat in {'icons','dividers'} and color_type not in {4,6}: fail(f'{aid}.png: expected alpha-capable PNG')
        else:
            data=p.read_bytes()
            if len(data)<12 or data[:4]!=b'RIFF' or data[8:12]!=b'WEBP': fail(f'{aid}.webp: invalid WebP')

for cat,count in EXPECTED.items():
    if len(bycat[cat])!=count: fail(f'{cat}: expected {count} assets; found {len(bycat[cat])}')
    for fmt in FORMATS:
        p=ASSETS/cat/fmt
        actual=len(list(p.glob(f'*.{fmt}'))) if p.exists() else 0
        if actual!=count: fail(f'{cat}/{fmt}: expected {count} files; found {actual}')

for aid,srcname in LOGOS.items():
    src=SOURCE/srcname; dst=ASSETS/'logos/png'/f'{aid}.png'
    if not src.exists() or not dst.exists(): fail(f'{aid}: missing logo source or PNG production copy')
    elif src.read_bytes()!=dst.read_bytes(): fail(f'{aid}: PNG differs from protected master')

for qa in ('qa/icons-contact-sheet.jpg','qa/dividers-contact-sheet.jpg'):
    if not (ASSETS/qa).exists(): fail(f'missing QA contact sheet: {qa}')

for p in ASSETS.rglob('*'):
    if p.is_file() and any(token in p.name.lower() for token in ('icon_','button_','ui_control_')): fail(f'meaningless legacy crop filename remains: {p.relative_to(ROOT)}')

for rel in ('brand/README.md','brand/assets/README.md','brand/colors.md','website/styles/design-system.md'):
    p=ROOT/rel
    if not p.exists(): fail(f'missing governing file: {rel}')
    else:
        text=p.read_text(encoding='utf-8',errors='replace')
        for token in ('#7B96B2','#D6B0A0','Brushed Dusty Steel'):
            if token not in text: fail(f'{rel}: missing {token}')

if errors:
    print('LuxSync production brand validation FAILED:')
    for e in errors: print('-',e)
    raise SystemExit(1)
print('LuxSync production brand validation PASSED')
print('Assets: 31 clean atomic assets / 93 production files')
print('Formats: SVG + PNG + WebP')

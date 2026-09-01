#!/usr/bin/env python3
from pathlib import Path

# One-time source cutover helper for the clean triple-format production library.
ROOT=Path(__file__).resolve().parents[1]
TEXT_SUFFIXES={'.md','.txt','.json','.py','.js','.mjs','.yml','.yaml','.html','.css'}

for path in ROOT.rglob('*'):
    if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
        continue
    if any(part in {'.git','node_modules','dist'} for part in path.parts):
        continue
    if path.name in {'generate-clean-production-assets.py','patch-clean-asset-references.py'}:
        continue
    text=path.read_text(encoding='utf-8',errors='replace')
    new=text.replace('brand/assets/01-logos/','brand/assets/logos/png/')
    new=new.replace('`brand/assets/02-icons/` through `brand/assets/09-stationery/`','the retired numbered grid-sliced asset folders')
    new=new.replace('outside `brand/assets/logos/png/` are reference-only except for assets explicitly marked `production-approved` in a current asset manifest','are governed by `brand/assets/asset-manifest.json`; only entries marked approved and QA-passed are production-safe')
    if path.name=='validate-repository-consistency.py':
        new=new.replace('if list((ROOT / "brand/assets").rglob("*.svg")):\n    errors.append("brand/assets must remain SVG-free for the Production Raster validator")\n','')
        new=new.replace('"LuxSync_Logo_Horizontal_Combo.png", "LuxSync_Logo_Horizontal_Final.png", "LuxSync_Logo_Orb.png",','"luxsync-horizontal-combo.png", "luxsync-horizontal.png", "luxsync-orb.png",')
    if new!=text:
        path.write_text(new,encoding='utf-8')
print('CLEAN_ASSET_REFERENCE_PATCH_COMPLETE')

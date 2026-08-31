#!/usr/bin/env python3
from pathlib import Path
import base64, json, shutil
ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'brand'/'assets'
INSTALL=ROOT/'.atomic-installer'
if ASSETS.exists(): shutil.rmtree(ASSETS)
old=ROOT/'brand'/'assets-v3'
if old.exists(): shutil.rmtree(old)
(ASSETS/'10-source-sheets').mkdir(parents=True,exist_ok=True)
for b64 in INSTALL.glob('*.webp.b64'):
    target=ASSETS/'10-source-sheets'/b64.name[:-4]
    target.write_bytes(base64.b64decode(b64.read_text().strip()))

def crop_svg(source, sw, sh, box, aria):
    x0,y0,x1,y1=map(int,box); w=x1-x0; h=y1-y0
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{aria}">\n  <image href="../10-source-sheets/{source}" x="{-x0}" y="{-y0}" width="{sw}" height="{sh}" preserveAspectRatio="none"/>\n</svg>\n'

def full_svg(source, sw, sh, aria):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{sw}" height="{sh}" viewBox="0 0 {sw} {sh}" role="img" aria-label="{aria}">\n  <image href="../10-source-sheets/{source}" x="0" y="0" width="{sw}" height="{sh}" preserveAspectRatio="none"/>\n</svg>\n'

def write(rel, content):
    p=ASSETS/rel; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(content,encoding='utf-8')

logos={
'LuxSync_Logo_Horizontal_Combo.svg':('../../source-logo/LuxSync_Logo_Horizontal_Combo.png',2048,768,'LuxSync combined horizontal logo'),
'LuxSync_Logo_Horizontal_Final.svg':('../../source-logo/LuxSync_Logo_Horizontal_Final.png',2048,768,'LuxSync horizontal wordmark logo'),
'LuxSync_Logo_Orb.svg':('../../source-logo/LuxSync_Logo_Orb.png',1254,1254,'LuxSync LS orb logo'),
}
for fn,(href,w,h,aria) in logos.items():
    write('01-logos/'+fn, f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{aria}">\n  <image href="{href}" x="0" y="0" width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet"/>\n</svg>\n')

icon_names=[['home','light-bulb','thermostat','security-shield','security-camera'],['smart-lock','smart-speaker','wifi','monitor','smartphone'],['analytics-bars','clock','settings-gear','automation-lightning','efficiency-leaf']]
xs=[190,455,720,985,1245]; ys=[285,555,805]
for r,y in enumerate(ys):
  for c,x in enumerate(xs):
    n=icon_names[r][c]; write(f'02-icons/{n}.svg',crop_svg('icon-sheet.webp',1448,1086,(x-92,y-92,x+92,y+92),f'LuxSync {n} icon'))
button_boxes={'primary-shop-now':(28,420,405,515),'secondary-learn-more':(530,420,900,515),'tertiary-view-details':(1015,425,1325,515),'filled-secondary-discover-smart-living':(30,610,405,682),'outline-book-a-call':(532,610,900,682),'utility-add-to-cart':(988,610,1325,682),'state-default':(25,960,240,1030),'state-hover':(270,960,490,1030),'state-pressed':(525,960,750,1030),'state-disabled':(780,960,990,1030)}
for n,b in button_boxes.items(): write(f'03-buttons/{n}.svg',crop_svg('button-style-guide.webp',1448,1086,b,f'LuxSync {n} button'))
for n,x in zip(['cart','favorite-heart','account','search','phone','email','share','menu'],[125,290,455,610,760,910,1060,1195]): write(f'03-buttons/icon-{n}.svg',crop_svg('button-style-guide.webp',1448,1086,(x-52,770,x+52,870),f'LuxSync {n} icon button'))
ui_boxes={'toggle-off':(160,235,270,285),'toggle-on':(160,295,270,345),'checkbox-unchecked':(420,235,580,285),'checkbox-checked':(420,295,580,345),'radio-unselected':(690,235,835,285),'radio-selected':(690,295,835,345),'slider':(960,240,1320,310),'select-dropdown-open':(75,455,350,690),'quantity-selector':(415,455,585,520),'search-bar':(660,455,990,520),'sort-dropdown':(1035,455,1230,525),'filter-button':(1260,455,1340,525),'pagination':(525,730,875,790),'primary-button':(75,870,320,935),'secondary-button':(335,870,565,935),'tertiary-button':(590,870,755,935),'text-link':(785,870,915,935),'icon-heart':(950,870,1015,935),'icon-cart':(1020,870,1085,935),'icon-arrow':(1090,870,1160,935),'badge-new':(1210,870,1340,935),'accent-line-spark':(335,980,665,1035),'accent-diamond':(670,970,735,1038),'accent-line-star':(755,980,1025,1035),'accent-brushed-steel':(1080,980,1300,1035)}
for n,b in ui_boxes.items(): write(f'04-ui-controls/{n}.svg',crop_svg('ui-style-board.webp',1448,1086,b,f'LuxSync {n} UI control'))
for i,(y,h) in enumerate([(174,34),(225,28),(276,28)],1): write(f'05-dividers-accents/thin-divider-{i:02d}.svg',crop_svg('dividers-accents-guide.webp',1448,1086,(250,y,1380,y+h),f'LuxSync thin divider {i}'))
for n,b in [('gradient-rose-wide',(255,340,790,390)),('gradient-steel-wide',(810,340,1385,390)),('gradient-rose-thin',(255,395,790,435)),('gradient-steel-thin',(810,395,1385,435)),('accent-rule-rose',(255,455,925,500)),('accent-rule-dusty-steel',(255,500,925,545)),('accent-rule-rose-dotted',(940,455,1385,500)),('accent-rule-steel-dotted',(940,500,1385,545))]: write(f'05-dividers-accents/{n}.svg',crop_svg('dividers-accents-guide.webp',1448,1086,b,f'LuxSync {n}'))
for i,x in enumerate([315,455,570,660,725,790,855,945,1045,1155,1255,1340],1): write(f'05-dividers-accents/sparkle-{i:02d}.svg',crop_svg('dividers-accents-guide.webp',1448,1086,(x-42,565,x+42,650),f'LuxSync sparkle {i}'))
write('05-dividers-accents/brushed-dusty-steel-wide.svg',crop_svg('dividers-accents-guide.webp',1448,1086,(260,675,1360,735),'LuxSync Brushed Dusty Steel accent'))
for i,b in enumerate([(390,755,530,830),(565,755,675,830),(690,755,760,830),(800,755,965,830),(995,755,1140,830),(1180,755,1380,830)],1): write(f'05-dividers-accents/ornament-{i:02d}.svg',crop_svg('dividers-accents-guide.webp',1448,1086,b,f'LuxSync ornament {i}'))
for i,b in enumerate([(260,835,520,925),(575,835,820,925),(850,835,1100,925),(1150,835,1390,925)],1): write(f'05-dividers-accents/section-ender-{i:02d}.svg',crop_svg('dividers-accents-guide.webp',1448,1086,b,f'LuxSync section ender {i}'))
for i,x in enumerate([260,320,385,445,505,570,725,935,1170,1320],1): write(f'05-dividers-accents/mini-accent-{i:02d}.svg',crop_svg('dividers-accents-guide.webp',1448,1086,(x-48,930,x+48,1025),f'LuxSync mini accent {i}'))
for n,b in zip(['touch-panel','smart-speaker','4k-camera','smart-lock'],[(42,155,423,790),(442,155,825,790),(845,155,1230,790),(1250,155,1610,790)]): write(f'06-product-cards/{n}.svg',crop_svg('product-card-sheet.webp',1672,941,b,f'LuxSync {n} product card'))
write('07-heroes/homepage-smart-living.svg',full_svg('homepage-hero.webp',1672,941,'LuxSync smart living homepage hero'))
write('08-roi/smart-home-roi-guide-hero.svg',full_svg('roi-guide-hero.webp',1672,941,'LuxSync Smart Home ROI Guide hero'))
for n,b in {'business-card-front':(50,45,550,330),'business-card-back':(50,375,550,650),'invoice-note':(25,685,575,1035),'letterhead':(600,55,1380,1030)}.items(): write(f'09-stationery/{n}.svg',crop_svg('stationery-suite.webp',1448,1086,b,f'LuxSync {n}'))
write('11-marketing/roi-guide-promo.svg',full_svg('roi-guide-hero.webp',1672,941,'LuxSync ROI guide promotion'))
write('11-marketing/homepage-luxury-smart-home.svg',full_svg('homepage-hero.webp',1672,941,'LuxSync luxury smart home marketing hero'))
palette={'slate-navy':'#0D1526','dark-suede':'#172036','pale-driftwood':'#D0BEB0','warm-taupe-mauve':'#9E8B85','antique-rose-taupe':'#967878','dusty-steel':'#7B96B2','champagne-rose-gold-anchor':'#D6B0A0'}
for n,hx in palette.items(): write(f'12-palette/{n}.svg',f'<svg xmlns="http://www.w3.org/2000/svg" width="600" height="240" viewBox="0 0 600 240" role="img" aria-label="LuxSync {n} swatch"><rect width="600" height="240" fill="{hx}"/></svg>\n')
write('12-palette/brushed-dusty-steel-metallic.svg',crop_svg('brand-board.webp',1448,1086,(905,220,1215,280),'LuxSync Brushed Dusty Steel metallic sample'))
write('12-palette/champagne-rose-gold-metallic.svg',crop_svg('brand-board.webp',1448,1086,(1230,220,1390,280),'LuxSync Champagne Rose Gold metallic sample'))
readme='''# LuxSync Atomic Brand Asset Library\n\n**Status:** Approved production source of truth\n\nThis directory replaces all prior LuxSync asset systems. Every reusable object from the approved brand pass is exposed as an individual SVG file. The SVGs crop or reference the approved source sheets directly, preserving the approved appearance without redrawing.\n\n## Authoritative logos\nThe only authoritative logo masters are in `brand/source-logo/`: `LuxSync_Logo_Horizontal_Combo.png`, `LuxSync_Logo_Horizontal_Final.png`, and `LuxSync_Logo_Orb.png`. Logo wrappers in `01-logos/` reference those exact files. Never redraw, recolor, soften, or re-typeset the logo artwork.\n\n## Approved colors\nSlate Navy `#0D1526`; Dark Suede `#172036`; Pale Driftwood `#D0BEB0`; Warm Taupe Mauve `#9E8B85`; Antique Rose Taupe `#967878`; Dusty Steel `#7B96B2`; Champagne Rose Gold Metallic, anchor `#D6B0A0`.\n\n**Brushed Dusty Steel** is the approved metallic-blue treatment. Electric blue and any other blue are prohibited unless explicitly approved. No new color may be added without explicit approval.\n\n## Individual asset groups\n`01-logos/`, `02-icons/`, `03-buttons/`, `04-ui-controls/`, `05-dividers-accents/`, `06-product-cards/`, `07-heroes/`, `08-roi/`, `09-stationery/`, `10-source-sheets/`, `11-marketing/`, and `12-palette/`.\n\nEditable website text remains Manrope + Inter.\n'''
write('README.md',readme)
files=sorted(str(p.relative_to(ASSETS)) for p in ASSETS.rglob('*') if p.is_file())
write('asset-manifest.json',json.dumps({'version':'4.0-atomic','status':'approved','source_of_truth':'brand/assets','authoritative_logos':['brand/source-logo/LuxSync_Logo_Horizontal_Combo.png','brand/source-logo/LuxSync_Logo_Horizontal_Final.png','brand/source-logo/LuxSync_Logo_Orb.png'],'approved_palette':palette,'metallic_blue':'Brushed Dusty Steel based on #7B96B2','asset_count':len(files),'files':files},indent=2))
for rel in ['scripts/generate-luxury-orbit-assets.py','scripts/normalize-luxury-orbit-fonts.py','scripts/render-luxury-orbit-assets.py','scripts/regenerate-brand-raster-assets.py','scripts/reconcile-asset-metadata.py','scripts/apply-approved-logo-artwork.py']:
    p=ROOT/rel
    if p.exists(): p.unlink()
if INSTALL.exists(): shutil.rmtree(INSTALL)
(ROOT/'brand'/'README.md').write_text('''# LuxSync Brand System\n\n**Status:** Active / Authoritative\n\nThe only active graphic asset system is `brand/assets/`. The former `brand/assets-v3/` and legacy generated asset library are retired and removed.\n\n## Authoritative logo masters\nThese three files in `brand/source-logo/` are immutable: `LuxSync_Logo_Horizontal_Combo.png`, `LuxSync_Logo_Horizontal_Final.png`, and `LuxSync_Logo_Orb.png`. Never redraw, recolor, soften, regenerate, or re-typeset these logos.\n\n## Approved palette\nSlate Navy `#0D1526`; Dark Suede `#172036`; Pale Driftwood `#D0BEB0`; Warm Taupe Mauve `#9E8B85`; Antique Rose Taupe `#967878`; Dusty Steel `#7B96B2`; Champagne Rose Gold Metallic, anchor `#D6B0A0`.\n\nBrushed Dusty Steel is the approved metallic-blue treatment. Electric blue and any additional blue are prohibited unless explicitly approved. No new brand color may be introduced without explicit approval.\n\n## Typography\nUse Manrope for headings/UI and Inter for body/supporting text. Logo lettering remains protected artwork only.\n\n## Atomic asset rule\nEvery reusable object is an individual file under `brand/assets/`. Composite source sheets remain only under `brand/assets/10-source-sheets/` to preserve the exact approved appearance.\n''',encoding='utf-8')
colors=ROOT/'brand'/'colors.md'
if colors.exists():
    txt=colors.read_text(encoding='utf-8').replace('Derived icy-blue highlight tints may be used inside gradients and light effects when necessary for depth.','Do not derive brighter icy-blue or electric-blue tints. Branded blue accents must remain Dusty Steel `#7B96B2` or the approved Brushed Dusty Steel metallic treatment.')
    colors.write_text(txt,encoding='utf-8')
print(f'Installed {sum(1 for p in ASSETS.rglob("*") if p.is_file())} approved atomic asset files.')

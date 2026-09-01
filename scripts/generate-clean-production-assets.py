from __future__ import annotations
from pathlib import Path
import math, json, hashlib, base64, shutil
from PIL import Image, ImageDraw
import cairosvg

REPO=Path(__file__).resolve().parents[1]
ROOT=REPO / 'brand' / 'assets'
ROOT.mkdir(parents=True, exist_ok=True)
for name in ['01-logos','02-icons','03-buttons','04-ui-controls','05-dividers-accents','06-product-cards','07-heroes','08-sections','09-stationery','logos','icons','dividers','qa']:
    p=ROOT/name
    if p.exists(): shutil.rmtree(p)
for p in ['logos/svg','logos/png','logos/webp','icons/svg','icons/png','icons/webp','dividers/svg','dividers/png','dividers/webp','qa']:
    (ROOT/p).mkdir(parents=True, exist_ok=True)

ROSE='#D6B0A0'; STEEL='#7B96B2'; PALE='#D0BEB0'

def defs():
    return f'''<defs><linearGradient id="metal" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="256" y2="256"><stop offset="0" stop-color="{STEEL}"/><stop offset="0.48" stop-color="{PALE}"/><stop offset="0.55" stop-color="{ROSE}"/><stop offset="1" stop-color="{STEEL}"/></linearGradient><linearGradient id="rose" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="800" y2="0"><stop offset="0" stop-color="#967878"/><stop offset="0.5" stop-color="{ROSE}"/><stop offset="1" stop-color="#967878"/></linearGradient><linearGradient id="steel" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="800" y2="0"><stop offset="0" stop-color="#516B86"/><stop offset="0.5" stop-color="{STEEL}"/><stop offset="1" stop-color="#516B86"/></linearGradient><filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>'''

def svg_icon(body,label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" role="img" aria-label="{label}">{defs()}<g fill="none" stroke="url(#metal)" stroke-width="12" stroke-linecap="round" stroke-linejoin="round">{body}</g></svg>'

def poly(points): return ' '.join(f'{x:.1f},{y:.1f}' for x,y in points)
def gear(cx=128,cy=128,r1=42,r2=58,teeth=10):
    pts=[]
    for i in range(teeth*4):
        a=math.pi*2*i/(teeth*4)-math.pi/2
        r=r2 if i%4 in (0,1) else r1
        pts.append((cx+math.cos(a)*r,cy+math.sin(a)*r))
    return poly(pts)

icons={
'security-shield-check':svg_icon('<path d="M128 28 202 56v55c0 52-29 91-74 117-45-26-74-65-74-117V56z"/><path d="m91 126 25 25 52-58"/>','Security shield check'),
'lighting-bulb':svg_icon('<path d="M87 112a41 41 0 1 1 82 0c0 20-10 31-22 43-8 8-11 15-11 27h-16c0-12-3-19-11-27-12-12-22-23-22-43z"/><path d="M108 182h40M112 202h32M128 28v18M62 66l14 14M194 66l-14 14M54 123h20M182 123h20"/>','Lighting bulb'),
'climate-thermostat':svg_icon('<circle cx="128" cy="128" r="82"/><circle cx="128" cy="128" r="61" stroke="url(#steel)"/><path d="M128 90v44"/><circle cx="128" cy="151" r="11" fill="url(#rose)" stroke="none"/><path d="M184 70l12-14M195 83l16-6"/>','Climate thermostat'),
'music-note':svg_icon('<path d="M105 176V72l82-18v104"/><ellipse cx="84" cy="183" rx="25" ry="17"/><ellipse cx="166" cy="165" rx="25" ry="17"/><path d="M105 91l82-18"/>','Music note'),
'shades-window':svg_icon('<rect x="51" y="45" width="154" height="166" rx="5"/><path d="M59 70h138M59 96h138M59 122h138M59 148h138M59 174h138"/><path d="M198 58v133"/><circle cx="198" cy="198" r="8" fill="url(#rose)" stroke="url(#metal)"/>','Window shades'),
'smart-lock':svg_icon('<rect x="72" y="36" width="112" height="184" rx="28"/><circle cx="128" cy="169" r="26"/><circle cx="101" cy="78" r="4" fill="url(#metal)" stroke="none"/><circle cx="128" cy="78" r="4" fill="url(#metal)" stroke="none"/><circle cx="155" cy="78" r="4" fill="url(#metal)" stroke="none"/><circle cx="101" cy="104" r="4" fill="url(#metal)" stroke="none"/><circle cx="128" cy="104" r="4" fill="url(#metal)" stroke="none"/><circle cx="155" cy="104" r="4" fill="url(#metal)" stroke="none"/>','Smart lock'),
'concierge-bell':svg_icon('<path d="M62 157h132"/><path d="M79 151c3-52 22-78 49-78s46 26 49 78"/><path d="M113 73h30M128 55V42"/><path d="M52 180h152"/>','Concierge bell'),
'installation-tools':svg_icon('<path d="M62 57c17-14 40-11 54 3l-28 28 23 23 28-28c14 14 17 37 3 54-15 18-42 22-61 9l-33 33 29 29 33-33c-13-19-9-46 9-61"/><path d="M151 71l45-45 18 18-45 45"/><path d="M45 183l28 28"/>','Installation tools'),
'support-headset':svg_icon('<path d="M57 135v-15a71 71 0 0 1 142 0v15"/><rect x="43" y="126" width="29" height="60" rx="13"/><rect x="184" y="126" width="29" height="60" rx="13"/><path d="M198 183c0 24-17 35-42 35h-14"/><rect x="111" y="206" width="35" height="17" rx="8"/>','Support headset'),
'automation-home-gear':svg_icon(f'<path d="M37 117 128 43l91 74"/><path d="M56 106v104h144V106"/><polygon points="{gear(132,147,25,38,10)}"/><circle cx="132" cy="147" r="14"/>','Automation home and gear'),
'energy-bolt':svg_icon('<circle cx="128" cy="128" r="88"/><path d="M145 36 84 139h45l-18 81 63-111h-45z" fill="url(#rose)" stroke="url(#metal)"/>','Energy bolt'),
'camera':svg_icon('<path d="M62 68h132v36c0 45-28 80-66 80s-66-35-66-80z"/><path d="M78 68V44h100v24"/><circle cx="128" cy="121" r="31"/><circle cx="128" cy="121" r="10" fill="url(#rose)" stroke="none"/>','Camera'),
'faq-chat':svg_icon('<path d="M47 60h162a19 19 0 0 1 19 19v83a19 19 0 0 1-19 19h-72l-40 31v-31H47a19 19 0 0 1-19-19V79a19 19 0 0 1 19-19z"/><path d="M103 109c2-18 14-28 29-28 17 0 30 10 30 25 0 17-17 21-25 31-4 5-5 9-5 15M132 169h.1"/>','FAQ chat bubble'),
'phone':svg_icon('<rect x="76" y="28" width="104" height="200" rx="24"/><path d="M111 50h34M111 205h34"/>','Phone'),
'calendar':svg_icon('<rect x="43" y="51" width="170" height="166" rx="15"/><path d="M43 91h170M82 33v35M174 33v35"/><rect x="72" y="119" width="22" height="22"/><rect x="117" y="119" width="22" height="22"/><rect x="162" y="119" width="22" height="22"/><rect x="72" y="161" width="22" height="22"/><rect x="117" y="161" width="22" height="22"/><rect x="162" y="161" width="22" height="22"/>','Calendar'),
'location-pin':svg_icon('<path d="M128 226s-62-61-62-118a62 62 0 1 1 124 0c0 57-62 118-62 118z"/><circle cx="128" cy="108" r="24"/><ellipse cx="128" cy="229" rx="59" ry="14" stroke="url(#steel)"/>','Location pin')}

def divider_svg(body,label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 100" role="img" aria-label="{label}">{defs()}<g fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</g></svg>'

divs={
'divider-steel':divider_svg('<path d="M35 50H765" stroke="url(#steel)" stroke-width="4"/>','Steel divider'),
'divider-rose':divider_svg('<path d="M35 50H765" stroke="url(#rose)" stroke-width="4"/>','Rose gold divider'),
'divider-dual':divider_svg('<path d="M35 50H765" stroke="url(#metal)" stroke-width="5"/>','Dual metallic divider'),
'divider-spark':divider_svg('<path d="M35 50H765" stroke="url(#rose)" stroke-width="3"/><path d="M400 14v72M374 50h52M386 36l28 28M414 36l-28 28" stroke="url(#metal)" stroke-width="4" filter="url(#glow)"/>','Spark divider'),
'divider-diamond':divider_svg('<path d="M35 50H350M450 50H765" stroke="url(#steel)" stroke-width="3"/><path d="m400 28 22 22-22 22-22-22z" stroke="url(#metal)" stroke-width="5"/>','Diamond divider'),
'divider-orbit':divider_svg('<path d="M35 50H310M490 50H765" stroke="url(#rose)" stroke-width="3"/><ellipse cx="400" cy="50" rx="83" ry="24" transform="rotate(-8 400 50)" stroke="url(#steel)" stroke-width="4"/><ellipse cx="400" cy="50" rx="70" ry="18" transform="rotate(11 400 50)" stroke="url(#rose)" stroke-width="3"/>','Orbit divider'),
'badge-underline-steel':divider_svg('<path d="M150 45H650" stroke="url(#steel)" stroke-width="4"/><path d="M400 20v50M382 45h36" stroke="url(#metal)" stroke-width="4"/>','Steel badge underline'),
'badge-underline-rose':divider_svg('<path d="M150 45H650" stroke="url(#rose)" stroke-width="4"/><path d="M400 20v50M382 45h36" stroke="url(#rose)" stroke-width="4"/>','Rose badge underline'),
'corner-steel':divider_svg('<path d="M55 88V28h60M55 28c24 0 38-14 38-28" stroke="url(#steel)" stroke-width="5"/>','Steel ornamental corner'),
'corner-rose':divider_svg('<path d="M55 88V28h60M55 28c24 0 38-14 38-28" stroke="url(#rose)" stroke-width="5"/><path d="M55 9v38M36 28h38" stroke="url(#metal)" stroke-width="3"/>','Rose ornamental corner'),
'orbit-stroke-steel':divider_svg('<ellipse cx="400" cy="50" rx="170" ry="26" transform="rotate(-7 400 50)" stroke="url(#steel)" stroke-width="5"/><path d="M560 23v25M548 35h25" stroke="url(#metal)" stroke-width="3"/>','Steel orbit stroke'),
'orbit-stroke-rose':divider_svg('<ellipse cx="400" cy="50" rx="170" ry="26" transform="rotate(7 400 50)" stroke="url(#rose)" stroke-width="5"/><path d="M240 22v27M227 35h26" stroke="url(#metal)" stroke-width="3"/>','Rose orbit stroke')}

def render(svg_text,out_png,out_webp,size):
    cairosvg.svg2png(bytestring=svg_text.encode(),write_to=str(out_png),output_width=size[0],output_height=size[1])
    Image.open(out_png).convert('RGBA').save(out_webp,'WEBP',quality=92,method=4)

for name,svg in icons.items():
    (ROOT/'icons/svg'/f'{name}.svg').write_text(svg)
    render(svg,ROOT/'icons/png'/f'{name}.png',ROOT/'icons/webp'/f'{name}.webp',(512,512))
for name,svg in divs.items():
    (ROOT/'dividers/svg'/f'{name}.svg').write_text(svg)
    render(svg,ROOT/'dividers/png'/f'{name}.png',ROOT/'dividers/webp'/f'{name}.webp',(1600,200))

logo_sources={'luxsync-horizontal-combo':REPO/'brand/source-logo/LuxSync_Logo_Horizontal_Combo.png','luxsync-horizontal':REPO/'brand/source-logo/LuxSync_Logo_Horizontal_Final.png','luxsync-orb':REPO/'brand/source-logo/LuxSync_Logo_Orb.png'}
for name,src in logo_sources.items():
    im=Image.open(src).convert('RGBA')
    shutil.copy2(src,ROOT/'logos/png'/f'{name}.png')
    im.save(ROOT/'logos/webp'/f'{name}.webp','WEBP',quality=95,method=6)
    data=base64.b64encode(src.read_bytes()).decode(); w,h=im.size
    (ROOT/'logos/svg'/f'{name}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="LuxSync logo"><image width="{w}" height="{h}" href="data:image/png;base64,{data}"/></svg>')

def make_contact(srcdir,names,out,columns,cell):
    rows=math.ceil(len(names)/columns); canvas=Image.new('RGBA',(columns*cell,rows*cell),(13,21,38,255)); draw=ImageDraw.Draw(canvas)
    for i,name in enumerate(names):
        im=Image.open(srcdir/f'{name}.png').convert('RGBA'); im.thumbnail((cell-40,cell-55),Image.LANCZOS)
        x=(i%columns)*cell+(cell-im.width)//2; y=(i//columns)*cell+12; canvas.alpha_composite(im,(x,y)); draw.text(((i%columns)*cell+8,(i//columns)*cell+cell-28),name,fill=(208,190,176,255))
    canvas.convert('RGB').save(out,quality=92)
make_contact(ROOT/'icons/png',list(icons),ROOT/'qa/icons-contact-sheet.jpg',4,220)
make_contact(ROOT/'dividers/png',list(divs),ROOT/'qa/dividers-contact-sheet.jpg',2,460)

manifest={'version':'6.0-clean-atomic-triple-format','brand':'LuxSync','formats':['svg','png','webp'],'assets':[]}
for category,names in [('logos',logo_sources.keys()),('icons',icons.keys()),('dividers',divs.keys())]:
    for name in names:
        ent={'id':name,'category':category,'production_status':'approved','qa_status':'passed','files':{}}
        for fmt in ['svg','png','webp']:
            p=ROOT/category/fmt/f'{name}.{fmt}'; ent['files'][fmt]={'path':str(p.relative_to(ROOT)).replace('\\','/'),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
        manifest['assets'].append(ent)
(ROOT/'asset-manifest.json').write_text(json.dumps(manifest,indent=2))
(ROOT/'README.md').write_text('''# LuxSync Clean Atomic Production Assets\n\n**Version:** 6.0 clean atomic triple-format\n**Official slogan:** Where Luxury Lives Intelligently\n\nThis directory is the only deployable LuxSync graphic asset library.\n\n- `logos/` contains exact protected artwork in SVG fidelity-container, PNG master and WebP delivery formats.\n- `icons/` contains clean semantic vector icons rebuilt as atomic artwork.\n- `dividers/` contains clean vector dividers, orbit strokes and ornamental accents.\n- `qa/` contains rendered contact sheets for visual review only.\n\nEvery production asset has matching SVG, PNG and WebP files with the same semantic basename. Buttons, forms, cards, navigation and other interactive UI remain live HTML/CSS rather than raster screenshots. The old numbered grid-sliced asset folders are retired. Protected logo lettering is never retyped or regenerated.\n''',encoding='utf-8')

replacements={'brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png':'brand/assets/logos/png/luxsync-horizontal-combo.png','brand/assets/01-logos/LuxSync_Logo_Horizontal_Final.png':'brand/assets/logos/png/luxsync-horizontal.png','brand/assets/01-logos/LuxSync_Logo_Orb.png':'brand/assets/logos/png/luxsync-orb.png','../../brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png':'../../brand/assets/logos/png/luxsync-horizontal-combo.png','../../brand/assets/01-logos/LuxSync_Logo_Horizontal_Final.png':'../../brand/assets/logos/png/luxsync-horizontal.png','../../brand/assets/01-logos/LuxSync_Logo_Orb.png':'../../brand/assets/logos/png/luxsync-orb.png','../../../brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png':'../../../brand/assets/logos/png/luxsync-horizontal-combo.png','../../../brand/assets/01-logos/LuxSync_Logo_Horizontal_Final.png':'../../../brand/assets/logos/png/luxsync-horizontal.png','../../../brand/assets/01-logos/LuxSync_Logo_Orb.png':'../../../brand/assets/logos/png/luxsync-orb.png'}
for path in REPO.rglob('*'):
    if not path.is_file() or path.suffix.lower() not in {'.md','.json','.js','.mjs','.py','.yml','.yaml','.html','.css'} or any(part in {'.git','node_modules','dist'} for part in path.parts) or path==Path(__file__): continue
    text=path.read_text(encoding='utf-8',errors='replace'); newtext=text
    for old,newp in replacements.items(): newtext=newtext.replace(old,newp)
    if newtext!=text: path.write_text(newtext,encoding='utf-8')
print(f'CLEAN_ASSET_BUILD_COMPLETE assets={len(manifest["assets"])} files={len(manifest["assets"])*3}')

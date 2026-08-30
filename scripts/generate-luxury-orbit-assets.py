#!/usr/bin/env python3
from pathlib import Path
from html import escape

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'brand'/'assets'
P={'navy':'#0D1526','blue':'#172036','blush':'#D0BEB0','taupe':'#9E8B85','rose':'#967878','powder':'#7B96B2','gold':'#D6B0A0','ink':'#090E1B'}
DISPLAY="font-family='Manrope,Arial,sans-serif'"
UI="font-family='Manrope,Arial,sans-serif'"
BODY="font-family='Inter,Arial,sans-serif'"
DEFS=f'''<defs><linearGradient id="n" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{P['navy']}"/><stop offset="1" stop-color="{P['ink']}"/></linearGradient><linearGradient id="m" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#FFF2EA"/><stop offset=".18" stop-color="#EAC8B9"/><stop offset=".42" stop-color="{P['gold']}"/><stop offset=".64" stop-color="#9C675C"/><stop offset=".82" stop-color="#F2D6C8"/><stop offset="1" stop-color="#7D4E49"/></linearGradient><linearGradient id="b" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#F4FAFF"/><stop offset=".45" stop-color="#D7E8FF"/><stop offset="1" stop-color="{P['powder']}"/></linearGradient><radialGradient id="w"><stop stop-color="#F9E3D7" stop-opacity=".95"/><stop offset=".45" stop-color="#E7A27D" stop-opacity=".45"/><stop offset="1" stop-color="#E7A27D" stop-opacity="0"/></radialGradient><filter id="g" x="-70%" y="-70%" width="240%" height="240%"><feGaussianBlur stdDeviation="13" result="q"/><feMerge><feMergeNode in="q"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>'''

def svg(w,h,body,bg=None,aria='LuxSync graphic'):
    back=f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(aria)}">{DEFS}{back}{body}</svg>'

def write(rel,text):
    p=OUT/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')

def label(name): return ' '.join(w.capitalize() for w in name.replace('luxsync-','').replace('.svg','').replace('-',' ').split())

def mono(cx,cy,s=1,disk=False):
    r=210*s; z=''
    if disk:z+=f'<circle cx="{cx}" cy="{cy}" r="{r*1.12}" fill="url(#n)" stroke="{P["gold"]}" stroke-opacity=".25" stroke-width="3"/>'
    z+=f'<g fill="none" stroke="url(#b)" filter="url(#g)"><ellipse cx="{cx}" cy="{cy}" rx="{245*s}" ry="{83*s}" transform="rotate(-12 {cx} {cy})" stroke-width="{9*s}"/><ellipse cx="{cx}" cy="{cy}" rx="{235*s}" ry="{76*s}" transform="rotate(17 {cx} {cy})" stroke-width="{3*s}" opacity=".55"/></g>'
    z+=f'<text x="{cx}" y="{cy+102*s}" text-anchor="middle" {DISPLAY} font-size="{315*s}" font-weight="600" letter-spacing="{-42*s}" fill="url(#m)" stroke="#7D4E49" stroke-width="{2.5*s}" paint-order="stroke fill">LS</text>'
    return z

def wordmark(y=0,light=False):
    c=P['blush'] if light else P['navy']; s=P['rose'] if light else P['navy']
    return f'<text x="800" y="{190+y}" text-anchor="middle" {DISPLAY} font-size="174" letter-spacing="22" fill="{c}">LUXSYNC</text><text x="800" y="{268+y}" text-anchor="middle" {BODY} font-size="36" fill="{s}">Where Luxury Lives Intelligently</text>'

# 01 brand
write('01-brand/luxsync-monogram-orb.svg',svg(1000,1000,mono(500,490,1.25),aria='LuxSync LS orbit monogram'))
write('01-brand/luxsync-favicon.svg',svg(512,512,mono(256,250,.56,True),aria='LuxSync favicon'))
write('01-brand/luxsync-horizontal-lockup.svg',svg(1600,500,mono(260,245,.52)+f'<text x="540" y="235" {DISPLAY} font-size="145" letter-spacing="17" fill="{P["navy"]}">LUXSYNC</text><text x="550" y="305" {BODY} font-size="34" fill="{P["navy"]}">Where Luxury Lives Intelligently</text>'))
write('01-brand/luxsync-stacked-lockup.svg',svg(1000,900,mono(500,300,.72)+f'<text x="500" y="650" text-anchor="middle" {DISPLAY} font-size="120" letter-spacing="14" fill="{P["navy"]}">LUXSYNC</text><text x="500" y="715" text-anchor="middle" {BODY} font-size="30" fill="{P["navy"]}">Where Luxury Lives Intelligently</text><path d="M260 785H430M570 785H740" stroke="{P["gold"]}" stroke-width="3"/><path d="M500 763l11 22 22 11-22 11-11 22-11-22-22-11 22-11z" fill="{P["gold"]}"/>'))
write('01-brand/luxsync-wordmark-dark.svg',svg(1600,420,wordmark(0,False)))
write('01-brand/luxsync-wordmark-light.svg',svg(1600,420,wordmark(0,True)))
write('01-brand/luxsync-divider.svg',svg(1600,260,f'<path d="M35 156C300 22 500 235 810 120S1320 215 1565 84" fill="none" stroke="url(#m)" stroke-width="13" stroke-linecap="round"/><path d="M65 176C340 70 545 224 820 133S1330 192 1540 108" fill="none" stroke="{P["powder"]}" stroke-width="4" opacity=".45"/>'))
write('01-brand/luxsync-hero-card.svg',svg(1200,1200,f'<rect x="65" y="65" width="1070" height="1070" rx="88" fill="url(#n)" stroke="{P["gold"]}" stroke-opacity=".3" stroke-width="3"/>{mono(600,420,.9)}<text x="600" y="820" text-anchor="middle" {DISPLAY} font-size="145" letter-spacing="18" fill="{P["blush"]}">LUXSYNC</text><text x="600" y="900" text-anchor="middle" {BODY} font-size="38" fill="{P["rose"]}">Where Luxury Lives Intelligently</text>'))

# 02+03 icons
brand_icons=['ambient-glow','breathing-space','check','close','corner-radius','effortless-sophistication','intelligent-calm','layered-depth','organic-motion','soft-border','tactile-luxury','warm-futurism']
web_icons=['arrow-right','cart','chevron-down','delivery','heart','lock','phone','search','security','smart-home','star','support','user','value']
glyphs={'ambient-glow':'◉','breathing-space':'□','check':'✓','close':'×','corner-radius':'⌜','effortless-sophistication':'∿','intelligent-calm':'≋','layered-depth':'▱','organic-motion':'⌁','soft-border':'▢','tactile-luxury':'✦','warm-futurism':'◎','arrow-right':'→','cart':'🛒','chevron-down':'⌄','delivery':'▣','heart':'♡','lock':'▤','phone':'☎','search':'⌕','security':'✓','smart-home':'⌂','star':'☆','support':'◉','user':'♙','value':'$'}
for cat,names in [('02-icons-brand',brand_icons),('03-icons-website',web_icons)]:
    for n in names:
        g=glyphs[n]
        body=f'<circle cx="256" cy="256" r="170" fill="none" stroke="url(#m)" stroke-width="9" opacity=".24"/><text x="256" y="318" text-anchor="middle" {UI} font-size="190" fill="url(#m)">{escape(g)}</text>'
        write(f'{cat}/{n}.svg',svg(512,512,body,aria=f'LuxSync {label(n)} icon'))

# 04 social
for n,g in {'facebook':'f','instagram':'◎','linkedin':'in','pinterest':'p','x':'X','youtube':'▶'}.items():
    body=f'<circle cx="256" cy="256" r="202" fill="url(#n)" stroke="url(#m)" stroke-width="17"/><text x="256" y="320" text-anchor="middle" {UI} font-size="170" font-weight="600" fill="url(#m)">{g}</text>'
    write(f'04-icons-social/{n}.svg',svg(512,512,body))

# 05 palette
swatches={'antique-rose-taupe':('DUSTY ROSE',P['rose']),'dark-suede':('MIDNIGHT BLUE',P['blue']),'dusty-steel':('SOFT POWDER BLUE',P['powder']),'pale-driftwood':('PALE BLUSH',P['blush']),'slate-navy':('DEEP NAVY',P['navy']),'warm-taupe-mauve':('TAUPE',P['taupe'])}
for n,(t,c) in swatches.items():
    write(f'05-palette/{n}.svg',svg(720,480,f'<rect x="34" y="34" width="652" height="410" rx="44" fill="{c}"/><rect x="34" y="320" width="652" height="124" fill="{P["blush"]}"/><text x="70" y="370" {UI} font-size="34" fill="{P["navy"]}">{t}</text><text x="70" y="414" {BODY} font-size="28" fill="{P["navy"]}">{c}</text>'))
x=40; body=''
for t,c in [('DEEP NAVY',P['navy']),('MIDNIGHT BLUE',P['blue']),('PALE BLUSH',P['blush']),('TAUPE',P['taupe']),('DUSTY ROSE',P['rose']),('POWDER BLUE',P['powder'])]:
    body+=f'<rect x="{x}" y="45" width="240" height="160" rx="32" fill="{c}"/><text x="{x+120}" y="252" text-anchor="middle" {UI} font-size="21" fill="{P["navy"]}">{t}</text><text x="{x+120}" y="282" text-anchor="middle" {BODY} font-size="19" fill="{P["navy"]}">{c}</text>';x+=258
write('05-palette/plush-drift-palette-strip.svg',svg(1600,330,body,bg='#FFFFFF'))
write('05-palette/suede-texture-tile.svg',svg(900,900,f'<rect width="900" height="900" fill="url(#n)"/><path d="M0 780C250 610 480 910 900 620" fill="none" stroke="url(#m)" stroke-width="14" opacity=".22"/>'))

# 06 gradients
for n,body in {'navy-drift':f'<rect width="1600" height="900" fill="url(#n)"/><circle cx="1250" cy="260" r="330" fill="url(#w)" opacity=".18"/>','rose-drift':f'<rect width="1600" height="900" fill="{P["blush"]}"/><circle cx="1120" cy="430" r="390" fill="url(#w)" opacity=".6"/><path d="M-80 760C300 400 700 950 1660 370" fill="none" stroke="url(#m)" stroke-width="24" opacity=".3"/>','warm-veil':f'<rect width="1600" height="900" fill="{P["blush"]}"/><circle cx="520" cy="470" r="620" fill="{P["rose"]}" opacity=".22"/>','lavender-mist':f'<rect width="1600" height="900" fill="#EDF3FB"/><circle cx="1080" cy="420" r="560" fill="{P["powder"]}" opacity=".44"/><circle cx="620" cy="590" r="390" fill="{P["rose"]}" opacity=".2"/>'}.items():write(f'06-gradients/{n}.svg',svg(1600,900,body))

# 07 components
components=['badge-curated','badge-host-ready','badge-luxsync-pick','badge-no-subscription','button-outline','button-primary','button-secondary','notification-card','pagination','quantity-selector','quote-card','scene-tag','search-field','sort-control','toggle-off','toggle-on','trust-bar']
for n in components:
    t=label(n).upper(); w,h=1000,360
    if n.startswith('badge'): w,h=800,320
    if n in ('notification-card','quote-card'):w,h=1000,520
    if n=='trust-bar':w,h=1600,280
    if n.startswith('toggle'):w,h=600,300
    if n=='search-field':w,h=1200,320
    if n=='pagination':w,h=1200,320
    if n=='scene-tag':w,h=700,280
    dark=not (n=='button-secondary' or n=='button-outline' or n=='scene-tag')
    fill='url(#n)' if dark else P['blush']; tc=P['blush'] if dark else P['navy']
    if n=='button-outline': fill='none'
    body=f'<rect x="{w*.1}" y="{h*.24}" width="{w*.8}" height="{h*.52}" rx="{min(w,h)*.11}" fill="{fill}" stroke="{P["gold"]}" stroke-width="4"/><text x="{w/2}" y="{h*.57}" text-anchor="middle" {UI} font-size="{min(w,h)*.12}" font-weight="600" fill="{tc}">{escape(t)}</text>'
    if n=='quantity-selector':body=f'<rect x="100" y="80" width="700" height="150" rx="34" fill="url(#n)" stroke="{P["gold"]}" stroke-width="3"/><text x="220" y="182" text-anchor="middle" {UI} font-size="56" fill="{P["gold"]}">−</text><text x="450" y="182" text-anchor="middle" {UI} font-size="56" fill="{P["blush"]}">1</text><text x="680" y="182" text-anchor="middle" {UI} font-size="56" fill="{P["gold"]}">+</text>'
    elif n=='search-field':body=f'<rect x="70" y="82" width="1060" height="150" rx="34" fill="url(#n)" stroke="{P["gold"]}" stroke-width="3"/><text x="130" y="178" {BODY} font-size="43" fill="{P["powder"]}" opacity=".72">Search products...</text><text x="1040" y="180" text-anchor="middle" {UI} font-size="60" fill="{P["gold"]}">⌕</text>'
    elif n=='sort-control':body=f'<rect x="70" y="82" width="860" height="150" rx="34" fill="url(#n)" stroke="{P["gold"]}" stroke-width="3"/><text x="130" y="178" {UI} font-size="40" fill="{P["gold"]}">Sort by:</text><text x="300" y="178" {UI} font-size="40" fill="{P["blush"]}">Featured</text><text x="855" y="177" {UI} font-size="48" fill="{P["gold"]}">⌄</text>'
    elif n=='pagination':body=f'<rect x="110" y="86" width="980" height="144" rx="34" fill="url(#n)" stroke="{P["gold"]}" stroke-width="3"/><rect x="250" y="96" width="110" height="124" rx="24" fill="url(#m)"/><text x="305" y="178" text-anchor="middle" {UI} font-size="43" fill="{P["navy"]}">1</text><text x="475" y="178" text-anchor="middle" {UI} font-size="43" fill="{P["blush"]}">2</text><text x="625" y="178" text-anchor="middle" {UI} font-size="43" fill="{P["blush"]}">3</text><text x="805" y="178" text-anchor="middle" {UI} font-size="43" fill="{P["gold"]}">•••</text><text x="965" y="178" text-anchor="middle" {UI} font-size="43" fill="{P["blush"]}">10</text>'
    elif n.startswith('toggle'):body=f'<rect x="100" y="90" width="400" height="120" rx="60" fill="{P["blue"] if n.endswith("on") else P["taupe"]}" opacity="{1 if n.endswith("on") else .55}"/><circle cx="{428 if n.endswith("on") else 172}" cy="150" r="48" fill="url(#m)"/>'
    elif n=='trust-bar':body=f'<rect x="40" y="70" width="1520" height="140" rx="34" fill="{P["blush"]}" stroke="{P["taupe"]}" stroke-opacity=".5"/><text x="180" y="158" {UI} font-size="29" fill="{P["navy"]}">☆ Trusted Brands</text><text x="520" y="158" {UI} font-size="29" fill="{P["navy"]}">▣ Secure Checkout</text><text x="890" y="158" {UI} font-size="29" fill="{P["navy"]}">$ 30-Day Returns</text><text x="1230" y="158" {UI} font-size="29" fill="{P["navy"]}">◉ AI Expert Support</text>'
    write(f'07-components/{n}.svg',svg(w,h,body))

# 08 cards
cards=['always-do','diagnostic-matrix','effortless-sophistication-card','intelligent-calm-card','manifesto-card','never-do','never-sounds-like','sounds-like','tactile-luxury-card','tone-calibration','type-specimen-body','type-specimen-display','warm-futurism-card']
for i,n in enumerate(cards):
    t=label(n); dark=i%2==0; bg='url(#n)' if dark else P['blush']; tc=P['blush'] if dark else P['navy']; sc=P['powder'] if dark else P['taupe']
    body=f'<rect x="65" y="55" width="870" height="590" rx="56" fill="{bg}" stroke="{P["gold"]}" stroke-opacity=".5" stroke-width="3"/><circle cx="170" cy="165" r="58" fill="url(#m)"/><text x="170" y="188" text-anchor="middle" {DISPLAY} font-size="58" fill="{P["navy"]}">✦</text><text x="130" y="310" {DISPLAY} font-size="58" fill="{tc}">{escape(t)}</text><text x="130" y="380" {BODY} font-size="31" fill="{sc}">Luxury, clarity, comfort, and intelligent calm.</text><path d="M130 520C330 420 540 580 870 420" fill="none" stroke="url(#m)" stroke-width="13" opacity=".55"/>'
    write(f'08-cards/{n}.svg',svg(1000,700,body))

# 09 illustrations
ills=['ambient-glow-example','dashboard-tablet','floating-widgets','forbidden-light-example','layered-depth-stack','luxury-smart-hub','organic-motion-curve']
for i,n in enumerate(ills):
    t=label(n); bg='url(#n)' if n!='organic-motion-curve' and n!='forbidden-light-example' else P['blush']
    body=f'<rect width="1200" height="800" fill="{bg}"/><circle cx="850" cy="350" r="205" fill="url(#w)" opacity=".65"/><path d="M80 650C320 320 640 820 1190 300" fill="none" stroke="url(#m)" stroke-width="19" opacity=".55"/><text x="100" y="170" {DISPLAY} font-size="72" fill="{P["blush"] if bg=="url(#n)" else P["navy"]}">{escape(t)}</text>{mono(850,350,.42,False) if n in ("dashboard-tablet","luxury-smart-hub") else ""}'
    write(f'09-illustrations/{n}.svg',svg(1200,800,body))

# 10 product cards
prod={'category-comfort':('Comfort &amp; Lighting','$79+','◉'),'category-energy':('Energy &amp; Control','$24+','◫'),'category-hosting':('Hosting Essentials','$139+','⌂'),'category-security':('Security &amp; Access','$139+','▣')}
for n,(t,price,g) in prod.items():
    body=f'<rect x="34" y="34" width="732" height="1032" rx="54" fill="url(#n)" stroke="{P["gold"]}" stroke-opacity=".45" stroke-width="3"/><circle cx="400" cy="320" r="178" fill="url(#w)"/><text x="400" y="390" text-anchor="middle" {UI} font-size="210" fill="url(#m)">{g}</text><path d="M80 540C260 370 450 620 740 350" fill="none" stroke="url(#m)" stroke-width="13" opacity=".42"/><text x="90" y="720" {UI} font-size="46" fill="{P["blush"]}">{t}</text><text x="90" y="790" {BODY} font-size="40" fill="{P["gold"]}">{price}</text><text x="90" y="850" {BODY} font-size="32" fill="{P["gold"]}">★★★★★</text><rect x="90" y="910" width="620" height="104" rx="30" fill="url(#m)"/><text x="400" y="980" text-anchor="middle" {UI} font-size="32" fill="{P["navy"]}">SHOP CATEGORY</text>'
    write(f'10-product-cards/{n}.svg',svg(800,1100,body))

# 11 banners
def waves():return f'<path d="M690 560C930 320 1130 710 1590 330" fill="none" stroke="url(#m)" stroke-width="14" opacity=".42"/><path d="M760 610C980 390 1220 720 1600 410" fill="none" stroke="{P["gold"]}" stroke-width="4" opacity=".35"/>'
write('11-banners/hero-where-luxury-lives-intelligently.svg',svg(1600,700,f'<rect width="1600" height="700" rx="46" fill="url(#n)"/>{waves()}<text x="110" y="160" {UI} font-size="88" font-weight="600" fill="{P["gold"]}">Smart Living.</text><text x="110" y="258" {UI} font-size="88" font-weight="600" fill="{P["gold"]}">Elevated.</text><text x="115" y="330" {BODY} font-size="33" fill="{P["blush"]}">Luxury smart-home technology designed for modern living.</text><rect x="115" y="390" width="300" height="86" rx="26" fill="url(#m)"/><text x="265" y="446" text-anchor="middle" {UI} font-size="27" fill="{P["navy"]}">SHOP SMART HOME</text>{mono(1240,300,.55,True)}'))
write('11-banners/hero-technology-feels-like-home.svg',svg(1600,700,f'<rect width="1600" height="700" rx="46" fill="url(#n)"/>{waves()}<text x="110" y="190" {DISPLAY} font-size="82" fill="{P["blush"]}">Technology that feels</text><text x="110" y="285" {DISPLAY} font-size="82" fill="{P["gold"]}">like home.</text><text x="115" y="360" {BODY} font-size="33" fill="{P["powder"]}">Quiet intelligence. Beautifully integrated.</text>{mono(1240,310,.58,False)}'))
write('11-banners/shop-curated-smart-living.svg',svg(1600,600,f'<rect width="1600" height="600" rx="46" fill="url(#n)"/>{waves()}<text x="100" y="165" {UI} font-size="52" fill="{P["blush"]}">Luxury smart home hardware,</text><text x="100" y="230" {UI} font-size="52" fill="{P["gold"]}">curated for modern living.</text><rect x="105" y="300" width="240" height="82" rx="26" fill="url(#m)"/><text x="225" y="353" text-anchor="middle" {UI} font-size="27" fill="{P["navy"]}">SHOP NOW</text><rect x="760" y="200" width="160" height="265" rx="50" fill="#292C35" stroke="url(#m)" stroke-width="6"/><rect x="955" y="230" width="250" height="220" rx="52" fill="#F5EFEA"/><rect x="1240" y="280" width="90" height="150" rx="28" fill="#F5EFEA"/><rect x="1360" y="230" width="160" height="220" rx="38" fill="#111521" stroke="{P["gold"]}" stroke-width="4"/>'))
write('11-banners/str-smart-home-roi-guide.svg',svg(1600,600,f'<rect width="1600" height="600" rx="46" fill="url(#n)"/>{waves()}<g transform="translate(90 92) rotate(-7 250 210)"><rect width="500" height="420" rx="18" fill="{P["blush"]}"/><text x="54" y="92" {UI} font-size="34" fill="{P["navy"]}">SMART HOME</text><text x="54" y="156" {DISPLAY} font-size="68" fill="{P["navy"]}">ROI GUIDE</text><path d="M0 330C140 270 290 390 500 290" fill="none" stroke="url(#m)" stroke-width="18" opacity=".7"/></g><text x="680" y="190" {UI} font-size="60" font-weight="600" fill="{P["blush"]}">Free STR Smart Home ROI Guide</text><text x="685" y="265" {BODY} font-size="33" fill="{P["powder"]}">Unlock higher occupancy, smoother stays, and measurable ROI.</text><rect x="685" y="330" width="360" height="86" rx="26" fill="url(#m)"/><text x="865" y="386" text-anchor="middle" {UI} font-size="27" fill="{P["navy"]}">GET YOUR FREE GUIDE</text>'))

print('Generated',len(list(OUT.rglob('*.svg'))),'Luxury Orbit SVG masters')

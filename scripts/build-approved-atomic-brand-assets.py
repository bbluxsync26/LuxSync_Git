#!/usr/bin/env python3
"""Build the approved LuxSync atomic SVG asset library from the locked brand rules."""
from pathlib import Path
import json, shutil

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "brand" / "assets"
V3 = ROOT / "brand" / "assets-v3"
INSTALL = ROOT / ".atomic-installer"

if ASSETS.exists():
    shutil.rmtree(ASSETS)
if V3.exists():
    shutil.rmtree(V3)
ASSETS.mkdir(parents=True, exist_ok=True)

C = {
    "navy":"#0D1526", "suede":"#172036", "drift":"#D0BEB0",
    "taupe":"#9E8B85", "rose":"#967878", "steel":"#7B96B2",
    "champagne":"#D6B0A0"
}

DEFS = f'''<defs>
<linearGradient id="steel" x1="0" x2="1"><stop offset="0" stop-color="{C['suede']}"/><stop offset=".28" stop-color="{C['steel']}"/><stop offset=".5" stop-color="{C['drift']}"/><stop offset=".72" stop-color="{C['steel']}"/><stop offset="1" stop-color="{C['suede']}"/></linearGradient>
<linearGradient id="rose" x1="0" x2="1"><stop offset="0" stop-color="{C['rose']}"/><stop offset=".28" stop-color="{C['champagne']}"/><stop offset=".5" stop-color="{C['drift']}"/><stop offset=".72" stop-color="{C['champagne']}"/><stop offset="1" stop-color="{C['rose']}"/></linearGradient>
<radialGradient id="glow"><stop offset="0" stop-color="{C['steel']}" stop-opacity=".44"/><stop offset="1" stop-color="{C['navy']}" stop-opacity="0"/></radialGradient>
</defs>'''

def write(rel, text):
    p = ASSETS / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")

def svg(w, h, body, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">{DEFS}{body}</svg>\n'

def text(x,y,s,size=22,fill=None,weight=600,anchor="middle"):
    fill = fill or C['drift']
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Manrope,Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{s}</text>'

def line_icon(name):
    common=f'fill="none" stroke="{C["steel"]}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"'
    accent=f'fill="none" stroke="{C["champagne"]}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"'
    shapes={
      'home':f'<path {common} d="M28 88 100 28l72 60v82H52V88"/><path {accent} d="M78 170v-48h44v48"/>',
      'light-bulb':f'<path {common} d="M65 105c-18-13-27-30-27-50 0-35 28-55 62-55s62 20 62 55c0 20-9 37-27 50-10 8-14 18-14 31H79c0-13-4-23-14-31Z"/><path {accent} d="M80 151h40M86 170h28"/>',
      'thermostat':f'<rect {common} x="42" y="25" width="116" height="150" rx="26"/><circle {accent} cx="100" cy="100" r="31"/><path {common} d="M100 100V72m0 28 20 14"/>',
      'security-shield':f'<path {common} d="M100 18 160 42v52c0 42-25 68-60 88-35-20-60-46-60-88V42Z"/><path {accent} d="m72 99 19 19 39-43"/>',
      'security-camera':f'<rect {common} x="25" y="55" width="118" height="78" rx="17"/><circle {accent} cx="84" cy="94" r="24"/><path {common} d="m143 78 32-17v66l-32-17"/>',
      'smart-lock':f'<rect {common} x="48" y="78" width="104" height="94" rx="18"/><path {common} d="M70 78V57c0-39 60-39 60 0v21"/><circle {accent} cx="100" cy="119" r="10"/><path {accent} d="M100 129v20"/>',
      'smart-speaker':f'<rect {common} x="58" y="25" width="84" height="150" rx="36"/><circle {accent} cx="100" cy="75" r="19"/><path {common} d="M78 129h44m-36 21h28"/>',
      'wifi':f'<path {common} d="M25 75c43-38 107-38 150 0M49 103c29-25 73-25 102 0M74 131c15-12 37-12 52 0"/><circle fill="{C["champagne"]}" cx="100" cy="157" r="9"/>',
      'monitor':f'<rect {common} x="22" y="35" width="156" height="105" rx="14"/><path {accent} d="M75 170h50m-25-30v30"/>',
      'smartphone':f'<rect {common} x="58" y="18" width="84" height="164" rx="18"/><path {accent} d="M86 39h28M91 159h18"/>',
      'analytics-bars':f'<path {common} d="M35 170V95h27v75m25 0V58h27v112m25 0V25h27v145"/><path {accent} d="M25 170h150"/>',
      'clock':f'<circle {common} cx="100" cy="100" r="76"/><path {accent} d="M100 55v48l34 22"/>',
      'settings-gear':f'<circle {accent} cx="100" cy="100" r="26"/><path {common} d="M100 20v22m0 116v22M20 100h22m116 0h22M44 44l16 16m80 80 16 16M156 44l-16 16m-80 80-16 16"/><circle {common} cx="100" cy="100" r="57"/>',
      'automation-lightning':f'<path {common} d="M111 15 48 107h47l-9 78 66-102h-48Z"/><path {accent} d="M31 36h31M138 164h31"/>',
      'efficiency-leaf':f'<path {common} d="M171 31C99 27 43 58 32 116c-8 44 30 69 67 55 53-20 69-76 72-140Z"/><path {accent} d="M57 151c25-42 54-68 89-89"/>'
    }
    return svg(200,200,f'<rect width="200" height="200" rx="36" fill="{C["navy"]}"/>{shapes[name]}',f'LuxSync {name} icon')

# Exact authoritative logo wrappers. The PNG masters themselves remain untouched.
logo_specs={
 'LuxSync_Logo_Horizontal_Combo.svg':('../../source-logo/LuxSync_Logo_Horizontal_Combo.png',2048,768,'LuxSync combined horizontal logo'),
 'LuxSync_Logo_Horizontal_Final.svg':('../../source-logo/LuxSync_Logo_Horizontal_Final.png',2048,768,'LuxSync horizontal wordmark logo'),
 'LuxSync_Logo_Orb.svg':('../../source-logo/LuxSync_Logo_Orb.png',1254,1254,'LuxSync LS orb logo')}
for fn,(href,w,h,label) in logo_specs.items():
    write('01-logos/'+fn, f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}"><image href="{href}" x="0" y="0" width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet"/></svg>\n')

icons=['home','light-bulb','thermostat','security-shield','security-camera','smart-lock','smart-speaker','wifi','monitor','smartphone','analytics-bars','clock','settings-gear','automation-lightning','efficiency-leaf']
for n in icons: write(f'02-icons/{n}.svg', line_icon(n))

# Buttons and CTA states.
def button(label, mode='rose', disabled=False, icon=''):
    bg='url(#rose)' if mode=='rose' else ('url(#steel)' if mode=='steel' else C['suede'])
    stroke=C['steel'] if mode=='outline' else C['champagne']
    opacity='.42' if disabled else '1'
    body=f'<rect width="420" height="96" rx="48" fill="{bg}" stroke="{stroke}" stroke-width="3" opacity="{opacity}"/>'
    if icon: body+=f'<circle cx="58" cy="48" r="20" fill="none" stroke="{C["drift"]}" stroke-width="4"/>'
    body+=text(220,60,label,22,C['navy'] if mode in ('rose','steel') else C['drift'])
    return svg(420,96,body,f'LuxSync {label} button')
buttons={
 'primary-shop-now':('SHOP NOW','rose',False,''), 'secondary-learn-more':('LEARN MORE','steel',False,''),
 'tertiary-view-details':('VIEW DETAILS','outline',False,''), 'filled-secondary-discover-smart-living':('DISCOVER SMART LIVING','steel',False,''),
 'outline-book-a-call':('BOOK A CALL','outline',False,''), 'utility-add-to-cart':('ADD TO CART','rose',False,''),
 'state-default':('DEFAULT','outline',False,''), 'state-hover':('HOVER','steel',False,''),
 'state-pressed':('PRESSED','rose',False,''), 'state-disabled':('DISABLED','outline',True,'')}
for n,args in buttons.items(): write(f'03-buttons/{n}.svg',button(*args))
for n,glyph in [('cart','CART'),('favorite-heart','♡'),('account','USER'),('search','⌕'),('phone','TEL'),('email','MAIL'),('share','↗'),('menu','MENU')]:
    b=f'<circle cx="50" cy="50" r="46" fill="{C["suede"]}" stroke="url(#steel)" stroke-width="4"/>'+text(50,58,glyph,15,C['drift'])
    write(f'03-buttons/icon-{n}.svg',svg(100,100,b,f'LuxSync {n} icon button'))

# UI controls.
ui={}
ui['toggle-off']=f'<rect x="8" y="22" width="104" height="52" rx="26" fill="{C["suede"]}" stroke="{C["steel"]}" stroke-width="3"/><circle cx="36" cy="48" r="20" fill="{C["taupe"]}"/>'
ui['toggle-on']=f'<rect x="8" y="22" width="104" height="52" rx="26" fill="url(#steel)"/><circle cx="84" cy="48" r="20" fill="{C["navy"]}"/>'
ui['checkbox-unchecked']=f'<rect x="25" y="25" width="50" height="50" rx="8" fill="{C["suede"]}" stroke="{C["steel"]}" stroke-width="4"/>'
ui['checkbox-checked']=ui['checkbox-unchecked']+f'<path d="m36 51 10 11 22-26" fill="none" stroke="{C["champagne"]}" stroke-width="6" stroke-linecap="round"/>'
ui['radio-unselected']=f'<circle cx="50" cy="50" r="24" fill="{C["suede"]}" stroke="{C["steel"]}" stroke-width="4"/>'
ui['radio-selected']=ui['radio-unselected']+f'<circle cx="50" cy="50" r="12" fill="{C["champagne"]}"/>'
ui['slider']=f'<rect x="15" y="46" width="270" height="8" rx="4" fill="{C["taupe"]}"/><rect x="15" y="46" width="170" height="8" rx="4" fill="url(#steel)"/><circle cx="185" cy="50" r="18" fill="{C["champagne"]}"/>'
ui['select-dropdown-open']=f'<rect x="5" y="5" width="290" height="190" rx="18" fill="{C["suede"]}" stroke="{C["steel"]}"/>'+text(28,42,'SELECT',17,C['drift'],600,'start')+text(28,82,'Option One',16,C['drift'],500,'start')+text(28,118,'Option Two',16,C['taupe'],500,'start')+text(28,154,'Option Three',16,C['taupe'],500,'start')
ui['quantity-selector']=f'<rect x="5" y="20" width="190" height="60" rx="30" fill="{C["suede"]}" stroke="{C["steel"]}"/>'+text(42,59,'−',24)+text(100,59,'1',20)+text(158,59,'+',24)
ui['search-bar']=f'<rect x="5" y="20" width="330" height="60" rx="30" fill="{C["suede"]}" stroke="{C["steel"]}"/>'+text(35,58,'⌕',24,C['champagne'])+text(68,57,'Search',17,C['taupe'],500,'start')
ui['sort-dropdown']=f'<rect x="5" y="20" width="210" height="60" rx="20" fill="{C["suede"]}" stroke="{C["steel"]}"/>'+text(28,58,'Sort: Featured',16,C['drift'],500,'start')
ui['filter-button']=f'<rect x="5" y="20" width="130" height="60" rx="30" fill="{C["suede"]}" stroke="{C["champagne"]}"/>'+text(70,58,'FILTER',16)
ui['pagination']=''.join(f'<circle cx="{35+i*52}" cy="50" r="20" fill="{C["steel"] if i==1 else C["suede"]}" stroke="{C["steel"]}"/>'+text(35+i*52,57,str(i+1),15,C['navy'] if i==1 else C['drift']) for i in range(5))
ui['primary-button']=button('PRIMARY','rose')
ui['secondary-button']=button('SECONDARY','steel')
ui['tertiary-button']=button('TERTIARY','outline')
ui['text-link']=text(100,58,'TEXT LINK →',18,C['steel'])
ui['icon-heart']=f'<circle cx="50" cy="50" r="42" fill="{C["suede"]}" stroke="{C["steel"]}"/><path d="M50 69 29 49c-16-15 8-35 21-18 13-17 37 3 21 18Z" fill="none" stroke="{C["champagne"]}" stroke-width="4"/>'
ui['icon-cart']=f'<circle cx="50" cy="50" r="42" fill="{C["suede"]}" stroke="{C["steel"]}"/><path d="M27 31h10l7 29h25l8-21H40" fill="none" stroke="{C["champagne"]}" stroke-width="4"/><circle cx="48" cy="69" r="4" fill="{C["steel"]}"/><circle cx="68" cy="69" r="4" fill="{C["steel"]}"/>'
ui['icon-arrow']=f'<circle cx="50" cy="50" r="42" fill="{C["suede"]}" stroke="{C["steel"]}"/><path d="M30 50h38m-13-13 13 13-13 13" fill="none" stroke="{C["champagne"]}" stroke-width="4"/>'
ui['badge-new']=f'<rect x="5" y="20" width="125" height="54" rx="27" fill="url(#rose)"/>'+text(68,56,'NEW',16,C['navy'])
ui['accent-line-spark']=f'<path d="M5 50h290" stroke="url(#rose)" stroke-width="4"/><path d="M150 28v44M128 50h44" stroke="{C["drift"]}" stroke-width="3"/>'
ui['accent-diamond']=f'<path d="m50 15 35 35-35 35-35-35Z" fill="none" stroke="url(#rose)" stroke-width="5"/>'
ui['accent-line-star']=f'<path d="M5 50h290" stroke="url(#steel)" stroke-width="4"/><path d="m150 28 7 15 16 7-16 7-7 15-7-15-16-7 16-7Z" fill="{C["champagne"]}"/>'
ui['accent-brushed-steel']=f'<rect x="5" y="35" width="290" height="30" rx="15" fill="url(#steel)"/>'
for n,b in ui.items():
    if b.startswith('<svg'): write(f'04-ui-controls/{n}.svg',b)
    else: write(f'04-ui-controls/{n}.svg',svg(340 if n in ('search-bar','pagination') else 300 if n.startswith('accent') or n=='slider' else 220 if n in ('select-dropdown-open','sort-dropdown') else 140 if n in ('filter-button','badge-new') else 120 if n.startswith('toggle') else 100,b,f'LuxSync {n} UI control'))

# Dividers and accents: 44 standalone objects.
def divider(body,label,w=800,h=80): return svg(w,h,body,label)
for i,(stroke,width,dash) in enumerate([(C['steel'],2,''),(C['champagne'],2,''),(C['taupe'],1,'8 10')],1):
    write(f'05-dividers-accents/thin-divider-{i:02d}.svg',divider(f'<path d="M10 40h780" stroke="{stroke}" stroke-width="{width}" stroke-dasharray="{dash}"/>',f'LuxSync thin divider {i}'))
for n,grad,h in [('gradient-rose-wide','rose',8),('gradient-steel-wide','steel',8),('gradient-rose-thin','rose',3),('gradient-steel-thin','steel',3)]:
    write(f'05-dividers-accents/{n}.svg',divider(f'<path d="M10 40h780" stroke="url(#{grad})" stroke-width="{h}" stroke-linecap="round"/>',f'LuxSync {n}'))
for n,color,dash in [('accent-rule-rose',C['champagne'],''),('accent-rule-dusty-steel',C['steel'],''),('accent-rule-rose-dotted',C['champagne'],'4 12'),('accent-rule-steel-dotted',C['steel'],'4 12')]:
    write(f'05-dividers-accents/{n}.svg',divider(f'<path d="M10 40h780" stroke="{color}" stroke-width="4" stroke-dasharray="{dash}" stroke-linecap="round"/>',f'LuxSync {n}'))
for i in range(1,13):
    r=10+(i%4)*4; body=f'<path d="M50 {50-r}v{2*r}M{50-r} 50h{2*r}" stroke="{C["champagne"] if i%2 else C["steel"]}" stroke-width="3"/><circle cx="50" cy="50" r="3" fill="{C["drift"]}"/>'
    write(f'05-dividers-accents/sparkle-{i:02d}.svg',svg(100,100,body,f'LuxSync sparkle {i}'))
write('05-dividers-accents/brushed-dusty-steel-wide.svg',divider('<rect x="10" y="24" width="780" height="32" rx="16" fill="url(#steel)"/>','LuxSync Brushed Dusty Steel accent'))
for i in range(1,7):
    body=f'<path d="M20 50h40M140 50h40" stroke="{C["steel"]}" stroke-width="3"/><path d="m100 {20+i*2} {18+i} {28-i*2}-{18+i} {28-i*2}-{18+i}-{28-i*2}Z" fill="none" stroke="{C["champagne"]}" stroke-width="3"/>'
    write(f'05-dividers-accents/ornament-{i:02d}.svg',svg(200,100,body,f'LuxSync ornament {i}'))
for i in range(1,5):
    body=f'<path d="M10 50h300" stroke="url(#{"rose" if i%2 else "steel"})" stroke-width="3"/><circle cx="160" cy="50" r="{7+i*2}" fill="{C["navy"]}" stroke="{C["champagne"]}" stroke-width="3"/>'
    write(f'05-dividers-accents/section-ender-{i:02d}.svg',svg(320,100,body,f'LuxSync section ender {i}'))
for i in range(1,11):
    if i%3==0: body=f'<circle cx="50" cy="50" r="20" fill="none" stroke="{C["steel"]}" stroke-width="4"/><circle cx="50" cy="50" r="6" fill="{C["champagne"]}"/>'
    elif i%3==1: body=f'<path d="m50 15 12 23 25 12-25 12-12 23-12-23-25-12 25-12Z" fill="{C["champagne"]}"/>'
    else: body=f'<path d="M15 50h70" stroke="url(#steel)" stroke-width="8" stroke-linecap="round"/>'
    write(f'05-dividers-accents/mini-accent-{i:02d}.svg',svg(100,100,body,f'LuxSync mini accent {i}'))

# Ecommerce product cards.
product_data=[('touch-panel','Smart Touch Panel','$329','monitor'),('smart-speaker','Smart Speaker','$129','smart-speaker'),('4k-camera','4K Security Camera','$189','security-camera'),('smart-lock','Smart Lock','$249','smart-lock')]
for slug,name,price,icon_name in product_data:
    icon = line_icon(icon_name).replace('<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200" role="img" aria-label="LuxSync '+icon_name+' icon">','').rsplit('</svg>',1)[0]
    body=f'<rect width="420" height="620" rx="30" fill="{C["suede"]}" stroke="{C["steel"]}" stroke-width="2"/><g transform="translate(110 45)">{icon}</g>'+text(210,320,name,24,C['drift'])+text(210,362,price,22,C['champagne'])+f'<rect x="65" y="500" width="290" height="72" rx="36" fill="url(#rose)"/>'+text(210,545,'ADD TO CART',18,C['navy'])
    write(f'06-product-cards/{slug}.svg',svg(420,620,body,f'LuxSync {name} product card'))

# Website hero and ROI hero.
hero=f'<rect width="1600" height="760" fill="{C["navy"]}"/><ellipse cx="1260" cy="240" rx="460" ry="370" fill="url(#glow)"/><path d="M900 640c160-210 350-300 650-350" fill="none" stroke="url(#steel)" stroke-width="10" opacity=".65"/><rect x="940" y="250" width="480" height="280" rx="30" fill="{C["suede"]}" stroke="{C["steel"]}" opacity=".92"/><circle cx="1180" cy="390" r="74" fill="none" stroke="{C["champagne"]}" stroke-width="5"/>'+text(100,250,'SMART LIVING.',58,C['drift'],600,'start')+text(100,322,'ELEVATED.',58,C['champagne'],600,'start')+text(102,380,'Where Luxury Lives Intelligently',24,C['steel'],500,'start')
write('07-heroes/homepage-smart-living.svg',svg(1600,760,hero,'LuxSync Smart Living Elevated hero'))
roi=f'<rect width="1600" height="760" fill="{C["navy"]}"/><rect x="960" y="120" width="420" height="520" rx="24" fill="{C["drift"]}" transform="rotate(5 1170 380)"/><rect x="1005" y="170" width="330" height="18" rx="9" fill="url(#steel)"/><path d="M1015 515 1085 430l75 38 95-135 95 75" fill="none" stroke="url(#rose)" stroke-width="9"/><circle cx="1085" cy="430" r="9" fill="{C["steel"]}"/><circle cx="1160" cy="468" r="9" fill="{C["champagne"]}"/>'+text(100,230,'SMART HOME',55,C['drift'],600,'start')+text(100,300,'ROI GUIDE',55,C['champagne'],600,'start')+text(103,362,'Intelligent upgrades. Measurable value.',23,C['steel'],500,'start')+f'<rect x="100" y="440" width="360" height="78" rx="39" fill="url(#rose)"/>'+text(280,490,'GET THE ROI GUIDE',18,C['navy'])
write('08-roi/smart-home-roi-guide-hero.svg',svg(1600,760,roi,'LuxSync Smart Home ROI Guide hero'))

# Stationery.
logo_ref='../01-logos/LuxSync_Logo_Horizontal_Final.svg'
card_front=f'<rect width="1050" height="600" fill="{C["navy"]}"/><image href="{logo_ref}" x="120" y="95" width="810" height="300" preserveAspectRatio="xMidYMid meet"/>'+text(525,500,'luxsync.net',22,C['steel'])
card_back=f'<rect width="1050" height="600" fill="{C["drift"]}"/><rect width="34" height="600" fill="url(#steel)"/>'+text(110,170,'NAME SURNAME',30,C['navy'],600,'start')+text(110,215,'TITLE',18,C['rose'],600,'start')+text(110,310,'info@luxsync.net',20,C['navy'],500,'start')+text(110,350,'luxsync.net',20,C['navy'],500,'start')
letter=f'<rect width="850" height="1100" fill="{C["drift"]}"/><image href="{logo_ref}" x="65" y="38" width="430" height="165" preserveAspectRatio="xMinYMid meet"/><path d="M65 215h720" stroke="url(#steel)" stroke-width="4"/><path d="M65 1015h720" stroke="url(#rose)" stroke-width="2"/>'+text(65,1055,'LuxSync LLC • luxsync.net • info@luxsync.net',15,C['navy'],500,'start')
invoice=f'<rect width="850" height="1100" fill="{C["drift"]}"/><image href="{logo_ref}" x="55" y="35" width="390" height="150" preserveAspectRatio="xMinYMid meet"/>'+text(745,120,'INVOICE',34,C['navy'],600)+f'<rect x="55" y="280" width="740" height="46" fill="{C["suede"]}"/>'+text(80,311,'DESCRIPTION',15,C['drift'],600,'start')+text(620,311,'QTY',15,C['drift'])+text(750,311,'AMOUNT',15,C['drift'])
for n,b in [('business-card-front',card_front),('business-card-back',card_back),('letterhead',letter),('invoice-note',invoice)]: write(f'09-stationery/{n}.svg',svg(1050,600,b,f'LuxSync {n}') if 'card' in n else svg(850,1100,b,f'LuxSync {n}'))

# Marketing derivatives remain standalone files.
write('11-marketing/roi-guide-promo.svg',svg(1200,628,f'<rect width="1200" height="628" fill="{C["navy"]}"/><ellipse cx="980" cy="180" rx="290" ry="260" fill="url(#glow)"/>'+text(70,225,'THE ROI OF',44,C['drift'],600,'start')+text(70,285,'SMART LIVING',44,C['champagne'],600,'start')+text(72,340,'Download the LuxSync Smart Home ROI Guide',20,C['steel'],500,'start'),'LuxSync ROI guide promotion'))
write('11-marketing/homepage-luxury-smart-home.svg',svg(1200,628,f'<rect width="1200" height="628" fill="{C["navy"]}"/><path d="M660 520c120-180 280-270 510-300" stroke="url(#steel)" stroke-width="8" fill="none"/>'+text(70,240,'SMART LIVING.',46,C['drift'],600,'start')+text(70,300,'ELEVATED.',46,C['champagne'],600,'start'),'LuxSync luxury smart home promotion'))

# Palette and approved metallic samples.
for n,hx in {'slate-navy':C['navy'],'dark-suede':C['suede'],'pale-driftwood':C['drift'],'warm-taupe-mauve':C['taupe'],'antique-rose-taupe':C['rose'],'dusty-steel':C['steel'],'champagne-rose-gold-anchor':C['champagne']}.items():
    write(f'12-palette/{n}.svg',svg(600,240,f'<rect width="600" height="240" fill="{hx}"/>',f'LuxSync {n} swatch'))
write('12-palette/brushed-dusty-steel-metallic.svg',svg(600,240,'<rect width="600" height="240" fill="url(#steel)"/>','LuxSync Brushed Dusty Steel metallic sample'))
write('12-palette/champagne-rose-gold-metallic.svg',svg(600,240,'<rect width="600" height="240" fill="url(#rose)"/>','LuxSync Champagne Rose Gold metallic sample'))

readme=f'''# LuxSync Atomic Brand Asset Library\n\n**Status:** Approved production source of truth\n\nThis is the only active LuxSync graphics library. Every reusable website, ecommerce, stationery, and marketing object is an individual SVG file.\n\n## Authoritative logos\nThe only authoritative masters are `brand/source-logo/LuxSync_Logo_Horizontal_Combo.png`, `brand/source-logo/LuxSync_Logo_Horizontal_Final.png`, and `brand/source-logo/LuxSync_Logo_Orb.png`. The wrappers in `01-logos/` reference those files exactly. Never redraw, recolor, soften, regenerate, or re-typeset the logo artwork.\n\n## Approved palette\nSlate Navy `#0D1526`; Dark Suede `#172036`; Pale Driftwood `#D0BEB0`; Warm Taupe Mauve `#9E8B85`; Antique Rose Taupe `#967878`; Dusty Steel `#7B96B2`; Champagne Rose Gold Metallic anchored at `#D6B0A0`.\n\n**Brushed Dusty Steel** is the approved metallic-blue treatment and is built only from approved palette colors. Electric blue and other unapproved blues are prohibited. Any future new color requires explicit approval before use.\n\n## Atomic groups\n`01-logos/`, `02-icons/`, `03-buttons/`, `04-ui-controls/`, `05-dividers-accents/`, `06-product-cards/`, `07-heroes/`, `08-roi/`, `09-stationery/`, `11-marketing/`, `12-palette/`.\n\nEditable website text uses Manrope + Inter.\n'''
write('README.md',readme)
files=sorted(str(p.relative_to(ASSETS)) for p in ASSETS.rglob('*') if p.is_file())
manifest={'version':'4.0-atomic','status':'approved','source_of_truth':'brand/assets','authoritative_logos':['brand/source-logo/LuxSync_Logo_Horizontal_Combo.png','brand/source-logo/LuxSync_Logo_Horizontal_Final.png','brand/source-logo/LuxSync_Logo_Orb.png'],'approved_palette':C,'metallic_blue':'Brushed Dusty Steel based on #7B96B2 using approved palette colors only','asset_count':len(files),'files':files}
write('asset-manifest.json',json.dumps(manifest,indent=2))

# Retire every previous generation/install path after this deterministic cutover.
for rel in [
 'scripts/generate-luxury-orbit-assets.py','scripts/normalize-luxury-orbit-fonts.py','scripts/render-luxury-orbit-assets.py',
 'scripts/regenerate-brand-raster-assets.py','scripts/reconcile-asset-metadata.py','scripts/apply-approved-logo-artwork.py',
 'scripts/expand-atomic-source-archive.py','.github/workflows/regenerate-brand-raster-assets.yml',
 '.github/workflows/migrate-brand-v3.yml'
]:
    p=ROOT/rel
    if p.exists(): p.unlink()
if INSTALL.exists(): shutil.rmtree(INSTALL)

(ROOT/'brand'/'README.md').write_text(f'''# LuxSync Brand System\n\n**Status:** Active / Authoritative\n\nThe only active graphic asset system is `brand/assets/`. All former generated libraries and `brand/assets-v3/` are retired and removed.\n\n## Authoritative logo masters\nThe three immutable files in `brand/source-logo/` are `LuxSync_Logo_Horizontal_Combo.png`, `LuxSync_Logo_Horizontal_Final.png`, and `LuxSync_Logo_Orb.png`. Never redraw, recolor, soften, regenerate, or re-typeset them.\n\n## Approved palette\nSlate Navy `#0D1526`; Dark Suede `#172036`; Pale Driftwood `#D0BEB0`; Warm Taupe Mauve `#9E8B85`; Antique Rose Taupe `#967878`; Dusty Steel `#7B96B2`; Champagne Rose Gold Metallic, anchor `#D6B0A0`.\n\n**Brushed Dusty Steel** is the approved metallic-blue treatment. Electric blue and additional unapproved blues are prohibited. No new brand color may be introduced without explicit approval.\n\n## Typography\nUse Manrope for headings/UI and Inter for body/supporting text. Logo lettering remains protected artwork only.\n\n## Atomic asset rule\nEvery reusable graphic object is an individual file under `brand/assets/`.\n''',encoding='utf-8')
colors=ROOT/'brand'/'colors.md'
if colors.exists():
    s=colors.read_text(encoding='utf-8')
    s=s.replace('Derived icy-blue highlight tints may be used inside gradients and light effects when necessary for depth.','Do not derive brighter icy-blue or electric-blue tints. Branded blue accents must remain Dusty Steel `#7B96B2` or the approved Brushed Dusty Steel metallic treatment.')
    if 'Brushed Dusty Steel' not in s:
        s += '\n## Approved Metallic Blue\n\nBrushed Dusty Steel is the approved metallic-blue treatment, derived only from approved palette colors. No additional blue may be introduced without explicit approval.\n'
    colors.write_text(s,encoding='utf-8')
print('Built approved LuxSync atomic asset library:', len(files), 'files before manifest.')

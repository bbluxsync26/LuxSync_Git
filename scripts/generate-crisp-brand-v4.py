#!/usr/bin/env python3
"""Generate LuxSync Brand System 4.0 SVG masters from the approved logo artwork.

The logo PNGs are immutable source artwork. Generated SVGs may place them, but
must never redraw, retype, filter, recolor, or crop them.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "brand" / "brand-system-v4"

P = {
    "navy": "#0D1526",
    "suede": "#172036",
    "driftwood": "#D0BEB0",
    "taupe": "#9E8B85",
    "rose": "#967878",
    "steel": "#7B96B2",
}

LOGO_MONO = "../../assets/01-brand/luxsync-monogram-orb.png"
LOGO_HORIZONTAL = "../../assets/01-brand/luxsync-horizontal-lockup.png"


def write(rel: str, body: str) -> None:
    path = OUT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body.strip() + "\n", encoding="utf-8")


def shell(w: int, h: int, title: str, body: str, *, light: bool = False) -> str:
    bg = P["driftwood"] if light else P["navy"]
    fg = P["navy"] if light else P["driftwood"]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{title}">
<defs>
 <linearGradient id="champagne" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{P['driftwood']}"/><stop offset=".28" stop-color="{P['taupe']}"/><stop offset=".52" stop-color="{P['driftwood']}"/><stop offset=".75" stop-color="{P['rose']}"/><stop offset="1" stop-color="{P['taupe']}"/></linearGradient>
 <linearGradient id="steelLight" x1="0" y1="0" x2="1" y2="0"><stop stop-color="{P['steel']}" stop-opacity=".15"/><stop offset=".5" stop-color="{P['driftwood']}" stop-opacity=".92"/><stop offset="1" stop-color="{P['steel']}" stop-opacity=".18"/></linearGradient>
 <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0"><stop stop-color="{P['navy']}" stop-opacity=".96"/><stop offset=".58" stop-color="{P['navy']}" stop-opacity=".7"/><stop offset="1" stop-color="{P['navy']}" stop-opacity=".15"/></linearGradient>
 <filter id="shadow"><feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="{P['navy']}" flood-opacity=".55"/></filter>
 <filter id="glow"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
 <style>.display{{font-family:Manrope,Arial,sans-serif;font-weight:600}}.body{{font-family:Inter,Arial,sans-serif}}.caps{{letter-spacing:2.5px}}.light{{fill:{fg}}}.muted{{fill:{P['taupe']}}}.steel{{fill:{P['steel']}}}.card{{fill:{P['suede']};stroke:{P['taupe']};stroke-opacity:.28}}</style>
</defs><rect width="100%" height="100%" fill="{bg}"/>{body}</svg>'''


def sparkle(x: int, y: int, size: int = 18) -> str:
    return f'<g transform="translate({x} {y})" stroke="{P["driftwood"]}" opacity=".85" filter="url(#glow)"><path d="M{-size} 0H{size}M0 {-size}V{size}"/><circle r="2.5" fill="{P["driftwood"]}" stroke="none"/></g>'


def logo_placements() -> None:
    write("01-logos/logo-clear-space.svg", shell(1400, 760, "LuxSync logo clear space", f'''
      <text x="70" y="70" class="body caps muted" font-size="17">Approved Logo Clear Space · Do Not Retype</text>
      <rect x="90" y="120" width="500" height="500" rx="28" fill="{P['suede']}" stroke="{P['taupe']}" stroke-opacity=".4" stroke-dasharray="8 10"/>
      <image x="150" y="180" width="380" height="380" preserveAspectRatio="xMidYMid meet" xlink:href="{LOGO_MONO}"/>
      <rect x="670" y="180" width="650" height="310" rx="28" fill="{P['suede']}" stroke="{P['taupe']}" stroke-opacity=".4" stroke-dasharray="8 10"/>
      <image x="720" y="225" width="550" height="220" preserveAspectRatio="xMidYMid meet" xlink:href="{LOGO_HORIZONTAL}"/>
      <text x="90" y="690" class="body light" font-size="19">Keep one cap-height of quiet space around every approved logo placement.</text>'''))
    write("01-logos/logo-dark-background.svg", shell(1600, 500, "LuxSync horizontal logo on approved dark background", f'<image x="120" y="85" width="1360" height="330" preserveAspectRatio="xMidYMid meet" xlink:href="{LOGO_HORIZONTAL}"/>{sparkle(1500,90,13)}'))
    write("01-logos/logo-monogram-dark-background.svg", shell(900, 900, "LuxSync monogram on approved dark background", f'<image x="95" y="95" width="710" height="710" preserveAspectRatio="xMidYMid meet" xlink:href="{LOGO_MONO}"/>'))
    write("01-logos/logo-horizontal-llc.svg", shell(1600, 560, "LuxSync LLC horizontal legal lockup", f'''
      <image x="110" y="55" width="1380" height="355" preserveAspectRatio="xMidYMid meet" xlink:href="{LOGO_HORIZONTAL}"/>
      <line x1="660" y1="437" x2="940" y2="437" stroke="{P['rose']}" stroke-width="1.5"/>
      <text x="800" y="482" text-anchor="middle" class="body light" font-size="24" letter-spacing="8">LUXSYNC LLC</text>'''))


def foundation() -> None:
    swatches = [("Slate Navy", P["navy"]), ("Dark Suede", P["suede"]), ("Pale Driftwood", P["driftwood"]), ("Warm Taupe Mauve", P["taupe"]), ("Antique Rose Taupe", P["rose"]), ("Dusty Steel", P["steel"])]
    blocks = []
    for i, (name, color) in enumerate(swatches):
        x = 80 + i * 205
        blocks.append(f'<rect x="{x}" y="160" width="165" height="165" rx="25" fill="{color}" stroke="{P["taupe"]}" stroke-opacity=".35"/><text x="{x}" y="360" class="display light" font-size="17">{name}</text><text x="{x}" y="388" class="body muted" font-size="15">{color}</text>')
    blocks.append(f'<rect x="1310" y="160" width="210" height="165" rx="25" fill="url(#champagne)"/>{sparkle(1480,185,13)}<text x="1310" y="360" class="display light" font-size="17">Champagne Rose Gold</text><text x="1310" y="388" class="body muted" font-size="15">Metallic treatment</text>')
    write("02-foundation/approved-palette.svg", shell(1600, 500, "LuxSync approved color palette", '<text x="80" y="90" class="display light" font-size="36">Approved Palette</text><text x="80" y="122" class="body muted" font-size="16">Only these six anchors plus the Champagne Rose Gold metallic treatment.</text>' + ''.join(blocks)))
    write("02-foundation/typography.svg", shell(1400, 760, "LuxSync typography system", f'''
      <text x="80" y="86" class="body caps steel" font-size="16">Editable Brand Typography</text>
      <text x="80" y="190" class="display light" font-size="72">Manrope 600</text><text x="80" y="240" class="body muted" font-size="19">Display · headings · navigation · calls to action</text>
      <line x1="80" y1="300" x2="1320" y2="300" stroke="{P['rose']}" opacity=".55"/>
      <text x="80" y="420" class="body light" font-size="58">Inter 400 / 500</text><text x="80" y="470" class="body muted" font-size="19">Body copy · product detail · forms · captions · supporting UI</text>
      <text x="80" y="590" class="display" fill="url(#champagne)" font-size="43">Quiet intelligence. Beautifully integrated.</text>
      <text x="80" y="660" class="body light" font-size="18">The approved dimensional logo lettering remains artwork and is never retyped.</text>{sparkle(1295,610,14)}'''))


def ui() -> None:
    buttons = [("SHOP NOW", P["driftwood"], P["navy"]), ("EXPLORE SOLUTIONS", P["steel"], P["navy"]), ("GET THE ROI GUIDE", P["navy"], P["driftwood"]), ("BOOK A CONSULTATION", P["suede"], P["driftwood"]), ("ADD TO CART", P["rose"], P["driftwood"]), ("REQUEST A QUOTE", "none", P["driftwood"])]
    out = ['<text x="70" y="75" class="display light" font-size="34">Buttons & Calls to Action</text>']
    for i,(label,bg,fg) in enumerate(buttons):
        x=70+(i%2)*420; y=125+(i//2)*115
        stroke=P['steel'] if bg=='none' else bg
        out.append(f'<rect x="{x}" y="{y}" width="360" height="72" rx="36" fill="{bg}" stroke="{stroke}" stroke-width="2"/><text x="{x+180}" y="{y+45}" text-anchor="middle" class="display" font-size="16" fill="{fg}">{label} →</text>')
    write("03-ui/buttons-and-ctas.svg", shell(920, 560, "LuxSync website buttons and calls to action", ''.join(out)))
    badges = ["LUXSYNC PICK", "SMART HOME READY", "COMPATIBILITY VERIFIED", "NO SUBSCRIPTION", "HOST READY", "NEW ARRIVAL", "IN STOCK", "ROI GUIDE"]
    out=['<text x="60" y="68" class="display light" font-size="32">Badges</text>']
    for i,label in enumerate(badges):
        x=60+(i%2)*390; y=105+(i//2)*84; bg=P['steel'] if i in (1,4,5) else P['suede']
        out.append(f'<rect x="{x}" y="{y}" width="340" height="52" rx="26" fill="{bg}" stroke="{P["taupe"]}" stroke-opacity=".55"/><text x="{x+170}" y="{y+33}" text-anchor="middle" class="body light caps" font-size="12">{label}</text>')
    write("03-ui/badges.svg", shell(840, 520, "LuxSync ecommerce badges", ''.join(out)))
    write("03-ui/forms-and-search.svg", shell(1200, 620, "LuxSync forms and search controls", f'''
      <text x="65" y="70" class="display light" font-size="34">Forms, Search & Selection</text>
      <text x="65" y="130" class="body muted" font-size="15">SEARCH</text><rect x="65" y="150" width="500" height="66" rx="18" class="card"/><text x="90" y="191" class="body muted" font-size="17">Search curated solutions…</text><circle cx="526" cy="183" r="10" fill="none" stroke="{P['steel']}" stroke-width="2"/><path d="M533 191l10 10" stroke="{P['steel']}" stroke-width="2"/>
      <text x="635" y="130" class="body muted" font-size="15">SOLUTION TYPE</text><rect x="635" y="150" width="500" height="66" rx="18" class="card"/><text x="660" y="191" class="body light" font-size="17">Private Residence</text><path d="M1084 177l10 10 10-10" fill="none" stroke="{P['steel']}" stroke-width="2"/>
      <text x="65" y="290" class="body muted" font-size="15">YOUR GOAL</text><rect x="65" y="310" width="1070" height="126" rx="18" class="card"/><text x="90" y="352" class="body muted" font-size="17">Tell us what intelligent luxury should feel like…</text>
      <rect x="65" y="480" width="270" height="66" rx="33" fill="{P['driftwood']}"/><text x="200" y="521" class="display" fill="{P['navy']}" font-size="16" text-anchor="middle">FIND MY SOLUTION →</text>
      <text x="365" y="520" class="body muted" font-size="15">Smart recommendations reveal the next relevant questions.</text>'''))
    write("03-ui/ecommerce-controls.svg", shell(1200, 520, "LuxSync ecommerce controls", f'''
      <text x="60" y="68" class="display light" font-size="32">E-commerce Controls</text>
      <text x="60" y="125" class="body muted" font-size="14">QUANTITY</text><rect x="60" y="145" width="240" height="64" rx="20" class="card"/><text x="96" y="185" class="display steel" font-size="24">−</text><text x="180" y="185" text-anchor="middle" class="body light" font-size="18">1</text><text x="264" y="185" class="display steel" font-size="24">+</text>
      <text x="360" y="125" class="body muted" font-size="14">SORT</text><rect x="360" y="145" width="360" height="64" rx="20" class="card"/><text x="386" y="185" class="body light" font-size="17">Featured</text><path d="M678 172l10 10 10-10" fill="none" stroke="{P['steel']}" stroke-width="2"/>
      <text x="780" y="125" class="body muted" font-size="14">VIEW</text><rect x="780" y="145" width="132" height="64" rx="20" class="card"/><g fill="{P['steel']}"><rect x="810" y="167" width="12" height="12"/><rect x="828" y="167" width="12" height="12"/><rect x="810" y="185" width="12" height="12"/><rect x="828" y="185" width="12" height="12"/></g><path d="M870 172h22M870 181h22M870 190h22" stroke="{P['taupe']}" stroke-width="2"/>
      <text x="60" y="285" class="body muted" font-size="14">CART</text><rect x="60" y="305" width="852" height="86" rx="24" class="card"/><circle cx="110" cy="348" r="18" fill="none" stroke="{P['steel']}" stroke-width="2"/><text x="154" y="343" class="display light" font-size="17">Curated Smart Hub</text><text x="154" y="368" class="body muted" font-size="14">Compatibility verified</text><text x="700" y="356" class="body light" font-size="17">Qty 1</text><rect x="770" y="324" width="116" height="48" rx="24" fill="{P['driftwood']}"/><text x="828" y="354" text-anchor="middle" class="display" fill="{P['navy']}" font-size="13">CHECKOUT</text>'''))


ICONS = {
    "security": '<path d="M50 12l30 12v24c0 21-12 37-30 46C32 85 20 69 20 48V24z"/><path d="M37 51l9 9 19-22"/>',
    "lighting": '<circle cx="50" cy="42" r="25"/><path d="M38 70h24M40 80h20M50 5v9M13 20l8 8M87 20l-8 8"/>',
    "climate": '<path d="M43 16v47a18 18 0 1030 13 18 18 0 00-13-13V16a8 8 0 00-17 0z"/><path d="M51 32v40"/>',
    "access": '<rect x="22" y="14" width="56" height="78" rx="8"/><circle cx="62" cy="53" r="4"/><path d="M36 30h24"/>',
    "entertainment": '<rect x="12" y="20" width="76" height="54" rx="6"/><path d="M43 35l22 12-22 12zM35 88h30"/>',
    "water": '<path d="M50 9C40 26 24 43 24 61a26 26 0 0052 0C76 43 60 26 50 9z"/>',
    "automation": '<path d="M50 9l9 13 16-2 3 16 14 8-8 14 5 15-15 5-8 14-14-8-15 5-6-15-15-6 8-14-5-15 15-6 7-15z"/><circle cx="50" cy="51" r="15"/>',
    "analytics": '<path d="M15 86h75M24 75V49h14v26M47 75V31h14v44M70 75V17h14v58"/><path d="M18 38l23-18 20 10 25-20"/>',
}


def icons() -> None:
    for name, paths in ICONS.items():
        write(f"04-icons/{name}.svg", shell(100, 100, f"LuxSync {name} icon", f'<g fill="none" stroke="{P["steel"]}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">{paths}</g>'))
    tiles=[]
    for i,(name,paths) in enumerate(ICONS.items()):
        x=60+(i%4)*260; y=100+(i//4)*220
        tiles.append(f'<g transform="translate({x} {y})"><rect width="210" height="170" rx="28" class="card"/><g transform="translate(55 22)" fill="none" stroke="{P["steel"]}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">{paths}</g><text x="105" y="147" text-anchor="middle" class="body light" font-size="16">{name.title()}</text></g>')
    write("04-icons/icon-library.svg", shell(1120, 590, "LuxSync icon library", '<text x="60" y="62" class="display light" font-size="32">Core Line Icon Library</text>'+''.join(tiles)))


def hero(rel: str, title1: str, title2: str, subtitle: str, cta: str, scene: str, eyebrow: str) -> None:
    write(rel, shell(1600, 700, f"LuxSync {title1} {title2} hero", f'''
      <defs><clipPath id="scene"><rect width="1600" height="700"/></clipPath></defs><image width="1600" height="700" preserveAspectRatio="xMidYMid slice" clip-path="url(#scene)" xlink:href="{scene}"/><rect width="1600" height="700" fill="url(#fade)"/>
      <text x="100" y="142" class="body caps steel" font-size="17">{eyebrow}</text><text x="100" y="245" class="display light" font-size="76">{title1}</text><text x="100" y="329" class="display" fill="url(#champagne)" font-size="76">{title2}</text><text x="105" y="396" class="body light" font-size="25">{subtitle}</text>
      <rect x="100" y="458" width="270" height="64" rx="32" fill="{P['driftwood']}"/><text x="235" y="498" text-anchor="middle" class="display" fill="{P['navy']}" font-size="16">{cta} →</text>
      <image x="1195" y="42" width="330" height="120" preserveAspectRatio="xMidYMid meet" xlink:href="{LOGO_HORIZONTAL}"/>{sparkle(1450,610,14)}'''))


def heroes() -> None:
    hero("05-heroes/home-technology-feels-like-home.svg", "Technology that feels", "like home.", "Quiet intelligence. Beautifully integrated.", "EXPLORE SOLUTIONS", "../../assets/12-scenes/home-hero-room.png", "INTELLIGENT LUXURY")
    hero("05-heroes/roi-guide.svg", "The ROI of", "Smart Living", "See how comfort, efficiency, and property value work together.", "GET THE ROI GUIDE", "../../assets/12-scenes/roi-guide-backdrop.png", "LUXSYNC GUIDE")
    hero("05-heroes/shop-curated-smart-living.svg", "Curated technology.", "Confident choices.", "Compatibility-first products selected for beautiful modern living.", "SHOP CURATED", "../../assets/12-scenes/shop-smart-home-hardware.png", "THE LUXSYNC SHOP")
    hero("05-heroes/find-my-luxsync-solution.svg", "Your lifestyle.", "Intelligently matched.", "Start with the experience you want. We’ll shape the roadmap.", "FIND MY SOLUTION", "../../assets/12-scenes/dashboard-tablet-scene.png", "GUIDED RECOMMENDATIONS")
    hero("05-heroes/short-term-rentals.svg", "Five-star stays.", "Smarter operations.", "Elevated guest experiences with control that travels anywhere.", "EXPLORE HOST SOLUTIONS", "../../assets/12-scenes/mobile-automation-scene.png", "SHORT-TERM RENTALS")
    hero("05-heroes/smart-home-hub.svg", "One refined hub.", "Endless possibility.", "A compatibility-first foundation for every intelligent experience.", "BUILD YOUR SYSTEM", "../../assets/12-scenes/smart-hub-vignette.png", "CONNECTED LIVING")


def ecommerce() -> None:
    cats=[("SMART SECURITY","security"),("LIGHTING & AMBIENCE","lighting"),("CLIMATE & COMFORT","climate"),("ACCESS & ENTRY","access"),("ENTERTAINMENT","entertainment"),("WATER AWARENESS","water"),("AUTOMATIONS","automation"),("INSIGHTS & ROI","analytics")]
    cards=[]
    for i,(label,icon) in enumerate(cats):
        x=60+(i%4)*310; y=110+(i//4)*260
        cards.append(f'<g transform="translate({x} {y})"><rect width="270" height="220" rx="30" class="card"/><image x="85" y="26" width="100" height="100" xlink:href="../04-icons/{icon}.svg"/><text x="135" y="158" text-anchor="middle" class="display light" font-size="16">{label}</text><text x="135" y="189" text-anchor="middle" class="body steel" font-size="13">EXPLORE →</text></g>')
    write("06-ecommerce/category-cards.svg", shell(1320, 680, "LuxSync ecommerce category cards", '<text x="60" y="66" class="display light" font-size="34">Shop by Intelligent Experience</text>'+''.join(cards)))
    write("06-ecommerce/product-card.svg", shell(520, 760, "LuxSync ecommerce product card", f'''
      <rect x="35" y="35" width="450" height="690" rx="32" class="card" filter="url(#shadow)"/><rect x="58" y="58" width="404" height="350" rx="24" fill="{P['navy']}"/><image x="90" y="80" width="340" height="300" preserveAspectRatio="xMidYMid meet" xlink:href="../../assets/12-scenes/smart-hub-vignette.png"/>
      <rect x="75" y="75" width="115" height="32" rx="16" fill="{P['navy']}"/><text x="132" y="96" text-anchor="middle" class="body light caps" font-size="10">LUXSYNC PICK</text><path d="M420 80l7 9 11 2-7 9 1 11-12-5-11 5 2-11-8-9 11-2z" fill="none" stroke="{P['steel']}"/>
      <text x="70" y="462" class="display light" font-size="27">Curated Smart Hub</text><text x="70" y="496" class="body muted" font-size="16">Compatibility-first foundation for</text><text x="70" y="519" class="body muted" font-size="16">beautiful intelligent living.</text>
      <text x="70" y="566" class="body steel" font-size="14">SMART HOME READY · NO SUBSCRIPTION</text><rect x="70" y="620" width="380" height="66" rx="33" fill="{P['driftwood']}"/><text x="260" y="661" text-anchor="middle" class="display" fill="{P['navy']}" font-size="16">ADD TO CART →</text>'''))
    write("06-ecommerce/trust-bar.svg", shell(1400, 170, "LuxSync ecommerce trust bar", f'''
      <g class="body light" font-size="16" text-anchor="middle"><text x="175" y="77" class="display" font-size="18">Compatibility First</text><text x="175" y="104" class="muted" font-size="14">Selected to work together</text><text x="525" y="77" class="display" font-size="18">Secure by Design</text><text x="525" y="104" class="muted" font-size="14">Privacy-conscious choices</text><text x="875" y="77" class="display" font-size="18">Curated Quality</text><text x="875" y="104" class="muted" font-size="14">Fewer, better products</text><text x="1225" y="77" class="display" font-size="18">Premium Support</text><text x="1225" y="104" class="muted" font-size="14">Guidance when you need it</text></g><g stroke="{P['rose']}" opacity=".55"><path d="M350 45v80M700 45v80M1050 45v80"/></g>'''))


def stationery() -> None:
    write("07-stationery/business-card-front.svg", shell(1050, 600, "LuxSync LLC business card front", f'<image x="78" y="105" width="340" height="340" preserveAspectRatio="xMidYMid meet" xlink:href="{LOGO_MONO}"/><line x1="455" y1="90" x2="455" y2="510" stroke="{P["rose"]}" stroke-width="2"/><text x="510" y="220" class="display light" font-size="42">BRIDGETTE [LAST NAME]</text><text x="512" y="265" class="body steel" font-size="19">CO-FOUNDER &amp; CHIEF TECHNOLOGY</text><text x="512" y="294" class="body steel" font-size="19">AND STRATEGY OFFICER</text><text x="512" y="380" class="body light" font-size="18">info@luxsync.net</text><text x="512" y="414" class="body light" font-size="18">luxsync.net</text>{sparkle(946,105,12)}'))
    write("07-stationery/business-card-back.svg", shell(1050, 600, "LuxSync LLC business card back", f'<image x="125" y="145" width="800" height="310" preserveAspectRatio="xMidYMid meet" xlink:href="{LOGO_HORIZONTAL}"/>'))
    write("07-stationery/letterhead.svg", shell(1275, 1650, "LuxSync LLC letterhead", f'<image x="72" y="52" width="500" height="145" preserveAspectRatio="xMinYMid meet" xlink:href="{LOGO_HORIZONTAL}"/><line x1="72" y1="225" x2="1203" y2="225" stroke="{P["rose"]}"/><text x="1203" y="178" text-anchor="end" class="body steel" font-size="18">luxsync.net · info@luxsync.net</text><text x="72" y="1575" class="body muted" font-size="14">LuxSync LLC · Where Luxury Lives Intelligently</text><text x="1203" y="1575" text-anchor="end" class="body muted" font-size="14">luxsync.net</text>'))
    write("07-stationery/invoice.svg", shell(1275, 1650, "LuxSync LLC invoice", f'<image x="72" y="52" width="440" height="132" preserveAspectRatio="xMinYMid meet" xlink:href="{LOGO_HORIZONTAL}"/><text x="1203" y="110" text-anchor="end" class="display light" font-size="46">INVOICE</text><text x="1203" y="150" text-anchor="end" class="body muted" font-size="16">Invoice # · Date · Due</text><line x1="72" y1="225" x2="1203" y2="225" stroke="{P["rose"]}"/><text x="72" y="300" class="body steel" font-size="16">BILL TO</text><text x="670" y="300" class="body steel" font-size="16">PROJECT / PROPERTY</text><rect x="72" y="430" width="1131" height="54" fill="{P["suede"]}"/><text x="95" y="465" class="body light" font-size="16">DESCRIPTION</text><text x="1168" y="465" text-anchor="end" class="body light" font-size="16">AMOUNT</text><g stroke="{P["taupe"]}" stroke-opacity=".35"><path d="M72 560h1131M72 650h1131M72 740h1131"/></g><text x="1020" y="930" class="display light" font-size="20">TOTAL</text><text x="1203" y="930" text-anchor="end" class="display light" font-size="20">$0.00</text><text x="72" y="1575" class="body muted" font-size="14">LuxSync LLC · Thank you for choosing intelligent luxury.</text>'))
    write("07-stationery/email-signature.svg", shell(900, 300, "LuxSync LLC email signature", f'<image x="28" y="36" width="210" height="210" preserveAspectRatio="xMidYMid meet" xlink:href="{LOGO_MONO}"/><line x1="258" y1="38" x2="258" y2="258" stroke="{P["rose"]}" stroke-width="2"/><text x="292" y="92" class="display light" font-size="30">NAME</text><text x="292" y="126" class="body steel" font-size="16">TITLE · LUXSYNC LLC</text><text x="292" y="180" class="body light" font-size="15">info@luxsync.net · luxsync.net</text><text x="292" y="225" class="body muted caps" font-size="12">WHERE LUXURY LIVES INTELLIGENTLY</text>'))


def marketing() -> None:
    write("08-marketing/email-header.svg", shell(1200, 360, "LuxSync marketing email header", f'<image x="55" y="70" width="520" height="220" preserveAspectRatio="xMinYMid meet" xlink:href="{LOGO_HORIZONTAL}"/><text x="1140" y="155" text-anchor="end" class="display light" font-size="43">Smart living.</text><text x="1140" y="205" text-anchor="end" class="display" fill="url(#champagne)" font-size="43">Beautifully delivered.</text>{sparkle(1115,266,12)}'))
    write("08-marketing/social-square.svg", shell(1080, 1080, "LuxSync social media square", f'<image x="290" y="85" width="500" height="330" preserveAspectRatio="xMidYMid meet" xlink:href="{LOGO_MONO}"/><text x="540" y="535" text-anchor="middle" class="display light" font-size="67">Smart Living.</text><text x="540" y="610" text-anchor="middle" class="display" fill="url(#champagne)" font-size="67">Elevated.</text><text x="540" y="685" text-anchor="middle" class="body muted" font-size="23">Where Luxury Lives Intelligently</text><rect x="390" y="760" width="300" height="68" rx="34" fill="{P['driftwood']}"/><text x="540" y="802" text-anchor="middle" class="display" fill="{P['navy']}" font-size="17">DISCOVER LUXSYNC →</text>{sparkle(820,470,16)}'))
    write("08-marketing/flyer.svg", shell(1275, 1650, "LuxSync marketing flyer", f'<image x="80" y="62" width="550" height="190" preserveAspectRatio="xMinYMid meet" xlink:href="{LOGO_HORIZONTAL}"/><text x="80" y="420" class="display light" font-size="78">Luxury should feel</text><text x="80" y="505" class="display" fill="url(#champagne)" font-size="78">effortless.</text><text x="85" y="580" class="body light" font-size="26">Curated smart-home experiences designed around your life.</text><rect x="80" y="680" width="1115" height="560" rx="40" fill="{P['suede']}"/><image x="80" y="680" width="1115" height="560" preserveAspectRatio="xMidYMid slice" opacity=".88" xlink:href="../../assets/12-scenes/home-hero-room.png"/><rect x="80" y="680" width="1115" height="560" rx="40" fill="url(#fade)" opacity=".55"/><g class="body light" font-size="23"><text x="130" y="830">• Personalized comfort</text><text x="130" y="885">• Compatibility-first technology</text><text x="130" y="940">• Elegant automations</text><text x="130" y="995">• Guidance without overwhelm</text></g><rect x="80" y="1350" width="390" height="76" rx="38" fill="{P['driftwood']}"/><text x="275" y="1398" text-anchor="middle" class="display" fill="{P['navy']}" font-size="18">FIND MY LUXSYNC SOLUTION →</text><text x="80" y="1530" class="body muted" font-size="18">luxsync.net · info@luxsync.net</text>{sparkle(1125,1320,15)}'))
    write("08-marketing/presentation-cover.svg", shell(1600, 900, "LuxSync presentation cover", f'<image x="90" y="72" width="600" height="220" preserveAspectRatio="xMinYMid meet" xlink:href="{LOGO_HORIZONTAL}"/><text x="90" y="530" class="display light" font-size="75">Presentation Title</text><text x="95" y="600" class="body steel" font-size="27">Subtitle or strategic theme</text><line x1="95" y1="655" x2="760" y2="655" stroke="url(#champagne)" stroke-width="3"/><text x="95" y="720" class="body muted" font-size="18">LuxSync LLC · Month Year</text>{sparkle(1420,735,18)}'))


def docs() -> None:
    write("09-documentation/markdown-header.svg", shell(1200, 220, "LuxSync documentation header", f'<image x="35" y="22" width="430" height="170" preserveAspectRatio="xMinYMid meet" xlink:href="{LOGO_HORIZONTAL}"/><line x1="500" y1="46" x2="500" y2="174" stroke="{P["rose"]}"/><text x="545" y="98" class="display light" font-size="31">DOCUMENT TITLE</text><text x="545" y="137" class="body steel" font-size="16">LuxSync LLC · Document ID · Version</text>'))


def main() -> None:
    logo_placements(); foundation(); ui(); icons(); heroes(); ecommerce(); stationery(); marketing(); docs()
    print(f"Generated LuxSync v4 SVG masters under {OUT}")


if __name__ == "__main__":
    main()

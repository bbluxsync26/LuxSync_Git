#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRAND_SYSTEM = "LuxSync Production Raster v5"
SLOGAN = "Where Luxury Lives Intelligently"
PRIMARY_CTA = "Find My LuxSync Solution"
SECONDARY_CTA = "Shop Smart Home"
BRIDGETTE_TITLE = "Co-Founder & Chief Technology and Strategy Officer"
SHELDON_TITLE = "Co-Founder & Chief Customer and Operations Officer"


def write(rel: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def append_once(rel: str, marker: str, content: str) -> None:
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if marker not in text:
        path.write_text(text.rstrip() + "\n\n" + content.rstrip() + "\n", encoding="utf-8")


def remove_line_references(path: Path, needles: tuple[str, ...]) -> None:
    if not path.exists() or path.suffix.lower() not in {".md", ".txt", ".yml", ".yaml", ".py", ".json"}:
        return
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = [line for line in text.splitlines() if not any(n in line for n in needles)]
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


# 1. Normalize active brand naming and remove dead references.
replacements = {
    "LuxSync v3": BRAND_SYSTEM,
    "Brand System 4.0": BRAND_SYSTEM,
    "LuxSync Brand System 4.0": BRAND_SYSTEM,
    "brand/assets-v3/": "brand/assets/",
    "brand/assets-v3": "brand/assets",
    "scripts/validate-brand-v3.py": "scripts/validate-production-brand.py",
    "validate-brand-v3.py": "validate-production-brand.py",
}
text_suffixes = {".md", ".txt", ".json", ".yml", ".yaml", ".py", ".js", ".mjs", ".css", ".html"}
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in text_suffixes:
        continue
    if any(part in {".git", "node_modules"} for part in path.parts):
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    new = text
    for old, replacement in replacements.items():
        new = new.replace(old, replacement)
    if new != text:
        path.write_text(new, encoding="utf-8")

obsolete = (
    "scripts/migrate-brand-v3.py",
    "docs/runbooks/RB-007-Brand-Asset-Raster-Regeneration.md",
    "docs/runbooks/RB-008-Luxury-Orbit-Brand-Asset-Generation.md",
)
for rel in obsolete:
    p = ROOT / rel
    if p.exists():
        p.unlink()

needles = (
    "migrate-brand-v3.py",
    "RB-007-Brand-Asset-Raster-Regeneration.md",
    "RB-008-Luxury-Orbit-Brand-Asset-Generation.md",
)
for path in ROOT.rglob("*"):
    remove_line_references(path, needles)

# 2. Reclassify the installed raster library after visual QA.
manifest_path = ROOT / "brand/assets/asset-manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
manifest["version"] = "5.1-production-source-of-truth"
manifest["brand_system"] = BRAND_SYSTEM
manifest["source_package"] = "one-time verified import; source ZIP removed after installation"
manifest["publication_policy"] = (
    "Only the three exact logo copies in 01-logos are approved for direct publication from this raster library. "
    "Folders 02 through 09 are design-reference exports and must not be published directly because visual QA found "
    "baked/generated text, generated logo approximations, or board-crop artifacts. Build production UI with live HTML/CSS, "
    "the exact logo masters, and validated commerce/manufacturer imagery."
)
status_by_folder = {
    "01-logos": "production-approved",
    "02-icons": "reference-only",
    "03-buttons": "reference-only",
    "04-ui-controls": "reference-only",
    "05-dividers-accents": "reference-only",
    "06-product-cards": "reference-only",
    "07-heroes": "reference-only",
    "08-sections": "reference-only",
    "09-stationery": "reference-only",
}
manifest["status_by_folder"] = status_by_folder
for item in manifest.get("files", []):
    parts = Path(item["path"]).parts
    folder = next((part for part in parts if part in status_by_folder), None)
    item["publication_status"] = status_by_folder.get(folder, "reference-only")
manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

write("brand/assets/README.md", f'''# LuxSync Raster Asset Library

**Status:** Active source library  
**Brand system:** {BRAND_SYSTEM}

This folder preserves the verified raster import and the exact approved logo copies. Publication status is intentionally explicit so generated composites and board slices cannot accidentally become live website artwork.

## Production-approved

Only these files may be published directly from this library:

- `01-logos/LuxSync_Logo_Horizontal_Combo.png`
- `01-logos/LuxSync_Logo_Horizontal_Final.png`
- `01-logos/LuxSync_Logo_Orb.png`

They are byte-identical copies of the immutable masters under `brand/source-logo/`.

## Reference-only

Folders `02-icons/` through `09-stationery/` are **design-reference exports only**. Visual QA found that some files contain baked/generated copy, generated logo approximations, or board-crop artifacts. They are useful for style direction, but they must not be shipped as website UI, product data, founder information, support information, or public claims.

Production implementation must use:

1. exact protected logo masters;
2. live HTML/CSS for headings, buttons, forms, icons, cards, dividers, navigation, Concierge and Contact interactions;
3. validated commerce/manufacturer imagery for real products when available;
4. approved text-free photography only when a clean production image is available.

**Official slogan:** {SLOGAN}  
**Metallic blue:** Brushed Dusty Steel `#7B96B2`  
**Premium metallic anchor:** Champagne Rose Gold `#D6B0A0`

See `website/asset-map.md` for the route-by-route publication map.''')

write("brand/README.md", f'''# LuxSync Brand System

**Status:** Active / Authoritative  
**Brand system:** {BRAND_SYSTEM}  
**Design DNA:** Plush Drift  
**Voice:** Intelligent Calm

## Locked brand contract

- Official public slogan: **{SLOGAN}**
- Headings, navigation and UI: Manrope 500/600
- Body and supporting UI: Inter 400/500
- Slate Navy `#0D1526`
- Dark Suede `#172036`
- Pale Driftwood `#D0BEB0`
- Warm Taupe Mauve `#9E8B85`
- Antique Rose Taupe `#967878`
- Dusty Steel `#7B96B2`
- Champagne Rose Gold Metallic `#D6B0A0` anchor
- Brushed Dusty Steel is the only approved metallic-blue treatment.

## Immutable logo masters

The only authoritative logo masters are:

- `brand/source-logo/LuxSync_Logo_Horizontal_Combo.png`
- `brand/source-logo/LuxSync_Logo_Horizontal_Final.png`
- `brand/source-logo/LuxSync_Logo_Orb.png`

Never redraw, retype, recolor, soften, regenerate, or approximate them.

## Publication rule

The exact logo copies in `brand/assets/01-logos/` are production-approved. Other imported raster slices under `brand/assets/` remain reference-only after visual QA. Live website UI must be implemented with HTML/CSS and approved brand tokens rather than flattened board crops.

Canonical implementation references:

- `docs/production-source-of-truth.md`
- `website/asset-map.md`
- `website/implementation-manifest.json`
- `website/styles/design-system.md`
''')

write("docs/production-asset-library.md", f'''# LuxSync Production Visual Library

**Status:** Active / Authoritative  
**Brand system:** {BRAND_SYSTEM}

## Publication-safe assets

The three protected logo masters under `brand/source-logo/` and their byte-identical copies under `brand/assets/01-logos/` are approved for direct use.

All other raster files currently under `brand/assets/02-icons/` through `brand/assets/09-stationery/` are retained as **reference-only design material**. A visual QA pass identified baked/generated text, generated logo approximations, or board-crop artifacts in that import. They must not be used as public UI, live product cards, founder information, support information, or claims.

## Production visual strategy

The launch website should compose its visual language live:

- exact LuxSync logo artwork;
- Slate Navy and Dark Suede architectural fields;
- Pale Driftwood copy;
- Dusty Steel interaction states;
- restrained Champagne Rose Gold premium detail;
- Manrope/Inter live typography;
- CSS-built cards, controls, dividers, forms and responsive layouts;
- validated product/manufacturer imagery only when tied to a validated commerce item;
- clean text-free editorial photography only when it has been explicitly approved.

This avoids baking prices, availability, founder identities, support hours, slogans or other mutable information into image files.

See `website/asset-map.md` for the route-by-route visual assignment and `brand/assets/asset-manifest.json` for publication status.''')

# 3. Create one canonical production source of truth.
write("docs/production-source-of-truth.md", f'''# LuxSync Website Production Source of Truth

**Status:** FINAL launch source-of-truth baseline  
**Brand system:** {BRAND_SYSTEM}  
**Official slogan:** {SLOGAN}

This file is the shortest path through the repository. When two active files appear to conflict, this hierarchy wins:

1. `brand/README.md`, `brand/colors.md`, `brand/typography.md`, `brand/voice-and-tone.md`
2. `website/styles/design-system.md`
3. `website/implementation-manifest.json` and `website/asset-map.md`
4. page blueprints under `website/pages/`
5. approved copy under `content/`
6. architecture and operational detail under `docs/`
7. reusable prompts under `prompts/`

## Locked identity

- Official slogan: **{SLOGAN}**
- Primary CTA: **{PRIMARY_CTA}**
- Secondary CTA: **{SECONDARY_CTA}**
- Concierge: **LuxSync Intelligent Living Concierge**
- Result: **My LuxSync Blueprint**
- Bridgette Beardsley: **{BRIDGETTE_TITLE}**
- Sheldon Bardol: **{SHELDON_TITLE}**

## Locked website model

LuxSync begins with lifestyle outcomes and compatible intelligent-living experiences, then recommends technology categories and validated products. It is not positioned as a traditional on-site installation company unless a future approved decision changes the model.

## Canonical page set

- Home
- Find My LuxSync Solution / Concierge
- My LuxSync Blueprint
- Solutions hub
- Commercial Offices
- Senior Living / Nursing Homes
- Short-Term Rentals
- Residential Living
- Seniors / Caregivers / Aging in Place
- Shop / product collections
- Guides / ROI library
- About / founders
- FAQs
- Contact / Support

## Contact contract

The adaptive Contact page begins with Support, Product Information, Consultation, General Question, Business / Partnership, or Other. It reveals only the fields needed for the selected path and shares Property Profile conventions with the Concierge.

## Commerce contract

Names, prices, inventory, ratings, availability, subscriptions, compatibility and product imagery must come from validated commerce/manufacturer data. Never invent ratings, scarcity, stock status, warranties, shipping promises, testimonials or prices.

## Visual contract

Use exact logo masters plus live HTML/CSS for the active site. The imported raster slices outside `brand/assets/01-logos/` are reference-only until clean publication-safe exports are created. Do not publish generated logo approximations, baked support hours, fake founder identities, retired copy, or board-crop fragments.

## Implementation handoff

A site builder should begin with:

1. `website/implementation-manifest.json`
2. `website/navigation.md`
3. `website/asset-map.md`
4. `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md`
5. `docs/checklists/CL-001-Airo-First-Pass-Review.md`

The Concierge implementation source is `website/src/concierge/`, including the generated `luxsync-concierge-engine.v1.json` configuration.''')

# 4. Route and visual implementation map.
write("website/asset-map.md", f'''# LuxSync Website Asset Map

**Status:** Active / Authoritative  
**Brand system:** {BRAND_SYSTEM}

## Production-safe visual primitives

- Primary horizontal mark: `brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png`
- Alternate horizontal mark: `brand/assets/01-logos/LuxSync_Logo_Horizontal_Final.png`
- Compact/orb mark: `brand/assets/01-logos/LuxSync_Logo_Orb.png`
- Live UI: HTML/CSS using `website/styles/design-system.md`

Do not publish direct raster assets from `brand/assets/02-icons/` through `brand/assets/09-stationery/`. Those files remain reference-only after visual QA.

## Route visual assignments

| Route | Blueprint | Production visual assignment |
|---|---|---|
| `/` | `website/pages/home.md` | Horizontal Combo logo + live editorial Plush Drift hero; product/solution cards built live |
| `/find-my-luxsync-solution` | `website/pages/concierge.md` | Orb or Horizontal Combo logo + live Concierge cards/progress UI |
| `/my-luxsync-blueprint` | `website/pages/my-luxsync-blueprint.md` | Horizontal Combo logo + live Blueprint hierarchy/cards |
| `/solutions` | `website/pages/solutions.md` | Horizontal Combo logo + live audience pathway cards |
| `/solutions/commercial-offices` | `website/pages/solutions/commercial-offices.md` | Horizontal Combo logo + live architectural office composition |
| `/solutions/senior-living` | `website/pages/solutions/senior-living.md` | Horizontal Combo logo + live calm accessible-living composition |
| `/solutions/short-term-rentals` | `website/pages/solutions/short-term-rentals.md` | Horizontal Combo logo + live hosting/property composition |
| `/solutions/residential` | `website/pages/solutions/residential.md` | Horizontal Combo logo + live residential intelligent-living composition |
| `/solutions/aging-in-place` | `website/pages/solutions/aging-in-place.md` | Horizontal Combo logo + live accessible-living composition |
| `/shop` and collection routes | `website/pages/shop.md` | Horizontal Combo logo + validated commerce/manufacturer product imagery only |
| `/guides` | `website/pages/guides.md` | Horizontal Combo logo + live ROI editorial card system |
| `/about` | `website/pages/about.md` | Horizontal Combo logo + live founder profile layout; real approved portraits only if supplied |
| `/faqs` | `website/pages/faqs.md` | Orb logo + live FAQ search/accordion composition |
| `/contact` | `website/pages/contact.md` | Orb logo + live adaptive intent cards and form |

## Reference-only material

The imported composites under `brand/assets/07-heroes/` and `brand/assets/08-sections/`, plus the cropped icon/button/control/divider/product-card files, may inform spacing, lighting and mood only. They must not be placed on live pages because they contain or may contain baked/generated text, generated logo approximations, mutable claims, or crop artifacts.

## Rule for future clean imagery

A new image becomes production-safe only when it is text-free where practical, contains no regenerated LuxSync logo, contains no mutable commerce/support claims, uses approved visual language, and is explicitly added to the manifest with `publication_status: production-approved`.''')

routes = [
    {"route":"/","blueprint":"website/pages/home.md","content_source":"content/homepage.md","production_assets":["brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png"],"visual_recipe":"live-editorial-hero"},
    {"route":"/find-my-luxsync-solution","blueprint":"website/pages/concierge.md","content_source":"docs/architecture/intelligent-living-concierge.md","production_assets":["brand/assets/01-logos/LuxSync_Logo_Orb.png"],"visual_recipe":"live-concierge-ui"},
    {"route":"/my-luxsync-blueprint","blueprint":"website/pages/my-luxsync-blueprint.md","content_source":"website/src/concierge/modules/63-blueprint-schema.json","production_assets":["brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png"],"visual_recipe":"live-blueprint-ui"},
    {"route":"/solutions","blueprint":"website/pages/solutions.md","content_source":"content/product-catalog.md","production_assets":["brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png"],"visual_recipe":"live-solution-cards"},
    {"route":"/solutions/commercial-offices","blueprint":"website/pages/solutions/commercial-offices.md","content_source":"content/guides/roi/commercial-offices.md","production_assets":["brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png"],"visual_recipe":"live-office-composition"},
    {"route":"/solutions/senior-living","blueprint":"website/pages/solutions/senior-living.md","content_source":"content/guides/roi/senior-living-communities.md","production_assets":["brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png"],"visual_recipe":"live-accessible-living-composition"},
    {"route":"/solutions/short-term-rentals","blueprint":"website/pages/solutions/short-term-rentals.md","content_source":"content/guides/roi/str-owners.md","production_assets":["brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png"],"visual_recipe":"live-hosting-property-composition"},
    {"route":"/solutions/residential","blueprint":"website/pages/solutions/residential.md","content_source":"content/guides/roi/residential-homeowners.md","production_assets":["brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png"],"visual_recipe":"live-residential-composition"},
    {"route":"/solutions/aging-in-place","blueprint":"website/pages/solutions/aging-in-place.md","content_source":"content/guides/roi/residential-seniors-caregivers.md","production_assets":["brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png"],"visual_recipe":"live-accessible-living-composition"},
    {"route":"/shop","blueprint":"website/pages/shop.md","content_source":"content/product-catalog.md","production_assets":["brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png"],"visual_recipe":"live-commerce-grid-with-validated-imagery"},
    {"route":"/guides","blueprint":"website/pages/guides.md","content_source":"content/guides/roi/README.md","production_assets":["brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png"],"visual_recipe":"live-roi-editorial-cards"},
    {"route":"/about","blueprint":"website/pages/about.md","content_source":"content/about.md","production_assets":["brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png"],"visual_recipe":"live-founder-layout"},
    {"route":"/faqs","blueprint":"website/pages/faqs.md","content_source":"content/faqs.md","production_assets":["brand/assets/01-logos/LuxSync_Logo_Orb.png"],"visual_recipe":"live-faq-accordion"},
    {"route":"/contact","blueprint":"website/pages/contact.md","content_source":"content/contact.md","production_assets":["brand/assets/01-logos/LuxSync_Logo_Orb.png"],"visual_recipe":"live-adaptive-contact-form"},
]
manifest_impl = {
    "version":"1.0",
    "status":"production-source-of-truth",
    "brand_system":BRAND_SYSTEM,
    "official_slogan":SLOGAN,
    "primary_cta":PRIMARY_CTA,
    "secondary_cta":SECONDARY_CTA,
    "asset_map":"website/asset-map.md",
    "navigation":"website/navigation.md",
    "design_system":"website/styles/design-system.md",
    "routes":routes,
}
write("website/implementation-manifest.json", json.dumps(manifest_impl, indent=2))

write("website/navigation.md", f'''# LuxSync Navigation and Footer Contract

**Status:** Active / Authoritative  
**Brand system:** {BRAND_SYSTEM}

## Header

Primary navigation:

- Shop → `/shop`
- Solutions → `/solutions`
- Guides → `/guides`
- About → `/about`
- FAQs → `/faqs`
- Contact → `/contact`

Persistent utilities where supported by the commerce implementation:

- Search
- Account
- Cart

Primary header CTA: **{PRIMARY_CTA}** → `/find-my-luxsync-solution`

## Solutions submenu

- Commercial Offices
- Senior Living & Nursing Homes
- Short-Term Rentals
- Residential Living
- Seniors, Caregivers & Aging in Place

## Footer

- Shop
- Solutions
- Guides
- About
- FAQs
- Contact
- Support → `/contact?intent=support`
- Privacy placeholder until approved legal copy exists
- Terms placeholder until approved legal copy exists
- Social links only for approved active channels

Do not create dead navigation, invented social accounts, or unsupported commerce utilities.''')

# 5. Complete missing page blueprints.
write("website/pages/concierge.md", f'''# Find My LuxSync Solution / Intelligent Living Concierge

**Status:** Active production blueprint  
**Route:** `/find-my-luxsync-solution`  
**Engine:** `website/src/concierge/luxsync-concierge-engine.v1.json`

## Purpose

The **LuxSync Intelligent Living Concierge** is the flagship discovery experience. It begins with the customer's space, routines, priorities and existing technology, then recommends intelligent-living experiences before exact products.

Journey contract: **Lifestyle → Experience → Intelligence → Technology**.

## Flow

1. Welcome and intent
2. Property Profile
3. Existing technology
4. Lifestyle goals and pain points
5. Ranked priorities
6. Compatibility/foundation analysis
7. Recommended LuxSync Experiences
8. Implementation path and phased roadmap
9. **My LuxSync Blueprint** reveal
10. Next best action

Implementation paths remain **Essential Intelligence**, **Elevated Living**, and **Complete LuxSync Experience**.

## Visual assignment

Use `brand/assets/01-logos/LuxSync_Logo_Orb.png` or the exact horizontal master with live HTML/CSS cards, progress states and accessible controls. Do not publish flattened Concierge screenshots or imported raster composites.

Primary CTA: **Build My LuxSync Blueprint**. Preserve Back/Continue behavior, answers and accessible focus states. Do not present the experience as a novelty quiz.

See `website/asset-map.md` and `docs/architecture/intelligent-living-concierge.md`.''')

write("website/pages/my-luxsync-blueprint.md", f'''# My LuxSync Blueprint

**Status:** Active production blueprint  
**Route:** `/my-luxsync-blueprint`  
**Schema:** `website/src/concierge/modules/63-blueprint-schema.json`

## Purpose

Present the Concierge result as an understandable intelligent-living plan, not a product dump.

## Hierarchy

1. Your Space
2. What Matters Most
3. Intelligent Living Profile
4. Recommended LuxSync Experiences
5. Foundation and compatibility context
6. Implementation path
7. Phased roadmap
8. Technology behind the experience
9. Why LuxSync Chose This
10. Next best action

Exact products appear only when validated commerce and compatibility data exists. Otherwise show capability/device categories and clearly label them as planning recommendations.

## Visual assignment

Use the exact horizontal logo plus live Blueprint cards and hierarchy built from the design system. Do not use imported product-card raster slices as commerce UI.

Primary actions may include Shop Compatible Products, Save/Email Blueprint where implemented, Request a Consultation, or Refine My Priorities according to engine CTA logic.''')

write("website/pages/solutions.md", f'''# LuxSync Solutions Hub

**Status:** Active production blueprint  
**Route:** `/solutions`

Lead with outcomes and audience context, then connect visitors to the Concierge, ROI library and validated product collections.

## Pathways

- Commercial Offices
- Senior Living & Nursing Homes
- Short-Term Rentals
- Residential Living
- Seniors, Caregivers & Aging in Place

Each pathway should answer: what outcomes matter, which LuxSync Experiences are relevant, which technology categories may support them, and what the next best action is.

## Visual assignment

Use the exact horizontal logo and live Plush Drift pathway cards. No flattened generated solution boards.

Primary CTA: **{PRIMARY_CTA}**. Secondary paths: **Get the ROI Guide** and **Contact LuxSync**.''')

solution_pages = {
"website/pages/solutions/commercial-offices.md": '''# Commercial Offices

**Status:** Active production blueprint  
**Route:** `/solutions/commercial-offices`  
**ROI source:** `content/guides/roi/commercial-offices.md`

Focus on comfort, energy visibility, lighting, access, shared-space consistency, property awareness and simplified operations without inventing savings claims.

Relevant experience themes may include intelligent lighting, climate routines, access, energy awareness and property pulse. Exact devices and economics must come from validated data.

CTAs: **Find My LuxSync Solution**, **Commercial Offices ROI Guide**, **Request a Consultation**.

**Visual assignment:** exact horizontal LuxSync logo with a live architectural office composition using approved brand tokens.''',
"website/pages/solutions/senior-living.md": '''# Senior Living & Nursing Homes

**Status:** Active production blueprint  
**Route:** `/solutions/senior-living`  
**ROI sources:** `content/guides/roi/senior-living-communities.md` and `content/guides/roi/nursing-homes.md`

Focus on accessible living, comfort, lighting, environmental awareness, simplified routines and operational visibility. Do not make medical-monitoring, emergency-response or clinical-outcome claims unless a future validated product/service contract supports them.

Relevant experience themes may include Accessible Living, lighting routines, climate comfort, water awareness and property pulse.

CTAs: **Find My LuxSync Solution**, **Senior Living ROI Guide**, **Request a Consultation**.

**Visual assignment:** exact horizontal LuxSync logo with a live calm accessible-living composition using approved brand tokens.''',
"website/pages/solutions/short-term-rentals.md": '''# Short-Term Rentals

**Status:** Active production blueprint  
**Route:** `/solutions/short-term-rentals`  
**ROI sources:** `content/guides/roi/str-owners.md`, `str-operators.md`, and `str-managers.md`

Focus on Guest Ready, access, climate consistency, property awareness, water protection and repeatable turnover routines. Do not invent occupancy, review-score or labor-savings claims.

Relevant experience themes may include Guest Ready, Property Pulse, Water Watch, Welcome Home and Goodnight depending on property context.

CTAs: **Find My LuxSync Solution**, **Choose an STR ROI Guide**, **Request a Consultation**.

**Visual assignment:** exact horizontal LuxSync logo with a live hosting/property composition using approved brand tokens.''',
"website/pages/solutions/residential.md": '''# Residential Living

**Status:** Active production blueprint  
**Route:** `/solutions/residential`  
**ROI source:** `content/guides/roi/residential-homeowners.md`

Lead with comfort, control, confidence and routines rather than gadget count. Connect homeowners, busy professionals and families to Concierge-driven experiences and compatible technology categories.

Relevant experience themes may include Welcome Home, Goodnight, lighting and ambience, comfort and climate, security awareness, water protection, entertainment and energy awareness.

CTAs: **Find My LuxSync Solution**, **Residential ROI Guides**, **Shop Smart Home**.

**Visual assignment:** exact horizontal LuxSync logo with a live residential intelligent-living composition using approved brand tokens.''',
"website/pages/solutions/aging-in-place.md": '''# Seniors, Caregivers & Aging in Place

**Status:** Active production blueprint  
**Route:** `/solutions/aging-in-place`  
**ROI source:** `content/guides/roi/residential-seniors-caregivers.md`

Focus on independence, accessibility, easier routines, comfort, awareness and caregiver collaboration without implying medical care or guaranteed safety outcomes.

Relevant experience themes may include Accessible Living, lighting routines, simplified controls, environmental awareness and water protection.

CTAs: **Find My LuxSync Solution**, **Seniors & Caregivers ROI Guide**, **Request a Consultation**.

**Visual assignment:** exact horizontal LuxSync logo with a live accessible-living composition using approved brand tokens.''',
}
for rel, body in solution_pages.items():
    write(rel, body.replace("Find My LuxSync Solution", PRIMARY_CTA))

write("website/pages/shop.md", f'''# LuxSync Shop and Collection Blueprint

**Status:** Active production blueprint  
**Route:** `/shop`  
**Catalog source:** `content/product-catalog.md`

## Customer-facing collections

- Foundation & Connectivity
- Entry & Access
- Lighting & Ambience
- Comfort & Climate
- Property Awareness
- Water Protection
- Energy & Power
- Entertainment
- Hosting / Short-Term Rental
- Curated Bundles

## Commerce rules

Only validated live products and validated bundles may appear purchasable. Planning product families and LuxSync Experience concepts must be labeled clearly and must not masquerade as SKUs.

Names, prices, stock, ratings, shipping, warranties, subscription requirements, compatibility and product images must come from validated commerce/manufacturer data. No invented badges, review counts, scarcity or promotional claims.

## Visual assignment

Use the exact horizontal logo. Build collection and product cards live with HTML/CSS. Do not use `brand/assets/06-product-cards/` as public commerce cards; those imported slices are reference-only.

Primary CTA from category pages: **Add to Cart** only when backed by a validated live commerce item. Discovery CTA: **{PRIMARY_CTA}**.''')

# 6. Wire existing page blueprints to the canonical live visual system.
assignments = {
"website/pages/home.md": f'''## Production Visual Assignment

Use `brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png` in a live editorial hero composed with Slate Navy / Dark Suede, Pale Driftwood copy, Dusty Steel interaction cues and restrained Champagne Rose Gold detail. Build solution, Concierge, founder, FAQ, ROI and commerce cards live in HTML/CSS. Imported raster composites and board slices are reference-only. See `website/asset-map.md`.''',
"website/pages/about.md": '''## Production Visual Assignment

Use the exact horizontal LuxSync logo and a live balanced founder layout. Use founder copy from `docs/leadership/`. Do not invent portraits or use generated founder identities. If approved founder portraits are not supplied, use elegant non-person placeholder treatments rather than synthetic people. See `website/asset-map.md`.''',
"website/pages/faqs.md": '''## Production Visual Assignment

Use the exact LuxSync orb plus live FAQ search, category navigation and accessible accordions. Do not publish raster artwork containing baked support hours or generated copy. See `website/asset-map.md`.''',
"website/pages/contact.md": '''## Production Visual Assignment

Use the exact LuxSync orb plus live adaptive intent cards and forms. Support hours, response times and service promises must remain live copy only when explicitly approved. Do not bake contact information into imagery. See `website/asset-map.md`.''',
"website/pages/guides.md": '''## Production Visual Assignment

Use the exact horizontal LuxSync logo plus live editorial ROI guide cards. Audience names, formulas, limitations and download actions remain native text. Do not publish a flattened generated ROI cover as the authoritative content source. See `website/asset-map.md`.''',
}
for rel, content in assignments.items():
    append_once(rel, "## Production Visual Assignment", content)

# 7. Reconcile architecture, prompts and operations around the new canonical files.
append_once("docs/architecture/website-information-architecture.md", "## Production Route Baseline", f'''## Production Route Baseline

The authoritative route/blueprint matrix is `website/implementation-manifest.json`. Navigation is governed by `website/navigation.md`, and production visual usage is governed by `website/asset-map.md`.

Required launch routes include Home, Concierge, My LuxSync Blueprint, Solutions hub, Commercial Offices, Senior Living, Short-Term Rentals, Residential, Aging in Place, Shop, Guides, About, FAQs and Contact.''')

append_once("docs/architecture/intelligent-living-concierge.md", "## Production Implementation Handoff", '''## Production Implementation Handoff

- Page blueprint: `website/pages/concierge.md`
- Result blueprint: `website/pages/my-luxsync-blueprint.md`
- Engine modules: `website/src/concierge/modules/`
- Generated production configuration: `website/src/concierge/luxsync-concierge-engine.v1.json`
- Field dictionary: `website/src/concierge/luxsync-concierge-engine-field-map.md`

The generated configuration is rebuilt and checked in CI so implementation cannot drift from the tracked modules.''')

append_once("docs/master-catalog.md", "## Production Completion Baseline", f'''## Production Completion Baseline

**Authoritative visual system:** {BRAND_SYSTEM}  
**Official slogan:** {SLOGAN}

Canonical website implementation references:

- `docs/production-source-of-truth.md`
- `website/implementation-manifest.json`
- `website/asset-map.md`
- `website/navigation.md`
- `website/pages/`
- `website/src/concierge/luxsync-concierge-engine.v1.json`

The imported non-logo raster slices are reference-only and must not be published directly.''')

append_once("docs/project-runbook.md", "## Production Source-of-Truth Handoff", f'''## Production Source-of-Truth Handoff

The current website source-of-truth baseline is `{BRAND_SYSTEM}` with the implementation manifest at `website/implementation-manifest.json`. Use `docs/production-source-of-truth.md` as the first operational reference and `website/asset-map.md` for visual publication rules.''')

append_once("docs/value-proposition.md", "## Production Website Handoff", f'''## Production Website Handoff

Website implementation is governed by `{BRAND_SYSTEM}`, `docs/production-source-of-truth.md`, and `website/implementation-manifest.json`. The official public slogan remains **{SLOGAN}**.''')

append_once("docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md", "## Production Input Set", '''## Production Input Set

Before generating or revising the site, load these authoritative inputs in order:

1. `docs/production-source-of-truth.md`
2. `website/implementation-manifest.json`
3. `website/navigation.md`
4. `website/asset-map.md`
5. page blueprints under `website/pages/`
6. approved copy under `content/`

Use exact logo masters and live HTML/CSS. Do not import reference-only raster composites as public UI.''')

append_once("docs/checklists/CL-001-Airo-First-Pass-Review.md", "## Production Source-of-Truth Checks", '''## Production Source-of-Truth Checks

- Every required route in `website/implementation-manifest.json` exists.
- Header/footer match `website/navigation.md`.
- Only production-approved assets from `website/asset-map.md` are published.
- No generated logo approximations, baked support hours, fake founder identities or raster product-card fragments appear.
- Concierge uses the tracked production engine configuration.
- My LuxSync Blueprint recommends experiences before products.
- Commerce facts come from validated data.
- Contact begins with the approved adaptive intent branches.''')

append_once("prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md", "## Mandatory Production Source-of-Truth Inputs", f'''## Mandatory Production Source-of-Truth Inputs

Before generating the website, read and obey:

- `docs/production-source-of-truth.md`
- `website/implementation-manifest.json`
- `website/navigation.md`
- `website/asset-map.md`
- `website/styles/design-system.md`

Use **{SLOGAN}** as the sole public slogan. Use the exact protected logo files. Build buttons, cards, forms, icons, dividers, Concierge UI and Contact UI as live HTML/CSS. Do not publish the reference-only raster composites, generated logo approximations, baked founder/support information or board-crop fragments under `brand/assets/02-icons/` through `brand/assets/09-stationery/`.''')

append_once("prompts/content-writer.md", "## Production Source-of-Truth", '''## Production Source-of-Truth

Use `docs/production-source-of-truth.md` for current naming, routes, founder titles and public claims. Do not write copy that depends on baked image text or unvalidated commerce facts.''')

append_once("content/product-catalog.md", "## Website Display Contract", '''## Website Display Contract

The shop implementation is `website/pages/shop.md`. Product and collection surfaces are built live. The imported files under `brand/assets/06-product-cards/` are reference-only and must not supply product names, prices, ratings, inventory or imagery for live commerce.''')

append_once("website/src/README.md", "## Production Website Handoff", '''## Production Website Handoff

The route contract is `website/implementation-manifest.json`; navigation is `website/navigation.md`; visual publication rules are `website/asset-map.md`. The Concierge engine under `website/src/concierge/` is the primary executable website source currently tracked in this repository.''')

# 8. Update the normal CI workflow and validators.
write(".github/workflows/validate-repository-consistency.yml", '''name: Validate LuxSync repository consistency

on:
  pull_request:
    branches:
      - master
  push:
    branches:
      - master
  workflow_dispatch:

permissions:
  contents: read

jobs:
  validate:
    runs-on: ubuntu-latest

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Validate production brand library
        run: python scripts/validate-production-brand.py

      - name: Validate repository source of truth
        run: python scripts/validate-repository-consistency.py

      - name: Verify Concierge production engine is current
        run: |
          node website/src/concierge/assemble-engine.mjs
          git diff --exit-code -- website/src/concierge/luxsync-concierge-engine.v1.json

      - name: Validate whitespace
        run: git diff --check
''')

write("scripts/validate-production-brand.py", '''#!/usr/bin/env python3
from pathlib import Path
import json, struct

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "brand/assets"
SOURCE = ROOT / "brand/source-logo"
errors = []
expected = {
    "01-logos": 3,
    "02-icons": 15,
    "03-buttons": 18,
    "04-ui-controls": 25,
    "05-dividers-accents": 24,
    "06-product-cards": 4,
    "07-heroes": 4,
    "08-sections": 3,
    "09-stationery": 4,
}
logos = ["LuxSync_Logo_Horizontal_Combo.png", "LuxSync_Logo_Horizontal_Final.png", "LuxSync_Logo_Orb.png"]
for name in logos:
    src = SOURCE / name
    dst = ASSETS / "01-logos" / name
    if not src.exists(): errors.append(f"missing authoritative logo master: {name}")
    if not dst.exists(): errors.append(f"missing production logo copy: {name}")
    elif src.read_bytes() != dst.read_bytes(): errors.append(f"production logo differs from authoritative master: {name}")
for folder, count in expected.items():
    p = ASSETS / folder
    actual = len(list(p.glob("*.png"))) if p.exists() else 0
    if actual != count: errors.append(f"brand/assets/{folder}: expected {count} PNG files; found {actual}")
if list(ASSETS.rglob("*.svg")):
    errors.append("placeholder SVG files remain under brand/assets")
for p in ASSETS.rglob("*.png"):
    data = p.read_bytes()
    if not data.startswith(b"\\x89PNG\\r\\n\\x1a\\n") or data[12:16] != b"IHDR":
        errors.append(f"invalid PNG: {p.relative_to(ROOT)}")
        continue
    width, height = struct.unpack(">II", data[16:24])
    if width < 32 or height < 32: errors.append(f"implausibly small PNG: {p.relative_to(ROOT)}")
manifest_path = ASSETS / "asset-manifest.json"
if not manifest_path.exists():
    errors.append("missing brand/assets/asset-manifest.json")
else:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("version") != "5.1-production-source-of-truth": errors.append("asset manifest version mismatch")
    if manifest.get("source_of_truth") != "brand/assets": errors.append("asset manifest source_of_truth mismatch")
    if manifest.get("official_slogan") != "Where Luxury Lives Intelligently": errors.append("asset manifest slogan mismatch")
    statuses = manifest.get("status_by_folder", {})
    if statuses.get("01-logos") != "production-approved": errors.append("logo folder must be production-approved")
    for folder in expected:
        if folder != "01-logos" and statuses.get(folder) != "reference-only": errors.append(f"{folder} must be reference-only")
    files = manifest.get("files", [])
    if len(files) != sum(expected.values()): errors.append(f"asset manifest expected {sum(expected.values())} files; found {len(files)}")
    for item in files:
        path = Path(item.get("path", ""))
        status = item.get("publication_status")
        if "01-logos" in path.parts and status != "production-approved": errors.append(f"wrong publication status: {path}")
        if "01-logos" not in path.parts and status != "reference-only": errors.append(f"wrong publication status: {path}")
for rel in ("brand/README.md", "brand/assets/README.md", "brand/colors.md", "website/styles/design-system.md"):
    p = ROOT / rel
    if not p.exists(): errors.append(f"missing governing file: {rel}")
    else:
        text = p.read_text(encoding="utf-8")
        for token in ("#7B96B2", "#D6B0A0", "Brushed Dusty Steel"):
            if token not in text: errors.append(f"{rel}: missing {token}")
if errors:
    print("LuxSync production brand validation FAILED:")
    for error in errors: print("-", error)
    raise SystemExit(1)
print("LuxSync production brand validation PASSED")
''')

old_brand_validator = ROOT / "scripts/validate-brand-v3.py"
if old_brand_validator.exists():
    old_brand_validator.unlink()

write("scripts/validate-repository-consistency.py", f'''#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRAND_SYSTEM = {BRAND_SYSTEM!r}
SLOGAN = {SLOGAN!r}
PRIMARY_CTA = {PRIMARY_CTA!r}
SECONDARY_CTA = {SECONDARY_CTA!r}
BRIDGETTE_TITLE = {BRIDGETTE_TITLE!r}
SHELDON_TITLE = {SHELDON_TITLE!r}
CONCIERGE = "LuxSync Intelligent Living Concierge"
BLUEPRINT = "My LuxSync Blueprint"
SAFE_ASSETS = {{
    "brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png",
    "brand/assets/01-logos/LuxSync_Logo_Horizontal_Final.png",
    "brand/assets/01-logos/LuxSync_Logo_Orb.png",
}}
RETIRED_HERO = "Smart Living" + ". " + "Elevated" + "."
LEGACY_TERMS = [
    "LuxSync " + "v3",
    "Brand System " + "4.0",
    "assets" + "-v3",
    "migrate-brand-" + "v3.py",
    "validate-brand-" + "v3.py",
    "RB-007-Brand-Asset-" + "Raster-Regeneration.md",
    "RB-008-Luxury-Orbit-" + "Brand-Asset-Generation.md",
]
REQUIRED_FILES = [
    "README.md",
    "brand/README.md",
    "brand/colors.md",
    "brand/typography.md",
    "brand/voice-and-tone.md",
    "brand/assets/README.md",
    "brand/assets/asset-manifest.json",
    "docs/production-source-of-truth.md",
    "docs/production-asset-library.md",
    "docs/master-catalog.md",
    "docs/project-runbook.md",
    "docs/value-proposition.md",
    "docs/architecture/website-information-architecture.md",
    "docs/architecture/intelligent-living-concierge.md",
    "content/homepage.md",
    "content/about.md",
    "content/faqs.md",
    "content/contact.md",
    "content/product-catalog.md",
    "content/guides/roi/README.md",
    "website/implementation-manifest.json",
    "website/navigation.md",
    "website/asset-map.md",
    "website/styles/design-system.md",
    "website/pages/home.md",
    "website/pages/concierge.md",
    "website/pages/my-luxsync-blueprint.md",
    "website/pages/solutions.md",
    "website/pages/solutions/commercial-offices.md",
    "website/pages/solutions/senior-living.md",
    "website/pages/solutions/short-term-rentals.md",
    "website/pages/solutions/residential.md",
    "website/pages/solutions/aging-in-place.md",
    "website/pages/shop.md",
    "website/pages/guides.md",
    "website/pages/about.md",
    "website/pages/faqs.md",
    "website/pages/contact.md",
    "website/src/concierge/luxsync-concierge-engine.v1.json",
    "scripts/validate-production-brand.py",
]
ROI_FILES = [
    "commercial-offices.md", "nursing-homes.md", "senior-living-communities.md",
    "str-owners.md", "str-operators.md", "str-managers.md",
    "residential-homeowners.md", "residential-busy-professionals.md",
    "residential-intentional-parents.md", "residential-seniors-caregivers.md",
]
errors = []

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8", errors="replace")

def require(rel, token):
    if token not in read(rel): errors.append(f"{{rel}}: missing required token {{token!r}}")

for rel in REQUIRED_FILES:
    if not (ROOT / rel).exists(): errors.append(f"missing required file: {{rel}}")
if errors:
    print("LuxSync repository validation FAILED:")
    for e in errors: print("-", e)
    raise SystemExit(1)

# Active text must not preserve retired branding or retired generation paths.
text_suffixes = {{".md", ".txt", ".json", ".yml", ".yaml", ".py", ".js", ".mjs", ".css", ".html"}}
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in text_suffixes: continue
    if any(part in {{".git", "node_modules"}} for part in path.parts): continue
    text = path.read_text(encoding="utf-8", errors="replace")
    if RETIRED_HERO in text: errors.append(f"{{path.relative_to(ROOT)}}: retired hero phrase remains")
    for term in LEGACY_TERMS:
        if term in text: errors.append(f"{{path.relative_to(ROOT)}}: retired source-of-truth term remains: {{term}}")

for rel in (
    "docs/production-source-of-truth.md", "brand/README.md", "website/styles/design-system.md",
    "website/pages/home.md", "website/navigation.md", "website/asset-map.md",
    "prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md",
):
    for token in (BRAND_SYSTEM, SLOGAN): require(rel, token)

for rel in ("docs/leadership/bridgette-beardsley.md", "website/pages/home.md", "website/pages/about.md", "docs/master-catalog.md"):
    require(rel, BRIDGETTE_TITLE)
for rel in ("docs/leadership/sheldon-bardol.md", "website/pages/home.md", "website/pages/about.md", "docs/master-catalog.md"):
    require(rel, SHELDON_TITLE)

for rel in ("website/pages/home.md", "website/pages/concierge.md", "docs/architecture/intelligent-living-concierge.md", "docs/production-source-of-truth.md"):
    for token in (PRIMARY_CTA, CONCIERGE, BLUEPRINT): require(rel, token)

for token in ("Support", "Product Information", "Consultation", "General Question", "Business / Partnership", "property_type", "square_feet_exact", "square_feet_band"):
    require("website/pages/contact.md", token)
for token in ("support@luxsync.net", "info@luxsync.net"):
    require("content/contact.md", token)
    require("website/pages/contact.md", token)

for filename in ROI_FILES:
    rel = f"content/guides/roi/{{filename}}"
    require(rel, SLOGAN)
    require(rel, "ROI")
for token in ("Commercial Offices", "Nursing Homes", "Senior Living Communities", "STR Owners", "STR Operators", "STR Managers", "Seniors, Caregivers"):
    require("content/guides/roi/README.md", token)
    require("website/pages/guides.md", token)

for token in ("Physical Product Families", "Curated Bundle", "LuxSync Experiences", "Validated Live Product", "Solution Concept"):
    require("content/product-catalog.md", token)

# Route manifest must be complete, internally resolvable, and publication-safe.
impl = json.loads(read("website/implementation-manifest.json"))
if impl.get("brand_system") != BRAND_SYSTEM: errors.append("implementation manifest brand_system mismatch")
if impl.get("official_slogan") != SLOGAN: errors.append("implementation manifest slogan mismatch")
required_routes = {{
    "/", "/find-my-luxsync-solution", "/my-luxsync-blueprint", "/solutions",
    "/solutions/commercial-offices", "/solutions/senior-living", "/solutions/short-term-rentals",
    "/solutions/residential", "/solutions/aging-in-place", "/shop", "/guides", "/about", "/faqs", "/contact",
}}
routes = impl.get("routes", [])
route_names = {{r.get("route") for r in routes}}
if route_names != required_routes:
    errors.append(f"implementation manifest route set mismatch: {{sorted(route_names ^ required_routes)}}")
for route in routes:
    for key in ("blueprint", "content_source"):
        rel = route.get(key)
        if not rel or not (ROOT / rel).exists(): errors.append(f"{{route.get('route')}}: invalid {{key}} {{rel!r}}")
    assets = route.get("production_assets", [])
    if not assets: errors.append(f"{{route.get('route')}}: no production asset assigned")
    for asset in assets:
        if asset not in SAFE_ASSETS: errors.append(f"{{route.get('route')}}: reference-only asset wired as production: {{asset}}")
        if not (ROOT / asset).exists(): errors.append(f"{{route.get('route')}}: missing asset: {{asset}}")

# Page blueprints may not directly wire reference-only imported slices.
reference_prefixes = tuple(f"brand/assets/{{n:02d}}-" for n in range(2, 10))
for path in (ROOT / "website/pages").rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    for prefix in reference_prefixes:
        if prefix in text: errors.append(f"{{path.relative_to(ROOT)}}: reference-only raster path is wired directly")

for token in ("/shop", "/solutions", "/guides", "/about", "/faqs", "/contact", PRIMARY_CTA):
    require("website/navigation.md", token)

engine = json.loads(read("website/src/concierge/luxsync-concierge-engine.v1.json"))
for key in ("meta", "constants", "experience_catalog", "questionnaire", "scoring", "compatibility", "blueprint_schema"):
    if key not in engine: errors.append(f"Concierge engine missing top-level key: {{key}}")

workflow = read(".github/workflows/validate-repository-consistency.yml")
for token in ("validate-production-brand.py", "validate-repository-consistency.py", "assemble-engine.mjs"):
    if token not in workflow: errors.append(f"CI workflow missing {{token}}")

if (ROOT / "docs/business-plan.md").exists() and "Pricing status: unresolved" not in read("docs/business-plan.md"):
    errors.append("senior-service pricing must remain explicitly unresolved")

if errors:
    print("LuxSync repository validation FAILED:")
    for error in errors: print("-", error)
    raise SystemExit(1)
print("LuxSync repository validation PASSED")
print(f"Brand system: {{BRAND_SYSTEM}}")
print(f"Slogan: {{SLOGAN}}")
print(f"Routes: {{len(routes)}}")
''')

# Remove the temporary script and its workflow before the resulting commit.
for rel in ("scripts/complete-production-source-of-truth.py", ".github/workflows/complete-production-source-of-truth.yml"):
    p = ROOT / rel
    if p.exists():
        p.unlink()

print("LuxSync production source-of-truth reconciliation complete.")

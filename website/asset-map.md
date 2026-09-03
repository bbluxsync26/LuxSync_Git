# LuxSync Website Asset Map

**Status:** Active / Authoritative
**Brand system:** LuxSync Production Raster v5

## Visual source hierarchy

The website consumes the LuxSync omnichannel brand system. It does not define the brand library.

For visual selection use this hierarchy:

1. protected logo masters and approved logo deliveries;
2. faithful approved-board artwork when the approved metallic LuxSync visual itself is intended;
3. clean semantic vectors for compact/scalable interface illustration where exact board styling is not required;
4. live HTML/CSS for interactive controls, cards, navigation, forms and mutable content.

## Exact logos

- Primary horizontal mark: `brand/assets/logos/png/luxsync-horizontal-combo.png`
- Alternate horizontal mark: `brand/assets/logos/png/luxsync-horizontal.png`
- Compact/orb mark: `brand/assets/logos/png/luxsync-orb.png`

Matching SVG fidelity-container and WebP variants live beside the PNG families under `brand/assets/logos/`.

No generated, retyped, redrawn, recolored or substitute logo is allowed.

## Faithful approved metallic artwork

The full-resolution approval-board audit produced the current faithful branded illustration layer:

- Manifest: `brand/manifests/approved-board-asset-manifest.json`
- Masters: `brand/masters/approved-board-raster/`
- Digital exports: `brand/exports/digital/approved/`
- Visual inventory: `brand/audit/reference-board-visual-inventory.md`

Current set:

- 16 approved metallic icons
- 42 approved dividers/accents
- 58 reusable approved artworks total

For each asset, PNG and lossless WebP are available. SVG files are fidelity containers around the exact approved raster artwork and are not newly redrawn editable vectors.

### Approved metallic icon IDs

- `security-shield-check`
- `lighting-bulb`
- `climate-thermostat`
- `music-note`
- `shades-window`
- `smart-lock`
- `concierge-bell`
- `installation-tools`
- `support-headset`
- `automation-home-gear`
- `energy-bolt`
- `camera`
- `faq-chat`
- `phone`
- `calendar`
- `location-pin`

Use the faithful layer for branded editorial cards, solution imagery, Concierge moments, guide artwork, contact/support visual moments, promotional layouts and other places where the approved metallic LuxSync treatment is part of the brand expression.

### Approved divider/accent families

The 42 approved artworks include horizontal dividers, standalone sparkles, sparkle dividers, metallic lines/bars, badge underlines, orbit accents and corner/standalone ornaments. Use the IDs and exact file paths from `brand/manifests/approved-board-asset-manifest.json` rather than inventing or redrawing variants.

## Clean semantic vector primitives

The earlier clean vector library remains available under:

- `brand/assets/icons/`
- `brand/assets/dividers/`

These are semantically aligned, technically scalable primitives. Direct full-resolution audit established that they are visually simplified compared with the approved metallic board artwork.

Use them when a compact live UI context genuinely benefits from a simple scalable vector. Do not use them as a substitute for the faithful board-derived artwork when the approved metallic visual treatment is expected.

## Live UI

- General UI: HTML/CSS using `website/styles/design-system.md`
- VIP account interaction tokens: `website/styles/account-access-tokens.css`

Buttons, forms, toggles, navigation, product cards, search, tabs, pagination and other interactive controls must remain live HTML/CSS rather than flattened screenshots.

The approved buttons and UI-control boards define visual language and states, not permission to bake mutable labels, product facts, pricing, shipping/return claims, warranty claims or service claims into images.

## Route visual assignments

| Route | Blueprint | Production visual assignment |
|---|---|---|
| `/` | `website/pages/home.md` | Horizontal Combo logo + faithful metallic icons/dividers/accents + live editorial Plush Drift hero |
| `/find-my-luxsync-solution` | `website/pages/concierge.md` | Orb or Horizontal Combo logo + faithful Concierge/automation metallic artwork + live cards/progress UI |
| `/my-luxsync-blueprint` | `website/pages/my-luxsync-blueprint.md` | Horizontal Combo logo + faithful metallic capability artwork + live Blueprint hierarchy/cards |
| `/solutions` | `website/pages/solutions.md` | Horizontal Combo logo + faithful metallic capability artwork + live pathway cards |
| `/solutions/commercial-offices` | `website/pages/solutions/commercial-offices.md` | Horizontal Combo logo + approved automation, energy, climate, access/security and lighting artwork |
| `/solutions/senior-living` | `website/pages/solutions/senior-living.md` | Horizontal Combo logo + approved lighting, automation, support and awareness-oriented artwork |
| `/solutions/short-term-rentals` | `website/pages/solutions/short-term-rentals.md` | Horizontal Combo logo + approved lock, climate, energy, camera and automation artwork |
| `/solutions/residential` | `website/pages/solutions/residential.md` | Horizontal Combo logo + approved lighting, climate, entertainment/music and automation artwork |
| `/solutions/aging-in-place` | `website/pages/solutions/aging-in-place.md` | Horizontal Combo logo + approved lighting, support, automation and entry/access artwork |
| `/shop` and collection routes | `website/pages/shop.md` | Horizontal Combo logo + faithful category artwork where appropriate + validated commerce/manufacturer product imagery only |
| `/guides` | `website/pages/guides.md` | Horizontal Combo logo + approved energy, security, climate and automation artwork + live ROI card system |
| `/about` | `website/pages/about.md` | Horizontal Combo logo + approved ornaments/dividers + live founder profile layout; real approved portraits only if supplied |
| `/faqs` | `website/pages/faqs.md` | Orb logo + approved `faq-chat` artwork + live FAQ search/accordion composition |
| `/contact` | `website/pages/contact.md` | Orb logo + approved support, phone, calendar, location and Concierge artwork + live adaptive form |
| `/account/login` route family | `website/pages/account-login.md` | Horizontal Combo on desktop, Orb on compact/mobile, production-approved auth ambient graphics and semantic controls |

## VIP Account Access Asset Assignment

### Approved logo placement

- Desktop account welcome/header: `brand/assets/logos/png/luxsync-horizontal-combo.png`
- Extended horizontal use: `brand/assets/logos/png/luxsync-horizontal.png`
- Compact/mobile account access: `brand/assets/logos/png/luxsync-orb.png`

### Production-approved auth atmosphere

Authoritative SVG masters:

- `website/assets/auth/login-vip-hero.svg`
- `website/assets/auth/login-vip-hero-mobile.svg`
- `website/assets/auth/member-access-ambient.svg`
- `website/assets/auth/account-welcome-banner.svg`

Governed PNG/WebP derivatives live under `brand/exports/digital/account-access/`.

These remain text-free so authentication and status copy stays live and accessible.

### Auth design references

- `website/assets/auth/auth-card-reference.svg`
- `website/assets/auth/auth-input-states.svg`
- `website/assets/auth/auth-button-states.svg`

These are reference-only and should be implemented as live semantic HTML/CSS.

## Approved composition/reference boards

The following boards are durable approval evidence but are not direct flat production UI:

- `brand/reference-boards/buttons_board.png`
- `brand/reference-boards/product_cards_board.png`
- `brand/reference-boards/stationery_board.png`
- `brand/reference-boards/ui_controls_board.png`
- hero/banner compositions on `brand/reference-boards/approved_brand_board.png`
- section-separator examples on `brand/reference-boards/dividers_board.png`

Use their visual direction while keeping mutable text/data live and using validated business/commerce facts.

## Retired assets

The previous numbered grid-sliced production folders remain retired. They must not be restored or referenced by the website. The new board-derived library was rebuilt with explicit crop geometry, source hashes, stable semantic IDs and QA evidence instead of blindly restoring those old slices.

## Rule for future imagery

A new production image must be traceable to an approved source or an explicitly approved new design, contain no regenerated LuxSync logo or unvalidated mutable business claim, use the approved visual language, and be recorded in the appropriate manifest with QA evidence and technically justified formats.

**Official slogan:** Where Luxury Lives Intelligently

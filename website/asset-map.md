# LuxSync Website Asset Map

**Status:** Active / Authoritative
**Brand system:** LuxSync Production Raster v5
**Production asset library:** 6.0 clean atomic triple-format

## Production-safe visual primitives

### Exact logos

- Primary horizontal mark: `brand/assets/logos/png/luxsync-horizontal-combo.png`
- Alternate horizontal mark: `brand/assets/logos/png/luxsync-horizontal.png`
- Compact/orb mark: `brand/assets/logos/png/luxsync-orb.png`

Matching SVG fidelity-container and WebP variants live beside the PNG families under `brand/assets/logos/`.

### Clean semantic icons

Production SVG icons live under `brand/assets/icons/svg/`, with matching PNG and WebP variants.

Approved icon IDs:

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

Use SVG by default for website UI illustration. PNG and WebP are fallback/delivery formats, not alternative designs.

### Dividers and accents

Production SVG dividers and ornaments live under `brand/assets/dividers/svg/`, with matching PNG and WebP variants. These include steel, rose, dual, sparkle, diamond, orbit, badge underline and corner treatments.

### Live UI

- General UI: HTML/CSS using `website/styles/design-system.md`
- VIP account interaction tokens: `website/styles/account-access-tokens.css`

Buttons, forms, toggles, navigation, product cards and other interactive controls must remain live HTML/CSS rather than screenshots.

## Route visual assignments

| Route | Blueprint | Production visual assignment |
|---|---|---|
| `/` | `website/pages/home.md` | Horizontal Combo logo + clean icon/divider library + live editorial Plush Drift hero |
| `/find-my-luxsync-solution` | `website/pages/concierge.md` | Orb or Horizontal Combo logo + Concierge/automation icons + live cards/progress UI |
| `/my-luxsync-blueprint` | `website/pages/my-luxsync-blueprint.md` | Horizontal Combo logo + clean semantic capability icons + live Blueprint hierarchy/cards |
| `/solutions` | `website/pages/solutions.md` | Horizontal Combo logo + clean audience/capability icons + live pathway cards |
| `/solutions/commercial-offices` | `website/pages/solutions/commercial-offices.md` | Horizontal Combo logo + automation, energy, climate, access and lighting icons |
| `/solutions/senior-living` | `website/pages/solutions/senior-living.md` | Horizontal Combo logo + lighting, automation, support and awareness-oriented icons |
| `/solutions/short-term-rentals` | `website/pages/solutions/short-term-rentals.md` | Horizontal Combo logo + lock, climate, energy, camera and automation icons |
| `/solutions/residential` | `website/pages/solutions/residential.md` | Horizontal Combo logo + lighting, climate, entertainment and automation icons |
| `/solutions/aging-in-place` | `website/pages/solutions/aging-in-place.md` | Horizontal Combo logo + lighting, support, automation and entry icons |
| `/shop` and collection routes | `website/pages/shop.md` | Horizontal Combo logo + clean category icons + validated commerce/manufacturer product imagery only |
| `/guides` | `website/pages/guides.md` | Horizontal Combo logo + energy, security, climate and automation icons + live ROI card system |
| `/about` | `website/pages/about.md` | Horizontal Combo logo + live founder profile layout; real approved portraits only if supplied |
| `/faqs` | `website/pages/faqs.md` | Orb logo + `faq-chat` icon + live FAQ search/accordion composition |
| `/contact` | `website/pages/contact.md` | Orb logo + support, phone, calendar, location and Concierge icons + live adaptive form |
| `/account/login` route family | `website/pages/account-login.md` | Horizontal Combo on desktop, Orb on compact/mobile, production-approved auth ambient SVGs and semantic controls |

## VIP Account Access Asset Assignment

### Approved logo placement

- Desktop account welcome/header: `brand/assets/logos/png/luxsync-horizontal-combo.png`
- Extended horizontal use: `brand/assets/logos/png/luxsync-horizontal.png`
- Compact/mobile account access: `brand/assets/logos/png/luxsync-orb.png`

No generated, retyped, redrawn, recolored or substitute logo is allowed.

### Production-approved auth atmosphere

- `website/assets/auth/login-vip-hero.svg`
- `website/assets/auth/login-vip-hero-mobile.svg`
- `website/assets/auth/member-access-ambient.svg`
- `website/assets/auth/account-welcome-banner.svg`

These remain text-free so authentication and status copy stays live and accessible.

### Auth design references

- `website/assets/auth/auth-card-reference.svg`
- `website/assets/auth/auth-input-states.svg`
- `website/assets/auth/auth-button-states.svg`

These are reference-only and should be implemented as live semantic HTML/CSS.

## Retired assets

The previous numbered grid-sliced production folders were retired. They must not be restored or referenced by the website. Their crops were not atomic and could include neighboring icons, board fragments, labels or clipping.

## Rule for future imagery

A new production image must be cleanly isolated, contain no regenerated LuxSync logo or mutable business claim, use the approved visual language, and be entered in the production manifest with matching SVG/PNG/WebP where applicable and `qa_status: passed`.

**Official slogan:** Where Luxury Lives Intelligently

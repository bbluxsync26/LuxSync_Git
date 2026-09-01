# LuxSync Website Asset Map

**Status:** Active / Authoritative
**Brand system:** LuxSync Production Raster v5

## Production-safe visual primitives

- Primary horizontal mark: `brand/assets/logos/png/luxsync-horizontal-combo.png`
- Alternate horizontal mark: `brand/assets/logos/png/luxsync-horizontal.png`
- Compact/orb mark: `brand/assets/logos/png/luxsync-orb.png`
- Live UI: HTML/CSS using `website/styles/design-system.md`
- VIP account interaction tokens: `website/styles/account-access-tokens.css`

Do not publish direct raster assets from `brand/assets/02-icons/` through `brand/assets/09-stationery/`. Those files remain reference-only after visual QA. The dedicated auth vector mini-library lives under `website/assets/auth/` and has explicit publication status in `website/assets/auth/manifest.json`.

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
| `/account/login` route family | `website/pages/account-login.md` | Horizontal Combo on desktop, Orb on compact/mobile, production-approved auth ambient SVGs, live semantic HTML/CSS controls |

## VIP Account Access Asset Assignment

### Approved logo placement

- Desktop account welcome/header: `brand/assets/logos/png/luxsync-horizontal-combo.png`
- Extended horizontal use where space supports it: `brand/assets/logos/png/luxsync-horizontal.png`
- Compact/mobile account access: `brand/assets/logos/png/luxsync-orb.png`

No generated, retyped, redrawn, recolored, or substitute logo is allowed in the account experience.

### Production-approved auth atmosphere

- `website/assets/auth/login-vip-hero.svg` — desktop welcome-zone background
- `website/assets/auth/login-vip-hero-mobile.svg` — mobile background
- `website/assets/auth/member-access-ambient.svg` — reusable concealed orbit/underlight layer
- `website/assets/auth/account-welcome-banner.svg` — post-login welcome base

These assets remain text-free so all authentication, customer, and status copy stays live and accessible.

### Auth design references

- `website/assets/auth/auth-card-reference.svg`
- `website/assets/auth/auth-input-states.svg`
- `website/assets/auth/auth-button-states.svg`

These are reference-only. Do not publish them as functional UI. Implement their geometry, focus, hover, press, and reduced-motion behavior with semantic HTML/CSS using `website/styles/account-access-tokens.css`.

## Reference-only material

The imported composites under `brand/assets/07-heroes/` and `brand/assets/08-sections/`, plus the cropped icon/button/control/divider/product-card files, may inform spacing, lighting and mood only. They must not be placed on live pages because they contain or may contain baked/generated text, generated logo approximations, mutable claims, or crop artifacts.

## Rule for future clean imagery

A new image becomes production-safe only when it is text-free where practical, contains no regenerated LuxSync logo, contains no mutable commerce/support/authentication claims, uses approved visual language, and is explicitly added to the relevant manifest with `publication_status: production-approved`.

**Official slogan:** Where Luxury Lives Intelligently

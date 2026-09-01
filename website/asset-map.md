# LuxSync Website Asset Map

**Status:** Active / Authoritative
**Brand system:** LuxSync Production Raster v5

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

A new image becomes production-safe only when it is text-free where practical, contains no regenerated LuxSync logo, contains no mutable commerce/support claims, uses approved visual language, and is explicitly added to the manifest with `publication_status: production-approved`.

**Official slogan:** Where Luxury Lives Intelligently

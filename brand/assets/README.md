# LuxSync Raster Asset Library

**Status:** Active source library
**Brand system:** LuxSync Production Raster v5

This folder preserves the verified raster import, the exact approved logo copies, and explicitly approved clean account-access graphics. Publication status is intentionally explicit so generated composites and board slices cannot accidentally become live website artwork.

## Production-approved

### Exact approved logos

Only these logo files may be published directly:

- `01-logos/LuxSync_Logo_Horizontal_Combo.png`
- `01-logos/LuxSync_Logo_Horizontal_Final.png`
- `01-logos/LuxSync_Logo_Orb.png`

They are byte-identical copies of the immutable masters under `brand/source-logo/`.

Never redraw, retype, recolor, regenerate, simplify, or substitute these marks.

### VIP Account Access ambient graphics

The following clean, text-free SVGs under `10-auth/` are approved as decorative production atmosphere:

- `10-auth/login-vip-hero.svg`
- `10-auth/login-vip-hero-mobile.svg`
- `10-auth/member-access-ambient.svg`
- `10-auth/account-welcome-banner.svg`

They contain no mutable authentication copy or customer data. Render all login/account text and controls as live semantic HTML/CSS.

## Reference-only

Folders `02-icons/` through `09-stationery/` are **design-reference exports only**. Visual QA found that some files contain baked/generated copy, generated logo approximations, or board-crop artifacts. They are useful for style direction, but they must not be shipped as website UI, product data, founder information, support information, or public claims.

The following `10-auth/` assets are also reference-only and must not be used as functional UI:

- `10-auth/auth-card-reference.svg`
- `10-auth/auth-input-states.svg`
- `10-auth/auth-button-states.svg`

Use them only to reproduce the approved geometry and Plush Drift interaction behavior in live HTML/CSS.

Production implementation must use:

1. exact protected logo masters;
2. live HTML/CSS for headings, buttons, forms, icons, cards, dividers, navigation, Concierge, Contact, and account interactions;
3. validated commerce/manufacturer imagery for real products when available;
4. approved text-free photography or vector atmosphere only when explicitly marked production-approved;
5. `brand/assets/10-auth/manifest.json` to determine auth-asset publication status.

**Official slogan:** Where Luxury Lives Intelligently
**Metallic blue:** Brushed Dusty Steel `#7B96B2`
**Premium metallic anchor:** Champagne Rose Gold `#D6B0A0`

See `website/asset-map.md` for the route-by-route publication map and `website/pages/account-login.md` for the VIP account-access specification.

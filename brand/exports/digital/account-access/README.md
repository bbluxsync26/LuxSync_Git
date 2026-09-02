# LuxSync Account Access — Digital Derivative Exports

**Status:** Active / Wave 1 deterministic derivatives  
**Source authority:** `website/assets/auth/manifest.json`

These files are digital PNG/WebP derivatives of the four text-free account-access SVG assets currently marked `production-approved` in the authoritative auth manifest.

Source SVGs:

- `website/assets/auth/login-vip-hero.svg`
- `website/assets/auth/login-vip-hero-mobile.svg`
- `website/assets/auth/member-access-ambient.svg`
- `website/assets/auth/account-welcome-banner.svg`

Derivative paths:

- `brand/exports/digital/account-access/png/`
- `brand/exports/digital/account-access/webp/`

## Rules

- The SVG sources remain the authoritative masters for these four graphics.
- Derivatives contain no logo artwork and no mutable customer/authentication copy.
- PNG dimensions match the SVG intrinsic width/height.
- WebP derivatives are lossless and preserve alpha where the source renders transparency.
- Do not regenerate solely to refresh timestamps. Verify source hash, derivative hash, dimensions and QA state first.
- Publication status remains inherited from `website/assets/auth/manifest.json`; the three auth design-reference SVGs are not included here because they remain reference-only.

QA evidence for this derivative batch is recorded under `brand/audit/qa/` and in the omnichannel manifest.

# LuxSync Website Lifestyle & Hero Image Library

**Status:** Visual QA passed  
**Library ID:** LS-WEB-HERO-001  
**Brand system:** LuxSync Production Raster v5 / Plush Drift  
**Creative source:** Adobe Firefly  
**Governed manifest:** `brand/manifests/website-lifestyle-hero-image-library.json`

## Purpose

This library fills the website content-imagery gap that remained after PR-BRAND-001 completed the governed brand-graphics system. These images are editorial/lifestyle photography for website heroes and experience sections. They do not replace protected LuxSync logos, faithful approved-board metallic artwork, semantic icons, live UI, or manufacturer product imagery.

The library is intentionally text-free and logo-free so page headings, CTAs, pricing, commerce facts, ROI statements, accessibility content, and account state remain live HTML/CSS.

## Adobe source board

**LuxSync Website Lifestyle & Hero Image Library**  
Board ID: `urn:aaid:sc:US:4b3c7692-8f27-44d2-9606-2d9d9f8734b6`  
Board URL: `https://firefly.adobe.com/boards/id/urn:aaid:sc:US:4b3c7692-8f27-44d2-9606-2d9d9f8734b6`

The Adobe board is the current visual review surface for the 12 approved source images. The stable GenAI asset URNs are recorded in the manifest.

## Approved hero set

| Asset | Primary route/use | Copy-safe side | QA |
|---|---|---:|---|
| Homepage Hero | `/` | Left | Passed |
| Residential Hero | `/solutions/residential` | Right | Passed |
| Commercial Offices Hero | `/solutions/commercial-offices` | Left | Passed |
| Short-Term Rentals Hero | `/solutions/short-term-rentals` | Left | Passed |
| Senior Living Hero | `/solutions/senior-living` | Left | Passed |
| Aging in Place Hero | `/solutions/aging-in-place` | Right | Passed |
| Concierge Hero | `/find-my-luxsync-solution`, `/my-luxsync-blueprint` | Left | Passed |
| Energy & ROI Hero | `/guides` | Right | Passed |

## Approved lifestyle set

| Asset | Experience/use | QA |
|---|---|---|
| Intelligent Evening Lifestyle | Intelligent Evening | Passed |
| Cinema Lifestyle | Cinema | Passed |
| Welcome Home Lifestyle | Welcome Home | Passed |
| Water Watch Lifestyle | Water Watch | Passed |

## Visual rules

All approved images follow these constraints:

- editorial photorealism rather than stock-photo posing;
- Plush Drift palette: Slate Navy/Dark Suede shadows, taupe/driftwood neutrals, Dusty Steel cool light, restrained Champagne reflections;
- no purple, lavender, neon, cyberpunk, or arcade lighting;
- no generated LuxSync logo or substitute logo;
- no baked headings, captions, CTA copy, pricing, reviews, ROI claims, product facts, or readable UI screens;
- no fake product/manufacturer branding;
- smart-home intelligence is implied through architecture, lighting, shades, access, climate, and lived outcomes rather than gadget clutter;
- senior-living and aging-in-place imagery is dignified, independent, residential, and non-clinical.

## QA history

Three first-pass images were rejected during direct visual inspection:

1. Residential first draft: excessive orange/amber drift.
2. Short-Term Rentals first draft: generated a fake text/graphic panel.
3. Senior Living first draft: generated a fake text/graphic panel.

All three were regenerated and the replacements passed review. The final governed set contains 12 images.

## Storage and delivery status

The approved full-resolution source images currently persist as Adobe Firefly/GenAI assets and on the Firefly board above. Their stable Adobe asset URNs are the current provenance identifiers.

Binary image ingestion into GitHub delivery folders is a separate transfer step. Until that transfer is complete, the repo must not invent local PNG/WebP paths or claim that the binaries are already present. Once ingested, the recommended structure is:

- `brand/masters/lifestyle-hero/` for full-resolution approved PNG masters;
- `brand/exports/digital/lifestyle-hero/png/` for delivery PNG;
- `brand/exports/digital/lifestyle-hero/webp/` for lossless or visually lossless web delivery;
- a generated contact sheet and hash-bound QA record under `brand/audit/qa/`.

## Website implementation guidance

Use hero photography as a background or media layer while keeping all public copy live. Preserve the recorded copy-safe side when choosing object position and responsive crops. On smaller breakpoints, use subject-aware cropping or dedicated mobile crops rather than stretching the desktop image.

Do not place product prices, guarantees, testimonials, ratings, stock status, shipping claims, medical claims, or unvalidated savings statements into these images.

**Official slogan remains:** Where Luxury Lives Intelligently

# RB-007 — Brand Asset Raster Regeneration

**Status:** Superseded for current generation; retained for historical traceability  
**Date:** 2026-08-29  
**Superseded by:** `docs/runbooks/RB-008-Luxury-Orbit-Brand-Asset-Generation.md`

## Purpose

Record the original source-controlled process used to normalize LuxSync SVG typography and regenerate PNG/WebP derivatives.

This runbook established an important rule that remains active under RB-008:

- **Headings / display:** Manrope
- **Body / UI:** Inter

Changing text or font declarations in an SVG master does not automatically update baked raster derivatives. Raster outputs must be regenerated from the approved source and validated.

## Historical Baseline

On 2026-08-29, the first full typography regeneration:

- normalized 96 SVG masters,
- regenerated 51 text-bearing asset sets,
- rewrote 102 PNG/WebP raster derivatives,
- and was merged through PR #3 in commit `441116c791f992028699c5804cb2971b36cb3465`.

## Rules Carried Forward to RB-008

The current pipeline must continue to enforce:

1. Manrope 500/600 for generated display/heading/UI text.
2. Inter 400/500 for generated body/supporting UI text.
3. No reintroduction of Century Gothic or Candara as active system fonts.
4. Source-first edits followed by raster regeneration.
5. Dimension and visual validation after regeneration.
6. Native HTML/CSS text where possible for accessibility and responsiveness.
7. No manual raster-only text repair when a source asset exists.

## Current Procedure

Do not use this runbook as the current generation procedure.

Use:

`docs/runbooks/RB-008-Luxury-Orbit-Brand-Asset-Generation.md`

RB-008 governs the current generator, normalization layer, exact-logo protection, PNG/WebP rendering, scene-library boundary, and CI validation.

## Historical Failure Handling

If a generated asset is found to be incorrect, correct the source or generation process and rerun the current RB-008 pipeline. Do not repair only PNG/WebP derivatives while leaving the governing source incorrect.

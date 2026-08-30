# RB-008 — Luxury Orbit Brand Asset Generation

**Status:** Active  
**Repository:** `bbluxsync26/LuxSync_Git`  
**Base brand system:** Plush Drift v2.1  
**Web visual treatment:** Luxury Orbit

## Purpose

Generate and maintain the current LuxSync vector/UI graphics library while preserving authoritative brand rules and protected approved logo artwork.

RB-008 is the current generation runbook. It incorporates the typography/raster integrity controls originally documented in RB-007.

## Authoritative Rules

### Typography

- Headings / display / graphic UI: **Manrope 500/600**
- Body / supporting UI: **Inter 400/500**

Generated editable SVG text must not use Century Gothic, Candara, Montserrat, Bodoni-family, Didot, or Georgia as system fonts.

### Base palette

- Slate Navy `#0D1526`
- Dark Suede `#172036`
- Pale Driftwood `#D0BEB0`
- Warm Taupe Mauve `#9E8B85`
- Antique Rose Taupe `#967878`
- Dusty Steel `#7B96B2`

Derived rose-metal and icy orbit highlights are allowed as effects. They do not replace the six base colors.

### Protected approved logos

The exact approved primary logo rasters are protected and must not be regenerated from the generic SVG generator:

- `brand/assets/01-brand/luxsync-monogram-orb.png`
- `brand/assets/01-brand/luxsync-horizontal-lockup.png`

Their SVG wrappers intentionally reference the approved raster artwork. A new explicit logo decision is required to replace them.

## Source Files

- `scripts/generate-luxury-orbit-assets.py` — generates the 97 SVG-based graphics.
- `scripts/normalize-luxury-orbit-fonts.py` — enforces Manrope/Inter, Plush Drift base colors, safe category copy, and generation rules.
- `scripts/render-luxury-orbit-assets.py` — renders normalized SVGs to PNG/WebP and rebuilds contact sheets while preserving protected exact logo rasters.
- `scripts/regenerate-brand-raster-assets.py` — compatibility/orchestration entrypoint where retained.
- `.github/workflows/regenerate-brand-raster-assets.yml` — CI automation.

## Asset Library

Current logical library:

- 97 SVG-based graphics with PNG/WebP derivatives
- 6 text-free production scene raster pairs in `brand/assets/12-scenes/`
- Total logical assets: 103

Production scenes are curated raster assets and are not recreated by the SVG generator.

## Standard CI Flow

The workflow performs this sequence:

1. Check out the working branch.
2. Install Inkscape, ImageMagick, fontconfig, and Python image tooling.
3. Install **Manrope** and **Inter** on the runner.
4. Run `scripts/generate-luxury-orbit-assets.py`.
5. Run `scripts/normalize-luxury-orbit-fonts.py`.
6. Restore/protect exact approved primary logo wrappers.
7. Run `scripts/render-luxury-orbit-assets.py`.
8. Validate asset counts, required manifests/catalogs, protected logo wrappers, and forbidden legacy font declarations.
9. Run `git diff --check`.
10. Commit generated vector/catalog changes when required.

## Manual Regeneration

A local environment must provide Python 3, Inkscape, ImageMagick, Manrope, and Inter.

Run the same logical sequence as CI. Do not skip normalization before rendering.

## SVG and Image-Generation Boundary

Do **not** send the generated SVG library through an image generator. SVG source remains editable/searchable in Git.

Use image generation only for deliberately photographic or photorealistic scenes. Production scenes must remain text-free and must not contain baked-in navigation, prices, ratings, buttons, promotional copy, or unapproved logo recreations.

Render website copy and controls natively in HTML/CSS or use approved vector/raster brand assets.

## Validation

Before release:

1. Confirm exactly 97 generated SVG masters.
2. Confirm 97 non-scene PNG derivatives and 97 non-scene WebP derivatives.
3. Confirm 6 production-scene PNGs and 6 production-scene WebPs.
4. Confirm `brand/assets/12-scenes/scene-manifest.csv` exists.
5. Confirm `brand/assets/00-catalog/SVG-ASSET-LIST.md` exists.
6. Confirm `brand/assets/00-catalog/LuxSync-master-contact-sheet.png` exists.
7. Verify the official slogan: `Where Luxury Lives Intelligently`.
8. Verify Manrope/Inter in editable generated text.
9. Verify no forbidden legacy system-font declarations remain in generated SVGs or the editable generator source.
10. Verify Plush Drift v2.1 base colors remain authoritative.
11. Verify protected exact logo wrappers still reference the approved logo rasters.
12. Review representative assets visually on light and dark backgrounds.
13. Run repository consistency validation before release.

## Relationship to RB-007

RB-007 records the original typography-wide raster-regeneration process and remains useful historical traceability. For the current Luxury Orbit generation pipeline, **RB-008 governs** and carries forward the Manrope/Inter safeguards.

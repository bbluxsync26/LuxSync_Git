# RB-008 — Luxury Orbit Brand Asset Generation

**Status:** Active  
**Repository:** `bbluxsync26/LuxSync_Git`

## Purpose

Generate and maintain the current LuxSync Luxury Orbit web-graphics library without manually recreating 97 files.

## Source Files

- `scripts/generate-luxury-orbit-assets.py` — generates the 97 SVG masters.
- `scripts/regenerate-brand-raster-assets.py` — renders PNG/WebP siblings and rebuilds contact sheets.
- `.github/workflows/regenerate-brand-raster-assets.yml` — CI automation.

## Regeneration

From repository root:

```bash
python scripts/regenerate-brand-raster-assets.py
```

Expected output:

- 97 SVG masters
- 97 WebP siblings
- 97 PNG siblings
- catalog/contact-sheet PNGs
- `brand/assets/00-catalog/SVG-ASSET-LIST.md`

## CI Behavior

The workflow runs when the generator, raster script, or workflow itself changes on `master` or the `brand/luxury-orbit-refresh` branch. Generated `brand/assets` changes are committed by `github-actions[bot]`.

## SVG Rule

Do **not** send the SVG library through an image generator. SVG source is generated directly and remains editable/searchable in Git.

Use image generation only for photographic or photorealistic raster scenes. Keep copy, buttons, and precise brand text outside generated photos whenever possible.

## Validation

Before release:

1. Confirm exactly 97 SVG files.
2. Confirm exactly 97 WebP files.
3. Confirm at least 108 PNG files including contact sheets.
4. Review `00-catalog/LuxSync-master-contact-sheet.png`.
5. Verify the official slogan: `Where Luxury Lives Intelligently`.
6. Verify Deep Navy / Rose Gold / Powder Blue treatments visually.
7. Verify transparent assets on both light and dark test backgrounds.

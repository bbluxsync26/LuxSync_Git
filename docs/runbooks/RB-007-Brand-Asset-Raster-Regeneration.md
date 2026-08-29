# RB-007 — Brand Asset Raster Regeneration

**Status:** Active  
**Date:** 2026-08-29  
**Scope:** LuxSync SVG typography normalization and PNG/WebP regeneration

## Purpose

Provide the repeatable, source-controlled process for keeping LuxSync text-bearing raster assets synchronized with the authoritative brand typography.

This runbook exists because changing text or font declarations in an SVG master does **not** update text already baked into PNG or WebP derivatives.

## Governing Typography

LuxSync typography is authoritative as follows:

- Headings / display: **Manrope**
- Body / UI: **Inter**

Legacy generated-asset font names are superseded:

- `Century Gothic` → `Manrope`
- `Candara` → `Inter`

Do not reintroduce Century Gothic or Candara into text-bearing LuxSync brand assets.

## Governing Files

- SVG masters: `brand/assets/`
- Canonical asset inventory: `brand/assets/asset-manifest.csv`
- Asset summary: `brand/assets/asset-manifest.json`
- Regeneration script: `scripts/regenerate-brand-raster-assets.py`
- GitHub Actions workflow: `.github/workflows/regenerate-brand-raster-assets.yml`

## Operating Principle

**Edit the SVG master, then regenerate raster derivatives.**

Do not manually repaint, type over, or independently modify text inside PNG/WebP versions when an SVG master exists. That creates divergent assets and breaks the source-of-truth model.

## When to Run

Run raster regeneration when any of the following changes:

- Text in an SVG with PNG/WebP siblings
- Font family
- Font weight or text styling that changes raster appearance
- Slogan/tagline text
- Product/category labels embedded in graphics
- Brand card or banner copy
- A brand-wide typography correction

Raster regeneration is not necessary for a purely vector-only asset that has no PNG/WebP sibling.

## Automated Process

The regeneration script performs these actions:

1. Walks SVG masters under `brand/assets/`.
2. Normalizes legacy font declarations to Manrope/Inter.
3. Detects SVGs containing actual `<text>` elements.
4. Finds existing PNG and/or WebP siblings.
5. Reads the current raster dimensions.
6. Renders the SVG using Inkscape with the authoritative fonts installed.
7. Replaces the PNG at the same dimensions.
8. Rebuilds the WebP at the same dimensions.
9. Verifies regenerated raster dimensions match the prior dimensions.
10. Fails if a text-bearing SVG still contains a legacy Century Gothic or Candara declaration.

The script supports ImageMagick 6 and ImageMagick 7 environments.

## GitHub Actions Procedure

Use the workflow named:

`Regenerate LuxSync brand raster assets`

The workflow:

1. Checks out the working branch.
2. Installs Inkscape, ImageMagick, fontconfig, and curl.
3. Installs Manrope and Inter for the build runner.
4. Confirms the fonts resolve with fontconfig.
5. Executes `scripts/regenerate-brand-raster-assets.py`.
6. Runs `git diff --check`.
7. Scans text-bearing SVGs for forbidden legacy font declarations.
8. Commits regenerated `brand/assets` changes when changes exist.

Do not commit font binary files to the LuxSync repository. Fonts are installed transiently on the build runner for rendering only.

## Manual Local Procedure

If regeneration must be run locally, the environment must provide:

- Python 3
- Inkscape
- ImageMagick 6 or 7
- Manrope installed and discoverable by the renderer
- Inter installed and discoverable by the renderer

From the repository root, run:

```bash
python3 scripts/regenerate-brand-raster-assets.py
```

Then review the resulting SVG/PNG/WebP changes before commit.

## Required Validation

A regeneration pass is acceptable only when all of the following are true:

- The workflow/script completes successfully.
- Manrope and Inter are detected by the render environment.
- No text-bearing SVG contains `Century Gothic` or `Candara`.
- PNG/WebP dimensions remain unchanged unless a separate approved design change intentionally changes dimensions.
- Every text-bearing SVG with existing raster siblings has regenerated PNG/WebP derivatives.
- `git diff --check` passes.
- Visual spot checks confirm typography, text wrapping, cropping, transparency, and alignment remain acceptable.

## Visual Spot-Check Priority

Always inspect at least these customer-facing classes after a typography-wide regeneration:

- Brand lockups and wordmarks
- Hero graphics
- Storefront banners
- Product/category cards
- Buttons and badges with embedded text
- Trust/notification components
- Type specimens and brand-reference cards

## Website Use

For the website:

- Prefer SVG for logos and interface graphics when supported.
- Prefer WebP for larger raster graphics where raster use is appropriate.
- Use current files from `master`.
- Do not use a stale raster copied outside the repository when a current repository asset exists.
- Where text can be rendered semantically as HTML/CSS rather than embedded in an image, HTML/CSS remains preferable for accessibility and responsiveness.

## Current Baseline

On 2026-08-29, the first full typography regeneration:

- normalized **96 SVG masters**,
- regenerated **51 text-bearing asset sets**, and
- rewrote **102 PNG/WebP raster derivatives**.

That baseline was merged through PR #3 in commit:

`441116c791f992028699c5804cb2971b36cb3465`

## Failure Handling

If regeneration fails:

1. Do not merge partial generated output.
2. Read the failed workflow step and renderer error.
3. Correct the script, workflow, SVG source, or render environment on a branch.
4. Rerun the complete process.
5. Merge only after validation succeeds.

## Rollback

If regenerated assets are found to be visually incorrect after merge:

1. Revert the asset-regeneration commit or affected asset commit on a branch.
2. Correct the SVG master or rendering process.
3. Rerun the full regeneration and validation process.
4. Submit the corrected assets through normal review before merging.

Do not repair only the PNG/WebP while leaving the SVG master incorrect.

## Completion Criteria

A raster-regeneration cycle is complete when:

- SVG masters represent the approved typography and text.
- Existing PNG/WebP siblings have been regenerated where required.
- Automated validation passes.
- Customer-facing assets have been visually spot-checked.
- Changes are merged into `master`.

# LuxSync Omnichannel Brand Exceptions

**Prompt:** PR-BRAND-001  
**Current phase:** Complete  
**Overall brand/image cleanup state:** Complete

## Closed execution exceptions

### EX-001 — Reference-board pixels unavailable to current execution tooling

**Status:** Closed during Wave 1  
**Type:** Former environment/tool-access limitation  
**Human brand decision required:** No

The seven authoritative files under `brand/reference-boards/` were made visually accessible through a private, short-retention GitHub Actions audit artifact. Full-resolution originals were inspected directly. The element-level board inventory is recorded in `brand/audit/reference-board-visual-inventory.md`.

If visual access is lost in a future session, do not infer or regenerate unseen board artwork. Re-run the authenticated audit path or another approved method that exposes the exact approved pixels.

## Active technical-production constraints

These are intentional production constraints, not incomplete repository image cleanup.

### EX-002 — Print/specialty exports require asset-specific suitability review

**Status:** Intentionally deferred to real production jobs  
**Type:** Technical production dependency  
**Human brand decision required:** No  
**Blocks:** Blanket creation of meaningless PDF/EPS/TIFF/AI/specialty variants

True vectors, protected raster logos, board-derived raster artwork, photographs, stationery layouts, embroidery art, signage art, and print compositions have different technically appropriate master/export chains.

**Required behavior:**

- create a format only when the use case technically justifies it;
- obtain vendor/material/process constraints before specialty production adaptation;
- do not invent Pantone, thread, foil, ICC/profile, minimum-feature, trapping, cut-line, registration, or decoration-area requirements.

### EX-003 — Faithful approved-board artwork is raster-origin

**Status:** Accepted source-material constraint  
**Type:** Source-material provenance rule  
**Human brand decision required:** No  
**Blocks:** Claiming the 58 faithful board-derived artworks are newly created editable vectors

The authoritative visual source for these icons/dividers is raster board artwork. The faithful layer therefore preserves exact board appearance as raster-origin PNG masters with PNG, lossless WebP, and embedded-raster SVG fidelity-container exports.

**Required behavior:**

- do not call these SVGs true editable vectors;
- do not generatively redraw the artwork merely to obtain vector paths;
- preserve approved board-derived masters unchanged;
- create one-color, embroidery, engraving, foil, vinyl, screen-print, or other specialty adaptations only when technically justified for a real job and visually validated.

## Deferred job-specific manufacturing adaptations

The following are intentionally outside generic repository cleanup and must be created only after a selected vendor provides actual constraints:

- vendor-specific one-color logo conversion;
- embroidery stitch adaptation;
- screen-print separation/adaptation;
- vinyl cut-line adaptation;
- engraving/etching adaptation;
- foil/spot-metallic production plate;
- vendor ICC/profile-specific prepress conversion.

These are **not open brand-system gaps**.

## Brand approval conflicts

None detected.

## Protected-master exceptions

None detected. All three protected logo masters remain authoritative and unchanged.

## Current repository exception status

There are no open repository-wide image-cleanup blockers and no human brand decision is required to close PR-BRAND-001.

The current closeout evidence is recorded in:

- `brand/audit/brand-build-state.json`
- `brand/audit/brand-build-report.md`
- `brand/audit/image-cleanup-final-validation.md`

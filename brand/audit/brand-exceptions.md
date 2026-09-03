# LuxSync Omnichannel Brand Exceptions

**Prompt:** PR-BRAND-001  
**Current phase:** Wave 1

## Closed execution exceptions

### EX-001 — Reference-board pixels unavailable to current execution tooling

**Status:** Closed during Wave 1  
**Type:** Former environment/tool-access limitation  
**Human brand decision required:** No

The seven authoritative files under `brand/reference-boards/` were made visually accessible through a private, one-day GitHub Actions audit artifact. Full-resolution originals were inspected directly. The element-level board inventory is now recorded in `brand/audit/reference-board-visual-inventory.md`.

The prior rule remains important: if visual access is lost in a future session, do not infer or regenerate unseen board artwork. Re-run the private audit workflow or use another authenticated path that exposes the exact approved pixels.

## Open technical-production exceptions

### EX-002 — Print/specialty exports require asset-specific suitability review

**Type:** Technical production dependency  
**Human brand decision required:** No  
**Blocks:** Blanket creation of meaningless PDF/EPS/TIFF/AI variants

PR-BRAND-001 intentionally does not require every format for every asset. True vectors, protected raster logos, board-derived raster artwork, photographs, stationery layouts, embroidery art and print compositions have different technically appropriate master/export chains.

**Required behavior:** Determine format requirements asset by asset during Waves 1–3 and record intentionally omitted formats in the governing manifest.

### EX-003 — Board-derived Wave 1 artwork is raster-origin

**Type:** Source-material constraint  
**Human brand decision required:** No  
**Blocks:** Claiming the 58 faithful board-derived artworks are newly created editable vectors

The current authoritative visual source for these icons/dividers is raster board artwork. Wave 1 therefore preserves exact board appearance as raster-origin PNG masters with PNG, lossless WebP and embedded-raster SVG fidelity-container exports.

**Required behavior:**

- Do not call these SVGs true editable vectors.
- Do not generatively redraw the artwork merely to obtain vector paths.
- Preserve the approved board-derived master unchanged.
- Create true-vector, one-color, embroidery, engraving, foil or other specialty variants only when technically justified and visually validated in a later production wave.

## Brand approval conflicts

None detected.

## Protected-master exceptions

None detected. All three protected logo masters remain unchanged and continue to outrank every reference-board logo appearance.

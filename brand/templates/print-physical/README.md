# LuxSync Wave 3 Print & Physical Brand System

**Prompt:** PR-BRAND-001  
**Status:** Active / Wave 3  
**Brand system:** LuxSync Production Raster v5  
**Design DNA:** Plush Drift  
**Official slogan:** Where Luxury Lives Intelligently

## Purpose

This directory governs LuxSync print, stationery and physical-production source templates. The approved stationery reference board is composition evidence, not permission to reuse example names, addresses, phone numbers, email addresses, invoice data or other mutable information.

All generated static source art uses exact approved LuxSync logo delivery artwork. Mutable identity, contact, invoice and campaign content must be added in the final authoring application or approved vendor workflow.

## Print source set

`template-specs.json` governs these 300-DPI source compositions:

- business card front and back, 3.5 x 2 in trim with 0.125 in bleed;
- US letterhead, 8.5 x 11 in trim with 0.125 in bleed;
- #10 envelope, 9.5 x 4.125 in trim with 0.125 in bleed;
- note card, 5 x 3.5 in trim with 0.125 in bleed;
- invoice/header page, 8.5 x 11 in trim with 0.125 in bleed;
- document cover, 8.5 x 11 in trim with 0.125 in bleed;
- general one-page print-collateral frame, 8.5 x 11 in trim with 0.125 in bleed.

Each static composition is generated as:

- high-resolution PNG master;
- matching PNG delivery;
- 300-DPI CMYK TIFF companion;
- exact-page-size PDF composition source.

The PDFs are vendor-neutral source PDFs. They intentionally do not claim a vendor ICC profile, Pantone match, foil stock, substrate, coating, trapping or imposition standard that has not been supplied by the selected printer.

## Physical-production placement kit

`physical-production-specs.json` governs non-destructive logo-placement and production guidance for:

- signage;
- apparel left chest;
- apparel centered front/back;
- hat/front embroidery placement;
- mugs and drinkware;
- decals and vinyl;
- engraving and etching;
- screen print;
- foil / metallic finishing.

These are placement and handoff specifications, not vendor-ready manufacturing files. A vendor's actual material, stitch, ink, foil, cut-line and minimum-detail constraints must be validated before specialty artwork is created.

## Non-negotiable identity rule

Only approved protected LuxSync logo artwork may represent the LuxSync logo. Do not redraw, retype, trace, simplify, recolor, generatively recreate or substitute a monogram.

Full-color production compositions may place the exact approved raster logo artwork. Specialty one-color, embroidery, engraving, vinyl, screen-print or foil variants are not auto-invented by this Wave 3 kit. Create them only after the actual production process requires them and the resulting technical adaptation can be validated without changing the identity.

## Mutable data policy

Keep these live/template-driven:

- employee/founder names and titles;
- postal addresses;
- phone numbers;
- email addresses;
- websites if routing changes;
- invoice numbers, dates and totals;
- legal/tax/payment text;
- offer/campaign copy;
- product facts, prices and availability;
- printer marks that depend on a vendor's imposition requirements.

## Build and QA

- Build: `python scripts/build-wave3-print-physical.py`
- Validate: `python scripts/validate-wave3-print-physical.py`
- Static QA sheet: `brand/audit/qa/wave3-print-physical.jpg`
- Governed manifest: `brand/manifests/wave3-print-physical-manifest.json`

The generated art is a source layer. Final jobs should be preflighted against the selected printer or fabricator's specifications before manufacture.

<!-- LUXSYNC-BRAND-HEADER:START -->
<p align="center"><img src="../../brand/brand-system-v4/01-logos/luxsync-horizontal-approved.png" alt="LuxSync LLC — Where Luxury Lives Intelligently" width="620"></p>
<!-- LUXSYNC-BRAND-HEADER:END -->

# RB-010 — Crisp Brand System 4.0

## Purpose

This runbook governs all current LuxSync LLC brand, website, commerce, stationery, marketing, and documentation graphics.

## Source of truth

The approved board is `brand/brand-system-v4/00-reference/LuxSync_Brand_Board.png`. The only approved logo masters are:

- `brand/brand-system-v4/01-logos/luxsync-monogram-approved.png`
- `brand/brand-system-v4/01-logos/luxsync-horizontal-approved.png`

These files are immutable artwork. Do not redraw, retype, recolor, filter, crop, trace, or regenerate them.

## Generation

1. Edit `scripts/generate-crisp-brand-v4.py` only when a new deterministic SVG asset is required.
2. Run `python scripts/generate-crisp-brand-v4.py`.
3. Render each SVG to matching PNG and WebP outputs using Inkscape and ImageMagick.
4. Run `python scripts/apply-doc-branding.py` after adding or moving Markdown files.
5. Run `python scripts/validate-crisp-brand-v4.py`.
6. Render contact sheets and visually inspect every asset family before merge.

## Visual guardrails

- Use only Slate Navy `#0D1526`, Dark Suede `#172036`, Pale Driftwood `#D0BEB0`, Warm Taupe Mauve `#9E8B85`, Antique Rose Taupe `#967878`, Dusty Steel `#7B96B2`, and the approved Champagne Rose Gold metallic treatment.
- Use Manrope 500/600 and Inter 400/500 for editable text.
- Keep photographs crisp and dimensional.
- Limit sparkle/peak-shine accents to one or two intentional locations per composition.
- Do not create generic orbit backgrounds. The orbit belongs to the protected LS artwork.
- Reject lavender, purple, orange/copper drift, electric cyan, neon, cartoon styling, flat placeholder boards, and retyped logo lettering.

## Recovery

The pre-rebuild repository is preserved on `backup/pre-crisp-brand-rebuild-2026-08-31`.


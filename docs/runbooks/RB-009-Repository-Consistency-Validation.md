<!-- LUXSYNC-BRAND-HEADER:START -->
<p align="center"><img src="../../brand/brand-system-v4/01-logos/luxsync-horizontal-approved.png" alt="LuxSync LLC — Where Luxury Lives Intelligently" width="620"></p>
<!-- LUXSYNC-BRAND-HEADER:END -->

# RB-009 — Repository Consistency Validation

**Status:** Active
**Repository:** `bbluxsync26/LuxSync_Git`
**Purpose:** Prevent source-of-truth drift across LuxSync strategy, brand, website, prompts, runbooks, and asset metadata.

## Governing Contract

The automated validator enforces the current LuxSync baseline:

- Repository `master` is the source of truth.
- Plush Drift v2.1 is the authoritative base brand system.
- Crisp Dimensional is the active web/graphics treatment layered on that base.
- Manrope 500/600 is authoritative for headings/display/graphic UI.
- Inter 400/500 is authoritative for body/supporting UI.
- Official slogan: `Where Luxury Lives Intelligently`.
- Homepage hero: `Smart Living. Elevated.`.
- Primary CTA: `Shop Smart Home`.
- Secondary CTA: `Get the ROI Guide`.
- GoDaddy Commerce Plus remains the launch commerce system of record.
- Samsung SmartThings is the primary launch compatibility standard.
- Protected exact logo artwork must remain protected.
- Senior-service pricing remains unresolved until a dedicated pricing decision is committed.

## Automated Files

- `scripts/validate-crisp-brand-v4.py` — authoritative brand and documentation validation.
- `scripts/apply-doc-branding.py` — applies the approved LuxSync LLC header to Markdown.
- `.github/workflows/validate-crisp-brand-v4.yml` — runs validation for pull requests and pushes to `master` or brand branches.

## What the Validator Checks

### Brand and website contract

- Governing docs reference Manrope and Inter.
- Official slogan is consistent.
- Homepage hero and CTAs match the approved launch baseline.
- `brand/colors.md` contains the seven approved Plush Drift v2.1 colors, including Champagne Rose Gold Metallic rendered from approved palette colors, and does not retain the superseded replacement palette.

### Generated assets

- Generator source uses Manrope/Inter.
- Generator source does not reintroduce superseded Crisp Dimensional replacement base colors.
- Every v4 SVG master has matching PNG and WebP output.
- Editable SVG text declares Manrope and Inter.
- Protected exact logo copies match their sources by SHA-256.

### Asset integrity

- No retired `brand/assets-v3` directory remains.
- Every local SVG image reference resolves.
- Branded SVG masters use only approved palette values.
- Every Markdown document carries the approved LuxSync LLC header.

### Business guardrails

- Senior-service pricing is explicitly marked unresolved.
- The corrected Phase 2 founder-transition threshold is documented.
- The value proposition contains all five approved customer segments.
- `Smart Sleep Nursery` is the standardized nursery bundle name.

## Repository Validation

Run from repository root:

```bash
python scripts/validate-crisp-brand-v4.py
```

A non-zero exit means the repository should not be considered release-ready until the reported conflicts are resolved.

## Pull Request Gate

The consistency workflow runs on pull requests targeting `master` and on pushes to `master`.

Before merge:

1. Brand System 4.0 validation must pass.
2. `git diff --check` must pass.
3. Rendered contact sheets must be reviewed.
4. Any intentionally changed governing decision must update the corresponding docs, prompt/runbook/checklist, and master catalog in the same change set.

## When a Conflict Is Intentional

Do not weaken the validator just to make a new design or business change pass.

Instead:

1. Commit the new explicit decision or authoritative brand/business document.
2. Update dependent architecture, prompts, runbooks, checklists, and metadata.
3. Update the validator to represent the newly approved source-of-truth contract.
4. Run validation again.

## Completion Criteria

The repository consistency cycle is complete when:

- automated validation passes,
- no canonical metadata changes are left uncommitted,
- intentional decision changes are documented,
- and `docs/master-catalog.md` reflects the resulting durable artifacts.

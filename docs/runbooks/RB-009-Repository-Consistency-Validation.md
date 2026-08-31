# RB-009 — Repository Consistency Validation

**Status:** Active  
**Repository:** `bbluxsync26/LuxSync_Git`  
**Purpose:** Prevent source-of-truth drift across LuxSync strategy, brand, website, prompts, runbooks, and asset metadata.

## Governing Contract

The automated validator enforces the current LuxSync baseline:

- Repository `master` is the source of truth.
- Plush Drift v2.1 is the authoritative base brand system.
- Luxury Orbit is the active web/graphics treatment layered on that base.
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

- `scripts/validate-repository-consistency.py` — cross-repository validation.
- `scripts/reconcile-asset-metadata.py` — synchronizes asset CSV/JSON/inventory metadata with actual committed assets.
- `.github/workflows/validate-repository-consistency.yml` — runs validation for pull requests and pushes to `master`.

## What the Validator Checks

### Brand and website contract

- Governing docs reference Manrope and Inter.
- Official slogan is consistent.
- Homepage hero and CTAs match the approved launch baseline.
- `brand/colors.md` contains the seven approved Plush Drift v2.1 colors, including Champagne Rose Gold Metallic anchored at `#D6B0A0`, and does not retain the superseded replacement palette.

### Generated assets

- Generator source uses Manrope/Inter.
- Generator source does not reintroduce superseded Luxury Orbit replacement base colors.
- Exactly 98 SVG masters exist.
- Editable SVG text does not contain forbidden legacy system-font declarations.
- Protected exact logo wrappers still reference the approved logo rasters.

### Asset metadata

- `asset-manifest.json` reports Plush Drift v2.1 + Luxury Orbit + Manrope/Inter.
- Logical counts remain 104 total assets: 98 SVG-based graphics plus six production scenes.
- Every `asset-manifest.csv` width/height value matches the actual referenced SVG master.
- Six scene manifest rows, PNGs, and WebPs exist.

### Business guardrails

- Senior-service pricing is explicitly marked unresolved.
- The corrected Phase 2 founder-transition threshold is documented.
- The value proposition contains all five approved customer segments.
- `Smart Sleep Nursery` is the standardized nursery bundle name.

## Asset Metadata Reconciliation

Run from repository root:

```bash
python scripts/reconcile-asset-metadata.py
```

The script:

1. Loads the 98-row vector CSV manifest.
2. Confirms each referenced SVG exists.
3. Reads actual SVG width/height values.
4. Updates stale CSV dimensions.
5. Confirms expected category counts.
6. Confirms the six production scenes.
7. Rewrites the JSON library summary from the authoritative brand contract.
8. Rewrites the plain-text asset inventory.

The brand-generation workflow runs metadata reconciliation after SVG normalization/rendering so generated assets and canonical metadata stay synchronized.

## Repository Validation

Run from repository root:

```bash
python scripts/validate-repository-consistency.py
```

A non-zero exit means the repository should not be considered release-ready until the reported conflicts are resolved.

## Pull Request Gate

The consistency workflow runs on pull requests targeting `master` and on pushes to `master`.

Before merge:

1. Asset metadata reconciliation must produce no uncommitted changes.
2. Repository consistency validation must pass.
3. `git diff --check` must pass.
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

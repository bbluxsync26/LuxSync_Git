# RB-012 — Airo ↔ GitHub Development Loop

**Status:** Active
**Last updated:** 2026-09-03
**Scope:** Controlled LuxSync website iteration between GitHub and GoDaddy Airo

## Purpose

Provide the repeatable operating procedure for moving approved LuxSync website source from GitHub into GoDaddy Airo and returning Airo-generated changes to GitHub without creating a second uncontrolled source of truth.

The governing principle is simple:

> GitHub owns the product. Airo helps build the product. GoDaddy hosts and operates the approved production pieces.

## Related Artifacts

- `docs/architecture/airo-source-package-contract.md`
- `scripts/build-airo-source-package.py`
- `.github/workflows/build-airo-source-package.yml`
- `docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md`
- `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md`
- `docs/checklists/CL-001-Airo-First-Pass-Review.md`
- `docs/production-source-of-truth.md`
- `website/implementation-manifest.json`

## Branch Model

### Source of truth

`master`

Only validated, reviewed work is merged into `master`.

### Persistent website integration branch

`website/airo-development`

Use this branch as the controlled landing area for active Airo-backed website development cycles. It should regularly fast-forward/rebase from `master` before a new cycle begins.

### Per-cycle reconciliation branch

For each returned Airo export, create a short-lived branch from current `website/airo-development`, for example:

`website/airo-cycle-001`

or

`website/airo-homepage-refinement-20260903`

Do not apply raw Airo exports directly to `master`.

## Phase A — Prepare the GitHub Source

1. Confirm `master` is current.
2. Confirm repository validation is green.
3. Confirm PR-001 is current.
4. Confirm no unresolved business decision is being accidentally exposed as live website content.
5. Build the Airo source package.

Local command:

```bash
python scripts/build-airo-source-package.py
```

Validation-only command:

```bash
python scripts/build-airo-source-package.py --check
```

Default output:

`dist/airo/LuxSync-Airo-Source.zip`

Alternatively, run the GitHub Actions workflow **Build Airo source package** and download its artifact.

## Phase B — Start or Refresh the Airo Project

1. Open the intended non-production Airo project.
2. Upload `LuxSync-Airo-Source.zip` as project/source context.
3. Use PR-001 as the controlling instruction.
4. Tell Airo to evolve the supplied implementation rather than replacing the architecture wholesale.
5. Keep production DNS and live payments disconnected.
6. Do not manually re-create brand assets that are already supplied in the ZIP.
7. Use the Airo project only as a staging/design/code-generation environment.

## Phase C — Work in Airo

During the iteration:

- preserve `Where Luxury Lives Intelligently` as the sole public slogan/hero line;
- preserve Manrope + Inter;
- preserve the LuxSync Production Raster v5 / Plush Drift rules;
- use approved production logo deliveries only;
- preserve the Intelligent Living Concierge model and stable engine logic;
- preserve Contact branching and shared Property Profile concepts;
- preserve GoDaddy Commerce Plus as production commerce/account authority;
- do not invent live product facts or unsupported platform capability;
- do not turn mutable content into flattened image text;
- do not publish the production domain.

If Airo proposes a useful architecture change, treat it as a proposal. It does not override repository decisions until reviewed and intentionally committed.

## Phase D — Export from Airo

When the iteration is ready for repository review:

1. download/export the full Airo project ZIP;
2. do not edit the downloaded ZIP before preserving a reference copy;
3. record the Airo project name, preview URL, export date, and source-package commit SHA when known;
4. upload the untouched export for reconciliation.

The untouched export is evidence of what Airo generated. It is not automatically production source.

## Phase E — Reconcile the Airo Export

Create a fresh reconciliation branch from current `website/airo-development`.

Review the export in these buckets:

### Acceptable candidates

- layout improvements;
- responsive behavior improvements;
- accessible semantic markup;
- CSS/UI refinements consistent with Plush Drift;
- reusable components;
- performance improvements;
- content placement improvements that preserve canonical source meaning;
- visual implementation that consumes approved assets correctly.

### Requires deliberate review

- new dependencies;
- build-system changes;
- routing changes;
- API calls;
- analytics/tracking;
- storage/state changes;
- account/auth assumptions;
- cart/checkout behavior;
- generated product data;
- generated forms or server functions;
- generated environment variables.

### Reject by default

- secrets or credentials;
- fake products/prices/stock;
- invented reviews/testimonials;
- unapproved logo or font substitutions;
- alternate slogans;
- duplicated or replaced Concierge scoring logic;
- custom credential systems not explicitly approved;
- live payment configuration;
- production DNS configuration;
- unsupported supplier/partner claims;
- hidden tracking or external scripts without review;
- reference-board or QA artwork used as production UI.

## Phase F — Preserve Governed Source

Airo output must not silently replace repository-owned source contracts.

When conflicts occur:

1. preserve canonical content under `content/`;
2. preserve page contracts under `website/pages/`;
3. preserve stable Concierge source under `website/src/concierge/`;
4. preserve asset publication rules in `website/asset-map.md` and manifests;
5. preserve Commerce Plus boundaries;
6. adapt the generated implementation to those sources rather than the reverse.

If Airo produces a genuinely better architecture, create or update an explicit decision/architecture artifact before treating that architecture as authoritative.

## Phase G — Validate the Reconciled Branch

Required before PR:

```bash
python scripts/build-airo-source-package.py --check
python scripts/validate-production-brand.py
python scripts/validate-brand-derivatives.py
python scripts/validate-approved-board-assets.py
python scripts/validate-wave2-digital-marketing.py
python scripts/validate-wave3-print-physical.py
python scripts/validate-image-governance.py
python scripts/validate-repository-consistency.py
node website/src/concierge/assemble-engine.mjs
node site/build.mjs
node site/test.mjs
git diff --check
```

The standard GitHub validation workflow remains the final PR gate.

## Phase H — Pull Request and Merge

1. Open a PR from the per-cycle reconciliation branch to `master` or, for a larger multi-cycle website effort, first to `website/airo-development` followed by a release PR to `master`.
2. Include:
   - Airo source-package commit SHA;
   - Airo project/export identifier;
   - accepted changes;
   - rejected/generated changes;
   - screenshots/preview references when available;
   - commerce/auth impacts;
   - CL-001 result.
3. Require green CI.
4. Merge only after review.
5. Confirm the post-merge `master` validation succeeds.

## Phase I — Refresh the Persistent Development Branch

After accepted website changes reach `master`, move `website/airo-development` to the new validated `master` baseline before starting another major Airo cycle.

Do not allow the persistent branch to become an alternate long-lived product history.

## Airo Package Artifact Workflow

The repository workflow `.github/workflows/build-airo-source-package.yml` produces the source ZIP without committing it.

The artifact is transport material only. It should not be merged into source control.

## Failure Recovery

### Airo build goes sideways

Discard the Airo iteration and create a new project/cycle from a clean current source ZIP. No repository rollback is required because Airo is not authoritative.

### Airo export contains useful design but unusable code

Reimplement the approved visual behavior in the existing LuxSync codebase. Preserve the exported project only as design evidence.

### Reconciliation branch fails CI

Fix or remove the generated change. Do not weaken repository guardrails merely to accommodate generated output.

### Airo and repository disagree about business facts

The repository wins unless an explicit new decision is approved and committed.

### Native Git integration becomes available

Do not switch automatically. First validate:

- branch selection;
- push/pull direction;
- conflict behavior;
- secret handling;
- generated-file scope;
- PR compatibility;
- rollback;
- auditability.

If validated, update ARC-003 and this runbook so Git transport replaces ZIP transport without changing the source-of-truth model.

## Completion Criteria

Steps 1–4 of the LuxSync Airo/GitHub foundation are complete when:

- ARC-003 defines the source-package contract;
- the deterministic package builder validates and produces a ZIP;
- this reconciliation runbook is active;
- `website/airo-development` exists from a green `master` baseline.

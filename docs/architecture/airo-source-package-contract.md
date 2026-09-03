# ARC-003 — Airo Source Package Contract

**Status:** Active / Authoritative
**Last updated:** 2026-09-03
**Scope:** GitHub → GoDaddy Airo website-build handoff

## Purpose

Define the exact repository material that may be handed to GoDaddy Airo AI Builder for LuxSync website generation and revision.

The package is a curated projection of the repository, not a second source of truth. GitHub `master` remains authoritative. Airo consumes the package for design/code generation and returns an export for review; generated output does not become authoritative until reconciled through GitHub review, validation, and merge.

## Operating Model

```text
GitHub master
    ↓
validated Airo source package
    ↓
GoDaddy Airo staging project
    ↓
Airo project export
    ↓
GitHub reconciliation branch / PR
    ↓
LuxSync CI
    ↓
master
    ↓
validated staging / production candidate
```

This is intentionally one-way at each handoff. Until GoDaddy provides a validated native Git synchronization path, ZIP transport is the controlled integration boundary.

## Package Goals

The package must:

1. provide Airo enough current source to build the LuxSync website accurately;
2. expose the current production website implementation so Airo evolves an existing system rather than inventing a disconnected replacement;
3. include approved website-appropriate brand assets;
4. include governed content, page architecture, Concierge logic, and account-access specifications;
5. include PR-001 as the controlling build instruction;
6. preserve a reproducible source commit and per-file hashes;
7. exclude internal, historical, print/vendor, financial, and governance material that is unnecessary or risky for an AI website build.

## Canonical Package Name

Default output:

`dist/airo/LuxSync-Airo-Source.zip`

The ZIP contains two generated control files at its root:

- `AIRO-README.md`
- `AIRO-PACKAGE-MANIFEST.json`

The generated manifest records:

- package schema version;
- source repository;
- source commit SHA when available;
- package profile;
- generated timestamp;
- included file count;
- total uncompressed bytes;
- SHA-256 for every included repository file.

## Included Source Classes

### 1. Build instructions and production handoff

Include:

- `README.md`
- `docs/production-source-of-truth.md`
- `docs/master-catalog.md`
- `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md`
- `docs/checklists/CL-001-Airo-First-Pass-Review.md`
- `docs/checklists/CL-002-Account-Access-Review.md`

### 2. Website architecture and platform boundary

Include:

- `docs/architecture/website-information-architecture.md`
- `docs/architecture/intelligent-living-concierge.md`
- `docs/decisions/DEC-004-commerce-plus-and-airo-role.md`

Do not include unresolved pricing or financial planning decisions merely because they exist in the repository.

### 3. Brand rules required for website work

Include:

- `brand/README.md`
- `brand/brand-architecture.md`
- `brand/colors.md`
- `brand/typography.md`
- `brand/voice-and-tone.md`

Include website-appropriate approved digital assets:

- protected production logo deliveries under `brand/assets/logos/`;
- semantic icons under `brand/assets/icons/`;
- semantic dividers/ornaments under `brand/assets/dividers/`;
- faithful approved digital icon/divider exports under `brand/exports/digital/approved/`;
- account-access digital derivatives under `brand/exports/digital/account-access/`;
- governed digital-marketing compositions under `brand/exports/digital/marketing/` when present.

The package does not include protected logo source masters or approval-board originals. Airo receives production deliveries, not the archival identity source.

### 4. Website source and UX contracts

Include:

- `website/implementation-manifest.json`
- `website/navigation.md`
- `website/asset-map.md`
- `website/account-access-manifest.json`
- `website/pages/`
- `website/styles/`
- `website/src/`
- `website/assets/auth/`

### 5. Governed customer-facing content

Include:

- `content/`
- approved founder source profiles under `docs/leadership/`

### 6. Current production website implementation

Include:

- `site/`

This gives Airo the existing working implementation rather than only prose specifications.

## Explicit Exclusions

The packaging script must not include:

- `.git/` or Git metadata;
- `.github/` workflows and repository automation;
- `dist/` or generated output;
- `node_modules/` or dependency caches;
- secrets, environment files, tokens, keys, credentials, certificates, or local configuration;
- `docs/financial-model.md`;
- internal business-plan financial projections unless separately approved for the specific build;
- unresolved DEC-005 senior-service pricing material;
- `brand/reference-boards/`;
- `brand/source-logo/`;
- `brand/masters/`;
- `brand/audit/`;
- print/physical production exports and vendor-production specifications;
- TIFF/PDF/EPS/vendor manufacturing derivatives not needed for website generation;
- historical/superseded generators and migration artifacts;
- repository-only QA contact sheets unless explicitly required for a design-review cycle.

## Security and Privacy Rule

The package is intended for website generation. It must contain no secret or private operational credential.

The builder performs filename/path screening for common secret-bearing patterns. This is a guardrail, not a replacement for repository secret scanning.

If a future website feature requires a secret, the secret belongs in the supported deployment/platform secret store, never in this package.

## Airo Intake Rule

When starting an Airo project from this package:

1. upload the ZIP as source context;
2. use the current PR-001 as the controlling instruction;
3. tell Airo to treat `AIRO-README.md` and `AIRO-PACKAGE-MANIFEST.json` as provenance/control information;
4. require Airo to evolve supplied source instead of replacing governed Concierge, Contact, commerce, brand, or account architecture with invented equivalents;
5. keep the project staging-only until the exported result is reconciled and passes LuxSync CI.

## Export Return Rule

Airo output is never merged directly into `master`.

The untouched Airo export is first preserved as review input. Changes are then reconciled into a dedicated website branch. The reviewer must distinguish:

- useful visual/UX/code changes;
- generated dependencies;
- generated configuration;
- fabricated business facts;
- duplicated or replaced governed logic;
- production-impacting integration assumptions.

Only accepted changes proceed to PR and CI.

## Validation Requirements

`python scripts/build-airo-source-package.py --check`

must verify that:

- every required exact source exists;
- every include prefix resolves to at least one file;
- no forbidden path or secret-like filename enters the package;
- no generated package output is recursively included;
- the resulting package file list is deterministic for the same repository tree.

A manual or CI package build must create a ZIP and manifest from the same validated selection rules.

## Change Control

Changes to the package allowlist are architecture changes because they alter what source Airo can consume.

Any addition should answer:

1. Does Airo need this file to build/review the website?
2. Is it current and authoritative?
3. Is it safe to disclose to the Airo project context?
4. Could it cause Airo to confuse planning/reference material with live product behavior?

If the answer is unclear, do not include it by default.

# RB-009 — Repository Consistency Validation

**Status:** Active / Reconciled
**Last updated:** 2026-08-31

## Purpose

Prevent cross-repository drift after changes to LuxSync brand language, founder facts, website architecture, Contact routing, product/solution terminology, and the Intelligent Living Concierge.

The validator is:

`scripts/validate-repository-consistency.py`

Run it from the repository root:

```bash
python scripts/validate-repository-consistency.py
```

A non-zero exit code blocks the consistency gate.

## Current Contracts Enforced

### Brand language

- sole public slogan / hero line is **Where Luxury Lives Intelligently**
- retired alternate hero/slogan wording must not remain in text, scripts, or SVG source
- primary homepage CTA is **LuxSync Concierge**
- secondary homepage CTA is **Shop Smart Home**

### Founder identities

- Bridgette Beardsley — **Co-Founder & Chief Technology and Strategy Officer**
- Sheldon Bardol — **Co-Founder & Chief Customer and Operations Officer**

### Contact

Required routing:

- `support@luxsync.net` for existing product/order/setup/troubleshooting support
- `info@luxsync.net` for product information, consultations, general questions, and business/partnership inquiries

The Contact blueprint must preserve the adaptive Support / Product Information / Consultation / General Question / Business-Partnership branches and the shared Property Profile fields.

### Concierge

Required names:

- **LuxSync Concierge**
- **LuxSync Intelligent Living Concierge**
- **My LuxSync Blueprint**

The architecture must preserve the Lifestyle → Experience → Intelligence → Technology model and implementation paths:

- Essential Intelligence
- Elevated Living
- Complete LuxSync Experience

Concierge JSON modules under `website/src/concierge/modules/` must parse successfully.

### Product catalog

`content/product-catalog.md` must preserve the distinction between physical products, curated bundles, and LuxSync Experience / solution concepts.

Planning concepts must not silently become live commerce claims.

### Typography and palette

The active website design system must contain Manrope, Inter, and the approved LuxSync palette including Champagne Rose Gold Metallic anchor `#D6B0A0`.

## Required Source Files

The validator verifies existence of current core architecture, page blueprints, Contact content, Product & Solution Catalog, founder bios, reusable prompts, Airo prompt/runbook/checklist, design system, and Concierge source.

If a governing file is intentionally renamed, update the validator and Master Catalog in the same commit.

## When to Run

Run validation:

1. before an Airo staging generation;
2. after changing a slogan, founder fact, title, email route, product family, Experience name, Contact branch, or Concierge field contract;
3. after a broad prompt/document reconciliation;
4. before merging a website-generation/export branch;
5. before a release candidate is treated as production-ready.

## Retired Language Rule

Historical provenance may be preserved in Git history, but the current working tree should not contain retired public slogan/hero copy that could be consumed accidentally by generators.

If historical documentation must discuss a retired phrase, refer to it generically as `retired hero language` rather than reproducing the exact phrase.

## Failure Handling

When validation fails:

1. read every reported path;
2. determine which current artifact is authoritative using `docs/master-catalog.md`;
3. update dependent files together;
4. rerun validation;
5. do not weaken the validator merely to make a contradiction pass.

## GitHub Actions

The repository consistency workflow may invoke this validator automatically. A passing workflow means the encoded source-of-truth checks passed; it does not replace functional, accessibility, commerce, or visual QA.

## Completion Criteria

The consistency gate passes when:

- all required files exist;
- governing docs contain the official slogan;
- retired hero/slogan treatment is absent from the working tree;
- homepage CTAs match current architecture;
- founder titles are exact;
- Contact branches and email routing are intact;
- Concierge/Blueprint naming and implementation-path contracts are intact;
- Product & Solution Catalog has required distinctions;
- Concierge module JSON parses;
- design-system typography/palette contracts are intact.

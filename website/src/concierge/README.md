# LuxSync Intelligent Living Concierge Engine

This directory contains the implementation source for **LuxSync Concierge**, the LuxSync Intelligent Living Concierge and **My LuxSync Blueprint** recommendation engine.

## Structure

- `modules/` — maintainable source configuration split by questionnaire stage and decision-engine concern.
- `assemble-engine.mjs` — reconstructs the production `luxsync-concierge-engine.v1.json` configuration from the modules.
- `reference-evaluator.mjs` — reference deterministic scoring/evaluation implementation.
- `luxsync-concierge-engine-config.schema.json` — JSON Schema for engine configuration validation.
- `luxsync-concierge-engine-field-map.md` — stable field/API dictionary.
- `sample-private-residence-result.json` — residential scoring example.
- `sample-short-term-rental-result.json` — STR scoring example.

## Build

From this directory:

```bash
node assemble-engine.mjs
```

This generates `luxsync-concierge-engine.v1.json` from the tracked modules.

## Runtime Flow

1. Render stages from `questionnaire`.
2. Apply question visibility rules (`show_when`, `show_when_any`).
3. Normalize answers using stable field IDs.
4. Initialize all LuxSync Experience scores to zero.
5. Apply matching scoring rules and context bonuses.
6. Apply ranked-priority multipliers.
7. Determine compatibility status and foundation.
8. Rank Experiences using recommendation thresholds.
9. Select an implementation path and phased roadmap.
10. Evaluate consultation triggers.
11. Resolve the highest-priority matching CTA.
12. Render **My LuxSync Blueprint**.

## Design Contract

The Concierge recommends **experiences first**, then capability/device categories, then exact compatible products. Product compatibility, installation requirements, subscriptions, and internet dependencies must come from a separately maintained product catalog rather than lifestyle scoring alone.

Every customer-facing recommendation should explain **Why LuxSync Chose This**.

## Contact Routing

- Support: `support@luxsync.net`
- General / Consultation: `info@luxsync.net`

## Versioning

Treat `config_version` as immutable after release. Breaking field IDs, answer values, or Blueprint output fields requires a new major version. Saved Blueprints should retain the configuration version that generated them.

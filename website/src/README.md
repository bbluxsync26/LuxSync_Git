# Website Application Source

**Status:** Active source area / production framework not yet selected  
**Brand system:** LuxSync Production Raster v5  
**Design DNA:** Plush Drift

This directory contains reviewed LuxSync website application source that is appropriate to track before a final production framework is selected.

The **LuxSync Intelligent Living Concierge** under `website/src/concierge/` is active implementation source. A future reviewed GoDaddy Airo export or other approved site source may be added only after its framework, dependencies, build commands, APIs, analytics, generated secrets, and commerce integration are inspected.

This directory does **not** imply that a final production website framework has been selected.

## Objectives

- Fast performance
- Mobile-first design
- Accessibility
- Commerce-first customer journeys
- LuxSync Production Raster v5 visual system
- Plush Drift tactile interaction DNA
- Manrope + Inter typography
- SmartThings-focused launch messaging
- Maintainable source control
- Clean separation between staging/reference output and production integrations

## Brand Experience

Technology should feel invisible, intuitive, dependable, and at home in a premium living environment.

Use the current production hierarchy:

1. `docs/production-source-of-truth.md`
2. `brand/README.md`
3. `website/styles/design-system.md`
4. `website/implementation-manifest.json`
5. `website/asset-map.md`
6. page blueprints under `website/pages/`

## Current Implementation Source

`website/src/concierge/` governs the maintainable Concierge engine, including questionnaire stages, branching, stable field IDs, recommendation scoring, LuxSync Experience concepts, CTA logic, and the My LuxSync Blueprint schema.

Do not replace that engine with independently invented survey logic in a generated website.

## Source Intake Rule

When Airo or another approved builder exports source:

1. Preserve an untouched reference snapshot.
2. Inspect the framework, dependencies, scripts, APIs, analytics, and generated secrets.
3. Remove or externalize secrets before commit.
4. Confirm GoDaddy Commerce Plus remains the production commerce/account system of record unless a later approved decision changes it.
5. Review the generated experience using ARC-001, PR-001, CL-001, the Contact blueprint, and the account-access controls where applicable.
6. Validate responsive behavior, accessibility, content integrity, asset publication status, and commerce boundaries.
7. Only then establish additional production source structure beneath `website/` or `site/`.

## Production Website Handoff

- Route contract: `website/implementation-manifest.json`
- Navigation: `website/navigation.md`
- Visual publication rules: `website/asset-map.md`
- Design system: `website/styles/design-system.md`
- Airo build prompt: `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md`
- Concierge engine: `website/src/concierge/`

**Official slogan:** Where Luxury Lives Intelligently

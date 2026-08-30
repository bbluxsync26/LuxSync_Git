# Website Application Source

**Status:** Placeholder / source structure not yet selected

This directory is reserved for reviewed LuxSync website source after the first Airo staging generation is exported and its actual framework, dependencies, and build commands are inspected.

It does **not** currently imply that a production website application or framework has been selected.

## Objectives

- Fast performance
- Mobile-first design
- Accessibility
- Commerce-first customer journeys
- Plush Drift v2.1 base design system
- Luxury Orbit web treatment
- Manrope + Inter typography
- SmartThings-focused launch messaging
- Maintainable source control

## Brand Experience

Technology should feel invisible, intuitive, dependable, and at home in a premium living environment.

## Source Intake Rule

When Airo or another approved builder exports source:

1. Preserve an untouched reference snapshot.
2. Inspect the framework, dependencies, scripts, APIs, analytics, and generated secrets.
3. Remove or externalize secrets before commit.
4. Confirm Commerce Plus remains the production commerce system of record unless a later decision changes it.
5. Review the generated experience using ARC-001 and CL-001.
6. Only then establish the production source structure beneath `website/`.

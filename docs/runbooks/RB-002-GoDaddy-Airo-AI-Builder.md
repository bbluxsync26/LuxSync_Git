# RB-002 — GoDaddy Airo AI Builder

**Status:** Active  
**Date:** 2026-08-29  
**Scope:** LuxSync website generation and staging workflow

## Purpose

Provide the repeatable process for using GoDaddy Airo AI Builder without allowing the AI builder to override the LuxSync repository source of truth or prematurely replace the GoDaddy Commerce Plus commerce system.

## Governing References

Before beginning an Airo build, review:

1. `README.md`
2. `docs/architecture/website-information-architecture.md`
3. `docs/decisions/DEC-004-commerce-plus-and-airo-role.md`
4. `brand/README.md`
5. `brand/colors.md`
6. `brand/typography.md`
7. `brand/voice-and-tone.md`
8. `content/homepage.md`
9. `content/about.md`
10. `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md`
11. `docs/runbooks/RB-007-Brand-Asset-Raster-Regeneration.md`

## Current GoDaddy Product Distinction

Do not treat these names as interchangeable:

- **GoDaddy Commerce Plus / Websites + Marketing:** Current LuxSync launch commerce platform and system of record.
- **Airo AI Builder:** Standalone conversational builder capable of websites, applications, online-store prototypes, code-level editing, deployment, and code export.
- **Airo Plus:** AI-powered branding, optimization, marketing, and compliance-assistant features. It is not the LuxSync commerce architecture.

## Preconditions

Before starting a generation pass:

- Repository `master` is current.
- PR-001 is the approved prompt version to use.
- Official slogan is `Where Luxury Lives Intelligently`.
- Headline font is Manrope.
- Body/UI font is Inter.
- Plush Drift v2.1 colors are available.
- The build is treated as staging/prototype until the validation gate is complete.
- No live payment connection is enabled during the initial generation pass.

## Step 1 — Start the Airo AI Builder Project

1. Sign in to GoDaddy.
2. Open **Airo AI Builder**, not the legacy GoDaddy AI Website Builder.
3. Start a new website/store project.
4. Name the project clearly, for example:
   - `LuxSync Storefront Staging`
5. Paste the complete current PR-001 prompt from the repository.
6. Start the build.

## Step 2 — First-Pass Acceptance Review

Do not immediately edit cosmetic details.

First verify structural compliance:

- Home exists.
- Shop exists.
- Solutions exists.
- Guides exists.
- About exists.
- Support exists.
- Search/cart/account behavior is represented appropriately.
- Homepage uses `Technology That Feels Like Home` as hero messaging.
- Official slogan is present and exact.
- Primary CTA is `Shop Collections`.
- No unsupported audiences were invented.
- No future LuxSync Grid or template products are presented as live.
- No unsupported partnerships, awards, reviews, certifications, or customer counts were invented.
- No internal financial targets or supplier costs appear.

If the structure is wrong, correct the structure before visual polishing.

## Step 3 — Brand Calibration

Use Airo edits or manual editing to enforce:

### Colors

- Slate Navy `#0D1526`
- Dark Suede `#172036`
- Pale Driftwood `#D0BEB0`
- Warm Taupe Mauve `#9E8B85`
- Antique Rose Taupe `#967878`
- Dusty Steel `#7B96B2`

### Typography

- Manrope 500/600 for headings/display
- Inter 400/500 for body/UI

### Visual character

- Dark, calm surfaces
- Warm luxury neutrals
- Restrained rose/steel illumination
- Generous breathing space
- Refined rounded corners
- Minimal motion

Reject:

- Neon/cyberpunk styling
- Excessive gradients
- Gadget-store presentation
- Cartoon UI
- Aggressive popups
- Overly rounded bubble interfaces
- Busy dashboards on marketing pages

## Step 4 — Load Repository Assets

Prefer current assets from the repository.

Primary folders:

- `brand/assets/01-brand/`
- `brand/assets/02-icons-brand/`
- `brand/assets/03-icons-website/`
- `brand/assets/05-palette/`
- `brand/assets/06-gradients/`
- `brand/assets/07-components/`
- `brand/assets/08-cards/`
- `brand/assets/09-illustrations/`
- `brand/assets/10-product-cards/`
- `brand/assets/11-banners/`

Use SVG for logos/icons where supported and WebP for larger raster graphics.

Current text-bearing raster assets on `master` are generated from normalized SVG masters using Manrope/Inter. When text-bearing SVG content or typography changes, follow `RB-007 — Brand Asset Raster Regeneration` before using the updated PNG/WebP derivatives in Airo.

## Step 5 — Commerce Representation

During staging, represent commerce UX without assuming that Airo is the final commerce engine.

Required UX:

- Product catalog
- Collection/category browsing
- Product-detail presentation
- Search
- Cart
- Customer account concept where appropriate
- Checkout path representation

Do **not** connect live payments during the initial generation pass.

Do not create an unmanaged second source of product truth. Validated product data ultimately comes from the production commerce catalog.

## Step 6 — Responsive Review

Review at minimum:

- Desktop
- Tablet
- Mobile

Check:

- Navigation
- Hero crop
- CTA visibility
- Collection cards
- Product cards
- Forms
- Cart behavior
- Footer
- Font sizes
- Touch targets

Mobile must be intentionally composed, not a shrunken desktop layout.

## Step 7 — Accessibility Review

Validate:

- Semantic heading hierarchy
- Keyboard navigation
- Visible focus states
- Color contrast
- Meaningful alt text
- Accessible form labels
- Touch-target size
- Reduced-motion behavior
- No color-only status communication

Airo output is not presumed compliant merely because it was generated successfully.

## Step 8 — Content Review

Every claim must trace to repository-supported content.

Reject generated claims involving:

- Awards
- Certifications
- Testimonials
- Customer counts
- Guaranteed savings
- Unsupported compatibility
- Supplier relationships not documented in the repository
- Samsung/SmartThings endorsement
- Airbnb/VRBO endorsement
- Medical outcomes

## Step 9 — Export / Repository Review

If the Airo plan provides code export:

1. Export the generated code.
2. Preserve the untouched export as a reference snapshot before major refactoring.
3. Place reviewed website source beneath `website/` using a structure approved in a separate architecture decision.
4. Review dependencies, generated secrets, APIs, analytics code, and build tooling before commit.
5. Never commit API keys, payment credentials, passwords, or private tokens.

Do not invent a framework choice before inspecting the generated source.

## Step 10 — Commerce Validation Gate

Before any Airo-generated storefront could replace or bypass Commerce Plus, validate:

1. Product catalog behavior
2. Shipping
3. Sales tax
4. Payment processing
5. Order management
6. Refund/cancellation flow
7. Customer accounts
8. Fulfillment/supplier workflow
9. Recurring billing where required
10. Analytics
11. Accessibility
12. SEO
13. Source-control/export path
14. Rollback

If any required capability is missing, Commerce Plus remains the production commerce system.

## Step 11 — Publish Rules

Initial Airo builds are staging/reference builds.

Do not:

- Connect the production domain during first-pass generation.
- Enable live payment processing during first-pass generation.
- Replace the production storefront before validation.

Publishing to a temporary/staging URL is acceptable for review when it does not alter production DNS or commerce behavior.

## Step 12 — Record the Result

After each meaningful generation pass, record:

- Prompt version
- Airo project name
- Date
- Major deviations from PR-001
- Screens/pages approved
- Screens/pages requiring changes
- Whether code was exported
- Export commit/branch if applicable
- Commerce validation status

## Completion Criteria

RB-002 is complete for a generation cycle when:

- The staging site follows ARC-001.
- Brand rules are correctly applied.
- Generated claims are repository-supported.
- Responsive review is complete.
- Accessibility review is complete.
- Commerce-system boundaries remain intact.
- Any exported code is captured in GitHub for review.

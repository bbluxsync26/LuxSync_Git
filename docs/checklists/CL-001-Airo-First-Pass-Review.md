# CL-001 — Airo First-Pass Review

**Status:** Active / Reconciled
**Updated:** 2026-08-31
**Use:** Immediately after a PR-001 generation in Airo AI Builder

## Structure

- [ ] Home, Shop, Solutions, Guides, About, Contact, and Support exist
- [ ] Search, Account, and Cart are represented appropriately
- [ ] Navigation is compact and follows ARC-001

## Homepage

- [ ] Sole approved slogan / hero line is exactly `Where Luxury Lives Intelligently`
- [ ] No retired alternate slogan or hero treatment appears
- [ ] Supporting copy matches `website/pages/home.md`
- [ ] Primary CTA is `Find My LuxSync Solution`
- [ ] Secondary CTA is `Shop Smart Home`
- [ ] Supporting CTA is `Get the ROI Guide`
- [ ] Featured Solutions uses the five approved segments
- [ ] Find My LuxSync Solution receives flagship visual priority before the main product-collection grid
- [ ] Product Collections, How It Works, featured products, founder preview, FAQ preview, Contact/Support gateway, and lead-magnet blocks are present
- [ ] Featured products do not use invented prices, compatibility, or availability

## Intelligent Living Concierge

- [ ] Entry point is `Find My LuxSync Solution`
- [ ] Guided experience is named `LuxSync Intelligent Living Concierge`
- [ ] Output is named `My LuxSync Blueprint`
- [ ] Experience follows `Lifestyle → Experience → Intelligence → Technology`
- [ ] It is presented as a concierge/guided design experience, not a novelty quiz
- [ ] Property Profile includes property type and approximate square footage/range
- [ ] Relevant residence, STR, and business branching is present
- [ ] Existing technology discovery is present
- [ ] Lifestyle / routine discovery is present where appropriate
- [ ] Pain points and priorities influence recommendations
- [ ] Implementation preference is captured
- [ ] Recommended LuxSync Experiences are shown before exact product recommendations
- [ ] Blueprint includes foundation, compatibility context, implementation path, roadmap, and next best action
- [ ] Every recommendation includes a useful `Why LuxSync Chose This` explanation
- [ ] Implementation paths use `Essential Intelligence`, `Elevated Living`, and `Complete LuxSync Experience`
- [ ] Engine logic follows `website/src/concierge/`
- [ ] No unreleased saved-account or AI features are presented as live

## Dedicated Contact Page

- [ ] Contact page follows `website/pages/contact.md`
- [ ] Direct support email is `support@luxsync.net`
- [ ] Direct information/consultation email is `info@luxsync.net`
- [ ] First selection offers Support
- [ ] First selection offers Product Information
- [ ] First selection offers Consultation
- [ ] First selection offers General Question
- [ ] First selection offers Business / Partnership
- [ ] First selection offers Other
- [ ] Only relevant follow-up questions appear after the first selection
- [ ] Support includes setup, compatibility, SmartThings, automation, connectivity, account/app, order, installation, troubleshooting, and Other paths
- [ ] Product Information includes current product/solution categories
- [ ] Consultation includes `My LuxSync Blueprint Review`
- [ ] Business/Partnership supports property management, STR, real estate, interior design, builders, technology, manufacturer/distributor, corporate, media, affiliate, and Other
- [ ] Relevant Contact paths use the shared Property Profile
- [ ] Property Type includes Private Residence, Short-Term Rental, Business/Commercial, and Other
- [ ] Approximate square footage supports exact entry, ranges, and Not Sure
- [ ] STR branching captures units/platform/remote-management context where relevant
- [ ] Business branching captures business type and locations where relevant
- [ ] Blueprint context is prefilled when technically and legally appropriate
- [ ] Full street address is not required for initial inquiry
- [ ] Marketing consent is separate and optional
- [ ] No invented response-time SLA appears
- [ ] Dynamic submit labels match the selected intent

## Product and Solution Catalog

- [ ] Product-family terminology follows `content/product-catalog.md`
- [ ] Existing curated bundle concepts remain represented accurately
- [ ] Concierge-linked LuxSync Experiences are treated as solution concepts unless validated live SKUs exist
- [ ] No planning concept is misrepresented as current stock
- [ ] Exact product names/prices/stock/shipping/compatibility come only from validated data
- [ ] Senior Independent Safety pricing remains unpublished until DEC-005 is resolved

## Brand System

### Palette

- [ ] Slate Navy `#0D1526` anchors primary dark surfaces
- [ ] Dark Suede `#172036` is used for elevated/card surfaces
- [ ] Pale Driftwood `#D0BEB0` is the primary light text/surface tone
- [ ] Warm Taupe Mauve `#9E8B85` supports secondary information
- [ ] Antique Rose Taupe `#967878` provides restrained warm accent
- [ ] Dusty Steel `#7B96B2` provides interaction emphasis
- [ ] Champagne Rose Gold Metallic uses the `#D6B0A0` anchor for premium emphasis

### Typography

- [ ] Headings, navigation, CTAs, and graphic UI use Manrope 500/600
- [ ] Body copy, product descriptions, forms, and supporting UI use Inter 400/500
- [ ] Montserrat, Century Gothic, Candara, Bodoni-family, Didot, and Georgia are not website-system fonts
- [ ] Approved exact logo artwork is preserved rather than re-typeset

### Plush Drift Tactile Illumination

- [ ] Interactive buttons, cards, Concierge choices, and selectable tiles use darker foreground surfaces over restrained softer underlighting
- [ ] Dusty Steel is the preferred cool underlight
- [ ] Champagne Rose Gold Metallic is a restrained premium edge/accent, not a dominant halo
- [ ] Rest state keeps underlighting faint and localized
- [ ] Hover increases underlight modestly
- [ ] Keyboard focus includes an explicit accessible focus indicator
- [ ] Pressed state gives restrained physical compression/feedback
- [ ] Reduced-motion preference is honored
- [ ] No hard neon outlines, flashing, arcade halos, or glow-only state communication

## About and Leadership

- [ ] About follows `website/pages/about.md` and `content/about.md`
- [ ] Bridgette Beardsley's title is exactly `Co-Founder & Chief Technology and Strategy Officer`
- [ ] Sheldon Bardol's title is exactly `Co-Founder & Chief Customer and Operations Officer`
- [ ] Compact biographies preserve approved source meaning
- [ ] Both founders receive equal visual authority
- [ ] No invented credentials, founder history, or generated photographic likenesses

## Frequently Asked Questions

- [ ] FAQ page exists at `/guides/faqs`
- [ ] Questions and answers follow `content/faqs.md`
- [ ] Homepage shows no more than the approved FAQ preview set
- [ ] Accordion is keyboard operable and exposes expanded state correctly
- [ ] FAQ content remains available without JavaScript where practical
- [ ] FAQ structured data matches visibly rendered content
- [ ] Information routes to `info@luxsync.net`; support routes to `support@luxsync.net`

## Content Integrity

- [ ] No invented awards, testimonials, certifications, press, years in business, or customer counts
- [ ] No unsupported Samsung/SmartThings, Airbnb, or Vrbo endorsement
- [ ] No medical claims
- [ ] No claim that smart-home convenience/security technology replaces emergency services, life-safety systems, or professional monitoring
- [ ] No internal financial or supplier data exposed
- [ ] No unresolved senior-service pricing
- [ ] LuxSync Grid and downloadable SmartThings templates are not presented as live

## Commerce Boundary

- [ ] No live payments connected during staging review
- [ ] No production DNS changes
- [ ] No unmanaged second live catalog
- [ ] Staging cart/checkout is treated as representation until validated
- [ ] Commerce Plus remains the production system of record

## Responsive

- [ ] Desktop, tablet, and mobile reviewed
- [ ] Mobile navigation is compact
- [ ] Search/cart remain easy to reach
- [ ] Concierge choices are thumb-friendly
- [ ] Adaptive Contact fields remain easy to complete on mobile
- [ ] Tap targets and product cards are usable
- [ ] Hero copy and CTAs remain readable and visible

## Accessibility

- [ ] Heading hierarchy is logical
- [ ] Keyboard navigation works
- [ ] Focus states are visible
- [ ] Contrast is acceptable
- [ ] Forms have persistent labels
- [ ] Conditional fields and errors are announced/accessibly connected
- [ ] Images have meaningful alt text where needed
- [ ] Motion is non-essential and respects reduced-motion preferences
- [ ] Information does not rely on color alone

## Result

**Pass / Needs Revision:** ____________________

**Major issues:**

-
-
-

**Approved sections:**

-
-
-

**Next Airo prompt/edit:**

-

## Production Source-of-Truth Checks

- Every required route in `website/implementation-manifest.json` exists.
- Header/footer match `website/navigation.md`.
- Only production-approved assets from `website/asset-map.md` are published.
- No generated logo approximations, baked support hours, fake founder identities or raster product-card fragments appear.
- Concierge uses the tracked production engine configuration.
- My LuxSync Blueprint recommends experiences before products.
- Commerce facts come from validated data.
- Contact begins with the approved adaptive intent branches.

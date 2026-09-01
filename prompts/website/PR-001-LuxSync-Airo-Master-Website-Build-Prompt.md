# PR-001 — LuxSync Airo Master Website Build Prompt

**Status:** Active / Reconciled for staging generation
**Updated:** 2026-08-31
**Purpose:** Generate the LuxSync launch storefront in GoDaddy Airo AI Builder while preserving the repository source of truth, the Intelligent Living Concierge architecture, and the Commerce Plus production boundary.

## Prompt to paste into GoDaddy Airo AI Builder

Build a polished, mobile-first premium intelligent-living and smart-home storefront for **LuxSync LLC**.

This is a **staging/reference build**. Do not connect live payments, alter production DNS, or publish it as the production commerce site during the initial generation/review pass.

The LuxSync GitHub repository is the source of truth. Do not invent a different business model, target audience, visual identity, product strategy, pricing model, technology ecosystem, company history, founder background, or customer claims.

## Company and Positioning

LuxSync is a premium intelligent-living and curated smart-home commerce company launching with a retail-first, zero-inventory model.

LuxSync helps customers create smarter, more elegant, easier-to-manage environments through carefully selected SmartThings-compatible products, curated bundles, thoughtful automation guidance, and a flagship guided recommendation experience.

LuxSync is not a discount electronics retailer, generic DIY marketplace, traditional on-site installer, or software-first startup. The experience should feel like luxury interior architecture with intelligent technology quietly underneath it.

## Official Brand Language

- Company: **LuxSync**
- Sole approved public slogan / hero line: **Where Luxury Lives Intelligently**
- Primary homepage CTA: **Find My LuxSync Solution**
- Secondary homepage CTA: **Shop Smart Home**
- Supporting CTA: **Get the ROI Guide**
- Voice: **Intelligent Calm**

Do not introduce, restore, paraphrase, or regenerate retired LuxSync slogan or hero treatments. **Where Luxury Lives Intelligently** is the governing public slogan and hero line.

Supporting homepage copy:

**Luxury smart-home technology designed for modern living, with curated hardware and thoughtful automation that bring comfort, control, and confidence to every space.**

## Primary Audiences

1. **Short-Term Rental Operators** — guest experience, remote property awareness, access, energy management, water awareness, and turnover efficiency.
2. **Seniors & Caregivers / Accessible Living Customers** — convenience, pathway lighting, simplified control, property awareness, and other non-medical accessibility-supporting technology. Do not make medical claims.
3. **Smart Office & Property Managers** — lighting, climate, access-related routines, energy use, and multi-location property awareness.
4. **Intentional Parents** — household routines, lighting, comfort, and safety-conscious automation without medical or developmental claims.
5. **Busy Professionals** — convenience, ambience, premium experiences, and simplicity without becoming smart-home hobbyists.

Do not add unsupported target segments as established LuxSync markets.

## Navigation

Primary navigation:

**Home · Shop · Solutions · Guides · About · Contact · Support**

Commerce utilities remain separate and easy to reach:

**Search · Account · Cart**

Keep navigation compact and mobile-friendly. Contact and Support may be visually related, but both intents must remain clear.

## Homepage Sequence

1. Hero using **Where Luxury Lives Intelligently**, supporting copy, **Find My LuxSync Solution**, **Shop Smart Home**, and the supporting ROI-guide CTA.
2. Featured Solutions for the five approved audiences.
3. Why LuxSync: Curated Catalog; SmartThings Compatibility; Intelligent Discovery; Simplified Buying; Premium Customer Experience.
4. **Find My LuxSync Solution / Intelligent Living Concierge** flagship section.
5. Product Collections from `content/product-catalog.md`.
6. How It Works: Discover; Design; Choose; Evolve.
7. Featured Products/Bundles using validated catalog data or clearly labeled editable placeholders/solution concepts.
8. Meet the Founders using approved compact biographies and exact titles.
9. Frequently Asked Questions preview using approved homepage questions.
10. Contact / Support gateway.
11. STR Smart Home ROI Guide and calm optional email signup.
12. Footer with Shop, Solutions, Guides, About, Contact, Support, and legal placeholders.

## Flagship Experience — Find My LuxSync Solution

Treat **Find My LuxSync Solution** as a primary customer journey, not a minor product quiz.

Customer-facing architecture:

- Entry point: **Find My LuxSync Solution**
- Guided experience: **LuxSync Intelligent Living Concierge**
- Personalized output: **My LuxSync Blueprint**

Governing sources:

- `docs/architecture/intelligent-living-concierge.md`
- `website/src/concierge/`
- `content/product-catalog.md`

The experience follows:

**Lifestyle → Experience → Intelligence → Technology**

Start with how the customer wants the space to feel and function. Do not begin by asking the customer to choose hubs, protocols, or device models.

The Concierge should progressively capture, where relevant:

- primary intent and desired outcomes
- property type
- approximate square footage or range
- residence / STR / business subtype
- number of levels, units, or locations where relevant
- existing smart-home technology
- current setup health
- arrival, departure, evening, bedtime, morning, entertainment, and other lifestyle preferences
- frustrations / pain points
- accessibility-oriented convenience needs where selected
- priority ranking
- implementation preference

The rules engine under `website/src/concierge/` is the implementation source for stable field IDs, branching, scoring, recommendation thresholds, foundation logic, CTA logic, and Blueprint schema.

Do not replace the repository engine with invented survey logic.

### LuxSync Experiences

Version 1 may recommend these experience concepts:

- Welcome Home
- Effortless Departure
- Goodnight
- Gentle Morning
- Intelligent Evening
- Cinema
- Entertain
- Relax
- Away
- Protect
- Water Watch
- Climate Intelligence
- Energy Intelligence
- Night Path
- Guest Ready
- Turnover
- Property Pulse
- Accessible Living
- Vacation Mode

Experiences are outcome-first solution concepts. They are not automatically individual products or live SKUs.

### Blueprint Reveal

**My LuxSync Blueprint** should reveal progressively:

1. Your Space
2. What Matters Most
3. Your Intelligent Living Profile
4. Recommended LuxSync Experiences
5. Recommended Foundation
6. Compatibility Notes
7. Implementation Path
8. Phased Roadmap
9. Technology Behind the Experience
10. Next Best Action

Every recommendation should include a short **Why LuxSync Chose This** explanation.

### Implementation Paths

Use these names:

- **Essential Intelligence** — highest-impact starting point
- **Elevated Living** — broader connected experience across major spaces
- **Complete LuxSync Experience** — comprehensive implementation of the customer's Blueprint

Do not use Good / Better / Best language.

Possible dynamic CTAs include:

- Build My Solution
- Start With Phase 1
- Review My Compatibility
- Request a LuxSync Consultation
- Build My Rental Solution
- Save My Blueprint
- Ask LuxSync a Question

Do not imply account/save functionality is live unless it is implemented in the generated build.

## Shop and Product Catalog

Use `content/product-catalog.md` as the canonical planning catalog.

Customer-facing product-family architecture may include:

- Foundation & Connectivity
- Entry & Access
- Lighting & Ambience
- Comfort & Climate
- Property Awareness
- Water Protection
- Energy & Power
- Entertainment & Ambience
- Cleaning & Convenience
- Outdoor Living
- Hosting / Short-Term Rental
- Curated Bundles

Existing bundle concepts include:

- STR Property Automation Kit
- STR Guest Welcome & Keyless Entry Bundle
- Smart Sleep Nursery Kit
- Senior Independent Safety Bundle

Senior-service pricing remains unresolved and must not be published until explicitly approved.

Concierge-linked solution concepts may be displayed as experiences or solution pathways, but must not be presented as live purchasable SKUs unless validated commerce entries exist.

Do not invent prices, stock, ratings, reviews, scarcity, supplier relationships, margins, costs, discounts, shipping promises, exact compatibility, subscription terms, or financial projections.

## Solutions

Create pages for the five approved audiences. Each page should cover:

- the customer's need
- desired outcomes
- relevant LuxSync Experiences
- relevant product families / validated bundles
- SmartThings compatibility guidance
- a clear **Find My LuxSync Solution**, Shop, or information CTA

Do not imply Samsung, SmartThings, Airbnb, Vrbo, or another third-party endorsement unless documented.

## Guides and FAQs

Create space for:

- STR Smart Home ROI Guide
- compatibility guidance
- SmartThings setup concepts
- product-selection guidance
- automation ideas
- experience-specific setup guidance as it becomes available
- dedicated FAQ page at `/guides/faqs`

Build the FAQ page from `content/faqs.md` and `website/pages/faqs.md`. Preserve approved meaning. Use accessible accordion behavior, stable question links, and structured data only for visibly rendered FAQ content.

Do not present downloadable SmartThings automation templates or LuxSync Grid as currently available until explicitly released.

## About and Founders

About must follow `content/about.md` and `website/pages/about.md`.

Use these exact leadership identities and approved Compact Biographies from `docs/leadership/`:

- **Bridgette Beardsley — Co-Founder & Chief Technology and Strategy Officer**
- **Sheldon Bardol — Co-Founder & Chief Customer and Operations Officer**

Give both profiles equal visual authority. Do not generate photographic likenesses. Use approved portraits only when supplied; otherwise use a refined branded placeholder or monogram treatment.

Do not invent awards, certifications, testimonials, press, customer counts, years in business, or founder facts.

## Dedicated Contact Page

Create a dedicated Contact page from:

- `website/pages/contact.md`
- `content/contact.md`

The form must use adaptive conditional logic.

First selection:

- Support
- Product Information
- Consultation
- General Question
- Business / Partnership
- Other

### Support

Reveal topics such as Product Setup, Device Compatibility, SmartThings Connection, Automation/Routine, Device Not Responding, Wi-Fi/Connectivity, Account/App, Order, Installation, Troubleshooting, and Other.

Route Support submissions to:

**support@luxsync.net**

### Product Information

Offer relevant categories such as solution bundles, lighting/ambience, entry/access, property awareness, comfort/climate, energy, water protection, entertainment, SmartThings, Matter-compatible devices, Accessible Living, STR solutions, and business solutions.

Route to:

**info@luxsync.net**

### Consultation

Include New Smart Home Planning, Existing Smart Home Upgrade, SmartThings Setup, Home Automation Planning, STR Automation, Accessible Living Technology, Home Entertainment, Smart Lighting, Business/Office Automation, New Construction Planning, and **My LuxSync Blueprint Review**.

Route to:

**info@luxsync.net**

### General Question

Topics may include Products, Compatibility, SmartThings, Ordering, Shipping, Installation, Services, Consultations, Website/Account, Company Information, and Other.

Route to:

**info@luxsync.net**

### Business / Partnership

Topics may include Property Management, STR Management, Real Estate, Interior Design, Home Builder/Construction, Technology Partnership, Device Manufacturer, Distributor/Supplier, Corporate/Office Solutions, Media/Press, Affiliate Opportunity, and Other.

Route to:

**info@luxsync.net**

### Shared Property Profile

For relevant product, consultation, business, and property inquiries, capture the same conceptual Property Profile used by the Concierge:

- Private Residence / Short-Term Rental / Business-Commercial / Other
- approximate square footage or range
- subtype
- units/locations where relevant
- current smart-home ecosystem
- desired outcomes

Provide **Not Sure** wherever exact measurements are not necessary.

When a visitor arrives from My LuxSync Blueprint, preserve/prepopulate relevant Blueprint and property context where technically and legally appropriate so the customer does not re-enter information already supplied in the active journey.

Do not require a full street address for an initial inquiry.

Marketing consent must be separate and optional.

Do not invent response-time SLAs.

## Technology and Commerce Boundary

Samsung SmartThings is the primary launch compatibility standard. Emphasize compatibility before customization, simplicity before complexity, reliability before novelty, and customer experience before technology.

GoDaddy Commerce Plus remains the production commerce system of record. Represent storefront UX in staging, but do not connect live payments, alter production DNS, replace Commerce Plus, or create a second unmanaged live catalog.

## LuxSync Production Raster v5 Brand System

Use **LuxSync Production Raster v5** as the authoritative visual system and **Plush Drift** as the enduring design DNA.

Approved colors:

- Slate Navy `#0D1526`
- Dark Suede `#172036`
- Pale Driftwood `#D0BEB0`
- Warm Taupe Mauve `#9E8B85`
- Antique Rose Taupe `#967878`
- Dusty Steel `#7B96B2`
- Champagne Rose Gold Metallic `#D6B0A0` anchor

Use Champagne Rose Gold Metallic sparingly for premium detail and Dusty Steel for clear interaction states.

Typography:

- **Headings / display / navigation / CTA labels / graphic UI:** Manrope 500/600
- **Body / product copy / forms / supporting UI:** Inter 400/500

Approved exact LuxSync logo artwork may retain its exact visual lettering as artwork. Do not recreate or re-typeset protected logo art.

## Plush Drift Tactile Illumination

Interactive controls should feel like premium backlit physical controls, not flat SaaS buttons.

- darker Slate Navy or Dark Suede foreground
- softer concealed Dusty Steel underlight
- restrained Antique Rose Taupe / Pale Driftwood warmth where appropriate
- Champagne Rose Gold Metallic only as a subtle reflected edge or premium accent
- faint localized rest state
- slightly brighter/wider hover underlight
- explicit accessible keyboard focus indicator
- approximately 1–2px pressed visual compression with tighter shadow
- short calm release easing
- reduced-motion support

Use the effect strongly on interactive controls and more subtly on static cards. Avoid neon halos, hard glowing borders, flashing, arcade lighting, exaggerated bloom, aggressive scaling, or color-only state feedback.

## Voice

Use **Intelligent Calm**: warm, confident, thoughtful, unhurried, professional, human, refined, and approachable.

Avoid hype, fear-based security language, jargon, technical showing-off, urgency, excessive exclamation marks, and unsupported superlatives.

## Responsive, Accessibility, and Performance

Design mobile first.

Target WCAG 2.2 AA practices: semantic headings, keyboard access, visible focus, sufficient contrast, labels, meaningful alt text, adequate touch targets, reduced-motion behavior, and no color-only meaning.

For Contact and Concierge conditional forms, ensure dynamic fields and validation messages are announced/accessibly connected.

Use responsive images, modern formats, lazy loading, stable layouts, efficient font loading, minimal unnecessary JavaScript, and restrained effects.

## Repository Assets

Use the current approved asset system identified by `docs/master-catalog.md` and `brand/README.md`.

- Use protected approved primary logo artwork exactly as supplied.
- Prefer SVG for icons/vector UI and optimized WebP for scene imagery.
- Do not recreate protected logo artwork through an image generator.
- Do not restore graphics containing retired slogan/hero language.

## Future Roadmap

Leave clean expansion points for saved Blueprints, room-by-room planning, natural-language Concierge interaction, SmartThings automation templates, LuxSync Grid, and approved architecture services.

Do not advertise unreleased capabilities as live.

## Final Quality Standard

A first-time visitor should quickly understand that LuxSync is a premium curated intelligent-living brand; **Where Luxury Lives Intelligently** is the single governing slogan; **Find My LuxSync Solution** is a primary way to begin; **My LuxSync Blueprint** recommends experiences before products; SmartThings compatibility helps reduce complexity; the catalog is intentionally curated; Bridgette Beardsley and Sheldon Bardol are the accountable co-founders; and customers can shop, ask questions, request consultations, or get support without becoming smart-home experts.

Every important design, content, interaction, and commerce decision should reinforce:

**Where Luxury Lives Intelligently.**

## Mandatory Production Source-of-Truth Inputs

Before generating the website, read and obey:

- `docs/production-source-of-truth.md`
- `website/implementation-manifest.json`
- `website/navigation.md`
- `website/asset-map.md`
- `website/styles/design-system.md`

Use **Where Luxury Lives Intelligently** as the sole public slogan. Use the exact protected logo files. Build buttons, cards, forms, icons, dividers, Concierge UI and Contact UI as live HTML/CSS. Do not publish the reference-only raster composites, generated logo approximations, baked founder/support information or board-crop fragments under `brand/assets/02-icons/` through `brand/assets/09-stationery/`.

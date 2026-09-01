# PR-001 - LuxSync Airo Master Website Build Prompt

**Status:** Active / Fresh Build Edition / Reconciled for first-pass staging generation  
**Updated:** 2026-09-01  
**Purpose:** Generate the first complete LuxSync website in GoDaddy Airo AI Builder from a clean slate while preserving the current repository source of truth, Production Raster v5 brand system, Plush Drift design DNA, Intelligent Living Concierge architecture, VIP Account Access experience, and GoDaddy Commerce Plus production boundary.

## Prompt to paste into GoDaddy Airo AI Builder

Build a polished, mobile-first premium intelligent-living and smart-home storefront for **LuxSync LLC**.

## Fresh Build Directive

This is a **brand-new first-pass website build from scratch**.

Do not treat this as a redesign, migration, update, refresh, or continuation of any prior LuxSync website. Do not inherit layouts, copy, branding, navigation, account behavior, product data, imagery, or assumptions from an earlier generated site.

Start from a clean website structure and use only the current LuxSync source-of-truth inputs listed in this prompt.

This first pass is a **staging/reference build**. It should look and behave like a complete LuxSync website, but it must not:

- connect live payments;
- alter production DNS;
- publish over the production commerce site;
- create a second unmanaged live catalog;
- collect real customer credentials in a static prototype;
- invent authentication providers or security mechanisms;
- invent product prices, stock, shipping, ratings, reviews, testimonials, scarcity, or compatibility claims;
- advertise roadmap capabilities as currently live.

The LuxSync GitHub repository is the governing source of truth. If GoDaddy Airo cannot directly read a referenced repository path, do not invent the missing content. Use the supplied source material and leave an editable, clearly labeled implementation placeholder where a production integration is required.

## Company and Positioning

LuxSync is a premium intelligent-living and curated smart-home commerce company launching with a retail-first, zero-inventory model.

LuxSync helps customers create smarter, more elegant, easier-to-manage environments through carefully selected SmartThings-compatible products, curated bundles, thoughtful automation guidance, ROI education, and a flagship guided recommendation experience.

LuxSync is not a discount electronics retailer, generic DIY marketplace, traditional on-site installation company, medical monitoring service, or software-first startup.

The experience should feel like luxury interior architecture with intelligent technology quietly underneath it.

## Official Brand Language

- Company: **LuxSync**
- Sole approved public slogan / hero line: **Where Luxury Lives Intelligently**
- Primary homepage CTA: **Find My LuxSync Solution**
- Secondary homepage CTA: **Shop Smart Home**
- Supporting homepage CTA: **Get the ROI Guide**
- Voice: **Intelligent Calm**
- Flagship guided experience: **LuxSync Intelligent Living Concierge**
- Personalized result: **My LuxSync Blueprint**

Do not introduce, restore, paraphrase, or regenerate retired LuxSync slogan or hero treatments. **Where Luxury Lives Intelligently** is the sole governing public slogan.

Preferred supporting homepage copy:

**Luxury smart-home technology designed for modern living, with curated hardware and thoughtful automation that bring comfort, control, and confidence to every space.**

## Primary Audience Architecture

Build the public Solutions architecture around these five current solution paths:

1. **Commercial Offices** - lighting, climate, energy awareness, shared-space routines, access-related experiences, and multi-location property awareness.
2. **Senior Living & Nursing Homes** - non-clinical convenience, pathway lighting, simplified environmental control, property awareness, and operational efficiency. Do not make medical, emergency-response, or life-safety claims.
3. **Short-Term Rentals** - guest experience, remote property awareness, entry/access, energy management, water awareness, and turnover efficiency.
4. **Residential Living** - comfort, ambience, convenience, entertainment, energy awareness, household routines, and elegant automation for modern homes.
5. **Seniors, Caregivers & Aging in Place** - non-medical accessibility-supporting technology, simplified control, pathway lighting, comfort, property awareness, and independence-supporting convenience.

Residential content may appropriately speak to sub-audiences such as busy professionals, intentional parents/families, new homeowners, entertainers, and customers seeking premium convenience, but do not create unsupported markets or claims.

## Canonical Navigation

Primary navigation:

- **Shop** -> `/shop`
- **Solutions** -> `/solutions`
- **Guides** -> `/guides`
- **About** -> `/about`
- **FAQs** -> `/faqs`
- **Contact** -> `/contact`

Persistent utilities, where supported:

- **Search**
- **Account** -> preferred LuxSync experience route `/account/login`, delegated to the real GoDaddy Commerce Plus account flow when integrated
- **Cart**

Primary header CTA:

**Find My LuxSync Solution** -> `/find-my-luxsync-solution`

Support should route through:

`/contact?intent=support`

Do not create `/guides/faqs`. The canonical FAQ route is **`/faqs`**.

Do not create dead navigation, invented social accounts, unsupported commerce utilities, or unsupported authentication routes.

## Canonical First-Pass Page Set

Create a coherent first-pass experience for:

- Home `/`
- Find My LuxSync Solution `/find-my-luxsync-solution`
- My LuxSync Blueprint `/my-luxsync-blueprint`
- Solutions `/solutions`
- Commercial Offices `/solutions/commercial-offices`
- Senior Living & Nursing Homes `/solutions/senior-living`
- Short-Term Rentals `/solutions/short-term-rentals`
- Residential Living `/solutions/residential`
- Seniors, Caregivers & Aging in Place `/solutions/aging-in-place`
- Shop `/shop`
- Guides `/guides`
- About `/about`
- FAQs `/faqs`
- Contact `/contact`
- VIP Account Access route family beginning at `/account/login`, visually implemented but delegated to the real account platform when integrated

The first pass should feel like one connected website, not a collection of unrelated AI-generated pages.

## Homepage Sequence

1. Hero using **Where Luxury Lives Intelligently**.
2. Supporting copy and three clear paths: **Find My LuxSync Solution**, **Shop Smart Home**, **Get the ROI Guide**.
3. Featured Solutions for the five canonical audience paths.
4. Why LuxSync: Curated Catalog; SmartThings Compatibility; Intelligent Discovery; Simplified Buying; Premium Customer Experience.
5. Flagship **Find My LuxSync Solution / Intelligent Living Concierge** section.
6. Product Collections from `content/product-catalog.md`.
7. How It Works: Discover; Design; Choose; Evolve.
8. Featured products or bundle concepts using validated catalog data or clearly labeled non-commerce concepts only.
9. Meet the Founders using approved biographies and exact titles.
10. FAQ preview using approved questions.
11. ROI Guide gateway with audience-aware guide choices.
12. Contact / Support gateway.
13. Calm optional email signup only if consent is separate and optional.
14. Footer with Shop, Solutions, Guides, About, FAQs, Contact, Support, Account, and legal placeholders.

## Flagship Experience - Find My LuxSync Solution

Treat **Find My LuxSync Solution** as a primary customer journey, never as a lightweight product quiz.

Customer-facing architecture:

- Entry point: **Find My LuxSync Solution**
- Guided experience: **LuxSync Intelligent Living Concierge**
- Personalized output: **My LuxSync Blueprint**

Governing sources:

- `docs/architecture/intelligent-living-concierge.md`
- `website/src/concierge/`
- `content/product-catalog.md`

The experience follows:

**Lifestyle -> Experience -> Intelligence -> Technology**

Start with how the customer wants the space to feel and function. Do not start by asking them to choose hubs, protocols, standards, or device models.

The Concierge should progressively capture, where relevant:

- primary intent and desired outcomes;
- property type;
- approximate square footage or range;
- residence / STR / business subtype;
- levels, units, or locations where relevant;
- existing smart-home ecosystem;
- current setup health;
- arrival, departure, evening, bedtime, morning, entertainment, hosting, vacation, and other lifestyle preferences;
- frustrations / pain points;
- accessibility-oriented convenience needs where selected;
- priority ranking;
- implementation preference.

The rules engine under `website/src/concierge/` is the implementation source for stable field IDs, branching, scoring, recommendation thresholds, foundation logic, CTA logic, and Blueprint schema.

Do not replace repository logic with invented survey scoring.

### LuxSync Experiences

Version 1 may recommend these outcome-first experience concepts:

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

Experiences are solution concepts. They are not automatically live purchasable SKUs.

### My LuxSync Blueprint Reveal

Reveal progressively:

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

Every recommendation should include a concise **Why LuxSync Chose This** explanation.

### Implementation Paths

Use these names:

- **Essential Intelligence** - highest-impact starting point
- **Elevated Living** - broader connected experience across major spaces
- **Complete LuxSync Experience** - comprehensive implementation of the customer's Blueprint

Do not use Good / Better / Best language.

Possible dynamic CTAs include:

- Build My Solution
- Start With Phase 1
- Review My Compatibility
- Request a LuxSync Consultation
- Build My Rental Solution
- Save My Blueprint
- Ask LuxSync a Question

Only show save/account-dependent CTAs as functional when the actual account capability exists. Otherwise style them as future-ready or omit them from the first pass.

## Shop and Product Catalog

Use `content/product-catalog.md` as the canonical planning catalog.

Customer-facing product families may include:

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

Current bundle concepts may include:

- STR Property Automation Kit
- STR Guest Welcome & Keyless Entry Bundle
- Smart Sleep Nursery Kit
- Senior Independent Safety Bundle

These are planning concepts unless validated as live commerce entries.

Senior-service pricing remains unresolved and must not be published until explicitly approved.

Do not invent:

- prices;
- stock or scarcity;
- ratings or reviews;
- supplier relationships;
- margins or costs;
- discounts;
- shipping promises;
- warranties;
- exact compatibility that has not been validated;
- subscription terms;
- product endorsements;
- financial projections.

GoDaddy Commerce Plus remains the production commerce system of record.

## Solutions Pages

Each of the five canonical Solutions pages should include:

- who the experience is for;
- the customer's typical needs;
- desired outcomes;
- relevant LuxSync Experiences;
- relevant product families or validated bundles;
- SmartThings compatibility guidance;
- relevant ROI Guide CTA where available;
- a clear **Find My LuxSync Solution**, Shop, or Consultation CTA.

Do not imply Samsung, SmartThings, Airbnb, Vrbo, or any third party endorses LuxSync unless documented.

## ROI Guide Library

Treat ROI Guides as an important educational and conversion path, not a single STR download.

Create a polished Guides library capable of representing these current audiences:

- Commercial Offices
- Nursing Homes
- Senior Living Communities
- STR Owners
- STR Operators
- STR Managers
- Residential Homeowners
- Busy Professionals
- Intentional Parents and Families
- Seniors, Caregivers, and Aging in Place

Governing source:

`content/guides/roi/`

Use scenario-based education, journals, measurement fields, and clearly labeled examples. Never promise returns, guaranteed savings, medical outcomes, or unsupported savings percentages.

First-pass website CTAs may link to guide detail/download areas even if advanced logged-in tracking is reserved for a later phase.

## FAQs

Build the dedicated FAQ page at **`/faqs`** from:

- `content/faqs.md`
- `website/pages/faqs.md`

Use accessible accordion behavior, stable question links, semantic structure, and FAQ structured data only for visibly rendered FAQ content.

Do not present unreleased SmartThings automation templates or LuxSync Grid as currently available.

## About and Founders

About must follow:

- `content/about.md`
- `website/pages/about.md`
- `docs/leadership/`

Use these exact leadership identities and titles:

- **Bridgette Beardsley - Co-Founder & Chief Technology and Strategy Officer**
- **Sheldon Bardol - Co-Founder & Chief Customer and Operations Officer**

Give both profiles equal visual authority.

Do not generate photographic likenesses. Use approved portraits only if supplied. If no portrait is available, use a neutral premium image placeholder that cannot be confused with the LuxSync logo.

Do not invent awards, certifications, testimonials, press, customer counts, years in business, founder history, or credentials.

## Dedicated Contact Page

Create the dedicated adaptive Contact page from:

- `website/pages/contact.md`
- `content/contact.md`

The first selection must include:

- Support
- Product Information
- Consultation
- General Question
- Business / Partnership
- Other

### Support

Possible topics include Product Setup, Device Compatibility, SmartThings Connection, Automation/Routine, Device Not Responding, Wi-Fi/Connectivity, Account/App, Order, Installation, Troubleshooting, and Other.

Route Support submissions to:

**support@luxsync.net**

### Product Information

Use relevant categories from the current product architecture.

Route to:

**info@luxsync.net**

### Consultation

Possible consultation paths include New Smart Home Planning, Existing Smart Home Upgrade, SmartThings Setup, Home Automation Planning, STR Automation, Accessible Living Technology, Home Entertainment, Smart Lighting, Business/Office Automation, New Construction Planning, and **My LuxSync Blueprint Review**.

Route to:

**info@luxsync.net**

### General Question

Route to:

**info@luxsync.net**

### Business / Partnership

May include Property Management, STR Management, Real Estate, Interior Design, Home Builder/Construction, Technology Partnership, Device Manufacturer, Distributor/Supplier, Corporate/Office Solutions, Media/Press, Affiliate Opportunity, and Other.

Route to:

**info@luxsync.net**

### Shared Property Profile

For relevant product, consultation, partnership, and property inquiries, use the same conceptual Property Profile as the Concierge:

- `property_type`
- `square_feet_exact`
- `square_feet_band`
- residence / STR / business subtype
- units / levels / locations where relevant
- current smart-home ecosystem
- customer goals / desired outcomes

Provide **Not Sure** where exact measurements are unnecessary.

When a visitor arrives from My LuxSync Blueprint, preserve or prepopulate relevant Blueprint and property context where technically and legally appropriate.

Do not require a full street address for an initial inquiry.

Marketing consent must be separate and optional.

Do not invent response-time SLAs.

## VIP Account Access

Account access is part of the LuxSync brand experience, not a generic utility page.

Governing sources:

- `website/pages/account-login.md`
- `website/account-access-manifest.json`
- `website/styles/account-access-tokens.css`
- `website/assets/auth/manifest.json`
- `docs/checklists/CL-002-Account-Access-Review.md`

### Experience principle

Every LuxSync customer should receive the same high-care, VIP-level welcome.

VIP means calm, personal, private-feeling, thoughtful, friction-light, and polished. It does not mean artificial status tiers, exclusionary membership theater, fake exclusivity, or invented loyalty levels.

### Preferred account route family

- `/account/login`
- `/account/create`
- `/account/forgot-password`
- `/account/reset-password`
- `/account/verify`
- `/account/verification-code`
- `/account/locked`
- `/account/welcome`

These are preferred UX routes, not guaranteed production routes. Final routing must follow the actual supported GoDaddy Commerce Plus account integration.

### VIP login design

Desktop:

- calm two-zone composition;
- welcome atmosphere on the left;
- login card on the right;
- approved Horizontal Combo logo used directly;
- text-free ambient art behind live HTML text;
- restrained concealed underlight behind the account card.

Mobile:

- one column;
- approved Orb logo;
- welcome message;
- login card;
- recovery/create/support paths;
- mobile ambient art used only as atmosphere.

Preferred messaging:

- Eyebrow: **MEMBER ACCESS**
- Headline: **Welcome Back**
- Support line: **Your LuxSync experience is ready.**
- Primary action: **Sign In**
- Create action: **Create Your LuxSync Account**

### Authentication boundary

GoDaddy Commerce Plus remains the current production commerce/account authority.

For this first Airo build:

- reproduce the LuxSync account visual experience;
- do not create or store real credentials in prototype code;
- do not invent Apple, Google, Microsoft, social login, passkeys, SSO, MFA, biometrics, password policy, token policy, or session behavior;
- do not imply verification exists unless supported by the real platform;
- where a live auth integration is unavailable, use a clearly non-production visual state or delegated account link instead of fabricating backend behavior.

### Approved account graphics

Production-approved ambient vectors are under:

`website/assets/auth/`

Use only entries marked `production-approved` in:

`website/assets/auth/manifest.json`

Reference-only diagrams such as auth card/input/button state boards must not be published as functional UI.

## Protected Logo Rule

Use **only** the approved LuxSync logo masters:

- Desktop primary: `brand/assets/logos/png/luxsync-horizontal-combo.png`
- Extended horizontal alternate: `brand/assets/logos/png/luxsync-horizontal.png`
- Compact/mobile: `brand/assets/logos/png/luxsync-orb.png`

These are immutable brand masters.

Never:

- redraw the logo;
- retype the logo;
- recolor the logo;
- regenerate the logo;
- simplify the logo;
- create an inspired-by logo;
- generate alternate initials;
- create substitute monograms;
- place decorative marks that could be confused with the LuxSync logo.

If an exact approved logo asset cannot be loaded, leave the logo placement blank or use a clearly labeled implementation placeholder. Never improvise a replacement.

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

Use Champagne Rose Gold like jewelry, not wallpaper. Keep it to fine edges, restrained dividers, reflected premium detail, and subtle highlights.

Use Dusty Steel as the preferred cool interaction underlight.

Typography:

- **Headings / display / navigation / CTA labels / graphic UI:** Manrope 500/600
- **Body / product copy / forms / supporting UI:** Inter 400/500

The approved LuxSync logo lettering remains artwork. Never recreate it with typography.

## Plush Drift Tactile Illumination

Interactive controls should feel like premium backlit architectural controls rather than flat SaaS buttons.

Layering:

1. Slate Navy environmental field.
2. Low-opacity warm/cool atmosphere.
3. Dark Suede foreground control or card.
4. Concealed Dusty Steel underlight.
5. Restrained Champagne Rose Gold reflected edge.
6. Live content and accessible focus/state layer.

Interaction behavior:

- Rest: faint localized underlight.
- Hover: underlight subtly widens and brightens.
- Focus: explicit visible focus indicator plus restrained underlight.
- Press: approximately 1-2px visual compression, tighter shadow, slightly stronger concealed light.
- Release: calm return in roughly 140-220ms.
- Reduced motion: remove physical travel while preserving obvious state differentiation.

Use the effect most strongly on buttons, form controls, navigation actions, Concierge selections, Contact intent cards, and account controls. Use it more subtly on static cards.

Avoid neon, cyberpunk color, hard glowing outlines, flashing, arcade lighting, giant bloom, aggressive scaling, bouncing, or glow-only state communication.

## Voice

Use **Intelligent Calm**: warm, confident, thoughtful, unhurried, professional, human, refined, and approachable.

Avoid hype, fear-based security language, jargon, technical showing-off, urgency, excessive exclamation marks, unsupported superlatives, fake luxury language, and artificial exclusivity.

## Responsive, Accessibility, and Performance

Design mobile first.

Target WCAG 2.2 AA-oriented practices:

- semantic headings;
- keyboard access;
- visible focus;
- sufficient contrast;
- semantic form labels;
- meaningful alt text;
- minimum 44px touch targets;
- reduced-motion behavior;
- no color-only meaning;
- no glow-only meaning;
- accessible dynamic Contact and Concierge fields;
- validation messages programmatically associated with fields.

Use responsive imagery, modern formats, lazy loading, stable layout behavior, efficient font loading, restrained animation, and minimal unnecessary JavaScript.

## Repository Asset Policy

Use the current approved asset system identified by:

- `docs/master-catalog.md`
- `docs/production-source-of-truth.md`
- `brand/README.md`
- `brand/assets/README.md`
- `website/asset-map.md`

Rules:

- use exact protected logo artwork directly;
- build buttons, cards, forms, icons, dividers, navigation, Concierge UI, Contact UI, and auth UI as live HTML/CSS;
- use production-approved account vectors only from `website/assets/auth/manifest.json`;
- do not publish reference-only imported raster composites under `brand/assets/02-icons/` through `brand/assets/09-stationery/`;
- do not restore graphics with retired slogan or generated logo approximations;
- use validated commerce/manufacturer imagery for real products when available;
- do not bake mutable support, customer, account, product, pricing, founder, or availability information into decorative graphics.

## Technology and Commerce Boundary

Samsung SmartThings is the primary launch compatibility standard.

Emphasize:

- compatibility before customization;
- simplicity before complexity;
- reliability before novelty;
- customer experience before technical showing-off.

GoDaddy Commerce Plus remains the production commerce system of record and current account authority.

The first-pass Airo build may represent storefront UX and account UX, but it must not replace Commerce Plus, connect live payments, alter production DNS, fabricate auth behavior, or create a second unmanaged live catalog.

## Future Roadmap

Leave clean expansion points for:

- saved My LuxSync Blueprints;
- saved recommendations;
- interactive ROI Guide tracking;
- member journals and measurements;
- room-by-room planning;
- natural-language Concierge interaction;
- SmartThings automation templates;
- LuxSync Grid;
- approved architecture services;
- installable/PWA-style member experiences where the final platform supports them.

Do not advertise these as live unless they are actually implemented and approved.

## First-Pass Build Priorities

For this first generation, prioritize in this order:

1. Correct brand identity and exact approved logos.
2. Correct canonical navigation and routes.
3. Strong homepage hierarchy and primary CTA.
4. Complete Solutions architecture.
5. Intelligent Living Concierge entry journey and Blueprint presentation.
6. Shop architecture using safe catalog placeholders where live commerce data is unavailable.
7. Guides / ROI library.
8. About / founder content.
9. FAQ page at `/faqs`.
10. Adaptive Contact experience.
11. VIP Account Access visual experience.
12. Mobile responsiveness, accessibility, and performance.

Do not spend the first pass inventing integrations that are not yet validated.

## First-Pass Acceptance Criteria

The build passes the first review only if:

- the site visibly looks like one LuxSync experience rather than a generic template;
- **Where Luxury Lives Intelligently** is the only public slogan;
- the approved logo masters are used directly and exclusively;
- Manrope and Inter are used correctly;
- the palette matches Production Raster v5;
- Plush Drift tactile illumination is evident but restrained;
- the five canonical Solutions paths are present;
- `/faqs` is used as the FAQ route;
- **Find My LuxSync Solution** is a primary journey;
- My LuxSync Blueprint recommends experiences before technology;
- Contact uses adaptive intent branching;
- Account looks premium and VIP-level without inventing backend authentication;
- Guides represent the broader ROI library rather than only one STR guide;
- no unsupported claims, prices, reviews, testimonials, badges, awards, shipping promises, or endorsements appear;
- no generated substitute LuxSync logo appears anywhere;
- no reference-only raster board slices are published as live UI;
- the site works coherently on mobile and desktop;
- production commerce, authentication, payments, and DNS remain untouched.

## Mandatory Production Source-of-Truth Inputs

Before generating the website, read and obey the current versions of:

1. `docs/production-source-of-truth.md`
2. `docs/master-catalog.md`
3. `website/implementation-manifest.json`
4. `website/navigation.md`
5. `website/asset-map.md`
6. `website/styles/design-system.md`
7. `website/pages/`
8. `content/`
9. `docs/architecture/intelligent-living-concierge.md`
10. `website/src/concierge/`
11. `website/account-access-manifest.json`
12. `website/pages/account-login.md`
13. `website/styles/account-access-tokens.css`
14. `website/assets/auth/manifest.json`
15. `brand/README.md`
16. `brand/assets/README.md`
17. `brand/assets/01-logos/`

If any instruction in older generated material conflicts with these current sources, the current source-of-truth documents win.

## Final Quality Standard

A first-time visitor should quickly understand that:

- LuxSync is a premium curated intelligent-living brand;
- **Where Luxury Lives Intelligently** is the governing slogan;
- **Find My LuxSync Solution** is a primary way to begin;
- the Concierge starts with lifestyle outcomes rather than devices;
- My LuxSync Blueprint recommends experiences before technology;
- SmartThings compatibility helps reduce complexity;
- the product catalog is intentionally curated;
- ROI Guides help customers measure value without promising results;
- Bridgette Beardsley and Sheldon Bardol are the accountable co-founders;
- customers can shop, explore solutions, ask questions, request consultations, get support, or access their account without becoming smart-home experts;
- the entire experience feels calm, intelligent, premium, and unmistakably LuxSync.

Every important design, content, interaction, and commerce decision should reinforce:

**Where Luxury Lives Intelligently.**

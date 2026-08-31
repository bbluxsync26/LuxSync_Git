# LuxSync Homepage Blueprint

**Status:** Active launch baseline  
**Architecture reference:** `docs/architecture/website-information-architecture.md`  
**Concierge reference:** `docs/architecture/intelligent-living-concierge.md`

## 1. Hero

### Brand

LuxSync

### Official slogan / hero line

**Where Luxury Lives Intelligently**

This is the only approved public slogan/hero line. Do not introduce retired alternate hero phrases.

### Supporting copy

Luxury smart-home technology designed for modern living, with curated hardware and thoughtful automation that bring comfort, control, and confidence to every space.

### Calls to action

- Primary: **Find My LuxSync Solution**
- Secondary: **Shop Smart Home**
- Supporting: **Get the ROI Guide**

### Visual direction

Use LuxSync v3: Slate Navy / Dark Suede surfaces, restrained Champagne Rose Gold Metallic detail anchored at `#D6B0A0`, Dusty Steel interaction accents, Pale Driftwood copy, generous negative space, and premium smart-living imagery. Use current approved assets. Keep the primary and secondary CTAs visible above the fold on desktop and mobile.

---

## 2. Featured Solutions

Present the five approved customer segments as outcome-oriented pathways:

- Short-Term Rentals
- Seniors & Caregivers / Accessible Living
- Smart Office & Property Management
- Intentional Parents
- Busy Professionals

Each card should lead to a solution page or directly into a pre-contextualized Concierge journey rather than dumping the visitor into a generic product grid.

---

## 3. Why LuxSync

Explain the launch differentiation:

- **Curated Catalog** — thoughtful selection rather than endless choice
- **SmartThings Compatibility** — products selected around a common launch ecosystem
- **Intelligent Discovery** — begin with how the customer wants the space to live
- **Simplified Buying** — clear collections and bundles
- **Premium Customer Experience** — elegant presentation, guidance, and support

Use the Intelligent Calm voice. Avoid unsupported claims.

---

## 4. Find My LuxSync Solution

This is a flagship homepage experience and should appear before the main product-collection grid.

### Customer-facing identity

- Entry CTA: **Find My LuxSync Solution**
- Guided experience: **LuxSync Intelligent Living Concierge**
- Personalized result: **My LuxSync Blueprint**

### Heading

**Tell us how you want your space to live.**

### Body

**LuxSync starts with your space, routines, priorities, and existing technology. We translate those goals into recommended intelligent-living experiences, compatible technology categories, and a phased Blueprint you can build at your own pace.**

### Experience contract

The journey follows:

**Lifestyle → Experience → Intelligence → Technology**

The Concierge should capture property type, approximate square footage, existing technology, lifestyle goals, pain points, priorities, and implementation preference. It should reveal recommended LuxSync Experiences, foundation, compatibility notes, implementation path, roadmap, and next best action.

Use the actual engine under `website/src/concierge/`. Do not implement this as a novelty quiz.

Primary CTA: **Find My LuxSync Solution**

Secondary CTA: **See How the Blueprint Works**

---

## 5. Product Collections

Feature the current customer-facing collection structure from `content/product-catalog.md`.

Primary collection groupings include:

- Foundation & Connectivity
- Entry & Access
- Lighting & Ambience
- Comfort & Climate
- Property Awareness
- Water Protection
- Energy & Power
- Entertainment
- Hosting / Short-Term Rental
- Curated Bundles

Use validated commerce data for exact live items.

Primary section CTA: **Shop Collections**

---

## 6. How It Works

Use a concise four-step flow:

1. **Discover** — tell LuxSync about the space, routine, property, or outcome.
2. **Design** — receive recommended Experiences and My LuxSync Blueprint.
3. **Choose** — select validated compatible products or bundles.
4. **Evolve** — add compatible experiences over time.

Do not position LuxSync as a traditional on-site installation company unless a future repository decision changes the model.

---

## 7. Featured Products and Bundles

Display a restrained set of validated products, bundles, or clearly labeled solution concepts from `content/product-catalog.md`.

Rules:

- Product names, prices, stock state, compatibility, and availability must come from validated commerce/manufacturer data.
- Use editable placeholders during design when live catalog data is unavailable.
- Do not expose supplier costs or internal margin information.
- Do not invent ratings, reviews, badges, scarcity, or stock urgency.
- LuxSync Experiences are not automatically live SKUs.

---

## 8. Meet the Founders

Use a compact, balanced introduction to LuxSync leadership.

- **Bridgette Beardsley — Co-Founder & Chief Technology and Strategy Officer**
- **Sheldon Bardol — Co-Founder & Chief Customer and Operations Officer**

Use the Compact Biographies from `docs/leadership/`. Keep both profiles equal in visual weight and link to the About page. Do not invent credentials, portraits, or founder history.

---

## 9. Frequently Asked Questions

Show the six-question preview defined in `website/pages/faqs.md`, using shortened answers from `content/faqs.md` without changing their meaning.

- Section CTA: **View All FAQs**
- Secondary path: **Contact LuxSync**

Use accessible accordions and keep the section calm and concise.

---

## 10. Contact and Support

Provide a concise gateway to the dedicated adaptive Contact page in `website/pages/contact.md`.

Show:

- **Get Support** → support path
- **Ask a Question** → general information path
- **Request a Consultation** → consultation path

The full Contact form branches dynamically and shares Property Profile fields with the Concierge.

---

## 11. Lead Magnet and Email Signup

Feature the **LuxSync ROI Guide Library** with direct paths for Commercial & Care Environments, Short-Term Rentals, and Residential Living. The supporting homepage CTA remains **Get the ROI Guide** and should open the guide library so visitors can choose the audience-specific edition that fits them.

At minimum, surface cards for:

- Commercial Offices
- Nursing Homes
- Senior Living Communities
- STR Owners, Operators, and Managers
- Residential Homeowners
- Busy Professionals
- Intentional Parents and Families
- Seniors, Caregivers, and Aging in Place

Provide an email signup with calm, benefit-led copy rather than urgency. Marketing consent must remain separate from support/contact submissions.

---

## 12. Footer

Include:

- Shop
- Solutions
- Guides
- About
- Contact
- Support
- Privacy placeholder
- Terms placeholder
- Social links only for approved active channels

Commerce utilities such as Search, Account, and Cart should remain accessible through the site header/navigation pattern.

---

## Responsive Rules

### Desktop

- Editorial hero
- Controlled content width
- Spacious section rhythm
- Curated multi-column card layouts
- Concierge feature receives strong visual priority

### Tablet

- Preserve hierarchy
- Reduce columns
- Keep Concierge and commerce CTAs obvious

### Mobile

- Compact navigation
- Search/cart readily accessible
- One-column sections where appropriate
- Large tap targets
- Manrope headings and Inter body/UI remain readable
- Concierge choices remain easy to tap
- Avoid horizontally compressed desktop layouts

---

## Brand Rules

### Base palette

- Slate Navy `#0D1526`
- Dark Suede `#172036`
- Pale Driftwood `#D0BEB0`
- Warm Taupe Mauve `#9E8B85`
- Antique Rose Taupe `#967878`
- Dusty Steel `#7B96B2`
- Champagne Rose Gold Metallic `#D6B0A0` anchor

Use Champagne Rose Gold Metallic sparingly for premium detail and Dusty Steel for clear interactive states.

### Typography

- Headings / display / navigation / graphic UI: **Manrope 500/600**
- Body / supporting UI: **Inter 400/500**

Approved exact logo artwork is exempt from re-typesetting and does not redefine site fonts.

### Voice

**Intelligent Calm:** warm, confident, thoughtful, unhurried, professional, and human.

### Interaction

Apply Plush Drift tactile illumination to interactive cards, Concierge choices, CTAs, and navigation controls. Keep backlighting restrained and accessible.

---

## Homepage Acceptance Criteria

The homepage succeeds when a new visitor can quickly understand:

1. LuxSync is a curated premium intelligent-living and smart-home commerce brand.
2. **Where Luxury Lives Intelligently** is the single governing slogan/hero line.
3. Find My LuxSync Solution is a primary way to begin.
4. My LuxSync Blueprint recommends experiences before products.
5. What kinds of solutions and products are available.
6. Why compatibility and curation matter.
7. How to shop, ask a question, request a consultation, or get support.
8. Who leads LuxSync and why the company exists.

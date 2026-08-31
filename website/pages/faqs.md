# LuxSync FAQ Page Blueprint

**Status:** Active website design baseline
**Company:** LuxSync LLC
**Brand system:** LuxSync v3
**Canonical content:** `content/faqs.md`

## Page Goal

Answer common questions clearly, reduce uncertainty before purchase, and route customers to the right next step without making LuxSync feel like a technical support portal.

## Recommended Route and Metadata

- Route: `/guides/faqs`
- Page title: `LuxSync FAQs | Smart-Home Products, Compatibility and Support`
- Meta description: `Get clear answers about LuxSync, SmartThings compatibility, curated smart-home solutions, shopping, setup, support, and future services.`

## Entry Points

Link the FAQ page from:

- Guides navigation and Guides landing page
- Support page
- Homepage FAQ preview
- About-page CTA band
- Contact-form helper text
- Product and solution pages where a relevant answer prevents confusion

## Page Sequence

### 1. Hero

- Eyebrow: **LuxSync Guides**
- Heading: **Questions, thoughtfully answered.**
- Supporting copy: **Clear guidance for choosing compatible products, understanding the LuxSync experience, and finding the right kind of help.**
- Primary CTA: **Find My LuxSync Solution**
- Secondary CTA: **Contact LuxSync**

### 2. FAQ Search and Categories

Provide an optional lightweight client-side search labeled **Search frequently asked questions**.

Category filters:

- About LuxSync
- Choosing a Solution
- Products & Compatibility
- Shopping, Setup & Support
- Safety, Caregiving & Future Services

Search and filters enhance discovery but must not hide the complete FAQ content when JavaScript is unavailable.

### 3. Accessible Accordion

Render the canonical questions and answers from `content/faqs.md` as a calm single-column accordion.

Requirements:

- Use native `<details>` and `<summary>` where practical, or equivalent buttons with correct `aria-expanded` and `aria-controls` behavior.
- Every question and answer remains available to screen readers and search engines.
- Keyboard users can reach and operate every question.
- Opening one answer must not forcibly close another.
- Do not animate accordion height when reduced motion is requested.
- Deep links to individual questions should be supported with stable IDs.

### 4. Contextual Next Steps

Where appropriate, place quiet inline links beneath an answer:

- **Find My LuxSync Solution** for customers who need a recommendation
- **Shop Smart Home** for customers ready to browse
- **Contact Information** for product-selection questions
- **Contact Support** for existing orders or products

Do not place aggressive sales CTAs inside every answer.

### 5. Contact Fallback

- Heading: **Still deciding what fits?**
- Body: **Tell us about your space and what you want it to do. We will route your question to the right LuxSync path.**
- Primary CTA: **Find My LuxSync Solution**
- Secondary CTA: **Contact LuxSync**
- Information email: `info@luxsync.net`
- Support email: `support@luxsync.net`

## Homepage FAQ Preview

Show no more than six questions:

1. What is LuxSync?
2. What makes LuxSync different from a typical electronics store?
3. Where should I begin if I am not sure what I need?
4. Which smart-home platform does LuxSync support?
5. Does LuxSync provide on-site installation?
6. How can I get product or compatibility help?

Use short answers from the canonical content and link to **View All FAQs**.

## Structured Data and SEO

- Add `FAQPage` structured data only for questions and answers visibly rendered on the page.
- Structured-data wording must match the visible canonical answer meaning.
- Do not mark founder biographies, product marketing, or hidden keywords as FAQ answers.
- Use one H1 and a logical heading hierarchy.

## Visual and Brand Treatment

- Use LuxSync v3 assets and the approved seven-color palette only.
- Manrope 500/600 for questions, filters, and headings.
- Inter 400/500 for answers and supporting text.
- Use Champagne Rose Gold Metallic sparingly for selected dividers or expanded-state detail.
- Use Dusty Steel for visible focus and interactive state where contrast permits.
- Keep the page spacious and editorial; avoid a dense help-center grid.

## Content Guardrails

- `content/faqs.md` governs the answers.
- Do not invent compatibility, product availability, service coverage, shipping, return, warranty, subscription, or response-time claims.
- Do not present roadmap products as live.
- Do not make medical, emergency-monitoring, third-party endorsement, or universal compatibility claims.

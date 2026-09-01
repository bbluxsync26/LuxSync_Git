# LuxSync Contact Page Blueprint

**Status:** Active design baseline
**Content source:** `content/contact.md`
**Shared data contract:** LuxSync Property Profile used by `website/src/concierge/`

**Official slogan:** **Where Luxury Lives Intelligently**

## 1. Purpose

Create a dedicated Contact page that acts as an intelligent routing surface for support, product information, consultations, general questions, and business/partnership inquiries.

The page must feel like a concierge desk, not a generic form. Use conditional logic so visitors see only fields relevant to their first selection.

## 2. Header

# Contact LuxSync

**Smart living questions deserve intelligent answers.**

Supporting copy should explain that LuxSync can help with existing solutions, product questions, consultations, business opportunities, and general questions.

Display direct contact cards:

- **Customer Support:** `support@luxsync.net`
- **General Information:** `info@luxsync.net`

Primary CTA: **Start Contact Form**

## 3. Step 1 — What Can We Help You With?

Field ID: `contact_intent`

Use single-select cards:

- Support
- Product Information
- Consultation
- General Question
- Business / Partnership
- Other

The selected value controls the next branch.

## 4. Support Branch

If `contact_intent = support`, ask:

### What do you need help with?

Field ID: `support_topic`

Options:

- Product Setup
- Device Compatibility
- SmartThings Connection
- Automation or Routine
- Device Not Responding
- Wi-Fi or Connectivity
- Account or App Question
- Order Question
- Installation Question
- Troubleshooting
- Other

Then ask:

### Do you already own or use a LuxSync product or solution?

Field ID: `existing_customer`

Options: Yes / No / Not Sure

If Yes, reveal:

- LuxSync product, bundle, solution, or Blueprint reference
- Device/platform involved
- Description of the issue
- Optional screenshot/photo upload

Device/platform choices may include Samsung SmartThings, Matter, Amazon Alexa, Google Home, smart lighting, locks, cameras, sensors, climate, entertainment, networking/Wi-Fi, and Other.

Helper text: **Please include error messages, device names, and steps you have already tried.**

Route submissions to `support@luxsync.net`.

## 5. Product Information Branch

If `contact_intent = product_information`, ask:

### What would you like information about?

Field ID: `product_interest`

Options:

- LuxSync Solution Bundles
- Smart Lighting & Ambience
- Smart Entry & Access
- Property Awareness & Security
- Comfort & Climate
- Energy Intelligence
- Water Protection
- Entertainment
- SmartThings
- Matter-Compatible Devices
- Accessible Living
- Short-Term Rental Solutions
- Business / Office Solutions
- Other

Then continue to the shared Property Profile when the inquiry relates to a property or solution.

Route to `info@luxsync.net`.

## 6. Consultation Branch

If `contact_intent = consultation`, ask:

### What type of consultation are you interested in?

Field ID: `consultation_type`

Options:

- New Smart Home Planning
- Existing Smart Home Upgrade
- SmartThings Setup
- Home Automation Planning
- Short-Term Rental Automation
- Accessible Living Technology
- Home Entertainment
- Smart Lighting
- Business / Office Automation
- New Construction Planning
- My LuxSync Blueprint Review
- Other

Then continue to the shared Property Profile.

If the visitor arrived from **My LuxSync Blueprint**, prepopulate property and Blueprint context where technically and legally appropriate.

Route to `info@luxsync.net`.

## 7. General Question Branch

If `contact_intent = general_question`, ask:

### What is your question about?

Field ID: `general_topic`

Options:

- Products
- Compatibility
- SmartThings
- Ordering
- Shipping
- Installation
- Services
- Consultations
- Website or Account
- Company Information
- Other

Then show a required large text field: `question_text`.

Route to `info@luxsync.net`.

## 8. Business / Partnership Branch

If `contact_intent = business_partnership`, ask:

### What are you contacting LuxSync about?

Field ID: `business_topic`

Options:

- Property Management
- Short-Term Rental Management
- Real Estate
- Interior Design
- Home Builder / Construction
- Technology Partnership
- Device Manufacturer
- Distributor / Supplier
- Corporate / Office Solutions
- Media / Press
- Affiliate Opportunity
- Other

Then collect optional company name and company website plus a required opportunity-description field.

Continue to the Property Profile only when the inquiry involves a property, location, or solution design.

Route to `info@luxsync.net`.

## 9. Shared LuxSync Property Profile

Use the same normalized Property Profile concepts as the Intelligent Living Concierge.

### Property Type

Field ID: `property_type`

Options:

- Private Residence
- Short-Term Rental
- Business / Commercial Property
- Other

### Approximate Square Footage

Field IDs:

- `square_feet_exact` — optional numeric entry
- `square_feet_band` — optional range selector

Ranges:

- Under 1,000 sq. ft.
- 1,000–1,999 sq. ft.
- 2,000–2,999 sq. ft.
- 3,000–4,999 sq. ft.
- 5,000+ sq. ft.
- Not Sure

An estimate is always acceptable.

### Private Residence

Reveal residence type:

- Single-Family Home
- Apartment
- Condominium
- Townhome
- Vacation Home
- New Construction
- Other

### Short-Term Rental

Reveal:

- STR property type
- Number of rental units
- Booking platform: Airbnb / Vrbo / Both or Multiple / Direct Booking / Other / Not Yet Listed
- Remote-management status
- Desired automation areas

Desired automation may include guest entry, smart locks, lighting, climate, energy, noise awareness, water/leak awareness, occupancy awareness, turnover, property monitoring, guest experience, and Other.

### Business / Commercial

Reveal business type, square footage, and number of locations.

Business types may include office, retail, hospitality, professional services, medical/healthcare office, property management, multi-family, restaurant, studio, and Other.

### Other

Reveal a short description plus square footage.

## 10. Project / Solution Details

For product, consultation, or property-related inquiries, ask:

### What are you hoping to accomplish?

Allow multiple selections:

- Improve Convenience
- Improve Property Awareness
- Reduce Energy Usage
- Automate Lighting
- Automate Climate
- Improve Accessibility / Ease of Use
- Create Smart Routines
- Upgrade Existing Smart Devices
- Manage a Property Remotely
- Improve Guest Experience
- Build a New Smart Home
- Simplify an Existing Smart Home
- Improve Entertainment & Ambience
- Other

Then ask whether the visitor currently uses smart-home technology.

If Yes or A Few Devices, allow selection of Samsung SmartThings, Amazon Alexa, Google Home, Apple Home, Ring, Philips Hue, Lutron, Ecobee, Nest, Matter devices, or Other.

## 11. Contact Information

Collect:

- First Name — required
- Last Name — required
- Email Address — required
- Phone Number — optional
- Preferred Contact Method — Email / Phone
- City — required for consultation/property inquiries
- State — required for consultation/property inquiries

Do not require a full street address for the first inquiry.

## 12. Final Details

Optional large text field:

### Anything else we should know?

Helper text: **Tell us anything that will help us better understand your question, project, or support issue.**

## 13. Privacy and Marketing Consent

Required privacy acknowledgment:

**I understand that LuxSync may use the information I provide to respond to this inquiry in accordance with the LuxSync Privacy Policy.**

Marketing must be separate and optional:

**I'd like to receive occasional LuxSync product news, intelligent-living tips, and updates.**

Do not bundle marketing consent into form submission.

## 14. Dynamic Submit Labels

- Support → **Send Support Request**
- Product Information → **Request Information**
- Consultation → **Request Consultation**
- General Question → **Send Question**
- Business / Partnership → **Send Business Inquiry**
- Other → **Send Message**

## 15. Routing and Subject Lines

Support → `support@luxsync.net`

All other paths → `info@luxsync.net`

Automatically include intent and topic in the subject line, for example:

- `LuxSync Support Request — SmartThings Connection`
- `LuxSync Consultation Request — Short-Term Rental`
- `LuxSync Product Inquiry — Smart Lighting & Ambience`

## 16. Blueprint Integration

When a visitor comes from **My LuxSync Blueprint**, preserve and prefill, where appropriate:

- Blueprint ID
- Property type
- Approximate square footage
- Existing ecosystem
- Customer priorities
- Recommended experiences
- Compatibility-review flags
- Implementation preference

The customer should not need to re-enter information already supplied during the active Concierge journey.

## 17. Form UX Requirements

- Reveal approximately 3–6 fields at a time.
- Prefer selection cards for major choices.
- Preserve previous answers when navigating backward.
- Validate required fields and email format.
- Accept numeric square footage but always provide Not Sure.
- Use explicit labels, not placeholder-only fields.
- Be fully keyboard accessible.
- Expose validation errors programmatically.
- Honor reduced-motion preferences.
- Use low-friction spam protection.
- Do not collect more information than the selected path requires.

## 18. Visual Direction

Use LuxSync Production Raster v5 and Plush Drift tactile illumination.

The experience should feel calm, spacious, premium, and intelligent. Use Slate Navy / Dark Suede surfaces, Pale Driftwood copy, Dusty Steel interaction accents, and restrained Champagne Rose Gold Metallic detail.

Do not make the form resemble a survey dashboard or support-ticket bureaucracy.

## 19. Confirmation State

Heading: **Thank You**

Message: **Your message has been received. A LuxSync team member will review your request and respond using the contact information you provided.**

Do not promise an unapproved response-time SLA.

## Production Visual Assignment

Use the exact LuxSync orb plus live adaptive intent cards and forms. Support hours, response times and service promises must remain live copy only when explicitly approved. Do not bake contact information into imagery. See `website/asset-map.md`.

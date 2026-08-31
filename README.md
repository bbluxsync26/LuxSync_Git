<div align="center">

<img src="brand/assets/01-brand/luxsync-horizontal-lockup.png" alt="LuxSync" width="620" />

# LuxSync LLC

### Smart Living. Elevated.

**Where Luxury Lives Intelligently**

[![Brand](https://img.shields.io/badge/LuxSync-v3-0D1526?style=for-the-badge&labelColor=172036)](brand/README.md)
[![Design DNA](https://img.shields.io/badge/Design_DNA-Plush_Drift-967878?style=for-the-badge&labelColor=172036)](brand/brand-architecture.md)
[![Typography](https://img.shields.io/badge/Type-Manrope_%2B_Inter-D0BEB0?style=for-the-badge&labelColor=172036)](brand/typography.md)
[![Commerce](https://img.shields.io/badge/Commerce-GoDaddy_Commerce_Plus-7B96B2?style=for-the-badge&labelColor=172036)](docs/decisions/DEC-004-commerce-plus-and-airo-role.md)

**Curated smart-home commerce · Intelligent automation · Premium customer experience**

</div>

---

> ### ✦ The LuxSync Idea
> Premium technology should feel integrated into the home, not imposed on it. LuxSync curates smart-home products, bundles, and guidance around compatibility, simplicity, design, and intelligent living.
>
> The experience should feel like **premium interior architecture with intelligent technology quietly underneath it**.

---

## ◇ Repository at a Glance

| Surface | Purpose | Enter |
|---|---|---|
| **Strategy** | Business model, launch, finance, roadmap, decisions | [`docs/`](docs/) |
| **Brand** | LuxSync v3, Plush Drift DNA, palette, type, voice, assets | [`brand/`](brand/) |
| **Content** | Approved website copy, FAQs, About, guides | [`content/`](content/) |
| **Prompts** | Airo build prompts and reusable AI workflows | [`prompts/`](prompts/) |
| **Website** | IA, page blueprints, design system, source placeholder | [`website/`](website/) |

**Repository source of truth:** [`docs/master-catalog.md`](docs/master-catalog.md)

---

## ✦ Brand Architecture

<table>
<tr>
<td width="50%" valign="top">

### Plush Drift

The enduring **design DNA** beneath LuxSync.

- Layered dark surfaces
- Soft concealed backlighting
- Tactile press feedback
- Warm/cool balance
- Restrained metallic polish
- Calm architectural motion

**Governing reference:**  
[`brand/brand-architecture.md`](brand/brand-architecture.md)

</td>
<td width="50%" valign="top">

### LuxSync v3

The current **visual implementation** of that DNA.

- Active asset root: `brand/assets-v3/`
- Manrope + Inter
- Approved seven-color palette
- Protected exact logo artwork
- Ecommerce-first component system
- Intelligent Calm voice

**Governing reference:**  
[`brand/README.md`](brand/README.md)

</td>
</tr>
</table>

### Tactile Illumination

Plush Drift controls are designed to feel like **backlit physical controls** rather than flat software rectangles.

| State | Visual behavior |
|---|---|
| **Rest** | Dark Slate Navy / Dark Suede surface with faint concealed underlight |
| **Hover** | Underlight brightens and widens slightly |
| **Focus** | Accessible focus indicator plus restrained illumination |
| **Press** | Surface compresses inward ~1–2 px, shadow tightens, concealed light becomes more visible |
| **Release** | Smooth restrained return with reduced-motion support |

**Preferred underlight:** Dusty Steel `#7B96B2`  
**Warm alternatives:** Antique Rose Taupe `#967878`, Pale Driftwood `#D0BEB0`  
**Premium reflected detail:** Champagne Rose Gold Metallic `#D6B0A0` anchor

> **Not neon. Not arcade glow. Not generic SaaS.**  
> The light should feel concealed inside a premium architectural control.

---

## ◈ Approved Visual Foundation

### Palette

| Role | Color | Hex |
|---|---|---|
| Primary canvas | **Slate Navy** | `#0D1526` |
| Elevated surface | **Dark Suede** | `#172036` |
| Primary light / warm surface | **Pale Driftwood** | `#D0BEB0` |
| Secondary neutral | **Warm Taupe Mauve** | `#9E8B85` |
| Warm accent | **Antique Rose Taupe** | `#967878` |
| Intelligent-light accent | **Dusty Steel** | `#7B96B2` |
| Premium metallic | **Champagne Rose Gold Metallic** | `#D6B0A0` anchor |

Champagne Rose Gold Metallic may use the approved dimensional gradient:

`#FFF2EA → #EAC8B9 → #D6B0A0 → #9C675C → #F2D6C8 → #7D4E49`

The gradient stops create the metallic finish. They are **not additional flat brand colors**.

### Typography

| Role | Typeface | Weights |
|---|---|---|
| Headings, display, navigation, buttons, graphic UI | **Manrope** | 500 / 600 |
| Body, product copy, forms, supporting UI | **Inter** | 400 / 500 |

Protected logo lettering is artwork and is not recreated with live type.

---

## ◇ What LuxSync Is Building

LuxSync is a **retail-first luxury smart-home automation and commerce company** built around a curated, zero-inventory operating model.

The launch experience centers on:

- carefully selected SmartThings-compatible products;
- curated lifestyle and property bundles;
- guided product discovery;
- compatibility-first recommendations;
- thoughtful automation guidance;
- premium customer support and education.

### Launch Audiences

| Audience | Desired outcome |
|---|---|
| **Short-Term Rental Operators** | Remote property control, guest experience, efficiency |
| **Seniors & Caregivers** | Independent-living support and home awareness |
| **Smart Office & Property Managers** | Centralized oversight and multi-space control |
| **Intentional Parents** | Sleep, comfort, routines, and safety-focused automation |
| **Busy Professionals** | Elegant convenience without unnecessary complexity |

---

## ✦ Curated Commerce

### Bundle Concepts

- **STR Property Automation**
- **Guest Welcome & Keyless Entry**
- **Smart Sleep Nursery**
- **Senior Independent Safety**

### Product Families

Smart hubs · locks · lighting · shades · speakers · appliances · security · water management · entertainment

Public prices, stock, availability, shipping promises, and recurring-service pricing must come from validated commerce data. Internal planning assumptions are not storefront claims.

---

## ◈ Technology Philosophy

| Principle | Meaning |
|---|---|
| **Compatibility before customization** | Prefer proven interoperability over unnecessary complexity |
| **Simplicity before complexity** | Make intelligent living approachable |
| **Reliability before novelty** | Favor dependable outcomes |
| **Customer experience before technology** | Technology serves the lifestyle, not the reverse |

**Launch compatibility standard:** Samsung SmartThings  
**Production commerce system of record:** GoDaddy Commerce Plus

Airo AI Builder is used for staging, design exploration, and reviewed generation within the repository-defined architecture. It does not silently redefine the production commerce system.

---

## ✦ Website Direction

```text
Home | Shop | Solutions | Guides | About | Support
```

Commerce utilities:

```text
Search | Account | Cart
```

The launch storefront should feel:

- premium, warm, architectural, and calm;
- mobile-first and accessible;
- curated rather than crowded;
- tactile rather than flat;
- intelligently illuminated rather than neon;
- luxurious without becoming ornamental or difficult to use.

**Website design system:** [`website/styles/design-system.md`](website/styles/design-system.md)  
**Website architecture:** [`docs/architecture/website-information-architecture.md`](docs/architecture/website-information-architecture.md)  
**Airo master prompt:** [`prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md`](prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md)

---

## ◇ Intelligent Calm

LuxSync communicates with confidence without shouting.

**Warm · Thoughtful · Refined · Human · Unhurried · Professional**

Avoid hype, fear-based selling, excessive urgency, jargon, technical showing-off, and unsupported superlatives.

**Voice reference:** [`brand/voice-and-tone.md`](brand/voice-and-tone.md)

---

## ✦ Leadership

<table>
<tr>
<td width="50%" valign="top">

### Bridgette Beardsley
**Co-Founder & Chief Technology and Strategy Officer**

Technology strategy, operating architecture, digital commerce, governance, and intelligent customer experience.

[Approved biography →](docs/leadership/bridgette-beardsley.md)

</td>
<td width="50%" valign="top">

### Sheldon Bardol
**Co-Founder & Chief Customer and Operations Officer**

Customer experience, operations, product curation, supplier relationships, and commercial execution.

[Approved biography →](docs/leadership/sheldon-bardol.md)

</td>
</tr>
</table>

---

## ◈ Operating Source of Truth

```text
LuxSync_Git/
├── docs/                 Strategy, decisions, runbooks, financial and launch planning
├── brand/                Brand architecture, visual standards, identity and assets
├── content/              Approved website and customer-facing copy
├── prompts/              Reusable AI and generation prompts
└── website/              IA, page blueprints, design system and future source code
```

Key governing references:

- [`docs/master-catalog.md`](docs/master-catalog.md) — repository index and precedence
- [`brand/brand-architecture.md`](brand/brand-architecture.md) — Plush Drift design DNA
- [`brand/README.md`](brand/README.md) — LuxSync v3 visual system
- [`brand/colors.md`](brand/colors.md) — approved palette and metallic treatment
- [`brand/typography.md`](brand/typography.md) — Manrope + Inter
- [`website/styles/design-system.md`](website/styles/design-system.md) — interaction and UI implementation

---

## ✦ Mission

**To simplify luxury smart living through trusted curation, intelligent automation, and exceptional customer experiences.**

### Long-Term Vision

LuxSync will grow from curated smart-home commerce into a broader intelligent-living brand spanning:

**Commerce · Automation · Design · Education · Premium lifestyle experiences**

Future capabilities such as SmartThings automation templates and LuxSync Grid remain roadmap items until explicitly released.

---

<div align="center">

### LuxSync LLC

**Where Luxury Lives Intelligently**

*Plush Drift design DNA · LuxSync v3 visual system · Manrope + Inter*

</div>

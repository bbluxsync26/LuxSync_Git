# Typography

## Intelligent Calm Voice Through Type

The LuxSync typography system is designed to reflect our brand personality: warm, refined, human, and effortless.

---

## Headlines & Display Text

**Font: Manrope**

### Characteristics

- Soft, rounded geometric forms
- Premium without feeling corporate
- Modern and highly readable
- Strong visual hierarchy without harshness
- Excellent for brand presence and emphasis

### Recommended Weights

- **500** (Regular) — Subheadings, feature headings
- **600** (Semibold) — Primary headings, emphasizing key messages

**Avoid**: Heavy bold weights (700+) unless required for accessibility or very specific callouts.

### Usage

- Page titles and section headings
- Feature headlines
- Call-to-action text
- Brand storytelling
- Promotional messaging

---

## Body Copy & Paragraph Text

**Font: Inter**

### Characteristics

- Comfortable for extended reading
- Exceptional screen legibility
- Clean and unobtrusive
- Optimized for modern digital interfaces
- Friendly without being casual
- Professional yet approachable

### Recommended Weights

- **400** (Regular) — Standard body text, long-form content
- **500** (Medium) — Emphasis within body copy, labels, helper text

### Usage

- Article text and long-form content
- Description copy
- Product descriptions
- Customer testimonials
- Educational content
- Email body text

---

## UI Elements & Controls

**Font: Inter**

### Recommended Weight

- **500** (Medium) — All interactive elements

### Button Styling

- Sentence case preferred (not ALL CAPS)
- Letter spacing: `0.02em`
- Pair with Warm Taupe Mauve (#9E8B85) or Dusty Steel (#7B96B2)

### Usage

- Button labels
- Navigation links
- Form labels and placeholders
- Badges and tags
- Micro-copy and helper text
- Interface controls

---

## Font Stacks (Fallback Order)

### Headlines
```css
font-family: "Manrope", system-ui, -apple-system, sans-serif;
```

### Body & UI
```css
font-family: "Inter", system-ui, -apple-system, sans-serif;
```

---

## Typography Goals

**Embody These Qualities**

- Warm — Genuine and approachable
- Comfortable — Easy to read, never harsh
- Refined — Premium quality in every detail
- Human — Conversational, not robotic
- Modern — Clean, current aesthetic
- Effortless — Simple, intuitive experience

**Avoid These Qualities**

- Aggressive — No forceful or pushy messaging
- Corporate — Avoid stiff, formal tone
- Technical — No jargon or intimidating language
- Cold — Never sterile or impersonal

---

## Practical Examples

### Do This

**Headline (Manrope 600):** "Create Smarter, Safer Spaces"

**Body (Inter 400):** "Thoughtfully selected smart-home solutions designed to enhance your everyday living experience."

**Button (Inter 500):** "Explore Collections"

### Don't Do This

**Headline (Manrope 700):** "BUY NOW OR MISS OUT" — Too aggressive and heavy

**Body (Serif font):** "Lorem ipsum dolor sit amet..." — Wrong typeface for digital

**Button (Century Gothic):** "CLICK HERE NOW" — Wrong font and tone

---

## Web Integration

### Google Fonts Import

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Manrope:wght@500;600&display=swap" rel="stylesheet">
```

### CSS Variables (Recommended)

```css
:root {
  --font-headline: "Manrope", system-ui, sans-serif;
  --font-body: "Inter", system-ui, sans-serif;
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-headline);
  font-weight: var(--font-weight-semibold);
}

body, p, span {
  font-family: var(--font-body);
  font-weight: var(--font-weight-regular);
}

button, label {
  font-family: var(--font-body);
  font-weight: var(--font-weight-medium);
}
```

---

## Design Principle

> Where warmth meets intelligence.
>
> Where luxury feels like home.

Every typographic choice should support this philosophy — elegant yet approachable, sophisticated yet human.

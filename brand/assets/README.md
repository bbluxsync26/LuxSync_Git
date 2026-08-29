# LuxSync Brand Asset Library

**Plush Drift v2.1 — Complete Web Graphics Collection**

> Where warmth meets intelligence. Where luxury feels like home.

---

## Overview

Complete asset library for LuxSync branding and web presence:

- **96 individual web graphics** across 11 organized categories
- **Multiple formats**: SVG (vector), PNG (transparent/opaque), WebP (optimized)
- **Color system**: Plush Drift v2.1 palette integration
- **Primary use cases**: Logos, icons, banners, cards, illustrations, components

---

## Color Palette

| Role | Color | Hex |
|--------|--------|--------|
| Primary Background | Slate Navy | `#0D1526` |
| Card Surface | Dark Suede | `#172036` |
| Primary Text | Pale Driftwood | `#D0BEB0` |
| Secondary Text | Warm Taupe Mauve | `#9E8B85` |
| Tertiary Accent | Antique Rose Taupe | `#967878` |
| Primary Accent | Dusty Steel | `#7B96B2` |

---

## Asset Categories

### 1. Brand Marks
Primary logos, wordmarks, and signature brand identifiers.

**Formats**: SVG, PNG (transparent), WebP  
**Use**: Website header, social profiles, official documentation  
**Location**: `./brand-marks/`

---

### 2. Brand Icons
Decorative and symbolic icons representing LuxSync brand concepts.

**Formats**: SVG, PNG (transparent), WebP  
**Use**: Feature callouts, brand storytelling, visual hierarchy  
**Location**: `./brand-icons/`

---

### 3. Website Icons
Functional UI icons for navigation, actions, and interface elements.

**Formats**: SVG, PNG (transparent), WebP  
**Use**: Buttons, navigation, feature icons, interface controls  
**Location**: `./website-icons/`

---

### 4. Social Icons
Platform-specific and social media icons.

**Formats**: SVG, PNG (transparent), WebP  
**Use**: Social links, share buttons, platform integration  
**Location**: `./social-icons/`

---

### 5. Palette & Texture
Color swatches, texture samples, and visual references.

**Formats**: SVG, PNG, WebP  
**Use**: Brand guidelines, design reference, material samples  
**Location**: `./palette-texture/`

---

### 6. Gradients
Gradient fills, background patterns, and color transitions.

**Formats**: SVG, PNG, WebP  
**Use**: Hero sections, backgrounds, decorative elements  
**Location**: `./gradients/`

---

### 7. Components
Reusable UI components and design modules.

**Formats**: SVG, PNG (transparent), WebP  
**Use**: Button styles, form elements, component library  
**Location**: `./components/`

---

### 8. Cards
Card designs, containers, and layout modules.

**Formats**: SVG, PNG, WebP  
**Use**: Product cards, feature cards, content blocks  
**Location**: `./cards/`

---

### 9. Illustrations
Custom illustrations, diagrams, and visual narratives.

**Formats**: SVG, PNG (transparent), WebP  
**Use**: Hero images, storytelling, feature illustrations  
**Location**: `./illustrations/`

---

### 10. Category Cards
Pre-designed cards for product categories and navigation.

**Formats**: SVG, PNG, WebP  
**Use**: Product category pages, navigation tiles, feature cards  
**Location**: `./category-cards/`

---

### 11. Website Banners
Full-width banners and promotional graphics.

**Formats**: SVG, PNG, WebP  
**Use**: Hero sections, campaign banners, seasonal promotions  
**Location**: `./website-banners/`

---

## Format Guidance

### SVG (Preferred)
- **Use for**: Logos, icons, controls, badges, cards, and gradients
- **Advantage**: Vector-based, scales infinitely, smallest file size for simple graphics
- **Web use**: Direct embedding in HTML or CSS

### PNG
- **Use when**: CMS requires raster upload or transparency fallback
- **Advantage**: Universal compatibility, lossless quality, transparency support
- **Web use**: Standard `<img>` tags, email, fallback format

### WebP
- **Use for**: Banners, cards, textures, and illustrations where file size matters
- **Advantage**: Optimized compression, smaller than PNG/JPG
- **Web use**: Modern browsers with PNG fallback

---

## Manifest & Metadata

Complete asset metadata available in [`asset-manifest.json`](./asset-manifest.json):

- Asset descriptions
- Category organization
- Format specifications
- Dimensions (width/height)
- Transparency information
- File paths

---

## Typography Reference

> **Current Standard:** Headlines use Manrope (weights 500, 600); Body Copy and UI use Inter (weights 400, 500).
> The asset catalog was originally built with different fonts, but the current LuxSync brand standard is Manrope and Inter.

| Role | Font | Fallback |
|--------|--------|---------|
| Display/Headings | Manrope | system-ui, -apple-system, sans-serif |
| Body Copy | Inter | system-ui, -apple-system, sans-serif |

---

## Usage Guidelines

### For Web Projects
1. Choose SVG for logos and icons
2. Use WebP for banners and large graphics
3. Provide PNG fallbacks for older browsers
4. Reference color hex codes for design consistency

### For Documentation & READMEs
1. Reference SVG files directly in markdown
2. Use relative paths: `./brand-marks/asset-name.svg`
3. Include alt text for accessibility

### For Design Tools
1. Import SVG files into Figma, Illustrator, or similar
2. Maintain Plush Drift v2.1 color palette
3. Update asset-manifest.json with any modifications

---

## File Structure

```
brand/assets/
├── README.md                      (this file)
├── asset-manifest.json            (metadata index)
├── brand-marks/                   (11 assets)
├── brand-icons/                   (12 assets)
├── website-icons/                 (8 assets)
├── social-icons/                  (7 assets)
├── palette-texture/               (6 assets)
├── gradients/                     (9 assets)
├── components/                    (8 assets)
├── cards/                         (7 assets)
├── illustrations/                 (10 assets)
├── category-cards/                (11 assets)
└── website-banners/               (7 assets)
```

---

## Asset Management

### Adding New Assets
1. Place files in appropriate category folder
2. Update [`asset-manifest.json`](./asset-manifest.json)
3. Commit changes with clear messages
4. Update this README if adding new categories

### Updating Existing Assets
1. Replace files while maintaining names
2. Update asset-manifest.json metadata if needed
3. Commit with changelog message

---

## Design Principles

All assets follow LuxSync brand principles:

- **Intelligent Calm** — Professional yet approachable
- **Warm & Premium** — Luxury without coldness
- **Functional Beauty** — Form follows function
- **Consistent Quality** — Every detail matters

---

## Support

For questions about specific assets or usage:
- Check [`asset-manifest.json`](./asset-manifest.json) for detailed metadata
- Review category README files if available
- Refer to main brand guidelines in parent directory

---

**Version**: Plush Drift v2.1  
**Last Updated**: August 29, 2026  
**Total Assets**: 96 graphics  
**Categories**: 11  
**Formats**: SVG, PNG, WebP

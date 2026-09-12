# LuxSync catalog and shopping features

Catalog source: LuxSync Product Catalog - Distributor Sourcing.xlsx. Imported 38 products and 32 bundles. Only public catalog fields are shipped. All prices are null; no supplier costs, planning prices, margins, sourcing notes, or stock promises are published.

Bundle contents follow explicit component-SKU columns, with duplicate references aggregated into quantities. Higher-tier description conflicts require future merchandising review; displayed contents are marked preliminary.

Wishlists use authenticated saved_items records with owner-scoped reads and updates, custom titles, SKU validation, and optimistic version checks. Guest carts use opaque HttpOnly cookies and server storage. No payment or checkout is enabled.

## Category imagery

Generated with the built-in imagegen tool. Existing Plush Drift assets are reused for other collections. Products and bundle contents use authored two-tone inline device icons, without product photos.

### outdoor-living

Assets: src/heroes/category-outdoor-living-720.webp and src/heroes/category-outdoor-living-1600.webp.

Prompt: Use case: photorealistic-natural. Asset: wide 16:9 category hero photograph for the LuxSync smart living website. An elegant covered outdoor terrace at blue hour, comfortable taupe linen seating, pale travertine, walnut soffits, warm concealed amber lighting under steps and roof edges, softly illuminated planting, a calm garden beyond. Emphasize a lived-in connected outdoor space without any device close-up. Plush Drift art direction: tactile calm luxury, soft driftwood taupe, deep slate navy, restrained champagne metal accents, gentle amber warmth, believable architectural photography, detailed natural materials, balanced wide composition that crops well to 3:2 tiles, no people, no text, no logos, no watermark, no neon, no lens flares, no exaggerated glow. This is category lifestyle imagery only.

### water-protection

Assets: src/heroes/category-water-protection-720.webp and src/heroes/category-water-protection-1600.webp.

Prompt: Use case: photorealistic-natural. Asset: wide 16:9 category hero photograph for the LuxSync smart living website. An elegant residential utility and laundry room, pale stone sink and countertop, warm walnut cabinetry, discreet brushed steel plumbing beneath an open sink cabinet, orderly towel storage, a dry spotless stone floor, restrained concealed amber undercabinet lighting. The environment communicates care for water and the home, not a product advertisement. Plush Drift art direction: tactile calm luxury, soft driftwood taupe, deep slate navy, restrained champagne metal accents, gentle amber warmth, believable architectural photography, detailed natural materials, balanced wide composition that crops well to 3:2 tiles, no people, no text, no logos, no watermark, no neon, no lens flares, no exaggerated glow. This is category lifestyle imagery only.

### connectivity

Assets: src/heroes/category-connectivity-720.webp and src/heroes/category-connectivity-1600.webp.

Prompt: Use case: photorealistic-natural. Asset: wide 16:9 category hero photograph for the LuxSync smart living website. An elegant quiet smart-home study with warm walnut joinery and a discreet open technology cabinet built into the wall, neatly organized dark network equipment and cables, a plush taupe chair, natural travertine desk, window onto dusk trees, concealed amber cabinet illumination. Network infrastructure is integrated into the architecture, no device close-up. Plush Drift art direction: tactile calm luxury, soft driftwood taupe, deep slate navy, restrained champagne metal accents, gentle amber warmth, believable architectural photography, detailed natural materials, balanced wide composition that crops well to 3:2 tiles, no people, no text, no logos, no watermark, no neon, no lens flares, no exaggerated glow. This is category lifestyle imagery only.


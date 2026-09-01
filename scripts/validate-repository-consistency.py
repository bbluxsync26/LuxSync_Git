#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRAND_SYSTEM = 'LuxSync Production Raster v5'
SLOGAN = 'Where Luxury Lives Intelligently'
PRIMARY_CTA = 'Find My LuxSync Solution'
SECONDARY_CTA = 'Shop Smart Home'
BRIDGETTE_TITLE = 'Co-Founder & Chief Technology and Strategy Officer'
SHELDON_TITLE = 'Co-Founder & Chief Customer and Operations Officer'
CONCIERGE = "LuxSync Intelligent Living Concierge"
BLUEPRINT = "My LuxSync Blueprint"
SAFE_ASSETS = {
    "brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png",
    "brand/assets/01-logos/LuxSync_Logo_Horizontal_Final.png",
    "brand/assets/01-logos/LuxSync_Logo_Orb.png",
}
RETIRED_HERO = "Smart Living" + ". " + "Elevated" + "."
LEGACY_TERMS = [
    "LuxSync " + "v3",
    "Brand System " + "4.0",
    "assets" + "-v3",
    "migrate-brand-" + "v3.py",
    "validate-brand-" + "v3.py",
    "RB-007-Brand-Asset-" + "Raster-Regeneration.md",
    "RB-008-Luxury-Orbit-" + "Brand-Asset-Generation.md",
]
REQUIRED_FILES = [
    "README.md",
    "brand/README.md",
    "brand/colors.md",
    "brand/typography.md",
    "brand/voice-and-tone.md",
    "brand/assets/README.md",
    "brand/assets/asset-manifest.json",
    "docs/production-source-of-truth.md",
    "docs/production-asset-library.md",
    "docs/master-catalog.md",
    "docs/project-runbook.md",
    "docs/value-proposition.md",
    "docs/architecture/website-information-architecture.md",
    "docs/architecture/intelligent-living-concierge.md",
    "content/homepage.md",
    "content/about.md",
    "content/faqs.md",
    "content/contact.md",
    "content/product-catalog.md",
    "content/guides/roi/README.md",
    "website/implementation-manifest.json",
    "website/navigation.md",
    "website/asset-map.md",
    "website/styles/design-system.md",
    "website/pages/home.md",
    "website/pages/concierge.md",
    "website/pages/my-luxsync-blueprint.md",
    "website/pages/solutions.md",
    "website/pages/solutions/commercial-offices.md",
    "website/pages/solutions/senior-living.md",
    "website/pages/solutions/short-term-rentals.md",
    "website/pages/solutions/residential.md",
    "website/pages/solutions/aging-in-place.md",
    "website/pages/shop.md",
    "website/pages/guides.md",
    "website/pages/about.md",
    "website/pages/faqs.md",
    "website/pages/contact.md",
    "website/src/concierge/luxsync-concierge-engine.v1.json",
    "scripts/validate-production-brand.py",
]
ROI_FILES = [
    "commercial-offices.md", "nursing-homes.md", "senior-living-communities.md",
    "str-owners.md", "str-operators.md", "str-managers.md",
    "residential-homeowners.md", "residential-busy-professionals.md",
    "residential-intentional-parents.md", "residential-seniors-caregivers.md",
]
errors = []

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8", errors="replace")

def require(rel, token):
    if token not in read(rel): errors.append(f"{rel}: missing required token {token!r}")

for rel in REQUIRED_FILES:
    if not (ROOT / rel).exists(): errors.append(f"missing required file: {rel}")
if errors:
    print("LuxSync repository validation FAILED:")
    for e in errors: print("-", e)
    raise SystemExit(1)

# Active text must not preserve retired branding or retired generation paths.
text_suffixes = {".md", ".txt", ".json", ".yml", ".yaml", ".py", ".js", ".mjs", ".css", ".html"}
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in text_suffixes: continue
    if any(part in {".git", "node_modules"} for part in path.parts): continue
    text = path.read_text(encoding="utf-8", errors="replace")
    if RETIRED_HERO in text: errors.append(f"{path.relative_to(ROOT)}: retired hero phrase remains")
    for term in LEGACY_TERMS:
        if term in text: errors.append(f"{path.relative_to(ROOT)}: retired source-of-truth term remains: {term}")

for rel in (
    "docs/production-source-of-truth.md", "brand/README.md", "website/styles/design-system.md",
    "website/pages/home.md", "website/navigation.md", "website/asset-map.md",
    "prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md",
):
    for token in (BRAND_SYSTEM, SLOGAN): require(rel, token)

for rel in ("docs/leadership/bridgette-beardsley.md", "website/pages/home.md", "website/pages/about.md", "docs/master-catalog.md"):
    require(rel, BRIDGETTE_TITLE)
for rel in ("docs/leadership/sheldon-bardol.md", "website/pages/home.md", "website/pages/about.md", "docs/master-catalog.md"):
    require(rel, SHELDON_TITLE)

for rel in ("website/pages/home.md", "website/pages/concierge.md", "docs/architecture/intelligent-living-concierge.md", "docs/production-source-of-truth.md"):
    for token in (PRIMARY_CTA, CONCIERGE, BLUEPRINT): require(rel, token)

for token in ("Support", "Product Information", "Consultation", "General Question", "Business / Partnership", "property_type", "square_feet_exact", "square_feet_band"):
    require("website/pages/contact.md", token)
for token in ("support@luxsync.net", "info@luxsync.net"):
    require("content/contact.md", token)
    require("website/pages/contact.md", token)

for filename in ROI_FILES:
    rel = f"content/guides/roi/{filename}"
    require(rel, SLOGAN)
    require(rel, "ROI")
for token in ("Commercial Offices", "Nursing Homes", "Senior Living Communities", "STR Owners", "STR Operators", "STR Managers", "Seniors, Caregivers"):
    require("content/guides/roi/README.md", token)
    require("website/pages/guides.md", token)

for token in ("Physical Product Families", "Curated Bundle", "LuxSync Experiences", "Validated Live Product", "Solution Concept"):
    require("content/product-catalog.md", token)

# Route manifest must be complete, internally resolvable, and publication-safe.
impl = json.loads(read("website/implementation-manifest.json"))
if impl.get("brand_system") != BRAND_SYSTEM: errors.append("implementation manifest brand_system mismatch")
if impl.get("official_slogan") != SLOGAN: errors.append("implementation manifest slogan mismatch")
required_routes = {
    "/", "/find-my-luxsync-solution", "/my-luxsync-blueprint", "/solutions",
    "/solutions/commercial-offices", "/solutions/senior-living", "/solutions/short-term-rentals",
    "/solutions/residential", "/solutions/aging-in-place", "/shop", "/guides", "/about", "/faqs", "/contact",
}
routes = impl.get("routes", [])
route_names = {r.get("route") for r in routes}
if route_names != required_routes:
    errors.append(f"implementation manifest route set mismatch: {sorted(route_names ^ required_routes)}")
for route in routes:
    for key in ("blueprint", "content_source"):
        rel = route.get(key)
        if not rel or not (ROOT / rel).exists(): errors.append(f"{route.get('route')}: invalid {key} {rel!r}")
    assets = route.get("production_assets", [])
    if not assets: errors.append(f"{route.get('route')}: no production asset assigned")
    for asset in assets:
        if asset not in SAFE_ASSETS: errors.append(f"{route.get('route')}: reference-only asset wired as production: {asset}")
        if not (ROOT / asset).exists(): errors.append(f"{route.get('route')}: missing asset: {asset}")

# Page blueprints may not directly wire reference-only imported slices.
reference_prefixes = tuple(f"brand/assets/{n:02d}-" for n in range(2, 10))
for path in (ROOT / "website/pages").rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    for prefix in reference_prefixes:
        if prefix in text: errors.append(f"{path.relative_to(ROOT)}: reference-only raster path is wired directly")

for token in ("/shop", "/solutions", "/guides", "/about", "/faqs", "/contact", PRIMARY_CTA):
    require("website/navigation.md", token)

engine = json.loads(read("website/src/concierge/luxsync-concierge-engine.v1.json"))
for key in ("meta", "constants", "experience_catalog", "questionnaire", "scoring", "compatibility", "blueprint_schema"):
    if key not in engine: errors.append(f"Concierge engine missing top-level key: {key}")

workflow = read(".github/workflows/validate-repository-consistency.yml")
for token in ("validate-production-brand.py", "validate-repository-consistency.py", "assemble-engine.mjs"):
    if token not in workflow: errors.append(f"CI workflow missing {token}")

if (ROOT / "docs/business-plan.md").exists() and "Pricing status: unresolved" not in read("docs/business-plan.md"):
    errors.append("senior-service pricing must remain explicitly unresolved")

if errors:
    print("LuxSync repository validation FAILED:")
    for error in errors: print("-", error)
    raise SystemExit(1)
print("LuxSync repository validation PASSED")
print(f"Brand system: {BRAND_SYSTEM}")
print(f"Slogan: {SLOGAN}")
print(f"Routes: {len(routes)}")

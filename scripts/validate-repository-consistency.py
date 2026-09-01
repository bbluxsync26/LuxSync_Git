#!/usr/bin/env python3
from __future__ import annotations

import json
import re
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
    "brand/assets/logos/png/luxsync-horizontal-combo.png",
    "brand/assets/logos/png/luxsync-horizontal.png",
    "brand/assets/logos/png/luxsync-orb.png",
}
AUTH_PRODUCTION_ASSETS = {
    "website/assets/auth/login-vip-hero.svg",
    "website/assets/auth/login-vip-hero-mobile.svg",
    "website/assets/auth/member-access-ambient.svg",
    "website/assets/auth/account-welcome-banner.svg",
}
AUTH_REFERENCE_ASSETS = {
    "website/assets/auth/auth-card-reference.svg",
    "website/assets/auth/auth-input-states.svg",
    "website/assets/auth/auth-button-states.svg",
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
    "docs/checklists/CL-002-Account-Access-Review.md",
    "content/homepage.md",
    "content/about.md",
    "content/faqs.md",
    "content/contact.md",
    "content/product-catalog.md",
    "content/guides/roi/README.md",
    "website/implementation-manifest.json",
    "website/account-access-manifest.json",
    "website/navigation.md",
    "website/asset-map.md",
    "website/styles/design-system.md",
    "website/styles/account-access-tokens.css",
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
    "website/pages/account-login.md",
    "website/assets/auth/README.md",
    "website/assets/auth/manifest.json",
    "website/src/concierge/luxsync-concierge-engine.v1.json",
    "site/source-content.mjs",
    "site/src/app.js",
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
for rel in AUTH_PRODUCTION_ASSETS | AUTH_REFERENCE_ASSETS:
    if not (ROOT / rel).exists(): errors.append(f"missing VIP account asset: {rel}")
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

# Markdown HTML image references must be portable and resolve inside the repository.
for path in ROOT.rglob("*.md"):
    if any(part in {".git", "node_modules"} for part in path.parts):
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    for src in re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\']', text, flags=re.IGNORECASE):
        if src.startswith(("http://", "https://", "data:", "/")):
            continue
        if "\\" in src:
            errors.append(f"{path.relative_to(ROOT)}: nonportable backslash in image source: {src}")
            continue
        target = (path.parent / src).resolve()
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: image source escapes repository: {src}")
            continue
        if not target.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken image source: {src}")

# Active roadmap documents must preserve launch/release boundaries.
for token in (
    "gated roadmap, not a public launch commitment",
    "Templates remain unreleased unless",
    "LuxSync Grid remains a roadmap concept",
    "do not promise traditional on-site installation",
):
    require("docs/3-month-cookbook.md", token)
for forbidden in ("Official Launch", "Marketplace Go-Live", "$39/property/month"):
    if forbidden in read("docs/3-month-cookbook.md"):
        errors.append(f"docs/3-month-cookbook.md: roadmap capability is presented as live: {forbidden}")

# Production site must consume governed sources and implement the full Property Profile branches.
for token in ("readGovernedContent", "HOME.supportingCopy", "LEADERSHIP.bridgette", "catalog"):
    require("site/build.mjs", token)
for token in (
    "square_feet_exact", "residence_type", "str_property_type", "rental_units",
    "booking_platform", "remote_management_status", "desired_automation",
    "business_type", "number_of_locations", "property_description",
):
    require("site/src/app.js", token)

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

# VIP account source-of-truth package.
auth = json.loads(read("website/account-access-manifest.json"))
if auth.get("brand_system") != BRAND_SYSTEM:
    errors.append("account-access manifest brand_system mismatch")
if auth.get("primary_route") != "/account/login":
    errors.append("account-access manifest primary_route must be /account/login")
if set(auth.get("approved_logos", {}).values()) != SAFE_ASSETS:
    errors.append("account-access manifest approved logo set mismatch")
platform = auth.get("platform_boundary", {})
if platform.get("commerce_account_authority") != "GoDaddy Commerce Plus":
    errors.append("account-access manifest commerce/account authority mismatch")
if platform.get("custom_credential_backend_approved") is not False:
    errors.append("account-access manifest must not approve a custom credential backend")
if platform.get("social_login_providers_approved") != []:
    errors.append("account-access manifest must not invent social-login providers")
if platform.get("passkey_implementation_approved") is not False:
    errors.append("account-access manifest must not invent passkey support")
if "/account/login" not in auth.get("route_family", []):
    errors.append("account-access manifest route family missing /account/login")
visual = auth.get("visual_assets", {})
if set(visual.get("production_approved", [])) != AUTH_PRODUCTION_ASSETS:
    errors.append("account-access production asset set mismatch")
if set(visual.get("reference_only", [])) != AUTH_REFERENCE_ASSETS:
    errors.append("account-access reference asset set mismatch")
if visual.get("manifest") != "website/assets/auth/manifest.json":
    errors.append("account-access asset manifest path mismatch")

asset_manifest = json.loads(read("website/assets/auth/manifest.json"))
manifest_items = asset_manifest.get("assets", [])
manifest_map = {item.get("path"): item for item in manifest_items}
if set(manifest_map) != AUTH_PRODUCTION_ASSETS | AUTH_REFERENCE_ASSETS:
    errors.append("VIP auth asset manifest file set mismatch")
for rel in AUTH_PRODUCTION_ASSETS:
    item = manifest_map.get(rel, {})
    if item.get("publication_status") != "production-approved":
        errors.append(f"{rel}: production ambient asset must be production-approved")
    if item.get("text_free") is not True:
        errors.append(f"{rel}: production ambient asset must be text-free")
    svg = read(rel)
    if "<text" in svg:
        errors.append(f"{rel}: production ambient asset contains live-looking text")
for rel in AUTH_REFERENCE_ASSETS:
    item = manifest_map.get(rel, {})
    if item.get("publication_status") != "reference-only":
        errors.append(f"{rel}: auth design reference must remain reference-only")
    svg = read(rel)
    for family in ("Manrope", "Inter"):
        if family not in svg:
            errors.append(f"{rel}: auth design reference missing {family}")

if (ROOT / "brand/assets/10-auth").exists():
    errors.append("brand/assets/10-auth must not exist; auth SVGs belong under website/assets/auth")

for rel in (
    "website/pages/account-login.md",
    "website/account-access-manifest.json",
    "website/asset-map.md",
    "website/navigation.md",
    "docs/production-source-of-truth.md",
    "docs/master-catalog.md",
    "docs/checklists/CL-002-Account-Access-Review.md",
):
    if "brand/assets/10-auth" in read(rel):
        errors.append(f"{rel}: obsolete auth asset path remains")

for token in (
    "Welcome Back", "VIP", "Plush Drift", "GoDaddy Commerce Plus",
    "luxsync-horizontal-combo.png", "luxsync-horizontal.png", "luxsync-orb.png",
    "website/assets/auth/manifest.json",
):
    require("website/pages/account-login.md", token)
for token in (
    "--auth-canvas", "--auth-surface", "--auth-underlight", "--auth-metal",
    "translateY(2px)", "prefers-reduced-motion", "Manrope", "Inter",
):
    require("website/styles/account-access-tokens.css", token)

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
print(f"VIP auth assets: {len(AUTH_PRODUCTION_ASSETS)} production + {len(AUTH_REFERENCE_ASSETS)} reference")

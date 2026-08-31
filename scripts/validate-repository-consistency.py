#!/usr/bin/env python3
"""Validate current LuxSync source-of-truth contracts across docs, prompts, website and Concierge."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OFFICIAL_SLOGAN = "Where Luxury Lives Intelligently"
PRIMARY_CTA = "Find My LuxSync Solution"
SECONDARY_CTA = "Shop Smart Home"
CONCIERGE_NAME = "LuxSync Intelligent Living Concierge"
BLUEPRINT_NAME = "My LuxSync Blueprint"
SUPPORT_EMAIL = "support@luxsync.net"
INFO_EMAIL = "info@luxsync.net"
BRIDGETTE_TITLE = "Co-Founder & Chief Technology and Strategy Officer"
SHELDON_TITLE = "Co-Founder & Chief Customer and Operations Officer"

# Build the retired phrase without preserving it as a searchable repository literal.
RETIRED_HERO = "Smart Living" + ". " + "Elevated" + "."

REQUIRED_FILES = [
    "README.md",
    "docs/master-catalog.md",
    "docs/project-runbook.md",
    "docs/value-proposition.md",
    "docs/architecture/website-information-architecture.md",
    "docs/architecture/intelligent-living-concierge.md",
    "docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md",
    "docs/runbooks/RB-009-Repository-Consistency-Validation.md",
    "docs/checklists/CL-001-Airo-First-Pass-Review.md",
    "docs/leadership/bridgette-beardsley.md",
    "docs/leadership/sheldon-bardol.md",
    "content/homepage.md",
    "content/about.md",
    "content/faqs.md",
    "content/contact.md",
    "content/product-catalog.md",
    "prompts/content-writer.md",
    "prompts/product-descriptions.md",
    "prompts/email-writer.md",
    "prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md",
    "website/pages/home.md",
    "website/pages/about.md",
    "website/pages/faqs.md",
    "website/pages/contact.md",
    "website/styles/design-system.md",
    "website/src/concierge/README.md",
]

SLOGAN_GOVERNING_FILES = [
    "README.md",
    "docs/master-catalog.md",
    "docs/project-runbook.md",
    "docs/value-proposition.md",
    "docs/architecture/website-information-architecture.md",
    "docs/architecture/intelligent-living-concierge.md",
    "docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md",
    "docs/checklists/CL-001-Airo-First-Pass-Review.md",
    "content/homepage.md",
    "content/contact.md",
    "prompts/content-writer.md",
    "prompts/product-descriptions.md",
    "prompts/email-writer.md",
    "prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md",
    "website/pages/home.md",
    "website/pages/contact.md",
    "website/styles/design-system.md",
]

TEXT_SUFFIXES = {
    ".md", ".txt", ".json", ".svg", ".html", ".htm", ".py", ".js", ".mjs",
    ".ts", ".tsx", ".jsx", ".css", ".scss", ".yml", ".yaml", ".csv"
}


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        raise FileNotFoundError(rel)
    return path.read_text(encoding="utf-8", errors="replace")


def require(text: str, token: str, rel: str, errors: list[str]) -> None:
    if token not in text:
        errors.append(f"{rel}: missing required token {token!r}")


def validate_required_files(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"Missing required source-of-truth file: {rel}")


def validate_brand_language(errors: list[str]) -> None:
    for rel in SLOGAN_GOVERNING_FILES:
        try:
            text = read(rel)
        except FileNotFoundError:
            continue
        require(text, OFFICIAL_SLOGAN, rel, errors)

    # The old hero is retired everywhere, including docs, scripts and SVG source.
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in {".git", "node_modules", ".venv", "venv"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if RETIRED_HERO in text:
            errors.append(f"{path.relative_to(ROOT)}: retired hero phrase remains")
        # Catch the old two-line graphic treatment even when punctuation/case differs.
        upper = text.upper()
        if "SMART LIVING." in upper and "ELEVATED." in upper:
            errors.append(f"{path.relative_to(ROOT)}: retired split hero treatment remains")


def validate_homepage_contract(errors: list[str]) -> None:
    for rel in (
        "content/homepage.md",
        "website/pages/home.md",
        "docs/architecture/website-information-architecture.md",
        "prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md",
        "docs/checklists/CL-001-Airo-First-Pass-Review.md",
    ):
        try:
            text = read(rel)
        except FileNotFoundError:
            continue
        for token in (OFFICIAL_SLOGAN, PRIMARY_CTA, SECONDARY_CTA):
            require(text, token, rel, errors)


def validate_founders(errors: list[str]) -> None:
    b = read("docs/leadership/bridgette-beardsley.md")
    s = read("docs/leadership/sheldon-bardol.md")
    require(b, BRIDGETTE_TITLE, "docs/leadership/bridgette-beardsley.md", errors)
    require(s, SHELDON_TITLE, "docs/leadership/sheldon-bardol.md", errors)

    for rel in (
        "website/pages/home.md",
        "website/pages/about.md",
        "prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md",
        "docs/master-catalog.md",
    ):
        text = read(rel)
        require(text, BRIDGETTE_TITLE, rel, errors)
        require(text, SHELDON_TITLE, rel, errors)


def validate_contact(errors: list[str]) -> None:
    for rel in (
        "content/contact.md",
        "website/pages/contact.md",
        "docs/architecture/website-information-architecture.md",
        "prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md",
        "docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md",
    ):
        text = read(rel)
        require(text, SUPPORT_EMAIL, rel, errors)
        require(text, INFO_EMAIL, rel, errors)

    contact = read("website/pages/contact.md")
    for token in (
        "Support",
        "Product Information",
        "Consultation",
        "General Question",
        "Business / Partnership",
        "property_type",
        "square_feet_exact",
        "square_feet_band",
        BLUEPRINT_NAME,
    ):
        require(contact, token, "website/pages/contact.md", errors)


def validate_concierge(errors: list[str]) -> None:
    for rel in (
        "docs/architecture/intelligent-living-concierge.md",
        "website/pages/home.md",
        "docs/architecture/website-information-architecture.md",
        "prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md",
        "docs/master-catalog.md",
    ):
        text = read(rel)
        for token in (PRIMARY_CTA, CONCIERGE_NAME, BLUEPRINT_NAME):
            require(text, token, rel, errors)

    architecture = read("docs/architecture/intelligent-living-concierge.md")
    for token in (
        "Lifestyle",
        "Experience",
        "Intelligence",
        "Technology",
        "Essential Intelligence",
        "Elevated Living",
        "Complete LuxSync Experience",
    ):
        require(architecture, token, "docs/architecture/intelligent-living-concierge.md", errors)

    modules = ROOT / "website" / "src" / "concierge" / "modules"
    if not modules.exists():
        errors.append("website/src/concierge/modules: missing")
        return
    json_files = sorted(modules.glob("*.json"))
    if not json_files:
        errors.append("website/src/concierge/modules: no JSON modules found")
    for path in json_files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")


def validate_product_catalog(errors: list[str]) -> None:
    catalog = read("content/product-catalog.md")
    for token in (
        "Physical Product Families",
        "Curated Bundle",
        "LuxSync Experiences",
        "Welcome Home",
        "Goodnight",
        "Water Watch",
        "Guest Ready",
        "Property Pulse",
        "Accessible Living",
        "Validated Live Product",
        "Solution Concept",
    ):
        require(catalog, token, "content/product-catalog.md", errors)

    business = read("docs/business-plan.md")
    if "Pricing status: unresolved" not in business:
        errors.append("docs/business-plan.md: senior-service pricing must remain explicitly unresolved")


def validate_typography_and_palette(errors: list[str]) -> None:
    design = read("website/styles/design-system.md")
    for token in (
        "Manrope",
        "Inter",
        "#0D1526",
        "#172036",
        "#D0BEB0",
        "#9E8B85",
        "#967878",
        "#7B96B2",
        "#D6B0A0",
    ):
        require(design, token, "website/styles/design-system.md", errors)


def main() -> int:
    errors: list[str] = []
    validate_required_files(errors)

    # Stop deeper checks from raising on a missing baseline file.
    if errors:
        print("LuxSync repository validation FAILED:")
        for err in errors:
            print(f"- {err}")
        return 1

    validate_brand_language(errors)
    validate_homepage_contract(errors)
    validate_founders(errors)
    validate_contact(errors)
    validate_concierge(errors)
    validate_product_catalog(errors)
    validate_typography_and_palette(errors)

    if errors:
        print("LuxSync repository validation FAILED:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("LuxSync repository validation PASSED")
    print(f"Slogan: {OFFICIAL_SLOGAN}")
    print(f"Primary CTA: {PRIMARY_CTA}")
    print(f"Concierge: {CONCIERGE_NAME}")
    print(f"Blueprint: {BLUEPRINT_NAME}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

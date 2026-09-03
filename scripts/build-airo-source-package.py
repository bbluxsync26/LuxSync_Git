#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "dist/airo/LuxSync-Airo-Source.zip"
SCHEMA_VERSION = "1.0"
PROFILE = "website-authoritative"
REPOSITORY = "bbluxsync26/LuxSync_Git"

EXACT_FILES = (
    "README.md",
    "docs/production-source-of-truth.md",
    "docs/master-catalog.md",
    "docs/architecture/website-information-architecture.md",
    "docs/architecture/intelligent-living-concierge.md",
    "docs/decisions/DEC-004-commerce-plus-and-airo-role.md",
    "docs/checklists/CL-001-Airo-First-Pass-Review.md",
    "docs/checklists/CL-002-Account-Access-Review.md",
    "docs/leadership/bridgette-beardsley.md",
    "docs/leadership/sheldon-bardol.md",
    "brand/README.md",
    "brand/brand-architecture.md",
    "brand/colors.md",
    "brand/typography.md",
    "brand/voice-and-tone.md",
    "website/implementation-manifest.json",
    "website/navigation.md",
    "website/asset-map.md",
    "website/account-access-manifest.json",
    "prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md",
)

INCLUDE_PREFIXES = (
    "content/",
    "website/pages/",
    "website/styles/",
    "website/src/",
    "website/assets/auth/",
    "site/",
    "brand/assets/logos/",
    "brand/assets/icons/",
    "brand/assets/dividers/",
    "brand/exports/digital/approved/",
    "brand/exports/digital/account-access/",
    "brand/exports/digital/marketing/",
)

FORBIDDEN_PREFIXES = (
    ".git/",
    ".github/",
    "dist/",
    "node_modules/",
    "brand/reference-boards/",
    "brand/source-logo/",
    "brand/masters/",
    "brand/audit/",
    "brand/exports/print/",
    "brand/templates/print-physical/",
)

FORBIDDEN_EXACT = {
    "docs/financial-model.md",
    "docs/business-plan.md",
    "docs/decisions/DEC-005-senior-service-pricing.md",
}

SECRET_NAME_FRAGMENTS = (
    ".env",
    "secret",
    "credential",
    "private_key",
    "private-key",
    "id_rsa",
    "id_ed25519",
    "token.txt",
    "password",
    "passwd",
    "keystore",
)

SECRET_SUFFIXES = {".pem", ".p12", ".pfx", ".key", ".jks"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the governed LuxSync source package for GoDaddy Airo.")
    parser.add_argument("--check", action="store_true", help="Validate the package selection without writing a ZIP.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Output ZIP path.")
    return parser.parse_args()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_commit() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        return None


def is_secret_like(path: Path) -> bool:
    lower = path.name.lower()
    if path.suffix.lower() in SECRET_SUFFIXES:
        return True
    return any(fragment in lower for fragment in SECRET_NAME_FRAGMENTS)


def is_forbidden(repo_path: str) -> bool:
    if repo_path in FORBIDDEN_EXACT:
        return True
    return any(repo_path.startswith(prefix) for prefix in FORBIDDEN_PREFIXES)


def collect_files() -> tuple[list[Path], list[str]]:
    errors: list[str] = []
    selected: set[Path] = set()

    for repo_path in EXACT_FILES:
        path = ROOT / repo_path
        if not path.is_file():
            errors.append(f"missing required exact source: {repo_path}")
        else:
            selected.add(path)

    for prefix in INCLUDE_PREFIXES:
        base = ROOT / prefix
        files = [p for p in base.rglob("*") if p.is_file()] if base.exists() else []
        if not files:
            errors.append(f"include prefix resolved to no files: {prefix}")
            continue
        selected.update(files)

    clean: list[Path] = []
    for path in sorted(selected, key=lambda item: rel(item)):
        repo_path = rel(path)
        if is_forbidden(repo_path):
            errors.append(f"forbidden path selected: {repo_path}")
            continue
        if is_secret_like(path):
            errors.append(f"secret-like filename selected: {repo_path}")
            continue
        clean.append(path)

    return clean, errors


def package_manifest(files: list[Path]) -> dict:
    commit = git_commit()
    records = []
    total_bytes = 0
    for path in files:
        size = path.stat().st_size
        total_bytes += size
        records.append({
            "path": rel(path),
            "bytes": size,
            "sha256": sha256(path),
        })
    return {
        "schema_version": SCHEMA_VERSION,
        "package_profile": PROFILE,
        "repository": REPOSITORY,
        "source_commit": commit,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "file_count": len(records),
        "uncompressed_bytes": total_bytes,
        "files": records,
    }


def airo_readme(manifest: dict) -> str:
    commit = manifest.get("source_commit") or "unknown"
    return f"""# LuxSync Airo Source Package\n\nThis ZIP is a governed website-build projection of the LuxSync GitHub repository.\n\n**Repository:** `{REPOSITORY}`  \n**Source commit:** `{commit}`  \n**Profile:** `{PROFILE}`\n\n## Authority\n\nGitHub `master` remains the source of truth. This package is input to a staging/design/code-generation cycle only. Airo output is not authoritative until it is exported, reconciled into a GitHub branch, reviewed, validated by LuxSync CI, and merged.\n\n## Build Rules\n\n1. Follow `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md` as the controlling instruction.\n2. Preserve the supplied LuxSync brand system, approved logo deliveries, typography, palette, voice, page architecture, Concierge logic, Contact architecture, account-access boundaries, and Commerce Plus authority.\n3. Evolve the supplied `site/` implementation rather than inventing an unrelated second application.\n4. Do not invent prices, stock, compatibility claims, reviews, testimonials, suppliers, partnerships, awards, payment integrations, auth capabilities, or roadmap features.\n5. Do not connect production DNS or live payments during this build cycle.\n6. Keep mutable customer/product/business data in live code/content rather than baking it into generated graphics.\n7. Treat `AIRO-PACKAGE-MANIFEST.json` as provenance evidence for the supplied files.\n\n## Return Path\n\nWhen the Airo iteration is ready for review, export/download the full Airo project as a ZIP. Preserve that export unchanged and return it for GitHub reconciliation.\n"""


def build_zip(files: list[Path], output: Path) -> None:
    manifest = package_manifest(files)
    output = output if output.is_absolute() else ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    temp = output.with_suffix(output.suffix + ".tmp")

    manifest_json = json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    readme = airo_readme(manifest)

    with zipfile.ZipFile(temp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        archive.writestr("AIRO-README.md", readme)
        archive.writestr("AIRO-PACKAGE-MANIFEST.json", manifest_json)
        for path in files:
            archive.write(path, rel(path))

    os.replace(temp, output)
    print(f"Airo source package written: {output.relative_to(ROOT) if output.is_relative_to(ROOT) else output}")
    print(f"Repository files: {manifest['file_count']}")
    print(f"Uncompressed bytes: {manifest['uncompressed_bytes']}")
    print(f"Source commit: {manifest.get('source_commit') or 'unknown'}")


def main() -> int:
    args = parse_args()
    files, errors = collect_files()

    if errors:
        print("LuxSync Airo source package validation FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    if not files:
        print("LuxSync Airo source package validation FAILED: no files selected")
        return 1

    print("LuxSync Airo source package selection PASSED")
    print(f"Selected repository files: {len(files)}")

    if args.check:
        return 0

    build_zip(files, args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())

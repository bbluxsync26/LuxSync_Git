#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "brand/audit/brand-build-state.json"
REPORT = ROOT / "brand/audit/brand-build-report.md"
EXCEPTIONS = ROOT / "brand/audit/brand-exceptions.md"
FINAL = ROOT / "brand/audit/image-cleanup-final-validation.md"
PRODUCTION_GUIDE = ROOT / "docs/production-asset-library.md"

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def load_json(path: Path) -> dict:
    if not path.exists():
        fail(f"missing required JSON: {path.relative_to(ROOT)}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON {path.relative_to(ROOT)}: {exc}")
        return {}


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing required file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


state = load_json(STATE)
report = read(REPORT)
exceptions = read(EXCEPTIONS)
final = read(FINAL)
production_guide = read(PRODUCTION_GUIDE)

if state.get("overall_state") != "complete":
    fail("brand build overall_state must be complete")
if state.get("current_phase") != "complete":
    fail("brand build current_phase must be complete")
if state.get("human_decision_required") is not False:
    fail("completed image cleanup must not require a human brand decision")

phases = state.get("phases", {})
for phase_id in ("phase0", "wave1", "wave2", "wave3"):
    phase = phases.get(phase_id, {})
    if phase.get("state") != "complete":
        fail(f"{phase_id}: state must be complete")
    if phase.get("known_gaps", []) not in ([], None):
        fail(f"{phase_id}: known_gaps must be empty at closeout")

last_validation = state.get("last_validation", {})
if last_validation.get("result") != "success":
    fail("last durable repository validation must be successful")
if not last_validation.get("run_id"):
    fail("last durable repository validation run_id missing")

idem = state.get("idempotence", {})
expected_counts = {
    "validated_atomic_asset_count": 31,
    "validated_atomic_format_file_count": 93,
    "validated_account_derivative_asset_count": 4,
    "validated_account_derivative_file_count": 8,
    "approved_board_derived_asset_count": 58,
    "approved_board_icon_count": 16,
    "approved_board_divider_accent_count": 42,
    "wave2_static_template_count": 10,
    "wave2_static_delivery_file_count": 20,
    "wave3_static_print_asset_count": 8,
    "wave3_static_delivery_file_count": 24,
    "wave3_physical_placement_spec_count": 8,
    "protected_reference_board_count": 7,
    "protected_logo_master_count": 3,
}
for key, expected in expected_counts.items():
    if idem.get(key) != expected:
        fail(f"idempotence count mismatch for {key}: expected {expected}, found {idem.get(key)!r}")
if idem.get("skip_unless_invalidated") is not True:
    fail("completed image system must be skip_unless_invalidated")

required_paths = [
    "brand/assets/asset-manifest.json",
    "brand/manifests/omnichannel-brand-manifest.json",
    "brand/manifests/approved-board-asset-manifest.json",
    "brand/manifests/wave2-digital-marketing-manifest.json",
    "brand/manifests/wave3-print-physical-manifest.json",
    "brand/audit/reference-board-visual-inventory.md",
    "brand/audit/image-cleanup-final-validation.md",
    "brand/source-logo/LuxSync_Logo_Horizontal_Combo.png",
    "brand/source-logo/LuxSync_Logo_Horizontal_Final.png",
    "brand/source-logo/LuxSync_Logo_Orb.png",
]
for rel in required_paths:
    if not (ROOT / rel).exists():
        fail(f"missing governed image artifact: {rel}")

reference_boards = list((ROOT / "brand/reference-boards").glob("*.png")) if (ROOT / "brand/reference-boards").exists() else []
if len(reference_boards) != 7:
    fail(f"expected 7 protected reference-board PNGs; found {len(reference_boards)}")

retired_asset_dirs = (
    "01-logos", "02-icons", "03-buttons", "04-ui-controls", "05-dividers-accents",
    "06-product-cards", "07-heroes", "08-sections", "09-stationery",
)
for dirname in retired_asset_dirs:
    if (ROOT / "brand/assets" / dirname).exists():
        fail(f"retired grid-sliced production directory remains: brand/assets/{dirname}")

stale_report_phrases = (
    "Wave 1 in progress",
    "Wave 2 and Wave 3 remain intentionally pending",
    "pending pull-request and post-merge repository CI",
    "pending repository PR validation",
)
for phrase in stale_report_phrases:
    if phrase in report:
        fail(f"brand-build-report.md contains stale completion state: {phrase!r}")

if "**Run state:** Complete" not in report:
    fail("brand-build-report.md must declare complete run state")
if "**Current phase:** Complete" not in report:
    fail("brand-build-report.md must declare complete current phase")
if "**Current phase:** Complete" not in exceptions:
    fail("brand-exceptions.md must declare complete current phase")
if "no open repository-wide image-cleanup blockers" not in exceptions.lower():
    fail("brand-exceptions.md must explicitly close repository-wide image cleanup blockers")

required_final_tokens = (
    "repository-wide image cleanup is complete",
    "31 approved atomic assets",
    "58 reusable approved board-derived artworks",
    "10 deterministic text-safe static compositions",
    "8 governed 300-DPI print/stationery compositions",
    "GoDaddy production publishing: intentionally skipped",
)
final_lower = final.lower()
for token in required_final_tokens:
    if token.lower() not in final_lower:
        fail(f"final image validation record missing token: {token!r}")

for token in (
    "scripts/validate-production-brand.py",
    "scripts/validate-brand-derivatives.py",
    "scripts/validate-approved-board-assets.py",
    "scripts/validate-wave2-digital-marketing.py",
    "scripts/validate-wave3-print-physical.py",
    "scripts/validate-image-governance.py",
):
    if token not in production_guide:
        fail(f"production asset guide missing validator reference: {token}")

if errors:
    print("LuxSync image governance validation FAILED:")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("LuxSync image governance validation PASSED")
print("Brand/image state: complete")
print("Production waves: 3 of 3 complete")
print("Protected reference boards: 7")
print("Protected logo masters: 3")
print("No open repository-wide image cleanup blockers")

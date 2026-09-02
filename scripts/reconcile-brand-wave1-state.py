#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OMNI = ROOT / "brand/manifests/omnichannel-brand-manifest.json"
STATE = ROOT / "brand/audit/brand-build-state.json"
REPORT = ROOT / "brand/audit/brand-build-report.md"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


omni = load(OMNI)
batches = omni.get("generated_derivative_batches", {})
account = batches.get("account-access-ambient", {})
assets = account.get("assets", [])
complete = (
    account.get("qa_status") == "passed"
    and len(assets) == 4
    and all(a.get("qa_status") == "passed" for a in assets)
    and all(set(a.get("files", {})) == {"png", "webp"} for a in assets)
)
if not complete:
    raise SystemExit("Account-access derivative batch is not complete and QA-passed; refusing Wave 1 state promotion.")

omni["version"] = "1.1-wave1"
omni["status"] = "wave1-in-progress"
related = omni.setdefault("related_validated_assets", {})
related["gap"] = "closed: four production-approved account ambient SVG masters now have governed PNG/WebP derivative records"
related["derivative_batch"] = "account-access-ambient"
related["derivative_asset_count"] = 4
related["derivative_file_count"] = 8

stale_fragments = (
    "Auth production-approved ambient SVGs lack omnichannel PNG/WebP derivative records.",
    "The current repository includes stale pre-migration logo paths in active text/reference files; Phase 0 self-healing repairs them.",
)
omni["known_omnichannel_gaps"] = [
    item for item in omni.get("known_omnichannel_gaps", []) if item not in stale_fragments
]
omni["next_checkpoint"] = (
    "Wave 1 Checkpoint 1: visually inspect every element on brand/reference-boards, map each to an existing validated asset "
    "or a missing master, and create only missing faithful masters/justified derivatives. The account-access ambient digital "
    "derivative batch is complete and must be skipped unless its source or QA evidence changes."
)
write(OMNI, omni)

state = load(STATE)
state["working_branch"] = "feature/brand-omnichannel-wave1"
state["overall_state"] = "wave1-in-progress-board-visual-audit-blocked"
state["current_phase"] = "wave1"
wave1 = state.setdefault("phases", {}).setdefault("wave1", {})
wave1["state"] = "in_progress-blocked-only-on-board-pixel-access-for-new-board-derived-masters"
validated = wave1.setdefault("already_validated_inputs", [])
for item in (
    "4 account-access ambient PNG derivatives with manifest hashes and QA evidence",
    "4 account-access ambient lossless WebP derivatives with manifest hashes and QA evidence",
    "account-access derivative QA contact sheet",
    "self-healing feature-branch derivative renderer and CI validator",
):
    if item not in validated:
        validated.append(item)
wave1["known_gaps"] = [
    item for item in wave1.get("known_gaps", [])
    if "VIP account ambient PNG/WebP derivatives" not in item
]
completed = wave1.setdefault("completed_checks", [])
for item in (
    "account-access production SVG sources revalidated against website/assets/auth/manifest.json",
    "four PNG and four lossless WebP account-access derivatives rendered and hashed",
    "account-access derivative QA contact sheet generated",
    "brand derivative renderer made idempotent and feature-branch scoped",
    "brand derivative validation added to repository CI",
):
    if item not in completed:
        completed.append(item)
state["next_checkpoint"] = (
    "Wave 1 Checkpoint 1: obtain direct visual access to all seven brand/reference-boards, perform element-level mapping, "
    "then create only missing faithful website-critical masters. Skip the 31 validated atomic assets and the completed "
    "account-access derivative batch unless direct QA invalidates them."
)
write(STATE, state)

report = REPORT.read_text(encoding="utf-8")
marker = "## Wave 1 derivative checkpoint\n"
section = """## Wave 1 derivative checkpoint

Completed and QA-passed on `feature/brand-omnichannel-wave1`:

- Four production-approved account-access ambient SVG masters were rendered to PNG.
- The same four masters were rendered to lossless WebP.
- Source, PNG, WebP, dimensions, transparency and QA hashes are recorded in the omnichannel manifest.
- A QA contact sheet is stored at `brand/audit/qa/account-access-derivatives.jpg`.
- `scripts/render-brand-digital-derivatives.py` skips derivatives whose source and output hashes remain valid.
- `scripts/validate-brand-derivatives.py` enforces the batch in standard repository CI.
- `.github/workflows/build-brand-derivatives.yml` performs deterministic derivative generation only on brand feature branches and commits only governed derivative outputs.

This closes the account-access PNG/WebP gap. The next unfinished Wave 1 checkpoint remains the element-level visual audit of the seven approval boards.

"""
if marker not in report:
    anchor = "## Current execution constraint\n"
    if anchor in report:
        report = report.replace(anchor, section + anchor)
    else:
        report += "\n" + section
    REPORT.write_text(report, encoding="utf-8")

print("Wave 1 derivative state reconciled.")

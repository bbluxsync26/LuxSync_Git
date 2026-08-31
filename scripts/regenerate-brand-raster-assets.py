#!/usr/bin/env python3
"""Compatibility entrypoint for the authoritative LuxSync asset pipeline."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRE_RENDER_STEPS = (
    ROOT / "scripts" / "generate-luxury-orbit-assets.py",
    ROOT / "scripts" / "normalize-luxury-orbit-fonts.py",
)
POST_RESTORE_STEPS = (
    ROOT / "scripts" / "apply-approved-logo-artwork.py",
    ROOT / "scripts" / "render-luxury-orbit-assets.py",
    ROOT / "scripts" / "reconcile-asset-metadata.py",
)
PROTECTED_WRAPPERS = (
    ROOT / "brand" / "assets" / "01-brand" / "luxsync-monogram-orb.svg",
    ROOT / "brand" / "assets" / "01-brand" / "luxsync-horizontal-lockup.svg",
)


def main() -> int:
    protected = {path: path.read_text(encoding="utf-8") for path in PROTECTED_WRAPPERS}
    for step in PRE_RENDER_STEPS:
        subprocess.run([sys.executable, str(step)], check=True)
    for path, contents in protected.items():
        path.write_text(contents, encoding="utf-8")
    for step in POST_RESTORE_STEPS:
        subprocess.run([sys.executable, str(step)], check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

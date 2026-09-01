#!/usr/bin/env python3
"""Install the staged LuxSync production-site source bundle once."""
from __future__ import annotations

import base64
import io
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS = ROOT / "scripts" / "site_bundle"

parts = sorted(PARTS.glob("part*"))
if len(parts) != 9:
    raise SystemExit(f"Expected 9 site bundle parts, found {len(parts)}")

payload = "".join(part.read_text(encoding="utf-8").strip() for part in parts)
data = base64.b64decode(payload, validate=True)

with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as archive:
    root_resolved = ROOT.resolve()
    for member in archive.getmembers():
        target = (ROOT / member.name).resolve()
        if target != root_resolved and root_resolved not in target.parents:
            raise SystemExit(f"Unsafe archive member: {member.name}")
    archive.extractall(ROOT)

print("LuxSync production website source installed.")

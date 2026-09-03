#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"brand/manifests/wave3-print-physical-manifest.json"
APPROVAL=ROOT/"brand/audit/wave3-print-physical-qa-approval.json"


def sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()


def main()->None:
    m=json.loads(MANIFEST.read_text())
    a=json.loads(APPROVAL.read_text())
    qa_path=ROOT/m["qa"]["contact_sheet"]
    current=sha256(qa_path)
    if a.get("status")!="passed":
        raise SystemExit("Wave 3 QA approval is not passed")
    if a.get("reviewed_contact_sheet_sha256")!=current:
        raise SystemExit("Wave 3 QA approval does not match current contact sheet")
    m["status"]="qa-passed"
    m["qa"]["sha256"]=current
    m["qa"]["status"]="manual-review-passed"
    for rec in m.get("static_assets",[]):
        rec["qa_status"]="manual-contact-sheet-and-pdf-render-review-passed"
    MANIFEST.write_text(json.dumps(m,indent=2)+"\n")
    print("Wave 3 visual/PDF QA approval reconciled to manifest")

if __name__=="__main__": main()

#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from PIL import Image
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"brand/manifests/wave3-print-physical-manifest.json"
APPROVAL=ROOT/"brand/audit/wave3-print-physical-qa-approval.json"
EXPECTED_COUNT=8
DPI=300


def sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()


def fail(msg:str)->None:
    raise SystemExit(f"Wave 3 validation FAILED: {msg}")


def near(a:float,b:float,tol:float=.6)->bool:
    return abs(a-b)<=tol


def main()->None:
    if not MANIFEST.exists(): fail("manifest missing")
    if not APPROVAL.exists(): fail("manual QA approval record missing")
    m=json.loads(MANIFEST.read_text())
    a=json.loads(APPROVAL.read_text())
    if m.get("status")!="qa-passed": fail(f"manifest status is {m.get('status')}")
    assets=m.get("static_assets",[])
    if len(assets)!=EXPECTED_COUNT or m.get("static_asset_count")!=EXPECTED_COUNT: fail("unexpected static asset count")
    qa_path=ROOT/m["qa"]["contact_sheet"]
    if not qa_path.exists(): fail("QA contact sheet missing")
    qhash=sha256(qa_path)
    if m["qa"].get("sha256")!=qhash: fail("manifest QA hash mismatch")
    if a.get("reviewed_contact_sheet_sha256")!=qhash or a.get("status")!="passed": fail("manual QA approval is not bound to current contact sheet")
    if m["qa"].get("status")!="manual-review-passed": fail("manifest QA status not sealed")
    for rec in assets:
        trim=rec["trim_in"]; bleed=float(rec["bleed_in"])
        expected=(round((trim[0]+2*bleed)*DPI),round((trim[1]+2*bleed)*DPI))
        if tuple(rec["full_pixel_dimensions"])!=expected: fail(f"{rec['id']} manifest dimensions wrong")
        files=rec["files"]
        for key in ("master_png","png","tiff","pdf"):
            p=ROOT/files[key]["path"]
            if not p.exists(): fail(f"{rec['id']} missing {key}")
            if sha256(p)!=files[key]["sha256"]: fail(f"{rec['id']} {key} hash mismatch")
        mp=ROOT/files["master_png"]["path"]; pp=ROOT/files["png"]["path"]
        if sha256(mp)!=sha256(pp): fail(f"{rec['id']} PNG delivery differs from master")
        with Image.open(pp) as im:
            if im.size!=expected: fail(f"{rec['id']} PNG dimensions wrong")
            dpi=im.info.get("dpi")
            if dpi and (abs(dpi[0]-DPI)>2 or abs(dpi[1]-DPI)>2): fail(f"{rec['id']} PNG DPI wrong")
        tp=ROOT/files["tiff"]["path"]
        with Image.open(tp) as im:
            if im.size!=expected: fail(f"{rec['id']} TIFF dimensions wrong")
            if im.mode!="CMYK": fail(f"{rec['id']} TIFF is not CMYK")
        pdfp=ROOT/files["pdf"]["path"]
        reader=PdfReader(str(pdfp))
        if len(reader.pages)!=1: fail(f"{rec['id']} PDF must be one page")
        box=reader.pages[0].mediabox
        expw=(trim[0]+2*bleed)*72; exph=(trim[1]+2*bleed)*72
        if not near(float(box.width),expw) or not near(float(box.height),exph): fail(f"{rec['id']} PDF page size wrong")
        logo=ROOT/rec["logo_source"]["path"]
        if not logo.exists() or sha256(logo)!=rec["logo_source"]["sha256"]: fail(f"{rec['id']} approved logo source changed")
        orn=rec.get("ornament_source")
        if orn:
            op=ROOT/orn["path"]
            if not op.exists() or sha256(op)!=orn["sha256"]: fail(f"{rec['id']} ornament source changed")
    physical=ROOT/m["physical_spec"]["path"]
    if not physical.exists() or sha256(physical)!=m["physical_spec"]["sha256"]: fail("physical production spec changed")
    if m["physical_spec"].get("placement_count")!=8: fail("unexpected physical placement count")
    print("LuxSync Wave 3 print/physical validation PASSED")
    print(f"Static print assets: {EXPECTED_COUNT}")
    print("Formats: 300-DPI PNG + CMYK TIFF + exact-page PDF")
    print("Physical production: 8 vendor-neutral placement specifications")

if __name__=="__main__": main()

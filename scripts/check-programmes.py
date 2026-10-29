#!/usr/bin/env python3
"""Programmes, editions and archetypes compile; reviewer gates are legal and cannot be skipped (design brief 13)."""
import glob, os
from _common import (programmes, editions, archetypes, department_index, LIFECYCLE, EDITIONS, ARCHETYPES, path, rel,
                     load_yaml, finish)

depts = department_index()
progs = programmes()
problems, count = [], 0
if sorted(editions()) != sorted(EDITIONS):
    problems.append(f"editions/ must define exactly {EDITIONS}")
for e, v in editions().items():
    for k in ("id", "title", "typical_context", "design_emphasis", "coe_form", "champions_form", "governance_form", "depth_default"):
        if k not in v:
            problems.append(f"editions/{e}/edition.yaml: missing '{k}'")
if sorted(archetypes()) != sorted(ARCHETYPES):
    problems.append(f"archetypes/ must define exactly {ARCHETYPES}")
for pid, p in progs.items():
    count += 1
    where = f"programmes/{pid}/programme.yaml"
    if p.get("id") != pid:
        problems.append(f"{where}: id must equal the folder name")
    for st in p.get("lifecycle", []):
        if st not in LIFECYCLE:
            problems.append(f"{where}: lifecycle stage '{st}' is not in {LIFECYCLE}")
    for a in p.get("artefacts", []):
        if a.get("stage") not in p.get("lifecycle", []):
            problems.append(f"{where}: artefact '{a.get('id')}' stage '{a.get('stage')}' is not in the programme lifecycle")
        if sorted((a.get("depth") or {}).keys()) != sorted(EDITIONS):
            problems.append(f"{where}: artefact '{a.get('id')}' must set depth for {EDITIONS}")
        for v in (a.get("depth") or {}).values():
            if v not in ("omit", "light", "standard", "full"):
                problems.append(f"{where}: artefact '{a.get('id')}' depth '{v}' is not omit, light, standard or full")
    for g in p.get("gates", []):
        r = g.get("reviewer")
        if r not in depts or not depts[r].get("reviewer"):
            problems.append(f"{where}: gate reviewer '{r}' is not a reviewer-class department")
        if g.get("skippable") is not False or g.get("blocking") is not True:
            problems.append(f"{where}: gate '{r}' must be blocking: true and skippable: false (reviewer gates cannot be skipped)")
        if g.get("stage") not in p.get("lifecycle", []):
            problems.append(f"{where}: gate '{r}' stage is not in the programme lifecycle")
    for inc in p.get("includes", []):
        if inc["programme"] not in progs:
            problems.append(f"{where}: includes unknown programme '{inc['programme']}'")
    for d in p.get("supporting_departments", []):
        if d not in depts:
            problems.append(f"{where}: supporting department '{d}' is not in the catalogue")
# Any programme that produces delivery artefacts for agents must carry the security-privacy gate.
for pid, p in progs.items():
    if any(a["skill"].startswith("m365-agents:") for a in p.get("artefacts", [])):
        if not any(g["reviewer"] == "security-privacy" for g in p.get("gates", [])):
            problems.append(f"programmes/{pid}: agent delivery requires a blocking security-privacy gate")
# Reviewer tests: each active reviewer department has blocking cases.
for d in depts.values():
    if d.get("reviewer") and d["status"] == "active":
        f = path("tests", "reviewers", f"{d['id']}.yaml")
        if not os.path.exists(f):
            problems.append(f"tests/reviewers/{d['id']}.yaml is missing"); continue
        cases = (load_yaml(f) or {}).get("cases", [])
        count += len(cases)
        if not any(c.get("expected_verdict") == "blocking" for c in cases):
            problems.append(f"{rel(f)}: needs at least one case expected to block")
        if not any(c.get("expected_verdict") in ("advisory", "pass") for c in cases):
            problems.append(f"{rel(f)}: needs at least one case expected not to block (proportionality)")
        for c in cases:
            for k in ("id", "skill", "submission", "expected_verdict", "expected_reason"):
                if k not in c:
                    problems.append(f"{rel(f)}: case {c.get('id')} missing '{k}'")
finish("Programmes, editions, archetypes and gates", problems, count)

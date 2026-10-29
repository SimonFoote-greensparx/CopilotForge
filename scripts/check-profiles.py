#!/usr/bin/env python3
"""Sample profiles validate and are fictional; tailoring plans match the golden outputs; acceptance assertions hold.

    python3 scripts/check-profiles.py            # verify
    python3 scripts/check-profiles.py --update   # regenerate evaluations/golden/*.plan.yaml after a reviewed change
"""
import glob, json, os, sys
from _common import path, rel, load_yaml, validate_schema, finish
import importlib.util

spec = importlib.util.spec_from_file_location("tailor", path("scripts", "tailor.py"))
tailor = importlib.util.module_from_spec(spec); spec.loader.exec_module(tailor)
schema = json.load(open(path("profiles", "schema.json"), encoding="utf-8"))
update = "--update" in sys.argv
problems, count = [], 0
plans = {}
for f in sorted(glob.glob(path("profiles", "samples", "*.yaml"))):
    count += 1
    data = load_yaml(f)
    for e in validate_schema(data, schema):
        problems.append(f"{rel(f)}: {e}")
    if data.get("fictional") is not True:
        problems.append(f"{rel(f)}: samples must declare fictional: true")
    if "(fictional)" not in str(data.get("organisation", {}).get("name", "")):
        problems.append(f"{rel(f)}: sample organisation names end with '(fictional)'")
    plan, errs = tailor.plan(f)
    if errs:
        continue
    name = os.path.splitext(os.path.basename(f))[0]
    plans[name] = plan
    text = "# Golden tailoring plan. Regenerate with python3 scripts/check-profiles.py --update after review.\n" + tailor.dump(plan)
    golden = path("evaluations", "golden", f"{name}.plan.yaml")
    if update:
        open(golden, "w", encoding="utf-8").write(text)
    elif not os.path.exists(golden):
        problems.append(f"{rel(golden)} is missing; review the plan and run check-profiles.py --update")
    elif open(golden, encoding="utf-8").read() != text:
        problems.append(f"{rel(golden)} differs from the current tailoring output; review the change, then run check-profiles.py --update")

acc = path("evaluations", "acceptance.yaml")
for case in (load_yaml(acc) or {}).get("cases", []) if os.path.exists(acc) else []:
    p = plans.get(case["sample"])
    if not p:
        problems.append(f"evaluations/acceptance.yaml: sample '{case['sample']}' not found"); continue
    exp = case["expect"]
    count += 1
    if "edition" in exp and p["edition"]["id"] != exp["edition"]:
        problems.append(f"acceptance {case['id']}: edition {p['edition']['id']} != {exp['edition']}")
    if "archetype" in exp and p["archetype"]["id"] != exp["archetype"]:
        problems.append(f"acceptance {case['id']}: archetype {p['archetype']['id']} != {exp['archetype']}")
    for prog in exp.get("programmes_include", []):
        if prog not in p["programmes"]:
            problems.append(f"acceptance {case['id']}: programme '{prog}' missing")
    for prog in exp.get("programmes_exclude", []):
        if prog in p["programmes"]:
            problems.append(f"acceptance {case['id']}: programme '{prog}' should not be recommended")
    arts = {a["artefact"] for a in p["artefacts"]}
    for a in exp.get("artefacts_include", []):
        if a not in arts:
            problems.append(f"acceptance {case['id']}: artefact '{a}' missing")
    for a in exp.get("artefacts_exclude", []):
        if a in arts:
            problems.append(f"acceptance {case['id']}: artefact '{a}' should be omitted")
    gates = {g["reviewer"] for g in p["reviewer_gates"]}
    for g in exp.get("gates_include", []):
        if g not in gates:
            problems.append(f"acceptance {case['id']}: reviewer gate '{g}' missing")
for pair in (load_yaml(acc) or {}).get("proportionality", []) if os.path.exists(acc) else []:
    a, b = plans.get(pair["larger"]), plans.get(pair["smaller"])
    count += 1
    if a and b:
        if len(b["artefacts"]) >= len(a["artefacts"]):
            problems.append(f"proportionality: {pair['smaller']} should produce fewer artefacts than {pair['larger']}")
        if a["edition"]["id"] == b["edition"]["id"]:
            problems.append(f"proportionality: {pair['smaller']} and {pair['larger']} should land in different editions")
finish("Profiles, golden plans and acceptance", problems, count)

#!/usr/bin/env python3
"""The website's programme builder gives the same recommendation as scripts/tailor.py for every sample profile, and
its YAML output round-trips to a valid profile. Runs site/assets/programme-builder.js in Node.js (decision D14)."""
import json, os, shutil, subprocess, sys, glob, tempfile
from _common import path, load_yaml, programmes, editions, archetypes, departments, validate_schema, yaml, finish
import importlib.util

spec = importlib.util.spec_from_file_location("tailor", path("scripts", "tailor.py"))
tailor = importlib.util.module_from_spec(spec); spec.loader.exec_module(tailor)
problems, count = [], 0
node = shutil.which("node")
if not node:
    print("  WARN Node.js not found; programme builder not checked")
    sys.exit(0)
schema = json.load(open(path("profiles", "schema.json"), encoding="utf-8"))
D = {"schema": schema, "rules": load_yaml(path("data", "tailoring-rules.yaml")), "programmes": programmes(),
     "editions": editions(), "archetypes": archetypes(),
     "departments": {d["id"]: {"title": d["title"], "lead_role": d["lead_role"], "status": d["status"]} for d in departments()},
     "optional_facts": tailor.OPTIONAL_FACTS, "archetype_order": ["explorer", "adopter", "builder", "scaler", "ai-enterprise"]}
samples = sorted(glob.glob(path("profiles", "samples", "*.yaml")))
profiles = [load_yaml(f) for f in samples]
js = """
const b = require(process.argv[2]); const fs = require('fs');
const input = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
const out = input.profiles.map(p => { const r = b.plan(p, input.D);
  return {edition: r.edition.edition, archetype: r.archetype.archetype, overlay: r.overlay.overlay,
          signals: r.signals.map(s => s.signal), programmes: r.programmes, artefacts: r.artefacts.map(a => a.programme + '/' + a.artefact + '/' + a.depth),
          gates: r.gates.map(g => g.reviewer + '/' + g.stage), to_confirm: r.toConfirm, yaml: b.toYaml(p), errors: b.validate(p, input.D.schema)}; });
process.stdout.write(JSON.stringify(out));
"""
with tempfile.TemporaryDirectory() as tmp:
    runner, data = os.path.join(tmp, "run.js"), os.path.join(tmp, "in.json")
    open(runner, "w").write(js)
    json.dump({"profiles": profiles, "D": D}, open(data, "w"))
    res = subprocess.run([node, runner, path("site", "assets", "programme-builder.js"), data], capture_output=True, text=True)
if res.returncode != 0:
    problems.append("programme-builder.js failed in Node.js: " + res.stderr.strip()[:400])
else:
    for f, prof, js_out in zip(samples, profiles, json.loads(res.stdout)):
        count += 1
        py, _ = tailor.plan(f)
        name = os.path.basename(f)
        exp = {"edition": py["edition"]["id"], "archetype": py["archetype"]["id"], "overlay": py["assurance_overlay"]["id"],
               "signals": [s["signal"] for s in py["emerging_signals"]], "programmes": py["programmes"],
               "artefacts": [f"{a['programme']}/{a['artefact']}/{a['depth']}" for a in py["artefacts"]],
               "gates": [f"{g['reviewer']}/{g['stage']}" for g in py["reviewer_gates"]], "to_confirm": py["to_confirm"]}
        for k, v in exp.items():
            if js_out[k] != v:
                problems.append(f"{name}: builder {k} {js_out[k]} differs from tailor.py {v}")
        if js_out["errors"]:
            problems.append(f"{name}: builder validator reports {js_out['errors'][:3]}")
        back = yaml.safe_load(js_out["yaml"])
        if back != prof:
            problems.append(f"{name}: builder YAML does not round-trip to the same profile")
        if validate_schema(back, schema):
            problems.append(f"{name}: builder YAML is not valid against profiles/schema.json")
finish("Programme builder agrees with tailor.py", problems, count)

#!/usr/bin/env python3
"""Bundle the shared data the organisation-tailoring skills need into their references/ folders. --check verifies.

An installed plugin contains only its own folder, so the tailoring skills carry copies of the profile schema, rules,
catalogue and templates. The originals stay the source of truth. Only file types Microsoft 365 Copilot accepts in a
skill folder are used (.json, .yaml, .md).
"""
import json, os
from _common import (path, write_or_check, check_flag, finish, departments, programmes, templates, editions, archetypes,
                     GENERATED, yaml)

check, problems = check_flag(), []
base = "departments/organisation-tailoring/skills"
note = GENERATED.format(script="build-bundles.py")
schema = open(path("profiles", "schema.json"), encoding="utf-8").read()
rules = open(path("data", "tailoring-rules.yaml"), encoding="utf-8").read()
sample = open(path("profiles", "samples", "larkfield-services-scale.yaml"), encoding="utf-8").read()
cat = [{"id": d["id"], "title": d["title"], "layer": d["layer"], "reviewer": d.get("reviewer", False),
        "status": d["status"], "lead_role": d["lead_role"], "description": d["description"]} for d in departments()]
ed = {"about": note, "editions": editions(), "archetypes": archetypes()}
progs = {"about": note, "programmes": programmes()}
tpl = [f"<!-- {note} -->", "", "# CopilotForge templates (bundled)", ""]
for tid, f in templates().items():
    tpl += [f"<!-- template: {tid} -->", open(f, encoding="utf-8").read().rstrip(), "", "---", ""]
out = {
    "ai-profile-intake": {"profile-schema.json": schema, "sample-profile.yaml": f"# {note}\n" + sample},
    "edition-and-archetype": {"tailoring-rules.yaml": f"# {note}\n" + rules,
                              "editions-and-archetypes.json": json.dumps(ed, indent=2, sort_keys=True)},
    "ownership-map": {"departments.json": json.dumps({"about": note, "departments": cat}, indent=2)},
    "transformation-pack": {"programmes.json": json.dumps(progs, indent=2, sort_keys=True), "templates.md": "\n".join(tpl),
                            "tailoring-rules.yaml": f"# {note}\n" + rules},
}
n = 0
for skill, files in out.items():
    if not os.path.isdir(path(base, skill)):
        continue
    for name, content in files.items():
        n += 1
        write_or_check(f"{base}/{skill}/references/{name}", content, check, problems)
finish("Tailoring bundles", problems, n)

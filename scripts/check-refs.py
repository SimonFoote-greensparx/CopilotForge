#!/usr/bin/env python3
"""Every `department:skill` reference in skills, templates, programmes, scenarios and docs resolves (design brief 13)."""
import glob, re
from _common import skill_ids, department_index, programmes, templates, path, rel, REF, finish, load_yaml

ids, depts = skill_ids(), department_index()
problems, count = [], 0
files = (glob.glob(path("departments", "**", "*.md"), recursive=True) + glob.glob(path("reviewers", "**", "*.md"), recursive=True)
         + glob.glob(path("templates", "*.md")) + glob.glob(path("docs", "*.md")) + glob.glob(path("*.md")))
for f in files:
    if "/references/" in f:
        continue
    for m in REF.finditer(open(f, encoding="utf-8").read()):
        dep, sk = m.group(1), m.group(2)
        if dep not in depts:
            continue  # not a department reference (for example a URL scheme or a code token)
        count += 1
        if depts[dep]["status"] != "active":
            problems.append(f"{rel(f)}: `{dep}:{sk}` points into planned department '{dep}'; refer to the department by id until it is built")
        elif f"{dep}:{sk}" not in ids:
            problems.append(f"{rel(f)}: `{dep}:{sk}` does not resolve to a skill")
# Stale wording: a department described as planned, or as not yet built, once it is active.
STALE = re.compile(r"`([a-z0-9-]+)`(?: department)? \(planned\)|until (?:that|the `[a-z0-9-]+`) department is built|contract only")
for f in files:
    if "/references/" in f:
        continue
    for m in STALE.finditer(open(f, encoding="utf-8").read()):
        if m.group(1) is None or (m.group(1) in depts and depts[m.group(1)]["status"] == "active"):
            problems.append(f"{rel(f)}: stale wording '{m.group(0)}'; the department is built, so name the skill as `department:skill`")
tpl = templates()
for pid, p in programmes().items():
    for a in p.get("artefacts", []):
        count += 1
        if a["skill"] not in ids:
            problems.append(f"programmes/{pid}: artefact '{a['id']}' skill {a['skill']} does not resolve")
        if a["template"] not in tpl:
            problems.append(f"programmes/{pid}: artefact '{a['id']}' template '{a['template']}' is not in templates/")
for f in glob.glob(path("scenarios", "*.yaml")):
    sc = load_yaml(f)
    for step in sc.get("route", []):
        count += 1
        if step not in depts:
            problems.append(f"{rel(f)}: route step '{step}' is not a department")
    for sk in sc.get("skeleton_skills", []):
        count += 1
        if sk not in ids:
            problems.append(f"{rel(f)}: skeleton skill {sk} does not resolve")
cmap = load_yaml(path("data", "candidate-skill-map.yaml")) or {}
for dep, m in cmap.items():
    for cand, skill in (m or {}).items():
        count += 1
        if f"{dep}:{skill}" not in ids:
            problems.append(f"data/candidate-skill-map.yaml: {dep} candidate '{cand}' maps to {dep}:{skill}, which does not exist")
finish("References", problems, count)

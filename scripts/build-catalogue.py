#!/usr/bin/env python3
"""Emit catalogue/catalogue.json, docs/CATALOGUE.md and the generated tables in README.md and ROADMAP.md. --check verifies.

catalogue.json is the single data feed for the future website (decision D14), so site and repository cannot drift.
"""
import json, re
from _common import (departments, skills, programmes, templates, sources, department_root, rel, path, write_or_check,
                     check_flag, finish, GENERATED, PLUGIN_PREFIX, VERSION, load_yaml)

check, problems = check_flag(), []
sk = skills()
LAYERS = [("transformation", "A. Transformation"), ("adoption", "B. Adoption"), ("delivery", "C. Microsoft AI delivery"),
          ("assurance", "D. Assurance and operations"), ("spanning", "Spanning capabilities")]
cat = {"version": VERSION, "departments": [], "programmes": [], "templates": sorted(templates()),
       "sources": sorted(s["id"] for s in sources())}
for d in departments():
    mine = [s for s in sk if s["department"] == d["id"]]
    cat["departments"].append({
        "id": d["id"], "title": d["title"], "layer": d["layer"], "reviewer": d.get("reviewer", False),
        "status": d["status"], "phase": d["phase"], "lead_role": d["lead_role"], "description": d["description"],
        "plugin": PLUGIN_PREFIX + d["id"] if d["status"] == "active" else None,
        "path": rel(department_root(d)) if d["status"] == "active" else None,
        "skills": [{"id": f"{d['id']}:{s['folder']}", "name": s["folder"], "description": s["front"].get("description"),
                    **{k: s["front"].get("metadata", {}).get(k) for k in ("status", "lifecycle", "maturity", "risk-tiers",
                       "platforms", "edition-support", "reviewers", "sources")}} for s in mine],
        "candidate_skills": d.get("candidate_skills", []),
    })
for pid, p in programmes().items():
    cat["programmes"].append({"id": pid, "title": p["title"], "status": p["status"], "purpose": p["purpose"],
                              "artefacts": [a["id"] for a in p.get("artefacts", [])]})
write_or_check("catalogue/catalogue.json", json.dumps(cat, indent=2), check, problems)

def dept_table(rows_for):
    out = []
    for layer, label in LAYERS:
        ds = [d for d in cat["departments"] if d["layer"] == layer]
        out += [f"### {label}", "", "| Department | Status | Skills built | Purpose |", "|---|---|---|---|"]
        for d in ds:
            name = f"[`{d['id']}`]({d['path']}/README.md)" if d["path"] else f"`{d['id']}`"
            flag = " (reviewer)" if d["reviewer"] else ""
            out.append(f"| {name}{flag} | {d['status']} (phase {d['phase']}) | {len(d['skills'])} | {d['description']} |")
        out.append("")
    return out

lines = ["# Catalogue", "", f"<!-- {GENERATED.format(script='build-catalogue.py')} -->", "",
         f"{sum(1 for d in cat['departments'] if d['status']=='active')} of {len(cat['departments'])} departments active; "
         f"{len(sk)} skills; {len(cat['programmes'])} programmes; {len(cat['templates'])} templates; {len(cat['sources'])} source records.", ""]
lines += ["## Departments", ""] + dept_table(None)
lines += ["## Skills", ""]
for d in cat["departments"]:
    if not d["skills"]:
        continue
    lines += [f"### {d['title']}", "", "| Skill | Lifecycle | Editions | Reviewers | Description |", "|---|---|---|---|---|"]
    for s in d["skills"]:
        lines.append(f"| `{s['id']}` | {s['lifecycle']} | {s['edition-support']} | {s['reviewers']} | {s['description']} |")
    lines.append("")
lines += ["## Programmes", "", "| Programme | Status | Purpose | Artefacts |", "|---|---|---|---|"]
for p in cat["programmes"]:
    lines.append(f"| `{p['id']}` {p['title']} | {p['status']} | {p['purpose']} | {', '.join(p['artefacts'])} |")
lines += ["", "## Planned skills (backlog from the design brief)", ""]
for d in cat["departments"]:
    built = {s["name"] for s in d["skills"]}
    rest = [c for c in d["candidate_skills"] if c not in built]
    lines.append(f"- **{d['id']}**: {', '.join(rest)}")
write_or_check("docs/CATALOGUE.md", "\n".join(lines), check, problems)

def splice(file, tag, body):
    text = open(path(file), encoding="utf-8").read()
    block = f"<!-- BEGIN GENERATED: {tag} ({GENERATED.format(script='build-catalogue.py')}) -->\n" + body + f"\n<!-- END GENERATED: {tag} -->"
    pat = re.compile(rf"<!-- BEGIN GENERATED: {tag} .*?<!-- END GENERATED: {tag} -->", re.S)
    if not pat.search(text):
        problems.append(f"{file}: missing generated block markers for '{tag}'"); return
    write_or_check(file, pat.sub(lambda m: block, text), check, problems)

splice("README.md", "catalogue", "\n".join(dept_table(None)).rstrip())
status = ["| Department | Layer | Phase | Status |", "|---|---|---|---|"]
for d in sorted(cat["departments"], key=lambda d: (d["phase"], d["id"])):
    status.append(f"| `{d['id']}` | {d['layer']} | {d['phase']} | {d['status']} |")
splice("ROADMAP.md", "department-status", "\n".join(status))
finish("Catalogue", problems, len(cat["departments"]))

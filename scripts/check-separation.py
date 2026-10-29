#!/usr/bin/env python3
"""CopilotForge stays separate from D365Forge (decisions D1 and D9).

- No CopilotForge skill or plugin name collides with a D365Forge skill or plugin name, so both libraries can be
  installed side by side in Copilot Cowork.
- Plugin names carry the copilotforge- prefix and the marketplace is copilotforge.
- No file points installs, publishing or repository links at the D365Forge repository, marketplace or website, except
  the lineage files that credit it.
"""
import glob, json, os, re
from _common import ROOT, path, rel, load_toml, skills, departments, PLUGIN_PREFIX, MARKETPLACE, finish

reserved = load_toml(path("data", "reserved-names.toml"))["d365forge"]
problems, count = [], 0
for s in skills():
    count += 1
    if s["folder"] in reserved["skills"]:
        problems.append(f"{rel(s['path'])}: skill name '{s['folder']}' is already used by D365Forge; choose a distinct name")
for d in departments():
    count += 1
    if PLUGIN_PREFIX + d["id"] in reserved["plugins"]:
        problems.append(f"department '{d['id']}': plugin name collides with D365Forge")
for f in glob.glob(path("departments", "*", ".claude-plugin", "plugin.json")) + glob.glob(path("reviewers", "*", ".claude-plugin", "plugin.json")):
    name = json.load(open(f))["name"]
    if not name.startswith(PLUGIN_PREFIX):
        problems.append(f"{rel(f)}: plugin name '{name}' must start with '{PLUGIN_PREFIX}'")
mk = path(".claude-plugin", "marketplace.json")
if os.path.exists(mk) and json.load(open(mk))["name"] != MARKETPLACE:
    problems.append(".claude-plugin/marketplace.json: marketplace name must be 'copilotforge'")
LINEAGE = {"NOTICE.md", "README.md", "DECISIONS.md", "docs/LINEAGE.md", "ARCHITECTURE.md", "COWORK.md",
           "data/reserved-names.toml", "scripts/check-separation.py", "docs/STYLE-GUIDE.md", "CONTRIBUTING.md"}
BAD = re.compile(r"(?i)d365forge\.ai|github\.com/SimonFoote-greensparx/(D365Forge|dynamics-365-ce-roster)|@d365forge\b|R_kgDOVKseyA")
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in {".git", "dist", "input", "output", "__pycache__"}]
    for f in fn:
        p = os.path.join(dp, f); r = rel(p)
        if r in LINEAGE or os.path.splitext(f)[1] not in {".md", ".yaml", ".toml", ".json", ".py", ".sh", ".html", ".js", ".cff"}:
            continue
        count += 1
        if BAD.search(open(p, encoding="utf-8", errors="replace").read()):
            problems.append(f"{r}: refers to the D365Forge repository, marketplace or website; CopilotForge is a separate project")
finish("Separation from D365Forge", problems, count)

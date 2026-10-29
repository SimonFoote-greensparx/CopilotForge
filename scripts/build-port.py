#!/usr/bin/env python3
"""Emit each active department's plugin manifest and README, and the plugin marketplace. --check verifies.

Plugin names carry the copilotforge- prefix so CopilotForge and D365Forge plugins never collide (decision D9).
"""
import json, os
from _common import (active_departments, skills, department_root, rel, write_or_check, check_flag, finish, REPO_URL,
                     DISPLAY_NAME, MARKETPLACE, PLUGIN_PREFIX, VERSION, AUTHORS, GENERATED)

check, problems = check_flag(), []
all_skills = skills()
entries = []
for d in active_departments():
    root = rel(department_root(d))
    mine = [s for s in all_skills if s["department"] == d["id"]]
    manifest = {
        "name": PLUGIN_PREFIX + d["id"],
        "version": VERSION,
        "description": f"{DISPLAY_NAME} {d['title']}. {d['description']}",
        "author": {"name": AUTHORS},
        "homepage": REPO_URL,
        "repository": REPO_URL,
        "license": "CC-BY-4.0",
        "keywords": ["copilotforge", "microsoft-ai", d["layer"], d["id"]],
    }
    write_or_check(f"{root}/.claude-plugin/plugin.json", json.dumps(manifest, indent=2), check, problems)
    lines = [f"# {DISPLAY_NAME} - {d['title']}", "", f"<!-- {GENERATED.format(script='build-port.py')} -->", "",
             d["description"], "",
             f"- **Layer:** {d['layer']}" + (" (reviewer-class: may block)" if d.get("reviewer") else ""),
             f"- **Lead role:** {d['lead_role']}",
             f"- **Plugin name:** `{PLUGIN_PREFIX}{d['id']}`", "",
             "| Skill | Status | Lifecycle | Description |", "|---|---|---|---|"]
    for s in mine:
        md = s["front"].get("metadata", {})
        lines.append(f"| [`{s['folder']}`](skills/{s['folder']}/SKILL.md) | {md.get('status')} | {md.get('lifecycle')} | "
                     f"{s['front'].get('description', '').replace('|', '/')} |")
    built = {s["folder"] for s in mine}
    lines += ["", "## Credit", "",
              f"Created by {AUTHORS} as part of [{DISPLAY_NAME}]({REPO_URL}). Content is licensed under CC BY 4.0; keep the",
              "credit in each skill's `license` and `authors` fields when you share or adapt it. See NOTICE.md in the repository."]
    write_or_check(f"{root}/README.md", "\n".join(lines), check, problems)
    entries.append({"name": PLUGIN_PREFIX + d["id"], "source": f"./{root}", "description": manifest["description"],
                    "version": VERSION, "license": "CC-BY-4.0"})
market = {"name": MARKETPLACE, "owner": {"name": AUTHORS}, "metadata": {"description": f"{DISPLAY_NAME}: your Microsoft AI "
          "transformation team as installable AI skills.", "version": VERSION}, "plugins": entries}
write_or_check(".claude-plugin/marketplace.json", json.dumps(market, indent=2), check, problems)
finish("Plugin manifests and department READMEs", problems, len(entries))

#!/usr/bin/env python3
"""Templates are human-usable, keep their credit line, mark unknowns visibly and name the responsible skill (16.1)."""
import re
from _common import templates, skill_ids, rel, finish

CREDIT = ("Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), "
          "licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed "
          "document you may keep it as a footer or remove it.")
ids = skill_ids()
problems = []
for tid, f in templates().items():
    text = open(f, encoding="utf-8").read()
    where = rel(f)
    if not text.startswith("# "):
        problems.append(f"{where}: must start with a '# Title' heading")
    if text.rstrip().splitlines()[-1].strip("> ").strip() != CREDIT:
        problems.append(f"{where}: must end with the exact credit line in docs/STYLE-GUIDE.md")
    m = re.search(r"^Template id: `([a-z0-9-]+)`", text, re.M)
    if not m or m.group(1) != tid:
        problems.append(f"{where}: needs a line 'Template id: `{tid}`'")
    owners = re.findall(r"`([a-z0-9-]+:[a-z0-9-]+)`", text)
    if not owners:
        problems.append(f"{where}: must name the responsible skill as `department:skill`")
    for o in owners:
        if o not in ids:
            problems.append(f"{where}: responsible skill `{o}` does not resolve")
    if "[To confirm" not in text:
        problems.append(f"{where}: mark unknown facts as '[To confirm: ...]' so they are never invented")
finish("Templates", problems, len(templates()))

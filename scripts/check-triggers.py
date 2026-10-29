#!/usr/bin/env python3
"""Every skill has at least three positive and one negative trigger prompt; negatives name a real neighbour (13.1)."""
from _common import skills, triggers, skill_ids, active_departments, finish

ids = skill_ids()
suites = triggers()
problems, count = [], 0
active = {d["id"] for d in active_departments()}
for dep in suites:
    if dep not in active:
        problems.append(f"tests/triggers/{dep}.toml: '{dep}' is not an active department")
for s in skills():
    count += 1
    blocks = [b for b in suites.get(s["department"], []) if b.get("name") == s["folder"]]
    where = f"tests/triggers/{s['department']}.toml"
    if not blocks:
        problems.append(f"{where}: no [[skill]] block for '{s['folder']}'"); continue
    b = blocks[0]
    pos, neg = b.get("should_trigger", []), b.get("should_not_trigger", [])
    if len(pos) < 3:
        problems.append(f"{where}: '{s['folder']}' needs at least 3 should_trigger prompts")
    if len(neg) < 1:
        problems.append(f"{where}: '{s['folder']}' needs at least 1 should_not_trigger entry")
    for n in neg:
        exp = n.get("expected", "")
        if exp == f"{s['department']}:{s['folder']}":
            problems.append(f"{where}: '{s['folder']}' negative expects itself")
        elif exp not in ids and not (exp.endswith(":*") and exp[:-2]):
            problems.append(f"{where}: '{s['folder']}' negative expects '{exp}', which is not a skill (use department:* for a planned department)")
    if len(set(pos)) != len(pos):
        problems.append(f"{where}: '{s['folder']}' has duplicate prompts")
for dep, blocks in suites.items():
    for b in blocks:
        if f"{dep}:{b.get('name')}" not in ids:
            problems.append(f"tests/triggers/{dep}.toml: block '{b.get('name')}' has no matching skill")
finish("Trigger tests", problems, count)

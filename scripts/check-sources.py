#!/usr/bin/env python3
"""Source records are structured, unique and owned; volatile ones carry review metadata (design brief 14)."""
import datetime
from _common import sources, load_schema, validate_schema, department_index, skills, split_csv, finish

schema = load_schema("source")
depts = department_index()
problems, warnings, ids = [], [], set()
today = datetime.date.today()
MAX = {"high": 45, "medium": 120, "low": 400}
for s in sources():
    where = f"{s['_file']}:{s.get('id')}"
    for e in validate_schema(s, schema):
        problems.append(f"{where}: {e}")
    if s.get("id") in ids:
        problems.append(f"{where}: duplicate source id")
    ids.add(s.get("id"))
    for d in s.get("scope", {}).get("departments", []):
        if d not in depts:
            problems.append(f"{where}: unknown department '{d}'")
    fr = s.get("freshness", {})
    try:
        interval = int(fr.get("review_interval", "0d")[:-1])
        if interval > MAX.get(fr.get("volatility"), 400):
            problems.append(f"{where}: review_interval {interval}d is too long for {fr.get('volatility')} volatility (max {MAX[fr.get('volatility')]}d)")
        last = datetime.date.fromisoformat(fr.get("last_reviewed"))
        if (today - last).days > interval:
            warnings.append(f"{where}: review overdue (last reviewed {last}, interval {interval}d)")
    except Exception:
        pass
    if s.get("authority", {}).get("type") == "secondary" and not s["authority"].get("secondary_reason"):
        problems.append(f"{where}: secondary sources must say why no primary source is suitable")
used = set()
for sk in skills():
    for sid in split_csv(sk["front"].get("metadata", {}).get("sources")):
        used.add(sid)
for sid in ids - used:
    warnings.append(f"source '{sid}' is not cited by any skill yet")
finish("Source records", problems, len(ids), warnings)

#!/usr/bin/env python3
"""Every SKILL.md has valid frontmatter and the full section anatomy in docs/STYLE-GUIDE.md (design brief section 10).

Optional: pass one or more SKILL.md paths to check only those files.
"""
import re, sys
from _common import (skills, parse_skill, load_schema, validate_schema, department_index, split_csv, sections, word_count,
                     rel, SECTIONS, SCALE_SUBSECTIONS, SOURCES_PARAGRAPH, LIFECYCLE, EDITIONS, ARCHETYPES, RISK_TIERS,
                     PLATFORMS, finish, sources)

schema = load_schema("skill")
depts = department_index()
source_ids = {s["id"] for s in sources()}
reviewer_ids = {d for d, v in depts.items() if v.get("reviewer")}
only = [a for a in sys.argv[1:] if a.endswith("SKILL.md")]
problems, warnings, seen = [], [], {}
PLACEHOLDER = re.compile(r"<[a-z][^>\n]{0,60}>|\bTODO\b|\bTBC\b|\bTBD\b|lorem ipsum|\[add [^\]]*\]", re.I)
NA = re.compile(r"^\s*Not applicable\b", re.I)

for s in skills():
    if only and not any(s["path"].endswith(o.lstrip("./")) for o in only):
        continue
    where = rel(s["path"])
    fm, body = s["front"], s["body"]
    if not fm:
        problems.append(f"{where}: missing frontmatter"); continue
    for e in validate_schema(fm, schema):
        problems.append(f"{where}: frontmatter {e}")
    md = fm.get("metadata") or {}
    if fm.get("name") != s["folder"]:
        problems.append(f"{where}: name '{fm.get('name')}' must equal the folder name '{s['folder']}'")
    if md.get("department") != s["department"]:
        problems.append(f"{where}: metadata.department must be '{s['department']}'")
    if fm.get("name") in seen:
        problems.append(f"{where}: skill name '{fm.get('name')}' is already used by {seen[fm.get('name')]} (names are unique across the repository, decision D9)")
    seen[fm.get("name")] = where
    desc = fm.get("description", "")
    if "Use when" not in desc:
        problems.append(f"{where}: description must contain 'Use when' followed by concrete situations")
    for key, vocab in (("lifecycle", LIFECYCLE), ("maturity", ARCHETYPES), ("risk-tiers", RISK_TIERS),
                       ("platforms", PLATFORMS), ("edition-support", EDITIONS)):
        vals = split_csv(md.get(key))
        if not vals:
            problems.append(f"{where}: metadata.{key} is empty")
        for v in vals:
            if v not in vocab:
                problems.append(f"{where}: metadata.{key} value '{v}' is not in {vocab}")
    for r in split_csv(md.get("reviewers")):
        if r != "none" and r not in reviewer_ids:
            problems.append(f"{where}: metadata.reviewers '{r}' is not a reviewer-class department")
    for sid in split_csv(md.get("sources")):
        if sid != "none" and sid not in source_ids:
            problems.append(f"{where}: metadata.sources '{sid}' is not a source record in sources/*.toml")
    if not re.match(r"\s*# \S", body):
        problems.append(f"{where}: body must start with a '# Title' heading")
    secs = sections(body)
    top = [t for lvl, t, _ in secs if lvl == 2]
    if top != SECTIONS:
        missing = [x for x in SECTIONS if x not in top]
        extra = [x for x in top if x not in SECTIONS]
        problems.append(f"{where}: sections must be exactly, in order, {SECTIONS}"
                        + (f"; missing {missing}" if missing else "") + (f"; unexpected {extra}" if extra else "")
                        + ("" if missing or extra else "; order differs"))
        continue
    text = {t: x for lvl, t, x in secs if lvl == 2}
    subs = [t for lvl, t, _ in secs if lvl == 3]
    scale_subs = [t for t in subs if t in SCALE_SUBSECTIONS]
    if scale_subs != SCALE_SUBSECTIONS:
        problems.append(f"{where}: Scale notes must have ### Starter, ### Scale and ### Enterprise in that order")
    for title, content in text.items():
        if title == "Scale notes":
            continue
        if word_count(content) < 8 and not NA.match(content):
            problems.append(f"{where}: section '{title}' is empty or too thin; write it or start it with 'Not applicable' and a rationale")
        if NA.match(content) and word_count(content) < 6:
            problems.append(f"{where}: section '{title}' says Not applicable without a rationale")
    if PLACEHOLDER.search(body):
        problems.append(f"{where}: placeholder text found ({PLACEHOLDER.search(body).group(0)!r})")
    wc = word_count(text["Practitioner approach"])
    if not 250 <= wc <= 650:
        problems.append(f"{where}: Practitioner approach is {wc} words; it must be 250-650")
    if "Not this skill" in text["When to use"] or not re.search(r"`[a-z0-9-]+:[a-z0-9-]+`", text["When not to use"]):
        problems.append(f"{where}: 'When not to use' must name neighbouring skills as `department:skill`")
    q = re.findall(r"^\d+\. ", text["Questions to ask first"], re.M)
    if not 3 <= len(q) <= 6:
        problems.append(f"{where}: 'Questions to ask first' needs 3-6 numbered questions, found {len(q)}")
    if text["Sources"].strip() != SOURCES_PARAGRAPH:
        problems.append(f"{where}: 'Sources' must contain exactly the standard paragraph in docs/STYLE-GUIDE.md")
    if len(re.findall(r"^- ", text["Never"], re.M)) < 3:
        problems.append(f"{where}: 'Never' needs at least 3 bullets")
    if len(re.findall(r"^- ", text["Failure modes"], re.M)) < 3:
        problems.append(f"{where}: 'Failure modes' needs at least 3 bullets")
    gates = text["Reviewer gates"]
    if not NA.match(gates) and not re.search(r"`[a-z0-9-]+`|`[a-z0-9-]+:[a-z0-9-]+`", gates):
        problems.append(f"{where}: 'Reviewer gates' must name reviewer departments in backticks or say Not applicable with a rationale")
    if s["department"] in reviewer_ids and not re.search(r"\bblocking\b", body, re.I):
        problems.append(f"{where}: reviewer-class skills must classify findings as blocking or advisory")
    if md.get("status") != "draft":
        warnings.append(f"{where}: status is '{md.get('status')}'; only Simon Foote moves a skill past draft")

finish("Skill anatomy", problems, len(seen))

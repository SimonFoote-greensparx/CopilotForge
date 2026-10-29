#!/usr/bin/env python3
"""Emit each skill's references/sources.md and the generated summary in SOURCES.md from sources/*.toml. --check verifies."""
import re
from _common import (skills, sources, split_csv, rel, path, write_or_check, check_flag, finish, REPO_URL, DISPLAY_NAME,
                     AUTHORS, GENERATED)

check, problems = check_flag(), []
recs = {s["id"]: s for s in sources()}
USAGE = {"cite-only": "Read and cite. Summarise in your own words; do not reproduce the text.",
         "quote-with-attribution": "Short quotations with attribution are permitted; otherwise summarise.",
         "open-licence": "Openly licensed. Reuse is permitted under the stated licence, with attribution."}
for s in skills():
    ids = [i for i in split_csv(s["front"].get("metadata", {}).get("sources")) if i != "none"]
    folder = rel(s["path"]).rsplit("/", 1)[0]
    lines = [f"# Sources for `{s['department']}:{s['folder']}`", "", GENERATED.format(script="build-sources.py"), ""]
    if not ids:
        lines += ["This skill relies on durable practitioner judgement and cites no product source records.", ""]
    for i in ids:
        r = recs.get(i)
        if not r:
            continue
        a, f, u = r["authority"], r["freshness"], r["usage"]
        lines += [f"## {r['name']}", "", f"- Source id: `{r['id']}`", f"- Publisher: {a['publisher']} ({a['type']})",
                  f"- Link: {r['url']}", f"- Authoritative for: {a['authoritative_for']}",
                  f"- Volatility: {f['volatility']}; review every {f['review_interval']}; last reviewed {f['last_reviewed']}",
                  f"- What you may do: {USAGE[u['classification']]}", ""]
    lines += ["## Credit", "", f"This skill was created by {AUTHORS} as part of [{DISPLAY_NAME}]({REPO_URL}), licensed under",
              "CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Credit the author when you share or adapt it."]
    write_or_check(f"{folder}/references/sources.md", "\n".join(lines), check, problems)

# Generated summary inside SOURCES.md, between markers.
rows = ["| Source id | Name | Publisher | Volatility | Review | Last reviewed | Usage |", "|---|---|---|---|---|---|---|"]
for r in sorted(recs.values(), key=lambda r: r["id"]):
    rows.append(f"| `{r['id']}` | [{r['name']}]({r['url']}) | {r['authority']['publisher']} | {r['freshness']['volatility']} | "
                f"{r['freshness']['review_interval']} | {r['freshness']['last_reviewed']} | {r['usage']['classification']} |")
p = path("SOURCES.md")
text = open(p, encoding="utf-8").read()
block = f"<!-- BEGIN GENERATED: sources ({GENERATED.format(script='build-sources.py')}) -->\n" + "\n".join(rows) + "\n<!-- END GENERATED: sources -->"
new = re.sub(r"<!-- BEGIN GENERATED: sources.*?<!-- END GENERATED: sources -->", lambda m: block, text, flags=re.S)
write_or_check("SOURCES.md", new, check, problems)
finish("Source files", problems, len(recs))

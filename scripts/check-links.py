#!/usr/bin/env python3
"""Check that every source record URL answers (design brief 13, Sources). Needs network access, so it runs in the
weekly links workflow rather than in check-all.sh."""
import urllib.request
from _common import sources, finish

problems = []
for s in sources():
    req = urllib.request.Request(s["url"], method="GET", headers={"User-Agent": "CopilotForge link check"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            if r.status >= 400:
                problems.append(f"{s['id']}: HTTP {r.status} for {s['url']}")
    except Exception as e:  # noqa: BLE001
        problems.append(f"{s['id']}: {e} for {s['url']}")
finish("Source links", problems, len(sources()))

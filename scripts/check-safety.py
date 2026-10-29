#!/usr/bin/env python3
"""Repository safety scan (design brief 12.2 and 13): no credentials, no personal contact data, no real organisation
data, no client or employer material, no third-party licence text outside the licence files."""
import glob, os, re, subprocess
from _common import ROOT, path, rel, finish

SKIP_DIRS = {".git", "dist", "input", "output", "__pycache__"}
SKIP_FILES = {"LICENSE", "LICENSE-CODE"}
PATTERNS = [
    (re.compile(r"(?i)(api[_-]?key|secret|password|client[_-]?secret)\s*[:=]\s*['\"][^'\"\s]{8,}"), "possible credential"),
    (re.compile(r"ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}"), "GitHub token"),
    (re.compile(r"AKIA[0-9A-Z]{16}"), "AWS key"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "private key"),
    (re.compile(r"(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"), "GUID (tenant, client or object id?)"),
    (re.compile(r"\b(?:\+44\s?7\d{3}|\(?07\d{3}\)?)\s?\d{3}\s?\d{3}\b"), "UK mobile number"),
]
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
ALLOWED_EMAIL_FILES = {"SECURITY.md", "CODE_OF_CONDUCT.md"}
# Names of real organisations whose internal material informed the brief. Reusable methods are generalised; the
# names stay out of skills, templates, programmes and samples (decision D11). Lineage files may name them.
RESTRICTED_NAMES = re.compile(r"(?i)\bworkwell\b")
LINEAGE_FILES = {"DECISIONS.md", "docs/LINEAGE.md", "scripts/check-safety.py"}
TEXT_EXT = {".md", ".yaml", ".yml", ".toml", ".json", ".py", ".sh", ".txt", ".html", ".css", ".js", ".cff"}
problems, count = [], 0
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in SKIP_DIRS]
    for f in fn:
        p = os.path.join(dp, f)
        r = rel(p)
        if f in SKIP_FILES or os.path.splitext(f)[1] not in TEXT_EXT:
            continue
        count += 1
        text = open(p, encoding="utf-8", errors="replace").read()
        for pat, label in PATTERNS:
            if pat.search(text):
                problems.append(f"{r}: {label}")
        if r not in ALLOWED_EMAIL_FILES and r not in LINEAGE_FILES:
            for m in EMAIL.finditer(text):
                if not m.group(0).endswith(("@example.com", "@example.org", "@users.noreply.github.com")):
                    problems.append(f"{r}: email address {m.group(0)}")
        if r not in LINEAGE_FILES and RESTRICTED_NAMES.search(text):
            problems.append(f"{r}: names a source organisation; generalise the method (decision D11)")
        if r not in LINEAGE_FILES and "Creative Commons Corporation" in text:
            problems.append(f"{r}: contains licence legal text outside LICENSE")
# Nothing from input/ or output/ is tracked other than their README files.
for folder in ("input", "output"):
    for p in glob.glob(path(folder, "**", "*"), recursive=True):
        if os.path.isfile(p) and os.path.basename(p) != "README.md":
            if subprocess.run(["git", "-C", ROOT, "ls-files", "--error-unmatch", rel(p)], capture_output=True).returncode == 0:
                problems.append(f"{rel(p)} is tracked; organisation data never belongs in the repository")
finish("Safety scan", problems, count)

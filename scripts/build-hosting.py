#!/usr/bin/env python3
"""Build the website as a self-contained static site for professional web hosting (decision D14).

    python3 scripts/build-hosting.py [--site-url https://copilotforge.ai/] [--github-links]

Writes dist/website/ and dist/copilotforge-website.zip (dist/ is git-ignored). Unzip the archive into the web root,
for example public_html. See docs/HOSTING.md. The core pages come from site/ (scripts/build-site.py); this script adds
a page for every guide, department, skill, template and programme, the credit notice, a downloads area with the Copilot
Cowork plugins, single skills and sample profiles, the licence texts, 404, .htaccess, robots.txt and sitemap.xml, then
checks every local link and image resolves. Run `bash scripts/build-all.sh` first so generated files are current.
"""
from __future__ import annotations

import argparse, html, os, posixpath, re, shutil, zipfile
from _common import (ROOT, path, departments, skills, programmes, templates, finish, REPO_URL, DISPLAY_NAME, VERSION,
                     PLUGIN_PREFIX, department_root, rel as relpath, split_csv, editions)
from _site import SITE_URL, GITHUB_LINKS, site_page, unlinked_repo_mentions, AUTHOR_LINE
import _markdown as md

ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
ap.add_argument("--site-url", default=SITE_URL)
ap.add_argument("--github-links", dest="github_links", action="store_true", default=GITHUB_LINKS,
                help="Link repository-only references to GitHub (only once the repository is public)")
ap.add_argument("--out", default=path("dist", "website"))
ap.add_argument("--zip", default=path("dist", "copilotforge-website.zip"))
opts = ap.parse_args()
SITE = opts.site_url.rstrip("/") + "/"
OUT = opts.out
GEN = "scripts/build-hosting.py"
e = html.escape
problems: list[str] = []
depts, all_skills, progs, tpls = departments(), skills(), programmes(), templates()
active = [d for d in depts if d["status"] == "active"]
dept_by_id = {d["id"]: d for d in depts}
skill_ids = {f"{s['department']}:{s['folder']}" for s in all_skills}
FIXED = (2026, 1, 1, 0, 0, 0)

GUIDES = {"docs/COPILOT-COWORK.md": "guides/copilot-cowork.html", "cowork/custom-instructions.md": "guides/custom-instructions.html",
          "ROADMAP.md": "guides/roadmap.html", "SOURCES.md": "guides/sources.html", "docs/STYLE-GUIDE.md": "guides/style-guide.html",
          "CONTRIBUTING.md": "guides/contributing.html", "ARCHITECTURE.md": "guides/architecture.html",
          "DECISIONS.md": "guides/decisions.html", "docs/HOSTING.md": "guides/hosting.html", "NOTICE.md": "credit.html",
          "docs/CATALOGUE.md": "catalogue.html", "templates/README.md": "templates.html", "profiles/README.md": "downloads.html#profiles"}
GUIDE_ACTIVE = {"docs/COPILOT-COWORK.md": "Copilot Cowork", "cowork/custom-instructions.md": "Copilot Cowork"}
FIXED_MAP = {**GUIDES, "README.md": "index.html", "AUTHORS.md": "author.html", "LICENSE": "LICENSE.txt",
             "LICENSE-CODE": "LICENSE-CODE.txt", "CITATION.cff": "downloads/CITATION.cff", "cowork/README.md": "downloads.html",
             "cowork/plugins": "downloads.html", "cowork": "downloads.html", "templates": "templates.html",
             "programmes": "programmes.html", "departments": "catalogue.html", "reviewers": "catalogue.html",
             "profiles/schema.json": "downloads/profiles/schema.json", "profiles/samples": "downloads.html#profiles",
             "COWORK.md": "guides/architecture.html"}


def hosted(p: str) -> str | None:
    p = p.strip("/")
    if p in FIXED_MAP:
        return FIXED_MAP[p]
    m = re.fullmatch(r"(?:departments|reviewers)/([a-z0-9-]+)(/README\.md)?", p)
    if m and m.group(1) in dept_by_id:
        return f"departments/{m.group(1)}.html"
    m = re.fullmatch(r"(?:departments|reviewers)/([a-z0-9-]+)/skills/([a-z0-9-]+)(/SKILL\.md)?", p)
    if m:
        return f"skills/{m.group(1)}/{m.group(2)}.html"
    m = re.fullmatch(r"(?:departments|reviewers)/([a-z0-9-]+)/skills/([a-z0-9-]+)/references/sources\.md", p)
    if m:
        return f"skills/{m.group(1)}/{m.group(2)}.html#sources"
    m = re.fullmatch(r"templates/([a-z0-9-]+)\.md", p)
    if m:
        return f"templates/{m.group(1)}.html"
    m = re.fullmatch(r"programmes/([a-z0-9-]+)(/programme\.yaml)?", p)
    if m:
        return f"programmes/{m.group(1)}.html"
    m = re.fullmatch(r"cowork/plugins/([a-z0-9-]+)\.zip", p)
    if m:
        return f"downloads/{m.group(1)}.zip"
    m = re.fullmatch(r"profiles/samples/([a-z0-9-]+\.yaml)", p)
    if m:
        return f"downloads/profiles/{m.group(1)}"
    return None


def site_rel(target: str, page: str) -> str:
    t, _, frag = target.partition("#")
    r = posixpath.relpath(t, posixpath.dirname(page) or ".") if t else posixpath.basename(page)
    return r + ("#" + frag if frag else "")


def github(repo_path: str) -> str:
    kind = "blob" if "." in posixpath.basename(repo_path) else "tree"
    return f"{REPO_URL}/{kind}/main/{repo_path}".rstrip("/")


dropped: dict[str, int] = {}


def resolve(href: str, page: str, source: str | None) -> str | None:
    if href.startswith(("#", "mailto:")):
        return href
    if href.startswith(REPO_URL) and href.rstrip("/") == REPO_URL or isinstance(href, md.BareURL) and href.startswith(REPO_URL):
        if opts.github_links:
            return str(href)
        dropped[str(href)] = dropped.get(str(href), 0) + 1
        return None
    repo_path = None
    for prefix in (REPO_URL + "/blob/main/", REPO_URL + "/tree/main/"):
        if href.startswith(prefix):
            repo_path = href[len(prefix):]
    if href.startswith(SITE_URL):
        return SITE + href[len(SITE_URL):]
    if repo_path is None and not re.match(r"^[a-z]+:", href):
        if source is None:
            return href
        target, _, frag = href.partition("#")
        repo_path = posixpath.normpath(posixpath.join(posixpath.dirname(source), target)) + ("#" + frag if frag else "")
    if repo_path is None:
        return href
    target, _, frag = repo_path.partition("#")
    site = hosted(target)
    if site is not None:
        if frag and "#" not in site:
            site += "#" + frag
        return site_rel(site, page)
    if opts.github_links:
        return github(target) + ("#" + frag if frag else "")
    dropped[target] = dropped.get(target, 0) + 1
    return None


CODE_REF = re.compile(r"<code>([a-z0-9-]+):([a-z0-9-]+)</code>")
CODE_TPL = re.compile(r"<code>([a-z0-9-]+)</code>")


def crosslink(fragment: str, page: str) -> str:
    """Turn `department:skill` and template ids written as code into links to their pages."""
    def ref(m):
        sid = f"{m.group(1)}:{m.group(2)}"
        if sid in skill_ids:
            return f'<a href="{site_rel(f"skills/{m.group(1)}/{m.group(2)}.html", page)}">{m.group(0)}</a>'
        return m.group(0)

    def tpl(m):
        if m.group(1) in tpls:
            return f'<a href="{site_rel(f"templates/{m.group(1)}.html", page)}">{m.group(0)}</a>'
        if m.group(1) in dept_by_id and dept_by_id[m.group(1)]["status"] == "active":
            return f'<a href="{site_rel(f"departments/{m.group(1)}.html", page)}">{m.group(0)}</a>'
        return m.group(0)
    parts = re.split(r"(<a\b.*?</a>|<pre\b.*?</pre>)", fragment, flags=re.S)
    return "".join(p if p.startswith(("<a", "<pre")) else CODE_TPL.sub(tpl, CODE_REF.sub(ref, p)) for p in parts)


def render_md(text: str, page: str, source: str) -> str:
    return crosslink(md.render(text, lambda h: resolve(h, page, source)).replace(SITE_URL, SITE), page)


def root_of(page: str) -> str:
    return "../" * page.count("/")


pages: dict[str, str] = {}


def add_page(site_path: str, title: str, body: str, active_nav: str = "") -> None:
    pages[site_path] = site_page(title, body, active_nav, root=root_of(site_path), github_links=opts.github_links,
                                 generator=GEN)


def read(r: str) -> str:
    return open(path(r), encoding="utf-8").read()


def facts(items) -> str:
    return '<dl class="facts">' + "".join(f"<dt>{e(k)}</dt><dd>{v}</dd>" for k, v in items) + "</dl>"


def cowork_link(did: str, page: str) -> str:
    return f'<a href="{site_rel(f"downloads/{PLUGIN_PREFIX}{did}.zip", page)}" download>{e(dept_by_id[did]["title"])} plugin for Copilot Cowork</a>'


# ------------------------------------------------------------------ core pages from site/
for name in sorted(os.listdir(path("site"))):
    if not name.endswith(".html"):
        continue
    src = read(f"site/{name}")
    title = html.unescape(re.search(r"<title>(.*?) \| ", src).group(1))
    act = re.search(r'class="active">([^<]+)</a>', src)
    body = src[src.index('<main class="wrap">\n') + len('<main class="wrap">\n'):src.rindex("\n</main>")]
    add_page(name, title, body, act.group(1) if act else "")

# ------------------------------------------------------------------ guides and credit
for r, site in GUIDES.items():
    if "#" in site or site in ("catalogue.html", "templates.html"):
        continue
    _, text = md.strip_frontmatter(read(r))
    text = re.sub(r"<!-- (BEGIN|END) GENERATED[^>]*-->\n?", "", text)
    m = re.search(r"^# (.+)$", text, re.M)
    t = re.sub(r"[`*]", "", m.group(1)) if m else r
    body = render_md(text, site, r)
    if r == "docs/COPILOT-COWORK.md":
        body = (f'<div class="notice">Download the plugins from the <a href="{site_rel("downloads.html", site)}">downloads page</a>. '
                "The steps below say where to upload them.</div>\n") + body
    add_page(site, t, body, GUIDE_ACTIVE.get(r, ""))

# ------------------------------------------------------------------ departments
for d in active:
    did = d["id"]
    site = f"departments/{did}.html"
    r = relpath(os.path.join(department_root(d), "README.md"))
    _, text = md.strip_frontmatter(read(r))
    text = re.sub(r"<!-- Generated[^>]*-->\n?", "", text)
    box = (f'<div class="callout"><strong>Use it in Copilot Cowork:</strong> download the {cowork_link(did, site)} '
           f'and upload it under <em>Customize</em> &gt; <em>Plugins</em> &gt; <em>Upload plugin</em>. '
           f'<a href="{site_rel("guides/copilot-cowork.html", site)}">How to install</a>.</div>')
    crumbs = f'<p class="crumbs"><a href="{site_rel("catalogue.html", site)}">Catalogue</a> &rsaquo; {e(d["title"])}</p>'
    add_page(site, d["title"], crumbs + render_md(text, site, r).replace("</h1>", "</h1>\n" + box, 1), "Catalogue")

# ------------------------------------------------------------------ skills
for s in all_skills:
    did, name = s["department"], s["folder"]
    site = f"skills/{did}/{name}.html"
    r = relpath(s["path"])
    meta = s["front"].get("metadata", {})
    reviewers = [x for x in split_csv(meta.get("reviewers")) if x != "none"]
    fx = facts([
        ("Department", f'<a href="{site_rel(f"departments/{did}.html", site)}">{e(dept_by_id[did]["title"])}</a>'),
        ("Lifecycle", e(meta.get("lifecycle", ""))), ("Maturity", e(meta.get("maturity", ""))),
        ("Risk tiers", e(meta.get("risk-tiers", ""))), ("Platforms", e(meta.get("platforms", ""))),
        ("Editions", e(meta.get("edition-support", ""))), ("Reviewers", e(", ".join(reviewers) or "none")),
        ("Status", f'<span class="status {e(meta.get("status", ""))}">{e(meta.get("status", ""))}</span>'),
        ("Copilot Cowork", f"{cowork_link(did, site)}, or this skill on its own: "
                           f'<a href="{site_rel(f"downloads/skills/{did}/{name}/SKILL.md", site)}" download>Download SKILL.md</a>'),
        ("Licence", f'<a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>, by {e(str(meta.get("authors", "")))}'),
    ])
    crumbs = (f'<p class="crumbs"><a href="{site_rel("catalogue.html", site)}">Catalogue</a> &rsaquo; '
              f'<a href="{site_rel(f"departments/{did}.html", site)}">{e(dept_by_id[did]["title"])}</a> &rsaquo; {e(name)}</p>')
    body = render_md(s["body"], site, r).replace("</h1>", "</h1>\n" + f'<p class="lead">{e(s["front"].get("description", ""))}</p>' + fx, 1)
    sources_rel = r.replace("SKILL.md", "references/sources.md")
    if os.path.exists(path(sources_rel)):
        stext = read(sources_rel)
        stext = re.sub(r"^# .*\n", "", stext, count=1)
        stext = re.sub(r"^Generated by .*\n", "", stext, flags=re.M)
        stext = re.sub(r"^## ", "### ", stext, flags=re.M)
        body += f'\n<section id="sources" class="sources"><h2>Source records for this skill</h2>{render_md(stext, site, sources_rel)}</section>'
    add_page(site, f"{name} ({dept_by_id[did]['title']})", crumbs + body, "Catalogue")

# ------------------------------------------------------------------ templates
for tid, f in tpls.items():
    site = f"templates/{tid}.html"
    r = relpath(f)
    text = read(r)
    m = re.search(r"^# (.+)$", text, re.M)
    t = m.group(1).strip() if m else tid
    crumbs = f'<p class="crumbs"><a href="{site_rel("templates.html", site)}">Templates</a> &rsaquo; {e(t)}</p>'
    dl = f'<p><a class="btn ghost" href="{site_rel(f"downloads/templates/{tid}.md", site)}" download>Download the template (Markdown)</a></p>'
    add_page(site, t, crumbs + render_md(text, site, r) + dl, "Templates")

# ------------------------------------------------------------------ programmes
for pid, p in progs.items():
    site = f"programmes/{pid}.html"
    rows = "".join(
        f'<tr><td>{e(a["title"])}</td><td>{e(a["stage"])}</td><td><a href="{site_rel("skills/" + a["skill"].replace(":", "/") + ".html", site)}"><code>{e(a["skill"])}</code></a></td>'
        f'<td><a href="{site_rel(f"templates/{a["template"]}.html", site)}"><code>{e(a["template"])}</code></a></td>'
        f'<td>{e(a["depth"]["starter"])}</td><td>{e(a["depth"]["scale"])}</td><td>{e(a["depth"]["enterprise"])}</td></tr>' for a in p.get("artefacts", []))
    inc = "".join(f'<li><a href="{site_rel(f"programmes/{i["programme"]}.html", site)}">{e(progs[i["programme"]]["title"])}</a>'
                  + (" - when staff are already building agents, or the organisation is a Builder or beyond" if i.get("when") else "") + "</li>"
                  for i in p.get("includes", []))
    gates = "".join(f'<li><code>{e(g["reviewer"])}</code> at {e(g["stage"])} from risk tier {g["from_risk_tier"]}; blocking, cannot be skipped'
                    + ("" if dept_by_id[g["reviewer"]]["status"] == "active" else " (contract only until the department is built)") + "</li>"
                    for g in p.get("gates", []))
    planned = ", ".join(f"<code>{e(x)}</code>" for x in p.get("planned_departments", []))
    subs = "".join(f"<li>{e(v)}</li>" for v in (p.get("starter_substitutions") or {}).values())
    body = (f'<p class="crumbs"><a href="{site_rel("programmes.html", site)}">Programmes</a> &rsaquo; {e(p["title"])}</p>'
            f'<h1>{e(p["title"])}</h1><p class="lead">{e(p["purpose"])}</p>'
            + facts([("Status", e(p["status"])), ("Lifecycle", e(", ".join(p.get("lifecycle", []))))])
            + (f"<h2>Includes</h2><ul>{inc}</ul>" if inc else "")
            + (f'<h2>Artefacts</h2><div class="table-wrap"><table class="grid"><thead><tr><th>Artefact</th><th>Stage</th><th>Responsible skill</th><th>Template</th><th>Starter</th><th>Scale</th><th>Enterprise</th></tr></thead><tbody>{rows}</tbody></table></div>' if rows else "")
            + (f"<h2>Starter edition</h2><ul>{subs}</ul>" if subs else "")
            + (f"<h2>Reviewer gates</h2><ul>{gates}</ul>" if gates else "")
            + (f"<h2>Departments still to be built</h2><p>{planned}</p>" if planned else ""))
    add_page(site, p["title"], crosslink(body, site), "Programmes")

# ------------------------------------------------------------------ downloads
site = "downloads.html"
rows = []
for d in active:
    did = d["id"]
    z = path("cowork", "plugins", f"{PLUGIN_PREFIX}{did}.zip")
    if not os.path.exists(z):
        problems.append(f"cowork/plugins/{PLUGIN_PREFIX}{did}.zip missing; run bash scripts/build-all.sh")
        continue
    n = sum(1 for s in all_skills if s["department"] == did)
    rows.append(f'<tr><td><a href="departments/{did}.html">{e(d["title"])}</a></td><td><code>{PLUGIN_PREFIX}{did}</code></td><td>{n}</td>'
                f'<td>{max(1, os.path.getsize(z) // 1024)} KB</td><td><a href="downloads/{PLUGIN_PREFIX}{did}.zip" download>Download</a></td></tr>')
samples = sorted(f for f in os.listdir(path("profiles", "samples")) if f.endswith(".yaml"))
downloads = f"""<h1>Install {DISPLAY_NAME}</h1>
<p class="lead">Everything you need to use {DISPLAY_NAME} in Microsoft Copilot Cowork, version {VERSION}. Each department is one plugin; download only the ones you need.</p>
<h2>Copilot Cowork plugins</h2>
<p>In Copilot Cowork, select <em>Customize</em> &gt; <em>Plugins</em> &gt; <em>Upload plugin</em> and choose an archive. Cowork converts it into a plugin with its skills. The <a href="guides/copilot-cowork.html">Copilot Cowork guide</a> covers single skills, sharing and updates, and the <a href="guides/custom-instructions.html">suggested custom instructions</a> help Cowork use the skills well. Every plugin name starts with <code>{PLUGIN_PREFIX}</code>, so the plugins sit alongside other skill libraries without clashing.</p>
<div class="table-wrap"><table class="grid"><thead><tr><th>Department</th><th>Plugin name</th><th>Skills</th><th>Size</th><th>Download</th></tr></thead>
<tbody>{"".join(rows)}</tbody></table></div>
<p>To design a whole Microsoft AI programme, install all of them. Each skill page also offers its <code>SKILL.md</code> on its own.</p>
<h2 id="profiles">Organisation profiles</h2>
<p>The organisation-tailoring department turns an organisation profile into a recommended edition, archetype, programme and transformation pack. Build one with the <a href="programme-builder.html">programme builder</a>, or start from a fictional sample:</p>
<ul>{"".join(f'<li><a href="downloads/profiles/{e(f)}" download>{e(f)}</a></li>' for f in samples)}
<li><a href="downloads/profiles/schema.json" download>schema.json</a> (the profile format)</li></ul>
<h2>Credit and citation</h2>
<p>The plugins, skills and templates are licensed under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a> (<a href="LICENSE.txt">licence text</a>); the code under MIT (<a href="LICENSE-CODE.txt">licence text</a>). When you share or adapt them, credit {AUTHOR_LINE} as described on the <a href="credit.html">credit page</a>. <a href="downloads/CITATION.cff" download>CITATION.cff</a> holds the citation details.</p>"""
add_page(site, "Downloads", downloads, "Downloads")

notfound = site_page("Page not found", """<h1>Page not found</h1>
<p class="lead">That page does not exist or has moved.</p>
<p>Try the <a href="/catalogue.html">catalogue</a>, the <a href="/programmes.html">programmes</a> or the
<a href="/downloads.html">downloads</a>, or go back to the <a href="/index.html">home page</a>.</p>""",
                     "", root="/", github_links=opts.github_links, generator=GEN)
pages["404.html"] = notfound

# ------------------------------------------------------------------ write
if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)


def put(r: str, data) -> None:
    dest = os.path.join(OUT, r)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as fh:
        fh.write(data.encode("utf-8") if isinstance(data, str) else data)


for r, content in pages.items():
    put(r, content)
for dirpath, _, files in os.walk(path("site", "assets")):
    for f in files:
        full = os.path.join(dirpath, f)
        put(os.path.relpath(full, path("site")).replace(os.sep, "/"), open(full, "rb").read())
for d in active:
    z = path("cowork", "plugins", f"{PLUGIN_PREFIX}{d['id']}.zip")
    if os.path.exists(z):
        put(f"downloads/{PLUGIN_PREFIX}{d['id']}.zip", open(z, "rb").read())
for f in samples:
    put(f"downloads/profiles/{f}", open(path("profiles", "samples", f), "rb").read())
put("downloads/profiles/schema.json", open(path("profiles", "schema.json"), "rb").read())
for s in all_skills:
    put(f"downloads/skills/{s['department']}/{s['folder']}/SKILL.md", open(s["path"], "rb").read())
for tid, f in tpls.items():
    put(f"downloads/templates/{tid}.md", open(f, "rb").read())
put("downloads/CITATION.cff", open(path("CITATION.cff"), "rb").read())
put("LICENSE.txt", open(path("LICENSE"), "rb").read())
put("LICENSE-CODE.txt", open(path("LICENSE-CODE"), "rb").read())
put(".htaccess", f"""# {DISPLAY_NAME} website. Generated by {GEN}. Static files only; works on Apache and LiteSpeed hosting.
Options -Indexes
DirectoryIndex index.html
ErrorDocument 404 /404.html
AddDefaultCharset utf-8
AddType application/zip .zip
AddType text/plain .cff .yaml
AddType text/markdown .md
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteCond %{{HTTPS}} off
  RewriteRule ^ https://%{{HTTP_HOST}}%{{REQUEST_URI}} [L,R=301]
</IfModule>
<IfModule mod_headers.c>
  <FilesMatch "\\.(zip|cff|yaml|md)$">
    Header set Content-Disposition attachment
  </FilesMatch>
  Header always set X-Content-Type-Options "nosniff"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  Header always set X-Frame-Options "SAMEORIGIN"
</IfModule>
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/html "access plus 0 seconds"
  ExpiresByType text/css "access plus 7 days"
  ExpiresByType image/jpeg "access plus 30 days"
</IfModule>
""")
urls = sorted(p for p in pages if p != "404.html")
put("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{e(SITE + ('' if p == 'index.html' else p))}</loc></url>\n" for p in urls) + "</urlset>\n")
put("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")

# ------------------------------------------------------------------ link check
for r in pages:
    if r == "404.html":
        continue
    for m in re.finditer(r'(?:href|src)="([^"]+)"', pages[r]):
        h = html.unescape(m.group(1))
        if re.match(r"^[a-z]+:", h) or h.startswith(("#", "/")):
            continue
        target = posixpath.normpath(posixpath.join(posixpath.dirname(r), h.partition("#")[0]))
        if not os.path.exists(os.path.join(OUT, target)):
            problems.append(f"{r}: broken link {h}")
for r, content in pages.items():
    if f'href="{REPO_URL}' in content and not opts.github_links:
        problems.append(f"{r}: links to GitHub although GitHub links are off")
    if opts.github_links:
        for url in unlinked_repo_mentions(content):
            problems.append(f"{r}: the repository address {url} is shown but not linked")

os.makedirs(os.path.dirname(opts.zip), exist_ok=True)
names = []
for dirpath, _, files in os.walk(OUT):
    for f in files:
        names.append(os.path.relpath(os.path.join(dirpath, f), OUT).replace(os.sep, "/"))
with zipfile.ZipFile(opts.zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for n in sorted(names):
        info = zipfile.ZipInfo(n, date_time=FIXED)
        info.external_attr = 0o644 << 16
        info.compress_type = zipfile.ZIP_DEFLATED
        z.writestr(info, open(os.path.join(OUT, n), "rb").read())
print(f"  {len(pages)} pages, {len(names)} files, {os.path.getsize(opts.zip) // 1024} KB -> {os.path.relpath(opts.zip, ROOT)}")
if dropped:
    print(f"  {sum(dropped.values())} references to repository-only files shown as plain text (GitHub links are off)")
finish("Hosted website", problems, len(pages))

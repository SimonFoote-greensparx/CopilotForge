#!/usr/bin/env python3
"""Emit the website's core pages into site/ from the repository. --check verifies (decision D14).

Generated: site/index.html, catalogue.html, programmes.html, templates.html, programme-builder.html, author.html,
contributors.html, privacy.html. Hand-written: site/assets/site.css, site/assets/programme-builder.js and the author
photo. Edit this script or scripts/_site.py, never the HTML. scripts/build-hosting.py wraps these pages with every
guide, department, skill, template and programme page and the downloads into a site ready to upload.
"""
import html, json, os, re, sys
from _common import (departments, skills, programmes, templates, sources, editions, archetypes, path, rel, load_yaml,
                     write_or_check, check_flag, finish, split_csv, DISPLAY_NAME, PLUGIN_PREFIX, VERSION, department_root,
                     REPO_URL)
from _site import (site_page, linkify, unlinked_repo_mentions, TAGLINE, HEADLINE, AUTHORS, CONTRIBUTORS, CREDIT_LINE,
                   CC_BY_URL, JOURNEY, LAYERS, AUTHOR_LINE)

sys.path.insert(0, os.path.dirname(__file__))
check, problems = check_flag(), []
e = html.escape
depts, sk, progs, tpls, srcs = departments(), skills(), programmes(), templates(), sources()
dept_by_id = {d["id"]: d for d in depts}
active = [d for d in depts if d["status"] == "active"]
skill_by_id = {f"{s['department']}:{s['folder']}": s for s in sk}


def skill_href(sid):
    d, s = sid.split(":")
    return f"skills/{d}/{s}.html"


def tpl_title(tid):
    m = re.search(r"^# (.+)$", open(tpls[tid], encoding="utf-8").read(), re.M)
    return m.group(1).strip() if m else tid


def page(name, title, body, active_nav):
    write_or_check(f"site/{name}", site_page(title, body, active_nav), check, problems)


# ------------------------------------------------------------------ home
n_draft = sum(1 for s in sk if s["front"].get("metadata", {}).get("status") == "draft")
notice = (f'<div class="notice draft"><strong>Draft, version {VERSION}.</strong> First versions of all {len(active)} departments, '
          f'{len(sk)} skills, {len(progs)} programmes and {len(tpls)} templates are now available. Every skill is a first draft '
          f'({n_draft} marked draft) and is being reviewed department by department, so treat the advice as a practitioner\'s '
          f'first draft and check it before relying on it. <a href="guides/roadmap.html">See the roadmap</a>.</div>')
journey_html = []
for jid, jlabel in JOURNEY:
    items = []
    for d in depts:
        if d.get("journey") != jid:
            continue
        if d["status"] == "active":
            items.append(f'<li><a href="departments/{e(d["id"])}.html">{e(d["title"])}</a></li>')
        else:
            items.append(f'<li class="planned">{e(d["title"])}</li>')
    journey_html.append(f'<div class="stage"><h3>{jlabel}</h3><ul>{"".join(items)}</ul></div>')
ed = editions()
edition_cards = "".join(
    f'<div class="card"><h3>{e(ed[k]["title"])}</h3><p>{e(ed[k]["typical_context"])}</p><p class="meta">{e(ed[k]["design_emphasis"])}</p></div>'
    for k in ("starter", "scale", "enterprise"))
home = f"""<section class="hero">
<div><p class="kicker">{DISPLAY_NAME}</p><h1>{e(HEADLINE)}</h1><p>{e(TAGLINE)}</p>
<div class="buttons"><a class="btn" href="programme-builder.html">Design my AI programme</a><a class="btn ghost" href="catalogue.html">Browse capabilities</a><a class="btn ghost" href="downloads.html">Install CopilotForge</a><a class="btn ghost" href="{REPO_URL}">View on GitHub</a></div></div>
</section>
{notice}
<div class="cards">
<div class="card"><div class="stat">{len(depts)}</div><h3>Departments</h3><p>The organisation a Microsoft AI transformation needs, from strategy and adoption to delivery, assurance and operations. All {len(active)} have first-draft skills.</p></div>
<div class="card"><div class="stat">{len(sk)}</div><h3>Skills</h3><p>Practitioner judgement with explicit triggers, inputs, outputs, reviewer gates, failure modes and Starter, Scale and Enterprise notes.</p></div>
<div class="card"><div class="stat">{len(progs)}</div><h3>Programmes</h3><p>Flagship programmes, from Copilot adoption and Champions to an AI Centre of Excellence and the full AI transformation.</p></div>
<div class="card"><div class="stat">{len(tpls)}</div><h3>Templates</h3><p>Human-usable documents that turn advice into deliverables, with unknowns marked rather than invented.</p></div>
</div>

<h2>Three connected journeys</h2>
<div class="cards">
<div class="card"><h3>Adopt AI</h3><p>Help people use Microsoft Copilot effectively and responsibly: readiness, role-based scenarios, communications, learning, Champions, support and adoption measures.</p></div>
<div class="card"><h3>Build with AI</h3><p>Design and deliver agents, Cowork work designs, Copilot Code builds, Copilot Studio solutions and Microsoft Foundry solutions, including third-party models available through Microsoft.</p></div>
<div class="card"><h3>Scale AI</h3><p>Establish governance, an AI Centre of Excellence, an opportunity pipeline, review gates, a solution inventory and measurable value.</p></div>
</div>

<h2>The capability map</h2>
<p class="lead">Organised around what the organisation needs to do, not around a list of products. You do not need to know which Microsoft AI product you need before {DISPLAY_NAME} can help.</p>
<div class="journey">{''.join(journey_html)}</div>
<p><a href="catalogue.html">Search every department and skill</a></p>

<h2>How it works</h2>
<ol class="steps">
<li><strong>Describe your organisation.</strong> The <a href="programme-builder.html">programme builder</a> creates a profile in your browser: size, sector, Microsoft estate, current AI use, governance, adoption and constraints. Nothing is sent anywhere.</li>
<li><strong>Get a recommendation you can check.</strong> The profile is matched to an edition (Starter, Scale or Enterprise) and a maturity archetype, and each recommendation names the rule that produced it.</li>
<li><strong>Ask for the pack.</strong> In Microsoft Copilot Cowork, attach the profile and ask: <em>"Design our Microsoft AI programme."</em> The departments produce a coherent transformation pack: assessment, operating model, adoption and Champions programmes, CoE, opportunity process, agent-delivery route, governance, roadmap, ownership map and success measures.</li>
</ol>

<h2>Use it in Microsoft Copilot Cowork</h2>
<ol class="steps">
<li><strong>Download the departments you need</strong> from the <a href="downloads.html">downloads page</a>: one plugin per department, each named <code>{PLUGIN_PREFIX}&lt;department&gt;</code>.</li>
<li><strong>Upload them in Cowork:</strong> <em>Customize</em> &gt; <em>Plugins</em> &gt; <em>Upload plugin</em>, and share with your team.</li>
<li><strong>Add the <a href="guides/custom-instructions.html">suggested custom instructions</a></strong>, then ask your questions. The <a href="guides/copilot-cowork.html">Copilot Cowork guide</a> has the details.</li>
</ol>

<h2>Proportionate at every scale</h2>
<div class="edition-grid">{edition_cards}</div>
<p>Governance rises with impact, reach, data sensitivity and autonomy, through five progressive risk tiers. A personal prompt pattern and a customer-facing production agent do not pass through the same gates.</p>

<h2>Principles</h2>
<ul>
<li><strong>Outcome before technology.</strong> The first decision is whether AI is appropriate at all.</li>
<li><strong>Business-owned, AI-enabled.</strong> The business owns priorities, knowledge, outcomes, adoption and value; AI and IT teams enable.</li>
<li><strong>Evidence over attendance.</strong> Champions are recognised for demonstrated capability and contribution.</li>
<li><strong>Knowledge is infrastructure.</strong> Reliable AI depends on owned, current, classified knowledge.</li>
<li><strong>Current facts come from sources.</strong> Availability, licensing and limits are cited from Microsoft sources, never asserted from memory.</li>
<li><strong>Human accountability stays explicit.</strong> AI assists; people remain accountable for outcomes.</li>
</ul>

<h2>Use it freely, credit the author</h2>
<p>{DISPLAY_NAME} is free to use, including commercially and on client work. Content is licensed under <a href="{CC_BY_URL}">CC BY 4.0</a> and code under MIT. When you share or adapt it, credit the author:</p>
<blockquote>{linkify(CREDIT_LINE)}</blockquote>
<p>The source of every skill, programme, template and script is on GitHub: <a href="{REPO_URL}">{REPO_URL}</a>.</p>
<p>Documents you complete for your own organisation from the templates need no credit. The <a href="credit.html">credit page</a> has the full wording. Created by <a href="author.html">{AUTHOR_LINE}</a>, with thanks to our <a href="contributors.html">contributors</a>.</p>

<h2>Independence</h2>
<p>{DISPLAY_NAME} is an independent community project focused on Microsoft AI. It is not affiliated with, endorsed by or sponsored by Microsoft. Microsoft, Microsoft 365, Copilot, Copilot Studio, Microsoft Foundry and related names are trademarks of the Microsoft group of companies. Nothing here is legal, licensing or data-protection advice.</p>
"""
page("index.html", "Home", home, "Home")

# ------------------------------------------------------------------ catalogue
platforms = sorted({p for s in sk for p in split_csv(s["front"].get("metadata", {}).get("platforms"))})
cards = []
for d in depts:
    mine = [s for s in sk if s["department"] == d["id"]]
    badge = '<span class="badge reviewer">Reviewer-class</span>' if d.get("reviewer") else ""
    sts = {s["front"].get("metadata", {}).get("status") for s in sk if s["department"] == d["id"]}
    label = ("first version, draft" if sts == {"draft"} else "first version, " + ", ".join(sorted(sts))) if sts else d["status"]
    status = f'<span class="status {"draft" if "draft" in sts else e(d["status"])}">{e(label)}</span>'
    if mine:
        items = "".join(
            f'<li data-search="{e((s["folder"] + " " + s["front"].get("description", "") + " " + s["front"]["metadata"].get("platforms", "") + " " + s["front"]["metadata"].get("lifecycle", "")).lower())}" '
            f'data-platforms="{e(s["front"]["metadata"].get("platforms", ""))}">'
            f'<a href="skills/{e(d["id"])}/{e(s["folder"])}.html"><code>{e(d["id"])}:{e(s["folder"])}</code></a>'
            f'<span class="status {e(s["front"]["metadata"].get("status", ""))}">{e(s["front"]["metadata"].get("status", ""))}</span>'
            f'<p>{e(s["front"].get("description", ""))}</p><p class="meta">Lifecycle: {e(s["front"]["metadata"].get("lifecycle", ""))} &middot; '
            f'Editions: {e(s["front"]["metadata"].get("edition-support", ""))}</p></li>' for s in mine)
        body = f'<ul class="skills">{items}</ul>'
        title = f'<a href="departments/{e(d["id"])}.html">{e(d["title"])}</a>'
    else:
        body = ('<p class="meta">Planned. Candidate skills from the design:</p><ul class="candidates">'
                + "".join(f'<li data-search="{e((c + " " + d["description"]).lower())}" data-platforms="">{e(c)}</li>' for c in d.get("candidate_skills", []))
                + "</ul>")
        title = e(d["title"])
    cards.append(f'<section class="dept layer-{e(d["layer"])} {e(d["status"])}" data-journey="{e(d.get("journey", ""))}" data-status="{e(d["status"])}">'
                 f'<h2>{title} {badge} {status}</h2><p class="meta">{e(LAYERS[d["layer"]])} &middot; Journey: {e(d.get("journey", "").title())} &middot; '
                 f'Lead role: {e(d["lead_role"])} &middot; Built in phase {d["phase"]}</p><p>{e(d["description"])}</p>{body}</section>')
jf = "".join(f'<button data-journey="{k}">{v}</button>' for k, v in JOURNEY)
pf = "".join(f'<option value="{e(p)}">{e(p)}</option>' for p in platforms)
catalogue = f"""<h1>Capabilities</h1>
<p class="lead">{len(depts)} departments and {len(sk)} skills, all first drafts. Browse by outcome along the journey, by Microsoft technology, or search.</p>
<div class="controls"><input id="q" type="search" placeholder="Search, for example champions, agent testing, oversharing, CoE" aria-label="Search capabilities">
<div class="filters"><button data-journey="all" class="on">All</button>{jf}
<label class="label" for="plat" style="display:inline;margin-left:10px">Technology</label> <select id="plat" style="width:auto"><option value="">Any</option>{pf}</select>
<label style="display:inline;margin-left:10px"><input type="checkbox" id="built"> Built only</label></div><p id="count" aria-live="polite"></p></div>
{''.join(cards)}
<script>
const q=document.getElementById('q'),plat=document.getElementById('plat'),built=document.getElementById('built'),count=document.getElementById('count');let journey='all';
function apply(){{const t=q.value.trim().toLowerCase(),p=plat.value;let n=0;
document.querySelectorAll('.dept').forEach(d=>{{const ok1=(journey==='all'||d.dataset.journey===journey)&&(!built.checked||d.dataset.status==='active');let shown=0;
d.querySelectorAll('li').forEach(li=>{{const ok=ok1&&(!t||li.dataset.search.includes(t))&&(!p||li.dataset.platforms.split(', ').includes(p));li.hidden=!ok;if(ok)shown++;}});
const textOk=ok1&&!p&&(!t||d.textContent.toLowerCase().includes(t));d.hidden=!(shown>0||textOk);if(!d.hidden&&d.dataset.status==='active')n+=shown;}});
count.textContent=n+' built skills shown';}}
q.addEventListener('input',apply);plat.addEventListener('change',apply);built.addEventListener('change',apply);
document.querySelectorAll('.filters button').forEach(b=>b.addEventListener('click',()=>{{
document.querySelectorAll('.filters button').forEach(x=>x.classList.remove('on'));b.classList.add('on');journey=b.dataset.journey;apply();}}));
apply();
</script>"""
page("catalogue.html", "Capabilities", catalogue, "Catalogue")

# ------------------------------------------------------------------ programmes
pblocks = []
for pid in ["ai-transformation"] + [p for p in progs if p != "ai-transformation"]:
    p = progs[pid]
    rows = "".join(
        f'<tr><td>{e(a["title"])}</td><td>{e(a["stage"])}</td><td><a href="{skill_href(a["skill"])}"><code>{e(a["skill"])}</code></a></td>'
        f'<td><a href="templates/{e(a["template"])}.html">{e(tpl_title(a["template"]))}</a></td>'
        f'<td>{e(a["depth"]["starter"])}</td><td>{e(a["depth"]["scale"])}</td><td>{e(a["depth"]["enterprise"])}</td></tr>' for a in p.get("artefacts", []))
    inc = ""
    if p.get("includes"):
        inc = "<p><strong>Includes:</strong> " + ", ".join(f'<a href="#{e(i["programme"])}">{e(progs[i["programme"]]["title"])}</a>' + (" (when agents are emerging or the organisation is a Builder or beyond)" if i.get("when") else "") for i in p["includes"]) + "</p>"
    gates = "".join(f'<li><code>{e(g["reviewer"])}</code> at {e(g["stage"])}, from risk tier {g["from_risk_tier"]}, blocking'
                    + ("" if dept_by_id[g["reviewer"]]["status"] == "active" else " (contract only until the department is built)") + "</li>" for g in p.get("gates", []))
    gates = f"<p><strong>Reviewer gates</strong> (cannot be skipped):</p><ul>{gates}</ul>" if gates else ""
    pblocks.append(f'<section class="card" id="{e(pid)}" style="margin:16px 0"><h2 style="margin-top:0"><a href="programmes/{e(pid)}.html">{e(p["title"])}</a></h2><p>{e(p["purpose"])}</p>'
                   f'<p class="meta">Lifecycle: {e(", ".join(p.get("lifecycle", [])))}</p>{inc}'
                   + (f'<div class="table-wrap"><table class="grid"><thead><tr><th>Artefact</th><th>Stage</th><th>Responsible skill</th><th>Template</th><th>Starter</th><th>Scale</th><th>Enterprise</th></tr></thead><tbody>{rows}</tbody></table></div>' if rows else "")
                   + gates + "</section>")
programmes_html = f"""<h1>Programmes</h1>
<p class="lead">Programmes orchestrate departments into complete outcomes. They are the main way to use {DISPLAY_NAME}; departments and skills are the reusable parts beneath them. Each artefact names the skill responsible for it, the template it is written on, and how deep it goes in each edition.</p>
{''.join(pblocks)}"""
page("programmes.html", "Programmes", programmes_html, "Programmes")

# ------------------------------------------------------------------ templates
used = {}
for pid, p in progs.items():
    for a in p.get("artefacts", []):
        used.setdefault(a["template"], set()).add(p["title"])
trows = []
for tid in tpls:
    text = open(tpls[tid], encoding="utf-8").read()
    owners = [o for o in dict.fromkeys(re.findall(r"`([a-z0-9-]+:[a-z0-9-]+)`", text)) if o in skill_by_id][:2]
    trows.append(f'<tr><td><a href="templates/{e(tid)}.html">{e(tpl_title(tid))}</a></td><td><code>{e(tid)}</code></td>'
                 f'<td>{", ".join(f"<a href=\"{skill_href(o)}\"><code>{e(o)}</code></a>" for o in owners)}</td>'
                 f'<td>{e(", ".join(sorted(used.get(tid, []))))}</td></tr>')
templates_html = f"""<h1>Template library</h1>
<p class="lead">{len(tpls)} human-usable templates. Every fact your organisation must supply is marked <code>[To confirm: ...]</code> so nothing is invented, and each names the skill responsible for it.</p>
<div class="table-wrap"><table class="grid"><thead><tr><th>Template</th><th>Id</th><th>Responsible skill</th><th>Used by programmes</th></tr></thead><tbody>{''.join(trows)}</tbody></table></div>
<p>The templates are also bundled with the <code>organisation-tailoring:transformation-pack</code> skill, which fills them from your profile in Copilot Cowork.</p>"""
page("templates.html", "Templates", templates_html, "Templates")

# ------------------------------------------------------------------ programme builder
import importlib.util
spec = importlib.util.spec_from_file_location("tailor", path("scripts", "tailor.py"))
tailor = importlib.util.module_from_spec(spec); spec.loader.exec_module(tailor)
builder_data = {
    "schema": json.load(open(path("profiles", "schema.json"), encoding="utf-8")),
    "rules": load_yaml(path("data", "tailoring-rules.yaml")),
    "programmes": progs,
    "editions": editions(), "archetypes": archetypes(),
    "departments": {d["id"]: {"title": d["title"], "lead_role": d["lead_role"], "status": d["status"]} for d in depts},
    "optional_facts": tailor.OPTIONAL_FACTS,
    "archetype_order": ["explorer", "adopter", "builder", "scaler", "ai-enterprise"],
    "sample": load_yaml(path("profiles", "samples", "larkfield-services-scale.yaml")),
}
data_json = json.dumps(builder_data, ensure_ascii=False, sort_keys=True).replace("</", "<\\/")
builder = f"""<h1>Programme builder</h1>
<p class="lead">Describe your organisation and get a recommended edition, maturity archetype and programme, with the rule behind each recommendation. Then download the profile and give it to {DISPLAY_NAME} in Copilot Cowork. Everything runs in your browser: nothing you type is sent anywhere.</p>
<div class="callout"><strong>Keep it generic.</strong> Use an alias for the organisation and roles rather than names. Save the downloaded profile in your own OneDrive, attach it in Copilot Cowork and ask: <em>"Design our Microsoft AI programme from this profile."</em> You confirm the edition, archetype and ownership map before any document is written.</div>
<p><button type="button" class="secondary" id="load-sample">Load the fictional 600-person sample</button> <button type="button" class="secondary" id="clear">Start again</button></p>
<div class="builder"><form id="f" onsubmit="return false"></form>
<aside><div class="rec" id="rec" aria-live="polite"><h2>Recommendation</h2><p class="meta">Fill in the required fields to see a recommendation.</p></div>
<div id="status" aria-live="polite" style="margin-top:12px"></div>
<p><button type="button" class="action" id="dl">Download profile</button> <button type="button" class="secondary" id="copy">Copy</button></p>
<label for="yaml" class="label">Profile (YAML)</label><textarea id="yaml" spellcheck="false" readonly></textarea></aside></div>
<script type="application/json" id="builder-data">{data_json}</script>
<script src="assets/programme-builder.js"></script>"""
page("programme-builder.html", "Programme builder", builder, "Programme builder")

# ------------------------------------------------------------------ author and contributors
def author_card(a):
    bio = "".join(f"<p>{e(p)}</p>" for p in a["bio"])
    return (f'<article class="card author" id="{e(a["slug"])}">'
            f'<div class="author-head"><img src="{e(a["photo"])}" alt="Photo of {e(a["name"])}" width="104" height="104" loading="lazy">'
            f'<div><h3>{e(a["name"])}</h3><p class="headline">{e(a["headline"])}</p>'
            f'<p class="links"><a href="{e(a["url"])}">LinkedIn profile</a></p></div></div>'
            f'{bio}<p class="project-role"><strong>On this project:</strong> {e(a["project_role"])}</p></article>')


author = f"""<h1>Author</h1>
<p class="lead">{DISPLAY_NAME} is created and maintained by {AUTHOR_LINE}.</p>
<div class="authors">{''.join(author_card(a) for a in AUTHORS)}</div>
<p>{DISPLAY_NAME} is also shaped by its <a href="contributors.html">contributors</a>. To credit the work when you share or adapt it, see the <a href="credit.html">credit page</a>.</p>"""
page("author.html", "Author", author, "Author")


def contributor_card(c):
    initials = "".join(part[0] for part in c["name"].split()[:2]).upper()
    cred = f'<p class="headline">{e(c["credentials"])}</p>' if c.get("credentials") else ""
    return (f'<article class="card contributor" id="{e(c["slug"])}"><div class="initials" aria-hidden="true">{e(initials)}</div>'
            f'<div><h3>{e(c["name"])}</h3>{cred}<p class="links"><a href="{e(c["url"])}">LinkedIn profile</a></p></div></article>')


contributors = f"""<h1>Contributors</h1>
<p class="lead">{DISPLAY_NAME} is created and maintained by its <a href="author.html">author</a>, {AUTHOR_LINE}. These people have also contributed to the project. Thank you.</p>
<div class="contributors">{''.join(contributor_card(c) for c in CONTRIBUTORS)}</div>
<h2>Contribute</h2>
<p>Suggestions, corrections and new skills are welcome. The <a href="guides/contributing.html">contributing guide</a> explains how to propose a change. Contributors are listed here, in AUTHORS.md and in the git history.</p>"""
page("contributors.html", "Contributors", contributors, "Contributors")

privacy = f"""<h1>Privacy</h1>
<p class="lead">{DISPLAY_NAME} is a library of skills, programmes, templates and documentation. It does not run a service, and it does not collect, store or send any personal or organisation data.</p>
<h2>This website</h2>
<p>The website is a set of static pages. It sets no cookies of its own and has no analytics. Our web hosting provider may log requests, such as IP addresses and browser details, to operate and secure the service.</p>
<h2>The programme builder</h2>
<p>The <a href="programme-builder.html">programme builder</a> runs entirely in your browser. Nothing you type is sent anywhere; the profile file is created on your device when you select Download.</p>
<h2>The skills and plugins</h2>
<p>The skills are instructions that run inside the Microsoft AI assistant you install them in, such as Microsoft Copilot Cowork. Any data you share in those conversations is processed under that product's terms and your organisation's agreement with Microsoft, not by this project. The tailoring skills write organisation profiles and generated documents only to your own storage, never to this project.</p>
<h2>Contact</h2>
<p>Raise privacy questions with the <a href="author.html">author</a>.</p>"""
page("privacy.html", "Privacy", privacy, "")

from _site import GITHUB_LINKS
for f in sorted(os.listdir(path("site"))) if GITHUB_LINKS else []:
    if f.endswith(".html"):
        for url in unlinked_repo_mentions(open(path("site", f), encoding="utf-8").read()):
            problems.append(f"site/{f}: the repository address {url} is shown but not linked")
finish("Website pages", problems, 8)

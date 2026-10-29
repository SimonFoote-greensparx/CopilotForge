"""Website constants and the shared page shell, used by scripts/build-site.py and scripts/build-hosting.py.

Edit the author bio, contributors, tagline and site address here, then run bash scripts/build-all.sh and
python3 scripts/build-hosting.py. Decisions D14, D22 and D23 in DECISIONS.md.
"""
from __future__ import annotations

import html as _html
import re

from _common import DISPLAY_NAME, REPO_URL, VERSION

SITE_URL = "https://copilotforge.ai/"
TAGLINE = ("Open-source agents, skills, playbooks and templates for adopting, governing and delivering Microsoft AI, "
           "from first Copilot rollout to enterprise AI Centre of Excellence.")
HEADLINE = "Build your Microsoft AI capability."
# The website links every mention of the GitHub repository to it, as D365Forge's does (decision D24): a GitHub item in
# the navigation, a "View on GitHub" button, and links for files that exist only in the repository. While the
# repository is private (open decision O5), people without access see GitHub's "page not found". Set to False, or build
# with --no-github-links, to show repository-only references as plain text instead.
GITHUB_LINKS = True
CC_BY_URL = "https://creativecommons.org/licenses/by/4.0/"
CREDIT_LINE = f'"CopilotForge" by Simon Foote ({REPO_URL}), licensed under CC BY 4.0 ({CC_BY_URL}).'
AUTHOR_LINE = "Simon Foote"

# The author page. Generic by design: no employer, client or company names appear anywhere in the project (D11, D23).
AUTHORS = [
    {"name": "Simon Foote", "slug": "simon-foote", "photo": "assets/authors/simon-foote.jpg",
     "url": "https://www.linkedin.com/in/simonjayfoote/",
     "headline": "Microsoft AI and Power Platform Architect. Founder of a Microsoft AI consultancy and an AI adoption platform.",
     "project_role": "Creates and maintains CopilotForge: the departments, skills, programmes, templates, tooling and this website.",
     "bio": [
         "Simon has delivered Microsoft business applications for more than a decade. He started in 2014 as a technical "
         "consultant implementing Dynamics CRM, then led CRM and business intelligence teams for large facilities services "
         "organisations. He has been a Microsoft technical specialist and data engineer in a global technology company's UK "
         "innovation centre, and an architect, consultant and developer on Dynamics 365 and Power Apps. He grew a small group "
         "of citizen developers into a multi-skilled Power Platform and Azure development department, introducing Scrum, "
         "DevOps and ALM, then led Power Platform Centre of Excellence work for central government and a national Power "
         "Platform capability.",
         "Today he is a Microsoft AI and Power Platform architect and runs his own consultancy. He helps organisations adopt "
         "Microsoft Copilot by finding the use cases that pay back, putting governance and responsible AI guardrails in place "
         "before scaling, and building Copilot Studio agents grounded in their own data. He has designed and run "
         "evidence-led Copilot Champions programmes and AI Centres of Excellence, and in 2025 he founded an AI adoption "
         "platform that gives managed service providers and consultancies a structured approach to AI adoption, compliance "
         "and governance. CopilotForge turns that experience into an open, reusable operating model.",
     ]},
]
# People who have contributed beyond the author, in the order they joined. Also listed in AUTHORS.md.
CONTRIBUTORS = [
    {"name": "Matt Fitchett", "slug": "matt-fitchett", "credentials": "", "url": "https://www.linkedin.com/in/mattfitchett/"},
]

JOURNEY = [("strategy", "Strategy"), ("adopt", "Adopt"), ("build", "Build"), ("govern", "Govern"), ("scale", "Scale"),
           ("measure", "Measure")]
LAYERS = {"transformation": "Transformation", "adoption": "Adoption", "delivery": "Microsoft AI delivery",
          "assurance": "Assurance and operations", "spanning": "Spanning"}
REPO_RX = re.compile(r"https?://github\.com/SimonFoote-greensparx/CopilotForge[^\s<>()\[\]\"']*")
NAV = [("index.html", "Home"), ("catalogue.html", "Catalogue"), ("programmes.html", "Programmes"),
       ("templates.html", "Templates"), ("programme-builder.html", "Programme builder"),
       ("guides/copilot-cowork.html", "Copilot Cowork"), ("downloads.html", "Downloads"), ("author.html", "Author"),
       ("contributors.html", "Contributors")]


def linkify(text: str, github_links: bool = GITHUB_LINKS) -> str:
    """Escape text for HTML and turn every web address in it into a link that opens that address. Repository
    addresses stay plain text while GitHub links are off."""
    out, last = [], 0
    for m in re.finditer(r"https?://[^\s<>()\[\]\"']+", text):
        url = m.group(0).rstrip(".,;:!?")
        out.append(_html.escape(text[last:m.start()]))
        if REPO_RX.match(url) and not github_links:
            out.append(_html.escape(url))
        else:
            out.append(f'<a href="{_html.escape(url)}">{_html.escape(url)}</a>')
        last = m.start() + len(url)
    out.append(_html.escape(text[last:]))
    return "".join(out)


def unlinked_repo_mentions(page: str) -> list[str]:
    """Repository addresses a reader sees on the page but cannot click (code, scripts and forms excluded)."""
    body = re.sub(r"<script\b.*?</script>|<pre\b.*?</pre>|<code\b.*?</code>|<textarea\b.*?</textarea>", "", page, flags=re.S)
    body = re.sub(r"<a\b[^>]*>.*?</a>", "", body, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    return [m.group(0) for m in REPO_RX.finditer(body)]


def site_page(title: str, body: str, active: str, *, root: str = "", github_links: bool = GITHUB_LINKS,
              generator: str = "scripts/build-site.py") -> str:
    """The shared page shell. `root` is the relative path from the page back to the site root."""
    nav = list(NAV) + ([(REPO_URL, "GitHub")] if github_links else [])

    def href(h: str) -> str:
        return h if h.startswith(("http", "/")) else root + h

    links = "".join(f'<a href="{href(h)}"{" class=\"active\"" if t == active else ""}>{t}</a>' for h, t in nav)
    e = _html.escape
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | {DISPLAY_NAME}</title>
<meta name="description" content="{e(TAGLINE)}">
<meta name="theme-color" content="#3b2c85">
<meta property="og:site_name" content="{DISPLAY_NAME}">
<meta property="og:title" content="{e(title)} | {DISPLAY_NAME}">
<meta property="og:description" content="{e(TAGLINE)}">
<meta property="og:url" content="{SITE_URL}">
<link rel="stylesheet" href="{root}assets/site.css">
</head>
<body>
<!-- Generated by {generator}. Do not edit by hand. -->
<header class="top"><div class="wrap"><a class="brand" href="{root}index.html" aria-label="{DISPLAY_NAME} home"><span class="mark" aria-hidden="true">CF</span><span class="wordmark">Copilot<span>Forge</span></span><span class="draft-badge" title="All content is a first draft under review">Draft</span></a><nav>{links}</nav></div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap">Created by {AUTHOR_LINE}. Version {VERSION}. Content licensed under <a href="{CC_BY_URL}">CC BY 4.0</a>, code under MIT. <a href="{href('credit.html')}">How to credit</a> · <a href="{href('privacy.html')}">Privacy</a> · <a href="{href('author.html')}">Author</a> · <a href="{href('contributors.html')}">Contributors</a><br>An independent community project, not affiliated with or endorsed by Microsoft.</div></footer>
</body>
</html>
"""

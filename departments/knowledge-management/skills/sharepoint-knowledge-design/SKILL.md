---
name: sharepoint-knowledge-design
description: Designs SharePoint hubs, sites, libraries, pages, content types and metadata as AI-ready knowledge sources - authoritative content separated from working areas, permissions aligned to audience, consistent metadata and clear archive locations. Use when a knowledge domain is being set up or restructured for Copilot and agents, when one site mixes policy with drafts, or when makers cannot point an agent at a clean library.
license: CC-BY-4.0
metadata:
  department: knowledge-management
  lifecycle: Enable, Deliver
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: sharepoint, purview, m365-copilot, m365-agents, copilot-studio
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, design-authority
  sources: ms-copilot-privacy, ms-agent-builder, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# SharePoint knowledge design

## Purpose

Most knowledge that Copilot and Microsoft 365 agents draw on lives in SharePoint, and its structure decides whether AI
finds the authoritative answer or a draft in the next folder. This skill designs sites, libraries, pages and metadata so
that authoritative knowledge sits in clean, owned, correctly shared locations that agents can ground on, with working
material and archives kept apart. It goes wrong when design copies the organisation chart rather than how knowledge is
used, when one site serves every audience, or when an elaborate metadata model is designed that nobody fills in.

## When to use

- A knowledge domain is being set up, migrated or restructured, and should be ready for Copilot and agents.
- A single site mixes approved policy, drafts, project files and archives, and agents pick up the wrong version.
- Makers cannot find a clean library to use as an agent knowledge source.
- Clean-up has finished and the domain needs a structure that stops clutter returning.

## When not to use

- Configuring an agent's knowledge sources in Copilot Studio - use `copilot-studio:studio-knowledge-architecture`.
- Retrieval, indexing and chunking design for custom solutions - use `ai-foundry:retrieval-design`.
- Architectural grounding patterns across data platforms - use `ai-architecture:grounding-patterns`.
- Classifying sensitivity and audience of existing collections - use `knowledge-management:knowledge-classification`.
- Writing and structuring individual documents and pages - use `knowledge-management:ai-ready-content`.

## Questions to ask first

1. Which knowledge domains are in scope, who are their audiences, and which AI uses will depend on them?
2. What is authoritative in this domain, what is working material, and what is archive?
3. Do audiences differ within the domain - all staff, a function, managers only - and do any need restricted content?
4. What metadata would genuinely help people and AI find and judge content (owner, status, effective date, audience, topic), and who will maintain it?
5. What existing hubs, sites and navigation must the design fit, and who administers them?

## Required inputs

- The domains and sources in scope, with owners and condition, from `knowledge-management:knowledge-inventory`.
- Classification and intended audiences, from `knowledge-management:knowledge-classification`.
- The organisation's existing information architecture: hubs, navigation, site provisioning and naming rules.
- Representative questions per domain, to test findability before and after.

Where the SharePoint governance model (who may create sites, default sharing settings) is unknown, confirm it with the
Microsoft 365 administrators before designing; do not assume settings. Where audiences are undecided, design for the
narrowest plausible audience and record the decision as open.

## Decision framework

| Design decision | Choose | Avoid |
|---|---|---|
| Unit of authoritative knowledge | A dedicated library or set of pages per domain, owned by one content owner | Authoritative documents scattered across team sites |
| Separating status | Authoritative, working and archive in separate locations | Status shown only by folder names or file name suffixes |
| Audience | One site or library per distinct audience; permissions set at site or library, by group | Item-level unique permissions and sharing links on authoritative content |
| Format | Pages for short, frequently read guidance; documents for formal, versioned or printable material | The same content in both forms, maintained separately |
| Metadata | A small set of required columns (owner, status, effective date, review date, audience, topic) via a shared content type | Large optional schemas or deep folder trees as the only structure |
| Versions | Version history on, one current published item | Copies named "v2", "final", "old" beside each other |
| Archive | A restricted archive location outside agent scope | Archive folders inside authoritative libraries |

## Practitioner approach

Design from use, not from structure. Start with the representative questions people ask in each domain and trace where
the answer should come from. That reveals the minimum set of authoritative locations needed, and it usually shows that
the domain's knowledge is currently spread across several team sites built around projects or past organisation
charts.

Separate authoritative, working and archive content physically, not by convention. An authoritative library contains
only approved, current content owned by one content owner. Drafting happens in a working area, with publication as a
deliberate step. Superseded content moves to an archive location that is restricted and excluded from agent knowledge.
This one decision removes most "the agent quoted the draft" problems, and it gives makers an obvious, clean source to
ground on.

Align permissions to audience at the container level. Where audiences differ, create separate libraries or sites rather
than breaking inheritance item by item; fine-grained permissions are hard to audit and become the oversharing of
tomorrow. Remove broad access groups and sharing links from authoritative locations unless the audience genuinely is
everyone. Because Copilot grounding is permission-trimmed, a clean permission model is also what lets a single agent
safely serve several audiences.

Keep metadata small and required. A shared content type with five or six columns, most of them defaulted, is filled in;
a schema of twenty optional fields is not. Owner, status, effective date and next review date do the most work, because
they support review cycles, archive routines and a reader's judgement of currency. Choose pages or documents
deliberately: short, frequently read guidance is often clearer as pages with headings, while formal policies may need a
versioned document. Never maintain both.

Connect the domain to the wider estate through hubs and navigation so people find it, and register every authoritative
location in the knowledge register with its owner and grounding eligibility. Provision new knowledge sites from a
template carrying the structure, content type and default label, so good design repeats itself.

Test before handing over. Ask the representative questions in search and in Copilot with test accounts from different
audiences, and confirm answers come from the authoritative library and that restricted content does not appear for the
wrong audience. Record the results as the baseline for the domain.

## Outputs

- A knowledge site design for each domain: site and library map, audiences and permission groups, content types and metadata, page and document rules, archive location.
- A provisioning template for new knowledge sites, with default structure, metadata and label.
- Register entries for each authoritative location in the `knowledge-asset-register`.
- Before-and-after findability test results for representative questions.

## Microsoft platform considerations

SharePoint hubs, sites, libraries, pages, content types, columns, version history and default sensitivity labels are the
building blocks; Microsoft Purview applies labels and retention. How Copilot and each agent route use site structure,
pages, metadata, file types and permissions when grounding varies and changes, so confirm current behaviour in the
source records (`ms-copilot-privacy`, `ms-agent-builder`). Administrative features for access governance depend on
configuration and licensing; check them with administrators and the licensing guide.

## Adoption considerations

Changing where people find knowledge disrupts habits. Communicate the new locations, redirect old links, and involve
content owners and Champions in testing so they can explain the change to their teams.

## Knowledge considerations

The design implements decisions from `knowledge-management:knowledge-classification`, supports
`knowledge-management:knowledge-lifecycle` (working, authoritative and archive stages), and gives
`knowledge-management:knowledge-grounding-standards` clean sources to designate.

## Security and privacy considerations

Container-level permissions aligned to audience, no broad groups or sharing links on authoritative content, and a
restricted archive are the core controls. From risk tier 2, the permission design goes to
`security-privacy:data-exposure-review` before agents ground on it.

## Responsible AI considerations

Not applicable directly; structure does not change what AI decides. Check that audience design does not exclude
frontline or part-time roles from guidance they need.

## Evaluation requirements

Findability tests with representative questions across audiences must pass before handover: answers from the
authoritative location, no restricted content for the wrong audience. Pass these as test cases to
`m365-agents:agent-testing` for dependent agents.

## Value measures

Track the share of representative questions answered from the authoritative location, the number of authoritative
locations with item-level permissions or broad sharing links, and maker time to find a ready source. The Knowledge
Manager owns these, reported by domain.

## Scale notes

### Starter

Create one clean authoritative library per domain the first agents need, with simple metadata, and move drafts and
archives out.

### Scale

Provision knowledge sites from a template with standard content types and labels, connect them through hubs, and
register every authoritative location.

### Enterprise

Run a knowledge information architecture across business units with shared content types, provisioning governance and
regular access reviews, coordinated with records management.

## Hand-offs

- To site administrators to implement, and to `knowledge-management:knowledge-inventory` to register the new locations.
- To `copilot-studio:studio-knowledge-architecture` or `m365-agents:knowledge-source-readiness` when agents adopt the sources.
- To `knowledge-management:ai-ready-content` for authors working in the new structure.

## Reviewer gates

From risk tier 2, `security-privacy` reviews the permission and audience design, and `design-authority` may review
estate-wide information architecture decisions for conformance with the organisation's platform standards. Blocking
findings are resolved before agents ground on the new locations.

## Failure modes

- Authoritative, working and archive content share one library, separated only by folder names.
- Item-level permissions accumulate and nobody can say who sees what.
- A large optional metadata schema is designed and left empty.
- The same guidance is kept as a page and a document, and the two diverge.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Place archive or draft content inside an authoritative library that agents ground on.
- Use item-level sharing links as the access model for authoritative knowledge.
- Assume default sharing or provisioning settings without confirming them with administrators.
- Design structure around the organisation chart instead of how knowledge is used.

---
name: grounding-patterns
description: Chooses how an AI solution grounds on organisational data - Microsoft 365 work context, curated SharePoint knowledge, Graph connectors, Dataverse or structured data, or a custom retrieval index - judged on permissions, freshness, data movement and ownership. Use when a solution's knowledge spans several stores, when content would be copied or indexed outside its source, or when teams build overlapping indexes of the same data.
license: CC-BY-4.0
metadata:
  department: ai-architecture
  lifecycle: Envision, Deliver, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-copilot, m365-agents, copilot-studio, ai-foundry, sharepoint, purview, fabric, azure
  edition-support: starter, scale, enterprise
  reviewers: design-authority, security-privacy
  sources: ms-copilot-privacy, ms-agents-extensibility, ms-agent-builder, ms-declarative-agents, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# Grounding patterns

## Purpose

Most AI quality and exposure problems are grounding problems. This skill chooses, at architecture level, how a solution
reaches the organisational data it answers from: in place through Microsoft 365 work context, from a curated knowledge
source, through a connector that indexes another system, through queries on structured data, or through a custom
retrieval index. Each pattern has different consequences for permissions, freshness, data movement and ownership. The
work goes wrong when content is copied into a new index that ignores source permissions, when several teams index the
same data in different ways, and when nobody owns the copy.

## When to use

- A solution needs knowledge from more than one store, or from a system outside Microsoft 365.
- A design proposes copying or indexing content outside its source system.
- Several teams are building their own indexes or knowledge stores over the same data.
- A reference architecture needs a standard grounding pattern.
- An agent's answers are stale or surprising and the grounding route is suspected.

## When not to use

- Configuring the knowledge sources of a specific agent - use `m365-agents:agent-grounding`.
- Designing knowledge sources for a Copilot Studio agent - use `copilot-studio:studio-knowledge-architecture`.
- Choosing grounding approaches inside a Foundry build - use `ai-foundry:foundry-grounding-strategy`.
- Designing indexing, chunking and search for custom retrieval - use `ai-foundry:retrieval-design`.
- Setting the content standards sources must meet - use `knowledge-management:knowledge-grounding-standards`.
- Assessing whether a source is owned, current and permissioned correctly - use `m365-agents:knowledge-source-readiness`.

## Questions to ask first

1. What questions must the solution answer, and which stores hold the authoritative answers?
2. Do people already have the right access to those stores, and should the solution respect exactly those permissions?
3. How fresh must answers be - live, daily or whenever the owner publishes?
4. Would any pattern copy data outside its source, region or tenant, and who would own the copy?
5. Is the data unstructured content, structured records or both?

## Required inputs

- The solution brief with the questions it must answer and its audience.
- An inventory of candidate sources with owners and condition, ideally from `knowledge-management:knowledge-inventory`.
- Sensitivity classification of the sources.
- The platform decision from `ai-architecture:platform-selection`.

If a source has no owner, record it as a precondition rather than designing around it; an unowned source makes every
pattern fragile.

## Decision framework

Prefer patterns that leave data where it is and keep source permissions intact. Move down the table only when the row
above cannot meet the need.

| Pattern | Use when | Watch for |
|---|---|---|
| In-place Microsoft 365 work context | The answer is in content people can already reach in Microsoft 365 | Oversharing in the source becomes discoverable |
| Curated knowledge source (sites, libraries, files) | A defined audience needs answers from a governed, owned subset | Curation drifting from the authoritative copy |
| Connector indexing another system into Microsoft 365 | Content lives outside Microsoft 365 and must be searchable with mapped permissions | Permission mapping gaps, index freshness, ownership of the connector |
| Live query on structured data (Dataverse, APIs, analytics models) | The answer is a record or calculation, not a passage of text | Query scope, user identity on the query, performance |
| Custom retrieval index | Specialist retrieval is needed that the above cannot provide, and a team can operate it | Permissions must be re-implemented, data is copied, cost and ownership grow |

For every chosen pattern record: source, owner, permission model, freshness, where any copy lives, retention of the
copy, and the trigger for review.

## Practitioner approach

Start from the questions, not the stores. Collect a short list of real questions the solution must answer and trace
each to where the authoritative answer lives. This often shows that two of the five proposed sources are never needed,
and that the most important answer is in a system nobody mentioned.

Classify each needed source as content or records. Content suits retrieval; records usually suit a live query that
returns the exact value. Grounding a model on exported spreadsheets of records produces confident, out-of-date numbers.

Prefer in-place patterns. Microsoft 365 grounding respects the user's existing permissions, which is a strength and a
risk: it means any oversharing in the source becomes easy to find. The fix is to correct permissions at source with
`security-privacy:data-exposure-review`, not to copy content somewhere else.

When content must move, design the copy as a governed asset. A connector or custom index is a new store with its own
permissions, retention, region and owner. Ask how source permissions are mapped, how quickly deletions and permission
changes reach the index, and who answers when it is wrong. If nobody can answer, the pattern is not ready.

Look across the portfolio. Where several solutions need the same source, offer one shared, owned grounding asset rather
than many private indexes. This is often the largest saving the architecture function can make.

Choose custom retrieval last. It is right when specialist ranking, hybrid search or complex document structures are
genuinely needed and an engineering team will operate it. Hand the detailed design to `ai-foundry:retrieval-design`.

Record the decision with freshness and permission tests attached, so evaluation can check that a user without access
gets no answer and that a changed document is reflected in time.

## Outputs

- A grounding design for the solution: questions traced to sources, chosen pattern per source, permission model, freshness, copies and owners.
- An architecture decision record on the `architecture-decision-record` template for any pattern that copies or indexes data.
- Preconditions for knowledge owners and for permission fixes at source.

## Microsoft platform considerations

Microsoft 365 grounding, Agent Builder knowledge, Copilot Studio knowledge sources, connectors and Foundry retrieval each
support different source types, permission handling and freshness. Check `ms-copilot-privacy` for how permission-trimmed
grounding works and `ms-agents-extensibility` and `ms-agent-builder` for current knowledge options before fixing a
pattern.

## Adoption considerations

Users trust answers they can trace. Prefer patterns that cite the source, and tell knowledge owners how their content
is used so they keep it current.

## Knowledge considerations

This skill depends on `knowledge-management` for ownership, quality and review cycles. Every pattern needs a named
knowledge owner per source, and poor sources are a precondition, not something architecture can fix.

## Security and privacy considerations

Copies and indexes are where exposure grows. Record region, retention and permission mapping for every copy, and send
the design to the `security-privacy` review, with personal data in sources routed to
`security-privacy:privacy-assessment`.

## Responsible AI considerations

Answers grounded on incomplete or biased sources can disadvantage people. Where outputs inform decisions about people,
record source limitations and route the case to the `responsible-ai` review through risk classification.

## Evaluation requirements

Include permission tests (users with and without access), freshness tests (a changed or deleted document) and
groundedness tests in the solution's evaluation, consistent with `evaluation-quality:groundedness-testing`.

## Value measures

At portfolio level, track the number of duplicate indexes over the same data, shared grounding assets in use, and
grounding-related defects found in evaluation and operation. The AI solution architect owns these, with the knowledge
manager, and takes the baseline from the first portfolio review.

## Scale notes

### Starter

Ground on curated, owned Microsoft 365 content wherever possible, fix permissions at source and avoid custom indexes.

### Scale

Publish standard grounding patterns, maintain a list of grounding assets and their owners, and require a recorded
decision for any copy.

### Enterprise

Offer shared, owned grounding assets per major data domain, aligned with data governance and data products, and review
indexes for duplication and freshness on a set cycle.

## Hand-offs

- To `m365-agents:agent-grounding`, `copilot-studio:studio-knowledge-architecture` or `ai-foundry:foundry-grounding-strategy` for build.
- To `ai-foundry:retrieval-design` when custom retrieval is chosen.
- To `knowledge-management:knowledge-grounding-standards` for source preconditions.
- To `security-privacy:data-exposure-review` for the security gate.

## Reviewer gates

From risk tier 2 the grounding design is reviewed by `security-privacy` (blocking) for exposure and copies, and by
`design-authority` for conformance and duplication. Tier 3 and above also need evidence for `evaluation-quality`.

## Failure modes

- Content is copied into a custom index that ignores source permissions, and restricted content reaches everyone.
- Records are grounded as exported documents and the solution gives confident, stale numbers.
- Several teams index the same system separately, and their answers disagree.
- Deleted or corrected content remains in an index for weeks because freshness was never designed.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Copy content into a new store without recording its permissions, retention, region and owner.
- Fix oversharing by moving content instead of correcting permissions at source.
- Choose custom retrieval when an in-place pattern meets the need.
- Assume a connector maps source permissions correctly without testing it.

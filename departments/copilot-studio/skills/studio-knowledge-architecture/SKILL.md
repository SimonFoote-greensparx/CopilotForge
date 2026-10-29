---
name: studio-knowledge-architecture
description: Designs the knowledge layer of a Copilot Studio agent - which ready sources to connect and by which knowledge type, how each is scoped, described and permission-trimmed, whether content is live or uploaded, how answers cite sources and how the layer is refreshed and owned. Use when connecting knowledge to a Studio agent, when answers come from the wrong source, or when a maker wants to upload copies of documents.
license: CC-BY-4.0
metadata:
  department: copilot-studio
  lifecycle: Deliver, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-studio, power-platform, sharepoint, purview
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, evaluation-quality
  sources: ms-copilot-studio-guidance, ms-copilot-studio-security-governance, ms-copilot-privacy, ms-agents-extensibility
  status: draft
  authors: Simon Foote
---

# Studio knowledge architecture

## Purpose

A Copilot Studio agent's answers are only as good as the knowledge it can reach and its ability to choose the right
source for each question. This skill designs the knowledge layer: which ready sources are connected, through which
knowledge type, scoped how narrowly, described how precisely, trimmed to whose permissions, and refreshed by whom. It
usually goes wrong when a maker points the agent at a whole site, uploads convenient copies of documents that then go
stale, or mixes public web content with internal policy so users cannot tell which they are reading.

## When to use

- Knowledge sources in the brief have readiness verdicts and need connecting to a Copilot Studio agent.
- A maker proposes uploading files, adding a public website or connecting a large site or table.
- The agent answers from the wrong source, cites outdated copies or contradicts itself.
- An agent is adding a new audience whose access to content differs from the original users.

## When not to use

- Judging whether content is owned, current and fit to ground on - use `m365-agents:knowledge-source-readiness`.
- Configuring grounding for a declarative agent built in Agent Builder - use `m365-agents:agent-grounding`.
- Using Dataverse tables as knowledge or data in depth - use `copilot-studio:dataverse-integration`.
- Custom indexing, chunking and retrieval engineering - use `ai-foundry:retrieval-design`.
- Redesigning SharePoint sites and libraries themselves - use `knowledge-management:sharepoint-knowledge-design`.

## Questions to ask first

1. Which sources have a ready or ready-with-conditions verdict, and who owns each?
2. Should answers be trimmed to each user's own permissions, or must everyone in the audience see the same content?
3. Does any source need to stay live at its origin, and is any proposed copy (an uploaded file) acceptable to its owner?
4. Should the agent ever answer from the public web or general model knowledge, and how will users know when it does?
5. Which questions need structured records rather than documents?

## Required inputs

- Readiness verdicts and owners for each source from `m365-agents:knowledge-source-readiness`.
- The solution design and representative questions mapped to expected sources.
- The authentication design, because permission trimming depends on the user being signed in.
- The sensitivity labels or classification of each source.

A source without a verdict is not connected. If the authentication design is not settled, the knowledge design is
provisional, because anonymous agents cannot trim answers to a user's permissions.

## Decision framework

Choose the knowledge type that keeps content live, owned and permission-trimmed, and accept copies only with a reason.

| Need | Preferred pattern | Accept a copy or wider pattern only when |
|---|---|---|
| Policy and guidance owned in Microsoft 365 | Connect the specific SharePoint sites, libraries or folders, trimmed to the user | Never connect the whole tenant or a site broader than the questions need |
| Structured business records | Dataverse tables or a tool that queries the system of record | The data is reference-only and owned in Dataverse |
| Content held in other enterprise systems | An enterprise connector indexed into Microsoft 365, with its permissions mapped | The source cannot carry permissions and the content is approved for the whole audience |
| A small, stable reference set with no live home | Uploaded files, with a named owner and review date | The owner accepts responsibility for keeping the copy current |
| Public information | Named public websites, scoped to specific domains or paths | General web search only where the brief allows it and answers are labelled |

Prefer fewer, sharper sources. Each source needs a description that tells the orchestrator what it contains and when to
use it. Decide explicitly whether general model knowledge may be used; for most internal agents it should be off or
tightly limited.

## Practitioner approach

Start from the expected sources in the question map, not from what is easy to connect. For each representative question,
name the one source that should answer it. Where two sources could answer, decide which is authoritative and either
narrow the other or remove it; contradictions between connected sources are the most common cause of confident wrong
answers.

Scope tightly. Connect the library or folder that holds the content the questions need rather than a whole site, and
check what else sits in that location. A site that looks tidy often contains drafts, archives and old versions that
will surface in answers. Where scoping cannot exclude them, send the clean-up back to the knowledge owner before
connecting.

Decide permission behaviour deliberately. When users sign in and sources are connected with their identity, answers are
trimmed to what each user can open, which protects restricted content but means two users can get different answers. If
the business needs everyone to see the same answer, the content itself must be shared with the whole audience; never use
a service identity to bypass permissions without the owner's and reviewer's agreement.

Treat uploaded files as copies with an owner. Uploading is convenient and is how stale answers creep in: the original is
updated, the copy is not. Record every uploaded file with its origin, owner and review date, and prefer connecting the
live source.

Write source descriptions as carefully as tool descriptions. Say what the source contains, who it is for and what it does
not cover. Configure the agent to cite sources so users and testers can see where an answer came from.

Test with users of different access, ask questions whose answers changed recently, and ask questions that sit between
sources. Record which source each answer used. Then agree the refresh model: who tells the agent owner when a source
moves, is restructured or changes owner, and how often uploaded copies are reviewed.

## Outputs

- A knowledge map: each source, its knowledge type, scope, owner, readiness verdict, description, permission behaviour and refresh route.
- A question-to-source map showing the authoritative source for each representative question.
- A register of uploaded files with origin, owner and review date.
- The knowledge section of the `studio-solution-design`, and permission-trimming evidence for the release record.

## Microsoft platform considerations

Copilot Studio offers several knowledge types - Microsoft 365 content, Dataverse, uploaded files, public websites and
enterprise connectors among them - and their limits, indexing behaviour, permission handling and availability differ and
change frequently. Check `ms-copilot-studio-guidance` and `ms-copilot-privacy` for current behaviour, and
`ms-copilot-studio-security-governance` for admin controls such as restricting web knowledge or uploads.

## Adoption considerations

Tell users what the agent knows and what it does not. A short "what I can help with" message and visible citations build
trust faster than a broad agent that sometimes answers from the wrong place.

## Knowledge considerations

This skill depends on knowledge owners. Every connected source has a named owner who has agreed to the agent using it
and to tell the agent owner about changes. Route recurring content problems to `knowledge-management:knowledge-gap-analysis`.

## Security and privacy considerations

Connected sources can expose oversharing that was previously hidden by obscurity. Check effective permissions before
connecting, avoid service identities that widen access, and send broad or sensitive sources to
`security-privacy:data-exposure-review`. Uploaded copies lose the original's permissions and labels unless confirmed otherwise.

## Responsible AI considerations

Users should be able to see whether an answer came from organisational content or the public web. Where answers could
affect people's entitlements or safety, require citations and a route to a person when the agent is unsure.

## Evaluation requirements

Evaluation checks groundedness against the authoritative source, behaviour when knowledge is silent, permission trimming
across at least two user profiles from tier 2, and freshness after a source update. Cases come from the question-to-source map.

## Value measures

Track unanswered and low-confidence questions, answers citing the wrong source and stale-answer reports, measured at
agent level by the agent owner. A falling unanswered rate after knowledge changes shows the layer is improving.

## Scale notes

### Starter

One to three tightly scoped live sources, each with an owner, no uploaded copies without a review date, and citations on.

### Scale

Standard patterns per knowledge type, shared descriptions for commonly used sources and a register of which agents use
which sources, so a site change can be traced to the agents it affects.

### Enterprise

Maintain an organisation-wide source catalogue with approved scopes and owners, require data exposure review for any new
broad source from tier 2, and automate alerts when a connected source changes structure or ownership.

## Hand-offs

- Back to `m365-agents:knowledge-source-readiness` for any source that fails scoping or testing.
- To `copilot-studio:dataverse-integration` for structured data needs.
- To `security-privacy:data-exposure-review` for broad or sensitive sources.
- To `copilot-studio:studio-testing-and-evaluation` with the question-to-source map.

## Reviewer gates

From risk tier 2, `security-privacy` reviews scope, permission behaviour and any service identity, and `evaluation-quality`
reviews groundedness and permission-trimming evidence. A source connected with wider effective access than its
sensitivity allows is a blocking finding.

## Failure modes

- A whole site is connected and archived drafts surface as current policy.
- Uploaded copies go stale after the original changes, and nobody owns the copy.
- Two connected sources disagree and the agent alternates between them.
- Public web knowledge is enabled for an internal policy agent and users cannot tell which answers are organisational.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Connect a source that has no readiness verdict or no owner.
- Use a service identity to give users answers from content they cannot open, without owner and reviewer agreement.
- Upload copies of documents without an origin, owner and review date.
- Assert knowledge limits, file types or indexing behaviour from memory.

---
name: knowledge-source-readiness
description: Assesses each knowledge source an agent will ground on for owner, currency, accuracy, permissions and oversharing, classification and review cycle, and records a ready, ready-with-conditions or not-ready verdict. Use when an agent brief names its sources, when a maker wants to add a site or library as knowledge, or when an agent starts giving outdated or surprising answers.
license: CC-BY-4.0
metadata:
  department: m365-agents
  lifecycle: Deliver, Assure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, sharepoint, purview
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-agent-builder, ms-copilot-privacy, ms-declarative-agents, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# Knowledge source readiness

## Purpose

An agent can only be as good as the content it grounds on, and it will repeat a wrong, stale or overshared document with
the same confidence as a correct one. This skill checks each knowledge source named in an agent brief before the agent
is built or extended, and records whether it is ready, ready with conditions, or not ready. The common failure is to
point an agent at a whole site because "the answers are in there", then discover that the site holds three versions of
the same policy and a folder of salary data shared with everyone.

## When to use

- An agent brief lists its knowledge sources and they need a verdict before build.
- A maker wants to add a site, library, folder, file set or public website as knowledge.
- A live agent starts giving outdated, contradictory or unexpected answers.
- A periodic review of a live agent is due and its sources need re-checking.

## When not to use

- Writing the agent's purpose, scope and source list in the first place - use `m365-agents:agent-use-case-design`.
- Testing whether the agent's answers are correct and grounded - use `m365-agents:agent-testing`.
- The formal security review of what the agent can expose from tier 2 - use `security-privacy:data-exposure-review`.
- Fixing the content, owner model and lifecycle across the organisation's knowledge estate - use `knowledge-management:knowledge-lifecycle`.
- Classification schemes and data ownership beyond the agent's own sources - use `data-governance:data-classification-for-ai`.

## Questions to ask first

1. Who owns this content today, by name or role, and do they know an agent will answer from it?
2. When was it last reviewed, and how would anyone know if it were wrong or out of date?
3. Who can open it now, and is that the same group as the agent's intended audience?
4. Is there more than one version of the truth on this topic, and which one is authoritative?
5. Does it contain personal, confidential or commercially sensitive material, and is it labelled as such?

## Required inputs

- The agent brief from `m365-agents:agent-use-case-design`, with audience, purpose and candidate sources.
- Access to inspect each source's content, structure, version history and permissions, or a site owner who can.
- The organisation's classification scheme and sensitivity labels, if any.
- The representative user questions from the brief, to check coverage.

Where the owner cannot be found or permissions cannot be inspected, the verdict is "not ready" until they are; never
assume content is current or correctly shared because nobody has complained.

## Decision framework

Score each source on six criteria. Any "fail" on owner or permissions makes the source not ready; other fails make it
ready with conditions, each condition owned and dated.

| Criterion | Pass | Fail |
|---|---|---|
| Owner | A named owner accepts accountability for accuracy and review | No owner, or owner unaware of the agent |
| Currency | Reviewed within the agreed cycle; superseded items removed or marked | No review date; old versions sit beside current ones |
| Accuracy | Owner confirms content is authoritative; spot checks agree | Contradictions found, or drafts mixed with approved content |
| Permissions | Access matches the intended audience; no broad sharing links or inherited "everyone" access | Content is wider-shared than its sensitivity warrants |
| Classification | Sensitivity labelled or recorded, and compatible with the audience | Sensitive content unlabelled, or label conflicts with audience |
| Review cycle | A cycle is set and linked to the agent's review date | No cycle, so decay is invisible |

Coverage is a seventh, softer check: if the representative questions cannot be answered from ready sources, the gap is
recorded, not filled by widening the source.

## Practitioner approach

Begin with the sources the brief already names and resist additions until each has a verdict. For every source, find
the owner first. If the owner is a former employee or "the team", stop and agree a named owner before going further;
an unowned source is the single best predictor of an agent that decays within months.

Next, look at the content as the agent will. Open the library or site and sort by modified date. Look for drafts,
duplicates, documents titled "old" or "v2 final", and archived folders that are still in scope. Pick five of the
representative questions and find the answer by hand. If you find two different answers, the source is not ready;
the agent will pick one, and users will not know which.

Then check permissions properly, because grounding is permission-trimmed: the agent shows each user only what they
could already open, but it makes everything they can open far easier to find. Content that was overshared but obscure
becomes overshared and discoverable. Check site membership, sharing links, inherited permissions and any
"everyone except external users" grants. Compare that with the intended audience in the brief. Where access is wider
than the content's sensitivity allows, the fix is to correct the permissions at source, never to rely on the agent's
instructions to keep quiet.

Record the classification. If the organisation uses sensitivity labels, note the labels in use and whether any
content is unlabelled. If it does not, record the owner's view of sensitivity in plain words. Personal data in any
source is flagged for `security-privacy:privacy-assessment`.

For public websites as knowledge, record which sites, who decided they are trustworthy, and how users will tell a web
answer from an internal one. For files uploaded directly into an agent, record who will replace them when they change,
because uploaded copies do not update themselves.

Agree a review cycle with each owner and link it to the agent's review date, so a policy change triggers an agent
check. Write the verdicts into the knowledge section of the agent brief, with conditions, owners and dates.

Finally, be honest about what this skill cannot fix. Cleaning a sprawling site, rationalising versions or designing an
owner model across the estate is knowledge management work. Hand it to `knowledge-management:knowledge-cleanup`
and keep the agent's scope to the sources that are ready now. A narrower agent on good knowledge beats a broad agent on
poor knowledge every time.

## Outputs

- The knowledge section of the `agent-brief`: each source with owner, location, audience, currency, accuracy, permissions, classification, review cycle and verdict.
- A list of conditions to resolve before release, each with an owner and a date.
- Referrals for permission fixes, personal data and estate-wide knowledge problems.

## Microsoft platform considerations

Agents can ground on SharePoint and OneDrive content, connector-indexed content, uploaded files and public web content,
depending on the route and configuration; the options, limits and how each source is permission-trimmed differ by route
and change over time. Confirm them in the source records (`ms-agent-builder`, `ms-copilot-privacy`) before advising.
Where Microsoft Purview sensitivity labels are in use, record how labelled content behaves for the chosen route from the
current documentation, not from memory.

## Adoption considerations

Knowledge owners are part of the agent's success, not a compliance step. Tell them what questions the agent will answer
from their content and how they will hear about wrong answers. Owners who see their content used tend to keep it
current.

## Knowledge considerations

This skill is the knowledge check for an individual agent. Problems that span many agents or sites belong to
`knowledge-management:knowledge-readiness-assessment`; record them as estate-level findings so they are not fixed one agent at a
time.

## Security and privacy considerations

Oversharing is the main risk. Every source wider-shared than its sensitivity warrants is a not-ready verdict and, from
risk tier 2, goes to `security-privacy:data-exposure-review`. Personal data goes to `security-privacy:privacy-assessment`.

## Responsible AI considerations

Knowledge that encodes outdated or biased practice (for example an old hiring guide) will be repeated by the agent as
current guidance. Ask owners whether any content reflects practice the organisation no longer stands behind, and remove
it from scope.

## Evaluation requirements

Each condition must be verifiable: a permission change can be re-checked, a superseded document can be shown removed.
Pass the representative questions and known contradictions to `m365-agents:agent-testing` as test cases.

## Value measures

Track, per agent, the share of sources with a named owner and an in-date review, and the number of wrong-answer reports
traced to knowledge rather than configuration. The agent's business owner owns these; report at agent level, never by
individual author.

## Scale notes

### Starter

Check two or three curated sources by hand with their owners in a single session. Prefer a small set of approved
documents to a whole site.

### Scale

Make the readiness verdict a mandatory field in the agent brief and reuse verdicts across agents that share a source,
with a shared list of owned, ready sources.

### Enterprise

Feed verdicts into the knowledge inventory run through `knowledge-management:knowledge-inventory`, and require an
in-date verdict at each agent review. Use oversharing reports from the platform team to prioritise checks.

## Hand-offs

- Back to `m365-agents:agent-use-case-design` with verdicts and any scope change.
- To `m365-agents:agent-testing` with contradictions and coverage gaps as test cases.
- To `security-privacy:data-exposure-review` for oversharing from risk tier 2, and `security-privacy:privacy-assessment` for personal data.
- To `knowledge-management:knowledge-cleanup` for estate-wide clean-up.

## Reviewer gates

From risk tier 2, `security-privacy` reviews any source flagged for permissions, classification or personal data, and
its blocking findings must be resolved before release. Below tier 2 the agent owner signs the verdicts.

## Failure modes

- A whole site is accepted because the owner is confident, and old versions surface in answers.
- Permissions are checked at the site level only, missing sharing links on individual files.
- Uploaded files are never refreshed, so the agent quotes last year's policy.
- The review cycle is agreed but not linked to the agent, so content changes and nobody re-tests.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Mark a source ready without a named owner who knows the agent uses it.
- Rely on agent instructions to hide content that users should not be able to open.
- Widen the knowledge scope to fill a coverage gap without a new verdict.
- Assert how a grounding source behaves from memory rather than the current source records.

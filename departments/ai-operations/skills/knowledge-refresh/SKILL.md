---
name: knowledge-refresh
description: Keeps a live agent's knowledge current in operation - detecting source changes, moves and expiry, applying routine and urgent refreshes, confirming the solution picks up the change, retiring superseded content and re-running affected evaluation items. Use when a policy or document an agent relies on changes, when answers lag behind updated content, or when a knowledge library is moved or restructured under a live agent.
license: CC-BY-4.0
metadata:
  department: ai-operations
  lifecycle: Measure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, copilot-cowork, ai-foundry, sharepoint
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-declarative-agents, ms-agent-builder, ms-copilot-studio-guidance, ms-copilot-privacy, ms-foundry-models
  status: draft
  authors: Simon Foote
---

# Knowledge refresh

## Purpose

An agent is only as current as the knowledge it grounds on, and knowledge changes on its owners' schedule, not the
agent's. This skill keeps a live solution's knowledge current in operation: it detects when sources change, move or
expire, applies routine and urgent refreshes, confirms the solution actually reflects the change, removes superseded
content from reach and re-runs the evaluation items that depend on it. Refresh usually fails because the knowledge owner
updates a policy without knowing an agent depends on it, because the old version stays reachable alongside the new, or
because nobody checks that the agent picked up the change.

## When to use

- A policy, procedure or document that a live agent grounds on has changed or is about to.
- Users report answers that lag behind content they know has been updated.
- A knowledge library, site or index under a live agent is being moved, restructured or retired.
- A source has passed its review date and monitoring has flagged it.
- An urgent correction must reach a live agent quickly, for example a safety or legal change.

## When not to use

- Setting the review cycles and owners for knowledge in the first place - use `knowledge-management:knowledge-review-cycles`.
- Checking a source is ready before an agent is built or released - use `m365-agents:knowledge-source-readiness`.
- Managing content from creation to archive across the estate - use `knowledge-management:knowledge-lifecycle`.
- Clearing redundant, outdated and trivial content at scale - use `knowledge-management:knowledge-cleanup`.
- Judging the regression results after a refresh - use `evaluation-quality:regression-evaluation`.

## Questions to ask first

1. Which live solutions depend on this source, and does its owner know?
2. Is the change routine, or must it reach users urgently because the old answer could cause harm?
3. How does each solution connect to this source, and how does that route pick up changes?
4. Will the old version remain reachable anywhere a solution grounds on?
5. Which evaluation items depend on the changed content?

## Required inputs

- A dependency record linking each live solution to its knowledge sources and their owners, from the solution runbook or inventory.
- The change: what changed, when it takes effect, and whether it supersedes earlier content.
- The golden dataset with items mapped to sources.
- The route's current behaviour for picking up changes, confirmed in the source records.

Where no dependency record exists, build one before the next change; until then, ask the knowledge owner to notify the
solution owner of every substantive change and record the gap.

## Decision framework

Classify the refresh and act accordingly.

| Refresh type | Trigger | Action | Evidence |
|---|---|---|---|
| Routine | Scheduled review, minor edit, new supporting document | Update source, confirm pickup, run affected items at the next cycle | Items re-run and passed |
| Substantive | Policy or procedure change, new version superseding old | Update source, retire or restrict old version, confirm pickup, run affected items and regression subset before announcing | Regression result and owner confirmation |
| Urgent | Old answer could cause harm, legal or safety exposure | Contain first (warn users, restrict or remove the source), then update and confirm | Incident or change record with containment and re-test |
| Structural | Library moved, renamed, restructured or retired | Re-point the solution, check permissions, confirm grounding, run full set for affected topics | Full result for affected topics |
| Expiry | Source past review date with no owner response | Escalate to the business owner; restrict or warn if content is high consequence | Decision record |

Superseded content is removed from reach or clearly restricted; instructions telling the agent to prefer newer files
are not a substitute.

## Practitioner approach

Make dependencies visible to knowledge owners. The most common refresh failure is that the person updating the policy
does not know an agent relies on it. For each live solution, record its sources and owners, and give each owner a short
note: "These agents ground on your content; tell this person before you change or move it." Where the platform or
inventory can show dependencies, use it, and confirm the capability in the source records.

Agree a notification habit with each knowledge owner. Substantive changes are announced to the solution owner before
publication where possible, so the regression run can follow quickly. Routine edits can wait for the next scheduled
check.

Know how each route picks up changes. Content connected live, uploaded files, indexed sites and retrieval indexes
behave differently, and timing changes as products evolve. Confirm the current behaviour for each solution's route in
the source records, and write it into the runbook. Never assume an upload updates itself.

Retire the old version. When a new policy supersedes an old one, the old one must be removed from reach, moved to a
restricted archive or clearly marked superseded in a way the solution does not ground on. Leaving both reachable
produces answers that blend them.

Confirm pickup before announcing. After the change, ask the affected questions and check the answer and citation
reflect the new content. Then run the dataset items mapped to the source and, for substantive changes, the regression
subset. Update expected answers in the golden dataset with the knowledge owner's confirmation first; otherwise the
evaluation will mark the correct new answer as wrong.

Handle urgent changes as containment. If the old answer could cause harm, warn users or restrict the source immediately
through the incident route, then refresh and confirm. Do not wait for a routine cycle.

Watch structural changes closely. Site migrations, library reorganisations and permission changes often break grounding
silently. Ask the platform or site owner to include live solutions in their change impact checks, and run the full set
for affected topics afterwards.

Record each refresh: what changed, which solutions were affected, evidence of pickup and test results. Bring overdue
sources and repeated refresh problems to the scheduled reviews.

## Outputs

- A knowledge dependency record per solution: sources, owners, connection route and pickup behaviour, kept in the runbook.
- A refresh log with type, change, solutions affected, superseded content handled, pickup evidence and test results.
- Updated golden dataset expected answers, confirmed by the knowledge owner.
- Escalations for expired or ownerless sources.

## Microsoft platform considerations

How agents connect to SharePoint, uploaded files, connectors and indexes, and how quickly changes appear, differ by
route and change over time. Confirm current behaviour in `ms-declarative-agents`, `ms-agent-builder`,
`ms-copilot-studio-guidance` and `ms-foundry-models`. Permission changes during refresh affect what users can be shown;
check `ms-copilot-privacy` for how grounding respects permissions.

## Adoption considerations

When a significant change reaches an agent, tell its users. A short note that the agent now reflects the new policy
builds confidence and stops people double-checking every answer.

## Knowledge considerations

This skill is knowledge operations for live solutions. It relies on the review cycles and owners set by
`knowledge-management:knowledge-review-cycles`; recurring problems such as duplicates or unclear versioning go back to
the `knowledge-management` department to fix at estate level.

## Security and privacy considerations

Moves and restructures often change permissions. Check that a refreshed or relocated source is not more widely shared
than before, and raise any widening with `security-privacy:data-exposure-review`.

## Responsible AI considerations

Out-of-date answers about entitlements, eligibility or safety can harm people. Treat those changes as substantive or
urgent, and make sure users are told when answers they may have relied on have changed.

## Evaluation requirements

Every substantive, urgent or structural refresh is followed by affected items and, where required, the regression subset
through `evaluation-quality:regression-evaluation`, with expected answers updated and confirmed first.

## Value measures

Track time from source change to confirmed pickup, the share of sources within their review date, the number of answers
reported as out of date, and refreshes with test evidence. The AI Operations Lead and knowledge owners share these
measures, reported by solution and source, never by individual.

## Scale notes

### Starter

A list of each agent's sources and owners, a standing request to tell the agent owner before changing them, and a few
check questions asked after each change.

### Scale

Dependency records in every runbook, refresh types and evidence standardised across solutions, and regression runs after
substantive changes.

### Enterprise

Dependencies held in the solution inventory and linked to content management, notifications automated where the
platform allows, and refresh performance reported across the portfolio.

## Hand-offs

- To `evaluation-quality:regression-evaluation` after substantive, urgent or structural refreshes.
- To `ai-operations:ai-incident-management` when an urgent change needs containment.
- To the `knowledge-management` department, through `knowledge-management:knowledge-lifecycle`, for estate-level fixes.
- To `ai-operations:ai-review-calendar` with overdue and ownerless sources.

## Reviewer gates

Not applicable as a gate; refresh is an operating practice. Evidence from refresh feeds `evaluation-quality` regression
work, and permission widening found during refresh goes to `security-privacy`.

## Failure modes

- The knowledge owner updates a policy without knowing an agent depends on it, and the agent answers from the old version for weeks.
- Old and new versions both remain reachable, and answers blend them.
- A library is migrated and the agent silently loses its grounding.
- Expected answers in the golden dataset are not updated, so the correct new answer fails regression.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Leave superseded content reachable and rely on instructions to prefer the newer version.
- Announce a refresh without confirming the solution reflects the change.
- Wait for a routine cycle when an outdated answer could cause harm.
- Assume a route picks up changes automatically without checking the current source.

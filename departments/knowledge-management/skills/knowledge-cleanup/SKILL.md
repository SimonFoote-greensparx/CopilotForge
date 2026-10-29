---
name: knowledge-cleanup
description: Plans a clean-up of redundant, outdated and trivial content in the knowledge estate - triage rules, owner decisions to keep, update, archive or delete, retention checks, sequencing ahead of Copilot and agent rollout, and proof the clean-up worked. Use when duplicates and old versions surface in AI answers, before a Copilot wave reaches a cluttered domain, or when a site needs rationalising before agents ground on it.
license: CC-BY-4.0
metadata:
  department: knowledge-management
  lifecycle: Mobilise, Enable, Deliver, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: sharepoint, purview, m365-copilot, m365-agents
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-privacy, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# Knowledge clean-up

## Purpose

Most knowledge estates carry years of redundant copies, outdated versions and trivial files, and AI makes them visible:
Copilot and agents surface the old version as readily as the new one. This skill plans a bounded clean-up that removes
or archives that clutter where it harms AI answers, with owners making the decisions and retention rules respected. It
goes wrong when clean-up becomes an open-ended tidy of everything, when content is deleted without checking records
obligations, or when nobody can show afterwards that answers improved.

## When to use

- Duplicates, drafts and superseded versions are appearing in Copilot or agent answers.
- A Copilot rollout wave is about to reach a domain known to be cluttered.
- A site or library must be rationalised before an agent grounds on it.
- A readiness assessment or quality check rated a domain poor on currency or authority.

## When not to use

- Setting the ongoing review cadence that stops clutter returning - use `knowledge-management:knowledge-review-cycles`.
- Designing the end-to-end lifecycle including archive and disposal rules - use `knowledge-management:knowledge-lifecycle`.
- Setting retention rules for data created or used by AI - use `data-governance:ai-data-retention-rules`.
- Correcting overshared permissions as a security matter - use `security-privacy:data-exposure-review`.
- Redesigning sites and libraries after the clean-up - use `knowledge-management:sharepoint-knowledge-design`.

## Questions to ask first

1. Which domains and locations are in scope, and which AI uses are being harmed or are about to depend on them?
2. What retention and records obligations apply to this content, and who confirms them?
3. Who can decide, for each location, whether content is kept, updated, archived or deleted?
4. Is there an archive location, and will content there be excluded from AI grounding?
5. How will you show the clean-up worked - which questions or answers should change?

## Required inputs

- The locations in scope with owners, from `knowledge-management:knowledge-inventory`.
- Retention schedules and any legal hold status, from records management or the legal adviser.
- Representative questions whose answers are affected by clutter, as the before-and-after test.
- Administrative reports of activity, versions and duplicates for the locations in scope, where available.

If retention obligations are unknown, nothing is deleted; content may be archived or restricted until they are
confirmed. Where an owner cannot be found, escalate to the domain owner rather than deciding on their behalf.

## Decision framework

Triage each item or folder into one category, then apply the owner's decision.

| Category | Signals | Default action | Decision by |
|---|---|---|---|
| Redundant | Duplicate or copy of authoritative content elsewhere | Delete the copy, or replace it with a link | Content owner |
| Outdated | Superseded version, withdrawn policy, old product, past event | Archive outside AI scope, or delete if retention allows | Content owner, with records check |
| Trivial | Personal notes, temporary files, test uploads, no lasting value | Delete if retention allows | Content owner or steward |
| Working | Drafts and collaboration material in an authoritative location | Move to a working area | Content owner |
| Current but flawed | Still needed, but inaccurate or unclear | Keep and fix through quality remediation | Content owner |
| Current and good | Authoritative and in date | Keep and mark as authoritative | Content owner |

Never delete content under legal hold or within a retention period. Archive means moved to a location excluded from
AI grounding and broad access, not merely renamed "old".

## Practitioner approach

Bound the clean-up by AI use. Start with the domains that current or planned agents and Copilot scenarios depend on,
and with the representative questions that currently return conflicting or stale answers. That gives a clear finish
line and a test of success. An estate-wide clean-up with no finish line loses its sponsor within months.

Get records management in the room before anyone deletes anything. Confirm retention periods and any legal holds for
each location, and agree the archive location with them. The safest default for uncertain content is to archive and
restrict, not delete; deletion can follow once obligations are clear.

Use reports to triage at scale and owners to decide. Activity and modification reports separate content nobody has
opened in years from content in daily use; duplicate detection, file names containing "old", "copy" or "v2 final", and
version sprawl point to redundant and outdated material. Present owners with a pre-triaged list and default actions so
their job is to confirm or override, not to start from a blank page. Owners decide; the knowledge team proposes.

Run the clean-up in short sprints by domain. Each sprint has a scope, a deadline, a list of decisions and a
before-and-after check: the representative questions are asked again and answers compared. Short sprints keep owners
engaged and let you show progress quickly.

Treat permissions alongside clutter. Many outdated folders are also overshared; archiving them into a restricted
location fixes both. Record any sensitive content found during clean-up and route it to the security reviewers rather
than quietly moving it.

Stop the clutter returning. A clean-up without lifecycle changes is a one-off. Before closing each sprint, agree with
owners a working area for drafts, a review cycle for what remains, and an archive routine, through
`knowledge-management:knowledge-lifecycle` and `knowledge-management:knowledge-review-cycles`. Record the outcome in
the knowledge register.

## Outputs

- A clean-up plan: scope by domain, triage rules, retention checks, archive location, sprint schedule and success tests.
- Owner decision logs per location: item or folder, category, decision, decided by, date.
- A before-and-after record of representative questions for each sprint.
- Updates to the `knowledge-asset-register` and lifecycle actions to prevent recurrence.

## Microsoft platform considerations

SharePoint administrative reports and Microsoft Purview retention and records features help find inactive content and
apply retention correctly; which reports and features the organisation has depends on configuration and licensing, so
confirm them with administrators and the licensing guide. Archived content must be excluded from the locations agents
ground on and from broad access; check in the source records how each grounding route treats moved, restricted or
archived content rather than assuming.

## Adoption considerations

Owners engage when clean-up is quick and the result is visible. Show them the before-and-after answers. Communicate
archive locations clearly so users do not believe content has been lost.

## Knowledge considerations

Clean-up resets the estate; `knowledge-management:knowledge-lifecycle` and `knowledge-management:knowledge-review-cycles`
keep it clean. Update the knowledge register as locations are retired, merged or marked authoritative.

## Security and privacy considerations

Clean-up often uncovers overshared and sensitive content. Record it and route it to `security-privacy:data-exposure-review`;
personal data held beyond its purpose goes to `security-privacy:privacy-assessment`. Deletion decisions involving
personal data or legal obligations are confirmed with the DPO or legal adviser.

## Responsible AI considerations

Outdated content that reflects practice the organisation no longer stands behind is a priority for archive, because AI
will present it as current guidance.

## Evaluation requirements

Each sprint is judged by its before-and-after questions: fewer conflicting answers, no superseded versions cited.
Pass the questions to `m365-agents:agent-testing` for agents that ground on the cleaned domains.

## Value measures

Track the volume archived or removed in AI-dependent locations, the share of representative questions with one
authoritative answer before and after, and wrong-answer reports traced to stale content. The Knowledge Manager owns these,
reported by domain.

## Scale notes

### Starter

Clean up the one or two libraries the first agent uses, with their owner, in a single short sprint.

### Scale

Run domain sprints aligned to Copilot rollout waves, with records management and a shared archive location.

### Enterprise

Run a programme of clean-up sprints by business unit, using administrative reports to target effort, and link
completion to the readiness verdicts that gate further AI expansion.

## Hand-offs

- To `knowledge-management:knowledge-lifecycle` and `knowledge-management:knowledge-review-cycles` to stop clutter returning.
- To `knowledge-management:sharepoint-knowledge-design` where the structure itself causes clutter.
- To `security-privacy:data-exposure-review` for sensitive or overshared content found.

## Reviewer gates

From risk tier 2, `security-privacy` reviews sensitive content found during clean-up and any deletion involving personal
data; its blocking findings must be resolved first. Below tier 2 the content owner signs the decision log.

## Failure modes

- Clean-up has no boundary or finish line and loses sponsorship.
- Content is deleted within a retention period or under legal hold.
- Archived content stays in a location agents ground on, so old versions still appear.
- Nothing changes in the lifecycle, and the clutter returns within a year.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Delete content before retention obligations and legal holds are confirmed.
- Make keep or delete decisions on an owner's behalf.
- Call content archived while it remains in scope for AI grounding or broad access.
- Run clean-up without a before-and-after test of the answers it is meant to improve.

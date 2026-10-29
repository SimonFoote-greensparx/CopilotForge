---
name: knowledge-lifecycle
description: Designs the end-to-end knowledge lifecycle - create, approve, publish, use, review, update, archive and dispose - with the states, metadata, roles and controls at each stage, so knowledge AI grounds on enters correctly, stays current and leaves cleanly. Use when there is no consistent route from draft to published to archived, when superseded content lingers beside current, or when setting knowledge management up for AI.
license: CC-BY-4.0
metadata:
  department: knowledge-management
  lifecycle: Mobilise, Enable, Deliver, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: sharepoint, purview, power-platform, m365-agents
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-privacy, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# Knowledge lifecycle

## Purpose

AI grounding exposes every weakness in how knowledge is born, maintained and retired: drafts treated as approved,
superseded policies left in place, content that nobody ever disposes of. This skill designs one lifecycle that all
knowledge follows, with clear states, the controls that move content between them, and the roles responsible at each
step, so that what AI finds is approved, current and still wanted. It goes wrong when the lifecycle exists only as a
diagram, when every stage needs a committee, or when the end of life is left out entirely.

## When to use

- There is no consistent route from draft to published to archived, and each team does something different.
- Superseded content lingers beside current content and AI quotes both.
- Knowledge management is being set up or reset as part of an AI programme.
- After a clean-up, to stop clutter returning.

## When not to use

- Setting how often each kind of content is reviewed and how overdue reviews escalate - use `knowledge-management:knowledge-review-cycles`.
- A one-off clean-up of existing redundant, outdated and trivial content - use `knowledge-management:knowledge-cleanup`.
- Managing an agent from release to retirement - use `m365-agents:agent-lifecycle`.
- Retention rules for data created or used by AI - use `data-governance:ai-data-retention-rules`.

## Questions to ask first

1. What kinds of knowledge does the organisation produce, and do any need formal document control (regulated procedures, policies)?
2. Who may publish content as authoritative today, and how is approval recorded?
3. What retention and records obligations apply, and who owns the records schedule?
4. What happens to content when it is superseded - is it archived, deleted, or left in place?
5. Which stages can be automated, and which need a person's judgement?

## Required inputs

- The ownership model, from `knowledge-management:knowledge-owner-model`, so each stage has a responsible role.
- The classification scheme and knowledge status values, from `knowledge-management:knowledge-classification`.
- Retention schedules and records requirements, from records management or the legal adviser.
- The site and library structure, from `knowledge-management:sharepoint-knowledge-design`, or the current structure if not yet redesigned.

Where retention obligations are unknown, the lifecycle stops at archive and records disposal as "to confirm"; it never
sets disposal periods by assumption.

## Decision framework

Define states, the control that moves content to the next one, and whether it is in AI grounding scope.

| State | Entry control | Responsible role | In agent grounding scope |
|---|---|---|---|
| Draft | Created in a working area from a template | Author | No |
| In review | Submitted for approval; subject matter review where required | Content owner, subject matter reviewer | No |
| Published (authoritative) | Approved; required metadata complete; classification set | Content owner | Yes, if the source is approved for grounding |
| Under revision | Material change in progress; published version remains until replaced | Author, content owner | Published version only |
| Superseded | Replaced by a newer version, or withdrawn | Content owner | No |
| Archived | Moved to a restricted archive location | Steward | No |
| Disposed | Retention period ended; disposal approved | Records owner | No |

Proportionality rule: content with high consequence (policy, regulated procedures, guidance informing decisions about
people, money or safety) needs recorded approval and subject matter review; low-consequence content can be published
by its content owner directly.

## Practitioner approach

Map the current reality before designing. Pick three common kinds of content and trace how each actually moves today:
who drafts, where, who approves, how it is published, what happens when it changes and when it is no longer needed. The
gaps are usually at the ends. Publication is informal, so drafts sit beside approved content, and nothing leaves, so
the estate only grows.

Design the states so that location and status agree. The simplest robust design uses separate locations for working,
authoritative and archive content, with publishing as a move or a controlled publish step rather than a renamed file.
That makes the state visible to people, to administrators and to AI grounding without relying on anyone reading a
status column.

Make entry to the published state the control point. At publication, required metadata is completed (owner, status,
effective date, review date, audience), classification is set, and the previous version is superseded in the same step.
That last action is the one most often missed and the one that matters most for AI: if publishing a new policy does not
retire the old one, agents will find both.

Keep control proportionate. Formal approval and subject matter review belong to high-consequence content; requiring
them for every team guide makes people publish around the process. Let content owners publish low-consequence content
directly, with review cycles catching decay.

Design the end of life deliberately. Superseded content moves to archive promptly, outside grounding scope and broad
access. Disposal follows the retention schedule, approved by the records owner, never by the knowledge team alone. Where
records management already runs a disposal process, connect to it rather than creating another.

Automate what is mechanical and leave judgement to people. Reminders, state changes, moving superseded items to archive
and notifying owners of dependent agents can be automated; approval, accuracy and disposal decisions stay with roles.
Document the lifecycle on one page with the table above, a diagram and the role for each step, and build it into site
templates so new knowledge sites follow it from the start.

Finally, connect it to AI. When content is published, superseded or archived, the owners of agents grounding on that
source need to know, because some routes index content and some uploaded copies never update. A notification to
dependent agent owners at state change closes that loop.

## Outputs

- A knowledge lifecycle standard: states, entry controls, responsible roles, grounding scope and proportionality rules, on one page with a diagram.
- Lifecycle configuration for knowledge sites: working, authoritative and archive locations, required metadata, and automated steps.
- A change notification routine linking state changes to dependent agents recorded in the `knowledge-asset-register`.

## Microsoft platform considerations

SharePoint version history, content approval, page publishing, required columns and Power Automate can implement states
and controls; Microsoft Purview retention and records features support archive and disposal. The features available
depend on configuration and licensing, so confirm them with administrators and the licensing guide. How quickly each
grounding route reflects a published, moved or deleted item varies; check the source records rather than assuming
changes appear immediately.

## Adoption considerations

Authors follow a lifecycle that is easier than the workaround. Provide templates, a one-click route to publish, and a
clear answer to "where do drafts go?". Explain that the payoff is AI answers people can trust.

## Knowledge considerations

The lifecycle is the frame for the department's other skills: `knowledge-management:knowledge-review-cycles` runs the
review stage, `knowledge-management:knowledge-cleanup` deals with the backlog the lifecycle prevents, and
`knowledge-management:ai-ready-content` shapes what is drafted.

## Security and privacy considerations

Classification is set at publication and re-confirmed at review; archive locations are restricted. Disposal involving
personal data follows the retention schedule and is confirmed with the DPO where unclear.

## Responsible AI considerations

High-consequence content that informs decisions about people, money or safety needs recorded approval and prompt
supersession, because AI applying a withdrawn rule to people causes harm.

## Evaluation requirements

Sample published content quarterly: does each item have required metadata, has its predecessor been superseded, and is
archive content out of grounding scope? Record the result by domain.

## Value measures

Track the share of authoritative locations with superseded versions removed, the time from new version publication to
retirement of the old one, and wrong-answer reports traced to superseded content. The Knowledge Manager owns these,
reported by domain.

## Scale notes

### Starter

Agree three locations (working, authoritative, archive) and a simple publish-and-supersede step for the domains the first
agents use.

### Scale

Apply the lifecycle standard across domains through site templates, with automated reminders and archive moves and
notifications to dependent agent owners.

### Enterprise

Align the lifecycle with records management and document control across business units, with formal approval for
high-consequence content and lifecycle compliance reported to steering.

## Hand-offs

- To `knowledge-management:knowledge-review-cycles` to set review cadence within the lifecycle.
- To `knowledge-management:sharepoint-knowledge-design` to implement locations and metadata.
- To `ai-operations:knowledge-refresh` for agents affected by state changes.

## Reviewer gates

Not applicable as a release gate; the lifecycle governs content rather than releasing AI solutions. Disposal decisions
pass through records management, and the DPO where personal data is involved.

## Failure modes

- Publishing a new version does not supersede the old, and agents cite both.
- Every item needs committee approval, so people publish outside the process.
- Archive exists in name only and archived content stays in grounding scope.
- Disposal periods are set by the knowledge team without records management.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Leave superseded content in an authoritative location.
- Set retention or disposal periods without the records owner.
- Require heavyweight approval for low-consequence content.
- Assume a state change reaches every agent immediately.

---
name: grounding-readiness
description: Checks that the specific files, folders, mail, meetings and data a Copilot Cowork task will draw on are current, single-version, owned and shared no wider than they should be, and gives each a ready, ready-with-conditions or not-ready verdict before the task runs. Use when a task design names its sources, when Cowork outputs quote outdated or conflicting material, or before a shared task design is reused by others.
license: CC-BY-4.0
metadata:
  department: copilot-cowork
  lifecycle: Deliver, Assure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: copilot-cowork, m365-copilot, sharepoint, purview
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-privacy, ms-copilot-cowork-customise, ms-copilot-overview
  status: draft
  authors: Simon Foote
---

# Grounding readiness

## Purpose

Copilot Cowork works from the files, mail, meetings and data the delegating person can reach, and it will treat a stale
draft or an overshared spreadsheet with the same confidence as the approved version. This skill checks the specific
sources a Cowork task relies on before the task runs or is shared, and records a verdict for each. It is narrower than an
estate-wide knowledge review and faster than an agent knowledge assessment: it asks whether these sources are fit for
this task, today. It goes wrong when the check is skipped because "it is only my own files", which is exactly where
duplicate versions and forgotten sharing links live.

## When to use

- A task design names its sources and they need a verdict before the task runs or is shared.
- Cowork outputs quote outdated figures, superseded policies or conflicting versions.
- A task design built by one person is about to be reused by a team with different access.
- A direction checkpoint reported missing or contradictory sources.

## When not to use

- Assessing the knowledge sources a reusable agent will ground on - use `m365-agents:knowledge-source-readiness`.
- Preparing the organisation's wider Microsoft 365 work context (permissions, oversharing, settings) for Copilot - use `m365-copilot:work-context-readiness`.
- Assessing the readiness of the knowledge estate as a whole - use `knowledge-management:knowledge-readiness-assessment`.
- Naming which sources the task should use in the first place - use `copilot-cowork:task-context-design`.
- A formal security review of what sensitive content a task could expose - use `security-privacy:data-exposure-review`.

## Questions to ask first

1. Which exact sources does the task use, and who maintains each one?
2. Is there one current version of each, or do drafts, copies and attachments of older versions sit alongside it?
3. Who else can open each source, and does that match who should see the task's output?
4. When was each source last updated, and is that recent enough for this task?
5. Will everyone who reuses the task design have the same access, or will the task behave differently for different people?

## Required inputs

- The list of sources from the task design produced in `copilot-cowork:task-context-design`.
- The intended audience of the task's output.
- Any sensitivity labels or classifications applied to the sources, where the organisation uses them.
- For shared task designs, the roles who will reuse it.

If a source's owner or currency cannot be established, record it as to confirm and give it a not-ready or conditional
verdict. Never assume a source is current because it is the one the delegator usually opens.

## Decision framework

Give each source a verdict against six checks.

| Check | Ready | Ready with conditions | Not ready |
|---|---|---|---|
| Single version | One authoritative copy, others clearly archived | Duplicates exist but can be excluded by naming | Several live versions with no way to tell which is current |
| Currency | Updated within the period the task needs | Slightly old, gap noted in output | Out of date for the task's purpose |
| Owner | A person or role maintains it | Owner known but not confirmed | Nobody maintains it |
| Access matches audience | Access is no wider than the output's audience needs | Minor oversharing being fixed | Sensitive content shared far more widely than intended |
| Classification | Label or sensitivity known and compatible with the output | Unlabelled but low sensitivity | Sensitive and unlabelled, or label conflicts with output audience |
| Consistent for reusers | All reusers have equivalent access | Differences documented and harmless | Reusers would see materially different content |

A task can run when every source is ready or ready with conditions and the conditions are recorded in the task design.
Any not-ready source is excluded, fixed or replaced before the task runs.

## Practitioner approach

Start with the task design's source list and open each source as the delegator would. Look for the obvious problems
first: a folder holding "final", "final v2" and "final approved", a mail thread where the figures changed half-way, a
meeting series whose notes stopped being taken three months ago. These are the sources of most poor Cowork outputs, and
they are usually quicker to fix than to work around.

Decide which version is authoritative and make that unambiguous. Where possible, move superseded material into an
archive location and name it in the task design's exclusions. Where that is not possible, name the authoritative file
explicitly. Ask the owner, not the delegator, which version is current; the delegator often uses whichever opened last.

Check currency against the task's purpose. A pricing sheet updated last year may be fine for a historical comparison and
wrong for a quotation. If a source is out of date and cannot be refreshed in time, the task can still run if the output
states the gap plainly; record that as a condition.

Look at sharing with the output in mind. Cowork works within the delegator's permissions, so it will not reach what they
cannot open, but it can draw content from a widely shared file into an output meant for a narrower or a different
audience, or surface something the delegator could open but was never meant to. If a source holding personal or
confidential data is shared more widely than its sensitivity justifies, fix the sharing at source and raise it with the
owner; do not rely on the task to avoid it.

For task designs that others will reuse, check access for the reusing roles. If one team sees a restricted folder and
another does not, the same design will produce different outputs for each, and neither may notice. Either align access
deliberately or narrow the sources to those everyone shares.

Record the verdicts in the task design, with conditions, owners and dates. Feed recurring problems, such as a site with
no owner or a library full of duplicates, to the `knowledge-management` department so they are fixed for everyone. A
grounding check is quick when sources are healthy; when it is slow, that is a finding in itself.

## Outputs

- A source readiness table in the `cowork-task-design` template: each source with its verdict, conditions, owner and date.
- Exclusions and authoritative-version notes for the task context.
- A list of source problems referred to the source owner or the `knowledge-management` department.

## Microsoft platform considerations

Cowork grounds on Microsoft 365 work context within the user's permissions, and sensitivity labels and sharing settings in
SharePoint, OneDrive and Purview shape what reaches outputs. Confirm current grounding and permission behaviour in the
source records (`ms-copilot-privacy`, `ms-copilot-overview`). Organisation-wide oversharing controls belong to the
work-context readiness programme, not to individual task checks.

## Adoption considerations

Teams adopt good habits when the check is light. Give them a five-minute version for personal tasks (one version, recent,
right people) and reserve the full table for shared or higher-risk designs.

## Knowledge considerations

This skill is a consumer of knowledge management, not a substitute for it. Fix problems at source where you can, and
refer structural issues (unowned sites, no review cycle, poor information architecture) to the `knowledge-management`
department.

## Security and privacy considerations

Oversharing found during a check is a security finding, not a task inconvenience. Record it, tell the source owner and,
from risk tier 2 or wherever personal or confidential data is involved, refer it to `security-privacy:data-exposure-review`.

## Responsible AI considerations

Outdated or conflicting sources produce confident but wrong outputs, which matters most where outputs describe or affect
people. Require the output to state known gaps rather than present incomplete evidence as complete.

## Evaluation requirements

Not applicable as a separate evaluation; the source verdicts are inputs to `copilot-cowork:workflow-validation`, which
checks that outputs use the authoritative versions.

## Value measures

Track at team level how many outputs need correction because of source problems, before and after checks are adopted.
Report source problems by location and owner role, never by individual.

## Scale notes

### Starter

Use the quick check for personal tasks and the full table only for designs that others will reuse.

### Scale

Make the full check a step before any task design is published to a shared library, and feed recurring source problems
into the knowledge management backlog.

### Enterprise

Align task-level checks with the organisation's labelling and oversharing programme so verdicts use the same
classifications and problems flow into the same remediation process.

## Hand-offs

- To `copilot-cowork:task-context-design` with exclusions and authoritative versions.
- To `security-privacy:data-exposure-review` for oversharing involving sensitive content.
- To the `knowledge-management` department for structural source problems.
- To `copilot-cowork:workflow-validation` once all sources are ready or conditional.

## Reviewer gates

From risk tier 2, `security-privacy` reviews sources holding personal or confidential data for exposure through task
outputs. Findings are blocking or advisory; a blocking finding means the source is excluded until fixed.

## Failure modes

- The check is skipped for "my own files", which hold the duplicate versions and forgotten sharing links.
- A shared task design behaves differently for each team because their access differs, and nobody notices.
- Oversharing is worked around in the task instead of fixed at source, so it remains open to every other tool and person.
- The delegator, not the owner, decides which version is authoritative.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Run a shared task design with a not-ready source in it.
- Treat a source as current without asking its owner.
- Work around oversharing of sensitive content instead of reporting and fixing it.
- Widen anyone's access to a source just so a task can use it.

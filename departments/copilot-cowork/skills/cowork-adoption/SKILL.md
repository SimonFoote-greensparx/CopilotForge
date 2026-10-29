---
name: cowork-adoption
description: Plans and drives adoption of Copilot Cowork in teams - choosing starter tasks, building delegation habits, publishing validated task designs, enabling Champions and team leads, and measuring outcomes at team level - so Cowork becomes a trusted way of working rather than a novelty. Use when Cowork is reaching a new team, when early use stalls after the first weeks, or when a sponsor asks how teams will learn to delegate well.
license: CC-BY-4.0
metadata:
  department: copilot-cowork
  lifecycle: Enable, Launch, Measure, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2
  platforms: copilot-cowork, m365-copilot
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-cowork-customise, ms-champion-programme
  status: draft
  authors: Simon Foote
---

# Cowork adoption

## Purpose

Copilot Cowork asks more of people than a chat prompt: they must decide what to hand over, describe it well, respond at
checkpoints and review what comes back. Those are delegation skills, and most people have never practised them with
software. This skill plans adoption of Cowork within teams around real work: a few well-chosen starter tasks, validated
task designs to copy, Champions and team leads who model good delegation, and measures that show whether teams are getting
better outcomes. Adoption goes wrong when Cowork is launched like a feature, people try it on vague tasks, get vague
results and quietly stop.

## When to use

- Cowork is being introduced to a team, function or business unit.
- Early use rose quickly and has stalled, or teams report that results are not worth the effort.
- A sponsor asks how teams will learn to delegate well and safely.
- Validated task designs exist and need to reach the teams that would benefit.

## When not to use

- Planning the organisation-wide Copilot launch across all products - use `copilot-adoption:launch-plan`.
- Finding and prioritising AI scenarios across roles for Copilot generally - use `copilot-adoption:scenario-discovery`.
- Teaching everyday prompting and verification habits in Copilot Chat and the apps - use `m365-copilot:prompting-practice`.
- Setting the rules for what Cowork may be used for and which customisations are approved - use `copilot-cowork:cowork-governance`.
- Designing the Champion programme itself - use `champions:champion-programme-design`.

## Questions to ask first

1. Which recurring, multi-step tasks in this team take real time today and produce an output someone checks?
2. Are there validated task designs in the shared library that fit this team's work?
3. Who in the team (a Champion, a team lead) will model delegation and help colleagues through their first tasks?
4. What has the team been told about what Cowork is for, what stays with them and how outputs must be reviewed?
5. How will the team know, in six to eight weeks, whether Cowork is helping?

## Required inputs

- The organisation's Cowork governance position from `copilot-cowork:cowork-governance`.
- Candidate tasks from the team, assessed through `copilot-cowork:cowork-use-case-assessment`.
- Any validated task designs from the shared library.
- The team's readiness, from `copilot-adoption:adoption-readiness` where it has been assessed.

If governance has not been set, adoption is limited to low-consequence drafting tasks until it is. Never promise a team
access or features that availability and licensing have not been confirmed for; route licensing questions to the
Microsoft licensing guide or a licensing partner.

## Decision framework

Sequence adoption in three stages per team, moving on only when the exit signal is present.

| Stage | Focus | Typical tasks | Exit signal |
|---|---|---|---|
| 1. Try | Learn to describe outputs and review them | Low-consequence drafting and collating for the person's own use | Most people in the pilot group have completed a task and reviewed the output against a definition of done |
| 2. Repeat | Build reusable task designs for the team's recurring work | Team briefings, recurring reports, preparation packs | At least one shared task design validated and in regular use |
| 3. Extend | Take on more consequential or multi-step work with checkpoints | Work reaching other teams or external parties, with approvals | Checkpoints and review standard in place and working |

Choose starter tasks that score well on outcome clarity and verifiability and low on consequence. Avoid starting with the
team's most complex or sensitive work, however tempting the time saving.

## Practitioner approach

Begin with the work, not the product. Sit with the team lead and two or three members and list the recurring tasks that
eat time and produce something a person checks: the weekly status pack, the supplier comparison, the meeting preparation
brief. Assess each quickly for fit and pick two or three starter tasks that are clear, checkable and low in consequence.
These become the team's first experience of Cowork, and their quality decides whether people continue.

Teach delegation as a skill. Short, practical sessions work better than demonstrations: each person brings a real task,
writes its goal and definition of done, names the sources, runs it, and reviews the output against the definition.
The first lesson most people learn is that a vague request gets a vague result; the second is that checking takes
discipline. Both are worth learning on low-stakes work.

Use validated task designs as accelerators. If the shared library holds a design for work this team does, start there and
adapt it. If the team builds a good design, help them validate it and publish it, crediting the team. A library of
designs that genuinely work is the strongest adoption asset Cowork has, because it turns one team's learning into
another's starting point.

Put people in the room who have done it. A Champion or team lead who has delegated real work and can show the checkpoints
and review routine is more persuasive than any message. Equip them with the review standard and the governance position so
they model safe use, and give them a route to escalate questions.

Be explicit about what stays human. Tell teams plainly that accountability does not move to Cowork, that outputs are
reviewed before use, and what the not-permitted uses are. People are more willing to try delegation when they know where
the boundaries are.

Measure outcomes, not activity. Ask the team, at six to eight weeks, which tasks they now delegate, how much rework
outputs need and whether turnaround has improved. Use aggregate usage data only at team level and above the agreed
minimum group size. Where adoption stalls, look first at task choice and context quality, then at time and support; low
use is usually a design problem, not a motivation problem.

## Outputs

- A team Cowork adoption plan: starter tasks, stage plan, enablement sessions, Champions or leads, communications and measures.
- A set of starter task designs on the `cowork-task-design` template, validated where shared.
- A short team guide covering what Cowork is for here, what stays human, the review standard and where to get help.
- A six-to-eight-week outcome review at team level.

## Microsoft platform considerations

Microsoft's published adoption resources for Copilot provide scenario, launch and community material that can be adapted
for Cowork; check the current resources in `ms-copilot-adoption-hub`. Confirm which Cowork capabilities, customisations and
admin settings are available and approved before planning around them (`ms-copilot-cowork-customise`). Availability and
licensing change; do not assert them.

## Adoption considerations

This skill is the adoption plan for Cowork. Align it with the wider Copilot adoption programme in the `copilot-adoption`
department so teams hear one consistent story, and with the Champion network so Cowork enablement reuses existing
community channels.

## Knowledge considerations

Good adoption depends on teams' sources being in reasonable shape. Use starter tasks to surface source problems early and
route them to `copilot-cowork:grounding-readiness`. Treat the shared task library as a knowledge asset with owners and
review dates.

## Security and privacy considerations

Starter tasks should not involve sensitive personal or confidential data. Make the governance position and the review
standard part of every enablement session, so safe habits form from the first task.

## Responsible AI considerations

Be honest about what Cowork does and does not do well, and that outputs need checking. Do not frame adoption as a route to
reducing headcount or monitoring work; people adopt tools they trust. Role-level impact questions go to
`change-and-communications:people-change-impact`.

## Evaluation requirements

Shared task designs used in adoption must pass `copilot-cowork:workflow-validation` before teams are encouraged to rely on
them. Personal starter tasks need only the review standard.

## Value measures

Measure at team level: tasks regularly delegated, first-time acceptance of outputs, rework, and turnaround against a
baseline taken before adoption began. Report usage only in aggregate above the agreed minimum group size. Never rank,
score or monitor individuals' use.

## Scale notes

### Starter

One or two pilot teams, two starter tasks each, a Champion or lead who has used Cowork, and a simple outcome check after
six to eight weeks.

### Scale

Run adoption team by team through the Champion network, grow the shared task library, and use outcome reviews to decide
which teams move to the Extend stage.

### Enterprise

Business units run their own adoption waves with the shared stage model and library; the central team curates
organisation-wide task designs, tracks outcomes across units and feeds lessons into governance and learning.

## Hand-offs

- To `copilot-cowork:cowork-use-case-assessment` for candidate tasks.
- To `copilot-cowork:workflow-validation` for designs the team wants to share.
- To `copilot-adoption:adoption-measurement` to include Cowork outcomes in programme measures.
- To `champions:champion-programme-design` where Champions need a Cowork pathway.

## Reviewer gates

Not applicable for adoption activity itself, because it does not release a solution; task designs used in adoption pass
their own gates, and from risk tier 2 shared designs are reviewed by `responsible-ai` and `security-privacy` as set out in
`copilot-cowork:cowork-governance`.

## Failure modes

- Cowork is launched as a feature, people try it on vague tasks, get vague results and stop.
- Starter tasks are the team's most complex work, so early failures set the tone.
- Adoption is measured by activity counts, so teams with high use and heavy rework look successful.
- Usage data is used to chase individuals, and trust collapses.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Rank, score or monitor individual staff by their Cowork use.
- Start a team on sensitive or high-consequence work before review habits exist.
- Promise access, features or licensing that have not been confirmed.
- Present Cowork outputs as needing no review.

---
name: coe-opportunity-pipeline
description: Runs the CoE's opportunity management pillar as a working pipeline - a pillar owner, stages from Identify to Improve with entry and exit criteria, the opportunity-management method used at each stage, triage rhythm, work-in-progress limits, service levels and pipeline health measures. Use when ideas pile up without decisions, when nobody owns the pillar, or when pilots start without passing through assessment.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Envision, Mobilise, Deliver, Measure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-studio-guidance, ms-coe-starter-kit, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# CoE opportunity pipeline

## Purpose

Opportunity management is the pillar that decides what the CoE works on, so when it stalls everything downstream
stalls too. This skill runs the pillar as a pipeline: one owner, clear stages with entry and exit criteria, the right
opportunity-management method at each stage, a triage rhythm, limits on work in progress and measures that show where
ideas get stuck. Pipelines usually fail by accepting everything and deciding nothing, so the backlog becomes a
graveyard of ideas, or by letting enthusiastic teams skip assessment and start pilots that cannot be judged.

## When to use

- The CoE is launching its opportunity management pillar and needs a working pipeline, not just a backlog.
- Ideas accumulate faster than decisions, and people stop submitting because nothing happens.
- Pilots start without a framed problem, suitability decision or risk tier.
- The steering group cannot see where ideas are stuck or how long a decision takes.

## When not to use

- Designing the staff-facing route for submitting ideas - use `opportunity-management:idea-capture`.
- Operating the backlog board's fields, statuses and hygiene - use `opportunity-management:backlog-management`.
- Scoring and ranking opportunities against each other - use `opportunity-management:opportunity-prioritisation`.
- Designing the CoE's overall shape and routing table - use `ai-centre-of-excellence:coe-operating-model`.
- Managing solutions once they are live - use `ai-centre-of-excellence:coe-portfolio-management`.

## Questions to ask first

1. Who owns the opportunity management pillar, and how much time do they have for it?
2. How many ideas arrive each month, through which routes, and how many are waiting for a decision now?
3. How much delivery capacity does the CoE and its partners actually have per quarter?
4. Which forum makes triage and priority decisions, and how often does it meet?
5. What delegated limits apply, for example which tiers or effort levels the working group may approve without steering?

## Required inputs

- The routing table and intake design from `ai-centre-of-excellence:coe-operating-model`.
- The forum schedule and decision rights from `ai-centre-of-excellence:coe-cadence` and `ai-centre-of-excellence:coe-charter`.
- Risk tiers from `ai-centre-of-excellence:coe-governance-model`.
- Delivery capacity from `ai-centre-of-excellence:coe-delivery-model`, or an honest estimate marked "to confirm".
- The current list of ideas, however rough.

If capacity is unknown, set a provisional work-in-progress limit low and raise it with evidence. Never let the absence of
a capacity figure mean "no limit".

## Decision framework

Each stage has a method, an exit test and a default service level. Service levels are starting points to agree locally.

| Stage | Method used | Exit test | Default service level |
|---|---|---|---|
| Identify | `opportunity-management:idea-capture` | Idea logged with submitter role and the problem in their words | Acknowledged within one working week |
| Assess - frame | `opportunity-management:problem-framing` | Named business owner, problem, outcome and baseline | Framed or returned within three weeks |
| Assess - suitability and risk | `opportunity-management:ai-suitability`, `opportunity-management:risk-classification` | Route chosen and provisional tier recorded | Decided at the next triage |
| Assess - value and effort | `opportunity-management:value-hypothesis`, `opportunity-management:effort-assessment` | Value hypothesis and effort range recorded | Before prioritisation |
| Prioritise | `opportunity-management:opportunity-prioritisation`, `opportunity-management:portfolio-balancing` | Ranked, with a capacity slot or a deferral reason | At the next steering for items above delegated limits |
| Build | `ai-centre-of-excellence:coe-delivery-model` | Release evidence complete for the tier | Per delivery plan |
| Deploy | `m365-agents:agent-release-readiness` or the equivalent route | Released with owner, baseline and review date | Per delivery plan |
| Measure | `ai-centre-of-excellence:coe-value-tracking` | Value measured against baseline | At the agreed review date |
| Improve | `opportunity-management:scale-or-stop` | Scale, iterate, pivot or stop decision recorded | At the review date |

Ideas leave the pipeline early by design. Process fixes, training and adoption scenarios are successful exits, recorded
with their outcome, not rejections.

| Pipeline signal | Action |
|---|---|
| Items in Build exceed the work-in-progress limit | Stop pulling new work; finish or pause something first |
| Items waiting in Assess beyond the service level | Add framing capacity or tighten intake guidance |
| Ideas returned for lack of an owner rise | Brief business units on what a good submission needs |
| Prioritised items wait more than two cycles for capacity | Defer explicitly and tell the submitter |

## Practitioner approach

Name the pillar owner first, usually the opportunity and process lead, and agree their time. A pipeline with no owner
drifts back into an inbox. The owner's job is not to do every assessment but to keep items moving, chase stuck ones and
bring the pipeline view to triage.

Map the stages onto the opportunity lifecycle the CoE already uses and agree the exit test for each. Exit tests matter
more than entry tests, because they stop half-assessed ideas sliding forward. The non-negotiable rule is that nothing
enters Build without a business owner, a framed problem, a suitability decision, a risk tier and a value hypothesis. If
a team has already started building, bring the work back into Assess rather than pretending it passed.

Set a work-in-progress limit on Build, based on real capacity. This is the single most effective control. Without it
the CoE starts everything, finishes little and spreads people too thin. When the limit is reached, triage pulls new work
only when something finishes or is deliberately paused.

Set the triage rhythm with `ai-centre-of-excellence:coe-cadence`. Weekly or fortnightly triage moves items through
Assess and makes delegated decisions; steering decides items above delegated limits and conflicts between business
units. Bring a single pipeline view to each: counts by stage, items over their service level and decisions needed.

Close the loop with submitters. Every idea gets an outcome, including "not now" and "fix the process first", with the
reason and the route it went. Submitters who hear back become repeat contributors, and the reasons teach the
organisation what makes a good idea.

Watch the early exits. A healthy pipeline sends many ideas to process fixes, training and adoption scenarios. If almost
everything ends up as an agent build, suitability is being skipped or the front door is attracting only tool requests.

Review the pipeline monthly with three questions: where do items wait longest, what share of ideas reach a decision
within the service level, and is the mix of work balanced between quick wins and strategic bets? Adjust capacity,
guidance or limits, and record the change. Say plainly what the pipeline cannot tell you: a fast pipeline is not proof of
value, which is measured later through value tracking.

## Outputs

- A pipeline definition: pillar owner, stages, methods, exit tests, service levels, delegated limits and work-in-progress limit.
- A pipeline view for each triage and steering meeting: counts by stage, items over service level, decisions needed.
- Submitter feedback standards, with the outcome and reason for every idea.
- Opportunity records on the `opportunity-canvas` template and ranking on the `prioritisation-matrix` template, maintained through the methods at each stage.

## Microsoft platform considerations

The pipeline can run on any list or board the organisation already uses, such as a Microsoft Lists list, a Planner
board or a Power Apps front end. Where the CoE Starter Kit is used for inventory, link live items to it rather than
keeping two registers. Check current tooling in `references/sources.md` before committing to a component.

## Adoption considerations

The pipeline is often the first contact the business has with the CoE. Publish how to submit, what happens next and
typical decision times, and share anonymised examples of each exit route so people see that "not an AI problem" still
gets help.

## Knowledge considerations

Make knowledge condition an Assess question for anything at tier 1 or above. Ideas that depend on unowned or poor
knowledge leave Assess with a precondition routed to `ai-centre-of-excellence:coe-knowledge-pillar`.

## Security and privacy considerations

Record data sensitivity at Assess so the risk tier is right before prioritisation. The pipeline must not let an item
reach Build at tier 2 or above without the `security-privacy` review scheduled in its plan.

## Responsible AI considerations

Flag at Assess any idea that informs decisions about people, money, safety or rights, so it is classified at tier 3
consideration and reaches the responsible AI review before build. Some ideas should leave the pipeline as "not to be
built"; record that outcome plainly.

## Evaluation requirements

Not applicable to the pipeline itself, which moves decisions rather than producing AI output. The pipeline checks that
each item entering Build has acceptance criteria that `m365-agents:agent-testing` or the relevant evaluation method can
test.

## Value measures

Measure flow at team level: ideas received, median days from submission to decision, share of decisions within service
level, share of ideas routed to non-AI exits, items in Build against the limit, and share of released items with an
owner and baseline. The pillar owner reports these to steering through `ai-centre-of-excellence:coe-kpi-framework`.

## Scale notes

### Starter

One list, one owner and a fortnightly conversation. Stages may be collapsed into Identify, Assess, Do and Review, but the
exit tests still apply. The work-in-progress limit may be two or three items.

### Scale

A board with explicit stages, weekly triage, monthly steering, delegated limits and a published service level. The pillar
owner reports pipeline health every month.

### Enterprise

Each spoke runs its own pipeline for tiers 0 to 2 under common stages and exit tests; the hub runs a combined view,
handles tier 3-4 items and arbitrates capacity between spokes.

## Hand-offs

- To `opportunity-management:backlog-management` for board fields, statuses and hygiene.
- To `ai-centre-of-excellence:coe-delivery-model` when an item enters Build.
- To `ai-centre-of-excellence:coe-portfolio-management` when an item goes live.
- To `ai-centre-of-excellence:coe-value-tracking` for measurement after release.

## Reviewer gates

Not applicable to the pipeline design, which governs flow rather than releasing solutions. The pipeline makes sure each
item's gates from `security-privacy`, `responsible-ai`, `evaluation-quality` and `design-authority` are scheduled by
tier before Build starts.

## Failure modes

- Everything is accepted, nothing is decided, and the backlog becomes a list nobody trusts.
- No work-in-progress limit, so the CoE starts many builds and finishes few.
- Teams skip Assess, start pilots, and the pilots cannot be judged because nobody set a baseline.
- Submitters never hear back and the front door goes quiet.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Let an item enter Build without a business owner, framed problem, suitability decision, risk tier and value hypothesis.
- Run the pipeline without a work-in-progress limit on Build.
- Leave a submitter without an outcome and a reason.
- Report pipeline measures by individual submitter or maker.

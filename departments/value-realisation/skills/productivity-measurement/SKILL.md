---
name: productivity-measurement
description: Measures the productivity effect of Copilot, agents, Cowork tasks and automation credibly - throughput, cycle time and capacity released from work data, sampled timing and comparison groups - and tracks where released capacity went, keeping self-reported hours saved as a perception measure only. Use when an hours-saved survey is challenged, when a sponsor asks what people did with saved time, or when a pilot must show a productivity effect.
license: CC-BY-4.0
metadata:
  department: value-realisation
  lifecycle: Deliver, Launch, Measure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-code, copilot-studio, power-platform
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-adoption-hub, ms-copilot-privacy, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Productivity measurement

## Purpose

"Hours saved" is the most quoted and least trusted AI benefit. This skill measures productivity effects in a way a
finance lead and a sceptical manager would both accept: from the work itself, using throughput, cycle time and effort
per unit, triangulated with sampled timing and, where fair, comparison groups. It also tracks the question most
measurement skips - where the released capacity went. It goes wrong when survey estimates are multiplied by headcount,
when time saved on one step reappears as review effort on another, and when measurement turns into monitoring people.

## When to use

- A productivity benefit is registered and needs a measurement method before launch.
- The current evidence is a self-reported survey of hours saved and it is being challenged.
- A sponsor asks what people are doing with the time AI saves them.
- A pilot needs to show, or disprove, a productivity effect before a scale decision.
- Productivity claims from several solutions need to be reconciled into one portfolio figure.

## When not to use

- Designing the pre-launch baseline itself - use `value-realisation:baseline-design`.
- Measuring accuracy, rework and error effects - use `value-realisation:quality-measurement`.
- Converting released time into money with finance - use `value-realisation:financial-benefits`.
- Measuring the value of an individual automation - use `automation:automation-value`.
- Measuring Copilot usage and adoption - use `copilot-adoption:adoption-measurement`.

## Questions to ask first

1. Which unit of work does the benefit concern (a case, a proposal, a report, a code change), and how is it counted today?
2. Is the expected effect more output from the same people, faster turnaround, or less effort per unit - and which matters to the business?
3. What baseline exists, from which design, and with what confidence?
4. What will the owner do with released capacity, and has that decision been made?
5. What has the data protection officer and HR agreed about measuring work at team level?

## Required inputs

- The registered productivity benefit and its owner, from `value-realisation:benefit-hypothesis`.
- The frozen baseline and its design from `value-realisation:baseline-design`.
- Access to operational data on volumes, timestamps and effort, agreed with the data owner.
- The owner's intended use of released capacity, or a note that it is undecided.

Where the redeployment decision is missing, measure released capacity but record it as unrealised. Never convert it to
a cash figure or report it as realised value until the owner has decided and acted.

## Decision framework

Use the strongest available method and triangulate with at least one other. Report the method beside every figure.

| Method | What it measures | Strength | Weakness |
|---|---|---|---|
| Work data (throughput, cycle time, effort per unit) | Actual change in output or speed | Objective, repeatable | Needs a clear unit and a stable definition |
| Comparison group | Effect relative to similar teams without the change | Separates AI from other change | Needs fair waves; groups drift over time |
| Sampled timing or work study | Effort per task with and without assistance | Direct, task-level | Small samples; observer effect |
| Task-level structured estimate | People estimate time for named tasks before and after | Cheap, broad | Perception; inflates with enthusiasm |
| General survey of hours saved | Overall perceived saving | Easy to collect | Weakest; never used alone |

Classify every productivity effect on the capacity ladder, and only the top rung counts as realised.

| Rung | Meaning |
|---|---|
| Time released | Effort per unit has measurably fallen |
| Capacity redeployed | The owner has directed released time to named work |
| Outcome achieved | The redeployed capacity produced a measured result (backlog cleared, more customers served, overtime reduced) |

## Practitioner approach

Define the unit of work first. Productivity is output per unit of effort, so without a countable unit there is nothing
to measure. Proposals issued, cases closed, reports produced and pull requests merged all work; "knowledge work" does
not. Where the work is too varied for one unit, pick the two or three scenarios that carry the benefit and measure
those.

Measure net, not gross. AI often shortens drafting and lengthens checking. Time the whole task from start to accepted
output, including verification, correction and any hand-back. A drafting agent that saves twenty minutes and adds
fifteen minutes of review has released five, and that figure is the honest one. Watch for effort moving to another
team, such as reviewers, support or the service desk.

Triangulate. Pair the work data with a small sampled timing study or a comparison group, and with a structured estimate
for the specific tasks. When the methods agree, confidence is high. When the survey shows far more than the work data,
report both and explain the gap; it usually reflects enthusiasm, time saved on low-value tasks, or savings absorbed
into the working day.

Follow the capacity. Ask the owner, before launch, what released time is for: clearing a backlog, absorbing growth
without recruitment, more customer contact, better quality, or reducing overtime and agency use. Then measure that
outcome. Capacity that nobody directs is usually absorbed, and the benefit is real for wellbeing but invisible in the
organisation's results. Record it honestly as unrealised rather than counting it.

Keep everything at team, role or process level above the minimum group size. Productivity data about named people is
performance data, and using it erodes the trust that adoption depends on. If a manager asks which individuals saved the
most time, decline and offer the team view.

Separate the effect of AI from other change by using the comparison group or time series from the baseline design, and
naming the confounders. For Copilot Code, productivity in delivery effort must be read beside quality and review
measures, because faster change with more defects is not a gain.

Report a range with the method and confidence, never a single precise number. Then reconcile across the portfolio so
that no two solutions claim the same released hours, using the apportionment agreed in the benefit statements.

## Outputs

- A productivity measurement plan per benefit: unit of work, methods, sample, schedule and responsible roles.
- Measured results recorded in the `benefits-register`: net effect as a range, method, confidence and capacity rung reached.
- A capacity redeployment record showing what released time was directed to and the outcome measured.
- A reconciliation note across solutions touching the same work.

## Microsoft platform considerations

Microsoft publishes adoption and usage reporting and, for some products, estimates of assisted activity. Treat any
built-in time-saved estimate as a modelled perception measure: useful context, never a substitute for work data. What
these reports contain and how they are calculated changes; check `references/sources.md` before quoting them. For
automations, run history in Power Platform can provide reliable volume and duration data.

## Adoption considerations

People are more willing to share honest time estimates when they trust the data will not be used against them. Explain
the method, publish team-level results back to the teams, and involve Champions in designing task-level estimates.

## Knowledge considerations

In knowledge scenarios, much of the saving is in finding rather than writing. Measure time to locate a trusted answer
and the share of questions escalated to experts, and remember that expert time released is often the larger benefit.

## Security and privacy considerations

Timestamps and effort data can identify individuals in small teams. Aggregate before analysis where possible, suppress
groups below the minimum size, keep raw data with its owner, and confirm the lawful basis with the data protection
officer. Employee consultation obligations go to HR.

## Responsible AI considerations

Pressure to show productivity can push people to skip verification. Pair every productivity measure with a quality
guard from `value-realisation:quality-measurement`, and never set individual speed targets for AI-assisted work.

## Evaluation requirements

Net productivity depends on how much correction outputs need. Use the solution's evaluation results to check that the
review effort observed is consistent with the quality measured at release.

## Value measures

This skill's success is the share of productivity benefits reported with work-data evidence and a capacity rung, owned
by the Benefits Realisation Lead, starting from the share that currently rests on surveys alone.

## Scale notes

### Starter

One scenario, one unit of work, a before-and-after from existing data plus a short task-level estimate, and a simple
note of what released time was used for.

### Scale

Standard methods per scenario type, comparison groups from rollout waves, and capacity redeployment recorded as part of
every benefit review.

### Enterprise

Common units and definitions across business units, portfolio reconciliation of released capacity, and links to
workforce planning so redeployment decisions are made deliberately.

## Hand-offs

- To `value-realisation:financial-benefits` once capacity is redeployed and needs valuing.
- To `value-realisation:quality-measurement` for the paired quality guard.
- To `value-realisation:benefit-owner` when capacity is released but not redeployed.
- To `value-realisation:post-implementation-review` with the measured results.

## Reviewer gates

Not applicable as a release gate, because this is a measurement method. Where effort or timing data about staff is
collected, `security-privacy` confirms aggregation and minimum group size before collection, and HR confirms any
consultation needed.

## Failure modes

- A survey estimate is multiplied by headcount and salary, and finance rejects the whole value report.
- Drafting time falls but review time rises, and only the gross saving is reported.
- Released capacity is never directed, is absorbed, and the benefit cannot be found a year later.
- Team-level data is drilled down to individuals at a manager's request, and adoption stalls.
- Two solutions report the same released hours, and the portfolio total exceeds the time available.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Report self-reported hours saved as the only evidence of productivity.
- Measure, rank or report the productivity of named individuals.
- Count released capacity as realised value before it has been redeployed.
- Quote a vendor or built-in time-saved estimate as the organisation's measured result.

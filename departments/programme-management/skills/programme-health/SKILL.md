---
name: programme-health
description: Assesses and reports AI programme health across outcomes, schedule, cost, capacity, risk, adoption, assurance, governance and stakeholder confidence, with defined RAG criteria, an evidence-based narrative, corrective actions with owners, and a recovery plan when health is red. Use when the board needs a monthly health report, when status reports are all green but the programme feels stuck, or when a programme needs a health check or recovery.
license: CC-BY-4.0
metadata:
  department: programme-management
  lifecycle: Deliver, Assure, Launch, Measure, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, iso-iec-42001, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Programme health

## Purpose

Programme status reports drift towards green: each workstream reports what it did, and nobody reports whether the
programme is still on course for its outcomes. This skill assesses health across a fixed set of dimensions with defined
criteria for red, amber and green, writes a short evidence-based narrative, and turns each problem into a corrective
action with an owner and a date. When health is red it produces a recovery plan. Health reporting goes wrong when RAG
ratings are opinions, when activity is reported in place of outcomes, and when adoption and quality are left out because
they are harder to measure than dates.

## When to use

- The programme board needs a monthly health report.
- Status reports are consistently green but milestones slip, adoption stalls or stakeholders are uneasy.
- A sponsor asks for an independent health check of an AI programme.
- A programme is in trouble and needs a recovery plan.
- A stage gate is approaching and health is part of its evidence.

## When not to use

- Checking the health of the Champions programme itself - use `champions:champions-health-check`.
- Assessing how mature the AI CoE is - use `ai-centre-of-excellence:coe-maturity-assessment`.
- Specifying the sponsor's value dashboard across value, adoption, capability and governance - use `value-realisation:value-dashboard`.
- Setting the CoE's KPIs and scorecard - use `ai-centre-of-excellence:coe-kpi-framework`.
- Managing an individual risk or issue - use `programme-management:programme-risk-log`.

## Questions to ask first

1. What outcomes, tolerances and closure criteria did the charter set, so health can be judged against them?
2. Which measures already exist (plan, budget, risk log, adoption measures, evaluation results, reviewer outcomes), and how current are they?
3. Who reads the report and what decisions do they need to take from it?
4. Has the board agreed what red, amber and green mean for each dimension, or will this report propose definitions?
5. Is this a routine report, an independent check, or a recovery?

## Required inputs

- The programme charter with outcomes, tolerances and closure criteria.
- The integrated plan and baseline, the budget and capacity report, and the risk log.
- Adoption measures at team or role level from `copilot-adoption:adoption-measurement` where adoption is in scope.
- Solution gate outcomes and evaluation results for solutions in flight.
- Feedback from workstream leads and, for an independent check, short interviews with the sponsor, business owners and reviewers.

Where a dimension has no data, rate it grey ("not measured") and say what is needed, rather than defaulting to green.

## Decision framework

Rate each dimension against criteria agreed with the board. Starting criteria to adapt:

| Dimension | Green | Amber | Red |
|---|---|---|---|
| Outcomes | Contribution measured and on track | Measures in place, trend unclear | No baseline, or trend moving away |
| Schedule | Critical path within tolerance | Forecast within tolerance but slipping | Forecast beyond tolerance |
| Cost | Forecast within tolerance | Consumption or services trending up | Forecast beyond tolerance |
| Capacity | Scarce roles within declared time | One role over-committed in the next quarter | Several roles over-committed now |
| Risk | No risks above threshold without response | Responses late on some top risks | Threshold risks without response, or issues unresolved |
| Adoption | Use and behaviour change on track by team | Uneven across teams | Stalled or declining |
| Quality and assurance | Gates passed with evidence; no open blocking findings beyond plan | Evaluation or review delays | Blocking findings ignored or evidence missing |
| Governance | Decisions taken on time and recorded | Decision latency growing | Decisions stalled or reopened |
| Stakeholder confidence | Sponsor and owners engaged | Attendance or engagement falling | Sponsor disengaged or a key function opposed |

Overall health is not an average. It is red if outcomes, quality and assurance, or two other dimensions are red; amber if
any dimension is red or three are amber; otherwise green.

| Overall | Response |
|---|---|
| Green | Report by exception |
| Amber | Corrective actions with owners and dates, reviewed at the next board |
| Red | Recovery plan to the sponsor within an agreed short period, with options including re-scope or pause |

## Practitioner approach

Agree the criteria first. Take the table above to the board and adapt it, so ratings are applied to agreed definitions
and not to the reporter's mood. Publish the criteria with every report; it is the single most effective guard against
optimism.

Gather evidence from the programme's own artefacts. Schedule from the baseline, cost from the budget report, risk from the
log, adoption from the measures, quality from gate outcomes and evaluation results. Rate each dimension, then write two or
three sentences of narrative: what the evidence shows, why, and what is being done. Where the evidence is missing, rate
grey and say so; a missing measure is itself a finding.

Look for the patterns that recur in AI programmes. Milestones met while adoption stalls usually means the programme is
delivering technology rather than change. Releases queuing at the gates usually means reviewer capacity was not planned.
Growing consumption cost without a matching value measure usually means a solution was scaled before its scale-or-stop
decision. Name the pattern when you see it; it helps the board act on causes rather than symptoms.

Turn every amber and red into an action. Each action has an owner by role, a date and the expected effect on the rating.
Track actions from report to report and show which have worked. A health report whose actions are never followed up
becomes theatre.

For an independent health check, add short structured conversations with the sponsor, two or three business owners, a
reviewer and a workstream lead, and look for divergence between what people say and what the artefacts show. Report
findings about the programme, never about individuals' performance.

When overall health is red, prepare a recovery plan: the cause, the options (re-sequence, reduce scope, add capacity
through a supplier, pause a workstream, stop), the recommendation, the effect on outcomes and the decision required. Take
it to the sponsor quickly; recovery options narrow with every week of delay. A well-evidenced pause or stop is a
legitimate outcome.

## Outputs

- A programme health report on the `programme-health-report` template: overall rating, dimension ratings against published criteria, narrative, top risks and issues, decisions required, corrective actions with owners and dates, and gate status.
- An action tracker carried from report to report.
- For a red rating, a recovery plan with options and a recommendation for the sponsor.

## Microsoft platform considerations

Adoption and usage data from Microsoft reporting tools feed the adoption dimension at team or role level only; check what
each report measures and how current it is against `references/sources.md` before relying on it. Platform changes that
affect the plan appear through `programme-management:dependency-management`.

## Adoption considerations

Adoption is a health dimension in its own right, not a footnote. Report it by team or role above the agreed minimum group
size, and look for behaviour change and scenario use, not only active-user counts.

## Knowledge considerations

Knowledge readiness often explains slipping agent milestones. Where it does, name it in the narrative and route the action
to the knowledge owners, not the build team.

## Security and privacy considerations

Health reports may contain security and supplier information; restrict access to the board and programme office. Never
include individual usage data or names in adoption findings.

## Responsible AI considerations

Report open responsible AI findings and pending risk acceptances under quality and assurance. A programme cannot be green
while a tier 3 or 4 solution proceeds without its `responsible-ai` review.

## Evaluation requirements

Not applicable to the report as an AI solution; it reads evaluation outcomes from `evaluation-quality` as evidence for the
quality dimension and flags solutions whose evaluation evidence is missing.

## Value measures

The health report's own measure is whether it changes decisions: the share of amber and red ratings with actions closed
by their date, and the time from red to an agreed recovery decision. The AI Programme Manager owns the report; ratings
describe the programme, never individuals.

## Scale notes

### Starter

A half-page monthly note to the sponsor covering outcomes, schedule, cost, adoption and risks, with three or four actions.

### Scale

A monthly report on the template with agreed criteria for all dimensions, an action tracker and a recovery route.

### Enterprise

Reports per tranche or business unit rolled up to programme and portfolio, periodic independent health checks, and
consistent criteria across programmes.

## Hand-offs

- To `programme-management:programme-board-cadence` for the board's decisions on actions and recovery.
- To `programme-management:stage-gates` where health is gate evidence.
- To `programme-management:programme-risk-log` for new risks and issues the assessment reveals.
- To `value-realisation:value-dashboard` where the sponsor needs the value view rather than programme health.

## Reviewer gates

Not applicable, because the health report releases no solution; it reports outcomes from `security-privacy`,
`responsible-ai`, `evaluation-quality` and `design-authority` exactly as those departments classified them.

## Failure modes

- RAG ratings are opinions without criteria, so everything is green until it is suddenly red.
- The report lists activity rather than progress towards outcomes.
- Adoption and quality are omitted because dates are easier to measure.
- Actions are written but never followed up.
- A health check turns into an assessment of individuals and loses the trust it needs.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Rate a dimension green without evidence.
- Average ratings in a way that hides a red outcome or assurance dimension.
- Report individual usage, performance or attendance as health evidence.
- Soften or reclassify a reviewer's blocking finding in the report.

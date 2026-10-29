---
name: coe-value-tracking
description: Runs the CoE's routine for tracking value delivered - a value ledger with one line per solution showing estimate at intake, baseline, measured result, method and confidence, a monthly update rhythm, roll-up to the sponsor scorecard and the value review, and honest treatment of attribution and unproven claims. Use when steering asks what the CoE has delivered, when value claims vary by teller, or when nobody revisits estimates after release.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Measure, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-studio-guidance, ms-coe-starter-kit, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# CoE value tracking

## Purpose

A CoE that cannot show what it has delivered loses its sponsor, however good its work. This skill runs the routine that
tracks value across everything the CoE has touched: a single ledger, one line per solution or adoption scenario, updated
on a fixed rhythm and rolled up for steering, with the method and confidence of every figure visible. Value tracking
goes wrong when it relies on survey-based hours saved, when estimates made at intake are reported as results, and when
the most visible solutions get measured while the rest are quietly assumed to work.

## When to use

- Steering or the sponsor asks what the CoE has delivered so far, and the answer is anecdotes.
- Value figures differ depending on who presents them.
- Solutions were approved on value estimates that nobody has checked since release.
- The CoE's first value review is approaching and the scorecard's value quadrant is empty.

## When not to use

- Designing the CoE's KPI framework and sponsor scorecard - use `ai-centre-of-excellence:coe-kpi-framework`.
- Designing baselines before change in depth - use `value-realisation:baseline-design`.
- Building a return-on-investment model - use `value-realisation:roi-model`.
- Measuring one agent's value against its hypothesis - use `m365-agents:agent-value-measurement`.
- Deciding whether one solution should scale or stop - use `opportunity-management:scale-or-stop`.

## Questions to ask first

1. Which solutions and adoption scenarios are live, and which had a value hypothesis and baseline recorded at intake?
2. Who is the business owner for each benefit, and will they provide the measured figures?
3. What data sources exist for the work itself (cycle times, volumes, error rates), rather than self-reported estimates?
4. When does the value review in the CoE cadence happen, and what decisions does it take?
5. Has the data protection officer agreed how usage and work data may be aggregated and reported?

## Required inputs

- The CoE scorecard and measure definitions from `ai-centre-of-excellence:coe-kpi-framework`, on the `coe-kpi-scorecard` template.
- Value hypotheses and baselines from intake records, through `ai-centre-of-excellence:coe-opportunity-pipeline`.
- The list of live solutions from `ai-centre-of-excellence:coe-portfolio-management`.
- Business owners for each benefit, ideally recorded through `value-realisation:benefit-owner`.

Where a solution has no baseline, record "no baseline" and either capture one now (for future comparison) or report the
solution's value as unproven. Never back-fill a baseline from memory.

## Decision framework

Each ledger line records: solution or scenario, business owner, value hypothesis, measure, baseline and date, estimate
at intake, latest measured value and date, method, confidence, run cost or "to confirm", and status.

Grade every reported figure by method; the grade travels with the figure.

| Confidence | Method | How to report |
|---|---|---|
| High | Measured from the work itself against a baseline, with a comparison group or clear before and after | Report as achieved value |
| Medium | Measured from the work against a baseline, without a comparison | Report as achieved, noting other changes in the period |
| Low | Self-reported estimates, sampled time studies or proxy measures | Report as indicative, beside a high or medium measure where possible |
| Unproven | Estimate at intake only, or no baseline | Report as expected, never as delivered |

Set status from the latest measured value.

| Status | Rule | Action |
|---|---|---|
| On track | Measured value at or near the hypothesis | Continue; consider for reuse |
| Behind | Measured value clearly below the hypothesis | Owner explains and sets an action |
| Not measured | Review date passed without a measurement | Escalate to the value review |
| Stopped | Solution retired or stopped | Keep the line with its final value and lessons |

## Practitioner approach

Build the ledger from what exists. List every live solution and adoption scenario, and pull its value hypothesis,
baseline and estimate from intake. Many lines will have gaps; record them honestly. A ledger with visible gaps is more
credible than a polished one with invented numbers, and the gaps become actions.

Make business owners responsible for the figures. The CoE lead runs the ledger, but the business owner of each benefit
supplies and stands behind the measured value. This keeps value with the business and stops the CoE marking its own
homework.

Prefer measures from the work. Cycle time from a case system, documents produced, rework rates and error counts are more
convincing than survey estimates. Where time saved is the only available measure, gather it with a method that can be
explained, such as a structured sample, and grade it low. Pair adoption measures with outcome measures, never present
usage as value.

Update on a fixed rhythm. Monthly for the ledger owners, quarterly for the value review. Each solution's first measured
value is due at the review date set at release; a passed date with no measurement is itself a finding.

Roll up carefully. Add figures only where methods and units match, and show achieved, indicative and expected value in
separate columns. Do not add an unproven estimate to a measured result to make a bigger number. Show run cost beside
value so steering sees net contribution, and show the non-financial benefits, such as risk reduction or quality, in
their own terms rather than forcing them into money.

Handle attribution plainly. Several changes often happen at once: a new process, a new system and an agent. Record what
else changed and how confident the owner is that the solution contributed. Where attribution is weak, say so.

Feed the results onward. The value quadrant of the sponsor scorecard draws from the ledger. Solutions that are behind go
to `opportunity-management:scale-or-stop`. Success stories with high or medium confidence go to the success stories
area, and lessons from lines that missed their hypothesis go back into intake guidance, so estimates improve over time.

Be clear about limits. The ledger shows whether solutions are delivering against their own hypotheses; it does not prove
the organisation's overall return on AI. That wider question belongs to the `value-realisation` department.

## Outputs

- A CoE value ledger: one line per solution and scenario with hypothesis, baseline, estimate, measured value, method, confidence, cost and status.
- A quarterly value review pack: achieved, indicative and expected value shown separately, lines behind or not measured, and decisions needed.
- The value quadrant figures for the `coe-kpi-scorecard` template.
- A lessons log comparing estimates with results, fed back into intake guidance.

## Microsoft platform considerations

Microsoft's usage reporting for Copilot, Copilot Studio analytics and admin tooling show adoption and activity, which are
useful context but not value on their own. Check what each report can and cannot show, and how it aggregates data, in
`references/sources.md` before relying on it.

## Adoption considerations

Credible value stories are the best adoption material the CoE has. Share them with their confidence grade, and share
honest misses too; teams trust a CoE that reports what did not work.

## Knowledge considerations

Where a solution's value depends on knowledge quality, record knowledge fixes in the ledger notes, because improvements
in answers often come from content rather than the solution itself.

## Security and privacy considerations

Usage and work data used for value tracking is reported at team or role level above an agreed minimum group size, as
confirmed by the data protection officer. Do not combine datasets in ways that identify individuals.

## Responsible AI considerations

Value measures must not reward solutions for removing human oversight that the risk tier requires. Where a benefit comes
from faster decisions about people, money, safety or rights, record the quality and fairness checks beside the speed
gain.

## Evaluation requirements

Value is only meaningful if the solution's outputs are good enough. Show the latest evaluation result beside the value
for tier 2 and above solutions, and treat value from a solution failing its quality threshold as at risk.

## Value measures

Measure the tracking itself: share of live solutions with a measured value by their review date, share of reported value
at high or medium confidence, and gap between estimates and results over time. The CoE lead owns these measures. Never
report value by individual user.

## Scale notes

### Starter

A short table of the few solutions and scenarios in use, with the owner's measure and a before and after figure where
possible, reviewed quarterly by the working group and sponsor.

### Scale

A full ledger, monthly updates by business owners, a quarterly value review and confidence grading on every figure.

### Enterprise

Spokes keep ledger lines for their solutions under common methods; the hub rolls up across units, separates shared
services from local solutions and aligns with the organisation's benefits realisation and finance processes.

## Hand-offs

- To `ai-centre-of-excellence:coe-kpi-framework` for the scorecard's value quadrant.
- To `opportunity-management:scale-or-stop` for solutions behind their hypothesis.
- To `value-realisation:financial-benefits` when finance needs cashable and non-cashable benefits quantified.
- To `change-and-communications:success-stories` for credible stories to share.

## Reviewer gates

Not applicable, because value tracking reports results rather than releasing a solution. Finance or the benefits owner
may challenge figures, and that challenge is recorded on the ledger; `evaluation-quality` evidence is shown alongside
value for tier 2 and above.

## Failure modes

- Estimates made at intake are reported as delivered value.
- Survey-based hours saved are the only measure and the finance team stops believing any figure.
- Only flagship solutions are measured and the rest are assumed to work.
- The CoE reports its own value without business owners standing behind the figures.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Report an estimate or an unproven figure as delivered value.
- Add figures with different methods or confidence into one headline number.
- Back-fill a baseline after the change from memory.
- Track or report value by individual user or employee.

---
name: automation-value
description: Measures the value an automation delivers against its baseline - cycle time, handling effort, errors and rework, throughput - net of human review, exception handling, run cost and support, and reports it to the process owner without counting runs as value. Use when an automation goes live, when a sponsor asks what an automation saved, or when deciding whether to extend, fix or retire it.
license: CC-BY-4.0
metadata:
  department: automation
  lifecycle: Measure, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: power-platform, copilot-studio, ai-foundry, platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-coe-starter-kit, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# Automation value

## Purpose

Automation value is often reported as runs completed or hours "saved" by multiplying runs by a guessed minute count.
Neither tells a sponsor whether the process got faster, cheaper or more accurate. This skill measures what an automation
actually delivers against the baseline taken before it went live, net of the effort it creates (reviewing AI output,
working exceptions, supporting the flow) and its run cost. It goes wrong when no baseline was captured, when review and
exception effort is ignored, and when time released is claimed as cash without finance agreeing.

## When to use

- An automation is going live and its value measures and reporting need setting up.
- A sponsor or process owner asks what an automation has delivered.
- An automation with AI steps is due for review and the decision is to extend, fix or retire it.
- Several automations need comparable value reporting for the CoE portfolio.
- Reported savings look implausible and need checking.

## When not to use

- Measuring the value of an agent against its hypothesis - use `m365-agents:agent-value-measurement`.
- Designing baselines across the programme before any change - use `value-realisation:baseline-design`.
- Agreeing cashable and non-cashable benefits with finance - use `value-realisation:financial-benefits`.
- Deciding whether to scale or stop an initiative based on evidence - use `opportunity-management:scale-or-stop`.
- Monitoring run health and AI quality signals - use `automation:automation-monitoring`.

## Questions to ask first

1. What was the value hypothesis at assessment, and which measure did the process owner say would show success?
2. Was a baseline captured before go-live, from what source, and over what period?
3. How much time do people now spend reviewing AI results and working exceptions?
4. What does the automation cost to run and support, including consumption, licences assigned to it and support time?
5. Has the time released been used for something, and has finance agreed how any of it is counted?

## Required inputs

- The value estimate and assumptions from `automation:automation-assessment`.
- Baseline measures from before go-live, with their sources and periods.
- The run log, review measures and exception data from `automation:automation-monitoring`.
- Run and support cost figures from the automation owner, marked as estimates where not measured.

If no baseline exists, say so plainly. Reconstruct one only from records that pre-date go-live (system timestamps, case
volumes, error logs), label it as reconstructed and lower the confidence of the result. Never back-fill a baseline from
memory.

## Decision framework

Measure each dimension that the hypothesis named, and always measure the offsetting effort.

| Dimension | Measure | Source |
|---|---|---|
| Speed | End-to-end cycle time from request to outcome | System timestamps before and after |
| Effort | Handling time per item, including review and exception work | Time studies or sampled observation at team level |
| Quality | Error, rework and complaint rates | Error logs, rework records, complaints |
| Throughput | Items completed per period at the same staffing | System records |
| Offsetting effort | Review time, exception handling, support and maintenance | Review measures, exception data, support records |
| Run cost | Consumption, capacity and other running costs | Automation owner and finance |

Then decide.

| Evidence | Recommendation |
|---|---|
| Net value meets or exceeds the hypothesis | Keep; consider extending to similar processes |
| Gross value good, but review or exception effort erodes it | Fix: improve inputs, AI step or thresholds before extending |
| Value below hypothesis and no credible fix | Retire or return to manual, recording the lessons |
| No baseline and no reconstructable data | Report as unproven; set a baseline now for the next review |

## Practitioner approach

Start from the hypothesis, not the dashboard. Read the assessment and the measure the process owner chose. If the goal
was faster response to customers, report cycle time first; run counts are context, not value.

Check the baseline before measuring anything. Confirm the period, source and definition, and make sure the after
measure uses the same definition. A baseline of "time to first touch" compared with an after figure of "time to
resolution" is a common and misleading mismatch. Where the process changed during redesign, separate the value of the
redesign from the value of the automation; both are real, but they are different claims.

Measure the offsetting effort honestly. Count the time reviewers spend on AI results and the time teams spend on
exceptions, using the review and exception data rather than estimates. Add support and maintenance time and run costs.
Many automations with AI steps look strong on gross time saved and modest on net value; the net figure is the one to
report.

Measure quality as well as speed. An automation that halves cycle time but doubles rework has moved effort rather than
removed it. Look at error and complaint rates before and after, and at the share of AI results reviewers amend.

Be careful with money. Released time is capacity, not cash, unless a budget changes. State released capacity in hours
at team level and what it was used for, and agree any financial figure with finance through
`value-realisation:financial-benefits`. Never convert hours to cash by multiplying by a salary rate without that
agreement.

Report ranges and confidence. Give the measured value, the assumptions and the confidence, and say what you could not
measure. Sponsors trust a modest figure with clear method more than a large figure with none.

Close with a recommendation: keep, extend, fix or retire, with the evidence. Feed it to the CoE portfolio and set the
next review date.

## Outputs

- An automation value report: hypothesis, baseline and source, after measures, offsetting effort, run cost, net value as a range with confidence, quality effects, released capacity and its use, recommendation and next review date.
- Any financial figures, marked as agreed with finance or not.
- Lessons for future automation assessments, especially where estimates proved wrong.

## Microsoft platform considerations

Run data from Power Automate analytics, the CoE Starter Kit's inventory and the flow's own run log can supply volumes and
timings, while business outcomes usually come from the systems of record. Consumption and licensing costs depend on the
organisation's agreements; take them from the owner and finance, check current models in `references/sources.md`, and
route licensing questions to the Microsoft licensing guide or a licensing partner.

## Adoption considerations

The teams whose work changed should see the results and recognise them. Share findings with them, including where the
automation created extra work, and use their view to explain the numbers. Report effort at team level, never per person.

## Knowledge considerations

Not applicable to most value measurement, because it uses process and run data rather than grounding knowledge. Keep the
value report with the automation design so the next review can find its baseline.

## Security and privacy considerations

Value measurement may use system records containing personal data. Use aggregated figures, minimum group sizes for any
team-level effort data, and the least data needed to compute each measure.

## Responsible AI considerations

Check whether speed gains were bought at the cost of fairness or quality for some groups, for example more errors on
particular document types or languages. Report such effects alongside the value, not as a footnote.

## Evaluation requirements

Not applicable as a release gate, because this skill measures value after go-live rather than testing outputs. Its own
evidence is the baseline, the after data and the method, recorded so another person could repeat the calculation.

## Value measures

This skill produces the value measures for automations. The process owner owns the benefit; the automation lead owns the
method and the portfolio roll-up. Never measure or report the productivity of individuals.

## Scale notes

### Starter

Capture a simple before and after on one or two measures the owner cares about, net of review effort, and report it in
a short note after the first quarter.

### Scale

Use a standard value report for every automation, roll results into the CoE portfolio and compare estimates with
outcomes to improve future assessments.

### Enterprise

Align automation value with the organisation's benefits framework and finance processes, with benefit owners in each
business unit and regular portfolio reviews that drive extend, fix and retire decisions.

## Hand-offs

- To `value-realisation:financial-benefits` to agree any cashable or financial figures.
- To `opportunity-management:scale-or-stop` with the evidence for extending or stopping.
- To `automation:automation-assessment` with lessons on estimates for future candidates.
- To `automation:automation-process-design` where fixes to inputs or steps are recommended.

## Reviewer gates

Not applicable, because value measurement informs portfolio decisions rather than releasing a solution. Where findings
show harm or unfair effects, they are referred to the `responsible-ai` department through the process owner.

## Failure modes

- Value is reported as runs multiplied by a guessed minute count, and nobody can defend it.
- Review and exception effort is ignored, so a marginal automation is extended across the organisation.
- Released hours are presented as cash savings without finance agreeing, damaging credibility when challenged.
- No baseline was captured, and the automation's value can never be shown.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Report run counts or gross time saved as the value of an automation.
- Convert released hours to cash without finance agreeing the method.
- Back-fill a baseline from memory.
- Measure or report the productivity of individual people.

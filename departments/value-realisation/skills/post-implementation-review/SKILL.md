---
name: post-implementation-review
description: Runs a post-implementation review an agreed period after an AI solution or programme goes live, comparing actual outcomes, costs, adoption, quality and risk with the approved case, explaining each variance, capturing lessons and agreeing actions for benefits still to come. Use when a live solution reaches its review date, when a funding body asks whether the case was delivered, or when lessons should improve how future cases are estimated.
license: CC-BY-4.0
metadata:
  department: value-realisation
  lifecycle: Measure, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, nist-ai-rmf, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# Post-implementation review

## Purpose

The post-implementation review is where the organisation finds out whether an AI investment delivered what was
promised, and why or why not. This skill runs that review a set period after go-live: it compares outcomes, costs,
adoption, quality and risk with the approved case, explains the variances, records lessons that change how future cases
are estimated and delivered, and agrees what happens to the benefits still to come. It goes wrong when the review is
skipped once the team has moved on, when it becomes a celebration or a blame session, and when its lessons are filed and
never used.

## When to use

- A live AI solution, Copilot rollout or programme reaches the review date set in its realisation plan.
- A funding body, board or audit asks whether an approved case was delivered.
- A solution has been live for some time and nobody has compared results with the case.
- The organisation wants to calibrate future value estimates against past results.
- A major change to the solution or its scope is proposed and the current position needs establishing first.

## When not to use

- Deciding whether a pilot should scale, iterate, pivot or stop - use `opportunity-management:scale-or-stop`.
- Running scheduled operational reviews of every live solution - use `ai-operations:ai-review-calendar`.
- Assessing overall programme health and corrective action - use `programme-management:programme-health`.
- Re-running quality evaluation after a change - use `evaluation-quality:regression-evaluation`.
- Reviewing the portfolio of live solutions as a whole - use `ai-centre-of-excellence:coe-portfolio-management`.

## Questions to ask first

1. What exactly was approved: which case, which benefits, which costs, which risks and which dates?
2. Is enough time past go-live for the benefits to have appeared, given the timing in the realisation plan?
3. What evidence exists for each benefit, cost and risk, and at what confidence?
4. Who needs to be in the review, and who will act on its findings?
5. What decision, if any, does the review need to support (continue, extend, change, retire, release funding)?

## Required inputs

- The approved case and the ROI model as approved, from `opportunity-management:business-case` or `ai-strategy:investment-case` and `value-realisation:roi-model`.
- The benefits register entries with baselines, targets, owners and measured results.
- Actual costs from finance and the programme, including run and support costs.
- Adoption, quality and incident evidence for the period, at team or role level.
- Any earlier scale-or-stop record or change decisions.

Where evidence for a line is missing, record it as unevidenced rather than estimating it in the meeting. A benefit with
no evidence is reported as not demonstrated, with the reason, not as achieved.

## Decision framework

Compare each element of the case with the evidence and classify the variance.

| Element | Compare | Evidence source |
|---|---|---|
| Benefits | Actual against target range, by class | Benefits register, measurement results |
| Costs | Actual one-off and run costs against the model | Finance, programme budget |
| Adoption | Actual adoption against the level benefits assumed | Adoption chain, team-level reporting |
| Quality | Live quality against release threshold and guards | Quality measurement, evaluation results |
| Risk | Incidents, near misses and control effectiveness against the risk assessment | Incident log, risk register |
| Timing | Actual milestones against plan | Realisation plan |

| Variance class | Meaning | Typical action |
|---|---|---|
| Achieved | Within or above the target range, with adequate evidence | Confirm, close or move to business as usual tracking |
| Delayed | On course but later than planned | Re-profile with the owner, set the next measurement point |
| Partial | Below range for a known, fixable cause | Agree corrective actions and owners |
| Not achieved | Below range with no realistic route to target | Re-baseline the case openly, or retire the benefit |
| Not demonstrated | No adequate evidence either way | Fix measurement, then re-review |

## Practitioner approach

Schedule the review when the case is approved, not when someone remembers. The realisation plan sets the date at the
point benefits should be visible, typically after adoption has settled; reviewing too early finds nothing and reviewing
too late finds nobody who remembers why decisions were made.

Prepare the evidence before the meeting. The Benefits Realisation Lead assembles a pack: the case as approved, the
register entries, measured results with their confidence, actual costs, adoption and quality evidence, and incidents.
Circulate it in advance so the meeting discusses causes, not figures. Use the
`post-implementation-review-report` template so reviews are comparable across the portfolio.

Run the review as a learning conversation. Bring the benefit owners, the solution owner, finance, the CoE and someone
who supported users. Walk each element against the evidence and classify the variance. For every variance, ask why,
and keep asking until the cause is something the organisation could change: an adoption assumption that was too
optimistic, a process change nobody made, knowledge that was not maintained, review effort that was not modelled.
Variances in both directions deserve explanation; unexplained over-achievement is as unreliable as under-achievement.

Separate the solution from the case. A solution may work well while the case was wrong, or the case may have been sound
while delivery fell short. Recording which applies stops the organisation from drawing the wrong lesson, such as
abandoning a pattern that would work with a better estimate.

Agree actions for benefits still to come. Some will need re-profiling, some corrective action, and some should be
retired honestly. Where the case no longer holds, say so and re-baseline it openly with the sponsor; quietly carrying
unachievable benefits forward damages every later report.

Capture lessons in a form people will use. Two kinds matter most: estimation lessons (which assumptions were wrong and
by how much) and delivery lessons (what made realisation easier or harder). Feed estimation lessons into the ROI model
conventions and the value hypothesis guidance, and delivery lessons into the CoE's playbooks.

Finally, publish a short summary. Sharing results, including disappointing ones, builds credibility for the next case
and shows that the organisation measures honestly. Report at team, role or solution level only, never by individual.

## Outputs

- A post-implementation review report on the `post-implementation-review-report` template: case as approved, evidence, variance by element and class, causes, actions and lessons.
- Updated `benefits-register` entries with variance classes, re-profiled dates and retired benefits.
- An estimated-versus-actual comparison for the ROI model.
- A lessons log routed to the owners of estimation and delivery practice.
- A short summary suitable for wider sharing.

## Microsoft platform considerations

Product capability may have changed since the case was approved, for better or worse. Where a variance depends on a
feature, licence or limit, check the current position in `references/sources.md` rather than relying on what was
assumed at approval, and record what has changed.

## Adoption considerations

Adoption shortfalls are the commonest cause of benefit variance. Read adoption at team or role level and look at whether
use was sustained, and route causes to the adoption lead as programme actions rather than as criticism of teams.

## Knowledge considerations

Check whether the knowledge the solution depends on was maintained as planned. Knowledge decay is a frequent hidden
cause of falling quality and benefits, and it is fixable once named.

## Security and privacy considerations

Review any security or privacy incidents in the period and whether controls worked as intended. Evidence packs must not
contain personal data beyond what the review needs; use aggregated figures.

## Responsible AI considerations

For solutions that inform decisions about people, review whether human oversight operated as designed and whether any
harm or complaint arose. Findings go to `responsible-ai:ai-impact-assessment` for the solution's next review.

## Evaluation requirements

Compare live quality with the release evaluation threshold. If live quality has drifted, record it as a quality variance
and request re-evaluation through the solution's evaluation owner.

## Value measures

Success is the share of approved cases reviewed on schedule, the share of benefits with an evidenced variance class,
and whether the gap between estimated and actual value narrows across successive reviews, tracked by the Benefits
Realisation Lead.

## Scale notes

### Starter

A single short review meeting with the business owner and whoever leads AI, a one-page report, and one or two lessons
written down and shared.

### Scale

Scheduled reviews for every initiative above a size or risk threshold, a standard evidence pack, finance participation,
and lessons fed into the value review.

### Enterprise

A portfolio programme of reviews with independent facilitation for major investments, calibration of estimation
conventions from accumulated results, and an annual summary to the executive.

## Hand-offs

- To `opportunity-management:scale-or-stop` where the review raises a decision about the solution's future.
- To `value-realisation:benefit-realisation-plan` with re-profiled and retired benefits.
- To `value-realisation:roi-model` and `opportunity-management:value-hypothesis` with estimation lessons.
- To `ai-operations:ai-solution-retirement` where the review concludes the solution should be retired.

## Reviewer gates

Not applicable as a release gate, because a post-implementation review looks back at a live solution. Where it finds
unresolved risk or harm for a tier 2 or above solution, the finding is referred to `responsible-ai` or
`security-privacy` as appropriate.

## Failure modes

- The review never happens because the delivery team has moved on and nobody owns the date.
- Figures are debated in the meeting because the evidence pack was not prepared, and no causes are found.
- Over-achievement is celebrated without explanation, and an unreliable figure becomes the next case's assumption.
- Unachievable benefits are carried forward rather than re-baselined, and credibility drains away.
- Lessons are recorded and never reach the people who write the next case.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Report a benefit as achieved without adequate evidence.
- Use the review to assign blame to individuals or report their usage.
- Quietly re-baseline a case without the sponsor's agreement and a record of why.
- Skip the review because results are expected to be disappointing.

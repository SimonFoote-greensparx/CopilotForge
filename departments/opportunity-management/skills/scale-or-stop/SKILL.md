---
name: scale-or-stop
description: Makes the evidence-based decision after a pilot or first release to scale, iterate, pivot or stop, judged against the value hypothesis, adoption, quality and cost, and treats a well-evidenced stop as a success. Use when a pilot reaches its review date, when a sponsor wants to roll a solution out wider, or when a live initiative has been running for months without anyone deciding its future.
license: CC-BY-4.0
metadata:
  department: opportunity-management
  lifecycle: Measure, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-copilot, m365-agents, copilot-cowork, copilot-code, copilot-studio, ai-foundry, power-platform
  edition-support: scale, enterprise
  reviewers: evaluation-quality, security-privacy
  sources: ms-copilot-adoption-hub, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Scale or stop

## Purpose

This skill closes the loop between building something and deciding whether it deserves more investment. At a pre-agreed
point after a pilot or first release, it weighs the evidence on value, adoption, quality and cost and reaches one of four
decisions: scale, iterate, pivot or stop. Programmes go wrong here by never holding the review, so pilots drift on
indefinitely; by judging success on enthusiasm or usage alone; or by treating a stop as failure, which teaches teams to
hide weak results instead of learning from them.

## When to use

- A pilot or first release reaches the review date set on the roadmap.
- A sponsor wants to roll a solution out to more people, units or customers.
- An initiative has been live for months with no decision about its future.
- Evidence suggests a solution is not delivering, or is costing more to run than expected.

## When not to use

- Measuring organisation-wide Copilot adoption - use `copilot-adoption:adoption-measurement`.
- Checking that an agent is ready for its first release - use `m365-agents:agent-release-readiness`.
- Re-ranking the whole backlog - use `opportunity-management:opportunity-prioritisation`.
- Building detailed benefits models and post-implementation reviews across the portfolio - use `value-realisation:post-implementation-review`.

## Questions to ask first

1. What value hypothesis, baseline and success threshold were agreed before the pilot started?
2. What does the evidence show for value, adoption, quality and cost, and how confident are we in it?
3. What would scaling actually change: audience, units, data, connectors, autonomy or external reach?
4. Who is the business owner, and will they own the solution at the larger scale?
5. If we stopped tomorrow, what would we lose, and what have we learned?

## Required inputs

- The framed opportunity, suitability decision and risk tier from the `opportunity-canvas`.
- The value hypothesis, baseline and success threshold agreed before the pilot.
- Evidence gathered during the pilot: outcome measures against baseline, adoption at team or role level, quality and evaluation results, incidents, and run and support cost.
- Feedback from users and the support route.

If no baseline or threshold was agreed beforehand, say so in the review, reconstruct a baseline only where it can be
measured honestly, and lower the confidence of the decision. Never set the threshold after seeing the results.

## Decision framework

Rate each dimension against the threshold agreed before the pilot as met, partly met or not met.

| Dimension | Evidence |
|---|---|
| Value | Movement in the outcome measure against baseline |
| Adoption | Sustained use by the intended roles, at team or role level |
| Quality | Evaluation results against the acceptance threshold; error and incident rates |
| Cost | Build, run, support and review effort against the value achieved |

| Decision | When |
|---|---|
| Scale | Value and quality met, adoption met or clearly rising, cost proportionate, and the owner accepts the larger scope |
| Iterate | The value signal is real but quality, adoption or cost is partly met with a known, bounded fix |
| Pivot | The problem is confirmed but the solution pattern or audience is wrong; return to suitability |
| Stop | Value not met with no credible fix, or cost disproportionate, or the owner no longer accepts accountability |

A scale decision always triggers re-classification, because wider reach can move the risk tier. In a CoE, scaling
also means reuse: a pattern proven in one team is offered to others under the controls already agreed, so the
organisation governs once and repeats everywhere rather than rebuilding per unit.

## Practitioner approach

Put the review in the diary when the pilot starts, not when it ends. Agree the value hypothesis, the baseline, the
success threshold for each dimension and the date of the decision before the first user touches the solution. A pilot
without these is an experiment without a question, and its review will be decided by whoever argues most persuasively.

Gather evidence across all four dimensions, not just usage. High usage of a solution that produces wrong answers is a
quality problem, not a success. Strong value in a small, motivated team may not survive contact with the wider
workforce. Read adoption at team or role level only, and look at whether use was sustained after the novelty faded.
Include the cost of support and review, which pilots routinely understate because enthusiasts absorb it.

Hold the review with the business owner, someone from the CoE or portfolio, and the people who supported the pilot.
Walk each dimension against its threshold, using the evidence rather than impressions. Separate the problem from the
solution: a pilot can confirm that the problem is real and worth solving while showing that this solution is the wrong
answer. That is a pivot, and it is valuable.

Be explicit about what scaling changes. Moving from one team to a department, from internal to customer-facing, or
from drafting to acting can move the risk tier and bring new gates, owners and support needs. Re-classify through
`opportunity-management:risk-classification` before any scale decision is confirmed, and check that the owner, the
knowledge owners and the support route can carry the larger scope.

Treat a well-evidenced stop as a good outcome. It frees capacity for better opportunities and generates learning about
the problem, the users and the pattern. Write a short stop note: what was tried, what the evidence showed, what was
learned, and what happens to users, data and any assets. Share it with the community and thank the team. Organisations
that celebrate useful stops get more honest pilots.

Close the value-tracking stage properly. Update the backlog entry and the portfolio register with the measured value,
set beside the value and return estimated at assessment, and move the entry to its next stage. Where a solution scales,
package what made it work - instructions, knowledge sources, test set, adoption material - as a reusable asset for the
next unit, and share the result in the CoE's success stories space.

Record the decision and its reasoning, set the next review date for anything that continues, and feed the result back
into prioritisation and the roadmap. Over time, compare predicted value scores with actual results to improve how the
organisation estimates value.

## Outputs

- A scale-or-stop review on the `scale-or-stop-review` template: hypothesis and thresholds, evidence by dimension with confidence, decision and reasoning, re-classification outcome, conditions, owner confirmation and next review date.
- For a stop, a stop note covering learning and decommissioning steps for users, data and assets.
- An update to the backlog and roadmap reflecting the decision, and the measured value recorded against the solution in the portfolio register.
- For a scale decision, a reusable asset pack for other units and a short success story for the CoE community.

## Microsoft platform considerations

Scaling may change the platform position: a solution built in a personal or team zone may need moving to a governed
environment, and wider sharing may need different sharing and data policies. Check the current source records for
what controls and capabilities apply before planning the move, and do not assume pilot settings carry over.

## Adoption considerations

A scale decision is the start of an adoption effort, not the end of a project; route it to the adoption programme for
launch planning. A stop decision needs communicating to pilot users with thanks and a clear account of what replaces the
solution, if anything.

## Knowledge considerations

Check whether the knowledge the solution relies on can support the larger audience: owned, current and correctly
permissioned for everyone who will use it. Knowledge that was adequate for a pilot team is often not adequate for the
organisation.

## Security and privacy considerations

Wider reach and new data sources can expose content that was safely contained in the pilot. Where scaling raises the
tier or widens access, the `security-privacy` review must pass before the wider release. For a stop, confirm how data
and outputs created during the pilot are retained or deleted.

## Responsible AI considerations

Ask whether the pilot revealed unintended effects on people, such as uneven quality for some groups, over-reliance, or
decisions taken without the intended human check. Such findings block scaling until addressed, and for tier 3 and 4
solutions they go to `responsible-ai:ai-impact-assessment`.

## Evaluation requirements

The quality dimension relies on evaluation evidence against the threshold agreed before the pilot. For tier 2 and
above, scaling requires an evaluation set representative of the wider audience, not only the pilot group, reviewed
through `evaluation-quality:golden-dataset`.

## Value measures

The decision is measured by the value measure in the hypothesis, against its baseline, owned by the business owner.
At portfolio level, track the share of pilots reaching a timely decision, the split of scale, iterate, pivot and stop,
and the gap between predicted and realised value. Never report results by individual user.

## Scale notes

### Starter

Starter organisations rarely run formal pilots; where they do, a short conversation between the owner and the person
leading AI, recorded on one page against the original problem, is enough. The full review is omitted by default.

### Scale

Every pilot has a dated review at CoE steering using the standard template, with re-classification before any scale
decision and published stop notes.

### Enterprise

Reviews are part of portfolio governance. Units hold their own reviews for tier 0 to 2; the hub joins for tier 3 and 4
and for any cross-unit scale-up. Predicted versus realised value is reported to the executive board.

## Hand-offs

- To `opportunity-management:risk-classification` before any scale decision is confirmed.
- To `copilot-adoption:launch-plan` to plan the wider rollout.
- To `opportunity-management:ai-suitability` for a pivot.
- To `opportunity-management:opportunity-prioritisation` and `ai-strategy:ai-roadmap` to reflect the decision.

## Reviewer gates

Scaling at tier 2 and above cannot proceed until `security-privacy` has reviewed the wider access and
`evaluation-quality:ai-release-evidence` has accepted evaluation evidence for the wider audience. Where
re-classification moves the solution to tier 3 or 4, `responsible-ai:ai-impact-assessment` also applies. A stop decision needs no gate.

## Failure modes

- No review date or threshold was set, so the pilot drifts on and the decision goes to the loudest voice.
- Usage is taken as success while answer quality and real outcomes are never examined.
- A pilot scales to the whole organisation without re-classification, and sensitive content is overshared.
- Stops are treated as failures, so teams hide weak results and poor solutions linger.
- Each business unit rebuilds a proven solution from scratch because nobody packaged it for reuse.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Set or change success thresholds after seeing the pilot results.
- Scale a solution without re-classifying its risk tier and confirming its owner.
- Judge success on usage alone, or report adoption by individual user.
- Treat an evidenced stop as a failure or let it go unrecorded.

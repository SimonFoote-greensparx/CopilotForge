---
name: opportunity-prioritisation
description: Scores and balances a backlog of framed AI opportunities on value, feasibility, risk, readiness of knowledge and ownership, and strategic fit, and shapes a portfolio of quick wins and strategic bets. Admits nothing without an owner, problem, outcome, risk tier and suitability decision. Use when ideas outnumber capacity, when a steering group must choose what goes next, or when the backlog has lost its link to outcomes.
license: CC-BY-4.0
metadata:
  department: opportunity-management
  lifecycle: Envision, Mobilise, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: nist-ai-rmf, ms-copilot-adoption-hub, ms-agents-compare
  status: draft
  authors: Simon Foote
---

# Opportunity prioritisation

## Purpose

This skill decides which AI opportunities the organisation pursues next and in what mix. It scores framed and assessed
opportunities on consistent criteria, then balances the portfolio so that visible quick wins build confidence while a
small number of strategic bets move the outcomes that matter. Prioritisation usually goes wrong when the loudest sponsor
wins, when scores are taken as precise rather than as structured judgement, or when opportunities with no owner or
unready knowledge are ranked as if they could start tomorrow.

## When to use

- There are more framed opportunities than the organisation can deliver, and a choice is needed.
- A steering group or CoE must decide what enters the next roadmap horizon.
- The backlog has grown without review and no longer reflects the strategic outcomes.
- A business unit asks why its idea is waiting and needs a transparent answer.

## When not to use

- Turning an idea into a framed problem with an owner - use `opportunity-management:problem-framing`.
- Deciding whether AI is the right answer for one opportunity - use `opportunity-management:ai-suitability`.
- Assigning the risk tier - use `opportunity-management:risk-classification`.
- Sequencing the chosen work over horizons with capacity and dependencies - use `ai-strategy:ai-roadmap`.
- Deciding whether a pilot should scale or stop - use `opportunity-management:scale-or-stop`.

## Questions to ask first

1. Which strategic outcomes are the current priorities, and how are they weighted?
2. Has every candidate been framed, passed suitability and been given an initial risk tier?
3. How much delivery, review and ownership capacity is available in the coming horizon?
4. Who makes the final decision, and who may challenge it?
5. What mix of quick wins and strategic bets does the sponsor want, and why?

## Required inputs

- Framed opportunities on the `opportunity-canvas`, each with owner, problem, expected outcome, baseline or baseline plan, suitability decision and initial risk tier.
- The strategic outcomes from `ai-strategy:strategic-outcomes`.
- A view of capacity by scarce role for the next horizon.

Admission rule: an opportunity missing any of owner, problem statement, expected outcome, risk tier or suitability
decision is not scored. It is returned with the specific gap. Where an estimate (effort, value) is uncertain, record
the range and the confidence rather than a single invented number.

## Decision framework

Score each admitted opportunity from 1 to 5 on each criterion, with a sentence of evidence per score.

| Criterion | 5 looks like | 1 looks like | Default weight |
|---|---|---|---|
| Value | Large, measured cost or quality gain against a baseline | Small or unmeasured benefit | 30% |
| Strategic fit | Directly moves a priority outcome | Supports no agreed outcome | 20% |
| Feasibility | Proven pattern, skills available, low integration effort | Novel engineering, unknown effort | 20% |
| Readiness | Owner engaged, knowledge owned and current, data accessible | Owner nominal, knowledge unowned or poor | 20% |
| Risk (inverted) | Tier 0-1, controls already in place | Tier 3-4 with controls not yet available | 10% |

Then place each opportunity in a portfolio quadrant: quick win (high readiness and feasibility, moderate value), strategic
bet (high value and fit, lower feasibility or readiness), foundation-first (high value but blocked by readiness, so the
readiness work is prioritised instead), or park (low value or fit). A healthy horizon has quick wins and at least one
strategic bet, and no more strategic bets than reviewers and owners can support.

## Practitioner approach

Hold the admission rule firmly. The fastest way to lose control of a portfolio is to rank half-formed ideas alongside
framed ones; they look cheap because nobody has thought about them. Return incomplete items with a clear note of what
is missing, and track how long items wait for framing so that intake, rather than the backlog, is fixed.

Agree the weights before looking at any opportunity. Leaders who set weights after seeing the list tend to tune them to
favour a project they already like. Start from the defaults, adjust once to reflect the strategy, and record the
reasons. Revisit them at the quarterly review, not mid-cycle.

Score in a small group that includes a business voice, someone who understands delivery effort and someone who
understands risk. Write evidence for each score. Where the group disagrees by more than one point, discuss the evidence
rather than splitting the difference; disagreement usually reveals an assumption about knowledge readiness or
ownership that needs testing.

Treat the weighted total as a conversation starter, not a verdict. Look at the shape: an opportunity with high value
and low readiness is not a low priority, it is a foundation-first case, and the right decision is to fund the
readiness work (an owner, a knowledge clean-up, a baseline) and re-score next cycle. Likewise, a top-scoring quick win
may be better routed as an adoption scenario than built as a solution.

Balance the portfolio deliberately. Quick wins show staff and sponsors that the programme delivers, but a portfolio of
nothing but quick wins never moves the strategic outcomes. Strategic bets move outcomes but consume scarce owners and
reviewers, so cap them by capacity. Check spread across business units and journeys too; a portfolio concentrated in
one enthusiastic team leaves others behind and builds resentment.

Record the decision for each opportunity: proceed, foundation-first, wait for capacity, or park, with reasons. Tell
every owner the outcome and the reason, including those who were not chosen. Then hand the chosen set to
`ai-strategy:ai-roadmap` for sequencing. Re-run prioritisation at each roadmap review, after each scale-or-stop
decision, and whenever the strategic outcomes change.

## Outputs

- A scored and balanced backlog on the `prioritisation-matrix` template: admitted opportunities, scores with evidence, weights, quadrant, decision and reason, and the excluded items with their gaps.
- A portfolio view showing the balance of quick wins, strategic bets and foundation-first work by outcome, unit and journey.
- A short decision note for each opportunity owner.

## Microsoft platform considerations

Feasibility depends partly on platform: an individual Copilot pattern, a declarative agent and an engineered solution
carry very different build and operating effort. Use the suitability decision's pattern rather than re-deciding it here,
and check any capability assumption behind a feasibility score against the current source records.

## Adoption considerations

Transparent prioritisation is an adoption tool. Publish the criteria and the outcomes so people see that ideas are
judged fairly. Recognise those who raised ideas, including Champions, whether or not their idea proceeds.

## Knowledge considerations

Knowledge readiness is scored explicitly, not assumed. Where poor or unowned knowledge holds back a high-value
opportunity, the foundation-first route sends the gap to the knowledge owner and the `knowledge-management` department
(planned), with the opportunity re-scored once it is fixed.

## Security and privacy considerations

The risk criterion uses the tier from `opportunity-management:risk-classification`; this skill does not re-assess
security. Higher-tier work also consumes review capacity, which must be counted when choosing how many strategic bets
to admit.

## Responsible AI considerations

An opportunity rated tier 3 or 4 cannot be prioritised into a horizon unless the responsible AI review it needs can be
staffed in that horizon. Opportunities the strategy places outside appropriate use are parked with that reason, whatever
their score.

## Evaluation requirements

Not applicable to solution testing. The prioritisation is checked by whether each decision cites evidence for its
scores, and whether a later scale-or-stop review can compare actual value with the value score given here.

## Value measures

Measure the portfolio by the share of chosen opportunities that reach their value hypothesis at review, the time from
admission to decision, and the share of capacity spent on strategic outcomes. The portfolio owner (CoE lead or AI
portfolio manager) owns these. Never score or rank the individuals who raised ideas.

## Scale notes

### Starter

A short list of five to ten opportunities scored in one meeting with the sponsor. Use three criteria (value, readiness,
risk) if five feel heavy, and keep the admission rule.

### Scale

Quarterly prioritisation at CoE steering, with the full criteria, recorded weights, and published decisions. Re-score
after each scale-or-stop review.

### Enterprise

Business units prioritise their own backlogs on the shared criteria; the hub runs an enterprise portfolio review that
balances cross-unit bets, avoids duplicate builds and allocates shared review and engineering capacity.

## Hand-offs

- To `ai-strategy:ai-roadmap` to sequence chosen opportunities into horizons.
- To `m365-agents:agent-use-case-design` when a chosen opportunity is an agent.
- To `copilot-adoption:scenario-discovery` when a chosen quick win is best delivered as an adoption scenario.
- Back to `opportunity-management:problem-framing` for items returned with gaps.

## Reviewer gates

Not applicable. Prioritisation decides order, not release; the gates set by `opportunity-management:risk-classification`
still apply to every chosen opportunity when it reaches the Assure stage.

## Failure modes

- Incomplete ideas are ranked alongside framed ones, and the top of the list cannot actually start.
- Weights are adjusted after scoring to favour a sponsor's preferred project.
- The portfolio is all quick wins, so strategic outcomes never move, or all bets, so nothing visible lands for a year.
- Readiness is ignored, and high-value opportunities stall on unowned knowledge mid-build.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Score or admit an opportunity that lacks an owner, problem, outcome, risk tier or suitability decision.
- Present weighted scores as precise measurements rather than structured judgement.
- Change weights after seeing the scores.
- Rank or score the people who submitted ideas.

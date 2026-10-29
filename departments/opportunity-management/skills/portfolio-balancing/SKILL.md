---
name: portfolio-balancing
description: Reviews the whole AI opportunity portfolio, planned and in flight, and rebalances its mix across quick wins, strategic bets and foundation work, risk-tier exposure, scarce owner and reviewer capacity, business units, outcomes and platforms, then decides what to start, pause, accelerate or stop. Use when the portfolio feels lopsided, when reviewers or owners are overloaded, or at each quarterly portfolio review.
license: CC-BY-4.0
metadata:
  department: opportunity-management
  lifecycle: Mobilise, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: nist-ai-rmf, iso-iec-42001, ms-copilot-studio-zoned-governance
  status: draft
  authors: Simon Foote
---

# Portfolio balancing

## Purpose

This skill looks at the AI portfolio as a whole rather than one opportunity at a time. It checks whether the mix of
work in flight and about to start is healthy across value type, risk, capacity, business units, outcomes and platforms,
and makes deliberate rebalancing decisions: start, pause, accelerate, merge or stop. Scoring individual opportunities
well does not guarantee a good portfolio. Portfolios usually go wrong by filling up with quick wins that never move an
outcome, by concentrating high-risk work on the same few reviewers, or by letting one enthusiastic unit consume the
capacity everyone else was waiting for.

## When to use

- The quarterly portfolio review is due.
- Owners, makers, engineers or reviewers are overloaded and work is queuing.
- The portfolio is dominated by one business unit, one platform or one kind of work.
- Several tier 3 or tier 4 initiatives are heading for review at once.
- The strategy has been refreshed and the portfolio must be realigned to changed outcomes.

## When not to use

- Scoring and ranking individual opportunities for the next horizon - use `opportunity-management:opportunity-prioritisation`.
- Deciding the future of one pilot or release - use `opportunity-management:scale-or-stop`.
- Operating the backlog board, its stages and hygiene - use `opportunity-management:backlog-management`.
- Sequencing initiatives over time with dependencies - use `ai-strategy:ai-roadmap`.
- Running the CoE's register and lifecycle of live solutions - use `ai-centre-of-excellence:coe-portfolio-management`.

## Questions to ask first

1. Which strategic outcomes is the portfolio meant to move this horizon, and how is effort currently spread across them?
2. What is in flight, at what stage and with what risk tier?
3. Which roles are scarce (business owners, knowledge owners, makers, engineers, reviewers) and how loaded are they?
4. What mix of quick wins, strategic bets and foundation work did the sponsor intend?
5. Who has authority to pause or stop work in flight?

## Required inputs

- The backlog with stage, owner, risk tier, value range, effort range and status, from `opportunity-management:backlog-management`.
- Strategic outcomes and the current roadmap horizon.
- Capacity by scarce role for the horizon, including reviewer capacity by reviewer department.
- Recent scale-or-stop decisions and any initiatives overdue for review.

If capacity data is not available, estimate load by counting active initiatives per scarce role and mark the result as
indicative. Never balance on capacity assumptions that the managers of those roles have not confirmed.

## Decision framework

Test the portfolio against these balance checks. Each failed check needs a decision.

| Dimension | Healthy | Warning sign |
|---|---|---|
| Value type | Quick wins, strategic bets and foundation work all present, in the sponsor's intended mix | All quick wins, or strategic bets with no foundations beneath them |
| Outcomes | Every priority outcome has at least one active initiative | Effort concentrated on one outcome; another has none |
| Risk exposure | Tier 3 and 4 work within reviewer capacity, staggered | Several high-tier initiatives reaching review together |
| Capacity | No scarce role above its sustainable load | Owners or reviewers on many initiatives at once |
| Spread | Units and journeys represented in proportion to need | One unit holds most of the portfolio |
| Platform | Work spread in line with the platform strategy | Heavy build on a platform at "not now" or "specialist" posture |
| Flow | Items move through stages; few overdue for decision | Pilots past review date; work stuck awaiting owners |

Use a small set of rebalancing moves: start (from the prioritised list), pause (release capacity without losing work),
accelerate (add capacity to a strategic bet), merge (combine duplicates), stop (send to scale-or-stop or close), and
foundation-first (fund readiness work instead of a blocked initiative).

## Practitioner approach

Prepare a one-page portfolio picture before the review. Plot every initiative in flight and every one ready to start by
outcome, value type, stage and risk tier, and overlay the load on each scarce role. Patterns appear quickly on a single
page that are invisible in a list: three strategic bets all needing the same knowledge owner, or no initiative at all
for one of the outcomes.

Start with capacity, because it is the hardest constraint. Count how many active initiatives each scarce role is
carrying, by role rather than by person, and compare with the load the managers agreed is sustainable. Overloaded
reviewers are the commonest hidden bottleneck; when they are saturated, everything behind them queues and teams start
looking for ways round the gates.

Then check risk exposure. High-tier work is valuable but consumes review, evaluation and oversight capacity. Stagger
tier 3 and 4 initiatives so they do not reach the same gates in the same month, and do not start one unless its
reviews can be staffed.

Check the value mix against the sponsor's intent. A portfolio of quick wins looks busy and moves nothing strategic; a
portfolio of strategic bets with no visible early results loses sponsor patience. Where strategic bets are blocked by
readiness, use foundation-first moves rather than letting them sit.

Check spread across outcomes, units and platforms. Gaps often reveal adoption or ownership problems rather than a lack
of ideas; pass them to the relevant teams. Concentration on a platform outside its agreed posture is a strategy issue
for the AI strategy lead.

Make the decisions explicitly. For each failed check, propose a move, its effect on capacity and outcomes, and who is
affected. Pausing or stopping work in flight is the hardest decision; anchor it in the evidence and in the value
hypothesis, and route individual futures through `opportunity-management:scale-or-stop` where a review is due.

Record the decisions and tell affected owners before the wider announcement, with the reasoning. Update the backlog and
roadmap the same week. Revisit at the next quarterly review, or sooner if capacity changes sharply.

## Outputs

- A portfolio balance review: the one-page picture, results of each balance check, rebalancing decisions with reasons, and their effect on capacity and outcomes.
- Updated backlog entries on the `prioritisation-matrix` template reflecting starts, pauses, merges and stops.
- A capacity view by scarce role (never by named individual) for the next horizon.
- A short note for each affected owner explaining the decision.

## Microsoft platform considerations

Check platform concentration against the organisation's platform strategy. Heavy Copilot Studio building needs
environment, data policy and managed environment capacity; Foundry work needs engineering and operations capacity.
Platform capability and licensing assumptions are checked against `references/sources.md`, not decided here.

## Adoption considerations

A balanced portfolio includes adoption work, not only builds. Where many ideas resolve to existing capability, a
portfolio decision to invest in an adoption campaign may deliver more value than another build.

## Knowledge considerations

Knowledge owners are often the scarcest role and the least visible. Count their load explicitly, and treat knowledge
readiness work as foundation initiatives in the portfolio rather than hidden tasks inside builds.

## Security and privacy considerations

Aggregate exposure matters: several solutions touching the same sensitive data or widening access together may need a
combined look by the security lead. Raise this rather than assuming each initiative's review covers it.

## Responsible AI considerations

Track how many high-impact initiatives are in flight and whether oversight and review capacity matches. The risk
management source records support treating aggregate AI risk as a portfolio concern, not only a solution concern.

## Evaluation requirements

Not applicable to solution testing. The balancing review is checked by whether each decision is traceable to a failed
balance check and whether the next review shows the expected change in load or mix.

## Value measures

Measure share of capacity on priority outcomes, number of scarce roles above sustainable load, time items wait at each
stage, and share of pilots decided on time. The AI portfolio manager owns these. Capacity is reported by role, never as
a ranking of individuals.

## Scale notes

### Starter

A short quarterly conversation with the sponsor over a list of fewer than ten initiatives, checking value mix, owner
load and risk. The main move is usually "pause one, finish one".

### Scale

A structured quarterly review at CoE steering with the one-page picture, all balance checks and recorded decisions.

### Enterprise

Business units balance their own portfolios; the hub balances shared capacity (reviewers, engineers, platforms) and
cross-unit bets, and merges duplicate initiatives across units.

## Hand-offs

- To `opportunity-management:opportunity-prioritisation` to fill freed capacity from the scored list.
- To `opportunity-management:scale-or-stop` for initiatives whose future must be decided.
- To `ai-strategy:ai-roadmap` to reflect rebalanced work in the horizons.
- To `programme-management:budget-and-capacity` when capacity must be added or released.

## Reviewer gates

Not applicable. Balancing decides the mix and pace of work, not releases. Reviewer departments are consulted on their
own capacity, and every initiative still passes the gates set by its risk tier.

## Failure modes

- Each opportunity is scored well, but the portfolio as a whole is all quick wins and moves no outcome.
- Reviewers are saturated, gates become queues, and teams start working around them.
- Pausing and stopping are avoided, so everything continues slowly and nothing finishes.
- One unit dominates because it shouts loudest, and others disengage.
- Capacity is tracked by named individuals, which feels like surveillance and is resisted.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Start a tier 3 or tier 4 initiative whose reviews cannot be staffed in the horizon.
- Report capacity or load as a ranking of named individuals.
- Pause or stop work in flight without telling its owner first and giving the reason.
- Treat balancing as re-scoring; individual scores belong to prioritisation.

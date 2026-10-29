---
name: ai-review-calendar
description: Maintains a calendar of scheduled reviews for every live agent and AI solution, with frequency set by risk tier, a standard agenda covering ownership, quality, usage, feedback, incidents, knowledge, risk tier and cost, and a recorded outcome to continue, improve, re-tier, escalate or retire. Use when live solutions have no review dates, when reviews keep slipping, or when nobody can say which solutions are still needed.
license: CC-BY-4.0
metadata:
  department: ai-operations
  lifecycle: Measure, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, copilot-cowork, ai-foundry, power-platform, platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-coe-starter-kit, ms-managed-environments, ms-copilot-studio-zoned-governance, iso-iec-42001, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI review calendar

## Purpose

Every live AI solution should be looked at on a schedule, not only when something breaks. Owners change, knowledge
ages, platforms update, usage shifts and risk tiers drift as solutions acquire new audiences or actions. This skill
keeps a calendar of scheduled reviews for every live solution, sets their frequency by risk tier, gives each review a
standard agenda drawing on operational evidence, and records an outcome. Review calendars usually fail because review
dates are set at release and then forgotten, because reviews become a tick-box with no evidence, or because nobody has
the authority to act on the outcome.

## When to use

- Live solutions have no scheduled review dates.
- Review dates exist but keep slipping, and nobody follows up.
- Nobody can say which live solutions are still needed, used or owned.
- A new release gate requires a review date and the organisation needs a consistent approach.
- An audit or management system review asks how live AI solutions are overseen.

## When not to use

- Deciding to scale, iterate, pivot or stop after a pilot - use `opportunity-management:scale-or-stop`.
- Comparing realised benefits with the business case - use `value-realisation:post-implementation-review`.
- Setting the CoE's own meeting rhythm and terms of reference - use `ai-centre-of-excellence:coe-cadence`.
- Maintaining the inventory of agents, flows and solutions - use `platform-governance:ai-solution-inventory`.
- Managing one agent through its whole lifecycle - use `m365-agents:agent-lifecycle` or `copilot-studio:studio-agent-lifecycle`.

## Questions to ask first

1. Which solutions are live, and where is the authoritative list?
2. Who owns each solution, and who has authority to decide its future?
3. What evidence is available for review - monitoring, feedback, incidents, evaluation, knowledge freshness, cost?
4. What happens when a review is overdue or an owner does not respond?
5. Which forum receives review outcomes that need a decision beyond the owner?

## Required inputs

- The solution inventory with owners, risk tiers and release dates, from `platform-governance:ai-solution-inventory` or the CoE register.
- Monitoring trends, feedback themes, incident records and refresh logs for each solution.
- The release evidence and value measures recorded at release.
- The organisation's rule for what happens to overdue or ownerless solutions.

Where the inventory is incomplete, the calendar starts with what is known and a discovery task for the rest; never
treat an unlisted solution as reviewed.

## Decision framework

Set frequency by tier and adjust for events. The frequencies are a CopilotForge starting convention; set your own and
record them.

| Tier | Scheduled review | Brought forward by |
|---|---|---|
| 1 | Twice a year, by the owner | Owner change, audience change, repeated negative feedback |
| 2 | Quarterly, owner with CoE | Plus any high-severity incident, quality trigger or material change |
| 3 | Quarterly, with reviewer input | Plus any incident, platform change affecting grounding, safety or actions |
| 4 | Monthly or as set at risk acceptance | Plus any event in the risk acceptance conditions |

Standard agenda for every review:

| Area | Question |
|---|---|
| Ownership | Are the business, solution and knowledge owners still in role and active? |
| Purpose and scope | Is the solution still needed for its original purpose, and has its use drifted? |
| Quality | Do sampled answers still meet the release thresholds? |
| Usage and feedback | Who uses it, at team level, and what themes are users raising? |
| Incidents | What happened since last review, and are actions closed? |
| Knowledge | Are sources within review dates, and were refreshes evidenced? |
| Risk tier | Has audience, data, autonomy or impact changed enough to re-tier? |
| Cost and value | Is consumption within plan, and is the value measure on track? |

Outcomes: continue; improve with actions; re-tier and re-review through the relevant gates; escalate for a
scale-or-stop decision; retire.

## Practitioner approach

Build the calendar from the inventory. Every live solution gets a next review date set by its tier, an owner and a
forum. Put review dates where owners will see them, in their own calendars as well as the register. A calendar only the
operations team can see is a list of missed meetings.

Prepare the evidence pack, not the owner's memory. Before each review, gather monitoring trends, a quality sample, feedback
themes, incidents and refresh logs. Keep it short: one page per solution with exceptions highlighted. The aim is a
fifteen-minute conversation for a healthy tier 1 or 2 solution, and a deeper one only where evidence demands it.

Run the agenda in order and record each answer. Ownership comes first, because a solution without an active owner
cannot be improved or defended. Purpose comes second: many solutions drift from their original scope, and a solution
used for something it was never evaluated for is a risk tier question.

Re-tier honestly. If an agent built for one team now serves a department, or has gained an action, its tier may have
risen. Send it back through `opportunity-management:risk-classification` and the gates of the new tier before the
next release of anything.

Record one outcome per review, with actions, owners and dates. "Continue" is a valid outcome, but it needs evidence.
"Retire" is equally valid and should be welcomed, not avoided; unused solutions carry cost, risk and maintenance for no
value.

Handle overdue reviews firmly. Agree a rule with the CoE: a reminder, then escalation to the business owner, then a
restriction such as narrowing sharing, and finally retirement for solutions that remain unreviewed and ownerless.
Apply the rule consistently, and tell owners in advance.

Feed the portfolio. Summarise review outcomes for the CoE on its cadence: solutions reviewed on time, outcomes, re-tiered
solutions and retirements. Patterns across reviews, such as repeated knowledge expiry, inform standards and training.

## Outputs

- A review calendar for all live solutions with tier, frequency, next date, owner and forum, recorded in each `support-and-monitoring-plan`.
- A one-page review pack template and completed packs per review.
- A review record per solution with outcome, actions, owners and dates.
- A portfolio summary for the CoE cadence.

## Microsoft platform considerations

Inventory and admin tooling, including the CoE Starter Kit and Managed Environments features, can help list solutions,
find inactive ones and identify owners; their capabilities change, so confirm them in `ms-coe-starter-kit` and
`ms-managed-environments`. Environment zoning described in `ms-copilot-studio-zoned-governance` can guide which
solutions need closer review.

## Adoption considerations

Review outcomes are a source of good news as well as problems. Share examples of solutions that improved after review
or were retired cleanly, so owners see reviews as useful rather than bureaucratic.

## Knowledge considerations

Knowledge freshness is a standing agenda item. Align review dates with knowledge owners' cycles where possible, so one
conversation covers both.

## Security and privacy considerations

Reviews check that sharing scope and connections still match what was approved. Any widening since release goes back to
the `security-privacy` reviewers before the solution continues.

## Responsible AI considerations

For solutions affecting people, reviews include whether oversight arrangements still work and whether any complaints or
appeals arose, with input from the `responsible-ai` reviewers at tier 3 and 4.

## Evaluation requirements

Each review includes a quality sample scored against the release rubric. Results below threshold trigger
`evaluation-quality:regression-evaluation` before the outcome is "continue".

## Value measures

Track the share of live solutions reviewed on time, outcomes by type, solutions re-tiered and solutions retired, and
time from overdue to resolution. The AI Operations Lead owns these measures; report by solution and portfolio, never by
individual owner performance.

## Scale notes

### Starter

A simple list of live agents with owners and next review dates, reviewed by the owner with whoever leads AI, using the
standard agenda on one page.

### Scale

A maintained calendar linked to the solution inventory, evidence packs prepared by operations, reviews in the CoE
cadence for tier 2 and above, and a consistent overdue rule.

### Enterprise

Federated reviews by business units for tier 1 and 2 under the same agenda, central reviews for tier 3 and 4 with
reviewer input, and portfolio reporting to the CoE and risk committees.

## Hand-offs

- To `opportunity-management:scale-or-stop` when a review escalates a scale or stop decision.
- To `opportunity-management:risk-classification` when a solution needs re-tiering.
- To `ai-operations:ai-solution-retirement` when the outcome is retire.
- To `value-realisation:post-implementation-review` when value evidence needs a fuller review.

## Reviewer gates

Not applicable as a gate in itself; scheduled reviews are an operating control. Where a review re-tiers a solution or
finds widened sharing, the `security-privacy`, `evaluation-quality` and `responsible-ai` gates for the new tier apply
before it continues.

## Failure modes

- Review dates are set at release and never appear in anyone's calendar.
- Reviews rely on the owner's impressions with no evidence, and every solution is "continue".
- A solution's audience grows without re-tiering, and it runs at tier 3 with tier 1 controls.
- Overdue reviews have no consequence, so ownerless solutions accumulate.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Leave a live solution without a next review date and an owner.
- Record "continue" without evidence of quality, ownership and purpose.
- Use reviews to assess or rank individual owners or makers.
- Let a solution run at a higher effective tier than the gates it passed.

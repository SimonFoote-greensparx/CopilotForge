---
name: ai-roadmap
description: Builds a prioritised, sequenced AI roadmap across the Adopt AI, Build with AI and Scale AI journeys and the lifecycle stages, showing dependencies, capacity, foundations and review points against the agreed outcomes. Use when leaders need a plan for the next twelve to twenty-four months, when initiatives compete for the same people, or when an existing roadmap has drifted from its outcomes.
license: CC-BY-4.0
metadata:
  department: ai-strategy
  lifecycle: Mobilise, Scale, Improve
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-code, copilot-studio, ai-foundry, power-platform
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-copilot-adoption-hub, ms-copilot-overview, ms-agents-compare
  status: draft
  authors: Simon Foote
---

# AI roadmap

## Purpose

This skill turns agreed outcomes, the maturity baseline and a prioritised backlog into a sequenced plan that the
organisation can resource and review. It balances three journeys (Adopt AI, Build with AI and Scale AI) so that people
capability, solutions and the operating foundations advance together. Roadmaps usually go wrong by listing initiatives
without the foundations they depend on, by scheduling more work than the organisation's people can absorb, or by
becoming a fixed plan that is never revisited as evidence arrives.

## When to use

- Strategic outcomes are agreed and leaders need a twelve to twenty-four month plan to deliver them.
- Several initiatives compete for the same owners, makers, Champions or reviewers.
- A roadmap exists but has drifted into a list of tools or pilots unconnected to outcomes.
- A scale-or-stop decision, a new business unit or a major product change requires the plan to be re-sequenced.

## When not to use

- Agreeing the outcomes and principles the roadmap serves - use `ai-strategy:strategic-outcomes`.
- Scoring and ranking individual opportunities in the backlog - use `opportunity-management:opportunity-prioritisation`.
- Planning a specific Copilot launch wave in detail - use `copilot-adoption:launch-plan`.
- Running the programme plan, RAID log and stage gates day to day - use `programme-management:integrated-roadmap`.

## Questions to ask first

1. Which strategic outcomes does the roadmap serve, and which matter most in the first horizon?
2. What did the maturity assessment identify as the binding constraints, such as knowledge ownership, governance or adoption?
3. What is in the prioritised opportunity backlog, and which items have passed suitability and risk classification?
4. How much capacity exists, in business owners, knowledge owners, makers, Champions, reviewers and partners, per quarter?
5. When will leaders review the roadmap, and who can change it?

## Required inputs

- Strategic outcomes, principles and exclusions from `ai-strategy:strategic-outcomes`.
- The maturity assessment from `ai-strategy:ai-maturity-assessment`.
- The prioritised backlog from `opportunity-management:opportunity-prioritisation`.
- The target operating model from `ai-strategy:ai-operating-model`, or a note that one is still being designed.
- A realistic view of capacity by role, including partner support.

Where capacity or backlog information is missing, build a first horizon only, mark later horizons "to confirm" and set
an early review. Never fill a horizon with initiatives that have no owner.

## Decision framework

Sequence work using these rules, in order.

| Rule | Apply it like this |
|---|---|
| Foundations first | Approved-use guidance, ownership, knowledge readiness and measurement are scheduled before the solutions that depend on them |
| Balance the journeys | Each horizon contains Adopt, Build and Scale work; a horizon that is all Build is a warning sign |
| Respect risk tiers | Tier 2 and above initiatives are scheduled only when the gates they need can be staffed |
| Fit capacity | Total demand on each scarce role per quarter stays within its stated capacity, with a reserve for support and unplanned work |
| Mix quick wins and bets | Early horizons include visible tier 0-1 wins that build confidence alongside one or two strategic bets |
| Decision points | Every pilot and first release has a dated scale-or-stop review on the roadmap |

Use three horizons: now (the next quarter, committed), next (two to three quarters, planned) and later (beyond, indicative).

## Practitioner approach

Start by pinning the roadmap to the outcomes. Write each outcome across the top, then ask what has to be true, in
people, solutions and foundations, for it to move. This produces three lanes per outcome: Adopt AI work (readiness,
scenarios, learning, Champions), Build with AI work (agents, Cowork task designs, automations, engineered solutions)
and Scale AI work (operating model, CoE, governance, knowledge ownership, measurement). Anything on the backlog that
serves no outcome is parked, not slotted in.

Map dependencies explicitly. An agent over HR policies depends on the policies having an owner and a review cycle; a
customer-facing assistant depends on responsible AI and incident response capability that may not exist yet. Draw these
links and schedule the foundation first, even when it is less visible. Use the maturity assessment's binding constraints
as the first candidates for foundation work.

Then test capacity. List the scarce roles and estimate demand per quarter. In most organisations the constraint is not
makers but business owners, knowledge owners and reviewers. If three tier 2 agents land in one quarter and there is one
security reviewer, the roadmap is fiction. Move work rather than assuming people will stretch, and keep a reserve for
supporting what has already launched.

Place the lifecycle stages on each initiative so progress is visible: Envision, Deliver, Assure, Launch, Measure, then
a dated scale-or-stop review. Put those reviews on the roadmap itself; they are where evidence changes the plan. Also
put a roadmap review in the governance calendar, normally quarterly, at which outcomes are checked, completed work is
assessed and the next horizon is committed.

Keep platform choices tentative in later horizons. Product capabilities and names change, and an initiative scheduled
for a specific feature eighteen months away is a guess. Record the pattern needed (individual use, shared agent,
engineered solution) and confirm the platform against the current source records when the initiative enters the "now"
horizon.

Present the roadmap on one page per audience: the executive view by outcome and horizon, the delivery view by
initiative and dependency, and the people view showing what changes for staff and when. Keep them consistent by
generating all three from the same source table.

## Outputs

- An AI roadmap on the `ai-roadmap` template: outcomes, three horizons, initiatives by journey lane with owner, risk tier, lifecycle stage and dependencies, capacity check and dated review points.
- A dependency view showing foundation work and what it unblocks.
- A capacity summary by scarce role per quarter, with the reserve stated.
- A review calendar with roadmap reviews and scale-or-stop decisions.

## Microsoft platform considerations

The roadmap names solution patterns before products. Where an initiative depends on a platform capability, check the
source records for availability, licensing and limits before it enters the committed horizon, and record the check.
Different patterns (individual use, declarative agents, Copilot Studio, Cowork, Copilot Code, Microsoft Foundry) carry
different ownership and operating costs, so the roadmap should show the support load each will add.

## Adoption considerations

Pace change at the rate people can absorb it. Several launches hitting the same roles in one quarter dilute each other.
Show the people view to managers and Champions so they can prepare, and leave room after each launch for reinforcement.

## Knowledge considerations

Treat knowledge readiness as roadmap work, with owners and dates, not as an assumption. An initiative grounded on
knowledge that is not yet owned and current cannot enter the "now" horizon until that precondition is met.

## Security and privacy considerations

Schedule security and privacy reviews as capacity, not as a formality at the end. Initiatives that widen access to
sensitive data must show the review in the plan before their build starts.

## Responsible AI considerations

Higher-tier initiatives need responsible AI review, human oversight design and incident response before launch.
Where that capability does not yet exist, schedule building it as Scale AI work ahead of the initiative, or move the
initiative to a later horizon.

## Evaluation requirements

Not applicable to the roadmap itself, which is a plan. Each Build initiative on it must carry the evaluation activity
its risk tier requires, scheduled before its launch date.

## Value measures

Roadmap progress is measured by movement of the outcome measures, not by initiatives delivered. At each review, report
each outcome's measure against its baseline, the initiatives that contributed, and any initiative stopped or re-scoped
with the reason. The sponsor owns the review.

## Scale notes

### Starter

One page, two horizons, a handful of initiatives, mostly Adopt AI with one or two shared assets. The working group
reviews it quarterly with the sponsor.

### Scale

Three horizons, journey lanes, a capacity check for owners and reviewers, and scale-or-stop reviews built in. Reviewed
quarterly at steering.

### Enterprise

An enterprise roadmap of shared foundations and cross-unit initiatives, with business-unit roadmaps beneath it that
follow the same structure. The hub reconciles dependencies and capacity across units and reports to the executive board.

## Hand-offs

- To `opportunity-management:opportunity-prioritisation` to refresh the backlog that feeds the next horizon.
- To `copilot-adoption:launch-plan` for detailed planning of Adopt AI launches.
- To `opportunity-management:scale-or-stop` for each dated review point.
- To `ai-centre-of-excellence:coe-cadence` to put roadmap reviews into the governance calendar.

## Reviewer gates

Advisory only. `design-authority:platform-fit-review` may review the roadmap for platform sprawl or sequencing that
schedules tier 2 and above solutions ahead of the foundations they need. The CoE lead records the advice and the
sponsor decides.

## Failure modes

- The roadmap lists solutions only, and the foundations they depend on are discovered mid-build.
- Demand on owners and reviewers exceeds capacity, so every initiative slips together.
- No scale-or-stop points are scheduled, so pilots continue indefinitely without a decision.
- Later horizons commit to specific product features that change or never arrive.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Schedule an initiative that has no business owner or serves no agreed outcome.
- Commit later horizons to product capabilities asserted from memory.
- Plan beyond the stated capacity of owners, knowledge owners and reviewers.
- Treat delivery of initiatives as the measure of success instead of movement in outcomes.

---
name: integrated-roadmap
description: Integrates every AI programme workstream plan - adoption, Champions, learning, knowledge, platform, agent delivery, governance and value - into one dated delivery plan with milestones, a critical path, cross-workstream dependencies and a baseline that changes only by decision. Use when workstreams plan separately, when nobody can say what the next milestone depends on, or when the strategic roadmap needs turning into a plan people can run.
license: CC-BY-4.0
metadata:
  department: programme-management
  lifecycle: Mobilise, Enable, Deliver, Launch
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# Integrated roadmap

## Purpose

The strategic AI roadmap says what will happen in which horizon; a programme also needs a plan that says what happens
in which week and what each milestone waits for. This skill integrates the workstream plans into one dated delivery plan
with milestones, a critical path and the dependencies between workstreams, and sets a baseline that changes only by
decision. Integrated plans go wrong when they are a stapled collection of workstream plans, when the dates come from
hope rather than capacity, or when they track activity and lose sight of the outcomes the roadmap serves.

## When to use

- A programme has been chartered and its workstreams have drafted their own plans.
- Workstream leads disagree about when something will be ready, or discover late that they were waiting on each other.
- The strategic roadmap needs turning into dated milestones for the next one or two quarters.
- A launch date has been proposed and someone needs to show what must be true by then.
- The plan has slipped and needs re-baselining with the board's agreement.

## When not to use

- Sequencing initiatives across horizons against strategic outcomes - use `ai-strategy:ai-roadmap`.
- Managing an individual dependency with its giver and receiver, including Microsoft release changes - use `programme-management:dependency-management`.
- Recording the risks and issues the plan reveals - use `programme-management:programme-risk-log`.
- Planning one Copilot launch in detail by persona and wave - use `copilot-adoption:launch-plan`.
- Planning the CoE's own launch phases - use `ai-centre-of-excellence:coe-launch-roadmap`.

## Questions to ask first

1. Which strategic roadmap initiatives fall within this programme's charter, and which horizon is committed?
2. What plans do the workstreams already have, at what level of detail, and who owns each?
3. Which dates are fixed by something outside the programme (a licence renewal, a contract, a business event, a regulator), and which are targets?
4. Which scarce roles (business owners, knowledge owners, reviewers, makers) do several workstreams need at the same time?
5. Who can approve a change to the baseline?

## Required inputs

- The signed programme charter from `programme-management:programme-charter`, with workstreams and tolerances.
- The strategic roadmap from `ai-strategy:ai-roadmap`, showing initiatives, horizons and foundations.
- Each workstream's draft plan, however rough, with its owner.
- Declared capacity for scarce roles from `programme-management:budget-and-capacity` or the ownership map.
- Programme stage gates from `programme-management:stage-gates`, so gate dates sit on the plan.

If a workstream has no plan, record its milestones as `[To confirm: ...]` with the owner who will supply them, and show
the gap on the plan rather than inventing dates.

## Decision framework

Integrate at the level of milestones, not tasks. A milestone is a verifiable state ("knowledge sources for the HR agent
have owners and a review date"), not an activity ("work on knowledge").

| Element | Rule |
|---|---|
| Milestones | Each has an owner, a definition of done and the evidence that shows it; three to eight per workstream per quarter |
| Dependencies | Only cross-workstream or external links; each has a giver, a receiver and a need-by date |
| Critical path | The longest chain of dependent milestones to the next gate or launch; managed weekly |
| Capacity check | No scarce role is committed beyond its declared time in any month, with a reserve for supporting what is live |
| Fixed and target dates | Mark which is which; only fixed dates may be shown without a confidence range |
| Baseline | Set after the board approves the plan; changes beyond tolerance need a recorded decision |

Typical cross-workstream links worth checking in every AI programme:

| Receiver | Usually depends on |
|---|---|
| Copilot launch wave | Technical readiness, approved-use guidance, Champions in place, support route ready |
| Agent release | Knowledge sources ready, evaluation set agreed, reviewer slots booked, owner and support named |
| Measurement | Baseline captured before the change it measures |
| Champion learning | Scenarios and approved-use guidance published |
| Scale-out to a new unit | A scale-or-stop decision on the pilot |

## Practitioner approach

Collect the workstream plans as they are and do not rewrite them. Ask each lead for their milestones over the committed
horizon, the definition of done for each, and what they need from others. The integrated plan sits above the workstream
plans; it does not replace them, and workstreams that feel their plans have been taken over stop maintaining them.

Lay the milestones on a single timeline grouped by workstream, then walk the dependencies. For each milestone ask "what
must be true before this can happen, and who makes it true?". Most AI programme slippage comes from the same few links:
an agent cannot be tested because knowledge owners have not cleaned the content, a Copilot wave cannot launch because the
support route is not ready, a benefit cannot be shown because nobody measured the baseline. Draw these links explicitly
and give each one to `programme-management:dependency-management` to track.

Find the critical path to the next stage gate or launch and say plainly which milestones are on it. These get weekly
attention; everything else is reviewed at the workstream meeting. If the critical path runs through a single scarce role,
such as the only security reviewer, that is a capacity risk to record, not a scheduling detail.

Test the plan against capacity before anyone sees dates. Add up what each scarce role is committed to by month and
compare it with what they have declared. Business owners and knowledge owners are usually more constrained than makers.
Where demand exceeds supply, move milestones or reduce scope; do not assume people will stretch, and keep time for
supporting what has already been released.

Show confidence honestly. Fixed external dates appear as dates; everything else gets a target with a range until the
work is understood. Product-dependent milestones carry a note of the capability relied on and the source record checked,
because Microsoft release timing is outside the programme's control.

Agree the plan at the programme board and baseline it. From then on, report progress against the baseline, forecast
honestly, and bring changes beyond tolerance to the board as decisions rather than quietly moving dates. Re-baseline at
each stage gate, and keep the link back to `ai-strategy:ai-roadmap` so a change in the plan that affects an outcome is
visible to the people who own the strategy.

## Outputs

- An integrated delivery plan: milestones by workstream with owner, definition of done, evidence, fixed or target date and confidence, built from the initiatives in the `ai-roadmap` template.
- A critical path to the next gate or launch, with the milestones on it named.
- A capacity check by scarce role and month, with the actions taken to resolve overload.
- A baseline record and a change log of approved re-baselines.

## Microsoft platform considerations

Milestones that depend on a Microsoft capability, a release wave or a licence change are marked as such, with the
capability relied on and the source record checked. Do not schedule against a feature's expected availability from
memory; check `references/sources.md` and track the link through `programme-management:dependency-management`.

## Adoption considerations

Give adoption milestones the same standing as build milestones. Plans dominated by technical go-lives tend to schedule
launches without the communications, Champions and manager enablement that make them land.

## Knowledge considerations

Treat knowledge readiness as milestones with owners, placed before the agent and Cowork milestones that need it. Content
clean-up routinely takes longer than build, so give it its own confidence range.

## Security and privacy considerations

Reviewer slots for `security-privacy` and, where needed, privacy assessment are booked milestones on the plan, not
assumed. Store the plan with programme records; it should name roles, not individuals.

## Responsible AI considerations

For tier 3 and 4 solutions, schedule the `responsible-ai` review and any risk acceptance decision as milestones on the
critical path. A plan that leaves them to the week before launch invites pressure to waive them.

## Evaluation requirements

Not applicable to the plan itself; it must show the evaluation milestones each solution needs (evaluation set agreed,
results reviewed) before its release milestone, held by `evaluation-quality` from risk tier 2.

## Value measures

Track milestone predictability (share of milestones met within their confidence range) and critical path stability at
programme level, reported by the AI Programme Manager to the board. Baseline capture milestones protect the later value
case.

## Scale notes

### Starter

One page: a dozen milestones across three or four workstreams over a quarter, with the main dependencies drawn and a
monthly check at the working group.

### Scale

A milestone plan per workstream rolled up into one integrated view, a named critical path, a capacity check by month and
a formal baseline agreed at the programme board.

### Enterprise

Integrated plans per tranche and business unit rolled up to a programme view, with a planning office maintaining the
baseline and cross-unit dependencies reviewed at the portfolio board.

## Hand-offs

- To `programme-management:dependency-management` for each cross-workstream and external dependency.
- To `programme-management:programme-risk-log` for risks and issues the plan reveals.
- To `programme-management:programme-board-cadence` for baseline approval and change decisions.
- To `programme-management:programme-health` for schedule health reporting.

## Reviewer gates

Not applicable, because the plan releases no solution; it schedules the `security-privacy`, `evaluation-quality`,
`responsible-ai` and `design-authority` reviews its solutions need, from the risk tiers those departments set.

## Failure modes

- Workstream plans are stapled together and nobody owns the links between them.
- Dates are set top-down from a launch announcement and the capacity check is skipped.
- Knowledge readiness is missing from the plan, so agent testing stalls on content nobody has cleaned.
- The baseline moves quietly every month and the board loses any sense of slippage.
- Milestones depend on a Microsoft feature assumed from memory that arrives later than planned.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Invent dates or milestones for a workstream that has not supplied them.
- Commit a scarce role beyond its declared capacity.
- Move the baseline without a recorded decision.
- Schedule against Microsoft product availability from memory.

---
name: coe-launch-roadmap
description: Turns an agreed CoE charter and operating model into a dated launch plan across the Establish, Foundation, Deliver and Scale phases - workstreams, milestones, exit criteria, quick-win selection, first-ninety-day actions, dependencies, launch communications and go or hold decisions at each phase boundary. Use when the CoE is approved and needs a plan to start, or when a launch has drifted with no clear next milestone.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Mobilise, Launch, Deliver, Scale
  maturity: explorer, adopter, builder, scaler
  risk-tiers: 0, 1, 2
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-coe-starter-kit, ms-copilot-studio-guidance, ms-champion-programme
  status: draft
  authors: Simon Foote
---

# CoE launch roadmap

## Purpose

An approved CoE needs a plan that turns intent into the first visible results within a few months. This skill builds
that plan: the four launch phases with dated milestones and exit criteria, the workstreams that run through them, the
selection of quick wins, the first ninety days in detail, and a go or hold decision at each phase boundary. Launches go
wrong by announcing the CoE before it can respond to anyone, by starting builds before the backlog and knowledge
register exist, and by treating the phase dates as commitments rather than moving on when the exit criteria are met.

## When to use

- The charter and operating model are agreed and the CoE needs a dated plan to start.
- A sponsor asks when the CoE will show its first results and what has to happen first.
- A launch began but has drifted, and nobody can say what the next milestone is.
- A new spoke is launching under an existing hub and needs its own plan.

## When not to use

- Checking whether the organisation is ready to launch a CoE at all - use `ai-centre-of-excellence:coe-readiness`.
- Designing the CoE shape and flow, including the summary launch phases - use `ai-centre-of-excellence:coe-operating-model`.
- Building the organisation-wide AI roadmap across all journeys - use `ai-strategy:ai-roadmap`.
- Integrating all programme workstreams into one programme roadmap - use `programme-management:integrated-roadmap`.
- Planning a Copilot rollout to users - use `copilot-adoption:launch-plan`.

## Questions to ask first

1. What did the readiness assessment conclude, and which conditions are still open?
2. When does the sponsor expect to see the first live result, and is that realistic for the capacity agreed?
3. Which pillars are active at launch, and which are deferred to later phases?
4. Which existing agents, automations or ideas could become quick wins, and do they have owners?
5. What fixed dates or dependencies matter: budget cycles, Copilot rollout waves, policy approvals, partner availability?

## Required inputs

- The readiness verdict and open conditions from `ai-centre-of-excellence:coe-readiness`.
- The signed charter from `ai-centre-of-excellence:coe-charter`.
- The operating model and phase summary from `ai-centre-of-excellence:coe-operating-model`.
- The team terms of reference from `ai-centre-of-excellence:coe-team-design`, with agreed time.
- Any organisation-wide AI roadmap on the `ai-roadmap` template, so the CoE plan fits it.

Where capacity or dates are unknown, mark them `[To confirm]` in the plan and make confirming them an Establish
milestone. Never commit a phase date that depends on unconfirmed capacity.

## Decision framework

Use four phases. Durations are typical starting points; exit criteria, not dates, decide when a phase ends.

| Phase | Typical duration | Workstream focus | Exit criteria |
|---|---|---|---|
| Establish | About a month | Sponsor, team, forums, collaboration space, readiness conditions | Sponsor commitment agreed; lead and core team in place with agreed time; forums scheduled; collaboration space live; front door ready but not yet announced |
| Foundation | About a month | Intake and backlog, knowledge register, risk tiers and register, Champions links, baselines | Backlog live with first ideas framed; knowledge register started; approved-use guidance and tiers in use; first quick wins chosen with owners and baselines |
| Deliver | Two to three months | Quick wins, first agents or automations, adoption, value measurement | Quick wins live with owners; first value measured against baseline; first value review held |
| Scale | Ongoing | Reuse, wider rollout, new pillars or spokes | Patterns reused by other teams; pipeline flowing within service levels; maturity reviewed |

Select quick wins with explicit tests.

| Test | Quick win if | Not a quick win if |
|---|---|---|
| Tier | Tier 0 or 1, or tier 2 with reviews already available | Needs tier 3-4 assurance |
| Owner | A business owner is ready and keen | Ownership is disputed |
| Knowledge | Sources are owned and ready | Content needs clean-up first |
| Visibility | Many people will notice the result | Benefits a single person |
| Measure | Baseline exists or can be captured now | No measurable outcome |
| Effort | Fits within the Deliver phase on available capacity | Needs a partner or platform not yet in place |

At each phase boundary the sponsor makes a go or hold decision. Hold is the right answer when exit criteria are not met;
a short hold costs less than starting Deliver without a backlog or knowledge register.

## Practitioner approach

Start with the open readiness conditions. Each becomes an Establish or Foundation milestone with an owner and date. If a
"before launch" condition is still open, the first milestone is closing it, and nothing is announced until it is.

Lay out the workstreams that run across the phases: sponsorship and governance, team and ways of working, opportunity
pipeline, knowledge, delivery, adoption and Champions, and value. For each, write the milestones per phase and who owns
them. Keep milestones as outcomes ("backlog live with first ten ideas framed"), not activities ("hold workshop").

Plan the first ninety days in detail and the rest in outline. Week by week for Establish, fortnight by fortnight for
Foundation, and monthly beyond that. Detailed plans for month six are fiction at this stage; outline them and replan at
each phase boundary.

Choose quick wins during Foundation, not before. Pull candidates from the backlog and from existing agents or
automations that only need an owner and a little work. Apply the tests in the decision framework and pick two or three.
More than that spreads a new team too thin. Capture each quick win's baseline before it starts, or its result will be an
anecdote.

Sequence the announcement. Launch communications go out at the end of Foundation, when the front door works, triage is
running and someone will respond to every idea. Coordinate with `change-and-communications:ai-communication-strategy`, and
make the sponsor the voice of the announcement.

Map dependencies explicitly: approved-use guidance from the governance owner, environment readiness from IT, partner
availability, Copilot rollout waves and budget decisions. Each dependency has an owner outside the CoE and a date it is
needed by. Where a dependency slips, adjust the plan rather than hoping.

Hold a go or hold decision at each phase boundary in steering, using the exit criteria. Record the decision and any
conditions. When a hold happens, write what must change and the new review date.

Write it all on the `coe-launch-plan` template and reflect the phase dates in the launch section of the `coe-charter`
template. Review the plan at every steering meeting during launch; after Scale begins, the plan gives way to the CoE's
normal cadence, roadmap and maturity reviews.

## Outputs

- A CoE launch plan on the `coe-launch-plan` template: readiness conditions, phases, workstreams, milestones with owners, exit criteria, quick wins, first ninety days, dependencies, communications moments and phase decisions.
- A quick-win selection record with the tests applied and baselines captured.
- A phase decision log of go or hold decisions with conditions.
- Updated launch dates in the launch roadmap section of the `coe-charter` template.

## Microsoft platform considerations

Platform dependencies often set the pace of Deliver: environments for makers, admin inventory, Copilot licence
assignment and approved connectors. Confirm each with IT in Establish and check current availability and capability in
`references/sources.md`. Route licensing questions to the Microsoft licensing guide or a licensing partner.

## Adoption considerations

Do not announce before the CoE can respond. When it does launch, show a real quick win, a clear way to submit ideas and
the people to talk to, and invite existing builders and Champions in first so they become early advocates.

## Knowledge considerations

Make the knowledge register a Foundation exit criterion, because quick wins nearly always depend on content. A quick win
that fails on stale knowledge damages trust in the CoE at the moment it most needs credibility.

## Security and privacy considerations

Confirm in Establish that information security and the data protection officer can review tier 2 quick wins inside the
Deliver phase. If they cannot, choose quick wins at tiers 0 and 1 rather than skipping reviews.

## Responsible AI considerations

Exclude ideas that inform decisions about people, money, safety or rights from the quick-win list. They may still enter
the backlog, but they need the full route, not a launch deadline.

## Evaluation requirements

Each tier 2 quick win needs a test set and threshold before release, through `m365-agents:agent-testing`. Build the time
for testing into the Deliver milestones rather than squeezing it at the end.

## Value measures

Measure the launch by outcomes: phase exit criteria met on the planned date, time from launch to the first measured
value, quick wins live with owners and baselines, and ideas received after the announcement. The CoE lead owns these and
reports them at steering.

## Scale notes

### Starter

A one-page plan for an AI working group: two phases (set up, then deliver), one or two quick wins, and a monthly check
with the sponsor.

### Scale

The full four-phase plan with workstreams, a detailed first ninety days, two or three quick wins and phase decisions in
steering.

### Enterprise

The hub launches first and proves the model; spokes then launch on a repeatable version of the plan, each with its own
readiness check, while the hub provides shared standards, patterns and specialists.

## Hand-offs

- To `ai-centre-of-excellence:coe-cadence` to run the forums the plan schedules.
- To `ai-centre-of-excellence:coe-opportunity-pipeline` to run intake once Foundation is complete.
- To `ai-centre-of-excellence:coe-value-tracking` for the first value review.
- To `ai-centre-of-excellence:coe-maturity-assessment` once the Scale phase has run for a few months.

## Reviewer gates

Not applicable to the launch plan itself, which schedules work rather than releasing a solution. Quick wins at tier 2
pass `security-privacy` and the other gates their tier requires, and the plan must leave time for them.

## Failure modes

- The CoE is announced in Establish and spends Foundation apologising for slow responses.
- Builds start before the backlog and knowledge register exist, and quick wins stall on content.
- Too many quick wins are chosen and none finishes within the Deliver phase.
- Phase dates are treated as commitments, so exit criteria are waived to meet them.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Announce the CoE before the front door and triage can respond.
- Start Deliver without a live backlog and a started knowledge register.
- Choose a quick win that skips a review its tier requires.
- Commit phase dates that depend on capacity nobody has agreed.

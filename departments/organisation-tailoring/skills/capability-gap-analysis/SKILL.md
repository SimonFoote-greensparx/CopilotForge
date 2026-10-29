---
name: capability-gap-analysis
description: Compares what the recommended AI programme demands - capabilities and time by role and quarter - with what the organisation has declared, classifies each shortfall as capability, capacity or vacancy, and chooses how to close it (develop, recruit, partner, borrow, re-sequence or defer) with the effect on the programme. Use when a pack or roadmap looks unstaffable, when capacity is the stated constraint, or before committing to delivery dates.
license: CC-BY-4.0
metadata:
  department: organisation-tailoring
  lifecycle: Envision, Mobilise, Scale
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-champion-best-practice, ms-copilot-studio-guidance, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Capability gap analysis

## Purpose

A tailored AI programme is only realistic if the organisation can staff it. This skill compares what the recommended
programme demands, in capabilities and in time by role over the coming quarters, with what the organisation has declared,
and turns the difference into a short list of gaps with a chosen way to close each one and its effect on the programme.
It works at role level from declared information, never from judgements about individuals. Gap analyses go wrong when
they count makers and forget the business, knowledge and reviewer roles that actually constrain AI delivery, when every
gap is answered with training, and when the analysis quietly becomes an assessment of people.

## When to use

- A transformation pack or roadmap has been produced and the sponsor asks whether it can be staffed.
- Capacity or skills was named as the main constraint during intake.
- Delivery dates are about to be committed and nobody has checked the scarce roles.
- The programme is scaling (more units, more agents, higher risk tiers) and its demand will change.
- A decision is needed on whether to develop, recruit or use a partner for part of the programme.

## When not to use

- Assigning accountable roles and recording vacancies against each department and artefact - use `organisation-tailoring:ownership-map`.
- Analysing the AI skills each role needs and designing learning for them - use `learning-and-skills:ai-skills-needs-analysis`.
- Selecting and managing a partner once sourcing is decided - use `programme-management:supplier-management`.
- Tracking programme budget and month-by-month capacity during delivery - use `programme-management:budget-and-capacity`.
- An evidenced maturity assessment across all capability dimensions - use `ai-strategy:ai-maturity-assessment`.

## Questions to ask first

1. Which programme, edition and depth has the sponsor confirmed, and over what period?
2. Which roles has the organisation declared, how much time can each give, and which are vacant or part-time?
3. What delivery capability exists internally (makers, developers, reviewers, adoption and change people), and what partners are already engaged?
4. Which constraint is firm (budget, headcount, timeline), and which could move if the case were made?
5. Which risk tiers and solution types will the programme deliver, since they drive reviewer and specialist demand?

## Required inputs

- The pack index or tailoring plan from `organisation-tailoring:transformation-pack`, with artefacts, programmes and depth.
- The ownership map from `organisation-tailoring:ownership-map`, with declared owners and time.
- Role definitions from `organisation-tailoring:ai-role-catalogue`, including separation rules.
- The roadmap or integrated plan, so demand can be placed by quarter.
- The profile's delivery capability and constraints from `organisation-tailoring:ai-profile-intake`.

Where declared time is unknown, record `[To confirm: ...]` with the role who can confirm it and treat it as zero in the
analysis until confirmed. Never estimate a person's availability, skills or performance on their behalf.

## Decision framework

Estimate demand per catalogue role per quarter, compare it with declared supply, and classify each shortfall.

| Gap type | Meaning | Usual close options |
|---|---|---|
| Capability | The role is filled but lacks a capability the programme needs | Develop, pair with a partner, borrow a specialist |
| Capacity | The role is filled and capable but lacks time | Re-sequence, release time from other work, partner, defer |
| Vacancy | No declared role holds it | Recruit, assign by combining roles within separation rules, partner, defer |

Choose a close option per gap.

| Option | Choose when | Watch for |
|---|---|---|
| Develop | Time allows and the capability must be owned long term | Training alone without practice or evidence |
| Recruit | The need is enduring and significant | Lead times longer than the plan allows |
| Partner | Speed matters or the need is specialist or temporary | Dependence without transfer |
| Borrow | Another function has the capability (security, data protection, records) | Their own capacity |
| Re-sequence | Demand peaks can move without harming outcomes | Pushing everything to the same later quarter |
| Defer or descope | No other option fits the risk and constraint | Shadow AI filling the gap |

Gaps in independent reviewer roles for tier 2 and above, and in the accountable executive for tier 3 and 4, cannot be
closed by combining them with builder roles. If they cannot be closed, the solutions that need them are deferred.

## Practitioner approach

Work out demand from the programme, not from a generic staffing model. Take the artefacts and initiatives in the pack and
roadmap, and for each one ask which catalogue roles it needs and roughly how much of their time in which quarter. Rough is
fine; ranges are better than false precision. Include the roles that are easy to forget: business owners who must make
decisions, knowledge owners who must clean and review content, reviewers who must assess each tier 2 release, and the
adoption lead who must keep the launch going after go-live.

Lay demand beside declared supply by role and quarter. The gaps usually show a familiar pattern: makers are not the
constraint, but knowledge owners, reviewers and business owners are, and demand peaks in the quarter when launches,
releases and Champion learning coincide. Point this out plainly; it changes the conversation from "we need more
developers" to "we need decisions and content from the business".

Classify each gap as capability, capacity or vacancy, and describe it as a role gap: "no role has time to own HR policy
content for the agent", not "the HR adviser is too busy". Then choose a close option with the sponsor. Develop where the
capability must be owned for the long term, partner where speed matters with transfer written in, borrow from other
functions where they hold the capability, and re-sequence or defer where nothing else fits. Training is only one answer,
and it closes capability gaps, never capacity gaps.

Show the effect on the programme for each option: dates that move, scope that narrows, costs that rise, risks that
appear. A gap with no affordable close option should change the plan, not be carried as a hope. Where reviewer or
accountable executive gaps cannot be closed, say which solutions must wait.

Keep the analysis at role level from declared information. Do not ask managers to rate individuals, do not use usage or
performance data, and do not let the analysis be used to decide who keeps a job. If the sponsor wants to know who should
take a role, return the capability the role needs and leave the appointment to them.

Repeat the analysis at each programme stage gate and when the programme scales, because demand changes with the solution
mix and risk tiers.

## Outputs

- A demand and supply table by catalogue role and quarter, with declared time and estimated demand as ranges.
- A gap register: role, gap type, quarter, effect if not closed, close option chosen, owner of the decision, and effect on the programme.
- Recommended changes to the roadmap, sequence or scope where gaps cannot be closed, and the gap summary carried into the `ownership-map` template.

## Microsoft platform considerations

Specialist capability (Copilot Studio architecture, Foundry engineering, platform administration, security tooling) is
often the gap partners fill. Do not infer from the Microsoft estate that a capability exists; ask. Platform facts used to
estimate demand come from `references/sources.md`.

## Adoption considerations

Adoption and change roles are frequently under-counted. Include the time line managers and Champions need, and make sure
the adoption programme does not depend on Champions doing work that belongs to a funded role.

## Knowledge considerations

Knowledge owner time is the gap most likely to delay agents. Estimate content clean-up and review effort for each agent's
sources and place it before the agent's release in the demand table.

## Security and privacy considerations

The analysis records role-level information only. If aliases for role holders appear, store it in the organisation's own
location with restricted access. Reviewer capacity gaps for `security-privacy` are treated as release blockers, not as
efficiency problems.

## Responsible AI considerations

Never use the analysis to assess, rank or profile individuals, or to inform employment decisions. Where tier 3 and 4 uses
are planned, a missing accountable executive or responsible AI reviewer is a gap that defers those uses.

## Evaluation requirements

Not applicable, because the analysis is an organisational artefact rather than an AI solution; evaluation effort for each
solution is counted as demand on the roles that build and review it.

## Value measures

Track the share of gaps with an agreed close option, gaps closed by their target quarter, and forecast versus actual
demand on scarce roles, reported by the Transformation Architect at role and programme level. Never measure individuals.

## Scale notes

### Starter

A one-page table of six to ten roles over two quarters, usually showing that one or two people and a partner carry most
of the work, with a short list of decisions for the sponsor.

### Scale

A full demand and supply table across role families and four quarters, with close options agreed and reflected in the
roadmap and supplier plans.

### Enterprise

Analyses per business unit rolled up to the hub, with shared reviewer and specialist capacity planned across units and
recruitment lead times built into the roadmap.

## Hand-offs

- To `organisation-tailoring:ownership-map` to record vacancies and appointments.
- To `programme-management:supplier-management` where the close option is a partner.
- To `learning-and-skills:ai-skills-needs-analysis` where the close option is developing capability.
- To `ai-strategy:ai-roadmap` or `programme-management:integrated-roadmap` where re-sequencing or deferral changes the plan.

## Reviewer gates

Not applicable, because the analysis releases no solution; gaps in independent reviewer capacity for `security-privacy`,
`responsible-ai`, `evaluation-quality` and `design-authority` are reported as constraints on which solutions can proceed.

## Failure modes

- Demand counts makers and developers but not business owners, knowledge owners and reviewers.
- Every gap is answered with training, including gaps that are really about time.
- Gaps are carried as hopes rather than changing the plan, and the roadmap slips quarter after quarter.
- The analysis drifts into rating individuals and the organisation stops declaring honest information.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Rate, rank or compare individuals, or use the analysis to inform employment decisions.
- Assume time or skills a role holder has not declared.
- Close a reviewer or accountable executive gap by combining it with a builder role.
- Treat training as the answer to a capacity gap.

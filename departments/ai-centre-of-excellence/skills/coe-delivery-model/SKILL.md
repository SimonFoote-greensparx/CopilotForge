---
name: coe-delivery-model
description: Defines how the CoE actually builds and releases agents and automations once work is approved - delivery routes from self-service makers to CoE-assisted, CoE-built, partner and pro-code teams, a definition of ready and of done by risk tier, maker support, reusable patterns and handover to operations. Use when approved work has no clear way to get built, when makers and partners work differently, or when solutions go live unsupported.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Mobilise, Deliver, Assure, Launch, Scale
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: m365-agents, copilot-cowork, copilot-code, copilot-studio, ai-foundry, power-platform
  edition-support: scale, enterprise
  reviewers: design-authority, evaluation-quality, security-privacy
  sources: ms-copilot-studio-guidance, ms-copilot-studio-zoned-governance, ms-managed-environments, ms-agents-compare, ms-agent-builder, ms-foundry-models
  status: draft
  authors: Simon Foote
---

# CoE delivery model

## Purpose

The operating model decides which route an idea takes; the delivery model decides how the build itself happens on each
route. This skill sets out who builds, with what support, to which standard of ready and done, and how a solution is
handed to the people who will run it. Delivery goes wrong when every build is a one-off negotiation, when makers are
left alone with tier 2 work, when partners hand over solutions nobody internal understands, and when "done" means
"published" rather than "owned, tested and supported".

## When to use

- The CoE has approved work in its backlog but no consistent way to get it built and released.
- Business makers, the CoE and partners build in different ways and to different standards.
- Solutions go live without test evidence, support arrangements or a review date.
- The CoE wants to move from building everything itself to enabling makers safely.

## When not to use

- Choosing the CoE's shape and routing ideas by suitability and tier - use `ai-centre-of-excellence:coe-operating-model`.
- Selecting the platform for one specific solution - use `ai-architecture:platform-selection`.
- Designing one agent's scope, knowledge and actions - use `m365-agents:agent-use-case-design`.
- Application lifecycle management for Copilot Studio agents in depth - use `copilot-studio:studio-alm`.
- Selecting and managing delivery partners contractually - use `programme-management:supplier-management`.
- The support model for live solutions - use `ai-operations:ai-support-model`.

## Questions to ask first

1. Which delivery routes exist today: business makers, a CoE build capability, an IT or digital team, partners, pro-code engineers?
2. What does each route build on, and which environments and tools does the governance model allow for each tier?
3. What support can the CoE give makers: office hours, review, pairing, templates?
4. Who will support solutions after release, and do they accept them today?
5. How many builds per quarter does the CoE need to deliver, and what capacity sits on each route?

## Required inputs

- The routing table from `ai-centre-of-excellence:coe-operating-model`.
- Risk tiers and minimum controls from `ai-centre-of-excellence:coe-governance-model`.
- The environment strategy, where it exists, from `platform-governance:ai-environment-strategy`.
- Declared maker skills and partner arrangements, recorded at role level.
- The support model owner, from `ai-operations:ai-support-model` or IT service management.

If no environment strategy exists, restrict tier 2 and above builds to a single managed route until it does, and mark the
gap "to confirm".

## Decision framework

Match the route to tier and complexity.

| Route | Who builds | Suits | CoE role |
|---|---|---|---|
| Self-service maker | Business maker in their team | Tier 0-1 assets: prompts, Cowork tasks, team agents, simple flows | Guidance, templates, registration |
| CoE-assisted maker | Business maker with CoE coaching and review | Tier 1-2 agents and automations within standard patterns | Design review, testing support, release gate |
| CoE build | CoE delivery team | Tier 2 solutions that need shared skills or reuse across teams | Builds, tests and hands over |
| Partner build | Partner under CoE standards | Peaks of demand, specialist skills, tier 2-3 | Sets standards, reviews, owns acceptance and knowledge transfer |
| Specialist or pro-code team | Engineering team using Copilot Code, Foundry or Azure | Tier 3-4 or custom solutions | Governs intake, gates and portfolio; does not build |

Definition of ready and done, by tier. Each tier adds to the one below.

| Tier | Ready to build when | Done when |
|---|---|---|
| 0-1 | Owner named, purpose and audience written, tool allowed for the tier | Registered, owner and review date recorded, basic checks by the maker |
| 2 | Agent or solution brief approved, knowledge sources ready, test set drafted, reviews scheduled | Test threshold met, `security-privacy` review passed, support route accepted, users briefed, baseline captured |
| 3-4 | As tier 2, plus design review and impact assessment scheduled | As tier 2, plus evaluation evidence accepted, responsible AI review passed, risk accepted by the accountable executive, monitoring live |

## Practitioner approach

Start by listing the routes that really exist, not the ones the organisation would like. Many CoEs discover that most
building is already happening by business makers in personal or team environments, and that their real job is to make
that route safe and supported rather than to replace it.

For each route, write who builds, on which platforms, in which environments, at which tiers, with what CoE support and
to which standard. Keep the routes few. Five clear routes are easier to follow than a matrix of exceptions.

Write the definition of ready and done next, because these are what make routes consistent. Ready protects the builders
from vague requests; done protects users from unsupported solutions. Agree them with the reviewers and the support
owner before the first build, so nobody discovers a gate at the end. The key rule is that "done" includes an owner, a
support route and a review date, not just a working solution.

Design maker support. A CoE-assisted route works when makers can get help quickly: regular office hours, a design
review at the start rather than the end, a test set template and a release checklist on the `agent-release-checklist`
template. Pair a maker with a CoE builder for their first tier 2 build; after that, review rather than rebuild.

Build reuse in. Keep a small library of patterns: instruction structures, knowledge layouts, flow templates, test sets
and briefing materials that worked. Each new build starts by checking the library and ends by contributing anything
reusable. Feed patterns to `ai-centre-of-excellence:coe-portfolio-management` so they appear in the catalogue.

Set partner terms that protect the organisation. Partners build to the CoE's definition of done, use the organisation's
environments, document what they build, and transfer knowledge to a named internal technical owner before acceptance.
The CoE, not the partner, accepts the solution.

Plan handover to operations explicitly. Before release, the support owner accepts the solution with its documentation,
known limitations, monitoring and escalation route. If nobody accepts it, it is not done.

Iterate in short cycles. Agents are improved by real questions, so plan a release, a short period of observation, then a
first improvement cycle, rather than a long build and a big reveal. Review the delivery model each quarter against cycle
times, rework and reviewer findings, and adjust routes or standards accordingly.

## Outputs

- A delivery model: routes with builders, platforms, environments, tiers, CoE role and capacity.
- A definition of ready and done by tier, agreed with reviewers and the support owner.
- A maker support offer: office hours, design review points, templates, pairing and the `agent-release-checklist` template.
- A pattern library with contribution rules.
- Partner delivery standards and a handover checklist for operations.

## Microsoft platform considerations

Agent Builder, Copilot Studio, Power Automate, Copilot Cowork, Copilot Code and Microsoft Foundry suit different routes
and skill levels. Environment zoning and Managed Environments let the platform enforce which route builds what; ALM and
deployment pipelines support tier 2 and above. Check current capability, availability and licensing in
`references/sources.md`, and route licensing questions to the Microsoft licensing guide or a licensing partner.

## Adoption considerations

A solution that is built but not adopted is not delivered. Include user briefing, scenario examples and Champion support
in the definition of done for tier 2 and above, coordinated with `copilot-adoption:launch-plan` where a wider launch is
needed.

## Knowledge considerations

No build starts at tier 1 or above until its knowledge sources have owners and a readiness outcome from
`ai-centre-of-excellence:coe-knowledge-pillar`. Knowledge owners are part of handover, not an afterthought.

## Security and privacy considerations

Tier 2 and above solutions pass the `security-privacy` review before release, including connectors, authentication and
data exposure. Makers must build in the environments the tier allows, never in personal environments for shared
solutions. Partners use organisation-controlled environments and identities.

## Responsible AI considerations

Solutions that inform decisions about people, money, safety or rights follow the tier 3-4 route whatever their technical
simplicity, with human oversight designed in, not added at release.

## Evaluation requirements

Every tier 2 and above build has a test set and threshold agreed with the business owner before build, using
`m365-agents:agent-testing` or `copilot-studio:studio-testing-and-evaluation`. Evidence is part of done, and regression
testing applies after any change to instructions, knowledge or model.

## Value measures

Measure delivery at route level: median cycle time from ready to done, share of releases meeting the definition of done
first time, reviewer findings per release, reuse of patterns and share of solutions accepted by operations at release.
The delivery lead owns these. Never compare individual makers.

## Scale notes

### Starter

Not usually a separate design. A Starter working group relies on self-service makers for tier 0-1 and a partner or IT
team for anything larger, with a simple definition of done.

### Scale

Three or four routes, a definition of ready and done by tier, maker office hours, a pattern library and partner
standards. The CoE builds selectively and coaches more than it builds.

### Enterprise

Spokes run self-service and assisted routes under hub standards; the hub runs CoE build for shared services, governs
partners across units and connects to specialist engineering teams for tier 3-4.

## Hand-offs

- To `m365-agents:agent-use-case-design` or `copilot-studio:studio-agent-design` for the design of each build.
- To `m365-agents:agent-release-readiness` for the release gate.
- To `ai-operations:ai-support-model` for support acceptance.
- To `ai-centre-of-excellence:coe-portfolio-management` when the solution goes live.

## Reviewer gates

From tier 2, `security-privacy` and `evaluation-quality:ai-release-evidence` review every release on the CoE-assisted,
CoE and partner routes. `design-authority:platform-fit-review` should challenge the route table for complex work sent to
routes that cannot support it, and `design-authority:ai-design-review` reviews tier 3-4 designs before build.

## Failure modes

- Makers are left alone with tier 2 work and release without tests or reviews.
- Partners hand over solutions with no internal technical owner and no documentation.
- "Done" means published, and support discovers new solutions from user complaints.
- The CoE builds everything itself and becomes the bottleneck the operating model was meant to avoid.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Release a tier 2 or above solution without an owner, test evidence, completed reviews and an accepted support route.
- Let partners accept their own work on the organisation's behalf.
- Allow shared solutions to be built or run from personal environments.
- Assert platform capability, availability or licensing from memory.

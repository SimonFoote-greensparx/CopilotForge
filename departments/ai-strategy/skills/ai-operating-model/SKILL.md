---
name: ai-operating-model
description: Designs the target operating model for AI - who decides, who builds, who supports and who owns value - choosing a central, hub-and-spoke or federated shape to suit the edition and archetype, and placing the Centre of Excellence within it. Use when AI work is spreading without clear ownership, when leaders ask how AI should be organised, or before a CoE is chartered.
license: CC-BY-4.0
metadata:
  department: ai-strategy
  lifecycle: Mobilise, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-coe-starter-kit, ms-copilot-studio-zoned-governance, ms-copilot-adoption-hub, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# AI operating model

## Purpose

This skill sets out how the organisation will run AI as an ongoing capability: where decisions are made, who builds
what, who supports it once live, and who is accountable for the value. It chooses a shape (central, hub-and-spoke or
federated) that fits the organisation's size and maturity and positions the Centre of Excellence as an enabler inside
that model rather than as the whole of it. Operating models usually go wrong by copying an enterprise structure into a
small organisation, by making IT the owner of business outcomes, or by leaving support and ownership after launch
undefined.

## When to use

- Agents, prompts and automations are appearing across teams and nobody can say who owns or supports them.
- Leaders ask whether AI should be run centrally, by each business unit, or both.
- A CoE is about to be chartered and needs a defined place in the wider model.
- The organisation is moving between editions or archetypes, for example from a working group to a federated model.

## When not to use

- Writing the CoE's own charter, mandate and membership - use `ai-centre-of-excellence:coe-charter`.
- Detailing how the CoE runs internally, its services and intake - use `ai-centre-of-excellence:coe-operating-model`.
- Assigning responsibility for individual CoE activities - use `ai-centre-of-excellence:coe-raci`.
- Recording named owners for specific assets and knowledge domains - use `organisation-tailoring:ownership-map`.
- Designing platform environments, data policies and zones - use `platform-governance:ai-environment-strategy`.

## Questions to ask first

1. What are the agreed strategic outcomes, and which business executives own them?
2. How many business units, and how different are their processes, regulators and risk appetites?
3. Where does AI work happen today: a central team, scattered makers, a partner, or all three?
4. Who supports AI solutions once they are live, and what happens when an owner leaves?
5. What edition and archetype apply, and where does the organisation expect to be in two years?

## Required inputs

- Strategic outcomes and principles from `ai-strategy:strategic-outcomes`.
- The maturity assessment and the edition and archetype recommendation.
- A current-state view of who decides, builds and supports AI today, including partners and unofficial makers.
- The existing IT service model and governance forums, so AI joins them rather than duplicating them.

If the current-state view is incomplete, design for what is known, mark unknown areas "to confirm" and schedule a
review once the solution inventory exists. Never assume a team or role exists because the model needs it.

## Decision framework

Choose the shape by edition and archetype, then adjust for regulatory pressure and variation between units.

| Shape | Fits | Decides | Builds | Supports | Watch for |
|---|---|---|---|---|---|
| Central | Starter, or explorer and adopter at any size | A small AI working group with the sponsor | Central team or partner, plus approved individual use | Existing IT service desk with a named AI owner | The central team becoming a bottleneck and request queue |
| Hub-and-spoke | Scale, builder and scaler | Hub sets standards and gates; spokes prioritise their own backlogs | Hub builds shared and higher-tier solutions; spokes build tier 0-1 within guardrails | Hub supports shared platform; spokes own their solutions | Spokes without capacity, hub without authority |
| Federated | Enterprise, scaler and ai-enterprise | Enterprise board sets policy and risk appetite; units decide within it | Units build up to an agreed tier; hub runs common engineering and assurance | Units own run and value; central operations for shared services | Inconsistent assurance and duplicated solutions |

Whatever the shape, four ownership rules hold: the business owns outcomes, priorities, knowledge, adoption and
benefits; IT and AI teams enable; reviewer gates are run once and reused across units; and every live solution has a
named owner and a support route.

## Practitioner approach

Begin with the four questions every operating model must answer for each risk tier: who decides whether this goes
ahead, who builds it, who supports it once live, and who owns the value. Map today's answers honestly, including the
uncomfortable ones such as "a contractor built it and left" or "nobody; it just runs". The gaps in that map are the
design brief for the target model.

Choose the shape from the decision framework, then test it against two or three real scenarios: a team wanting a
shared prompt library, a department wanting an agent over its policy documents, and a customer-facing use case. Walk
each through the model and see where it stalls. If the customer-facing case has nowhere to go for responsible AI
review, or the prompt library needs board approval, the model is wrong for its tiers.

Place the CoE as the enabling hub, not the owner of AI. Its job is to run intake, standards, reusable patterns,
community and the reviewer gates once, so units can repeat them. Be explicit that the CoE is not an IT project, a
monthly reporting group, a technology experiment or a request queue. Hand the detailed CoE design to the
`ai-centre-of-excellence` skills.

Define the roles the model needs by responsibility rather than job title: AI sponsor, business owner for each outcome,
knowledge owners, solution owners, makers, Champions, platform administrators, reviewers and the support route. Note
where one person can hold several roles in a smaller organisation, and where separation is required, for example a
maker should not approve their own tier 2 release. Check the role set against the platform governance guidance and the
AI management system standard in the source records so nothing structural is missing.

Decide the support model explicitly. AI solutions need first-line help (often Champions and the service desk),
second-line fixes from the solution owner or maker, and third-line platform or partner support. Agree how ownership
transfers when an owner moves on, and what happens to an orphaned solution.

Finally, describe how the model will evolve. A starter working group should know what would trigger a move to
hub-and-spoke, such as a second business unit building agents or the first tier 2 solution. Record those triggers so
the model is reviewed when they occur rather than when it has already broken.

## Outputs

- A target operating model on the `ai-operating-model` template: chosen shape with rationale, decision rights by risk tier, build and support responsibilities, role catalogue, CoE positioning and evolution triggers.
- A current-to-target gap list with owners for each change.
- Scenario walk-throughs showing how three representative requests move through the model.

## Microsoft platform considerations

The operating model shapes platform governance: who can create agents or environments, which zones exist for personal,
team and organisational solutions, and who administers them. Microsoft publishes guidance on zoned governance and a
CoE starter kit for Power Platform; use the source records to check what controls exist today rather than assuming
them, and leave the configuration to `platform-governance:ai-environment-strategy`.

## Adoption considerations

People need to know where to take an idea, a question or a problem. Publish the model as a simple "who to go to"
guide alongside the formal version. Champions are part of first-line guidance and opportunity spotting, but they never
replace technical support, architects or approval routes.

## Knowledge considerations

Name knowledge ownership as a business role in the model, with time recognised for review cycles. A model that gives
solution owners accountability but leaves the knowledge their agents rely on unowned will fail within months.

## Security and privacy considerations

Decision rights must place security and privacy review where the risk tiers require it, and must stop makers from
widening access to sensitive content without review. Confirm that the security lead and data protection officer agree
their place in the model.

## Responsible AI considerations

Assign accountability for responsible AI decisions explicitly, including who can accept residual risk for tier 3 and
tier 4 uses. In federated models, units may not lower the enterprise's responsible AI floor.

## Evaluation requirements

Not applicable to solution evaluation. The model is validated by the scenario walk-throughs; each must reach a decision,
a builder, a support route and a value owner without ambiguity.

## Value measures

The business owner of each outcome owns its value; the CoE owns the measures of its own service, such as time from
intake to decision and reuse of patterns. Track operating model health through solution ownership coverage (share of
live solutions with a current named owner) and the age of the intake backlog, reported by unit.

## Scale notes

### Starter

Central shape: an AI working group of three to five people, the sponsor attending quarterly, a partner for anything
beyond tier 1, and the existing service desk as the support route. Write it on two pages.

### Scale

Hub-and-spoke: a small core CoE team with business representatives, spokes in the largest functions, monthly steering
and a solution register. Reviewer gates from tier 2 are run by the hub.

### Enterprise

Federated: an executive board sets policy and risk appetite, business-unit spokes own their portfolios, and a hub runs
common engineering, assurance and operations. Decision rights by tier are formal and auditable.

## Hand-offs

- To `ai-centre-of-excellence:coe-charter` and `ai-centre-of-excellence:coe-operating-model` to design the CoE within this model.
- To `ai-centre-of-excellence:coe-raci` for activity-level responsibilities.
- To `organisation-tailoring:ownership-map` to name owners against the roles defined here.
- To `ai-strategy:ai-roadmap` to schedule the operating model changes.

## Reviewer gates

Advisory only. `design-authority:supportability-review` may challenge the model where decision rights or support routes
would leave tier 2 and above solutions without architecture or assurance oversight. The CoE lead records the challenge
and the sponsor decides.

## Failure modes

- An enterprise-style federated model is imposed on a small organisation, and the overhead kills momentum.
- IT is made accountable for business outcomes, so priorities follow technology rather than value.
- Nobody owns live solutions after launch, and agents decay or are switched off without notice.
- The CoE becomes a request queue, and teams route around it with ungoverned tools.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Make IT or the CoE the owner of business outcomes or benefits.
- Allow a maker to approve their own release at tier 2 or above.
- Design roles around named individuals rather than responsibilities.
- Present Champions as a substitute for support, architecture or approval.

---
name: coe-operating-model
description: Designs how an AI Centre of Excellence actually runs - the core team and business roles, a central, hub-and-spoke or federated shape chosen by edition, and the flow from intake through the opportunity lifecycle to the right delivery route, linked to the Champion community. Use when a charter is agreed and the CoE now needs people, routes and a workable flow, or when an existing CoE has become a bottleneck.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Mobilise, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-copilot-studio-guidance, ms-coe-starter-kit, ms-copilot-adoption-hub, ms-champion-programme, ms-copilot-studio-zoned-governance
  status: draft
  authors: Simon Foote
---

# CoE operating model

## Purpose

The charter says what the CoE is for; the operating model says how work moves through it and who does what. This skill
designs the CoE team, chooses a central, hub-and-spoke or federated shape that fits the organisation's size, and maps
the route an idea takes from intake through the opportunity lifecycle to the right delivery route. Operating models fail
when the CoE tries to build everything centrally and becomes a queue, or when it federates before there are shared
standards to federate.

## When to use

- A CoE charter is agreed and the team, roles and flow now need designing.
- Departments are building agents or automations independently and need one route that does not slow everyone down.
- An existing CoE has become a bottleneck, or business units are bypassing it.
- The organisation is growing from one business unit to several and the CoE shape must change.

## When not to use

- Agreeing the CoE's purpose, principles and decision rights - use `ai-centre-of-excellence:coe-charter`.
- The organisation-wide AI target operating model, across strategy, adoption, delivery and operations - use `ai-strategy:ai-operating-model`.
- Allocating responsibility and accountability per activity - use `ai-centre-of-excellence:coe-raci`.
- Designing the Champion community itself - use `champions:champion-programme-design`.
- Defining the scoring used to rank opportunities - use `opportunity-management:opportunity-prioritisation`.
- Designing a specific agent - use `m365-agents:agent-use-case-design`.

## Questions to ask first

1. How many business units run their own priorities, and do they have people who could act as spoke leads?
2. Where are ideas arriving today (email to IT, Teams chats, Champions, makers building directly), and how many per month?
3. Which delivery routes exist now: individual Copilot use, published prompts, agents built by makers, partner builds, automation, pro-code?
4. How much CoE capacity is real, in roles and days per week, not aspirations?
5. Which existing teams (IT service desk, architecture, information security, change) must the flow connect to?

## Required inputs

- The signed charter from `ai-centre-of-excellence:coe-charter`, including decision rights.
- The edition, archetype and emerging signals from `organisation-tailoring:edition-and-archetype`.
- The organisation-wide operating model on the `ai-operating-model` template, if `ai-strategy:ai-operating-model` has produced it, so the CoE design fits inside it.
- The current inventory of agents, automations and pilots, even if partial.

Where the inventory is missing, design the flow anyway and make "find what already exists" the first action of the
first month. Mark capacity figures `[To confirm]` rather than assuming them.

## Decision framework

Choose the shape from the edition and number of business units, then check it against the readiness tests.

| Shape | Typical edition | Choose when | Not yet if |
|---|---|---|---|
| Central working group | Starter | One business unit, few ideas, little internal build capability | Ideas are arriving faster than the group can triage monthly |
| Core team with business representatives (central hub) | Scale | Several departments, steady flow of ideas, some makers | No business representative can give regular time |
| Hub and spoke | Scale to Enterprise | Two or more business units with their own priorities and a spoke lead each | Shared intake criteria and risk tiers are not yet stable |
| Federated | Enterprise | Spokes run their own intake and tier 0-2 release under hub standards; hub runs tier 3-4 assurance and the portfolio | Spokes lack trained reviewers or a shared register |

Route every idea by the outcome of suitability and risk tier.

| Route | Typical risk tier | Who delivers | CoE involvement |
|---|---|---|---|
| Adoption scenario (individual Copilot use) | 0 | The team, helped by Champions | Publishes the scenario |
| Shared prompt, Cowork task or team agent | 1 | Business maker with named owner | Light registration |
| Organisational agent or automation | 2 | Makers or partner with CoE support | Full intake, reviewer gates |
| Business-critical or external solution | 3-4 | Specialist team or partner | Formal assurance and executive acceptance |

## Practitioner approach

Start from the flow, not the organisation chart. Draw the opportunity lifecycle - Identify, Assess, Prioritise, Build,
Deploy, Measure, Improve - across the page, and for each stage write who does the work today, who should do it, and what
leaves the stage. This exposes the real design questions faster than debating titles.

Design intake first. Give the organisation one front door: a short form or Teams channel that asks for the business
owner, the problem, the expected outcome and who is affected. Champions are the main feeders; they spot opportunities
and route them, but they do not approve or build high-risk solutions and must not become a second queue. Set the rule
from the charter in operational terms: nothing enters delivery without a named business owner, a framed problem, an
expected outcome, an initial risk tier and a recorded reason why AI beats process change, ordinary automation, training
or an existing capability.

Then design triage and routing. Most ideas should leave quickly: to an adoption scenario, to a published prompt, to a
process fix or to a team-owned tier 1 agent with light registration. Only tier 2 and above should pass through full CoE
assurance. A CoE that applies tier 3 controls to everything is the commonest reason makers go around it.

Now size the team. A Scale CoE usually needs a CoE lead, a portfolio and intake role, an adoption and Champions lead, a
platform and governance role working with IT, and business representatives from each major function. Several roles may
be held by one person part-time; record the time honestly. Add specialist roles (evaluation, architecture, responsible
AI) only when the portfolio needs them, and borrow from partners first.

Choose the shape using the decision framework. Hub and spoke is right when business units genuinely run their own
priorities and each can name a spoke lead; until then, a central hub with business representatives is safer. Federation
is earned when shared intake criteria, risk tiers and a single solution register have run for several cycles.

Finally, connect the model to the organisation-wide operating model on the `ai-operating-model` template, so the CoE is
one part of how AI runs rather than a parallel structure. Show interfaces with the service desk for support, with
information security for reviews, and with change and communications for launches. Write down what will trigger a
redesign, such as a new business unit or a doubling of intake.

## Outputs

- A CoE operating model section for the `ai-operating-model` template: shape chosen with rationale, team roles with time commitment, intake-to-delivery flow across the lifecycle, routing table by risk tier, interfaces with existing teams and triggers for redesign.
- Membership and decision rights reflected back into the `coe-charter` template where they changed.
- A first-month action list, including the inventory of existing agents and automations.

## Microsoft platform considerations

Where makers build agents in Copilot Studio or automations in Power Platform, the operating model should map routes to
environment zones (personal productivity, team, organisational) so the platform enforces what the flow describes.
Microsoft's zoned governance guidance and the CoE Starter Kit describe tooling for inventory and nurture; check current
capability in `references/sources.md` before committing to a component.

## Adoption considerations

The model must make the easy path the safe path. Publish the front door, the typical time to a decision and examples of
ideas that went each route. Link Champions explicitly as feeders and peer guides, using `champions:champion-programme-design`.

## Knowledge considerations

Make knowledge ownership part of intake for anything at tier 1 or above: which sources the solution will use and who
owns them. Weak knowledge is a routing outcome in its own right, sending the idea to fix content first.

## Security and privacy considerations

The flow must place the `security-privacy` review before release from tier 2, with time for it built into the plan.
Agents shared beyond their original audience re-enter the flow, because reach changes the tier.

## Responsible AI considerations

Route anything that informs decisions about people, money, safety or rights to tier 3 consideration, whatever its
technical simplicity, and record who holds human accountability for its outputs.

## Evaluation requirements

The model should name where evaluation happens (before release from tier 2, using `m365-agents:agent-testing`) and who
signs the evidence. The `evaluation-quality` department (planned) will own the standard; until then the CoE lead does.

## Value measures

Measure the flow, not just the output: ideas received, time from intake to decision, share routed to adoption or process
fixes, and solutions released with an owner and baseline. Report at team level through
`ai-centre-of-excellence:coe-kpi-framework`, owned by the CoE lead.

## Scale notes

### Starter

A working group triages ideas monthly from one shared list. Most route to adoption scenarios or partner help. No spokes,
no formal portfolio.

### Scale

A small core team with business representatives runs weekly triage and monthly steering, a single register, and
reviewer gates from tier 2. Consider spokes once two business units each have a willing lead.

### Enterprise

Hub and spoke or federated: spokes own intake and tier 0-2 decisions under hub standards; the hub runs tier 3-4
assurance, the portfolio, shared patterns and the register across units.

## Hand-offs

- To `ai-centre-of-excellence:coe-raci` to assign responsibilities across the flow.
- To `ai-centre-of-excellence:coe-cadence` to set the meetings the flow depends on.
- To `opportunity-management:problem-framing` as the first step after intake.
- To `champions:champion-programme-design` for the Champion feeder role.

## Reviewer gates

For organisations with tier 2 and above solutions, `design-authority` (planned) should challenge the routing table for
routes that send complex work to unsupported platforms. Until the department exists, the CoE lead records that
challenge in the steering decision log.

## Failure modes

- The CoE builds everything itself, intake backs up and departments build around it.
- Tier 3 controls are applied to tier 1 ideas, so makers stop registering anything.
- Spokes are created before shared criteria exist, so each unit invents its own governance.
- Champions become an informal request queue and burn out.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Let an idea enter delivery without a named business owner and a framed problem.
- Design a federated model before shared intake criteria, risk tiers and a register exist.
- Make Champions approvers or the owners of high-risk solutions.
- Assume capacity the organisation has not committed.

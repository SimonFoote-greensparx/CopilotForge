---
name: coe-operating-model
description: Designs how an AI Centre of Excellence runs - a business-owned structure with sponsor, lead, core team, four Champion roles and central AI enablement support, its shape by edition, the collaboration space, the intake-to-delivery flow and a phased launch. Use when a charter is agreed and the CoE now needs people, routes and a workable flow, or when an existing CoE has become a bottleneck.
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
6. Which business unit benefits most and will own the CoE, and what can a central AI enablement function offer it?

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
| AI working group | Starter | One business unit, few ideas, little internal build capability | Ideas are arriving faster than the group can triage |
| Business-owned CoE with central enablement support | Scale | Several departments, steady flow of ideas, some makers | No business unit will own it and give a lead real time |
| Hub and spoke | Scale to Enterprise | Two or more business units with their own priorities and a CoE lead each | Shared intake criteria and risk tiers are not yet stable |
| Federated | Enterprise | Spokes run intake and tier 0-2 release under hub standards; hub runs tier 3-4 assurance and the portfolio | Spokes lack trained reviewers or a shared register |

Staff each CoE from the business unit that benefits. Sizes are typical starting points, scaled to the edition.

| Role | Held by | Does |
|---|---|---|
| Executive sponsor | Business executive | Funds, decides priorities, removes blockers, drives adoption |
| CoE lead | Business manager in the owning unit | Runs the backlog, the cadence and the scorecard |
| Core team (often three to five) | Business people with process, knowledge and delivery skills | Assess, build or commission, deploy and measure |
| Champions network | Volunteers with agreed time, in four roles | Knowledge champion keeps content owned and current; process champion spots opportunities and measures benefit; adoption champion promotes use and shares success stories; AI champion supports agent testing and experimentation |
| Central AI enablement | Specialist function serving every CoE | Advises, coaches, governs and provides technical specialists; never owns the CoE |

Route every idea by the outcome of suitability and risk tier.

| Route | Typical risk tier | Who delivers | CoE involvement |
|---|---|---|---|
| Process change or training | Not applicable | The owning team | Records the outcome in the backlog |
| Adoption scenario (individual Copilot use) | 0 | The team, helped by Champions | Publishes the scenario |
| Shared prompt, Cowork task or team agent | 1 | Business maker with named owner | Light registration |
| Organisational agent or automation | 2 | Makers or partner with central enablement support | Full intake, reviewer gates |
| Business-critical or external solution | 3-4 | Specialist team or partner | Formal assurance and executive acceptance |

Launch in phases, moving on only when the exit items are met. Durations are typical, not commitments.

| Phase | Typical timing | Exit items |
|---|---|---|
| Establish | Month 1 | Sponsor confirmed, lead and core team named, collaboration space set up |
| Foundation | Month 2 | Backlog live, knowledge asset register started, first opportunities framed |
| Deliver | Months 3-4 | Quick wins live, first agents or automations deployed, value measured against baseline |
| Scale | Month 5 onwards | Patterns reused by other teams, wider rollout, adoption growing |

## Practitioner approach

Start from the flow, not the organisation chart. Draw the opportunity lifecycle - Identify, Assess, Prioritise, Build,
Deploy, Measure, Improve - across the page, and for each stage write who does the work today, who should do it, and what
leaves the stage. Lay the six pillars (opportunity management, knowledge management, agent development, automation,
adoption and change, governance) against it, so each stage has a pillar that owns its method and the CoE governs once
and repeats everywhere.

Design intake first. Give the organisation one front door that asks for the business owner, the problem, the expected
outcome and who is affected. The rule is simple: no backlog entry, no project. Nothing is resourced unless it sits in
the backlog with an owner, a priority, an estimated value, a return estimate and a status.

Then design triage and routing. Most ideas should leave quickly: to a process fix, training, an adoption scenario, a
published prompt or a team-owned tier 1 agent. Only tier 2 and above should pass through full assurance. A CoE that
applies tier 3 controls to everything is the commonest reason makers go around it.

Now staff it, using the structure table. Ownership sits with the benefiting business unit; the central AI enablement
function supports as advisor, coach, governance and technical specialist. Give each Champion one of the four defined
roles, so nobody is a vague "AI enthusiast", and agree their time with their manager. Champions feed and support; they
do not approve or own high-risk solutions. Record time honestly, and borrow specialist roles from partners first.

Set up the collaboration space before the first meeting, using tools the organisation already runs. A simple structure
works: a general area for announcements with a gallery of live agents and automations; an opportunities area holding
the backlog board; areas for knowledge management (with the knowledge asset register), agent development, automation
and governance; and a success stories area where value is shared. Visible work stops the CoE becoming a private queue.

Choose the shape using the decision framework. Hub and spoke is right when business units run their own priorities and
each can name a CoE lead; federation is earned when shared criteria, tiers and one register have run for several cycles.

Plan the launch in the four phases, and do not start Deliver until the backlog and knowledge register exist. Connect the
model to the organisation-wide operating model on the `ai-operating-model` template, and write down what will trigger a
redesign, such as a new business unit or a doubling of intake. The aim is business capability supported by AI.

## Outputs

- A CoE operating model section for the `ai-operating-model` template: shape chosen with rationale, structure and roles with time commitment, Champion role allocation, intake-to-delivery flow across the lifecycle and pillars, routing table, interfaces with existing teams and triggers for redesign.
- A collaboration space design: areas, the live solution gallery, the backlog board and the knowledge asset register, each with an owner role.
- A phased launch roadmap with exit items, recorded in the launch section of the `coe-charter` template.
- Membership and decision rights reflected back into the `coe-charter` template where they changed.
- A first-month action list for the Establish phase, including the inventory of existing agents and automations.

## Microsoft platform considerations

Where makers build agents in Copilot Studio or automations in Power Platform, the operating model should map routes to
environment zones (personal productivity, team, organisational) so the platform enforces what the flow describes.
Microsoft's zoned governance guidance and the CoE Starter Kit describe tooling for inventory and nurture; check current
capability in `references/sources.md` before committing to a component.

## Adoption considerations

The model must make the easy path the safe path. Publish the front door, the typical time to a decision and examples of
ideas that went each route. Link the four Champion roles to `champions:champion-programme-design`, which owns
recruitment, time agreements and recognition; Champion contribution is recognised there, never used to judge individual
performance. Use the success stories area to show peers real results.

## Knowledge considerations

Make knowledge ownership part of intake for anything at tier 1 or above: which sources the solution will use and who
owns them. Keep a knowledge asset register in layers (policies and standards, procedures, templates and guidance, FAQs
and lessons learned, then the agents and automations built on them), each item with an owner, a review date, version
control and a classification. Weak knowledge is a routing outcome in its own right, sending the idea to fix content
first; `knowledge-management:knowledge-grounding-standards` owns the standard.

## Security and privacy considerations

The flow must place the `security-privacy` review before release from tier 2, with time for it built into the plan.
Agents shared beyond their original audience re-enter the flow, because reach changes the tier.

## Responsible AI considerations

Route anything that informs decisions about people, money, safety or rights to tier 3 consideration, whatever its
technical simplicity, and record who holds human accountability for its outputs.

## Evaluation requirements

The model should name where evaluation happens (before release from tier 2, using `m365-agents:agent-testing`) and who
signs the evidence. `evaluation-quality:ai-evaluation-strategy` owns the standard.

## Value measures

Measure the flow, not just the output: ideas received, time from intake to decision, share routed to adoption or process
fixes, and solutions released with an owner and baseline. Report at team level through
`ai-centre-of-excellence:coe-kpi-framework`, owned by the CoE lead.

## Scale notes

### Starter

An AI working group triages ideas from one shared list in a single shared space. Champion roles may be combined in one
or two people. Most ideas route to adoption scenarios, process fixes or partner help. No spokes, no formal portfolio.

### Scale

A small core team with business representatives runs weekly triage and monthly steering, a single register, and
reviewer gates from tier 2. Consider spokes once two business units each have a willing lead.

### Enterprise

Hub and spoke or federated: each business unit runs its own CoE, owning intake and tier 0-2 decisions under hub
standards; the hub runs tier 3-4 assurance, the portfolio, shared patterns and one register across units, and the
central AI enablement function serves every spoke.

## Hand-offs

- To `ai-centre-of-excellence:coe-raci` to assign responsibilities across the flow.
- To `ai-centre-of-excellence:coe-cadence` to set the meetings the flow depends on.
- To `opportunity-management:problem-framing` as the first step after intake.
- To `champions:champion-programme-design` for recruiting and supporting the four Champion roles.
- To `opportunity-management:opportunity-prioritisation` to run the backlog the flow feeds.

## Reviewer gates

For organisations with tier 2 and above solutions, `design-authority:platform-fit-review` should challenge the routing
table for routes that send complex work to unsupported platforms, and the challenge and response are recorded in the
steering decision log.

## Failure modes

- The CoE builds everything itself, intake backs up and departments build around it.
- Tier 3 controls are applied to tier 1 ideas, so makers stop registering anything.
- Spokes are created before shared criteria exist, so each unit invents its own governance.
- Champions become an informal request queue and burn out, or carry a vague title with no defined role.
- The central AI team is treated as owner, so business units wait for it instead of leading.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Let an idea enter delivery without a named business owner and a framed problem.
- Design a federated model before shared intake criteria, risk tiers and a register exist.
- Make Champions approvers or the owners of high-risk solutions.
- Resource work that has no entry in the backlog.
- Assume capacity the organisation has not committed.

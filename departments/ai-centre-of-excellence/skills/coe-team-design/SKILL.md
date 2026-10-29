---
name: coe-team-design
description: Designs the people side of an AI Centre of Excellence - the lead, pillar leads and core team roles, specialists borrowed from security, data protection, architecture and partners, the skills each role needs, agreed time, sourcing and backfill - and writes the team's terms of reference. Use when the CoE shape is chosen and roles need filling, when the core team is all enthusiasts and no specialists, or when members have no agreed time.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Mobilise, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-studio-guidance, ms-coe-starter-kit, ms-copilot-adoption-hub, ms-champion-programme
  status: draft
  authors: Simon Foote
---

# CoE team design

## Purpose

The operating model sets the CoE's shape and flow; this skill turns it into a team people can actually join. It defines
each core and supporting role, the skills it needs, the time it takes, where the person comes from and who covers their
day job, and records it in terms of reference the team and their managers agree. Team design goes wrong when roles are
filled by whoever volunteered, when time is assumed rather than agreed with managers, and when specialist skills such as
knowledge management, process analysis or security are missing until a solution is stuck at a gate.

## When to use

- The CoE shape and flow are agreed and the roles now need defining and filling.
- The core team has plenty of enthusiasm but no process, knowledge or delivery skills.
- Members were appointed without agreed time, and CoE work is done in evenings or not at all.
- The CoE is growing into pillars or spokes and needs pillar leads and clearer role boundaries.

## When not to use

- Choosing the CoE shape, routes and intake-to-delivery flow - use `ai-centre-of-excellence:coe-operating-model`.
- Allocating responsible and accountable roles for each activity - use `ai-centre-of-excellence:coe-raci`.
- Defining the executive sponsor's role and commitments - use `ai-centre-of-excellence:coe-sponsor-role`.
- Fitting the four Champion roles into the CoE's pillars - use `ai-centre-of-excellence:coe-champion-integration`.
- Maintaining the catalogue of AI transformation roles across the whole programme - use `organisation-tailoring:ai-role-catalogue`.
- Analysing AI skills needs across the workforce - use `learning-and-skills:ai-skills-needs-analysis`.

## Questions to ask first

1. Which pillars are active at launch, and which are deferred, according to the charter?
2. How many ideas and solutions does the CoE expect to handle in its first six months, roughly?
3. Which skills already exist in the owning business unit, as declared by the people who hold them?
4. What can the central AI enablement function, information security, data protection, architecture and partners lend, and on what terms?
5. Have managers agreed time for each proposed member, and who covers the work they stop doing?

## Required inputs

- The charter, with active pillars and decision rights, from `ai-centre-of-excellence:coe-charter`.
- The shape and routing table from `ai-centre-of-excellence:coe-operating-model`.
- Declared skills and availability of candidate members, provided by them and agreed with managers.
- The edition from `organisation-tailoring:edition-and-archetype`.

Where declared skills are missing, design roles first and mark the skills coverage "to confirm". Never infer skills
from job titles, and never assess candidates against each other.

## Decision framework

Design roles from the work, then size them. These are typical roles; combine them in smaller organisations.

| Role | Purpose | Core skills | Typical source |
|---|---|---|---|
| CoE lead | Runs the backlog, cadence, scorecard and team | Facilitation, prioritisation, stakeholder management | Owning business unit |
| Opportunity and process lead | Runs intake, framing and the pipeline | Process analysis, problem framing, benefits thinking | Business unit, often operations or improvement |
| Knowledge lead | Runs the knowledge pillar and register | Information management, content ownership | Business unit or knowledge function |
| Delivery lead (agents and automation) | Runs the delivery model and maker support | Agent and flow building, testing, release practice | Business maker, enablement function or partner |
| Adoption and change lead | Runs adoption, Champions links and stories | Change, communications, learning design | Business unit or change function |
| Governance coordinator | Keeps the register, tiers and gate evidence moving | Risk, controls, record keeping | Business unit or risk function |
| Supporting specialists (borrowed) | Security, data protection, architecture, licensing, evaluation | Specialist review and advice | Central functions or partners, by agreement |

Size the core team from expected demand and agreed time, not headcount alone.

| Edition | Core team | Supporting specialists |
|---|---|---|
| Starter | Lead plus one or two people covering several roles | Partner or central IT on request |
| Scale | Lead plus three to five people, each owning one or two roles | Named contacts with agreed response times |
| Enterprise | Hub team with pillar leads; each spoke has a lead and two or three core members | Dedicated specialists in the hub serving spokes |

A role with no agreed time is a vacancy, not a member. A pillar with no lead is deferred until it has one.

## Practitioner approach

Start from the work each active pillar will do in the first two phases. For each, write the recurring tasks, such as
weekly triage, framing sessions with business owners, maintaining the knowledge register, supporting makers through
release, and preparing the steering pack. Estimate rough days per month for each task. This is the demand the team must
meet, and it usually surprises sponsors.

Group the tasks into roles using the decision framework. Keep role boundaries clear: one person may hold two roles, but
each role has one holder, so nobody is unsure who runs the knowledge register or who prepares steering. Write a short
role profile for each: purpose, recurring tasks, decisions they may take, skills, time and who they work with.

Map declared skills to roles. Ask people to state their own skills and experience; do not assess them. Where a skill
is missing, choose a route: learn it through `learning-and-skills:ai-skills-needs-analysis`, borrow it from a central
function, or bring in a partner for a fixed period with knowledge transfer written into the arrangement. Process
analysis and knowledge management are the gaps most often missed, and both matter more than technical build skills in
the first months.

Agree time with each member's manager, and write down who covers the day job. Without backfill, CoE time is the first
thing dropped when the day job is busy. If the agreed time does not cover the demand, cut scope: defer a pillar, reduce
triage frequency, or route more work to partners. Do not plan on overtime.

Define the supporting specialists explicitly. For security, data protection, architecture, evaluation and licensing
questions, record a named contact role, how to request their help, and the response time they agree. This turns
reviewer gates from surprises into scheduled work.

Write the team's terms of reference on the `coe-terms-of-reference` template: mandate (pointing to the charter),
membership by role with time, role profiles, skills coverage, supporting specialists, ways of working, onboarding of new
members, and when the design is reviewed. Ask the members and their managers to agree it. The forum terms of reference
for steering and triage stay with `ai-centre-of-excellence:coe-cadence`; this document is about the team itself.

Plan for change. Name a deputy for the lead, record how a member hands over when they leave, and review the team design
at each quarterly strategy review against demand and the pipeline measures.

## Outputs

- CoE team terms of reference on the `coe-terms-of-reference` template: mandate, membership by role, time and backfill, role profiles, skills coverage, supporting specialists, ways of working, onboarding and review.
- A demand and capacity sheet: recurring tasks, estimated days per month and agreed time per role.
- A skills coverage map by role from declared skills, with the route chosen for each gap.
- Updates to the structure and membership section of the `coe-charter` template where roles changed.

## Microsoft platform considerations

The delivery lead needs enough hands-on familiarity with the platforms in use, typically Copilot Studio, Agent Builder,
Power Automate and the Microsoft 365 admin tools, to support makers credibly. Platform administration roles usually sit
with IT and should be recorded as supporting specialists, not CoE members. Check current product capability in
`references/sources.md` rather than writing it into role profiles.

## Adoption considerations

Include at least one role whose job is adoption and change, or the CoE will build things nobody uses. Make membership
visible in the collaboration space so the business knows who to ask, and avoid a team made up only of technical
enthusiasts, which signals that AI is an IT matter.

## Knowledge considerations

A knowledge lead or a clearly assigned knowledge role is needed from the Foundation phase, because the knowledge asset
register must exist before Deliver starts. Route the pillar's method to `ai-centre-of-excellence:coe-knowledge-pillar`.

## Security and privacy considerations

Record who the security and data protection contacts are and agree their response times before the first tier 2
solution arrives. CoE members with administrative access to platforms should hold it through IT's normal privileged
access process, not by virtue of CoE membership.

## Responsible AI considerations

Name who the team turns to for responsible AI questions and make sure at least one member understands when a solution
informs decisions about people, money, safety or rights, so those cases are spotted at intake.

## Evaluation requirements

Not applicable to the team design itself, which is an organisational artefact. Record which role prepares evaluation
evidence for releases so that `m365-agents:agent-testing` has an owner.

## Value measures

Measure capacity against demand at team level: agreed days per month versus estimated demand, roles vacant or uncovered,
and specialist requests answered within the agreed time. The CoE lead owns these and reviews them quarterly. Never
measure individual members' output.

## Scale notes

### Starter

Two or three people cover all roles in an AI working group, with a partner or IT contact for specialist questions.
The terms of reference fit on one page.

### Scale

A lead and three to five core members, each with one or two roles and agreed time, plus named specialist contacts.
Pillar leads appear as pillars become active.

### Enterprise

A hub team with pillar leads and dedicated specialists, and a small team in each spoke. Keep role profiles common across
spokes so people can move between them and the hub can support every spoke the same way.

## Hand-offs

- To `ai-centre-of-excellence:coe-raci` to assign activities to the roles designed here.
- To `ai-centre-of-excellence:coe-champion-integration` to connect Champion roles to the team.
- To `learning-and-skills:ai-skills-needs-analysis` for skills gaps the team chooses to learn.
- To `organisation-tailoring:ai-role-catalogue` to align role names across the programme.

## Reviewer gates

Not applicable, because team design is an organisational artefact and releases no AI solution. The sponsor agrees the
terms of reference; `security-privacy` is consulted only on administrative access for CoE roles.

## Failure modes

- Volunteers fill every role and nobody has process, knowledge or change skills.
- Time is agreed with the member but not their manager, so it disappears in the first busy month.
- Specialists are assumed to be available and every tier 2 release waits weeks for a review slot.
- One person quietly holds four roles and the CoE stops when they take leave.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Assess, score or rank candidates or members; use declared skills and agreed availability only.
- Count a role as filled without time agreed by the member's manager.
- Plan CoE work on unpaid overtime or goodwill.
- Give CoE members platform administration rights outside IT's normal access process.

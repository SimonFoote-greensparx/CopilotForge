---
name: ownership-map
description: Produces a role-based ownership map for an AI programme from declared roles only - the accountable role for each engaged department and each pack artefact, named owners only where the organisation has declared them, and roles left without an owner. Use when a transformation pack needs owners, when a sponsor asks who will do this work, or when nobody can say who owns adoption, governance or agents.
license: CC-BY-4.0
metadata:
  department: organisation-tailoring
  lifecycle: Mobilise
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-champion-programme, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Ownership map

## Purpose

A transformation pack is only as good as the people who will own each part of it. This skill maps the departments a
programme engages to the roles accountable for them, assigns an accountable role to each artefact, records a named
owner only where the organisation has declared one, and shows where capability or capacity is missing. It works from
declared roles, never from judgements about individuals. Ownership maps go wrong when they fill gaps with plausible
names, when one willing person is given everything, or when they drift into assessing people.

## When to use

- A transformation pack is being produced and every artefact needs an accountable role.
- A sponsor asks "who will actually do this?" and the answer is unclear.
- Nobody can say who owns adoption, Champions, governance or agents.
- A CoE is forming and its roles need to be reconciled with the departments the programme engages.
- Capacity is the stated constraint and the gaps need to be made visible.

## When not to use

- A full analysis of capability and capacity gaps against the programme - use `organisation-tailoring:capability-gap-analysis`.
- A detailed RACI for each CoE activity - use `ai-centre-of-excellence:coe-raci`.
- Designing the CoE team and its shape - use `ai-centre-of-excellence:coe-operating-model`.
- Assessing Champion capability through evidence - use `champions:evidence-assessment`.
- Producing the whole pack - use `organisation-tailoring:transformation-pack`.
- Ownership of an individual agent before release - use `m365-agents:agent-release-readiness`.

## Questions to ask first

1. Which roles has the organisation declared for this work (sponsor, CoE or working-group lead, adoption lead, platform lead, information security, data protection, business owners)?
2. Which of those roles are filled, which are vacant, and which are being covered by someone part-time?
3. How much time can each declared role give, in days per week or month?
4. Where is the organisation relying on a partner, and for which departments or artefacts?
5. Who is allowed to see this map, and where will it be stored?

## Required inputs

- The tailoring plan or programme list from `organisation-tailoring:transformation-pack` or `organisation-tailoring:edition-and-archetype`, showing which departments and artefacts are engaged.
- `references/departments.json`, which gives each department's lead role, layer, status and whether it is reviewer-class.
- Roles the organisation has declared, from the profile (for example the executive sponsor role) or from the sponsor.
- The profile's delivery capability and constraints (internal capability, makers, developers, partners, capacity).

If a role has not been declared, write the department's lead role from `references/departments.json` with
"named owner: to confirm". Never insert a person's name the organisation has not supplied, and never infer one.

## Decision framework

| Situation | Map entry |
|---|---|
| Role declared and filled | Accountable role plus the declared owner as given (role or alias) |
| Role declared but vacant | Accountable role, "named owner: to confirm", gap recorded with the role who decides the appointment |
| Role not declared | Department lead role from `references/departments.json`, "named owner: to confirm" |
| Department engaged in a later phase | Lead role recorded, with a note on who holds the responsibility in the meantime (usually the CoE lead) |
| Reviewer-class department | A reviewer role independent of the delivery owner; never the same role as the solution owner |
| One role is accountable for more than three departments | Flag a capacity risk, whatever the role's seniority |

Classify each gap as capability (the role exists but lacks a skill the edition needs), capacity (the role exists but lacks
time) or vacancy (no role). Edition sets the expected depth: Starter combines roles freely; Scale expects distinct
adoption, platform and governance roles; Enterprise expects spoke roles per business unit.

## Practitioner approach

Start from what the programme engages, not from the organisation chart. Take the list of artefacts from the tailoring
plan and group them by the department whose skill produces each. Each engaged department becomes a row: department,
accountable role, named owner, time available, gap. Reviewer-class departments that hold gates in the programme join the
list even if they produce no artefact.

Look up each department's lead role in `references/departments.json`. This is a default, not a prescription; most
organisations will map several lead roles onto one person, especially at Starter and Scale. Translate them into the
organisation's own titles with the sponsor, so "AI Portfolio Manager" may become "Head of Operations Excellence" in the
map. Record the original lead role beside it so the link to the skills is not lost.

Fill named owners only from what the organisation has declared. The profile usually declares the executive sponsor as a
role; the sponsor may declare more in conversation. Everything else stays "to confirm", and that is a useful output: a
visible list of appointments the sponsor must make.

Then assign each artefact an accountable role, using the department rows. Keep the principle that the business owns
outcomes: the adoption programme and success measures are accountable to business roles, while the governance framework
and platform controls are accountable to the CoE or IT. Reviewer roles must stay independent of the roles that build.

Now look for gaps. Count how many departments each role is accountable for and compare with the time declared. Use the
profile's capability and capacity fields: low internal capability with few makers means agent delivery depends on a
partner, which belongs in the map; low capacity with a short timeline means the first months must be narrow. Describe
gaps as role gaps, not people gaps: "no role has time for Champions coordination", not "the adoption lead is weak".

Never rank or assess individuals, and do not use adoption data or performance information to decide who owns what. If
the sponsor asks who is "best" for a role, return the capability the role needs and leave the choice to them.

Close with the appointments to make, the order to make them in, and where the map will be stored, which should be the
organisation's own storage with access limited to the programme team.

## Outputs

- An ownership map on the `ownership-map` template: engaged departments with accountable role, declared owner or "to confirm", time available and gap type; artefacts with accountable role.
- A gap list classified as capability, capacity or vacancy, with the role who decides each appointment.
- A note of departments engaged in a later phase and who covers them meanwhile.

## Microsoft platform considerations

Platform roles (tenant administration, Power Platform and Copilot Studio administration, security and compliance tooling)
should appear as roles distinct from business owners. Do not infer from the estate that a role exists; ask.

## Adoption considerations

Champions support many departments but own none; record them as contributors, not accountable roles. Make sure the
adoption programme has a business-side accountable role and not only an IT one.

## Knowledge considerations

Where agents or knowledge-heavy scenarios are in scope, include knowledge owners as a role family, even if unnamed. The
`knowledge-management` department has a Knowledge Manager lead role, defined through
`knowledge-management:knowledge-owner-model`; where that role is vacant, record the gap and who decides the appointment.

## Security and privacy considerations

The map holds organisational information and may contain role holders' aliases; store it in the organisation's own
location with restricted access. Record no personal data beyond what the organisation chose to declare.

## Responsible AI considerations

Human accountability must be explicit for any solution at tier 3 or above. If the map has no role able to accept that
accountability, record it as a vacancy that blocks those solutions.

## Evaluation requirements

Not applicable, because the map is an organisational artefact rather than an AI solution; it is tested by checking that
every engaged department and artefact has exactly one accountable role.

## Value measures

Track the share of artefacts and live solutions with a confirmed owner and the number of open vacancies, reported by the
CoE or working-group lead through `ai-centre-of-excellence:coe-kpi-framework`. Never measure individuals.

## Scale notes

### Starter

Five to eight rows. One person may hold several lead roles; record that honestly and note the partner's part. The
working-group lead covers departments engaged in a later phase.

### Scale

A row per engaged department with distinct adoption, platform, governance and portfolio roles, and reviewer roles kept
independent.

### Enterprise

A hub map and spoke maps per business unit, with spoke leads named by role and hub roles holding standards and reviewer
gates.

## Hand-offs

- To `ai-centre-of-excellence:coe-raci` to turn department ownership into activity-level responsibilities.
- To `organisation-tailoring:transformation-pack` to name the responsible owner on each artefact.
- To `ai-centre-of-excellence:coe-operating-model` where gaps change the CoE design.

## Reviewer gates

Not applicable, because the map releases no solution; it must still show `security-privacy` as an independent gate holder
from risk tier 2, separate from any delivery owner.

## Failure modes

- Gaps are filled with plausible names, and people discover they own something from a document.
- One enthusiastic role is accountable for everything, and the programme stalls when they are busy.
- Reviewer and builder are the same role, so gates are nominal.
- The map turns into a judgement of individuals and is quietly abandoned.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Name an owner the organisation has not declared.
- Rank, score or compare individuals.
- Make the same role accountable for building and reviewing a solution.
- Use usage or performance data to decide ownership.

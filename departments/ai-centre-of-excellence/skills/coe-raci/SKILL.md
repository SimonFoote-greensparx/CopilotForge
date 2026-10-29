---
name: coe-raci
description: Builds a role-based RACI for AI work across the opportunity lifecycle, governance decisions, knowledge ownership, release and value, with exactly one Accountable per activity and the business accountable for outcomes. Use when nobody can say who approves an agent, when IT is being held to account for business benefits, or when a new CoE needs clear responsibilities before its first steering meeting.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Mobilise, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-studio-zoned-governance, ms-copilot-studio-guidance, nist-ai-rmf, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# CoE RACI

## Purpose

When AI work goes wrong, the question that follows is "who agreed this?", and in most organisations nobody can answer.
This skill produces a RACI that names, by role, who is responsible, accountable, consulted and informed for each
activity across the opportunity lifecycle, governance, knowledge, release and value. It keeps the business accountable
for outcomes and benefits, and the CoE and IT accountable for method, platform and assurance. RACIs usually fail by
giving several roles an A, by naming people instead of roles, or by making IT accountable for benefits it cannot deliver.

## When to use

- A CoE or working group is forming and needs responsibilities agreed before its first decisions.
- Nobody can say who approves an agent for release, or who owns it afterwards.
- Benefits are being reported by IT or the CoE rather than by the business owner.
- An audit, incident or near miss has exposed unclear accountability.
- A hub-and-spoke model needs the split between hub and spoke written down.

## When not to use

- Deciding the CoE's purpose and decision rights in principle - use `ai-centre-of-excellence:coe-charter`.
- Designing the team and the intake-to-delivery flow - use `ai-centre-of-excellence:coe-operating-model`.
- Mapping accountable roles across every department in a transformation pack - use `organisation-tailoring:ownership-map`.
- Defining the controls each risk tier needs - use `ai-centre-of-excellence:coe-governance-model`.
- Ownership of a single agent's knowledge and lifecycle - use `m365-agents:agent-release-readiness`.

## Questions to ask first

1. Which roles actually exist today (sponsor, CoE lead, business owners, IT, information security, data protection, Champions, partners), and which are still to be appointed?
2. Which decisions does the charter give the CoE, and which stay with business owners or existing boards?
3. Is the organisation running one CoE or a hub with spokes, and which decisions are delegated to spokes?
4. Who currently signs off releases of shared agents or automations, formally or in practice?
5. Who reports benefits to the executive today, and on what basis?

## Required inputs

- The charter's decision rights from `ai-centre-of-excellence:coe-charter`.
- The operating model's flow and roles from `ai-centre-of-excellence:coe-operating-model`.
- The roles the organisation has declared, from the organisation profile or the ownership map.
- The risk tiers and gates from `ai-centre-of-excellence:coe-governance-model`, if already drafted.

Where a role does not yet exist, write the role title and mark it `[To confirm: role to be appointed]`. Never fill a
gap by assigning work to a named person, and never invent a role the organisation has not agreed to create.

## Decision framework

Apply these rules to every row before the RACI is accepted.

| Rule | Test | Fix if it fails |
|---|---|---|
| One Accountable | Exactly one A per activity | Split the activity or move the A to the role who answers for the result |
| Business owns outcomes | Benefits, priorities, adoption in a team and knowledge content have a business A | Move the A from IT or the CoE to the business owner |
| Enablers own method | Platform, standards, reviewer gates and the register have a CoE or IT A | Move the A away from the business |
| Reviewers stay independent | Reviewers are Consulted or hold a gate; they are never A for the thing they review | Separate reviewer from builder |
| Roles not names | Every cell names a role | Replace names with roles |
| A can say no | The A has the authority and information to refuse | Escalate or move the A |
| Champions bounded | Champions are R or C for peer guidance and routing, never A for approval or release | Reassign |

Start with a one-page summary the sponsor can hold in their head, then detail it. A typical starting allocation for a
business-owned CoE, where the CoE lead sits in the benefiting business unit, is below; challenge it locally rather than
copying it.

| Activity | Executive sponsor | CoE lead | Champions | Central AI enablement |
|---|---|---|---|---|
| Prioritisation | A | R | C | C |
| Funding | A | C | I | I |
| Delivery | I | A | R | C |
| Knowledge management | I | A | R | C |
| Governance | C | C | I | A |
| Adoption | C | A | R | C |

Individual solution benefits and knowledge content still sit with each solution's business owner and knowledge owner in
the detailed matrix. Cover these activity groups at minimum: opportunity lifecycle (Identify, Assess, Prioritise, Build, Deploy, Measure,
Improve), governance decisions (risk tier, release by tier, exceptions, risk acceptance), knowledge ownership, platform
and register, adoption and Champions, and value reporting.

## Practitioner approach

Begin with the summary. Six rows - prioritisation, funding, delivery, knowledge management, governance and adoption -
across the sponsor, the CoE lead, Champions and the central AI enablement function show at a glance that the business
leads and enablement supports. If the sponsor will not hold the A for prioritisation and funding, the CoE has no
authority, and that is a charter problem to fix before going further. A clear summary is also what stops AI delivery
turning into a request queue for the central team.

Then list detailed activities before roles. Walk the opportunity lifecycle and write each activity as a verb and
object: "frame the problem", "classify the risk tier", "approve release of a tier 2 agent", "maintain the knowledge source", "report the
benefit". Add the governance decisions and the recurring work - reviewing the register, retiring unused agents,
updating the acceptable-use starter. Twenty-five to forty rows is usually right for a Scale organisation; more than
sixty and nobody will read it.

Next, list roles, using the titles the organisation uses. Typical columns are executive sponsor, CoE lead, business
owner, knowledge owner, maker or delivery team, platform or IT lead, information security, data protection, the central
AI enablement function, Champions (split into knowledge, process, adoption and AI champion roles where that helps) and,
where used, a delivery partner. In a hub-and-spoke model add a spoke lead column.

Fill the A column first, one row at a time, asking "who answers for this if it goes wrong?". This is where the
principle bites. The business owner is accountable for the problem statement, the priority within their area, the
knowledge their solution uses, adoption in their team and the benefit. The CoE lead is accountable for the method,
intake criteria and register. The platform lead is accountable for environments, connectors and technical support.
Release approval belongs to the role the charter names for that tier, with the reviewers as gates, not owners.

Then fill R, C and I. Keep C small: consulting everyone slows every decision. Make reviewer-class roles C or gate
holders, never A for what they review, so their independence survives.

Test the draft against the decision framework and against two or three real cases: an agent a department built last
month, a Copilot scenario rolled out to a team, an automation that failed. If the RACI cannot say who should have acted,
fix it. Watch for the common distortions: IT as A for benefits, Champions as A for approvals, and the sponsor as A for
everything because nobody else would accept it.

Take the RACI to the steering forum for agreement and record the decision. Review it when the operating model changes
or when an incident reveals a gap.

## Outputs

- A one-page summary RACI on the `coe-raci` template across prioritisation, funding, delivery, knowledge management, governance and adoption, for the sponsor.
- A detailed RACI matrix on the `coe-raci` template: activities grouped by lifecycle stage, governance, knowledge, release and value; roles as columns; one A per row.
- A short list of role gaps marked `[To confirm]` with the proposed owner of the appointment decision.
- A record of the steering decision agreeing the RACI and its review date.

## Microsoft platform considerations

Platform administration roles (tenant, Power Platform and Copilot Studio administration, environment ownership) should
appear as roles, distinct from the business owner of any agent. Where environments are zoned, align the release approval
rows with the zones so the RACI and the platform controls tell the same story. Check current administrative roles and
controls in `references/sources.md`.

## Adoption considerations

Adoption in a team is a business accountability supported by the adoption lead and Champions. Publish a one-page
summary of who to go to for what, because staff use the RACI only if they can find it.

## Knowledge considerations

Every knowledge source used by a shared solution needs a business knowledge owner as A for its accuracy and review
cycle, separate from the solution owner where the source serves several solutions. The `knowledge-management`
department (planned) will refine this.

## Security and privacy considerations

Information security and data protection roles are gate holders from tier 2. The RACI must show they can block release
and that disagreement escalates to the accountable executive, recorded in writing.

## Responsible AI considerations

Name who holds human accountability for decisions informed by AI outputs at tier 3 and 4, and who accepts residual risk
at tier 4. That role must be an executive, not the CoE.

## Evaluation requirements

Not applicable to the RACI itself; the RACI should still show who is accountable for evaluation evidence before
release, which `ai-centre-of-excellence:coe-governance-model` defines by tier.

## Value measures

The RACI's effect shows in decision speed and clarity: time from request to release decision, the number of escalations
caused by unclear ownership, and the share of live solutions with a named business owner. The CoE lead reports these
through `ai-centre-of-excellence:coe-kpi-framework`.

## Scale notes

### Starter

The six-row summary plus a single page of fifteen to twenty rows and five or six roles. The sponsor or managing role is often A for release; that
is fine if it is written down.

### Scale

Twenty-five to forty rows across the full lifecycle, with release approval delegated by tier and knowledge owners named
per source.

### Enterprise

A hub RACI and a spoke RACI that inherits from it, showing what spokes decide alone, plus links to enterprise risk and
architecture boards. Formal assurance overlays add an evidence-recording role at each gate.

## Hand-offs

- To `ai-centre-of-excellence:coe-cadence` so each forum has the decisions the RACI assigns to it.
- To `organisation-tailoring:ownership-map` to align department-level accountable roles.
- To `ai-centre-of-excellence:coe-governance-model` for gate holders by tier.

## Reviewer gates

Not applicable as a release gate, because the RACI governs decisions rather than releasing a solution. `security-privacy`
should confirm its own rows before the RACI is agreed.

## Failure modes

- Two or three roles hold A for release, so each assumes another checked.
- IT is accountable for benefits, so the business never measures them.
- The RACI names people, and is out of date the first time someone moves role.
- Champions end up accountable for approvals they have neither the authority nor the time to give.
- The central AI enablement function is A for delivery and adoption, so business units queue requests instead of leading.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Allow more than one Accountable role for an activity.
- Name individuals in the matrix.
- Make IT or the CoE accountable for business outcomes or benefits.
- Make a reviewer accountable for the solution it reviews.

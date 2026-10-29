---
name: ai-role-catalogue
description: Maintains the catalogue of AI transformation roles - department lead roles plus sponsor, business, knowledge, solution and reviewer roles - each with purpose, responsibilities, decisions, capabilities, separation rules and typical time, and maps them to the job roles the organisation has declared. Use when an operating model names roles nobody recognises, when job titles must be matched to AI roles, or when the catalogue needs updating.
license: CC-BY-4.0
metadata:
  department: organisation-tailoring
  lifecycle: Mobilise, Enable, Scale
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-champion-programme, ms-copilot-studio-guidance, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# AI role catalogue

## Purpose

Operating models, RACIs and ownership maps all refer to roles such as "Agent Product Owner", "Knowledge Owner" or
"Responsible AI Reviewer", and organisations rarely have job titles that match. This skill maintains one catalogue of AI
transformation roles, each defined by purpose, responsibilities, decisions it holds, capabilities it needs, separation
rules and typical time by edition, and maps those roles to the job roles the organisation has declared. It is the shared
vocabulary that lets every other artefact name the same role the same way. Role catalogues go wrong when they become job
descriptions, when roles are defined by technology rather than responsibility, and when the mapping is used to judge the
people who hold the jobs.

## When to use

- An operating model, RACI or pack names roles that people in the organisation do not recognise.
- Job titles need to be matched to the AI roles the programme relies on, before owners are named.
- Several documents describe the same role differently and need a single definition.
- The organisation is adding roles as it scales (spoke leads, specialist reviewers, AI engineers) and the catalogue needs updating.
- HR or a line manager asks what an AI role involves and how much time it takes.

## When not to use

- Assigning an accountable role to each department and pack artefact - use `organisation-tailoring:ownership-map`.
- Designing the CoE core team and its supporting roles - use `ai-centre-of-excellence:coe-team-design`.
- Activity-level responsibilities for CoE work - use `ai-centre-of-excellence:coe-raci`.
- Analysing what AI skills each role needs to learn - use `learning-and-skills:ai-skills-needs-analysis`.
- Deciding the operating model shape the roles sit in - use `ai-strategy:ai-operating-model`.

## Questions to ask first

1. Which job roles and titles has the organisation declared for AI work, and which are filled, vacant or covered part-time?
2. Which edition and operating model shape apply, since they decide which roles are combined or separate?
3. Which roles must stay independent of each other (builder and approver, solution owner and reviewer)?
4. Does HR need role profiles for recruitment or job design, or only a working catalogue for the programme?
5. Who will own the catalogue and approve changes to it?

## Required inputs

- The department catalogue with each department's lead role, which supplies the backbone of the role list.
- The tailored operating model from `organisation-tailoring:operating-model-tailoring` or `ai-strategy:ai-operating-model`.
- The organisation's declared job roles and titles, from the profile or the sponsor.
- Separation requirements by risk tier from `opportunity-management:risk-classification` and the governance framework.

If the organisation has not declared a job role for a catalogue role, the mapping reads "not yet mapped" and the gap goes
to the ownership map. Never infer a mapping from a person's name, seniority or apparent interest.

## Decision framework

Organise the catalogue in role families. Each role entry has the same fields.

| Family | Example roles | Defined by |
|---|---|---|
| Direction | Executive sponsor, accountable executive for tier 3 and 4, AI Strategy Lead | Decisions on outcomes, funding and risk acceptance |
| Orchestration | AI CoE Lead, AI Programme Manager, AI Portfolio Manager, Transformation Architect | Running the system of work |
| Business ownership | Business owner, benefit owner, knowledge owner, solution owner | Owning outcomes, content and live solutions |
| Adoption | Adoption Lead, Champions Programme Owner, Change Lead, Learning Lead, Champion | Changing how people work |
| Delivery | Agent Product Owner, maker, Copilot Studio Architect, AI Engineer, Automation Lead | Building and changing solutions |
| Platform and operations | Platform Governance Lead, platform administrators, AI Operations Lead | Running the estate and live solutions |
| Assurance | Security and Privacy Reviewer, Responsible AI Reviewer, AI Evaluation Lead, AI Design Authority, DPO (as organisational role) | Independent review and approval |

| Field | Content |
|---|---|
| Purpose | One sentence on why the role exists |
| Responsibilities | Five to eight verbs and objects |
| Decisions held | What the role decides, approves or recommends |
| Capabilities | What the role must be able to do, as demonstrable capability |
| Separation | Roles it must not be combined with, and from which risk tier |
| Typical time by edition | Starter, Scale and Enterprise, as ranges to confirm locally |
| Mapped job roles | The organisation's declared titles that hold it, or "not yet mapped" |

Mapping rules: one catalogue role may map to several job roles (spoke leads), and one job role may hold several catalogue
roles, provided no separation rule is broken.

## Practitioner approach

Build the catalogue from responsibilities, not titles. Start with the lead roles in the department catalogue, then add the
roles every AI programme relies on that are not department leads: executive sponsor, accountable executive, business
owner, knowledge owner, solution owner, maker, Champion. Write each one's purpose in a single sentence. If you cannot,
the role is either two roles or not a role.

Fill the fields for each role. Write responsibilities as actions ("keeps grounding content current and reviews it on a
set cycle"), decisions as rights ("approves which content an agent may ground on"), and capabilities as things that can
be shown ("can explain how permissions affect what Copilot returns"). Avoid naming products in the role definition;
product names change faster than responsibilities.

Write separation rules carefully, because they are the part of the catalogue that protects people and the organisation.
The maker of a tier 2 or higher solution is not its release approver; reviewers are independent of solution owners; the
accountable executive for a tier 3 or 4 use is not the person who built it. Everything else can be combined when the
organisation is small.

Give typical time by edition as ranges and mark them as starting points to confirm. A Champions Programme Owner at Starter
may be a few hours a month; at Enterprise it may be a substantial part of a role. Never present these as standards; they
are prompts for an honest conversation about capacity.

Map to the organisation's declared job roles with the sponsor or HR. Take each catalogue role and ask which declared role
holds it today, or should. Record the mapping, the combinations and any separation conflicts. Leave unmapped roles
visible; they become vacancies in `organisation-tailoring:ownership-map`. Do not map by reputation or by who seems keen,
and never use the catalogue to compare the people in mapped roles.

Keep the catalogue as a living reference. Add roles when the operating model grows (spoke leads, specialist reviewers,
AI engineers), retire roles that are no longer needed, and record each change with its reason and approver. Every other
artefact that names a role should use the catalogue's name, so a change here is a change everywhere.

## Outputs

- An AI role catalogue: each role with family, purpose, responsibilities, decisions held, capabilities, separation rules and typical time by edition, consistent with the role catalogue section of the `ai-operating-model` template.
- A role mapping table: catalogue role, the organisation's declared job role or roles, combinations, separation check and status (mapped, not yet mapped, conflict).
- A change log for the catalogue with reasons and approvers.

## Microsoft platform considerations

Platform roles (tenant administration, Power Platform and Copilot Studio administration, security and compliance tooling,
Azure for Foundry solutions) are defined by responsibility; the admin roles that grant permissions in Microsoft products
are configured separately and checked against `references/sources.md`. Do not equate a catalogue role with a product
admin role.

## Adoption considerations

Champions are contributors, not owners: define the Champion role with clear boundaries so it does not drift into an
unpaid help desk. Make sure adoption roles sit on the business side as well as in IT.

## Knowledge considerations

Knowledge owner is the role most often missing from AI catalogues. Define it explicitly, with the decision right over what
an agent may ground on and the duty to keep content current.

## Security and privacy considerations

The catalogue holds role definitions and organisational job titles, not personal data. If the mapping includes aliases
for role holders, store it in the organisation's own location with restricted access.

## Responsible AI considerations

Define the accountable executive and Responsible AI Reviewer roles even at Starter, so tier 3 and 4 uses have somewhere to
go. Never use role mappings to assess, rank or profile the individuals who hold them.

## Evaluation requirements

Not applicable, because the catalogue is an organisational reference rather than an AI solution; it is tested by checking
that every role named in the pack exists in the catalogue and no mapping breaks a separation rule.

## Value measures

Track the share of catalogue roles mapped to a declared job role, separation conflicts open, and artefacts using catalogue
role names consistently, reported by the Transformation Architect at organisation level. Never measure the people in the
roles.

## Scale notes

### Starter

A short catalogue of ten to fifteen roles, most held by two or three job roles, with the separation rules stated and the
partner's roles included.

### Scale

A full catalogue across all families, mapped to declared job roles with HR, used by every artefact in the pack.

### Enterprise

A catalogue owned centrally with spoke variants per business unit, mapped to the organisation's job architecture, and
changed through a recorded approval route.

## Hand-offs

- To `organisation-tailoring:ownership-map` for unmapped roles and the appointments to make.
- To `ai-centre-of-excellence:coe-raci` so activity responsibilities use catalogue roles.
- To `learning-and-skills:ai-skills-needs-analysis` for the skills each role needs.
- To `organisation-tailoring:capability-gap-analysis` where mapped roles lack capability or time.

## Reviewer gates

Not applicable, because the catalogue releases no solution; it must define reviewer roles for `security-privacy`,
`responsible-ai`, `evaluation-quality` and `design-authority` as independent of builder and solution owner roles.

## Failure modes

- Roles are defined by tools ("the Copilot Studio person") and become obsolete when products change.
- The catalogue turns into job descriptions and stalls in HR review.
- Separation rules are dropped to make the mapping fit a small team.
- The mapping is used to judge the people in mapped roles, and the organisation stops sharing honest information.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Map a role to a named individual the organisation has not declared.
- Rank, score or compare the people who hold mapped roles.
- Combine roles in a way that breaks a separation rule.
- Present typical time ranges as fixed standards.

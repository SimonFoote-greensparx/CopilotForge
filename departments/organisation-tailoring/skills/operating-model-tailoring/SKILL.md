---
name: operating-model-tailoring
description: Right-sizes the AI target operating model for one organisation from its confirmed edition, overlay, archetype, signals and declared constraints - which structures to adopt now, which roles to combine, which forums to merge, what a partner covers, what to defer and what would trigger a change - each decision traced to a rule or constraint. Use when a generic operating model looks too heavy or too light, or when constraints change.
license: CC-BY-4.0
metadata:
  department: organisation-tailoring
  lifecycle: Envision, Mobilise
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-studio-zoned-governance, ms-coe-starter-kit, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# Operating model tailoring

## Purpose

A target operating model written for a large, federated organisation will crush a forty-person practice, and one written
for a small team will leave a regulated multi-unit organisation without the separation and assurance it needs. This skill
right-sizes the operating model for one organisation: from the confirmed edition, assurance overlay, archetype, signals
and declared constraints, it decides which structures to adopt now, which roles to combine, which forums to merge, where
a partner fills in, what to defer, and what would trigger a change. Every tailoring decision is traced to a rule or a
stated constraint so it can be explained and revisited. Tailoring goes wrong when it trims the controls that protect
people to save effort, when it copies a model from elsewhere, or when deferrals are never revisited.

## When to use

- A confirmed edition and archetype exist and the operating model needs to be sized before it is designed in detail.
- A sponsor says the proposed operating model is too heavy (or too light) for their organisation.
- Declared constraints (capacity, budget, timeline, partner dependence) mean the standard model cannot be staffed.
- Circumstances have changed, such as a second business unit starting to build agents or a regulator's new expectations, and the model's weight needs revisiting.
- Two business units need different weights of operating model within one organisation.

## When not to use

- Choosing the operating model shape and designing decision rights, build and support responsibilities - use `ai-strategy:ai-operating-model`.
- Recommending the edition, overlay and archetype in the first place - use `organisation-tailoring:edition-and-archetype`.
- Designing how the CoE itself runs - use `ai-centre-of-excellence:coe-operating-model`.
- Defining the roles and mapping them to the organisation's job roles - use `organisation-tailoring:ai-role-catalogue`.
- Quantifying the capability and capacity shortfall behind a constraint - use `organisation-tailoring:capability-gap-analysis`.

## Questions to ask first

1. Has the sponsor confirmed the edition, assurance overlay and archetype, and which emerging signals were reported?
2. What constraints has the organisation declared (people's time, budget, timeline, internal skills, partner use), and which are firm?
3. Is there already an operating model, CoE or working group, and what about it works?
4. Which risk tiers will the organisation build or use in the next year, since separation and assurance requirements follow the tiers?
5. Do business units differ enough that one model will not fit them all?

## Required inputs

- The confirmed recommendation from `organisation-tailoring:edition-and-archetype`, with rule ids and signals.
- The validated profile from `organisation-tailoring:ai-profile-intake`, especially delivery capability and constraints.
- Any existing operating model, CoE charter or working-group terms.
- The capability and capacity gaps from `organisation-tailoring:capability-gap-analysis`, where available.

Where a constraint is unknown, mark it `[To confirm: ...]` and tailor to the cautious reading: assume less capacity, not
more. Never infer that a role exists or that someone has time because the organisation has a certain size.

## Decision framework

Tailor each component of the operating model with one of five decisions.

| Decision | Use when | Record |
|---|---|---|
| Adopt | The component is needed now at the edition's standard depth | Depth and owner role |
| Combine | Two or more roles or forums can be held together without breaking a separation rule | What is combined and the separation preserved |
| Substitute | A lighter or partner-provided form meets the need for now | The substitute and when it should be replaced |
| Defer | The component is not needed until a trigger occurs | The trigger and who watches for it |
| Strengthen | The overlay, a signal or a risk tier needs more than the edition default | The reason and the rule or constraint behind it |

Typical tailoring by edition:

| Component | Starter | Scale | Enterprise |
|---|---|---|---|
| Governing body | AI working group in place of a CoE | Business-owned CoE with core team | Hub CoE with spokes per business unit |
| Forums | Working group with a sponsor decision slot | Working group, monthly steering, quarterly review | Spoke forums, hub steering, executive board |
| Roles | Several lead roles held by one or two people | Distinct adoption, platform, governance and portfolio roles | Spoke leads per unit, hub specialists |
| Assurance | Proportionate, reviewer roles may be borrowed or partnered | Reviewer roles independent of builders | Formal assurance where the overlay requires it |
| Delivery | Partner for anything above tier 1 | Internal makers for tier 0 to 2, partner for specialist work | Unit makers within guardrails, hub engineering |

Separation rules never tailored away: the role that builds a tier 2 or higher solution does not approve its release; a
reviewer role is independent of the solution owner; a named accountable executive exists for any tier 3 or 4 use. Signals
can strengthen components regardless of edition: agents emerging brings intake and agent ownership forward; shadow AI
brings an approved-use starter forward; a formal assurance overlay strengthens evidence at every gate.

## Practitioner approach

Start from the confirmed recommendation and read it back in operating model terms: "Scale, proportionate assurance,
adopter archetype, with agents emerging and weak knowledge ownership." That sentence already says most of what matters:
a business-owned CoE is right, adoption is the main effort, intake and agent ownership must arrive early, and knowledge
ownership is a precondition rather than a later nicety.

List the components of the operating model (governing body, forums, roles, decision rights by tier, delivery route,
support route, assurance, measurement) and take a tailoring decision for each using the five options. Write the reason
beside each one, citing the rule id from the edition and archetype recommendation or the declared constraint. A decision
with no stated reason will be reopened by the next person who disagrees with it.

Test combinations against the separation rules before agreeing them. Combining the adoption lead and Champions programme
owner in a Starter organisation is sensible; combining the maker and the release approver for tier 2 work is not,
however small the organisation. Where separation cannot be achieved internally, substitute a partner or a peer from
another function, and say so.

Use substitutions and deferrals honestly. An AI working group in place of a CoE is a substitution with a trigger, such
as a second business unit building agents or the first tier 2 solution entering delivery. A deferred knowledge pillar is
a deferral with a trigger, such as the first agent grounded on owned content. Name who watches for each trigger;
deferrals without a watcher become permanent gaps.

Check the tailored model against declared capacity. If the tailored model still needs more time than the declared roles
have, either tailor further, bring in a partner, or flag the shortfall to `organisation-tailoring:capability-gap-analysis`.
Do not hand on a model that cannot be staffed.

Explain the result to the sponsor in one page: what is adopted, combined, substituted, deferred and strengthened, and
why. Make clear that the tailoring is a CopilotForge proposal based on stated rules, not a Microsoft classification, and
that the sponsor can override edition-level choices with a recorded reason but not the separation rules. Then hand the
tailoring brief to `ai-strategy:ai-operating-model` to design within, or use it to adjust an existing model.

## Outputs

- An operating model tailoring record: each component with its decision (adopt, combine, substitute, defer, strengthen), depth, owner role, reason and rule id or constraint, recorded alongside the `ai-operating-model` template.
- A list of triggers for substituted and deferred components, with the role watching for each.
- A one-page sponsor explanation and a record of confirmation or recorded overrides.

## Microsoft platform considerations

Platform governance components (environment zoning, maker controls, inventory) also scale with edition; tailor them using
the zoned governance and CoE Starter Kit guidance in the source records, and check product facts in
`references/sources.md`. Do not tailor on the assumption that a governance feature is available or licensed.

## Adoption considerations

For explorers and adopters, tailoring should protect adoption roles and Champions coordination before adding delivery
structures. A lightweight model with a strong adoption lead usually outperforms a heavy model with none.

## Knowledge considerations

Where the weak-knowledge signal appears, strengthen knowledge ownership even at Starter: at minimum, name knowledge owner
roles for any content an agent will ground on. The `knowledge-management` skills hold the detailed method.

## Security and privacy considerations

Never tailor away the `security-privacy` gate from risk tier 2 or the DPO's role in personal data decisions. At Starter,
reviewer capacity may be borrowed from IT or a partner, but it must stay independent of the builder.

## Responsible AI considerations

Tier 3 and 4 uses require an accountable executive and `responsible-ai` review in every edition. If the tailored model
cannot provide them, record that such uses are out of scope until it can.

## Evaluation requirements

Not applicable, because the output is an organisational design rather than an AI solution; it is tested by walking two
or three real scenarios through the tailored model and confirming none stalls or bypasses a separation rule.

## Value measures

Track whether the tailored model is staffed (share of adopted roles with a declared owner), how many deferral triggers
have fired and been acted on, and time from intake to decision for typical requests, reported by the Transformation
Architect at organisation level.

## Scale notes

### Starter

Combine freely within the separation rules, substitute a working group for a CoE, partner for anything above tier 1, and
defer most pillars with clear triggers.

### Scale

Adopt the business-owned CoE, keep reviewer roles independent, combine only where capacity is genuinely limited, and
bring agent ownership forward when agents are emerging.

### Enterprise

Tailor per business unit where units differ materially, strengthen assurance where the overlay is formal, and keep hub
standards untailored so units repeat them.

## Hand-offs

- To `ai-strategy:ai-operating-model` with the tailoring brief, to design the model within it.
- To `organisation-tailoring:ai-role-catalogue` to define the combined and adopted roles.
- To `organisation-tailoring:transformation-pack` so artefacts are produced at the tailored depth.
- To `ai-centre-of-excellence:coe-operating-model` when the CoE's own design follows from the tailoring.

## Reviewer gates

Not applicable, because tailoring releases no solution; the tailored model must keep `security-privacy` from risk tier 2
and the `responsible-ai`, `evaluation-quality` and `design-authority` gates independent of the roles that build.

## Failure modes

- The model is trimmed by removing the reviewer roles that protect people, because they are the least visible.
- A model from another organisation is copied whole and does not fit the declared capacity.
- Deferrals have no trigger or watcher and quietly become permanent gaps.
- Tailoring decisions carry no reasons, so every new stakeholder reopens them.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Tailor away a separation rule, the `security-privacy` gate from tier 2, or the accountable executive for tier 3 and 4.
- Assume capacity or a role exists because of the organisation's size.
- Present tailoring decisions as Microsoft classifications.
- Defer a component without naming its trigger and who watches for it.

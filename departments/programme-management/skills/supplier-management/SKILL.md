---
name: supplier-management
description: Selects and manages the partners and suppliers an AI programme relies on - deciding what to source, setting outcome-based requirements and criteria, testing Microsoft AI capability claims on evidence, structuring work packages, knowledge transfer and exit, and reviewing delivery at service level. Use when a programme needs a Microsoft partner or ISV, when a supplier underdelivers, or when the organisation risks depending on a partner for good.
license: CC-BY-4.0
metadata:
  department: programme-management
  lifecycle: Mobilise, Enable, Deliver, Scale
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral, copilot-studio, ai-foundry, power-platform
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-adoption-hub, ms-copilot-studio-guidance, ms-foundry-models, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Supplier management

## Purpose

Most organisations use partners somewhere in an AI programme: adoption and change support, agent and automation build,
Foundry engineering, training, or an ISV product that sits on Microsoft's platforms. This skill decides what to source,
sets outcome-based requirements, evaluates suppliers on evidence rather than claims, structures the work so capability
transfers to the organisation, and manages delivery and exit. Supplier relationships go wrong when the organisation buys
activity rather than outcomes, when the partner builds solutions nobody internal can own, and when a supplier's AI
capability is taken on trust.

## When to use

- The capability gap analysis shows the programme needs a partner for some workstreams.
- A sponsor asks whether to use a Microsoft partner, an ISV product or internal people for a piece of AI work.
- Suppliers are being shortlisted and evaluation criteria are needed.
- An existing supplier is underdelivering, or knowledge transfer is not happening.
- The organisation fears it cannot run what a partner has built once the contract ends.

## When not to use

- Identifying which capabilities and capacity the programme lacks - use `organisation-tailoring:capability-gap-analysis`.
- Licensing and capacity questions about Microsoft AI products - use `platform-governance:ai-licensing-and-capacity`.
- Reviewing the connectors, APIs or tools a supplier's solution uses - use `security-privacy:connector-review`.
- Tracking a supplier deliverable as a dated dependency on the plan - use `programme-management:dependency-management`.
- Judging whether a supplier's proposed design is the right platform choice - use `design-authority:platform-fit-review`.

## Questions to ask first

1. Which outcomes or work packages does the programme want a supplier for, and why can it not do them internally now?
2. Which capabilities must the organisation own at the end, and which is it content to keep buying?
3. What procurement rules, frameworks and approval limits apply?
4. Will the supplier access organisational data, build solutions in the tenant, or bring its own product or models?
5. What will the organisation do if the supplier leaves or the contract ends?

## Required inputs

- The capability and capacity gaps from `organisation-tailoring:capability-gap-analysis` or the ownership map.
- The programme charter and integrated plan, showing scope, dates and the budget envelope.
- The organisation's procurement policy, supplier security and data protection requirements.
- The risk tiers of the solutions the supplier would work on, from `opportunity-management:risk-classification`.

Where procurement rules or approval limits are unknown, record them as `[To confirm: ...]` with procurement as the owner.
Never commit spend or sign anything on the programme's behalf without the delegated authority the charter sets.

## Decision framework

Decide first whether to source at all.

| Option | Choose when | Watch for |
|---|---|---|
| Build internal capability | The capability is core to running AI after the programme, and time allows | Underestimating ramp-up time |
| Partner with knowledge transfer | Speed matters and the organisation must own the result | Transfer written into the contract but never scheduled |
| Partner as managed service | The organisation genuinely prefers to buy the capability long term | Lock-in, unclear exit, weak internal oversight |
| ISV product on Microsoft platforms | A well-defined need is met by a product with a supportable route | Overlap with capabilities the organisation already licenses |
| Defer | Neither internal nor partner capacity is available at acceptable risk | Shadow AI filling the gap |

Evaluate shortlisted suppliers on evidence.

| Criterion | Evidence to ask for |
|---|---|
| Outcome understanding | How they would measure success for this programme, in business terms |
| Microsoft AI capability | Comparable work they can show, the roles who would do it, and how they keep current with Microsoft change |
| Governance fit | How their work passes risk tiers, reviewer gates, testing and evaluation |
| Ownership and transfer | How internal people will run the result, with a transfer plan and exit provisions |
| Security and data handling | Access model, data location, sub-processors, incident handling |
| Commercials | Outcome-linked milestones, change control, and how licence and consumption costs are separated from services |

Certifications and partner designations are useful signals but not proof; check them against Microsoft's current
listings and ask for evidence of delivery.

## Practitioner approach

Start from what the organisation must own. A programme that wants a self-sufficient CoE in eighteen months should not
buy a managed agent factory with no transfer, however quick it looks. Write down which capabilities stay inside and which
can be bought, and let that shape every later choice.

Write requirements as outcomes and work packages, not days. "Three governed agents released at tier 1 with owners,
evaluation sets and support routes, and two internal makers able to maintain them" is a better requirement than "sixty
days of Copilot Studio consultancy". Outcome-based packages make performance visible and give the supplier something to
be proud of.

Evaluate on evidence. Ask suppliers to walk through comparable work, show how they handled governance and testing, and
introduce the people who would actually do it. Test their understanding of Microsoft's current platform direction, but
verify product claims against the source records rather than accepting them; partners can be as out of date as anyone.
Be cautious with suppliers proposing non-Microsoft AI products where the organisation's scope is Microsoft AI.

Separate services from licences and consumption. Suppliers sometimes bundle licence advice with services; licensing
conclusions go to the Microsoft licensing guide or a licensing partner the organisation trusts, and consumption estimates
are tracked through `programme-management:budget-and-capacity`.

Build transfer into the work. Pair internal people with the supplier from the start, require documentation in the
organisation's own repositories and templates, and make solutions pass the same gates as internal work. Schedule the
transfer milestones on the integrated plan so they cannot quietly drop off.

Manage delivery at service level. Review each supplier monthly against outcomes, milestones, quality, transfer progress
and behaviour against governance. Raise issues early through the contract's own mechanisms and log them in the risk log.
Plan exit at the start: what the organisation would need to continue without the supplier, and how long that would take.

## Outputs

- A sourcing decision per work package, with the option chosen and the reasons.
- Outcome-based requirements and evaluation criteria for supplier selection, with an evidence checklist.
- A supplier register: supplier, work packages, outcomes, milestones, data access, transfer plan, exit provisions, contract owner by role and review date.
- Monthly supplier review notes and a transfer and exit plan for each material supplier.

## Microsoft platform considerations

Suppliers building in the organisation's tenant should work in the organisation's environments, under its data and
connector policies and its ALM route, so solutions remain ownable. ISV products and third-party models available through
Microsoft still need the same gates; model availability through Foundry is described in the source records. Check partner
listings, product facts and licensing positions against `references/sources.md`.

## Adoption considerations

Adoption support bought from a partner should build the organisation's own adoption capability, including its Champions
and managers, rather than replace it. Watch for generic training that ignores the organisation's scenarios.

## Knowledge considerations

Suppliers cannot own the organisation's knowledge. Agent work by a partner still needs internal knowledge owners for each
source, and the supplier's contract should not make content decisions on their behalf.

## Security and privacy considerations

Supplier access to data and to the tenant passes the organisation's supplier security and data protection checks, with
least privilege and time-bound access. Where personal data is shared, the DPO or legal adviser decides the contractual
terms. Solutions built by suppliers pass the `security-privacy` gate from risk tier 2.

## Responsible AI considerations

Require suppliers to follow the organisation's responsible AI principles and gates, and to disclose where their work uses
models or components that make decisions about people. Responsibility for outcomes stays with the organisation.

## Evaluation requirements

Supplier-built solutions carry the same evaluation evidence as internal ones, against thresholds the business owner
agrees. Make delivery of evaluation sets and results a contractual deliverable for tier 2 and above.

## Value measures

Track outcomes delivered against contract, transfer milestones met, internal roles able to run supplier-built solutions,
and supplier issues resolved in time, reported at programme level. Supplier staff are assessed by their employer, not by
the programme.

## Scale notes

### Starter

Often one partner covering much of the programme. Keep requirements outcome-based, insist on simple documentation and
transfer to the working group, and review monthly with the sponsor's delegate.

### Scale

Several suppliers by workstream, a supplier register, formal evaluation and monthly reviews, with transfer milestones on
the integrated plan.

### Enterprise

Framework agreements and preferred suppliers, a supplier management function, consistent evaluation across business
units, and exit plans tested for material suppliers.

## Hand-offs

- To `programme-management:dependency-management` for supplier deliverables on the plan.
- To `programme-management:budget-and-capacity` for supplier costs and forecasts.
- To `security-privacy:connector-review` for connectors, APIs and tools in supplier-built solutions.
- To `platform-governance:ai-licensing-and-capacity` for licensing questions raised during sourcing.

## Reviewer gates

Supplier selection where the supplier will access organisational data or build in the tenant needs `security-privacy`
input from risk tier 2; findings are classified blocking or advisory by that department. Supplier designs at tier 2 and
above are open to `design-authority` challenge like internal ones.

## Failure modes

- The organisation buys days rather than outcomes, and cannot tell whether the supplier is performing.
- Knowledge transfer is in the contract but never scheduled, and the organisation depends on the partner indefinitely.
- A supplier's product or licensing claim is accepted without checking, and the plan rests on it.
- Supplier-built agents bypass the organisation's gates because "the partner tested them".

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Name or recommend a specific partner organisation in a CopilotForge artefact.
- Accept a supplier's licensing conclusion; route it to the Microsoft licensing guide or a licensing partner the organisation chooses.
- Let supplier-built solutions skip the gates internal solutions pass.
- Commit spend beyond the delegated authority the charter sets.

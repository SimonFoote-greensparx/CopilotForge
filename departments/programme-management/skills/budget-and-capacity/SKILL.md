---
name: budget-and-capacity
description: Plans and tracks an AI programme's budget and people capacity - services, internal time, licences as advised, and consumption costs such as Copilot Studio and Foundry usage - with forecasts, variance against tolerance, and monthly capacity of scarce roles such as knowledge owners and reviewers. Use when a programme needs a cost and capacity baseline, when consumption costs are growing, or when the same people are committed twice.
license: CC-BY-4.0
metadata:
  department: programme-management
  lifecycle: Mobilise, Deliver, Measure, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral, m365-copilot, copilot-studio, ai-foundry, power-platform, azure
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-studio-guidance, ms-foundry-models, ms-managed-environments, ms-coe-starter-kit
  status: draft
  authors: Simon Foote
---

# Budget and capacity

## Purpose

An AI programme spends three kinds of resource: money on services and products, consumption that grows with use, and the
time of a few scarce people. This skill sets the programme's cost and capacity baseline, tracks actuals and forecasts
against the charter's tolerances, and keeps scarce roles from being committed twice. It goes wrong when consumption costs
are treated as fixed, when licence figures are estimated from memory, and when capacity planning counts makers but forgets
the business owners, knowledge owners and reviewers who actually constrain delivery.

## When to use

- A programme has been chartered and needs a budget baseline and a capacity plan.
- Consumption costs (agent messages, model usage, Azure resources) are growing faster than expected.
- Several workstreams are relying on the same business owners, knowledge owners or reviewers in the same month.
- The board asks for a forecast to completion or a variance explanation.
- A scale-out decision needs to know what more use would cost and who would support it.

## When not to use

- Building the funding case for the programme before approval - use `ai-strategy:investment-case`.
- Licensing and capacity questions about Microsoft AI products - use `platform-governance:ai-licensing-and-capacity`.
- Managing model and platform cost inside a specific Foundry solution - use `ai-foundry:foundry-cost-management`.
- Modelling return on investment and benefits - use `value-realisation:roi-model`.
- Finding which capabilities and roles the programme lacks altogether - use `organisation-tailoring:capability-gap-analysis`.

## Questions to ask first

1. What funding envelope has been approved, over what period, and what tolerance has the charter set?
2. Which costs are fixed (services, committed licences) and which grow with use (consumption-based agents, model usage, Azure resources)?
3. Who in finance and IT owns the licence and cloud cost data, and how often can the programme see it?
4. Which roles are scarce, and how much time has each declared for the programme by month?
5. What reserve is held for supporting what goes live, and for unplanned work?

## Required inputs

- The programme charter with funding envelope and tolerances, and any approved investment case.
- The integrated plan, so costs and capacity can be placed by month.
- Licence and consumption positions as advised by the Microsoft licensing guide, a licensing partner or the organisation's licensing team.
- Declared time for scarce roles from `organisation-tailoring:ownership-map` or `organisation-tailoring:capability-gap-analysis`.
- Cost data access agreed with finance and IT.

Any cost not confirmed by its owner is recorded as `[To confirm: ...]` with the owner named. Never estimate licence
prices, consumption rates or capacity limits from memory; those come from the source records, the licensing route or the
organisation's own billing data.

## Decision framework

Structure the budget by cost type, because each behaves differently.

| Cost type | Behaviour | Tracked by | Main control |
|---|---|---|---|
| Internal people time | Fixed by commitment, often hidden | Declared time by role and month | Capacity plan and reserve |
| Services and suppliers | Milestone or time-based | Contract and milestones | Outcome-based payment, change control |
| Licences | Step changes at assignment or renewal | Licensing team and billing | Assign against readiness, review unused |
| Consumption (agents, models, cloud) | Grows with use and design choices | Billing, platform admin and cost reporting | Budgets, alerts, design reviews, owner per solution |
| Contingency | Held for risk | Programme manager under board control | Release only by decision |

Classify variance and respond.

| Variance | Response |
|---|---|
| Within tolerance | Report in the health report |
| Forecast to breach tolerance | Options paper to the programme board |
| Breaches the sponsor's reserved limit | Sponsor decision |
| Consumption growing without a matching value case | Refer the solution to its owner and `opportunity-management:scale-or-stop` |

For capacity, no scarce role is committed beyond its declared time in any month, and each keeps a reserve for supporting
live solutions.

## Practitioner approach

Build the baseline with finance, not for them. Agree the cost categories, where actuals will come from, and how often the
programme will see them. Put internal people time into the baseline even if it is not charged; a programme that looks
cheap because its business owners are uncosted will over-commit them.

Treat licences as advice you receive, not numbers you produce. Record the licence positions the licensing team or partner
gives you, the date and the source, and assign licences against readiness rather than in one batch. Unused licences are
both a cost and an adoption signal; review them with the adoption lead, at team level, never by naming people.

Model consumption costs explicitly. Agents built in Copilot Studio, models deployed through Foundry and the Azure
resources behind engineered solutions all have costs that grow with use and with design choices such as how much an
agent retrieves or how often a flow runs. For each solution that consumes, name an owner, set a budget and an alert where
the platform allows it, and forecast from observed use rather than guesses. Check how each platform meters and reports use
in the source records, because metering models change.

Plan capacity by role and month. List the scarce roles (business owners, knowledge owners, security and privacy
reviewers, responsible AI reviewers, makers and engineers, adoption and Champions leads) and their declared time. Add up
the demand from the integrated plan. Where demand exceeds supply, move work, reduce scope, or bring in a supplier through
`programme-management:supplier-management`; do not assume people will stretch. Keep a reserve, typically for support of
live solutions and for the unplanned.

Report monthly: actuals, forecast to completion, variance against tolerance with the reason, consumption trends per
solution, and capacity hot spots. Bring forecast breaches to the board as options, not as surprises. When the programme
scales a solution, show the consumption and support cost of scaling next to its value case, so scale-or-stop decisions see
both.

At closure, hand ongoing licence, consumption and capacity tracking for live solutions to the CoE and platform team, with
an owner and budget per solution.

## Outputs

- A budget baseline by cost type and month, with sources and owners for each line and `[To confirm: ...]` where unconfirmed.
- A monthly cost report: actuals, forecast to completion, variance against tolerance and consumption trend per solution, feeding the `programme-health-report` template.
- A capacity plan by scarce role and month, with demand, declared supply, reserve and resolution actions.
- A hand-over of run costs and owners for live solutions at closure.

## Microsoft platform considerations

Licensing models, consumption metering, capacity allocations and the admin reporting available differ across Microsoft
365 Copilot, Copilot Studio, Power Platform, Foundry and Azure, and they change. Use the platform admin and cost reporting
the organisation already has, the CoE Starter Kit or Managed Environments where they help with inventory and usage, and
check each fact in `references/sources.md`. Licensing conclusions go to the Microsoft licensing guide or a licensing
partner.

## Adoption considerations

Assign licences in waves that follow readiness and launch plans, so cost tracks use. Report unused access at team level to
target support, never to identify individuals.

## Knowledge considerations

Knowledge owners' time is a real cost and usually the scarcest. Include content clean-up and review effort in the
capacity plan for every agent that grounds on owned knowledge.

## Security and privacy considerations

Cost and usage reports can reveal individual activity; aggregate them to solution, team or role level and restrict access.
Reviewer capacity is a security control in practice; never trim it to save money while release volume grows.

## Responsible AI considerations

Not applicable in depth, because budgeting does not decide about people; ensure responsible AI review capacity is funded
for any tier 3 and 4 work the charter includes, rather than squeezed by cost pressure.

## Evaluation requirements

Not applicable to the budget itself; evaluation effort (building evaluation sets, running regression after change) is
costed as part of each solution's delivery and run budget.

## Value measures

Track variance against baseline, forecast accuracy, consumption cost per solution alongside its value measure, and scarce
role over-commitment by month, reported at programme level by the AI Programme Manager with finance. Never report cost or
usage by individual.

## Scale notes

### Starter

A simple sheet of services, licences as advised and any consumption, reviewed monthly with the sponsor, and a list of the
three or four people whose time matters most, by role.

### Scale

A budget by cost type and month with finance, consumption budgets and alerts per solution, a monthly capacity plan for
scarce roles, and variance reporting to the board.

### Enterprise

Budgets per tranche and business unit, chargeback or showback of consumption where the organisation uses it, capacity
planning across programmes for shared reviewers, and portfolio-level cost visibility.

## Hand-offs

- To `programme-management:programme-health` for the cost and capacity dimensions of health.
- To `programme-management:supplier-management` where capacity gaps are met by suppliers.
- To `platform-governance:ai-licensing-and-capacity` for licensing and capacity questions.
- To `ai-foundry:foundry-cost-management` for cost optimisation inside a Foundry solution.

## Reviewer gates

Not applicable, because the budget releases no solution; it must fund the review capacity that `security-privacy`,
`evaluation-quality`, `responsible-ai` and `design-authority` need for the planned release volume.

## Failure modes

- Consumption costs are budgeted as fixed, and a successful agent breaks the budget.
- Licence figures are estimated from memory and prove wrong at renewal.
- Capacity planning counts makers but not business owners and reviewers, so releases queue at the gates.
- Unused licences are reported by person, and trust in the programme drops.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- State prices, licence terms, consumption rates or capacity limits from memory.
- Draw a licensing conclusion; route it to the Microsoft licensing guide or a licensing partner.
- Commit a scarce role beyond its declared time.
- Report cost, licence or usage data at individual level.

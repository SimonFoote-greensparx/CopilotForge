---
name: ai-licensing-and-capacity
description: Frames the licensing and capacity questions for Microsoft AI - who needs which kind of access, consumption-based usage, Dataverse and platform capacity, growth and cost owners - and gathers demand evidence for the Microsoft licensing guide or a licensing partner, never concluding itself. Use when a rollout or agent build raises licence or capacity questions, when consumption costs surprise budget holders, or before a renewal.
license: CC-BY-4.0
metadata:
  department: platform-governance
  lifecycle: Envision, Mobilise, Scale, Improve
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-studio, ai-foundry, power-platform, azure
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-overview, ms-copilot-studio-guidance, ms-managed-environments, ms-foundry-models, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# AI licensing and capacity

## Purpose

Licensing and capacity questions arrive at every stage of an AI programme, and the answers change often. This skill
does not answer them. It frames each question precisely, gathers the demand and usage evidence a licensing specialist
needs, records the answer with its source and date, and makes sure capacity and consumption have owners. That keeps
plans from being built on remembered licence terms. The work goes wrong when someone states a licensing conclusion
from memory, when consumption is switched on without a budget owner, and when capacity runs out because nobody watched
it.

## When to use

- A rollout, pilot or agent build raises the question of who needs which kind of access.
- Consumption-based costs for agents, flows or models are unknown or have surprised a budget holder.
- Dataverse, platform or model capacity is approaching limits, or nobody knows.
- A renewal or true-up is approaching and the organisation needs evidence of demand and use.
- A governance control depends on a feature whose licensing is unclear.

## When not to use

- Planning and tracking the programme budget and people capacity - use `programme-management:budget-and-capacity`.
- Managing model and platform cost for Foundry solutions - use `ai-foundry:foundry-cost-management`.
- Checking whether assigned Copilot licences are being used, as an adoption readiness question - use `copilot-adoption:adoption-readiness`.
- Building the funding case for the AI programme - use `ai-strategy:investment-case`.
- Watching consumption trends in operation - use `platform-governance:ai-admin-monitoring`.

## Questions to ask first

1. What exactly is being decided - access for a group of people, a consumption budget, capacity for an environment, or a renewal?
2. Which people, by role and number, need which capability, and how often will they use it?
3. Which solutions consume capacity or metered usage, and how will usage grow?
4. Who owns the budget for each consumption stream, and what alert threshold do they want?
5. When was the current answer last confirmed, and against which source?

## Required inputs

- The capability being planned (rollout wave, agent, flow, Foundry solution) and its audience by role and number.
- Current licence assignment and usage data at aggregate level.
- Capacity and consumption reports for environments and subscriptions.
- The organisation's agreements and contacts with its licensing partner, if any.

Where usage or growth is unknown, state assumptions as ranges and mark them "to confirm"; never present an estimate as
a measured figure.

## Decision framework

This skill routes rather than decides. Classify the question, then route it.

| Question type | What to gather | Routed to |
|---|---|---|
| Access for people (who needs what) | Roles, numbers, scenarios, frequency | Microsoft licensing guide or licensing partner |
| Consumption for agents, flows or models | Expected interactions, actions, model calls, growth, budget owner | Licensing partner, then cost owner for budget |
| Platform capacity (storage, environments) | Current use, growth, retention rules | Platform administrator, with licensing partner for entitlement |
| Feature entitlement for governance controls | Control needed, environments, users affected | Licensing partner |
| Renewal or true-up | Assignment, use, planned growth, unused access | Licensing partner and procurement |

Every answer is recorded with: the question, the evidence supplied, the answer, who gave it, the source and the date,
and the date it should be rechecked.

## Practitioner approach

Start by rewriting the question so a specialist can answer it. "Do we need licences for the agent?" becomes "Two
thousand staff in four roles will use a Copilot Studio agent in Teams about five times a week; it reads a SharePoint
library and creates tickets through a flow. What access and consumption arrangements apply, and what drives cost?" The
second version can be answered; the first invites a guess.

Gather demand evidence at role level. Use the scenario catalogue, adoption plans and solution briefs to estimate who
needs what and how often. Use current usage data, at aggregate level only, to show whether existing access is used. A
renewal argued from evidence goes better than one argued from enthusiasm.

Model consumption as drivers, not prices. For each solution, identify what drives metered use (conversations, actions,
model calls, retrieval, storage) and how it grows with adoption. Leave prices and rates to the licensing partner and
the source records. Give each consumption stream a budget owner and an alert threshold before it goes live.

Watch capacity. Environments, Dataverse storage and model quotas fill up as solutions grow, and logs and transcripts add
volume that nobody planned. Agree with the platform administrator who checks capacity, how often, and what happens at
thresholds.

Route and record. Send the framed question and evidence to the licensing guide or partner. Record the answer, its source
and date in a decisions log, and set a recheck date, because terms and product packaging change. Make sure plans cite
the log rather than restating the conclusion.

Feed decisions back. When a licensing answer changes a plan (a different rollout wave, a governance control that is not
available), tell the owners of the affected plans and update the platform strategy if needed.

Never let this skill become the source of licensing truth. Its value is in asking well, gathering evidence and making
sure answers are current and owned.

## Outputs

- A framed licensing and capacity question set, with demand evidence by role and solution.
- A consumption driver model per solution, with budget owners and alert thresholds.
- A licensing decisions log: question, evidence, answer, source, date and recheck date.
- A capacity watch list with owners and thresholds.

## Microsoft platform considerations

Microsoft changes licensing, packaging, consumption models, capacity entitlements and product names frequently, and
they vary by agreement. This skill never states them. Use `ms-copilot-overview`, `ms-copilot-studio-guidance`,
`ms-managed-environments` and `ms-foundry-models` only to understand what capability is being asked about, and route
every licensing conclusion to the Microsoft licensing guide or a licensing partner.

## Adoption considerations

Access decisions shape adoption. Make sure scenario and adoption evidence informs who gets access first, and that
unused access is followed up as an adoption question through `copilot-adoption` rather than simply withdrawn.

## Knowledge considerations

Not applicable to licensing questions themselves, because they concern access and consumption rather than content. Large
knowledge sources do drive storage capacity, which belongs on the capacity watch list.

## Security and privacy considerations

Not applicable to most licensing questions. Where a security or compliance control depends on an entitlement, record
the dependency so `security-privacy` reviewers know whether the control can be relied on.

## Responsible AI considerations

Not applicable to licensing directly. Access decisions should not exclude groups, such as frontline workers, from
capability without a reason the programme can explain.

## Evaluation requirements

Not applicable, because no AI output is produced. Check the decisions log for currency on its recheck dates.

## Value measures

Track decisions with a cited source and in-date recheck, consumption streams with budget owners and alerts, capacity
incidents, and the share of access in use at role level. The platform governance lead owns these, with finance for
budget measures, and takes the baseline from the first review.

## Scale notes

### Starter

Keep a short log of licensing questions and answers from the partner, and give any consumption a budget owner before it
is switched on.

### Scale

Add consumption driver models per solution, a capacity watch list and quarterly reviews ahead of renewal.

### Enterprise

Integrate with procurement and financial operations, allocate consumption to business units and run a standing
licensing review with the partner.

## Hand-offs

- To the Microsoft licensing guide or a licensing partner for every licensing conclusion.
- To `programme-management:budget-and-capacity` with costs and consumption owners.
- To `ai-foundry:foundry-cost-management` for Foundry solutions.
- To `platform-governance:ai-admin-monitoring` to watch consumption and capacity.

## Reviewer gates

Not applicable, because this skill frames questions and records answers rather than releasing solutions. Reviewer
departments such as `security-privacy` are told when a control they rely on depends on an unconfirmed entitlement.

## Failure modes

- A licensing conclusion stated from memory is built into a plan and turns out to be wrong.
- Consumption is switched on for an agent with no budget owner, and costs surprise finance months later.
- Storage fills with transcripts and logs nobody planned, and solutions fail.
- A renewal is negotiated without evidence of use, so unused access is renewed.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- State a licensing conclusion, price, entitlement or licence name as fact; route it to the licensing guide or a licensing partner.
- Switch on consumption without a budget owner and an alert threshold.
- Present an estimate of use as a measured figure.
- Use individual usage data to decide access; work at role level.

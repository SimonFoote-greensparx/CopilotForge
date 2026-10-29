---
name: ai-admin-monitoring
description: Sets up administrative monitoring of the AI estate - new and widely shared agents, policy and exception drift, orphaned solutions, unusual connector use, consumption and capacity trends - reported at estate, zone and business unit level, each signal with an owner. Use when governance relies on finding problems by accident, when the estate grows faster than reviews, or when steering asks what is happening across the platform.
license: CC-BY-4.0
metadata:
  department: platform-governance
  lifecycle: Assure, Measure, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: m365-copilot, m365-agents, copilot-studio, power-platform, purview, entra, azure
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-coe-starter-kit, ms-managed-environments, ms-copilot-studio-security-governance, ms-copilot-privacy, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# AI admin monitoring

## Purpose

Policies, zones and release rules only work if someone notices when the estate drifts from them. This skill sets up
administrative monitoring of the AI estate as a whole: what is being created and shared, where policy is being
stretched, which solutions have lost their owners, and how consumption and capacity are trending. Each signal has a
threshold, an owner and an action. Admin monitoring goes wrong when it becomes a dashboard nobody acts on, when it turns
into surveillance of individuals, and when it duplicates the operational monitoring of individual solutions.

## When to use

- Governance problems are found by accident rather than by monitoring.
- The number of agents and flows is growing faster than reviews can keep up.
- Steering or security asks what is happening across the AI estate.
- Policy exceptions, sharing limits or zones need checking in practice.
- Consumption or capacity needs regular watching.

## When not to use

- Monitoring one deployed solution's health, errors and quality - use `ai-operations:ai-solution-monitoring`.
- Reporting Copilot usage for adoption purposes - use `m365-copilot:copilot-usage-reporting`.
- Improving one Copilot Studio agent from its analytics - use `copilot-studio:studio-analytics`.
- Building the list of solutions and their owners - use `platform-governance:ai-solution-inventory`.
- Framing licensing questions - use `platform-governance:ai-licensing-and-capacity`.

## Questions to ask first

1. Which governance rules most need checking in practice - sharing, zones, connectors, ownership, release?
2. Which admin sources are available for each platform, and who has access?
3. Who will act on each signal, and how quickly?
4. What minimum group size applies to any reporting that could identify individuals?
5. What does steering need to see, and how often?

## Required inputs

- The inventory from `platform-governance:ai-solution-inventory`.
- The zoning plan, connector policy, maker rules and release policy to monitor against.
- Admin access or delegated reports for each platform.
- The organisation's policy on employee monitoring and reporting thresholds, agreed with HR and the DPO.

If the employee monitoring position is unclear, restrict reporting to estate and solution level until it is agreed;
never begin with individual-level reports.

## Decision framework

Monitor signals that lead to action. Each signal has a source, threshold, owner and action.

| Signal | Example threshold | Owner | Action |
|---|---|---|---|
| New solution shared beyond a team | Any, outside the release policy | Platform governance lead | Contact owner; register or restrict |
| Sharing reach increased | Audience crosses the tier boundary | CoE | Re-classify risk tier |
| Orphaned solution | Owner left or inactive past the agreed period | Platform governance lead | Transfer or retire |
| Connector or capability drift | Blocked capability used through exception or new connector | Security reviewer | Review exception or block |
| Exceptions past review date | Any | Policy owner | Renew or remove |
| Inactive solutions | No use past the agreed period | Solution owner | Confirm need or retire |
| Consumption trend | Above budget alert threshold | Budget owner | Review usage and budget |
| Capacity trend | Approaching agreed threshold | Platform administrator | Plan capacity or clean up |

Reporting levels: estate, zone, business unit and solution. Individual users never appear in reports; makers appear
only as owners of shared solutions, for follow-up, not for comparison.

## Practitioner approach

Start from the rules, not the reports. List the governance rules the organisation depends on and ask, for each, how a
breach would be noticed. The answer is often "it would not", and those gaps are where monitoring starts.

Find the sources. The Power Platform and Microsoft 365 admin centres, Copilot Studio views, the CoE Starter Kit, audit
logs and Azure monitoring each provide part of the picture. Check the current source records for what each exposes and
for how long data is retained.

Define a small set of signals, each with a threshold, an owner and an action. Eight good signals that are acted on
beat fifty that fill a dashboard. If nobody owns a signal, do not collect it yet.

Agree the reporting boundary before building anything. Admin data can identify individuals, and AI usage data is
sensitive. Report at estate, zone, business unit and solution level, above the agreed minimum group size. Owners of
shared solutions are contacted about their solutions; nobody is compared or ranked. Confirm the position with HR and
the DPO where employee monitoring rules apply.

Automate collection and alerting where possible, and route alerts to owners' existing queues rather than a new inbox.
Review the signals monthly with the CoE: what was found, what was done, and whether thresholds are right.

Summarise for steering quarterly: the size and shape of the estate, the share of shared solutions with owners and in
the right zone, policy drift and its resolution, and consumption and capacity trends. Pair the numbers with actions
taken.

Keep the boundary with operational monitoring clear. Admin monitoring watches the estate against governance rules;
`ai-operations:ai-solution-monitoring` watches each solution's health and quality. Share signals between them, such as a
solution whose errors rise after an ownership change, but do not merge them.

## Outputs

- An admin monitoring specification: signals, sources, thresholds, owners, actions and reporting levels.
- Alert routing to owners and a monthly signals review.
- A quarterly estate summary for steering.
- The agreed reporting boundary and minimum group size, recorded with HR and DPO input.

## Microsoft platform considerations

Admin centres, audit logs, Managed Environments reporting, Copilot Studio inventory, the CoE Starter Kit and Azure
monitoring each expose different data with different retention, and they change. Check `ms-coe-starter-kit`,
`ms-managed-environments`, `ms-copilot-studio-security-governance` and `ms-copilot-privacy` for current capability and
data handling.

## Adoption considerations

Monitoring that feels like surveillance damages the building culture. Tell makers what is monitored and why, emphasise
that it is about solutions and policy, and use findings to help owners rather than to reprimand them.

## Knowledge considerations

Not applicable to most signals, because they concern solutions and policy rather than content. Where knowledge sources
behind shared agents lose their owners, share the signal with `knowledge-management`.

## Security and privacy considerations

Admin data is itself sensitive. Restrict access, agree retention, and share security-relevant signals (connector drift,
exceptions, unusual sharing) with the `security-privacy` reviewers. Employee monitoring positions are confirmed with the
DPO and HR.

## Responsible AI considerations

Monitoring must not become a way to assess people. Report at group level above the minimum size, and route any request
for individual-level data to the DPO and HR, who will usually decline it.

## Evaluation requirements

Not applicable to solution quality, which is evaluated elsewhere. Test the monitoring itself by planting a known breach,
such as an unregistered shared test agent, and confirming the signal fires and reaches its owner.

## Value measures

Track the median time from breach to detection and to resolution, signals with owners, and the trend in shared
solutions outside policy. The platform governance lead owns these measures, with a baseline from the first month of
monitoring.

## Scale notes

### Starter

A monthly look at the admin centres for new shared agents, orphans and capacity, with a short note to the CoE, is a
good start.

### Scale

Automate the core signals, route alerts to owners and hold a monthly signals review with a quarterly steering summary.

### Enterprise

Integrate with security operations and service management, federate signals to business units and track resolution
times as governance performance measures.

## Hand-offs

- To `platform-governance:ai-release-policy` and `opportunity-management:risk-classification` when reach crosses a tier boundary.
- To `ai-operations:ai-solution-retirement` for inactive or orphaned solutions.
- To `platform-governance:ai-licensing-and-capacity` for consumption and capacity trends.
- To `security-privacy:connector-review` for connector drift on tier 2 and above solutions.

## Reviewer gates

Not applicable as a release gate, because monitoring operates after release. The reporting boundary and access to admin
data are agreed with `security-privacy` before monitoring begins.

## Failure modes

- A detailed dashboard is built and nobody acts on its signals.
- Admin data is used to compare individual makers or users, and trust in the programme collapses.
- Signals are routed to a shared inbox nobody reads.
- Admin monitoring duplicates solution monitoring and both teams assume the other will act.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Report, rank or compare individual users or makers.
- Collect a signal that has no owner and no action.
- Begin individual-level reporting without agreement from the DPO and HR.
- Treat a dashboard as monitoring without alert routing and follow-up.

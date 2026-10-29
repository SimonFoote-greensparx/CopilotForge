---
name: copilot-usage-reporting
description: Sets up and interprets Microsoft's Copilot usage reports and dashboards responsibly - who may access them, privacy and name-concealment settings, minimum group sizes, what each metric can and cannot show - and produces aggregate team or role reports with stated caveats. Use when usage reports are being switched on or shared, when a sponsor asks for usage figures, or when someone asks to see individual activity.
license: CC-BY-4.0
metadata:
  department: m365-copilot
  lifecycle: Measure, Improve
  maturity: adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: m365-copilot, copilot-chat, m365-agents
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-adoption-hub, ms-copilot-overview, ms-copilot-privacy, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# Copilot usage reporting

## Purpose

Microsoft provides usage reports and dashboards for Copilot, and they are useful for steering a rollout. They also
contain activity data about named people, which makes them easy to misuse. This skill configures access and privacy
settings, agrees the rules for who sees what at which level of aggregation, explains what each metric can and cannot
tell you, and produces aggregate reports that help the programme decide. It goes wrong when reports are switched on
with default access, shared as screenshots with names visible, or read as proof of value when they only show activity.

## When to use

- Copilot usage reports or dashboards are being enabled, or access to them is being granted.
- A sponsor, programme board or business unit asks for Copilot usage figures.
- Someone asks to see which individuals are or are not using Copilot.
- Usage figures are being used to argue about value, licence allocation or performance.

## When not to use

- Designing the overall adoption measurement framework across usage, capability, behaviour and outcomes - use `copilot-adoption:adoption-measurement`.
- Linking usage indicators to benefits - use `value-realisation:adoption-to-value-metrics`.
- Admin monitoring of the whole AI estate, including agents and flows - use `platform-governance:ai-admin-monitoring`.
- Measuring a specific agent's value - use `m365-agents:agent-value-measurement`.
- Measuring the health of the Champions programme - use `champions:champion-metrics`.

## Questions to ask first

1. Which reports and dashboards are in use or planned, and who currently has access to them?
2. What have the data protection lead, HR and any employee representatives agreed about usage data, and is it written down?
3. What minimum group size will the organisation report at, and are name-concealment or pseudonymisation settings applied?
4. Who receives usage reports, and what decision will each audience make with them?
5. What baseline and context (licences assigned, waves, scenarios launched) are needed to read the figures fairly?

## Required inputs

- A written position from the data protection lead and HR on the use of Copilot usage data.
- The list of current report and dashboard users and their roles.
- The current privacy and access settings, from the admin who owns them.
- The rollout plan, so figures can be read against waves and scenarios.
- The adoption measurement framework, if one exists.

If there is no written data protection position, restrict reports to the smallest administrative group and agree the
position before sharing anything. Never assume a report's privacy settings; check them.

## Decision framework

| Question | Rule |
|---|---|
| Who may access raw reports? | A small named administrative group with a documented need, reviewed periodically |
| At what level are results shared? | Team, role, business unit or wave, at or above the agreed minimum group size |
| Are names visible? | Concealed or pseudonymised wherever the tool allows, unless the data protection lead has approved a specific exception |
| Can reports be used about individuals? | No, for performance, conduct or ranking; any licence-administration use follows a separate agreed policy |
| What does a metric show? | Activity only; value needs outcome measures from the adoption or value framework |
| What accompanies every report? | Definitions, date range, population, caveats and the decision it supports |

A request that breaks a rule is declined with a reason and redirected to the aggregate alternative.

## Practitioner approach

Start with governance before any number is shared. Meet the data protection lead and HR, explain what the reports
contain, and agree the purpose, access, minimum group size and the uses that are not allowed. Write this down and share
it with the people who will see the reports. In many organisations, employee representatives should be told as well;
trust is easier to keep than to rebuild.

Then configure the tools. List every report and dashboard, who has access and how that was granted, and reduce access to
the agreed group. Apply name concealment or pseudonymisation where the tools offer it, and confirm the current options in
the source records and admin documentation, because these settings change. Record the configuration and the date
checked.

Learn what each metric means before reporting it. Usage reports typically count activity such as people who used
Copilot in a period, or actions in particular apps. They do not show whether the work improved. Read the definitions, note
the reporting lag and the population, and check how figures behave when licences are added mid-period. Write a short
definitions sheet for report readers.

Build reports around decisions. A rollout owner needs uptake by wave and app to target support; a sponsor needs a
trend in context alongside outcome evidence; a business unit lead needs their teams' position against the organisation.
Aggregate to the agreed minimum, show trends rather than league tables, and attach definitions and caveats to every page.
Avoid ranking teams against each other in ways that encourage pressure on individuals.

Handle requests for individual data calmly and consistently. Explain the agreed position, ask what decision the
requester is trying to make, and offer the aggregate view that supports it. Licence reallocation is the most common
reason; route it to the policy agreed in `m365-copilot:m365-copilot-rollout`.

Review the setup each quarter: access list, settings, definitions and whether reports are being used for the decisions
they were built for.

## Outputs

- A usage reporting governance note: purpose, access, minimum group size, privacy settings, prohibited uses and approvals.
- A configuration record for each report and dashboard with access and settings, and the date checked.
- A metric definitions sheet with caveats.
- Recurring aggregate usage reports by wave, team or role, each with definitions and the decision it supports.

## Microsoft platform considerations

Copilot usage reporting is available through Microsoft 365 admin reporting and Microsoft's Copilot analytics and
dashboard experiences; their names, metrics, privacy options and licensing change frequently. Check the current source
records (`ms-copilot-adoption-hub`, `ms-copilot-overview`) and the admin documentation before configuring or explaining a
report, and do not assert what a metric measures from memory.

## Adoption considerations

Aggregate usage helps the adoption team target support, scenarios and communications where uptake is low. Share it with
Champions and managers in a way that prompts help, not pressure. Report trends alongside stories and outcome evidence
from `copilot-adoption:adoption-measurement`.

## Knowledge considerations

Not applicable, because usage reporting concerns activity data rather than knowledge content; knowledge gaps revealed by
agent questions are handled by `knowledge-management:knowledge-gap-analysis`.

## Security and privacy considerations

Usage reports contain personal data about employees' activity. Access, purpose, retention and sharing must follow the
data protection position agreed with the data protection lead; `ico-ai-data-protection` describes the regulator's view
for UK organisations. Questions on lawfulness, transparency to staff or employee consultation go to the data protection
lead, legal adviser and HR.

## Responsible AI considerations

Usage data must not inform decisions about individuals' performance, pay, conduct or progression. Reports that could be
read that way are redesigned before release.

## Evaluation requirements

Before the first report is shared, check it with the data protection lead against the governance note: aggregation,
concealment, definitions and caveats. Re-check after any tool or setting change.

## Value measures

The skill's own measure is whether reports are used for the decisions they support, with no privacy incidents. Report
the share of report recipients with a documented need and the number of individual-data requests declined and
redirected. The adoption lead owns these measures.

## Scale notes

### Starter

One administrator with access, concealment applied, a monthly aggregate summary for the sponsor and a one-page
governance note.

### Scale

A small reporting group, a definitions sheet, wave and business-unit reports, and a quarterly access review.

### Enterprise

Central governance with regional data protection input, standardised aggregate reports across business units, and
reporting linked to the value dashboard.

## Hand-offs

- To `copilot-adoption:adoption-measurement` for the wider measurement framework.
- To `value-realisation:adoption-to-value-metrics` for linking usage to benefits.
- To `m365-copilot:m365-copilot-rollout` for licence allocation decisions under the agreed policy.
- To `platform-governance:ai-admin-monitoring` for estate-wide administrative monitoring.

## Reviewer gates

From risk tier 1, the governance note and any change to access or concealment settings are reviewed by
`security-privacy`, which classifies findings as blocking or advisory. A blocking finding stops report sharing until
fixed.

## Failure modes

- Reports are shared with names visible, and staff learn that their activity is being watched.
- Activity figures are presented as value, and the programme is judged on the wrong evidence.
- Managers use team league tables to pressure individuals, and trust falls.
- Settings change after a product update and concealment is silently lost.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Share or produce usage data about named individuals for performance, conduct or ranking.
- Report below the agreed minimum group size.
- Present activity metrics as evidence of value on their own.
- Configure or describe a report from memory without checking current settings and definitions.

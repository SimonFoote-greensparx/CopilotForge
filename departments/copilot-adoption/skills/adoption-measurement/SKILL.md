---
name: adoption-measurement
description: Defines how Copilot adoption is measured across usage, capability, behaviour change and business outcomes, with baselines set before launch, team or role-level reporting above a minimum group size, and feedback loops that change the programme. Use when setting adoption measures, when a sponsor asks whether Copilot is working, or when someone proposes tracking individual usage.
license: CC-BY-4.0
metadata:
  department: copilot-adoption
  lifecycle: Discover, Measure, Improve
  maturity: adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, copilot-cowork
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-adoption-hub, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Adoption measurement

## Purpose

This skill sets up measurement that tells a sponsor whether Copilot adoption is creating value, and tells the
adoption team what to change. It measures four layers: usage, capability, behaviour change and outcomes, each with a
baseline taken before launch. Measurement usually goes wrong in two ways: it stops at counting active users, which
says nothing about value, or it drifts into monitoring individuals, which destroys trust and may breach employment and
data protection obligations.

## When to use

- Before launch, to agree what will be measured, the baselines and how results will be reported.
- When a sponsor or board asks whether Copilot is "working" and the only evidence is licence counts.
- When usage figures look healthy but nobody can say what has changed in the work.
- When someone proposes dashboards of individual usage, and the request needs redirecting.

## When not to use

- Assessing readiness, including licences assigned versus used as a readiness signal - use `copilot-adoption:adoption-readiness`.
- Finding the scenarios whose outcomes will be measured - use `copilot-adoption:scenario-discovery`.
- Measuring the health and contribution of a Champions programme - use `champions:recognition-and-progression`.
- Financial benefits cases, return on investment and benefit owner models - the `value-realisation` department (planned).
- Measuring the quality of a specific agent or solution - the `evaluation-quality` department (planned).

## Questions to ask first

1. What outcome did the sponsor say Copilot should help achieve, and how is that outcome measured today?
2. Which teams and roles are in scope, and what is the smallest group size the organisation will report on?
3. What baseline data exists now, before launch, for the priority scenarios?
4. Who will receive the results, and what decisions will they make with them?
5. What have the data protection lead, HR and employee representatives agreed about collecting and using usage data?

## Required inputs

- The sponsor's stated outcome and the readiness baseline from `copilot-adoption:adoption-readiness`.
- Priority scenarios with their owner-agreed baselines from `copilot-adoption:scenario-discovery`.
- The organisation's agreed minimum reporting group size and its position on usage data, from the data protection lead and HR.
- Available usage reporting, confirmed by IT, and any survey tools the organisation already uses.

If no minimum group size has been agreed, propose one, record it as "to confirm" with the data protection lead, and do
not publish any results until it is agreed. Never invent baselines; a missing baseline is recorded as missing.

## Decision framework

Measure all four layers, and do not claim value from the first layer alone.

| Layer | What it shows | Typical measures | Source |
|---|---|---|---|
| Usage | Whether people are using Copilot at all | Active users as a share of licensed users; breadth of apps used | Organisation's usage reporting, aggregated |
| Capability | Whether people can use it well and safely | Self-assessed confidence; scenarios people report using; Champion community size, milestone conversion and reusable assets at programme level | Short pulse surveys, Champion programme data |
| Behaviour change | Whether ways of working have shifted | Share of teams using priority scenarios routinely; verification habits reported | Team surveys, manager check-ins, sampling |
| Outcomes | Whether the work is better | Time to complete, delay, rework or quality for priority scenarios against baseline | Owner-led sampling and existing business measures |

Reporting rules that apply to every layer:

| Rule | Requirement |
|---|---|
| Level | Team, role, persona or business unit; never named individuals |
| Minimum group size | Suppress any group below the agreed minimum, and combine small groups |
| Purpose | Improve the programme and support teams; never assess individual performance |
| Access | Results go to the sponsor, adoption team and team leads; raw data stays with its owner |

## Practitioner approach

Start with the decision the measures must support. A sponsor deciding whether to expand to the next business unit
needs different evidence from an adoption lead deciding which scenarios to refresh. Write down the two or three
decisions measurement will inform, and design backwards from them. Measures that inform no decision should be dropped.

Take baselines before launch, because they cannot be reconstructed afterwards. For each priority scenario, agree with
the business owner a simple baseline: how long the task takes, how often it is late, or how much rework it needs.
Sampling a few teams is enough; precision matters less than having a credible starting point the owner accepts.

Agree the people rules early and in writing. Meet the data protection lead and HR, and employee representatives where
they exist, to agree the minimum reporting group size, the purposes for which usage data may be used, and who can see
what. Make it explicit that adoption data will not be used to judge individual performance. Publishing this position
to staff builds the trust that honest survey answers depend on.

Build the measures layer by layer. Usage comes from the organisation's own reporting, aggregated by team or role.
Capability comes from short pulse surveys and, at programme level, from the Champions programme: how many people
have joined, how many have moved through each verified capability, and how many reusable assets they have produced.
Take these as aggregates from `champions:recognition-and-progression`, never from the tracker's individual rows. Behaviour change is
best seen through simple questions to teams and managers about which scenarios have become routine. Outcomes come from
the owner's sampling against the baseline, or from business measures the organisation already tracks.

Design the feedback loop alongside the measures. Every reporting cycle should end with actions: scenarios to refresh,
teams to support, guidance to clarify, knowledge to fix. Publish a short "you said, we did" note so people see their
feedback used. Review the measures themselves every few months and retire any that no longer inform a decision.

Present results honestly. Report what is not working as clearly as what is, show trends rather than single points,
and state the limits of the evidence. Low usage in a team is a prompt to ask what is missing, usually scenarios,
manager support or relevant knowledge, not a reason to name the team in a league table.

## Outputs

- A measurement plan in the measurement section of the `adoption-plan` template: decisions supported, measures by layer, baselines, sources, owners, reporting rhythm and the agreed minimum group size.
- An adoption scorecard on the `coe-kpi-scorecard` template, reporting at team or role level only.
- A written statement of the people rules for adoption data, agreed with the data protection lead and HR.
- A feedback loop with a review rhythm and a published "you said, we did" summary.

## Microsoft platform considerations

Microsoft provides usage reporting for Copilot through its admin and analytics tools, and the options, metrics and
privacy settings change over time. Check `references/sources.md` for what is currently available, and confirm with IT
which reports the organisation has enabled and how they aggregate data. Prefer aggregated, de-identified views.

## Adoption considerations

Measurement is itself an adoption intervention: what you measure tells people what matters. Measuring only usage
encourages shallow use; measuring scenarios, verification and outcomes encourages good use. Share results with teams in
ways that help them, not rank them.

## Knowledge considerations

Not applicable as a primary concern, because measurement does not depend on grounding content. Where feedback shows
answers failing because of poor knowledge, record it and pass it to the `knowledge-management` department (planned).

## Security and privacy considerations

Usage data is personal data. Collect only what the agreed purposes need, aggregate before sharing, suppress groups
below the minimum size, restrict access to raw data, and set a retention period. Survey comments can identify people
in small teams; review them before publishing. Data protection questions end with the organisation's DPO.

## Responsible AI considerations

Never use adoption data to make or inform decisions about an individual's performance, pay or prospects. Be wary of
targets that pressure people to use Copilot where it does not help; high usage is not a goal in itself.

## Evaluation requirements

Not applicable as solution evaluation, because this skill measures adoption rather than testing an AI solution. The
measurement plan is checked by confirming each measure has a baseline, a source, an owner and a decision it informs.

## Value measures

This skill defines value measures for adoption. Its own success is that the sponsor makes expansion and investment
decisions using the four-layer evidence, owned by the adoption lead and reviewed each reporting cycle.

## Scale notes

### Starter

Three or four measures: share of licensed people active, a short quarterly pulse survey, and one or two scenario
outcomes sampled by the owner. Report the whole organisation as one group if teams are below the minimum size.

### Scale

Measures by business unit and persona, a regular scorecard to the sponsor and CoE, and a quarterly review of the
measures themselves.

### Enterprise

A governed adoption measurement framework aligned with the CoE scorecard and value realisation, with formal agreement
from data protection, HR and works councils where applicable, and consistent suppression rules across regions.

## Hand-offs

- To `ai-centre-of-excellence:coe-operating-model` so adoption measures feed the CoE scorecard and portfolio decisions.
- To `copilot-adoption:launch-plan` with findings that should change the next wave.
- To `copilot-adoption:scenario-discovery` when scenarios need refreshing.
- To `champions:recognition-and-progression` with team-level adoption indicators for the Champions health check.
- To the `value-realisation` department (planned) for financial benefit and return on investment work.

## Reviewer gates

From risk tier 0, `security-privacy` reviews the measurement plan before any usage data is collected, looking for
purpose limitation, aggregation, the minimum group size, access restrictions and retention. Reporting individual-level
usage is a blocking finding.

## Failure modes

- Only active users are counted, and the programme declares success while nothing in the work has changed.
- Baselines are not taken before launch, so outcome claims cannot be supported later.
- Usage dashboards drift into individual-level views, trust collapses and survey answers stop being honest.
- Small teams are reported separately, making individuals identifiable.
- Adoption gains in teams with Champions are claimed as caused by the Champions, without evidence beyond correlation.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Monitor, rank or report the usage of named individuals.
- Publish results for a group smaller than the agreed minimum size.
- Claim business value from usage figures alone.
- Invent baselines or present estimates as measured results.

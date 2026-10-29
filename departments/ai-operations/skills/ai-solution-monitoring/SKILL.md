---
name: ai-solution-monitoring
description: Sets up operational monitoring for each live agent or AI solution - availability and errors, failed actions, usage by team, sampled answer quality, safety triggers, feedback, knowledge freshness and consumption - with thresholds, alert routing to named roles and a review rhythm. Use when a solution goes live, when users find failures before the owners do, or when alerts are so noisy that everyone ignores them.
license: CC-BY-4.0
metadata:
  department: ai-operations
  lifecycle: Launch, Measure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, power-platform, azure
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, evaluation-quality
  sources: ms-copilot-studio-guidance, ms-managed-environments, ms-coe-starter-kit, ms-foundry-models, ms-copilot-privacy, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI solution monitoring

## Purpose

A live AI solution can fail loudly, by going down or failing an action, or quietly, by answering worse than it did at
release. This skill sets up monitoring for each solution that catches both: technical signals such as availability,
errors and failed actions, and quality signals such as sampled answer quality, safety triggers, negative feedback and
stale knowledge, each with a threshold, a named role who receives the alert and a rhythm for looking at the trends.
Monitoring usually fails in one of two ways: only technical signals are watched, so quality decay goes unnoticed, or
every signal raises an alert and the owners learn to ignore them all.

## When to use

- A solution is about to go live and needs monitoring that matches its risk tier.
- Users are discovering failures before the solution owner does.
- Alerts exist but are so frequent or vague that nobody acts on them.
- A solution's quality seems to have drifted since release and nobody can show it.
- Several solutions are live and need a consistent monitoring baseline.

## When not to use

- Estate-wide admin monitoring of AI usage, agents and makers across the tenant - use `platform-governance:ai-admin-monitoring`.
- Designing telemetry and logging inside a pro-code solution - use `ai-engineering:ai-telemetry`.
- Tracing and observability setup for Microsoft Foundry agents - use `ai-foundry:foundry-observability`.
- Monitoring Power Automate flows that are not part of an AI solution - use `automation:automation-monitoring`.
- Measuring adoption and business value - use `copilot-adoption:adoption-measurement` or `value-realisation:value-dashboard`.

## Questions to ask first

1. What failures would hurt users or the business most, and how quickly must someone know about each?
2. Which signals does the chosen route expose today, confirmed in the current source records, and which would need building?
3. Who receives each alert, are they able to act on it, and what do they do first?
4. How will answer quality be sampled in live use, by whom and how often?
5. What usage data may be collected and reported, at what group size, as agreed with privacy and HR?

## Required inputs

- The support plan with named roles from `ai-operations:ai-support-model`.
- The release evidence, including the monitoring baseline, known limits and quality thresholds from `evaluation-quality:ai-release-evidence`.
- The solution's dependencies: knowledge sources, connectors, flows, models and environments.
- The organisation's agreed rules on usage data and minimum reporting group size.

Where no quality baseline exists from release, monitoring can still watch technical signals; mark quality monitoring
as "to confirm" and set a baseline from the first weeks of sampling before relying on trends.

## Decision framework

Choose signals by category and set the minimum by tier.

| Category | Example signals | Tier 1 | Tier 2 | Tier 3 and 4 |
|---|---|---|---|---|
| Availability and errors | Solution unavailable, error rates, timeouts | Owner notices via users | Alert to support | Alert with out-of-hours route where agreed |
| Actions | Failed or retried actions, unexpected volumes of writes | Not usually applicable | Alert on failure | Alert on failure and unusual volume |
| Usage | Conversations or tasks by team, trend over time | Monthly look | Monthly report | Weekly report |
| Quality | Sampled answers scored against the rubric, refusal and escalation rates | Owner spot check | Scheduled sample | Scheduled sample plus triggers for re-evaluation |
| Safety | Content control triggers, reported harmful outputs | Report route | Alert on any report | Alert on any trigger pattern and any report |
| Feedback | Negative ratings and comments | Monthly look | Weekly triage | Weekly triage with trend alert |
| Knowledge freshness | Sources past review date, broken or moved sources | Review date | Alert on overdue or broken source | Alert plus regression trigger |
| Consumption | Capacity or consumption against plan | Not usually applicable | Monthly | Alert on unexpected change |

For each signal, record the threshold, the receiving role, the first action and the escalation. A signal without a
first action is a report, not an alert.

## Practitioner approach

Start from failure, not from the dashboard. List the ways the solution could hurt users or the business - stops
answering, acts wrongly, answers from stale policy, produces something harmful - and for each, decide how fast someone
must know. That sets which signals become alerts and which become trends to review.

Inventory what the route provides before building anything. Copilot Studio, Agent Builder, Microsoft Foundry and Power
Platform expose different analytics, logs and admin reports, and these change. Confirm current capabilities in the
source records, use what exists, and build only the gaps that matter for the tier.

Monitor quality deliberately, because no technical signal shows it. Sample live answers on a schedule, score them with
the rubric used at release, and compare with the release baseline. Watch proxy signals too: rising refusal rates,
rising escalation to humans, falling satisfaction or a spike in a feedback category. Set a trigger that sends the
solution back to `evaluation-quality:regression-evaluation` when quality falls beyond the agreed tolerance.

Watch dependencies. Many AI failures are caused by something else changing: a knowledge library moved, a connector's
credentials expired, a flow was edited, a Microsoft platform update arrived. Monitor the dependencies that the
solution's runbook lists, and track platform announcements the organisation follows.

Design alerts for the people receiving them. Each alert names the solution, the signal, the threshold crossed and the
first action, and goes to a role that can act. Start with few alerts and tune them over the first weeks; an alert that
fires daily and is ignored is worse than none. Route anything suggesting harmful output or exposure of restricted
content directly to the incident route.

Respect people in usage data. Report usage by team or role above the agreed minimum group size, never by named user,
and agree the reporting rules with privacy and HR before collecting anything beyond what the platform reports by default.

Set a review rhythm: the solution owner looks at trends on a regular cycle proportionate to tier, and the review
calendar brings the trends to each scheduled review. Record decisions taken from monitoring, so it visibly drives action.

## Outputs

- The monitoring section of the `support-and-monitoring-plan`: signals, thresholds, receiving roles, first actions, escalation and review rhythm.
- A quality sampling plan with the rubric version and baseline it compares against.
- A dependency watch list taken from the solution runbook.
- Re-evaluation triggers handed to `evaluation-quality:regression-evaluation`.

## Microsoft platform considerations

Analytics and monitoring differ by route: Copilot Studio analytics, admin reporting in the Microsoft 365 and Power
Platform admin centres, Managed Environments features and Microsoft Foundry observability. Availability, retention and
detail change frequently, so confirm them in `ms-copilot-studio-guidance`, `ms-managed-environments`, `ms-foundry-models`
and `ms-coe-starter-kit`, and check what conversation data is retained in `ms-copilot-privacy` before relying on it.

## Adoption considerations

Falling usage in a team is often the first sign of a quality problem or a missed communication. Look at usage trends
alongside feedback, and talk to the team before drawing conclusions.

## Knowledge considerations

Knowledge freshness is a monitored signal. Sources past their review date or recently moved should alert the solution
owner and prompt `ai-operations:knowledge-refresh`.

## Security and privacy considerations

Monitoring data can include users' questions and answers. Agree with `security-privacy` what is collected, who can see
it and how long it is kept, aligned with `security-privacy:ai-interaction-retention`. Signals suggesting exposure of
restricted content go straight to incident handling.

## Responsible AI considerations

Monitoring must never become surveillance of individuals. Report at team or role level, be transparent with users about
what is monitored, and include signals for harm to people, such as complaints from affected people, where the solution
affects them.

## Evaluation requirements

Live quality sampling uses the rubric and baseline from release evaluation. Quality falling beyond tolerance triggers
`evaluation-quality:regression-evaluation`; sampled failures become candidate golden dataset items.

## Value measures

Track the share of issues detected by monitoring before users reported them, time from alert to action, alert volume
per solution, and solutions with a current quality sample. The AI Operations Lead owns these measures; report by
solution and team, never by individual user.

## Scale notes

### Starter

The owner checks the route's built-in analytics monthly, reads feedback, spot-checks a few answers, and has a clear
user route to report problems.

### Scale

A standard monitoring baseline per tier across solutions, alerts routed into the service desk, scheduled quality
sampling and a dependency watch list per solution.

### Enterprise

Central monitoring for tier 3 and 4 solutions with out-of-hours routes where agreed, portfolio dashboards of quality and
reliability trends, and monitoring linked to the solution inventory and incident management.

## Hand-offs

- To `ai-operations:ai-support-model` and `ai-operations:ai-incident-management` with alert routes.
- To `evaluation-quality:regression-evaluation` when quality triggers fire.
- To `ai-operations:knowledge-refresh` for stale or broken sources.
- To `ai-operations:ai-review-calendar` with trends for each scheduled review.

## Reviewer gates

From risk tier 2, `security-privacy` reviews what monitoring data is collected and retained, and `evaluation-quality`
confirms that live quality sampling uses the release rubric and baseline. Gaps found are recorded as blocking or
advisory by those reviewers.

## Failure modes

- Only uptime is monitored, so answer quality decays for months without anyone noticing.
- Every signal is an alert, and the alerts are ignored.
- A knowledge library moves, the agent loses its grounding and nobody is told.
- Usage reports name individuals, and trust in the solution and the programme is damaged.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Report or alert on usage by named individual.
- Rely on technical signals alone for a solution whose risk lies in answer quality.
- Create an alert that has no receiving role and no first action.
- Assume a platform analytics feature or retention period without checking the current source.

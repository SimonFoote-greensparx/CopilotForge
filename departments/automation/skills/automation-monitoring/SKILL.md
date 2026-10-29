---
name: automation-monitoring
description: Designs monitoring for an individual automation before hand-over - run failures, missing runs against expected volume, exception queue ageing, AI step quality signals such as low confidence and human override rates, connection expiry - and routes each alert to a named owner. Use when an automation is about to go live, when flows stop without anyone noticing, or when an owner asks what to watch.
license: CC-BY-4.0
metadata:
  department: automation
  lifecycle: Deliver, Launch, Measure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: power-platform, copilot-studio, ai-foundry, azure
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-coe-starter-kit, ms-managed-environments, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# Automation monitoring

## Purpose

The most damaging automation failures are silent: a flow that stopped triggering, a connection that expired, an AI step
whose accuracy slid as inputs changed, or an exception queue nobody has opened for a fortnight. This skill designs the
monitoring for a specific automation before it is handed over, so that each of these is noticed by a named owner within
a time the process can tolerate. It goes wrong when monitoring means "the maker gets an email on failure", when nothing
watches for runs that did not happen, and when AI quality is never measured once the flow is live.

## When to use

- An automation is approaching go-live and its monitoring and alerting have not been designed.
- A flow stopped running and nobody noticed until the business complained.
- An automation with AI steps is live, and the owner wants to know whether its accuracy is holding.
- Alerts go to a maker who has moved on, or to a mailbox nobody reads.
- The automation is being handed from the build team to an operating team.

## When not to use

- Running operational monitoring across the live AI estate as a service - use `ai-operations:ai-solution-monitoring`.
- Admin-level monitoring of usage, makers and the platform estate - use `platform-governance:ai-admin-monitoring`.
- Designing failure handling inside the flow - use `automation:exception-handling`.
- Measuring the business value delivered - use `automation:automation-value`.
- Telemetry design for pro-code AI services - use `ai-engineering:ai-telemetry`.

## Questions to ask first

1. How many runs should happen in a normal hour, day or week, and how long can a gap go unnoticed before it hurts?
2. Who owns the automation technically and who owns the business process, and how do they want to be alerted?
3. Which AI steps exist, and what signals would show their quality is slipping?
4. Which connections, credentials and certificates will expire, and when?
5. Who reads the exception queue, and how old can an item get before it matters?

## Required inputs

- The automation design, including AI step thresholds, review points and exception catalogue.
- Expected volumes and timing, from the assessment or early runs.
- Named technical and business owners, with agreed alert routes and working hours.
- The run log produced by the flow (item key, AI result, confidence, decision, outcome) from `automation:flow-design-patterns`.

If the flow does not write a run log, monitoring of AI quality is not possible; send it back to build. If owners are not
named, the automation is not ready for go-live.

## Decision framework

Design at least one signal in each row that applies. Each signal has a threshold, an owner and a response.

| Signal | Detects | Typical threshold | Alert to |
|---|---|---|---|
| Run failure | Flow or desktop flow failed | Any failure on tier 2 and above; rate above baseline below that | Technical owner |
| Missing runs (heartbeat) | Trigger stopped, connection broken, upstream change | Fewer runs than the expected minimum for the period | Technical owner |
| Exception queue age | Items not worked | Oldest item older than the agreed response time | Business owner |
| AI validation failure rate | Inputs or model behaviour changed | Rate above the level seen in testing | Technical and business owner |
| Low confidence rate | Inputs drifting from what the model handles | Rate above baseline for a sustained period | Business owner |
| Human override rate | AI results reviewers reject or amend | Rate above the level agreed at go-live | Business owner |
| Connection and credential expiry | Approaching expiry or revoked access | Warning ahead of expiry | Technical owner |
| Run cost or consumption | Unexpected volume or loops | Above budgeted range | Technical owner |

Thresholds come from testing and early live runs, agreed with the owners, and are reviewed after the first month.

## Practitioner approach

Start from what would hurt. Ask the business owner what failure would cost them most: a missed invoice, a customer not
answered, a duplicate payment. Work back to the signal that would show it early. This keeps monitoring focused on the
process rather than on every technical event.

Watch for absence as well as failure. Platforms tell you when a run fails; they do not tell you when it never started.
A heartbeat check compares actual runs against the expected minimum for the period and alerts when the gap is too
large. This catches broken triggers, revoked connections and upstream changes that send nothing.

Monitor AI quality from the run log. Because AI steps degrade gradually rather than failing outright, look at rates over
time: the share of results failing validation, falling below the confidence threshold, or rejected and amended by
reviewers. Agree a baseline from testing and early live weeks, and alert on sustained movement rather than single items.
A rising override rate is the earliest reliable sign that the inputs or the model have changed; it should prompt a
re-test against the evaluation sample, not a quiet threshold change.

Make every alert actionable. Each alert names what happened, which automation, the affected items and a link to where
the owner acts. Send technical alerts to the technical owner's team channel or service queue, and business alerts to
the business owner's queue. Avoid individual inboxes, which fail when people are away or leave. Agree working hours and
what happens out of hours for business-critical automations.

Keep noise low. An alert that fires daily and is always ignored trains people to ignore the one that matters. Start with
a few high-value signals, tune thresholds after the first month, and remove alerts nobody acts on.

Track expiry. List every connection, credential and certificate with its expiry date and send a warning well ahead of
it. Expired credentials are among the most common and most avoidable causes of automation outages.

Document the monitoring in the runbook: signals, thresholds, owners, response expected and how to pause the automation
safely. Hand over formally to the operating team, and record the automation in the solution inventory with its owners.

## Outputs

- A monitoring specification per automation: signals, thresholds, owners, alert routes, response expected and review date. It forms the monitoring section of the `automation-design` template.
- A runbook section on alerts, safe pause and restart.
- An expiry register for connections, credentials and certificates.
- A hand-over record to the operating team.

## Microsoft platform considerations

Power Automate run history, flow analytics, failure notifications and admin analytics, the CoE Starter Kit's monitoring
components, and logging to Azure services can all feed monitoring; Managed Environments add estate-level insights. What
each provides changes; confirm current capabilities in `references/sources.md` before designing around one, and prefer
the run log the flow writes for AI quality signals.

## Adoption considerations

Owners must want to receive alerts. Agree the routes and volume with them, show them an example alert before go-live
and review the first month together. Alerts that feel like noise are switched off quietly.

## Knowledge considerations

Not applicable to most monitoring, because it watches runs rather than knowledge. Where an AI step depends on reference
lists or category definitions, alert when those sources change so the step can be re-tested.

## Security and privacy considerations

Run logs and alerts should carry item keys and decisions, not full personal data. Restrict access to logs to the owners
who need them, set retention, and alert on unexpected connection or permission changes.

## Responsible AI considerations

Override and low-confidence rates can reveal that an AI step performs worse for some kinds of input, such as particular
languages or document types. Break rates down by input type where possible, and route patterns affecting people to the
`responsible-ai` department.

## Evaluation requirements

Before go-live, prove each alert fires by forcing its condition in a test environment: a failed run, a missed heartbeat,
an aged exception, a validation failure spike. After a sustained change in AI quality signals, re-run the evaluation
sample before adjusting any threshold.

## Value measures

Track time to detect and time to resolve automation outages, alerts acted on versus ignored, and silent failures found
by the business before monitoring (which should fall to zero). Report at automation level to the automation lead; never
per person.

## Scale notes

### Starter

Use built-in failure notifications routed to a team channel, a simple daily heartbeat check and a monthly look at AI
override rates. Keep an expiry list by hand.

### Scale

Standardise run logging and heartbeat child flows across automations, feed a shared dashboard of failures, exceptions
and AI quality signals, and review it at the CoE cadence.

### Enterprise

Integrate automation signals into the organisation's operational monitoring and service management, with on-call
arrangements for business-critical automations and estate-wide views of AI quality trends.

## Hand-offs

- To `ai-operations:ai-solution-monitoring` for ongoing operation within the estate monitoring service.
- To `automation:exception-handling` when signals show new failure classes.
- To `automation:automation-value` with run and quality data for value measurement.
- To `ai-operations:ai-incident-management` when an alert reveals harm or widespread failure.

## Reviewer gates

From risk tier 2, `design-authority` checks that heartbeat, AI quality and expiry signals exist with named owners before
go-live. A tier 2 automation with no route for alerts to a named owner is a blocking finding.

## Failure modes

- The flow's trigger silently stops, no run fails, and nobody notices for weeks.
- Alerts go to the maker's inbox, and the maker has moved to another team.
- AI accuracy drifts as inputs change, reviewers quietly fix more results, and nobody measures the override rate.
- A service account credential expires on a holiday weekend with no warning.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Rely on failure notifications alone without a check for runs that never happened.
- Route alerts to an individual's inbox as the only channel.
- Adjust an AI threshold to silence an alert without re-testing against the evaluation sample.
- Use monitoring data to track the activity of individual reviewers or staff.

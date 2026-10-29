---
name: ai-telemetry
description: Designs the telemetry a custom AI solution emits - traces across orchestration, model, retrieval and tool calls, versions, tokens, latency, safety and quality signals and correlation ids - and decides what prompt and response content is captured, redacted and kept. Use when building a pro-code AI solution, when failures cannot be diagnosed, or when logs hold more personal data than they should.
license: CC-BY-4.0
metadata:
  department: ai-engineering
  lifecycle: Deliver, Assure, Launch, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, github
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-foundry-models, ms-copilot-privacy, ico-ai-data-protection, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI telemetry

## Purpose

When a user says "the assistant gave me a wrong answer yesterday", the team needs to see what the solution did: which
prompt version, which model, what was retrieved, which tools were called and what each returned. Without that, quality
problems are argued about rather than diagnosed. This skill designs the telemetry a custom AI solution emits, so that
behaviour is traceable, performance and cost are visible and quality can be monitored, while capturing no more
personal or confidential content than the purpose justifies. It goes wrong in both directions: logging nothing useful,
or logging every prompt and response in full into a store everyone can read.

## When to use

- A team is building a pro-code AI solution and needs to decide what to log and trace.
- Failures or poor answers in production cannot be diagnosed from the logs available.
- Logs capture full prompts and responses with personal data, without a decision on retention or access.
- Several solutions log differently and estate-wide monitoring is not possible.
- The operations team needs signals for monitoring and alerting that the solution does not yet emit.

## When not to use

- Configuring tracing and observability features for Foundry agents specifically - use `ai-foundry:foundry-observability`.
- Running operational monitoring and alerting for live solutions - use `ai-operations:ai-solution-monitoring`.
- The reviewer assessment of how long prompts and responses are kept - use `security-privacy:ai-interaction-retention`.
- Monitoring Power Automate flows and automation run health - use `automation:automation-monitoring`.
- Measuring value and usage against the hypothesis - use `m365-agents:agent-value-measurement`.

## Questions to ask first

1. What questions will the team need telemetry to answer: why was this answer wrong, why was it slow, what did it cost, is quality drifting?
2. Who will read the telemetry, and what are they allowed to see?
3. Does the solution handle personal, special category or confidential data in prompts, retrieved content or responses?
4. What retention does the organisation require or permit for interaction content and for operational data?
5. Which monitoring and alerting will be built on the telemetry, and by whom?

## Required inputs

- The solution architecture, showing orchestration steps, model calls, retrieval and tools.
- Data classification of the inputs, retrieved content and outputs, from `data-governance:data-classification-for-ai` where available.
- Retention rules for interaction data, from `data-governance:ai-data-retention-rules` or the DPO.
- Monitoring needs from the operations team.

If retention or classification is not decided, log metadata only (no prompt or response content) and record the open
decision with the DPO or data owner. Never decide content retention for personal data without them.

## Decision framework

Split telemetry into layers and decide each separately.

| Layer | Examples | Default capture | Access |
|---|---|---|---|
| Trace structure | Request id, correlation id, spans for orchestration, model, retrieval and tool calls, timings | Always | Engineering and operations |
| Configuration | Model deployment and version, prompt version, tool versions, retrieval settings | Always | Engineering and operations |
| Usage and cost | Tokens in and out, calls, cache hits | Always | Engineering, operations, finance roll-up |
| Outcomes | Errors, timeouts, content filter results, refusals, tool failures | Always | Engineering and operations |
| Quality signals | Groundedness or validation scores, user feedback, escalations | Always, as scores and labels | Engineering, operations, business owner in aggregate |
| Retrieval references | Identifiers of retrieved items, not their content | Usually | Engineering |
| Interaction content | Prompt text, retrieved text, response text | Only with a documented purpose, redaction, restricted access and retention | Named roles only |

User identifiers are pseudonymised in operational telemetry unless a documented purpose requires otherwise.

## Practitioner approach

Start from the questions telemetry must answer, and from the people who will ask them. Engineers need to reconstruct a
request; operations need health and drift signals; business owners need aggregate quality and usage; finance needs
cost. Design the minimum that answers each question.

Trace every request end to end. Assign a correlation id at the entry point and carry it through orchestration, each
model call, each retrieval and each tool call, including calls to other services. Record spans with timings and
outcomes. Use an open tracing standard and the semantic conventions emerging for generative AI, so traces can be read by
common tools and compared across solutions.

Record configuration with every request: model deployment and version, prompt version, tool versions and retrieval
settings. This is what lets a team link a quality change to a release, and it is the most commonly missing piece.

Capture usage and outcomes. Log tokens in and out, latency per step, content filter outcomes, refusals, tool errors and
retries. These feed cost reporting, performance work and monitoring. Log quality signals as scores and labels:
validation results, groundedness checks run online, user feedback and escalations.

Decide content capture deliberately. Prompt and response text is the most useful data for diagnosis and the most
sensitive. Default to not storing it in operational telemetry. Where diagnosis or evaluation needs it, capture it in a
separate store with redaction of personal data where possible, access limited to named roles, a defined retention
period and agreement from the DPO or data owner. Sampling a small share of interactions for quality review is often
enough. Log identifiers of retrieved items rather than their text.

Make telemetry useful from day one. Build a small set of views: request trace lookup by correlation id, latency and error
rates by step, tokens and cost by day, content filter and refusal rates, and quality signals over time. Hand these to
operations with the alert thresholds they need.

Govern it. Document what is captured, why, where it is stored, who can access it and for how long. Review the design when
the solution's data or audience changes.

## Outputs

- A telemetry specification: layers captured, fields, correlation approach, content capture decision with purpose, redaction, access and retention.
- Instrumentation in the solution code using an open tracing standard.
- A starter set of views for engineering, operations, business owner and cost reporting.
- A record of the content capture decision, agreed with the DPO or data owner where personal data is involved.

## Microsoft platform considerations

Microsoft Foundry offers tracing and monitoring for models and agents, and Azure Monitor with Application Insights can
collect OpenTelemetry traces and metrics from custom code. Which signals are captured automatically, where content is
stored and how retention is configured differ by service and change. Check current behaviour in `references/sources.md`,
and do not assume a platform default meets the content capture decision.

## Adoption considerations

Telemetry is adopted when it saves engineers time. Provide shared instrumentation libraries and a trace lookup that turns
a user's complaint into a diagnosis in minutes, and teams will keep it up to date.

## Knowledge considerations

Retrieval references in telemetry show which knowledge items are used, never used, or associated with poor answers.
Share these patterns, in aggregate, with knowledge owners through `knowledge-management:knowledge-gap-analysis`.

## Security and privacy considerations

Telemetry can become the largest unmanaged copy of sensitive data in a solution. Keep content out of operational logs by
default, pseudonymise user identifiers, restrict access, set retention and protect telemetry stores like production
data. Content retention goes to `security-privacy:ai-interaction-retention` for review.

## Responsible AI considerations

Telemetry should make it possible to investigate a complaint from an affected person and to detect patterns of poorer
quality for particular groups or input types. Design the quality signals with that use in mind, while respecting the
minimum group sizes set for reporting.

## Evaluation requirements

Online quality signals and sampled interactions from telemetry feed regression and drift evaluation. Test the
instrumentation itself: a request should be traceable end to end by correlation id, and redaction should be verified on
sample content.

## Value measures

Track time to diagnose reported issues, share of requests fully traced, telemetry cost and any incidents of sensitive data
found in logs. The AI engineering lead owns these. Never use telemetry to monitor individual users' activity.

## Scale notes

### Starter

Trace requests end to end with configuration, tokens, latency and errors, and no content capture. Provide one trace lookup
and one health view.

### Scale

Use a shared instrumentation library and conventions across solutions, a governed sampled content store for quality
review, and common dashboards feeding operations.

### Enterprise

Run estate-wide telemetry standards, central stores with access control and retention by classification, and portfolio
views of cost, quality and safety signals across solutions.

## Hand-offs

- To `ai-operations:ai-solution-monitoring` with signals and suggested alert thresholds.
- To `security-privacy:ai-interaction-retention` with the content capture decision.
- To `ai-engineering:ai-performance-engineering` with latency and token data.
- To `ai-foundry:foundry-cost-management` with usage and cost telemetry.

## Reviewer gates

From risk tier 2, `security-privacy` reviews content capture, redaction, access and retention. Full prompt and response
content containing personal data stored without an agreed purpose, access limits and retention is a blocking finding.

## Failure modes

- Prompt and model versions are not logged, so a quality drop cannot be linked to the release that caused it.
- Full prompts and responses go into a general log store readable by many people and kept indefinitely.
- Correlation ids stop at the first service, and tool failures cannot be connected to the user's request.
- Telemetry is used to track what individual staff ask, damaging trust and breaching policy.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Store prompt and response content containing personal data without a documented purpose, access limits and retention agreed with the DPO or data owner.
- Use telemetry to monitor or rank individual users.
- Omit model and prompt versions from request telemetry.
- Rely on a platform's default logging without checking what content it captures and keeps.

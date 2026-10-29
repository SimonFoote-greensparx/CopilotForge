---
name: foundry-observability
description: Designs tracing and observability for Microsoft Foundry agents and applications in production - what each run records across model calls, retrieval, tool calls and checkpoints, how content is protected, which signals and online evaluations show quality drifting, and who looks. Use when a Foundry solution is heading to production, when a misbehaving agent cannot be explained, or when traces capture more personal data than anyone agreed.
license: CC-BY-4.0
metadata:
  department: ai-foundry
  lifecycle: Deliver, Launch, Measure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, evaluation-quality
  sources: ms-foundry-models, ico-ai-data-protection, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Foundry observability

## Purpose

When a Foundry agent gives a bad answer or takes an odd action, the team needs to see what it was asked, what it
retrieved, which tools it called with which arguments, and why it stopped, without having to reproduce the failure.
This skill designs the traces, signals and online evaluations that make an agent's behaviour explainable and its
quality visible over time, and decides how prompt and response content is protected inside them. Observability goes
wrong when it is added after the first incident, when traces either capture nothing useful or capture everything
including personal data with no retention rule, and when dashboards show uptime while answer quality quietly declines.

## When to use

- A Foundry agent or workflow is being built and tracing must be designed in before production.
- An agent misbehaved and nobody can reconstruct why from what was logged.
- Quality complaints are rising but the dashboards look healthy.
- Traces or logs are found to hold prompts, documents or personal data without an agreed purpose or retention.
- A solution is moving from pilot to wider use and the team needs signals that show drift.

## When not to use

- General logging and telemetry standards for any custom AI solution - use `ai-engineering:ai-telemetry`.
- Operational alerting, on-call routes and service health once signals exist - use `ai-operations:ai-solution-monitoring`.
- Tenant-level admin monitoring of AI usage across the estate - use `platform-governance:ai-admin-monitoring`.
- Analytics for Copilot Studio agents - use `copilot-studio:studio-analytics`.
- Reviewing retention of prompts and transcripts as a gate - that is the reviewer skill `security-privacy:ai-interaction-retention`.

## Questions to ask first

1. When this solution fails, what will the support engineer need to see to explain the failure within an hour?
2. Which steps happen inside a run: model calls, retrieval, tool calls, hand-offs between agents, human checkpoints?
3. Will traces contain personal or sensitive content, who may see it, and for how long may it be kept?
4. What does good quality look like in production, and which signals would show it slipping before users complain?
5. Who will look at the traces and quality signals, how often, and what will they do with them?

## Required inputs

- The agent or workflow architecture, with the steps, tools and checkpoints in a run.
- The evaluation plan and thresholds from `ai-foundry:model-evaluation`, so online signals mirror offline ones.
- Data classification of prompts, grounding content and tool results.
- The organisation's logging, monitoring and retention standards for Azure workloads.

Where retention for traced content has not been agreed with the data owner and DPO, mark it `[To confirm: ...]` and
trace metadata only, with content capture switched off, until it is. Never default to keeping everything.

## Decision framework

| Signal layer | What it records | Content capture default | Primary user |
|---|---|---|---|
| Run trace | Each step of a run with timing, model and version, token counts, tool names, outcome and errors, linked by one run identifier | Metadata only | Engineering and support |
| Content trace | Prompts, retrieved passages, tool arguments and results, responses | Off in production; on in test; sampled and protected in production only with an agreed purpose and retention | Named investigators |
| Operational metrics | Latency, error and throttling rates, cost per run, budget and step-limit breaches | Not applicable | Operations |
| Quality signals | Online evaluation scores on sampled runs, groundedness, refusal and escalation rates, user feedback | Scores kept; content per the content trace rule | Solution owner |
| Safety signals | Content filter actions, detected injection attempts, blocked tool calls | Event and category, not content, by default | Security and responsible AI |

Raise content capture only for a stated investigative purpose, with access restricted and retention set.

## Practitioner approach

Start with the failure you will need to explain. Walk through a realistic bad run with the support engineer: the user
reports a wrong answer or an unexpected action, and they must find the run, see each step and identify where it went
wrong. Whatever they need for that becomes the minimum trace. Usually that means one identifier per run that ties
together every model call, retrieval, tool call, hand-off and checkpoint, with the model version, prompt version and
configuration in force at the time.

Instrument with open standards where the platform supports them, so traces flow into the organisation's existing
monitoring tools rather than a separate store nobody watches. Record prompt and instruction versions as attributes on
every run; without them, a change in behaviour cannot be tied to a change in the solution.

Decide content capture deliberately. Full prompts and responses are the most useful thing to have during an
investigation and the most sensitive thing to hold. Keep content capture on in development and test, off by default in
production, and enable sampled or time-limited capture only for a recorded purpose, with access restricted to named
roles and retention agreed with the DPO. Redact or mask known sensitive fields before they are stored, and remember
that grounding passages and tool results can contain more personal data than the user's question.

Make quality observable, not only availability. Run online evaluation on a sample of production runs using the same
measures as offline evaluation where possible, such as groundedness, task adherence and safety, and track escalation,
refusal and user-feedback rates beside them. Set thresholds that open an investigation, and agree who receives them.
Drift often appears first as rising escalations, longer runs or more tool retries rather than outright errors.

Give each signal an owner and a rhythm. Operations watch latency, errors and throttling continuously; the solution
owner reviews quality signals weekly at first; security and responsible AI see safety events as they occur. Feed
confirmed failures back into the evaluation set through `ai-foundry:model-evaluation`, so each incident makes the next
release safer.

Test the observability before launch: run a deliberately failing scenario and confirm the support engineer can find and
explain it from the traces alone. State what observability cannot determine: whether an answer that looked fine was
actually right, which needs sampled human review.

## Outputs

- The observability section of the `foundry-solution-design` template: run trace schema, content capture rules and retention, metrics, online evaluations and thresholds, owners and review rhythm.
- A tracing test showing a failed run can be reconstructed from traces alone.
- Signal and alert definitions handed to operations on the `support-and-monitoring-plan` template.

## Microsoft platform considerations

Foundry provides tracing and evaluation capabilities for agents and applications that integrate with Azure monitoring
services, and the instrumentation options, content capture settings and online evaluation features are evolving, some
in preview. Check the current source records for what is captured by default, where trace data is stored and processed,
and how content capture is controlled, before designing retention around it.

## Adoption considerations

User feedback is one of the best quality signals, but only if giving it is easy and people see it acted on. Add a
simple feedback route in the solution surface and report back on what changed. Make clear to users what is recorded
about their interactions.

## Knowledge considerations

Traces show which sources were retrieved and which questions found nothing. Share unanswered and poorly grounded
questions with the knowledge owners through `knowledge-management:knowledge-gap-analysis`, at question-pattern level
rather than as user transcripts.

## Security and privacy considerations

Traces are a copy of the conversation and can become the largest unplanned store of personal data in the solution.
Minimise content, restrict access, set retention, protect trace stores to the same standard as the source data, and
confirm processing location. `security-privacy:ai-interaction-retention` reviews capture and retention from tier 2.

## Responsible AI considerations

Observability is how oversight works after launch. Make sure safety events and escalations are visible to the people
accountable for them, and never use traces to assess or monitor individual users' behaviour or performance.

## Evaluation requirements

Online evaluation uses the same measures and thresholds as offline evaluation where possible, on a sample sized to the
risk tier. Confirmed production failures join the regression set, with `evaluation-quality:regression-evaluation`.

## Value measures

Measure mean time to explain an incident, the share of runs with a complete trace, and the time from quality drift to
detection, owned by the solution owner. Report usage and quality at solution, team or role level only.

## Scale notes

### Starter

Trace every run with metadata and versions, keep content capture off in production, run a weekly sampled quality
review by the owner, and test that one failed run can be explained.

### Scale

Standardise the trace schema, content capture policy and quality dashboard across Foundry solutions so support teams
can move between them, and automate online evaluation on samples.

### Enterprise

Run central observability for all custom AI with consistent schemas, governed content capture, cross-solution safety
event monitoring and formal retention, integrated with the organisation's security operations.

## Hand-offs

- To `ai-operations:ai-solution-monitoring` for alerting and on-call routes.
- To `ai-engineering:ai-telemetry` for shared telemetry standards and pipelines.
- To `ai-foundry:model-evaluation` with production failures for the evaluation set.
- To `ai-foundry:foundry-cost-management` with cost per run signals.
- To `ai-foundry:foundry-production-readiness` with the tracing test result.

## Reviewer gates

From risk tier 2, `security-privacy` reviews content capture, access and retention of traces, and
`evaluation-quality` checks that online quality signals mirror the offline evaluation. Content capture in production
without an agreed retention rule is a blocking finding.

## Failure modes

- Tracing is added after the first incident, and that incident can never be explained.
- Full prompts and retrieved documents are kept indefinitely in a log store with broad access.
- Dashboards show availability and latency only, and answer quality declines for months unnoticed.
- Prompt versions are not recorded, so a behaviour change cannot be linked to the release that caused it.
- Traces are used to review how individual employees use the solution, and trust collapses.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Capture prompt and response content in production without a stated purpose, restricted access and agreed retention.
- Ship a Foundry agent without run-level tracing that links every step.
- Treat availability metrics as evidence of answer quality.
- Use traces to monitor or assess individual users.

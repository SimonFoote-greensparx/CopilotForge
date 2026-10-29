---
name: ai-resilience
description: Engineers resilience into custom AI solutions - timeouts, bounded retries, circuit breakers, evaluated fallback deployments or models, degraded modes, content filter and malformed output handling, idempotent tools - so they fail safely and honestly. Use when building a pro-code AI solution, after an outage or throttling incident, or when nothing defines what happens if the model is unavailable.
license: CC-BY-4.0
metadata:
  department: ai-engineering
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure
  edition-support: scale, enterprise
  reviewers: design-authority
  sources: ms-foundry-models, ms-responsible-ai, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI resilience

## Purpose

AI solutions depend on model deployments, indexes, tools and business systems, any of which can be slow, throttled,
unavailable or return something unusable. Models add failure modes of their own: content filter blocks, refusals,
malformed structured output and answers that look right but are not. This skill engineers how the solution behaves when
these happen, so it degrades gracefully, tells users honestly what it can and cannot do, and never makes a bad situation
worse through retry storms or repeated actions. It goes wrong when every error triggers a retry, when a fallback model
is switched in without evaluation, and when the solution hides failure behind a confident but wrong answer.

## When to use

- A team is building a pro-code AI solution and needs to define failure behaviour.
- An outage, throttling episode or provider incident caused user-visible failure or duplicated actions.
- The solution has no defined behaviour when its model, index or a tool is unavailable.
- Retry logic is causing cascades, cost spikes or repeated side effects.
- A tier 3 or 4 solution needs resilience evidence before production.

## When not to use

- Business continuity and manual fallback when an AI capability is unavailable for a long period - use `ai-operations:ai-continuity`.
- Exception handling, retries and queues in Power Automate flows - use `automation:exception-handling`.
- Latency, throughput and capacity tuning - use `ai-engineering:ai-performance-engineering`.
- Responding to an incident in progress - use `ai-operations:ai-incident-management`.
- Choosing deployment topology and regions for availability - use `ai-foundry:foundry-deployment-architecture`.

## Questions to ask first

1. What must the solution still do when the model is unavailable, and what can it stop doing?
2. Which calls are safe to repeat, and which have side effects (writes, sends, payments)?
3. Is there an alternative deployment, region or model that has been evaluated for this task?
4. What should users see when the solution cannot help, and where should they go instead?
5. What availability target and recovery time were agreed, and with whom?

## Required inputs

- The solution architecture with dependencies and which are critical.
- Availability and recovery targets from `ai-architecture:ai-non-functional-requirements`.
- Tool contracts, including idempotency, from `ai-engineering:ai-api-and-tooling`.
- Telemetry showing current failure types and rates, from `ai-engineering:ai-telemetry`.

If no targets exist, propose them with the business owner and record them before engineering resilience. If a fallback
model has not been evaluated, it is not a fallback.

## Decision framework

Match each failure to a response. Responses must be bounded, observable and safe to repeat.

| Failure | Response | Guardrail |
|---|---|---|
| Timeout or slow dependency | Timeout per call within the latency budget | Timeouts shorter than the user will wait in total |
| Transient error or throttling | Retry with exponential backoff and jitter, honouring retry-after signals | Cap attempts and total time; only for idempotent calls |
| Persistent dependency failure | Circuit breaker opens; stop calling; serve degraded mode | Breaker state visible in telemetry; half-open probing |
| Model deployment unavailable | Fail over to an alternative deployment or region of the same model | Alternative tested and within data residency rules |
| Model unavailable everywhere | Fall back to an evaluated alternative model, or to degraded mode | Fallback model passed evaluation; behaviour differences known |
| Content filter block or refusal | Do not retry to evade; give an honest message or route to a person | Track rates; review legitimate inputs that are blocked |
| Malformed structured output | One repair attempt or re-request, then fail safely | Never pass unvalidated output to tools or users |
| Tool or business system failure | Report failure clearly; never claim the action succeeded | Idempotency keys; compensation for partial effects |

Degraded modes are designed in advance: for example search results without a generated summary, a form instead of a
conversation, or a clear route to a person.

## Practitioner approach

Map dependencies and classify them. For each model deployment, index, tool and system, note whether the solution can
function without it, and what it would do instead. This map drives everything that follows and is usually the first time
anyone has written it down.

Set timeouts everywhere. Default client timeouts are often far longer than users will wait. Allocate time from the latency
budget to each call so the whole request either completes or fails within an acceptable time.

Retry with discipline. Retry only transient failures on idempotent calls, with exponential backoff, jitter and a cap on
attempts and total time. Honour retry-after signals from throttled services. Retrying everything multiplies load during
an incident and turns throttling into an outage.

Add circuit breakers on critical dependencies. When failures pass a threshold, stop calling for a period, serve the
degraded mode and probe periodically. Expose breaker state in telemetry so operations can see what is happening.

Plan fallbacks honestly. A second deployment of the same model in another region is the safest fallback, provided data
residency rules allow it. A different model is a different solution: it must pass the evaluation harness before it can be
used as a fallback, and its known differences recorded. Where no evaluated fallback exists, the fallback is degraded mode.

Handle model-specific failures. Do not retry content filter blocks or refusals in the hope of a different result; that is
evasion, not resilience. Give the user an honest message and, where appropriate, a route to a person, and track rates so
legitimate inputs that are blocked can be investigated. For malformed structured output, allow one repair or re-request,
then fail safely.

Protect side effects. Tools with effects use idempotency keys so retries cannot repeat them. When a later step fails after
an effect, report the true state to the user and, where needed, run a compensating action. Never tell a user an action
succeeded unless the system confirmed it.

Design what users see. Write failure and degraded-mode messages with the business owner: what happened in plain terms,
what the user can do now, and where to go. A clear "I cannot complete this right now; here is the form" preserves trust;
a confident wrong answer destroys it.

Test failure deliberately. Inject timeouts, throttling, deployment loss and malformed output in a test environment, and for
critical solutions run controlled failure exercises in pre-production. Record results as release evidence.

## Outputs

- A dependency and failure map: dependencies, criticality, failure responses, degraded modes and user messages.
- Resilience configuration in code: timeouts, retry policies, circuit breakers, failover and fallback rules.
- A fallback register: alternative deployments or models, evaluation status and known differences.
- Failure test results, as release evidence for tier 3 and above.

## Microsoft platform considerations

Microsoft Foundry deployment types, regional availability, throttling signals and model lifecycle affect which failover
and fallback options exist, and Azure services such as API Management can apply retry, load balancing and circuit
breaking in front of model endpoints. These options and their limits change; confirm in `references/sources.md` and check
data residency implications before failing over across regions.

## Adoption considerations

Users forgive occasional unavailability if the solution is honest and offers another route; they stop using it after a
confident wrong answer. Agree user-facing messages with the business owner and tell support teams what each degraded mode
looks like.

## Knowledge considerations

When retrieval is unavailable, the solution must not answer from the model's general knowledge as if it were grounded.
Degraded mode for grounded solutions is "cannot answer from the approved sources right now", not an ungrounded answer.

## Security and privacy considerations

Failover to another region or fallback model can move data to a different processing location or provider terms. Confirm
data residency and processing terms for every fallback before enabling it, and keep fallback paths within the same
security controls.

## Responsible AI considerations

Silent degradation can affect people unfairly, for example when a fallback model handles some languages worse. Make
degradation visible to users, record when fallbacks were active and include fallback behaviour in safety evaluation.

## Evaluation requirements

Fallback models and degraded modes are evaluated like any release. Failure tests (timeouts, throttling, deployment loss,
malformed output, tool failure) are run before production for tier 3 and above and after material changes.

## Value measures

Track availability against target, time in degraded mode, failed requests by cause, retries per request and duplicated
side effects (which should be zero). The AI engineering lead owns these and reports to the business owner.

## Scale notes

### Starter

Set timeouts, bounded retries on idempotent calls, honest failure messages and idempotency keys on any write tool. Keep
degraded mode simple: a clear message and an alternative route.

### Scale

Add circuit breakers, regional failover where residency allows, evaluated fallback models for critical steps and failure
injection tests in the pipeline.

### Enterprise

Provide shared resilience components and gateway policies, coordinate failover across solutions, run regular failure
exercises for critical solutions and track resilience across the estate.

## Hand-offs

- To `ai-operations:ai-continuity` for business continuity and manual fallback over longer outages.
- To `ai-engineering:ai-solution-testing` for failure-path tests.
- To `ai-engineering:ai-telemetry` to expose breaker, fallback and degraded-mode signals.
- To `ai-operations:ai-incident-management` with runbook steps for outages.

## Reviewer gates

From risk tier 3, `design-authority` checks the failure map, fallback evaluation and failure test evidence before
production. An unevaluated fallback model or a write tool without idempotency protection is a blocking finding.

## Failure modes

- Every error is retried immediately, multiplying load and turning throttling into a full outage.
- A fallback model is switched in automatically without evaluation, and answers degrade without anyone knowing.
- A tool call times out after succeeding, is retried and the customer is charged twice.
- Retrieval fails and the solution answers from general model knowledge as if from approved sources.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Retry non-idempotent calls, or retry without caps, backoff and jitter.
- Use a fallback model that has not passed evaluation for the task.
- Retry or rephrase to get past a content filter block or refusal.
- Tell a user an action succeeded without confirmation from the system that performed it.

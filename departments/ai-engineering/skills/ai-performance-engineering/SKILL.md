---
name: ai-performance-engineering
description: Engineers the latency and throughput of custom AI solutions against agreed targets - latency budgets per step, token budgets, streaming, caching, parallel calls, right-sized models, quota and capacity planning, and load testing - while protecting quality and cost. Use when an AI solution is too slow, when usage is about to grow, when throttling appears under load, or before a tier 3 solution goes to production.
license: CC-BY-4.0
metadata:
  department: ai-engineering
  lifecycle: Deliver, Assure, Scale, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure
  edition-support: scale, enterprise
  reviewers: design-authority
  sources: ms-foundry-models, ms-agents-compare
  status: draft
  authors: Simon Foote
---

# AI performance engineering

## Purpose

AI solutions are slow in ways ordinary applications are not: each model call takes seconds, agents chain several calls
with retrieval and tools, and capacity is limited by quotas and tokens rather than servers. Users abandon a helpful
assistant that takes too long, and a solution that works for a pilot group can throttle when a department arrives.
This skill engineers latency and throughput against agreed targets by budgeting time and tokens per step, cutting
unnecessary calls, using streaming and caching, choosing appropriately sized models and planning capacity, without
quietly trading away quality or blowing the budget. It goes wrong when teams tune without measuring, and when a faster,
smaller model is swapped in without re-running evaluation.

## When to use

- Users report that an AI solution is too slow, or abandon requests before they complete.
- Usage is expected to grow (a wider rollout, a new channel, a seasonal peak).
- Throttling or quota errors appear under load.
- A tier 3 or 4 solution needs performance evidence before production.
- Cost per request is rising and performance work could reduce tokens and calls.

## When not to use

- Setting the performance targets and other non-functional requirements - use `ai-architecture:ai-non-functional-requirements`.
- Managing model and platform cost as a FinOps discipline - use `ai-foundry:foundry-cost-management`.
- Choosing deployment types, regions and topology - use `ai-foundry:foundry-deployment-architecture`.
- Retries, fallbacks and graceful degradation when dependencies fail - use `ai-engineering:ai-resilience`.
- Comparing models on quality for a task - use `ai-foundry:model-evaluation`.

## Questions to ask first

1. What latency do users need, measured how (time to first token, time to complete answer), and at what percentile?
2. What peak load is expected (concurrent users, requests per minute, tokens per minute), and when?
3. How many model calls, retrieval queries and tool calls does a typical request make, and which are sequential?
4. What quota and capacity does the solution have, in which deployments and regions?
5. What quality thresholds must be maintained, and what is the cost budget per request or per month?

## Required inputs

- Agreed performance targets from `ai-architecture:ai-non-functional-requirements`, or from the business owner.
- Telemetry with per-step latency and tokens, from `ai-engineering:ai-telemetry`.
- Current deployments, quotas and capacity, and expected load.
- The evaluation harness and thresholds, to check quality after each change.

If no targets have been agreed, measure the current state, propose targets to the business owner and record them before
tuning. If per-step telemetry is missing, instrument first; tuning without it is guesswork.

## Decision framework

Work through the levers in order; earlier levers are usually cheaper and safer for quality.

| Lever | Use when | Watch for |
|---|---|---|
| Measure and budget | Always first | Targets defined at a percentile, not an average |
| Remove calls | Steps are redundant, or could be code rather than a model call | Losing a check that protected quality |
| Parallelise | Independent retrieval or tool calls run in sequence | Rate limits on downstream systems |
| Stream | Users wait for long answers | Validation that needs the full answer before display |
| Trim tokens | Prompts carry unused instructions, history or retrieved text | Dropping context that quality depends on |
| Cache | Repeated identical or near-identical requests, stable content | Serving stale or another user's results |
| Right-size models | Some steps (routing, classification) do not need the largest model | Quality regression; must re-run evaluation |
| Capacity and quota | Throttling under expected load | Cost commitments; licensing and capacity questions route to the guide or a partner |

Every change is followed by an evaluation run. A performance gain that breaches a quality threshold is rejected.

## Practitioner approach

Measure before changing anything. Use telemetry to break a typical request into its steps (retrieval, each model call,
each tool call, post-processing) with time and tokens for each, at the 50th, 90th and 99th percentiles. The slowest
step is often not the one people assume; a sequential chain of three tool calls or an oversized retrieval payload can
cost more than the main model call.

Set a latency budget per step that adds up to the target, and a token budget per call. Budgets turn vague complaints into
engineering decisions and make regressions visible in the pipeline.

Remove before you optimise. Look for model calls doing work code could do (formatting, simple routing, extracting a
field from structured data), duplicate retrieval, and agent loops that run more turns than needed. Each removed call
saves seconds and cost, and removes a failure point.

Run independent work in parallel. Retrieval from several sources, or tool calls that do not depend on each other, can
run concurrently. Check downstream rate limits before parallelising widely.

Stream responses where users read them. Time to first token matters more to perceived speed than total time. Where
output must be validated before display, stream progress indicators or partial, safe content instead.

Trim tokens with care. Shorten instructions, cap conversation history with summarisation, and retrieve fewer, better
chunks. Smaller prompts are faster and cheaper, but each trim can affect quality, so evaluate after each change.

Cache deliberately. Cache embeddings, retrieval results for stable content and responses to identical requests where
appropriate, keyed so one user's permission-trimmed results are never served to another. Set expiry aligned with how
often the content changes.

Right-size models per step. Routing, classification and extraction often run well on smaller, faster models; reserve
larger models for steps that need them. Treat any model change as a release that re-runs the full evaluation.

Plan capacity. Translate expected peak load into tokens per minute and requests per minute per deployment, compare with
quota, and decide on additional capacity, deployments or load spreading. Run load tests that reproduce realistic mixes of
requests at expected peak and beyond, and watch for throttling and latency growth. Capacity commitments and their
licensing implications go to the platform team and the Microsoft licensing guide or a licensing partner.

## Outputs

- A performance baseline per step and percentile, and latency and token budgets.
- A tuning log: each change, its effect on latency, tokens, cost and evaluation scores, and the decision.
- A capacity plan: expected peak, required throughput per deployment, quota position and actions.
- Load test results against targets, as release evidence for tier 3 and above.

## Microsoft platform considerations

Microsoft Foundry offers several deployment types with different throughput, latency and cost characteristics, and
quotas and capacity are allocated per model, deployment and region. These options, their limits and their pricing
change often; check `ms-foundry-models` and other records in `references/sources.md` and record what was confirmed before
designing capacity. Never quote quotas or prices from memory.

## Adoption considerations

Perceived speed shapes adoption more than measured speed. Streaming, progress indicators and honest messages when a
request will take longer keep users engaged. Share improvements with the business owner in terms users notice.

## Knowledge considerations

Retrieval payload size drives latency and tokens. Well-structured, concise knowledge with good metadata lets retrieval
return fewer, better chunks; raise content issues with knowledge owners through `knowledge-management:ai-ready-content`.

## Security and privacy considerations

Caches can leak data across users if keys ignore identity or permissions. Key caches on user or permission scope for
user-scoped content, set expiry and protect cache stores like the data they hold.

## Responsible AI considerations

Swapping in a smaller model or trimming context can reduce quality unevenly, for example for less common languages or
complex cases. Check evaluation results by segment after performance changes, not only overall averages.

## Evaluation requirements

Re-run the evaluation harness after every performance change, and reject changes that breach thresholds. Include load
test results and latency at the agreed percentile in release evidence for tier 3 and above.

## Value measures

Track latency at the agreed percentile, throttled requests, tokens and cost per request, and abandonment rates where
measurable, at solution level. The AI engineering lead owns these, reporting to the business owner.

## Scale notes

### Starter

Most starter solutions need measurement, streaming and token trimming rather than capacity work. Instrument per-step
latency and fix the slowest step first.

### Scale

Set budgets per step, run load tests before wide rollouts, right-size models per step and plan quota with the platform
team ahead of growth.

### Enterprise

Manage capacity across solutions and regions, share caching and routing components, and include performance budgets in
engineering standards with load testing in the pipeline for critical solutions.

## Hand-offs

- To `ai-foundry:foundry-cost-management` with token and cost changes.
- To `ai-foundry:foundry-deployment-architecture` where deployment type or region changes are needed.
- To `ai-engineering:ai-resilience` for throttling and overload behaviour.
- To `ai-engineering:evaluation-harness` to confirm quality after each change.

## Reviewer gates

From risk tier 3, `design-authority` checks performance evidence against agreed targets before production. A model
change made for speed without a passing evaluation run is a blocking finding.

## Failure modes

- A smaller, faster model is swapped in, latency improves and answer quality falls without anyone measuring it.
- A cache keyed only on the question serves one user's permission-trimmed answer to another.
- Load testing uses one repeated simple request, and real traffic throttles on day one of rollout.
- Tuning targets averages, while the slowest tenth of requests remain unusable.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Change a model or trim context for speed without re-running evaluation.
- Cache user-scoped results without keying on the user's identity or permissions.
- State quotas, throughput limits or prices from memory.
- Tune without per-step measurement and agreed targets.

---
name: exception-handling
description: Designs how an automation with AI steps handles what goes wrong - transient failures and retries, permanent technical faults, business exceptions, invalid or low-confidence AI output, content filtering and partial runs - so every failure is caught, routed to an owner and recoverable. Use when building an automation, when flows fail silently or leave half-finished work, or when exception queues grow without an owner.
license: CC-BY-4.0
metadata:
  department: automation
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: power-platform, copilot-studio, ai-foundry
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-copilot-studio-guidance, ms-managed-environments, ms-coe-starter-kit
  status: draft
  authors: Simon Foote
---

# Exception handling

## Purpose

Automations with AI steps fail in more ways than ordinary flows: as well as timeouts and unavailable systems, the model
can return malformed output, refuse, be blocked by content filtering or return something plausible but wrong. This skill
designs how each kind of failure is detected, retried or routed, and recovered, so nothing fails silently and nothing is
left half done. It goes wrong when every failure is treated alike, when retries repeat effects, and when exceptions land
in a shared mailbox that nobody owns.

## When to use

- An automation is being built and its failure behaviour has not been designed.
- Flows fail silently, or are found to have stopped days later.
- A run fails midway and leaves records partly updated or messages partly sent.
- AI steps occasionally return unusable output and the flow either crashes or continues regardless.
- An exception queue or mailbox is growing and nobody is sure who should work it.

## When not to use

- Designing the human approval and review steps themselves - use `automation:human-in-the-loop`.
- Alerting, dashboards and run health after go-live - use `automation:automation-monitoring`.
- Responding to a significant AI failure or harm affecting users - use `ai-operations:ai-incident-management`.
- Resilience patterns in pro-code services, such as circuit breakers and fallback models - use `ai-engineering:ai-resilience`.
- Business continuity when an AI service is unavailable for a long period - use `ai-operations:ai-continuity`.

## Questions to ask first

1. What are the effects of a run (records changed, messages sent, payments made), and in what order do they happen?
2. Which failures are temporary and worth retrying, and which will never succeed however often they are tried?
3. What should happen when an AI step returns output that fails validation or falls below the confidence threshold?
4. Who owns business exceptions, how quickly must they be worked, and where will they see them?
5. If a run stops halfway, can it be safely rerun, or must earlier steps be undone?

## Required inputs

- The automation design, including effects, AI step definitions, thresholds and the exception catalogue.
- The owner of each exception type and their agreed response times.
- Known behaviour of each connected system on failure (timeouts, throttling, error responses), where documented.
- The flow structure from `automation:flow-design-patterns`.

If exception owners are not named, the automation is not ready for production; record it as a blocking gap in the design.

## Decision framework

Classify each failure, then apply the matching response. Every class ends with a record and, if not resolved
automatically, a named owner.

| Failure class | Examples | Response |
|---|---|---|
| Transient technical | Timeout, throttling, temporary unavailability | Retry with increasing delay and a cap; only for steps that are safe to repeat |
| Permanent technical | Authentication expired, missing permission, record not found, changed schema | No retry; park the item, alert the technical owner, keep inputs for rerun |
| AI output invalid | Output fails schema, missing fields, values outside allowed list | One controlled retry at most, then route to review with the reason |
| AI low confidence | Below the design threshold | Route to review; never retry to fish for a higher score |
| AI refused or filtered | Model declines, content filter blocks input or output | Route to review with the reason; check whether input is legitimate |
| Business exception | Case outside the rules, missing information, policy conflict | Route to the business owner's queue with context and time limit |
| Partial run | Some effects done, a later step failed | Resume from a checkpoint if steps are idempotent; otherwise compensate and record |

Retries apply only where the step is idempotent or protected by a key. A retry that can repeat an effect is a defect.

## Practitioner approach

Begin by listing the effects of a run in order, and marking each as safe to repeat or not. Sending an email, creating a
record without a key or posting a payment are not safe to repeat. This list drives everything else: it tells you where
retries are allowed, where checkpoints are needed and what must be undone if a run stops halfway.

Classify failures before writing any handling. Most flows have one catch-all that emails the maker. Replace it with
handling per class. Transient failures get bounded retries with increasing delay. Permanent technical failures get no
retries, because retrying an expired credential a hundred times only delays the alert; they go straight to the technical
owner with the item preserved for rerun.

Treat AI failures as their own classes. Malformed output may deserve one retry, since models are not deterministic, but
repeated retries to get a "better" answer amount to shopping for a result and hide a weak AI step. Low-confidence and
filtered results go to a person with the reason shown. Track the rate of each; a rising rate is an early sign that inputs
have changed or the model version has.

Design the exception queue as a product. Put business exceptions where the owning team already works, such as a list,
a case queue or a Teams channel with a tracked item, not a shared mailbox. Each item shows what was attempted, why it
stopped, the original input and what the person needs to do. Set a response time with the owner and an escalation when
it passes. Close the loop: when a person resolves an item, the automation should be able to resume or record the manual
outcome.

Make partial runs recoverable. Write a checkpoint after each significant effect, with the item key. On rerun, skip
completed steps. Where a later failure makes earlier effects wrong (an order created but not confirmed), define the
compensating action and who approves it. Test these paths deliberately, by forcing failures at each step in a test
environment.

Never let a failure disappear. Every run ends in one of three recorded states: completed, routed to an owner, or failed
with an alert. If a run can end any other way, the handling is incomplete.

## Outputs

- An exception handling design per automation: effects and repeat safety, failure classes with responses, retry rules, AI failure handling, exception queue location and owners, response times, escalation, checkpoint and compensation rules. It forms the exceptions section of the `automation-design` template.
- Test evidence that each failure class was forced and handled as designed.
- An exception owner list with agreed response times.

## Microsoft platform considerations

Power Automate offers configurable retry policies, scopes with run-after settings, and timeouts on actions; AI models
in Power Platform and models deployed through Microsoft Foundry return different error and filtering signals. Default
retry behaviour may not suit AI steps or non-idempotent actions. Check current settings and limits in
`references/sources.md` and configure retries explicitly rather than relying on defaults.

## Adoption considerations

The team that works exceptions will judge the automation by the quality of its exception items. Show them examples
before go-live, agree the format with them and adjust it after the first weeks. A clear exception item builds trust;
a cryptic one teaches people to work around the automation.

## Knowledge considerations

Not applicable to most exception handling, because it concerns run behaviour rather than grounding. Where business
exceptions need guidance to resolve, link the exception item to the maintained procedure.

## Security and privacy considerations

Exception items and error logs often capture full inputs, which may include personal or confidential data. Store them
where access matches the original data, set retention, and avoid emailing raw inputs to wide distribution lists.

## Responsible AI considerations

When an AI step fails or is filtered on an item about a person, that person's case must still be handled fairly and in
time. Make sure exception routes do not create a slower, worse path for particular groups, for example inputs in other
languages that the model handles poorly.

## Evaluation requirements

Force each failure class in testing and record the result. Include malformed, low-confidence and filtered AI outputs, a
mid-run failure with recovery, and a timeout on the exception queue. Re-test after changes to the flow, model or prompt.

## Value measures

Track exceptions by class, time to resolution, items recovered automatically and runs with unrecorded outcomes (which
should be zero). Report at automation and team level to the process owner; rising AI failure rates feed improvement work.

## Scale notes

### Starter

Use a standard try, catch and finally structure, a single owned exception list per automation and explicit retry
settings. Test the main failure paths by hand.

### Scale

Provide a shared exception-routing child flow and queue pattern, and report exception rates across automations at the
CoE cadence.

### Enterprise

Run a common exception and recovery framework across automations, with central visibility of queues, response times and
AI failure trends, and agreed compensation procedures for business-critical processes.

## Hand-offs

- To `automation:automation-monitoring` for alerts on failure rates and queue ageing.
- To `automation:human-in-the-loop` for review of low-confidence and filtered items.
- To `ai-operations:ai-incident-management` when failures cause harm or affect many people.
- To `automation:flow-design-patterns` to build the handling into the flow.

## Reviewer gates

From risk tier 2, `design-authority` checks that retries are confined to idempotent steps, partial runs are recoverable
and every exception class has an owner. Missing exception owners at tier 2 and above are a blocking finding.

## Failure modes

- A default retry resubmits a non-idempotent step and sends the same message or payment several times.
- AI steps are retried until they return a high-confidence answer, hiding a poorly performing model.
- Exceptions go to a shared mailbox, nobody owns it, and customers wait weeks.
- A run fails midway, leaves records half updated and nobody knows which items were affected.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Retry a step that can repeat an external effect without an idempotency key.
- Retry an AI step repeatedly to obtain a more favourable result.
- Let a run end without a recorded outcome.
- Route business exceptions to a mailbox or queue without a named owner and response time.

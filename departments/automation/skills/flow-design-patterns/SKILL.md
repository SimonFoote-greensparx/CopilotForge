---
name: flow-design-patterns
description: Sets the build patterns for robust Power Automate cloud flows that include AI steps - triggers, solution-aware structure, connection references, environment variables, structured AI outputs validated before use, idempotency, concurrency and error scopes. Use when a maker starts building an approved automation design, when a flow with an AI step is fragile, or when the CoE needs standard flow patterns.
license: CC-BY-4.0
metadata:
  department: automation
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: power-platform, copilot-studio, ai-foundry
  edition-support: starter, scale, enterprise
  reviewers: design-authority, security-privacy
  sources: ms-copilot-studio-guidance, ms-managed-environments, ms-copilot-studio-security-governance, ms-coe-starter-kit
  status: draft
  authors: Simon Foote
---

# Flow design patterns

## Purpose

Most flows that fail in production were built to work once in the maker's environment: hard-coded addresses, personal
connections, no handling for duplicates, and an AI step whose free-text output is passed straight into the next action.
This skill sets the patterns that make a Power Automate flow with AI steps buildable, testable, movable between
environments and safe to leave running. It goes wrong when AI output is trusted as if it were data from a system, and
when flows are built outside solutions and cannot be promoted or supported.

## When to use

- An approved automation design is ready to build.
- A flow with an AI step produces intermittent wrong results or breaks on unusual inputs.
- A flow built in a personal environment needs to move to a governed environment.
- The CoE wants a standard set of flow patterns and a review checklist for makers.
- A flow is being extended with an AI step and the maker needs to know how to wire it safely.

## When not to use

- Deciding what to automate and which steps need AI - use `automation:automation-assessment`.
- Redesigning the process or defining exceptions and owners - use `automation:automation-process-design`.
- Retry policies, fallbacks and exception queues in detail - use `automation:exception-handling`.
- Flows called as actions from a Copilot Studio agent - use `copilot-studio:power-automate-actions`.
- Pro-code services and pipelines outside Power Platform - use `ai-engineering:ai-engineering-standards`.

## Questions to ask first

1. What starts the flow, how many times a day, and can the same item trigger it twice?
2. Which environment will it run in for production, and is it built inside a solution from the start?
3. Whose connections will it use in production, and who owns them when the maker moves on?
4. For each AI step, what exact output shape does the next action need, and what happens when the output does not fit?
5. Which actions have an effect outside the flow (send, update, pay, delete), and must anything happen before them?

## Required inputs

- The signed automation design on the `automation-design` template, including AI step definitions and exceptions.
- The target environments, their data policy position and the connectors permitted there.
- The connection model agreed under `automation:automation-connector-governance`.
- Sample inputs, including awkward ones, for build-time testing.

If the design is missing AI step definitions or exception routes, send it back to `automation:automation-process-design`
rather than inventing them in the build.

## Decision framework

Apply the patterns proportionately to the risk tier. Below tier 1 a personal flow may skip some; from tier 1 they are
the default; from tier 2 they are checked at review.

| Area | Pattern | Required from tier |
|---|---|---|
| Structure | Build in a solution; use child flows for reusable steps; keep each flow to one purpose | 1 |
| Configuration | Environment variables for addresses, sites, thresholds and lists; nothing hard-coded | 1 |
| Connections | Connection references, never connections embedded per maker; owned production connections | 1 |
| Triggers | Trigger conditions filter out irrelevant events; duplicate triggers are detected | 1 |
| Idempotency | A key per item so a rerun does not repeat effects; check before create | 2 |
| AI output | Ask for structured output with a defined schema; parse and validate before use; reject and route on failure | 1 |
| Confidence | Threshold from the design; below it, route to review rather than continue | 2 |
| Effects | Actions with external effect come after validation and any approval, never before | 1 |
| Error scopes | Try, catch and finally scopes; failures routed to the exception design | 1 |
| Concurrency | Set deliberately; limit where order or rate matters | 2 |
| Logging | Record item key, AI result, confidence, decision and outcome for each run | 2 |

## Practitioner approach

Start in the right place. Create the flow inside a solution in a development environment, with connection references
and environment variables from the first action. Retrofitting these later is the most common reason flows cannot be
promoted. Name flows, actions and variables so that a support engineer who has never seen the flow can follow it.

Design the trigger carefully. Use trigger conditions so the flow ignores events it should not process, rather than
starting and exiting. Assume every trigger can fire twice: give each item a key and check whether it has already been
processed before any action with an effect. This single pattern prevents most duplicate emails, records and payments.

Treat each AI step as an untrusted input. Ask the model for a defined structure (named fields and allowed values) rather
than prose. Parse the result against a schema, then validate the content: required fields present, values in the
allowed list, numbers in a sensible range, dates real. If any check fails, or the confidence is below the design
threshold, do not continue. Route the item to review or the exception queue with the reason. Never pass free-text AI
output into an action that updates a system or sends a message without validation and, where the design requires it,
human approval.

Keep prompts and thresholds out of the flow logic where possible. Store the prompt in a managed prompt or model asset,
and thresholds in environment variables, so they can be tuned with a controlled change rather than a flow edit.
Record which prompt and model version produced each result.

Place effects last. Read, interpret, validate, approve, then act. Wrap the main path in a try scope, with a catch scope
that records the failure and routes it, and a finally scope that writes the run record. Use
`automation:exception-handling` for retry and fallback rules; do not rely on default retry behaviour for AI steps.

Set concurrency deliberately. Parallel runs speed throughput but break processes where order matters or where a
downstream system limits calls. Use pagination and batching for large lists instead of loops over thousands of items.

Test with the awkward inputs: blank fields, attachments in unexpected formats, very long text, other languages and items
that look like duplicates. Then hand over with a short runbook naming the owner, connections, environment variables and
where failures go.

## Outputs

- A solution-aware flow, or set of flows, built to the patterns above, with connection references and environment variables.
- An AI step specification per AI action: prompt or model reference, output schema, validation rules, threshold and failure route.
- A build checklist recorded against the pattern table, with any deviation justified.
- A short runbook: purpose, owner, trigger, connections, configuration, failure routes and test evidence.

## Microsoft platform considerations

Solutions, connection references, environment variables, trigger conditions, scopes, concurrency control and AI actions
in Power Automate evolve, and Managed Environments add controls that affect how flows are shared and promoted. AI steps
may use Power Platform AI capabilities or call models deployed through Microsoft Foundry through a connector. Check
current behaviour, limits and licensing in `references/sources.md`, and route licensing to the Microsoft licensing guide or
a licensing partner.

## Adoption considerations

Publish the patterns as a short maker guide with a starter solution that already contains the scopes, configuration and
run logging. Makers follow the easy path; make the robust path the easy one. Run review clinics rather than rejecting
flows at the gate.

## Knowledge considerations

Not applicable to most flow patterns, because flows act on records rather than ground on knowledge. Where an AI step uses
reference lists or category definitions, read them from a maintained source at run time rather than pasting them into
the prompt.

## Security and privacy considerations

Production flows run on owned connections or service identities with least privilege, never on a maker's personal
connection. Run logs should record keys and decisions, not full personal data, unless the design justifies it. Data sent
to AI steps is limited to what the task needs.

## Responsible AI considerations

Where AI output triggers an effect on a person, validation and the human review set by `automation:human-in-the-loop`
must sit before the effect in the flow. A threshold set by the maker alone is not acceptable; the process owner agrees it.

## Evaluation requirements

Test each AI step against the sample set in the design and record accuracy against the agreed threshold. Re-run the same
set after any change to prompt, model, schema or threshold, and before promotion to production.

## Value measures

Track flow reliability (successful runs, runs routed to exceptions, failures needing a fix) and the share of AI results
passing validation. The flow owner reports these to the process owner; business value is measured in
`automation:automation-value`.

## Scale notes

### Starter

Use one starter solution with the patterns built in, one development and one production environment, and a short
checklist at hand-over.

### Scale

Maintain a library of child flows for common steps (AI extraction with validation, approval, exception routing) and
review tier 2 flows against the pattern table before promotion.

### Enterprise

Treat shared child flows and AI step components as products with owners, versions and release notes. Promote through
pipelines with automated checks, and use estate inventory to find flows that bypass the patterns.

## Hand-offs

- To `automation:exception-handling` for retry, fallback and exception queue rules.
- To `automation:human-in-the-loop` for review and approval steps.
- To `automation:automation-monitoring` for alerts and run health.
- To `security-privacy:connector-review` when the flow uses new or sensitive connectors.

## Reviewer gates

From risk tier 2, `design-authority` checks the flow against the pattern table and `security-privacy` checks connections,
identities and data flows through `security-privacy:connector-review`. Findings are recorded against the build checklist.

## Failure modes

- AI output is passed straight into an update or send action, and one malformed response corrupts records or emails a customer.
- A duplicate trigger runs the flow twice and creates two orders, payments or messages.
- The flow is built outside a solution on the maker's connections, and breaks the day the maker leaves.
- Default retries resubmit an AI step repeatedly, adding cost and duplicate effects.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Pass unvalidated AI output into an action that changes a system or sends a message.
- Run a production flow on a maker's personal connection.
- Hard-code addresses, sites, thresholds or credentials in flow actions.
- Place an action with external effect before validation and any required approval.

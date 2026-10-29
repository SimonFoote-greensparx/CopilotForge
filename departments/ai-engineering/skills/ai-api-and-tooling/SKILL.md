---
name: ai-api-and-tooling
description: Designs the APIs and shared tooling that custom AI solutions call or expose - contract-first interfaces, narrow tool surfaces a model can use correctly, input validation, user-scoped authorisation, idempotent writes, rate limits, versioning and errors a model can act on. Use when building a service an agent will call as a tool, when exposing an AI capability as an API, or when shared tool libraries are needed across solutions.
license: CC-BY-4.0
metadata:
  department: ai-engineering
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, copilot-studio, m365-agents, github
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, design-authority
  sources: ms-agents-extensibility, ms-agents-compare, ms-foundry-models, ms-copilot-studio-security-governance
  status: draft
  authors: Simon Foote
---

# AI API and tooling

## Purpose

Agents and AI services are only as safe and reliable as the APIs they call and the APIs that expose them. A model chooses
which tool to call and with what arguments based on names, descriptions and schemas, so an API that is fine for a
careful developer can be misused by a model in ways nobody intended. This skill sets the engineering of those interfaces:
narrow, well-described tools, validated inputs, authorisation in the user's context, idempotent writes, limits,
versioning and errors the model can recover from. It goes wrong when an existing broad API is handed to a model as is,
and when tools run with a service identity that can do far more than the user.

## When to use

- A team is building a service that an agent in Foundry, Copilot Studio or Microsoft 365 will call as a tool or action.
- An AI capability (classification, extraction, summarising) is to be exposed as an API for other systems.
- An existing internal API is proposed as an agent tool and its suitability needs checking.
- Several solutions need the same tools, and a shared, owned tool library is wanted.
- A tool is misused by a model, called with wrong arguments or called when it should not be.

## When not to use

- Designing which functions a specific Foundry agent should have - use `ai-foundry:foundry-tool-design`.
- Connecting Model Context Protocol servers and tools to agents safely - use `ai-foundry:mcp-integration`.
- Choosing actions and tools for a Copilot Studio agent - use `copilot-studio:studio-actions-and-tools`.
- Choosing integration patterns between AI and business systems at architecture level - use `ai-architecture:ai-integration-patterns`.
- Identity, secrets and managed identities in detail - use `ai-engineering:secrets-and-identity`.

## Questions to ask first

1. Who or what will call the API - a model choosing tools, application code, or both - and on whose behalf?
2. What is the narrowest set of operations the AI solution actually needs, and which of them change data or send anything?
3. Whose permissions should apply to each call: the signed-in user's, or a service identity's, and why?
4. What happens if the same call arrives twice, or arrives with plausible but wrong arguments?
5. Who will own the API, its versions and its consumers over time?

## Required inputs

- The solution design naming the tools or APIs needed and the agent or systems that will use them.
- The data each operation reads or changes, and its sensitivity.
- The identity model from `ai-architecture:ai-identity-design` or the solution architecture.
- Non-functional targets (latency, volume) from `ai-architecture:ai-non-functional-requirements`.

If the identity model is undecided, design for user-delegated access and mark service identity use as "to confirm" with a
named decision owner. Never default a write tool to a broad service identity.

## Decision framework

Apply each rule to every tool or API operation. From tier 2, a failed rule needs a recorded justification.

| Rule | What good looks like |
|---|---|
| Narrow surface | One operation per tool, doing one thing, rather than a general query or "execute" endpoint |
| Descriptive contract | Clear name, plain description of when to use and when not to, typed parameters with allowed values and examples |
| Contract first | Interface defined in a machine-readable specification before implementation, and versioned |
| Input validation | Server-side checks on every argument; never trust that the model passed valid values |
| Authorisation in context | Calls run with the user's permissions where data is user-scoped; service identities only with narrow, documented scope |
| Read and write separated | Write, send and delete operations are distinct tools, return a preview where effect is material, and require confirmation upstream |
| Idempotency | Writes accept an idempotency key so retries do not repeat effects |
| Useful errors | Errors say what was wrong and what the caller can do, without leaking internals or data |
| Limits | Rate limits, payload limits and timeouts declared and enforced |
| Versioning | Breaking changes get a new version; old versions have a retirement date |
| Logging | Each call logged with caller, user context, operation, outcome and correlation id |

## Practitioner approach

Start from the task, not the existing API. List what the agent or AI service genuinely needs to do, then design the
smallest set of operations that achieves it. An existing API with fifty endpoints and a free-form query parameter is a
poor tool: the model will find uses nobody tested. Wrap it with a narrow facade that exposes only the needed operations.

Write the contract before the code. Define each operation in a machine-readable specification with names, descriptions,
parameters, allowed values and examples. For tools a model will call, the description is part of the prompt: say when
to use the tool, when not to, and what each parameter means in business terms. Test descriptions by asking the model to
choose tools for realistic requests, including near misses, and refine the wording until selection is reliable.

Validate everything on the server. Models produce plausible arguments that may be wrong, out of range or crafted by
injected content. Check types, ranges, allowed values and that referenced records exist and are visible to the user.
Reject with a clear, safe error rather than guessing.

Authorise in the user's context wherever the data is user-scoped. A tool that searches documents or records should
return only what the signed-in user could see. Where a service identity is unavoidable, scope it to the operations the
tool performs, document why and name an owner. Follow `ai-engineering:secrets-and-identity`.

Separate reads from writes, and make writes safe. Give write, send and delete operations their own tools. Where the
effect is material, return a preview the calling solution can show the user for confirmation, then commit with an
idempotency key. Make errors actionable: a model can recover from "the date must be in the future" but not from a stack
trace.

Plan for load and change. Declare and enforce rate limits and timeouts, because agents can call tools in loops. Version
the contract, publish changes to consumers and keep old versions running until a set retirement date. Log every call
with a correlation id so a user's request can be traced through orchestration, model and tool.

Where several solutions need the same tools, package them as a shared library or service with an owner, tests, versions
and documentation, and register them so teams find and reuse them instead of rebuilding.

## Outputs

- A tool and API catalogue for the solution: operations, contracts, descriptions, authorisation model, read or write, idempotency, limits and owner.
- Machine-readable interface specifications, versioned in the solution repository.
- Tool selection test results showing the model picks the right tool for realistic and near-miss requests.
- For shared tooling, a library or service with documentation, versioning policy and a registration in the solution inventory.

## Microsoft platform considerations

Foundry agents, Copilot Studio agents and Microsoft 365 agents consume tools through different mechanisms, including
OpenAPI-described actions, connectors, functions and Model Context Protocol servers; Azure API Management can front and
govern APIs. Supported formats, authentication options and limits change. Check current behaviour in
`references/sources.md` before choosing an interface style, and record what was checked.

## Adoption considerations

Makers and engineers reuse tools they can find and trust. Publish shared tools with clear documentation, examples and
an owner to contact, and make the shared route easier than building a private copy.

## Knowledge considerations

Not applicable to most API design, because tools act on systems rather than ground on content. Where a tool performs
retrieval, its results must respect the knowledge owner's access rules; see `ai-foundry:retrieval-design`.

## Security and privacy considerations

Tools are the main route by which prompt injection turns into action. Validate inputs, authorise per user, keep writes
narrow and confirmed, avoid returning more data than the task needs, and log calls. Tools that reach personal data or
external services go to `security-privacy:connector-review`.

## Responsible AI considerations

Tools that change records about people, send messages or make decisions need human confirmation upstream and an audit
trail. Design previews so the person confirming can see what will actually happen, in plain language.

## Evaluation requirements

Include tool selection and argument accuracy in the evaluation harness, with near-miss requests and injected content.
Contract tests check every tool against its specification on each change; see `ai-engineering:ai-solution-testing`.

## Value measures

Track reuse of shared tools across solutions, tool call error rates, rejected invalid arguments and incidents caused by
tool misuse. The AI engineering lead owns these measures at portfolio level.

## Scale notes

### Starter

Expose a few narrow read tools with user-delegated access and clear descriptions. Avoid write tools until confirmation
and idempotency are in place.

### Scale

Introduce contract-first design for all tools, a shared tool library for common systems, an API gateway for limits and
logging, and tool selection tests in the pipeline.

### Enterprise

Run a governed internal catalogue of AI tools and APIs with owners, versions, consumers and retirement dates, and
review new write-capable tools centrally.

## Hand-offs

- To `ai-foundry:foundry-tool-design` to wire tools into a specific Foundry agent.
- To `ai-engineering:secrets-and-identity` for identities and credentials.
- To `ai-engineering:ai-solution-testing` for contract and tool selection tests.
- To `security-privacy:connector-review` for write tools and external data flows from tier 2.

## Reviewer gates

From risk tier 2, `security-privacy` reviews authorisation, validation and write controls, and a write tool running on a
broad service identity beyond user rights is blocking. `design-authority` checks contracts, versioning and reuse of
shared tools.

## Failure modes

- A broad internal API is handed to a model unchanged, and the model finds operations nobody intended it to use.
- A tool trusts model-supplied arguments, and injected content causes it to act on the wrong record.
- A write tool has no idempotency key, a retry repeats the effect and a customer receives two messages.
- A tool returns full records when a summary would do, exposing data the user did not need.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Expose a general query or execute endpoint to a model as a tool.
- Trust model-supplied arguments without server-side validation.
- Run a write tool under a service identity with rights beyond what the user and task require.
- Make breaking changes to a tool contract without a new version and notice to consumers.

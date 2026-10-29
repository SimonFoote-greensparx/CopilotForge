---
name: foundry-tool-design
description: Designs the individual tools and functions a Foundry agent can call - name, description, input and output schema, side effects, identity, confirmation, error behaviour and limits - so the model calls them correctly and they cannot be misused. Use when an agent's tool list is agreed and each tool needs a contract, when an agent calls tools wrongly, or before a write action goes live.
license: CC-BY-4.0
metadata:
  department: ai-foundry
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, entra
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, evaluation-quality
  sources: ms-foundry-models, ms-agents-extensibility, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Foundry tool design

## Purpose

A tool is the point where an agent stops talking and starts doing, so a badly designed tool turns a model's
misunderstanding into a real-world effect. This skill gives each tool or function a contract the model can use
reliably and the organisation can defend: a clear purpose, a tight schema, known side effects, the right identity and a
human checkpoint where the effect matters. Tool design goes wrong when existing APIs are exposed wholesale, when
descriptions are written for developers rather than for the model, and when write tools have no limits or confirmation.

## When to use

- `ai-foundry:foundry-agent-architecture` has produced a tool inventory and each tool needs a contract.
- An agent calls the wrong tool, passes malformed arguments or loops on a failing call.
- A read-only agent is about to gain its first write or send action.
- A team proposes exposing an existing API to an agent as-is.

## When not to use

- Deciding which tools an agent should have at all, and its overall shape - use `ai-foundry:foundry-agent-architecture`.
- Connecting a Model Context Protocol server rather than designing a function - use `ai-foundry:mcp-integration`.
- Designing the underlying business API the tool wraps - use `ai-engineering:ai-api-and-tooling`.
- Designing actions for a Copilot Studio agent - use `copilot-studio:studio-actions-and-tools`.
- Formal security testing of the finished tools - that is the reviewer skill `security-privacy:ai-security-testing`.

## Questions to ask first

1. What single job does this tool do, and how will the model know when to use it rather than another tool?
2. Does it only read, or does it create, change, send, delete or spend, and can the effect be undone?
3. Whose identity does it run with, and what is the most it could do if called with the worst plausible arguments?
4. What should happen when it fails, times out or returns nothing?
5. Who owns the system behind it, and have they agreed to agent access?

## Required inputs

- The agent architecture with the tool inventory and the identity approach per action.
- Documentation of the underlying API or system, and its owner's agreement to agent access.
- The data classification of what the tool reads and returns.
- The risk tier and any human-oversight requirements already set.

Where the system owner has not agreed access, or the classification is unknown, mark the tool `[To confirm: ...]` and
leave it out of the build. Never wire a tool to a system on the assumption that its owner will agree later.

## Decision framework

Classify each tool by effect, then apply the controls for its class. Controls accumulate down the table.

| Effect class | Examples | Minimum controls |
|---|---|---|
| Read, low sensitivity | Look up opening hours, product facts | Narrow schema, result size limit, clear description |
| Read, sensitive | Customer record, case history | Plus user-delegated identity or explicit trimming, logging of access |
| Reversible write | Draft a record, create a task | Plus idempotency key, the agent shows what it will do before doing it |
| Irreversible or external effect | Send an email, submit an order, change access, make a payment | Plus mandatory human confirmation, value or scope limits, rate limits, audit trail |
| Prohibited for agents | Decided by risk classification or policy | Not exposed; the agent hands over to a person or process |

Prefer several narrow tools over one general tool. A tool that accepts free-text queries or arbitrary operations is
treated as the highest class its underlying system allows.

## Practitioner approach

Write the tool description for the model, not for a developer. Say what the tool does, when to use it, when not to,
and what each parameter means, in plain sentences. The model chooses tools largely from these descriptions, so vague
or overlapping descriptions are the commonest cause of wrong calls. Read all of an agent's tool descriptions side by
side and remove overlaps the way you would for neighbouring skills.

Make schemas tight. Use enumerations rather than free text where the values are known, required fields rather than
optional ones where the tool cannot work without them, and explicit formats for dates, identifiers and amounts. Return
only what the agent needs, in a compact structure, with a size limit; returning whole records wastes tokens and leaks
data into the conversation that the user may not be entitled to see.

Never expose an existing API wholesale. Wrap it in a purpose-built function that does one job and calls only the
operations that job needs. This is where most least-privilege failures start: the API can delete, so the agent can
delete.

Decide identity per tool with the agent architecture. User-delegated calls keep the user's permissions in force;
managed identity calls need scoping and a recorded reason. For any tool that reads content from outside the
organisation or from user-supplied documents, assume that content can carry instructions aimed at the model, and make
sure no tool can be triggered with elevated effect purely by what it reads.

Design failure behaviour. Return structured errors the model can act on, such as "not found" or "not permitted",
rather than stack traces. Set timeouts and retry rules, make write tools idempotent, and stop the agent looping on a
failing call. For irreversible tools, the agent proposes the action with its arguments and a person confirms; record
the confirmation in the audit trail.

Test each tool on its own before testing the agent: correct calls, malformed arguments, permission failures and
attempts to push it beyond its limits. Record each contract in the tool register within the `foundry-solution-design`
template, with owner, class, identity, controls and test evidence. State what design cannot guarantee: the model may
still choose a tool wrongly, which only evaluation and confirmation steps catch.

## Outputs

- A tool contract per tool in the `foundry-solution-design` template: purpose, model-facing description, schema, effect class, identity, controls, failure behaviour, owner and test evidence.
- A side-by-side review of tool descriptions with overlaps removed.
- Unit test cases for each tool, handed to `ai-engineering:ai-solution-testing`.

## Microsoft platform considerations

Foundry agents can call several kinds of tools, including functions the organisation hosts, built-in tools and
connections to other services, and the available types and their authentication options change. Check the current
source records for which tool types support user-delegated identity, how approvals can be required and which
capabilities are in preview. Host custom functions inside the organisation's Azure governance with managed identities
rather than stored keys.

## Adoption considerations

Not applicable to most tool design, because users experience outcomes rather than tools. Where a tool requires user
confirmation, design the confirmation text with the business owner so people understand what they are approving.

## Knowledge considerations

Not applicable for action tools. Where a tool retrieves knowledge, its design belongs with
`ai-foundry:retrieval-design` so trimming, freshness and citation are handled consistently.

## Security and privacy considerations

Each tool is an attack surface for prompt injection, privilege misuse and data leakage. Apply least privilege, return
minimal data, log access to sensitive data, and require human confirmation for irreversible effects.
`security-privacy:ai-security-testing` tests the tools at tier 2 and above.

## Responsible AI considerations

Tools that affect people, money, safety or rights need confirmation by an accountable person and an audit trail, agreed
with `responsible-ai:human-oversight`. Some actions should never be delegated to an agent; record those as prohibited.

## Evaluation requirements

Evaluate tool selection accuracy, argument correctness and refusal to call tools outside scope, using cases that
include ambiguous requests and injected instructions. Agree thresholds per effect class before testing; irreversible
tools need near-perfect confirmation behaviour.

## Value measures

Measure task completion through the tool, wrong-call rate and confirmation decline rate at solution level, owned by the
solution owner. A high decline rate signals that the agent proposes actions people do not want.

## Scale notes

### Starter

Start with read tools only, then add one reversible write tool with confirmation. Keep the tool count small enough that
every description can be read together.

### Scale

Keep a shared library of reviewed tool wrappers for common systems, so agents reuse contracts and controls rather than
reinventing them.

### Enterprise

Maintain a tool registry with owners, effect classes and identities across all agents, and require security review
before any irreversible tool is added to any agent.

## Hand-offs

- To `ai-engineering:ai-api-and-tooling` for the underlying APIs and hosting.
- To `ai-engineering:secrets-and-identity` for managed identity and secret handling.
- To `ai-foundry:model-evaluation` for tool-calling evaluation.
- To `ai-foundry:foundry-observability` so tool calls are traced.

## Reviewer gates

From risk tier 2, `security-privacy` reviews each tool's identity, data exposure and controls, and `evaluation-quality`
checks the tool-calling evidence. Any irreversible tool without human confirmation is a finding at any tier.

## Failure modes

- An existing API is exposed whole, and the agent can perform operations nobody intended it to have.
- Two tools have overlapping descriptions, and the model alternates between them unpredictably.
- A tool returns full records, and sensitive fields appear in answers to users who should not see them.
- A failing tool returns an unhelpful error, and the agent retries in a loop, consuming tokens and rate limits.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Expose an existing API wholesale to an agent.
- Allow an irreversible or external-effect tool to run without human confirmation and an audit trail.
- Store keys or secrets in tool definitions, prompts or code.
- Wire a tool to a system whose owner has not agreed to agent access.

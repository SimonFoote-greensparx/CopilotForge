---
name: studio-actions-and-tools
description: Designs the tools a Copilot Studio agent can call - connector actions, agent flows, prompts, custom connectors, REST APIs and MCP servers - with names and descriptions the orchestrator can use, typed inputs and outputs, read versus write, user confirmation, identity and failure behaviour. Use when an agent must do more than answer, when it calls the wrong tool or fills inputs badly, or when a write action needs safeguards.
license: CC-BY-4.0
metadata:
  department: copilot-studio
  lifecycle: Deliver, Assure
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-studio, power-platform, azure
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, design-authority
  sources: ms-copilot-studio-guidance, ms-agents-extensibility, ms-copilot-studio-security-governance, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Studio actions and tools

## Purpose

Tools are where a Copilot Studio agent stops talking and starts changing things: creating a request, updating a record,
sending a message. This skill designs each tool so the orchestrator chooses it at the right moment, fills its inputs
correctly, asks the user before anything irreversible, runs under an appropriate identity and fails in a way the user
can understand. Tool design usually goes wrong through vague descriptions that make the agent call the wrong thing,
write actions that run without confirmation, and errors that vanish so the user believes something happened when it did not.

## When to use

- The solution design includes any action beyond answering from knowledge.
- The agent calls the wrong tool, calls tools unprompted, or fills inputs with invented values.
- A write, send or delete action is being added, or an existing tool's audience is widening.
- A team proposes exposing a REST API, custom connector or MCP server to an agent.

## When not to use

- Choosing and governing the connectors and connections themselves - use `copilot-studio:studio-connectors`.
- Building the Power Automate flow behind a tool - use `copilot-studio:power-automate-actions`.
- Governing an MCP server as a platform integration - use `ai-foundry:mcp-integration`.
- Designing tools for agents built on Foundry Agent Service - use `ai-foundry:foundry-tool-design`.
- The formal security review of a tool's permissions - use `security-privacy:connector-review`.

## Questions to ask first

1. What outcome does the user need, and what is the smallest operation in which system that achieves it?
2. Does the tool read, create, update, send or delete, and can its effect be undone?
3. Whose identity should the operation run under, and can the end user already do this themselves?
4. Which inputs come from the user, which from context, and which must never be guessed?
5. What should the user see if the target system is slow, unavailable or refuses the request?

## Required inputs

- The action register from `copilot-studio:studio-agent-design`.
- The target system's owner, the operations available and their permission model.
- The connector or integration route confirmed by `copilot-studio:studio-connectors`.
- The risk tier, which sets the confirmation and review depth.

If the system owner has not agreed to the agent acting on their system, the tool is not built. Missing permission
models are recorded as preconditions, never assumed.

## Decision framework

Choose the simplest tool type that does the job, then apply controls by effect.

| Tool type | Use it when | Watch for |
|---|---|---|
| Prebuilt connector action | A single operation exists on a governed connector | Connection identity and data policy classification |
| Agent flow or Power Automate flow | Several steps, systems or conditions are needed | Response time inside a conversation and error returns |
| Prompt tool | A bounded language task (classify, extract, rewrite) with structured output | Treat output as untrusted input to later steps |
| Custom connector or REST API | No connector exists and the API is owned and documented | Ownership, authentication and versioning of the API |
| MCP server | An owned server exposes several tools that will be reused | Which tools are exposed, and changes made on the server without the agent owner knowing |

| Effect | Minimum control |
|---|---|
| Read | Runs as the end user where possible; outputs limited to fields the user needs |
| Create or update | User sees a summary and confirms; result echoed back with a reference |
| Send, delete or financial effect | Explicit confirmation, run as the user, audit trail, and human approval from tier 3 |

## Practitioner approach

Start with the user's outcome and work back to the operation. "Book leave" might be one connector action or a flow that
checks balance, creates the request and notifies a manager. Choose the smallest operation that achieves the outcome; a
broad tool such as "update any record" gives the orchestrator too much room.

Name and describe each tool for the orchestrator. The description should say what the tool does, when to use it, when
not to, and what it returns, in the language users use. Describe each input with its type, format, allowed values and
whether it may be inferred from the conversation or must be asked. Mark inputs such as amounts, dates and recipients as
"ask the user" rather than letting the model fill them from context. Invented inputs are the most damaging tool failure,
because the action succeeds with the wrong values.

Decide confirmation by effect, not by convenience. Before any create, update, send or delete, show the user what will
happen in plain language and ask them to confirm. After the action, echo the result with a reference the user can
check. For irreversible or high-impact actions at tier 3 and above, route to a human approval step through
`automation:human-in-the-loop` rather than relying on chat confirmation alone.

Set identity per tool. Running as the end user means the agent can do nothing the user could not already do, which is
the right default. Where a shared or service connection is proposed, record why, scope it to the minimum operations and
data, and get approval from the system owner and the security reviewer.

Design failure. Every tool should return a clear success or failure with a reason the agent can explain, and the
conversation should offer a next step, such as trying again later or contacting a named support route. Never let a
failure look like success. Return only the fields the agent needs, because everything returned may be shown to the user
and stored in transcripts.

Treat tool output, especially from prompts, external APIs and MCP servers, as untrusted input. Content returned by a tool
can contain instructions that try to redirect the agent; do not let it trigger further write actions without the same
confirmation. Test each tool directly, through orchestration with realistic phrasing, and with the target system unavailable.

## Outputs

- A tool specification per tool: purpose, type, description, inputs with type and source, outputs, effect, confirmation, identity, failure behaviour and owner.
- The updated action register in the `studio-solution-design`, with approvals for any shared or service identity.
- Test cases for correct selection, input handling, confirmation, permission denial and system failure.

## Microsoft platform considerations

Copilot Studio supports several tool types, including connector actions, flows, prompts, custom connectors, REST APIs
and Model Context Protocol servers, and their configuration, authentication options and preview status change often.
Check `ms-copilot-studio-guidance` and `ms-agents-extensibility` for current options, and
`ms-copilot-studio-security-governance` for admin controls over tools and connectors.

## Adoption considerations

Users trust agents that tell them what they are about to do and confirm what they did. Include the agent's actions and
their limits in launch messages, so users know what it can change on their behalf.

## Knowledge considerations

Not applicable for tool mechanics, because tools act on systems rather than ground answers; where a tool reads records
to answer questions, design it with `copilot-studio:studio-knowledge-architecture` so sources do not contradict each other.

## Security and privacy considerations

Least privilege per tool, end-user identity by default, minimal returned fields and no secrets in tool configuration.
Tool outputs flow into transcripts, so personal data returned by a tool is retained with the conversation. Every new
write tool goes to `security-privacy:connector-review`.

## Responsible AI considerations

Actions that affect people, money or access need a clear human decision point. Record where the agent acts on a user's
instruction and where a person approves, and make sure users can see and reverse what the agent did where reversal is possible.

## Evaluation requirements

Test tool selection with realistic phrasing, input handling with missing and ambiguous values, confirmation on every
write, behaviour under denied permissions and when the system is unavailable. Writing without confirmation is a
zero-tolerance failure.

## Value measures

Track tool success and failure rates, confirmations declined, and the business outcome the action supports, for example
requests completed without a hand-off. The agent owner reports them at agent level, never by individual user.

## Scale notes

### Starter

Read-only tools and simple create actions on governed connectors, with confirmation and end-user identity. Defer
anything needing a service identity until there is a reviewer.

### Scale

Publish tool description standards and reusable, reviewed tools for common systems, so makers reuse a governed "create
service request" tool rather than building their own.

### Enterprise

Maintain a catalogue of approved tools and MCP servers with owners and versions, require security review for every new
write tool, and monitor tool failures centrally.

## Hand-offs

- To `copilot-studio:studio-connectors` for connector choice, connections and data policy fit.
- To `copilot-studio:power-automate-actions` for flow-based tools.
- To `security-privacy:connector-review` for every write tool and every shared identity.
- To `copilot-studio:studio-testing-and-evaluation` with the tool test cases.

## Reviewer gates

From risk tier 1 for write tools and tier 2 for read tools, `security-privacy` reviews identity, scope, returned data and
confirmation. From tier 2, `design-authority` reviews whether the tool type and granularity are appropriate. A write tool
without confirmation, or a shared identity without approval, is a blocking finding.

## Failure modes

- Two tools have similar descriptions and the orchestrator calls the one that writes when the user wanted to look something up.
- The model fills a required amount or recipient from earlier context, and the action succeeds with the wrong value.
- A tool runs under the maker's connection, so every user acts with the maker's rights.
- A flow fails silently and the agent tells the user their request was submitted.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Let an agent create, update, send or delete without showing the user what will happen and asking them to confirm.
- Allow the model to invent values for amounts, dates, recipients or identifiers.
- Expose a broad "do anything" tool when a narrow operation would do.
- Let content returned by a tool trigger further write actions without confirmation.

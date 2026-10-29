---
name: power-automate-actions
description: Designs Power Automate flows that a Copilot Studio agent calls as tools - when a flow is the right action, its input and output contract, response time within a conversation, the identity it runs under, error returns the agent can explain, solution packaging and flow ownership. Use when an agent needs a multi-step or cross-system action, when a flow called by an agent times out or fails silently, or when a maker wants to reuse an existing flow.
license: CC-BY-4.0
metadata:
  department: copilot-studio
  lifecycle: Deliver, Assure
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-studio, power-platform
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, design-authority
  sources: ms-copilot-studio-guidance, ms-copilot-studio-security-governance, ms-coe-starter-kit
  status: draft
  authors: Simon Foote
---

# Power Automate actions

## Purpose

Flows let a Copilot Studio agent do multi-step work across systems: check a balance, create a request, notify an
approver and return a reference. This skill designs flows specifically as agent tools, with a clean contract between the
conversation and the flow, a response the user can wait for, an identity that matches the user's rights, and errors the
agent can explain. Flows called by agents usually go wrong when an existing automation is reused without regard to who
it runs as, when a slow flow leaves the user waiting with no answer, or when the flow fails and the agent reports success.

## When to use

- A tool in the solution design needs several steps, several systems or conditional logic.
- A maker wants to call an existing cloud flow from an agent.
- A flow called by an agent times out, returns nothing useful or fails without the user knowing.
- Long-running work, such as an approval, must start from a conversation and finish later.

## When not to use

- Designing what the tool does, its description, inputs and confirmation - use `copilot-studio:studio-actions-and-tools`.
- General robust flow patterns for automations not called by agents - use `automation:flow-design-patterns`.
- Designing human approval steps in depth - use `automation:human-in-the-loop`.
- Retry, exception and failure handling across automation estates - use `automation:exception-handling`.
- Choosing and governing the connectors inside the flow - use `copilot-studio:studio-connectors`.

## Questions to ask first

1. What exactly must the flow do, in which systems, and what must it return to the conversation?
2. Can the work complete while the user waits, or does it need to continue after the conversation?
3. Whose identity should each step use - the user's, or a scoped service connection - and does that match the tool's identity design?
4. What should the user be told for each way the flow can fail?
5. Is there an existing flow that does this, who owns it, and was it designed to be called by an agent?

## Required inputs

- The tool specification from `copilot-studio:studio-actions-and-tools`, including confirmation and identity.
- The connector register from `copilot-studio:studio-connectors`.
- The target systems' owners and any business rules the flow must respect.
- The solution and environments the agent lives in, from `copilot-studio:studio-alm`.

If the owner of a reused flow is unknown or has left, treat the flow as unowned and do not call it from an agent until
ownership is assigned.

## Decision framework

| Situation | Pattern |
|---|---|
| Work completes quickly and the user needs the result | Synchronous flow returning a typed result and a status |
| Work takes longer or waits for a person | Start the work, return a reference immediately, notify the user when it completes |
| Steps must happen exactly once, even if the agent retries | Idempotent design: check for an existing record before creating one |
| An existing flow does almost the right thing | Create a purpose-built child flow for the agent rather than adding agent branches to a business-critical flow |
| The logic is a single connector call | Use a connector action directly, not a flow |

Every agent flow returns a status (success, failed with a reason the user can act on, or failed with a support route) and
only the fields the conversation needs.

## Practitioner approach

Write the contract first. Define the inputs the agent will pass, with types, formats and which are mandatory, and the
outputs the flow will return, including a status and a short message the agent can use. A clear contract lets the maker
building the flow and the maker building the agent work independently, and it makes testing straightforward.

Design for the conversation's patience. Users will wait a few seconds for an answer; they will not watch a spinner while
an approval sits in someone's inbox. If any step can take longer than the conversation can comfortably hold, split the
work: the flow starts the process, returns a reference straight away, and a separate notification tells the user when it
is done. Check the current response-time behaviour for agent flows in the source records rather than assuming a limit.

Set identity per step to match the tool design. A flow can run some steps under the user's connection and others under a
service connection. Default to the user so the agent cannot exceed their rights; where a step needs a service
connection, keep it to that step, scope the account and record the approval. Never reuse a flow that runs under a
departed or personal account.

Make failures visible and useful. Wrap the main steps so any failure returns a structured status rather than an
unhandled error. Map each likely failure - system unavailable, permission denied, validation failed, duplicate found - to a
message the agent can give and a next step for the user. Log enough to diagnose without logging personal data the
investigation does not need.

Make writes safe to repeat. Conversations retry and users click twice. Before creating a record, check whether the same
request was already created, and return the existing reference if so.

Package and own it. Build the flow in the agent's solution, use connection references and environment variables, give it
a clear name that says it is called by an agent, and record an owner and a co-owner. Reusing a business-critical flow by
adding agent branches couples two products; build a small agent-facing flow that calls shared child flows instead.

Test the flow on its own with the contract, then through the agent with realistic phrasing, then with each target system
unavailable.

## Outputs

- A flow contract: inputs, outputs, status values, user-facing messages and response-time pattern.
- A flow design: steps, identity per step, idempotency check, error handling and logging.
- Ownership and packaging details recorded in the `studio-solution-design` and the `alm-and-environment-plan`.
- Test cases for success, each failure path, repeat submission and slow or unavailable systems.

## Microsoft platform considerations

How agents call flows, what flow types are available to agents, time-outs, run-as options and how flow runs are billed
or counted change over time. Check `ms-copilot-studio-guidance` for current behaviour and
`ms-copilot-studio-security-governance` for controls; send any licensing or capacity question to
`platform-governance:ai-licensing-and-capacity`. The `ms-coe-starter-kit` record helps find existing flows and their owners.

## Adoption considerations

Users judge the agent by whether their request actually happened. Return references they can check and send completion
notices for longer work, so they do not fall back to the old route "just in case".

## Knowledge considerations

Not applicable, because flows called as tools perform actions rather than supply grounding; where a flow retrieves data
for answers, treat its output as a source and agree it with `copilot-studio:studio-knowledge-architecture`.

## Security and privacy considerations

Least privilege per step, no personal or departed accounts, secrets in a managed store, and logs that avoid unnecessary
personal data. Flow inputs come from a conversation and are untrusted: validate them before use in queries or messages.
New service connections go to `security-privacy:connector-review`.

## Responsible AI considerations

Flows that change entitlements, money or access need a human decision point; design it with `automation:human-in-the-loop`
and make sure the agent tells users when a person still has to approve.

## Evaluation requirements

Test the contract directly, through the agent, under each failure, with repeated submissions and under users who lack
rights. A failure that the agent reports as success is a zero-tolerance failure.

## Value measures

Track flow success rate, failure reasons, average completion time and requests completed end to end through the agent,
owned by the flow owner and reported at agent level.

## Scale notes

### Starter

Simple synchronous flows in the agent's solution, running as the user, with a status and message returned for every path.

### Scale

Shared child flows for common operations, a standard contract format and naming convention for agent-called flows, and
failure alerts to owners.

### Enterprise

Treat agent flows as integration components with versioning, dependency tracking across agents, central monitoring and
change control agreed with the owners of target systems.

## Hand-offs

- To `copilot-studio:studio-actions-and-tools` to finalise the tool description and confirmation.
- To `automation:human-in-the-loop` for approval steps.
- To `security-privacy:connector-review` for service connections.
- To `copilot-studio:studio-testing-and-evaluation` with the flow test cases.

## Reviewer gates

From risk tier 2, `security-privacy` reviews identities, inputs and logging, and `design-authority` reviews coupling with
existing flows and supportability. A flow that runs under a personal account for other users is a blocking finding.

## Failure modes

- An existing flow is reused and runs as its original maker, so every agent user acts with that maker's rights.
- A slow step makes the conversation time out while the flow later completes, and the user submits again.
- An unhandled error returns nothing and the agent says the request was submitted.
- Agent branches are added to a business-critical flow, and a change for the agent breaks the business process.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Call a flow from an agent without a defined input and output contract and a status for every path.
- Reuse a flow whose owner is unknown or that runs under a personal or departed account.
- Leave a user waiting on long-running work with no reference or follow-up.
- Assert flow time-outs, run limits or licence implications from memory.

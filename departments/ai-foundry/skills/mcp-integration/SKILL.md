---
name: mcp-integration
description: Integrates Model Context Protocol servers with Microsoft Foundry agents safely - vetting who runs each server, allowing only the tools needed, authentication and identity, approval for consequential calls, pinning versions and handling changes in what a server offers. Use when a team wants to connect an MCP server to a Foundry agent, when an internal service should be exposed over MCP, or when a connected server changes its tools.
license: CC-BY-4.0
metadata:
  department: ai-foundry
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, entra
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, design-authority
  sources: ms-foundry-models, ms-agents-extensibility, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# MCP integration

## Purpose

The Model Context Protocol lets an agent discover and call tools offered by a server, which makes it quick to give a
Foundry agent new capabilities and equally quick to give it capabilities nobody reviewed. This skill decides whether a
given server may be connected, which of its tools the agent may use, under which identity, with what approval, and how
changes on the server side are noticed before they change the agent's behaviour. MCP integration goes wrong when a
public server is connected because a demonstration looked useful, when every tool a server advertises is allowed by
default, and when the server's owner changes a tool description that the agent then follows.

## When to use

- A team wants to connect an existing MCP server, internal or external, to a Foundry agent.
- An internal service is to be exposed over MCP so several agents can use it.
- A connected server has added, removed or changed tools, or changed its owner or hosting.
- A prototype agent uses MCP servers informally and needs a production integration design.
- Reviewers ask who runs a server the agent depends on and what data it sees.

## When not to use

- Designing the contract of a function the organisation hosts itself for one agent - use `ai-foundry:foundry-tool-design`.
- Deciding which capabilities the agent needs at all - use `ai-foundry:foundry-agent-architecture`.
- Choosing integration patterns across the estate, of which MCP is one option - use `ai-architecture:ai-integration-patterns`.
- Adding MCP servers to a Copilot Studio agent - use `copilot-studio:studio-actions-and-tools`.
- Reviewing connectors, tools and MCP servers at the security gate - that is the reviewer skill `security-privacy:connector-review`.

## Questions to ask first

1. Who builds, hosts and operates the server, under what terms, and what happens to the data the agent sends it?
2. Which of the server's tools does the agent actually need, and which of those read, write, send or spend?
3. How does the server authenticate the agent and, where relevant, the user, and whose permissions apply to each call?
4. How will the organisation learn that the server's tools, descriptions or behaviour have changed?
5. What should the agent do when the server is slow, unavailable or returns something unexpected?

## Required inputs

- The agent architecture with its tool inventory and identity approach, on the `foundry-solution-design` template.
- Documentation of the server: owner, hosting location, tool list, authentication options and versioning.
- The data classification of what the agent would send to and receive from the server.
- Agreement from the owner of any system the server acts on.

Where the server's owner, hosting or data handling cannot be established, mark them `[To confirm: ...]` and do not
connect it. A server nobody can vouch for is treated as untrusted, whatever its popularity.

## Decision framework

| Server type | Default position | Conditions to connect |
|---|---|---|
| Built and run by the organisation inside its Azure governance | Preferred | Owner named, tools reviewed, managed identity or user-delegated access, versioned releases |
| Provided by Microsoft or a supplier under contract | Acceptable | Terms and data handling reviewed, tools allow-listed, authentication per user where data is personal |
| Public or community server run by an unknown party | Not for production | Only in an isolated sandbox with no organisational data, or rebuilt or hosted internally after review |

| Tool effect | Control |
|---|---|
| Read, non-sensitive | Allow-listed, result size bounded |
| Read, sensitive | Plus user-delegated access and access logging |
| Write, send, delete or spend | Plus approval before each call and an audit trail; prefer an organisation-built tool designed with `ai-foundry:foundry-tool-design` |

Allow only named tools. A server connection that exposes every advertised tool is treated as the highest effect class
among them.

## Practitioner approach

Establish provenance before capability. Find out who wrote the server, who runs it, where it is hosted and what it does
with requests. An MCP server can see everything the agent sends it, including user questions and retrieved content, and
can return text the model will read as context. Treat a server you cannot vouch for as an untrusted party in the
conversation. For public servers, the usual answer is to rebuild or host a reviewed copy inside the organisation's
governance rather than connecting to someone else's endpoint.

List the server's tools and decide which the agent needs. Allow those by name and block the rest, even if the platform
would expose everything by default. Read each tool's description as the model will read it; a description written to
attract the model's attention, or one that contains instructions, is a warning sign. Remove tools whose descriptions
overlap with the agent's other tools.

Design identity per tool. Where the server reaches organisational data, prefer user-delegated access so the user's
permissions apply. Where a service identity is unavoidable, scope it to the least the allowed tools need and record why.
Never place long-lived keys in agent configuration; use a managed secret store and identities designed with
`ai-engineering:secrets-and-identity`.

Require approval for consequential calls. Any tool that writes, sends, deletes or spends should need a person to
confirm before it runs, with the arguments shown in plain language. For tier 2 and above, approval should be the
default for every call until evaluation shows read-only tools behave predictably.

Control change. Pin to a known server version or record a fingerprint of its tool list and descriptions, and check it on
a schedule and before each release. A new tool, a changed description or a new required scope is a change to the agent
and goes through review. Agree with internal server owners that they announce changes; for external servers, assume
they will not.

Plan for failure. Set timeouts, decide what the agent tells the user when a server is unavailable, and stop the agent
retrying in a loop. Trace every MCP call with server, tool, version and latency so problems can be diagnosed.

Record the integration in the MCP section of the solution design. State what remains uncertain, such as how an external
server handles data after a call, which only contract terms can settle.

## Outputs

- An MCP server register entry in the `foundry-solution-design` template per server: owner, hosting, terms, allowed tools, effect class, identity, approval rule, version pin and change check.
- An allow-list of tools per agent with the reason each is needed.
- Test cases for each allowed tool, including injected content in server responses, handed to `ai-engineering:ai-solution-testing`.

## Microsoft platform considerations

Foundry Agent Service and the wider Microsoft agent platforms are adding MCP support quickly, and the available
authentication methods, approval settings, hosting options and preview status vary and change. Check the current
source records before relying on a capability, such as per-tool allow-listing or user-delegated authentication to an
MCP server. Where the same server is used by Copilot Studio or Microsoft 365 agents, align the review so the server is
assessed once and its approved tool list is shared.

## Adoption considerations

Not applicable for most integrations, because users experience the agent rather than the server. Where approvals are
required, write the approval prompt with the business owner so people understand what they are confirming.

## Knowledge considerations

Where an MCP server supplies knowledge rather than actions, its content needs an owner and freshness route like any
other source, and its retrieval behaviour should be checked with `ai-foundry:retrieval-design`.

## Security and privacy considerations

An MCP server is both a data recipient and a source of untrusted text, so it carries exfiltration and indirect injection
risk. Confirm what data leaves the organisation, apply least privilege and user-delegated access, and require approval
for consequential calls. `security-privacy:connector-review` reviews each server from tier 2, and personal data sent to
an external server needs the DPO's view.

## Responsible AI considerations

Actions taken through an MCP tool are the agent's actions in the eyes of the people affected. Consequential calls need
a human checkpoint agreed with `responsible-ai:human-oversight`, and users should be able to see which external service
acted on their behalf.

## Evaluation requirements

Evaluate tool selection, argument correctness and refusal to call disallowed tools, including cases where a server
response contains instructions. Re-run the evaluation whenever the server's tool list or descriptions change.

## Value measures

Track successful task completion through MCP tools, failed or timed-out calls and approval decline rates at solution
level, owned by the solution owner. Count servers connected without review as a governance measure.

## Scale notes

### Starter

Connect only internally built or contracted servers, allow a small number of read-only tools, and check the tool list
manually before each release.

### Scale

Keep a shared register of reviewed MCP servers with approved tools, so agents reuse reviewed integrations instead of
repeating the work, and automate the tool-list change check.

### Enterprise

Run internal MCP servers as governed products with owners, versioning and change notice, route all external servers
through a central review, and monitor for unregistered server connections.

## Hand-offs

- To `security-privacy:connector-review` for the gate review of each server.
- To `ai-foundry:foundry-tool-design` when a server tool should be replaced by an organisation-built function.
- To `ai-engineering:secrets-and-identity` for credentials and identities.
- To `ai-foundry:foundry-observability` so MCP calls are traced.
- To `platform-governance:ai-solution-inventory` to record server dependencies.

## Reviewer gates

From risk tier 2, `security-privacy` reviews provenance, data flows, identity and approval rules for each server, and
`design-authority` checks the integration conforms to the reference architecture. A public server connected to
production with organisational data is a blocking finding at any tier.

## Failure modes

- A public server is connected for convenience, and user questions and retrieved documents flow to an unknown party.
- Every advertised tool is allowed, and the agent calls a delete operation nobody knew the server offered.
- A server owner rewrites a tool description, and the agent starts calling it for requests it was never meant to handle.
- A slow external server makes the agent retry repeatedly, exhausting quotas and leaving users waiting.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Connect a production agent to an MCP server whose owner, hosting and data handling are unknown.
- Allow every tool a server advertises instead of a named allow-list.
- Let a write, send, delete or spend tool run without approval and an audit trail.
- Treat a change to a server's tools or descriptions as anything other than a change to the agent.

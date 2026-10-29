---
name: ai-integration-patterns
description: Chooses how an AI solution connects to business systems - standard or custom connectors, flows as actions, APIs, MCP servers, events, Dataverse or Graph - deciding direction, identity, synchronous or asynchronous timing, write confirmation and failure behaviour for each interface. Use when an agent or AI solution must read from or act in other systems, when an interface list is growing unplanned, or when a write action needs a safe pattern.
license: CC-BY-4.0
metadata:
  department: ai-architecture
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, power-platform, entra, azure
  edition-support: starter, scale, enterprise
  reviewers: design-authority, security-privacy
  sources: ms-agents-extensibility, ms-copilot-studio-security-governance, ms-copilot-studio-guidance, ms-managed-environments
  status: draft
  authors: Simon Foote
---

# AI integration patterns

## Purpose

An AI solution that only answers questions is relatively contained; one that reads from and writes to business systems
becomes part of the organisation's integration estate. This skill decides, interface by interface, how an AI solution
connects to other systems: the mechanism, the direction, whose identity is used, whether the call is synchronous, how a
write is confirmed and what happens when it fails. Integration goes wrong when the model is allowed to improvise
multi-step changes, when maker credentials carry every call, and when nobody owns the far end of the connection.

## When to use

- An agent brief or solution design includes reading from or acting in a system of record.
- A solution's list of connectors, flows and APIs has grown without a design.
- A write, send or approval action needs a safe pattern before build.
- Teams want to expose an internal API or MCP server to agents.
- An existing integration estate (an integration platform, event bus or API gateway) should be reused rather than bypassed.

## When not to use

- Designing the individual tools and functions inside a Foundry agent - use `ai-foundry:foundry-tool-design`.
- Building MCP servers and connecting them to Foundry solutions - use `ai-foundry:mcp-integration`.
- Designing the actions a Copilot Studio agent calls - use `copilot-studio:studio-actions-and-tools`.
- Reviewing the security of connectors already chosen - use `security-privacy:connector-review`.
- Setting organisation-wide connector and data policy - use `platform-governance:connector-policy`.
- Identities used across the solution as a whole - use `ai-architecture:ai-identity-design`.

## Questions to ask first

1. Which systems does the solution touch, and for each, does it read, create, update, delete or send?
2. Must the user see the result immediately, or can the work complete in the background?
3. Whose identity should each call carry, and does the far system support that?
4. What should happen if the call fails halfway, and who would notice?
5. Does the organisation already have an integration platform or API layer for this system?

## Required inputs

- The agent or solution brief, with actions and their business purpose.
- The platform decision from `ai-architecture:platform-selection`.
- For each target system, its owner, available interfaces and authentication options.
- The environment's data policy and governance zone.

Where a system owner or interface is unknown, record the interface as unresolved; never design around an assumed API or
assume a connector runs as the user.

## Decision framework

Choose the simplest mechanism that keeps identity, confirmation and failure handling under control.

| Need | Preferred pattern | Avoid |
|---|---|---|
| Read reference data in Microsoft 365 | Permission-trimmed grounding or Graph-based connectors | Copying content into a separate store without need |
| Read a line-of-business record | Standard or custom connector under user identity, narrow operation | Broad query tools the model can call freely |
| Single, bounded write | Action with explicit user confirmation, showing what will change | Silent writes from model reasoning |
| Multi-step change across systems | Deterministic flow or service called as one action, with its own error handling | Letting the model sequence several writes |
| Long-running or high-volume work | Asynchronous pattern - queue, event or flow - with status reported back | Holding a conversation open for a long process |
| Reusable capability for many agents | An owned API or MCP server with documented tools, versioning and access control | Each agent wiring the same system differently |
| Existing enterprise integration | Call the integration layer rather than the system directly | Bypassing it for speed |

For every interface record: mechanism, direction, operations, identity, timing, confirmation, idempotency, error and
retry behaviour, logging, data leaving the tenant, and owner of the far end.

## Practitioner approach

Start with an interface list, not a diagram. For each system the solution touches, write one row: what is read or
changed, why, and how often. Separate reads from writes; a solution that only reads is a much smaller design and review
than one that acts.

For reads, prefer patterns that respect the caller's own permissions. If the user cannot see a record in the source
system, the agent should not see it on their behalf. Keep query tools narrow: a tool that retrieves one customer by
reference is safer and easier to test than one that runs arbitrary searches.

For writes, keep the model out of the sequencing. The model is good at understanding what the user wants and filling in
parameters; it is poor at guaranteeing that three dependent updates either all happen or none do. Put multi-step changes
in a deterministic flow or service with its own error handling, and call it as a single action. Show the user what will
change and wait for confirmation before any write with effect outside their own content.

Decide timing deliberately. Conversations suit short synchronous calls. Anything that can take longer, or touches many
records, should be queued or triggered as an event, with the solution telling the user how they will learn the outcome.
Design idempotency so a retried call does not create duplicates.

Settle identity per interface with the system owner, then pass the summary to `ai-architecture:ai-identity-design`.
Where the far system cannot accept the user's identity, use a dedicated service identity with the narrowest scope and an
owner; never the maker's personal connection.

Reuse what exists. If the organisation already exposes the system through an API layer or integration platform, call
that and inherit its throttling, logging and support. Where several agents need the same system, propose an owned API or
MCP server rather than letting each team wire its own connection.

Finally, design failure. For each interface state what the user sees when it is unavailable, what is logged, who is
alerted and how partial changes are prevented or reversed. Agree each row with the far system's owner.

## Outputs

- An interface catalogue for the solution: one row per interface with mechanism, direction, operations, identity, timing, confirmation, idempotency, failure behaviour, logging, data boundary and owner.
- An architecture decision record on the `architecture-decision-record` template for any non-standard pattern.
- Requests to system owners for access, scopes or new interfaces.

## Microsoft platform considerations

Connectors, flows as actions, custom connectors, APIs, plug-ins and MCP servers are supported differently across Agent
Builder, Copilot Studio and Microsoft Foundry, and data policies apply per environment. Confirm current support and
authentication options in `ms-agents-extensibility` and `ms-copilot-studio-security-governance` before fixing a pattern.

## Adoption considerations

Makers reach for the connector that works first. Publish the approved integration patterns with fictional worked
examples so the safe route is also the quick one, and route novel interfaces to an architect early.

## Knowledge considerations

Not applicable to most interfaces, because this skill covers actions and record access rather than grounding content.
Where an interface indexes content for grounding, use `ai-architecture:grounding-patterns`.

## Security and privacy considerations

Every interface is a potential path for data to leave or for unauthorised change. Record identity, scope and data
boundary per row so `security-privacy:connector-review` can review facts, and route personal data leaving the tenant to
`security-privacy:privacy-assessment`.

## Responsible AI considerations

Actions that change records about people, send communications or approve requests need human confirmation and an audit
trail. Flag such interfaces for the `responsible-ai` review from tier 3.

## Evaluation requirements

Test each write interface for confirmation, correct identity, failure without partial change and idempotent retry.
Include these cases in the solution's test plan and in regression after change.

## Value measures

At portfolio level, track reuse of shared APIs and MCP servers, integration-related incidents and the share of write
actions with confirmation and logging. The AI solution architect owns these measures, with system owners, and takes the
baseline from the first interface catalogues.

## Scale notes

### Starter

Keep early solutions read-only or limited to standard connectors under user identity, with any write routed through a
simple confirmed flow.

### Scale

Publish approved integration patterns, require an interface catalogue for every solution with actions, and start
offering shared APIs for frequently used systems.

### Enterprise

Route AI integrations through the enterprise integration layer, with owned MCP servers or APIs per system, versioning
and central monitoring, and federated review of standard patterns.

## Hand-offs

- To `ai-architecture:ai-identity-design` with the identity required per interface.
- To `copilot-studio:studio-actions-and-tools`, `copilot-studio:power-automate-actions` or `ai-foundry:foundry-tool-design` for build.
- To `security-privacy:connector-review` for the security gate.

## Reviewer gates

From risk tier 2 the interface catalogue is reviewed by `security-privacy` (blocking) and by `design-authority` for
pattern conformance. From tier 3, interfaces that act on people are also seen by `responsible-ai`.

## Failure modes

- The model sequences several writes, one fails, and records are left inconsistent.
- A shared agent calls a system through the maker's connection, giving every user the maker's rights.
- A long-running call is held inside a conversation and times out, and the user retries and creates duplicates.
- Each team integrates the same system differently, and a change in that system breaks several agents at once.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Let the model sequence multi-step writes that must succeed or fail together.
- Design an interface around maker or shared personal credentials.
- Allow write or send actions with effect beyond the user's own content without confirmation.
- Bypass the organisation's integration layer without a recorded decision.

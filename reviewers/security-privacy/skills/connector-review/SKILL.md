---
name: connector-review
description: Reviews the connectors, actions, tools, MCP servers and APIs an agent or automation uses, covering user versus maker authentication, least privilege, data policies, data leaving the tenant and confirmation for write actions, and classifies each finding as blocking or advisory with a fix. Use when an agent gains an action or tool, when a flow uses a new connector, or when a maker shares a connection.
license: CC-BY-4.0
metadata:
  department: security-privacy
  lifecycle: Deliver, Assure, Launch, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, power-platform, ai-foundry, entra, azure
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-studio-security-governance, ms-managed-environments, ms-copilot-studio-zoned-governance, ms-agents-extensibility, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Connector review

## Purpose

An agent that only answers can expose information; an agent that acts can change it, send it elsewhere and do so under
someone else's identity. This reviewer skill examines every connector, action, tool, MCP server and API an agent or
automation uses, and classifies each finding as blocking or advisory with a specific fix. Reviews go wrong when they
check that a connector is "allowed" by policy and stop there, without asking whose credentials it runs on, what it can
write, and where the data ends up.

## When to use

- An agent or automation at risk tier 2 or above reaches its `security-privacy` gate with actions or tools.
- A maker adds a new connector, custom connector, MCP server, plug-in or API call to an existing solution.
- A connection is to be shared with other makers or embedded in an agent used by others.
- Data policy changes are proposed to allow a connector that was blocked.
- An incident suggests an agent acted beyond what users expected.

## When not to use

- Reviewing what knowledge content the solution can reach and reveal - use `security-privacy:data-exposure-review`.
- Lawful basis, transparency and retention for personal data moving through the actions - use `security-privacy:privacy-assessment`.
- Designing the actions and their confirmation rules in the first place - use `m365-agents:agent-use-case-design`.
- Setting organisation-wide connector policy and environment strategy - use `platform-governance:connector-policy`.
- Detailed authentication and connector engineering for Copilot Studio builds - use `copilot-studio:studio-authentication` and `copilot-studio:studio-connectors`.

## Questions to ask first

1. What does each connector, action or tool do - read, create, update, delete, send - and in which system?
2. Whose identity does it run under: the signed-in user, the maker, a shared account or a service identity?
3. Does it need all the permissions it has been granted, or could a narrower scope work?
4. Does any data leave the organisation's tenant or reach a third-party service, and under what agreement?
5. Must a person confirm before a write or send action takes effect?

## Required inputs

- An inventory of connectors, actions, tools, MCP servers and APIs, with operations used, authentication mode and permissions.
- The environment, its data policy classification and governance zone.
- The agent brief or automation design with audience and risk tier.
- Action test results from `m365-agents:agent-testing`, including confirmation and failure tests.

An action with an unknown authentication mode or unknown permissions is a blocking finding from tier 2 until it is
documented. Never assume a connector runs as the user.

## Decision framework

Classify every finding. From risk tier 2 a blocking finding stops release and is not traded against dates; below tier 2
findings are advisory to the owner, but anything that would be blocking sends the solution back to risk classification.

| Finding | Blocking when | Advisory when | Typical fix |
|---|---|---|---|
| Authentication mode | Maker or shared credentials let users act or read beyond their own rights | Service identity with narrow, documented scope and an owner | Switch to user authentication, or a dedicated service identity with least privilege |
| Least privilege | Broad scopes (all mailboxes, all sites, admin roles) where narrow ones would work | Slightly wider scope than needed on low-sensitivity data | Reduce scopes, split read from write |
| Data policy | Connector sits outside the environment's data policy or relies on an exception with no owner | Policy allows it but grouping is untidy | Move to a correctly governed environment, document the exception |
| Data leaving the tenant | Organisational or personal data reaches an external service with no agreement or assessment | External service is assessed and contracted | Remove, replace, or complete supplier and privacy assessment |
| Write and send actions | Actions change records, send messages or move money without user confirmation | Low-impact writes to the user's own content | Add explicit confirmation, show what will change, log the action |
| MCP servers and custom APIs | Unvetted server or API, unknown owner, or tool descriptions that could be manipulated | Vetted, owned server with documented tools | Vet, assign owner, pin versions, restrict tools exposed |
| Logging and failure | No record of actions taken, or failures leave partial changes | Logging exists but is not reviewed | Enable action logging, define safe failure behaviour |

Each finding names the risk, the rule behind it, the fix and an owner. Disagreement escalates to the accountable
executive for risk acceptance in writing.

## Practitioner approach

Start with an inventory, because makers rarely have one. List every connector, action, tool, MCP server and API call,
the operations actually used, and the system each touches. Separate reads from writes and sends; a solution with only
reads is a different review from one that can change records or contact customers.

For each item, establish whose identity it runs under. This is the most important question in the review. A connection
created with the maker's credentials and embedded in a shared agent lets every user act with the maker's rights. If the
maker is an administrator, the agent is too. User authentication keeps each person within their own access; a
dedicated service identity can be acceptable where its scope is narrow, documented and owned.

Then test least privilege. Compare the permissions granted with the operations used. Broad delegated or application
permissions, such as access to all mailboxes or all sites, are blocking when a narrower scope would serve. Ask the
maker to show why each scope is needed.

Check the data policy position. Confirm the environment, its governance zone and that each connector is permitted there
without an undocumented exception. Exceptions are legitimate, but each needs an owner, a reason and a review date.

Follow the data out. For each external service, ask what data is sent, whether personal data is included, where it is
processed and stored, and whether a supplier assessment and agreement exist. Personal data leaving the tenant also goes
to `security-privacy:privacy-assessment`.

Give MCP servers, plug-ins and custom APIs particular care. Find out who runs the server, how it is authenticated, which
tools it exposes and whether tool descriptions or returned content could steer the agent into unintended actions.
Expose only the tools the agent needs, and pin versions so behaviour does not change silently.

Review write and send actions with the action test evidence. Each should show the user what will happen and wait for
confirmation, run under the expected identity, log what it did, and fail without leaving partial changes. Prefer a
deterministic flow for multi-step changes over letting the model improvise a sequence.

Be proportionate. A tier 2 agent that reads one list with user authentication might pass with one advisory note. Record
findings with risk, fix and owner, and close the review only when blocking fixes are evidenced.

## Outputs

- The connectors and actions section of the `ai-risk-assessment`: inventory, authentication mode, permissions, data policy position, external data flows, confirmation rules, findings classified as blocking or advisory with fix and owner, and the verdict.
- Any written risk acceptance from the accountable executive.
- Requests to the platform team for policy changes or exceptions, with rationale.

## Microsoft platform considerations

Authentication options, data policies, environment routing, Managed Environments controls, connector classification and
MCP support differ between routes and change often. Confirm current behaviour in the source records
(`ms-copilot-studio-security-governance`, `ms-managed-environments`, `ms-agents-extensibility`) before relying on a
control, and record what was checked.

## Adoption considerations

Makers often choose maker authentication because it is easier to get working. Publish a short pattern guide showing the
approved alternatives, so the secure route is also the easy one and reviews find fewer blocking issues.

## Knowledge considerations

Not applicable to most connector findings, because this review concerns actions and data flows rather than grounding
content. Where a connector indexes content for grounding, that content is reviewed in `security-privacy:data-exposure-review`.

## Security and privacy considerations

This skill is the security review of connectors and actions. Personal data flows go to
`security-privacy:privacy-assessment`; grounding exposure goes to `security-privacy:data-exposure-review`.

## Responsible AI considerations

Actions that affect people (sending messages, updating records about individuals, approving requests) need human
confirmation and an audit trail. From tier 3, `responsible-ai:human-oversight` reviews the oversight design.

## Evaluation requirements

Blocking fixes need evidence: the changed authentication setting, the reduced permission set, a re-run of the
confirmation and failure tests. Advisory findings need an owner and a date.

## Value measures

Track, at portfolio level, the share of agents with actions using user or documented service identities, the number of
policy exceptions with owners and review dates, and time to close blocking findings. The security and privacy lead
owns these measures.

## Scale notes

### Starter

Keep first agents read-only or limited to standard connectors with user authentication; review any write action in a
short session with the maker and owner.

### Scale

Maintain an approved connector and action pattern list, require the inventory for every agent with actions, and review
exceptions in the CoE cadence.

### Enterprise

Federate standard-pattern reviews to business-unit reviewers, with the central team reviewing custom connectors, MCP
servers, service identities and tier 3 and 4 solutions. Track exceptions across the estate.

## Hand-offs

- Back to `m365-agents:agent-use-case-design` with changes to actions, identities and confirmation rules.
- To `security-privacy:privacy-assessment` for personal data leaving the tenant.
- To `m365-agents:agent-release-readiness` with the verdict.
- To `platform-governance:connector-policy` for policy and environment changes.

## Reviewer gates

This skill is the `security-privacy` gate for connectors and actions. It applies as a blocking gate from risk tier 2 and
as an advisory check below it. Blocking findings stop release and are not traded against dates; disagreement escalates
to the accountable executive for written risk acceptance.

## Failure modes

- A maker's connection is embedded in a shared agent, giving every user the maker's access.
- A connector is "allowed by policy", so nobody checks what it writes or where data goes.
- An MCP server is added from an unvetted source and its tools change without notice.
- Write actions run without confirmation, and a misunderstood request updates live records.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Pass a shared agent that runs actions on maker or shared credentials beyond users' own rights.
- Treat data policy permission as proof that a connector is safe.
- Trade a blocking finding against a launch date.
- Allow write or send actions with consequences outside the user's own content without confirmation.

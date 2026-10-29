---
name: automation-connector-governance
description: Applies connector and data policy governance to individual automations in delivery - which connectors a flow may use in its environment, whose connections run it, custom connectors and AI services, and how a maker requests and justifies an exception. Use when a flow needs a connector its environment blocks, when production flows run on personal connections, or before an automation moves to production.
license: CC-BY-4.0
metadata:
  department: automation
  lifecycle: Deliver, Assure, Launch, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: power-platform, copilot-studio, entra
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-managed-environments, ms-copilot-studio-security-governance, ms-copilot-studio-zoned-governance, ms-coe-starter-kit
  status: draft
  authors: Simon Foote
---

# Automation connector governance

## Purpose

Organisation-wide data policies decide which connectors may be combined in which environments; they do not decide
whether a particular flow should use them, whose credentials it runs on or what happens when the maker leaves. This
skill applies connector governance to automations as they are built and promoted: it checks each connector against
the environment's policy, settles the connection model for production, handles custom connectors and AI services, and
runs the exception route when a flow needs something the policy blocks. It goes wrong when flows reach production on
personal connections, and when exceptions are granted informally and never reviewed.

## When to use

- A maker's flow needs a connector that the target environment's data policy blocks or classifies differently.
- An automation is about to move to production and its connections have not been reviewed.
- Production flows are found running on personal connections of makers or former staff.
- A flow needs a custom connector, an HTTP call or a connection to an external AI service.
- The automation team needs a consistent route for connector exception requests.

## When not to use

- Setting the organisation-wide connector and data policies themselves - use `platform-governance:connector-policy`.
- The formal security review of connectors, actions and identities - use `security-privacy:connector-review`.
- Choosing and governing connectors used by Copilot Studio agents - use `copilot-studio:studio-connectors`.
- Designing environments and zones for makers - use `platform-governance:ai-environment-strategy`.
- Identity and secrets for pro-code services - use `ai-engineering:secrets-and-identity`.

## Questions to ask first

1. Which connectors and operations does the automation use, and which environment will it run in for production?
2. Whose identity will each production connection use: a named person, a dedicated service account or a service principal?
3. Does any connector send data outside the tenant or to an AI service, and has that service been assessed?
4. If a connector is blocked, what business need does it serve and is there an approved alternative?
5. Who will own the connections, renew credentials and respond when one expires?

## Required inputs

- The flow's connector inventory, with operations used and the data each carries.
- The target environment, its governance zone and data policy classification.
- The organisation's connector policy and exception process, from `platform-governance:connector-policy`.
- The automation's risk tier and data sensitivity.

If the organisation has no connector exception process, record requests on the automation design with a named
approver and a review date, and raise the gap with the platform governance lead. Never treat silence as approval.

## Decision framework

| Situation | Decision | Condition |
|---|---|---|
| Connector permitted in the target environment and used for its intended purpose | Proceed | Production connection model agreed |
| Connector permitted, but production would run on a personal connection | Change before promotion | Move to a dedicated service account or service principal with least privilege and an owner |
| Connector blocked, approved alternative exists | Use the alternative | Design updated |
| Connector blocked, no alternative, need justified | Request an exception | Named approver, reason, scope limited to this solution and environment, review date |
| Custom connector or direct HTTP call | Treat as new integration | Owner, authentication, data flow, security review from tier 2 |
| External AI service outside approved Microsoft services | Stop and escalate | Supplier, privacy and security assessment before any build continues |

Every exception is time-limited, owned and recorded in the solution inventory. An exception that expires without review
lapses.

## Practitioner approach

Build the connector inventory early, from the automation design, not at the gate. For each connector, record the
operations used (read, create, update, delete, send), the data carried and the systems touched. Makers often add an
HTTP action or a convenience connector during build; ask for the inventory to be updated with each change, and check it
again before promotion.

Check each connector against the target environment's policy rather than the development environment's, which is often
looser. A flow that works in a sandbox and fails policy in production is a common and avoidable delay. Where a connector
is blocked, look first for an approved alternative that meets the need. Many requests for a third-party file-sharing or
messaging connector can be met by a connector the organisation already governs.

Settle the production connection model. Personal connections tie the flow to one person's access and employment, and
let the flow act with that person's rights, which are often wider than the flow needs. For production, prefer dedicated
service accounts or service principals with permissions limited to what the flow does, owned by the team that owns the
automation, with credential renewal on someone's calendar. Use connection references so connections can be swapped
without editing the flow.

Treat custom connectors and direct HTTP calls as integrations. They need an owner, documented authentication, a record
of the data sent and, from tier 2, a security review through `security-privacy:connector-review`. Calls to AI services
need particular care: confirm the service is an approved Microsoft service or one the organisation has assessed, what
data is sent and where it is processed. AI services outside the approved Microsoft estate stop the build until assessed.

Run exceptions as decisions. Each request states the business need, why alternatives do not work, the data involved,
the scope (this solution, this environment) and a review date. The approver is named by the platform governance lead,
not the maker's manager by default. Record the exception against the automation in the solution inventory so it can
be found and reviewed.

Finally, check what happens when things change: a connection owner leaves, a credential expires, a policy is tightened.
Each should alert an owner, not silently stop the flow.

## Outputs

- A connector inventory per automation: connector, operations, data carried, environment classification, connection identity and owner.
- A production connection model, with service accounts or service principals, their permissions and credential renewal owner.
- Exception records: need, alternatives considered, data, scope, approver, review date.
- Inputs to `security-privacy:connector-review` for custom connectors, HTTP calls and AI services from tier 2.

## Microsoft platform considerations

Power Platform data policies, connector classification, connection references, Managed Environments controls, service
principal connections and the CoE Starter Kit's inventory components shape what is possible, and they change often.
Confirm current behaviour in `references/sources.md` (`ms-managed-environments`, `ms-copilot-studio-security-governance`,
`ms-coe-starter-kit`) and record what was checked. Licensing for service accounts and connectors routes to the Microsoft
licensing guide or a licensing partner.

## Adoption considerations

Makers experience connector governance as delay. Publish the list of approved connectors per environment, the approved
alternatives to commonly requested blocked connectors and a simple exception form, so most makers never need to ask.

## Knowledge considerations

Not applicable, because this skill governs connectors and connections rather than knowledge used for grounding.
Connectors that index content for agents are handled under `copilot-studio:studio-connectors`.

## Security and privacy considerations

This skill prepares the evidence that `security-privacy:connector-review` assesses. Least privilege, owned non-personal
production identities and a clear record of data leaving the tenant are the minimum. Personal data flowing to new
services also goes to `security-privacy:privacy-assessment`.

## Responsible AI considerations

Not applicable in most cases, because connector governance concerns data flows rather than how AI output is used. Where
a connector lets an automation act on people (sending messages, updating records about individuals), confirm the human
review design in `automation:human-in-the-loop`.

## Evaluation requirements

Before promotion, confirm in the target environment that the flow runs under the production connections and that each
connector passes policy. Test credential expiry and connection removal in a test environment to prove they alert an owner.

## Value measures

Track, at portfolio level, the share of production automations on non-personal owned connections, open exceptions past
their review date, and time to decide exception requests. The automation lead owns these measures.

## Scale notes

### Starter

Keep production automations to standard connectors in one governed environment, with a small number of service accounts
owned by the automation team. Record exceptions on the design.

### Scale

Publish approved connectors and alternatives per environment, require the connector inventory at promotion, and review
exceptions at the CoE cadence using estate inventory.

### Enterprise

Federate exception decisions for standard connectors to business-unit platform owners, with the central team deciding
custom connectors, HTTP calls and AI services. Track exceptions and production identities across the estate.

## Hand-offs

- To `security-privacy:connector-review` for custom connectors, HTTP calls, AI services and tier 2 automations.
- To `platform-governance:connector-policy` when a pattern of exceptions suggests the policy needs to change.
- To `automation:flow-design-patterns` with the connection references and identities to use.
- To `automation:automation-monitoring` for alerts on connection failure and credential expiry.

## Reviewer gates

From risk tier 2, `security-privacy` reviews the connector inventory, production identities and any exception through
`security-privacy:connector-review`; a production flow running on personal or over-privileged credentials is blocking.

## Failure modes

- A flow reaches production on the maker's personal connection and stops the day the maker leaves.
- An exception is granted by email, never recorded and never reviewed, and other makers copy it.
- An HTTP action quietly sends business data to an unassessed external AI service.
- A service account is given broad permissions for convenience and becomes the most privileged identity in the estate.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Promote a production automation that runs on a maker's personal connection.
- Grant a connector exception without a named approver, a scope and a review date.
- Allow data to reach an unassessed external AI service.
- Treat a connector being permitted by policy as proof that its use in a flow is safe.

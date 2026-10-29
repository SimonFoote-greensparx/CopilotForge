---
name: studio-connectors
description: Chooses the connectors a Copilot Studio agent depends on - prebuilt, certified or custom - and governs their use in the agent through connection references, the account each connection runs under, data policy grouping, ownership of custom connectors and their change control. Use when a maker needs a connector the agent does not yet use, when a custom connector is proposed, or when a data policy blocks an agent.
license: CC-BY-4.0
metadata:
  department: copilot-studio
  lifecycle: Deliver, Assure
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-studio, power-platform, azure
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-studio-security-governance, ms-copilot-studio-guidance, ms-managed-environments, ms-agents-extensibility
  status: draft
  authors: Simon Foote
---

# Studio connectors

## Purpose

Almost every Copilot Studio agent that acts, and many that read from business systems, rely on connectors. This skill
chooses the right connector for each need and governs how the agent uses it: which connection it runs under, how that
connection moves between environments, which data policy group it sits in and who owns it when it is custom. It usually
goes wrong when makers create personal connections that silently become the identity behind a shared agent, when a
custom connector is built against an API nobody owns, or when a data policy blocks an agent the day before launch.

## When to use

- The solution design or a tool specification needs a connector the agent does not yet use.
- A maker proposes a custom connector, or wraps an internal API for an agent.
- A data policy blocks an agent or flow, or a maker asks for a connector to be reclassified.
- An agent is moving to test or production and its connections must be re-pointed.

## When not to use

- Setting the organisation's tenant-wide data and connector policies - use `platform-governance:connector-policy`.
- Governing connectors for automations without an agent - use `automation:automation-connector-governance`.
- Designing what each tool does, its inputs and confirmation - use `copilot-studio:studio-actions-and-tools`.
- Deciding whether users sign in and how identity flows end to end - use `copilot-studio:studio-authentication`.
- The formal security review of connectors, actions and shared connections - use `security-privacy:connector-review`.

## Questions to ask first

1. What operation is needed in which system, and does a prebuilt connector already provide it?
2. Under whose account will each connection run - the end user's, the maker's, or a dedicated service account - and who approved that?
3. How does the organisation's data policy classify this connector in the target environments, and will it sit alongside the agent's other connectors?
4. If a custom connector is needed, who owns the API, its authentication and its changes?
5. Does data leave the tenant or the organisation's chosen region through this connector?

## Required inputs

- Tool specifications from `copilot-studio:studio-actions-and-tools`.
- The data policies applied to the development, test and production environments.
- The system owner's agreement and the API documentation for any custom connector.
- The authentication design from `copilot-studio:studio-authentication`.

If the data policy for production is unknown, do not assume the connector will be allowed there; check with the platform
owner first. If an API has no owner, a custom connector to it is not built.

## Decision framework

| Need | Choose | Conditions |
|---|---|---|
| Common Microsoft or third-party service | Prebuilt connector | Allowed in the target data policy group; publisher and data flows understood |
| Internal or line-of-business API with an owner | Custom connector in a solution | API owned, documented, versioned and authenticated; connector owned by a named team |
| One-off call during a pilot | Avoid; design the connector properly or defer the action | Pilots become production more often than planned |
| A system with no API | Do not build a connector to screen-scrape it; refer to `automation:desktop-automation` with care | The system owner agrees to automation |

For every connection, apply this order of preference: end-user credentials, then a dedicated and scoped service account
owned by a team, and never a maker's personal account for a shared agent.

## Practitioner approach

Start from the tool specification and check what already exists. Look first for a governed, prebuilt connector or an
approved custom connector already used by another agent or flow; reuse beats a second connector to the same system. Read
what the connector does with data - which service it calls and where that service runs - and record it.

Check the data policy before building. Find out which policy applies to each environment the agent will pass through and
how the connector is grouped. Agents and flows generally cannot combine connectors from groups the policy separates, and
policies can differ between development and production. Raise reclassification requests with the platform owner early
and with a business reason; never ask for a production environment to be exempted from policy.

Decide the account behind each connection deliberately. A connection created in the authoring canvas often defaults to the
maker's own account. That is acceptable while building alone and unacceptable once anyone else uses the agent, because
every user then acts with the maker's rights and the agent breaks when the maker leaves. Prefer end-user authentication
for the connector where it supports it; where a service account is genuinely needed, use a dedicated account owned by a
team, with the minimum permissions in the target system, and record the approval.

Package connectors properly. Put custom connectors in the agent's solution or a shared solution, and use connection
references and environment variables so each environment points to its own connections and endpoints. Hard-coded URLs
and personal connections are the commonest reason an agent works in development and fails after import.

Treat a custom connector as a small product. It needs an owner, versioning, a change process agreed with the API owner,
secure authentication with secrets held outside the definition, and a list of agents and flows that depend on it. When
the API changes, the owner tells dependent agent owners before release.

Finally, record each connector in the solution design with its group, account, owner and data flows, and send new or
changed connectors to `security-privacy:connector-review`.

## Outputs

- A connector register for the agent: connector, operations used, data policy group per environment, account behind the connection, data flows and owner.
- A custom connector specification where needed: API owner, authentication, versioning, dependants and change process.
- Connection references and environment variables listed for the `alm-and-environment-plan`.
- Data policy change requests with business justification, where required.

## Microsoft platform considerations

Connector catalogues, certification, data policy behaviour, endpoint filtering and the connector controls available
through Managed Environments change often. Check `ms-copilot-studio-security-governance` and `ms-managed-environments`
for current controls, and route any question about which connectors require which licence to
`platform-governance:ai-licensing-and-capacity`, which ends with the Microsoft licensing guide or a licensing partner.

## Adoption considerations

Makers lose momentum when a data policy blocks them late. Publish which connectors are allowed in which zones, and give
makers a quick route to request a review, so governance is visible rather than discovered.

## Knowledge considerations

Not applicable in most cases, because connectors here carry actions rather than knowledge; where an enterprise connector
brings content into Microsoft 365 as knowledge, design it with `copilot-studio:studio-knowledge-architecture`.

## Security and privacy considerations

Connections are credentials. Never share a personal connection, never embed secrets in connector definitions, scope
service accounts to the minimum, and record where data goes. Connectors that send data outside the tenant or region are
reviewed before use, and personal data flows go to `security-privacy:privacy-assessment`.

## Responsible AI considerations

Not applicable as a separate concern, because connector choice is a security and governance decision; the effects of the
actions connectors enable are covered under `copilot-studio:studio-actions-and-tools`.

## Evaluation requirements

Test each connection in each environment after import, test under a user with no rights in the target system, and test
behaviour when the connector or service is unavailable. A connection that runs as the maker after import fails the test.

## Value measures

Track reuse of approved connectors, time from connector request to decision, and agent launches delayed by data policy
issues, owned by the Copilot Studio Architect and reported at portfolio level.

## Scale notes

### Starter

Use prebuilt connectors already allowed by policy, end-user connections where possible, and no custom connectors without
a named API owner.

### Scale

Maintain a shared solution of approved custom connectors with owners, a published list of allowed connectors by zone and
a request route for new ones.

### Enterprise

Run custom connectors as owned products with versioning and dependency tracking, automate checks for personal
connections in shared agents, and align with the organisation's API management.

## Hand-offs

- To `security-privacy:connector-review` for every new or changed connector or shared connection.
- To `platform-governance:connector-policy` for data policy changes.
- To `copilot-studio:studio-alm` with connection references and environment variables.
- Back to `copilot-studio:studio-actions-and-tools` if no acceptable connector exists.

## Reviewer gates

From risk tier 1, `security-privacy` reviews any shared or service connection and any connector sending data outside the
tenant; from tier 2 it reviews every connector the agent uses. A shared agent running on a maker's personal connection is
a blocking finding.

## Failure modes

- The agent runs on the maker's personal connection and stops working when the maker changes role.
- A data policy in production blocks a connector that was allowed in development, and launch slips.
- A custom connector points at an API that changes without notice and breaks several agents at once.
- Endpoints and credentials are hard-coded, so the imported agent calls the development system from production.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Let a shared agent run on a maker's personal connection.
- Embed secrets or credentials in a connector definition or agent configuration.
- Ask for a production environment to be exempted from data policy.
- State which connectors need which licence; route the question to the licensing guide or a licensing partner.

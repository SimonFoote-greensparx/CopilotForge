---
name: ai-identity-and-access-review
description: Reviews the identities an AI solution runs under and the access around it - who can use, edit, share and administer it, agent and service identities, privileged roles, guest access, sign-in controls and what happens when owners leave - and classifies each finding as blocking or advisory with a fix. Use when an agent or AI solution reaches its security gate, when ownership or audience changes, or when nobody knows whose identity an agent uses.
license: CC-BY-4.0
metadata:
  department: security-privacy
  lifecycle: Assure, Launch, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, power-platform, entra, azure
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-studio-security-governance, ms-managed-environments, ms-agent-builder, ms-copilot-privacy, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI identity and access review

## Purpose

Every AI solution acts as someone. It answers as the signed-in user, calls systems as a maker, a service principal or
an agent identity, and is edited, shared and administered by people who may change role or leave. This reviewer skill
examines those identities and the access wrapped around the solution, and classifies each finding as blocking or
advisory with a specific fix. Reviews go wrong when they check the agent's knowledge and connectors in detail but never
ask who can change the agent itself, so a well-reviewed solution is quietly rewritten or widened by an account nobody
is watching.

## When to use

- An agent or AI solution at risk tier 2 or above reaches its `security-privacy` gate.
- The solution uses a service principal, managed identity, agent identity or shared account.
- Ownership, co-authors or administrators change, or an owner leaves the organisation.
- The audience is about to include guests, partners or customers.
- An incident or audit cannot establish whose identity performed an action.

## When not to use

- Reviewing each connector, action, tool or MCP server and its authentication mode - use `security-privacy:connector-review`.
- Reviewing what content the solution can reach and reveal - use `security-privacy:data-exposure-review`.
- Designing the identity architecture for users, agents and services - use `ai-architecture:ai-identity-design`.
- Implementing secrets, managed identities and least privilege in code - use `ai-engineering:secrets-and-identity`.
- Setting the estate-wide rules for which identities may reach which data - use `data-governance:ai-data-access-model`.

## Questions to ask first

1. Whose identity does the solution use for each thing it does - answering, reading data, writing data, calling external services?
2. Who can use it, who can edit its instructions, knowledge and actions, who can share or publish it, and who administers its environment or resource?
3. Are any of those identities privileged, shared, non-human or external, and is each one owned by a named role?
4. What controls apply at sign-in - conditional access, device and location conditions, multifactor authentication - and do they apply to every channel the solution is published to?
5. What happens to access when an owner, co-author or maker changes role or leaves?

## Required inputs

- The agent brief or solution design, with audience, channels, risk tier and owners.
- An identity map: every human and non-human identity involved, its purpose and its permissions.
- Role and membership exports for the agent, its environment or resource group, and any security groups used for sharing.
- Findings from `security-privacy:connector-review`, so per-connector authentication is not reviewed twice.

An identity nobody can explain is itself a finding: blocking from tier 2. Never infer an identity's permissions from
its name or from the maker's recollection; ask for the export.

## Decision framework

Classify every finding. From risk tier 2 a blocking finding stops release and is not traded against dates; below tier 2
the review is advisory, but a finding that would be blocking means the tier needs re-checking.

| Area | Blocking when | Advisory when | Typical fix |
|---|---|---|---|
| Runtime identity | The solution acts with a person's privileged or personal credentials on behalf of others | A service identity has broader rights than the design needs on low-sensitivity data | Move to user-delegated access or a narrowly scoped service or agent identity |
| Edit and publish rights | People outside the owning team can change instructions, knowledge or actions of a tier 2+ solution | Co-author list is wider than needed but all are in the owning team | Restrict authoring to named owners; separate build from production |
| Privileged roles | Environment, resource or tenant admin roles are held permanently by makers or shared accounts | Admin roles are justified but not time-bound | Remove standing privilege; use time-bound elevation and separation of duties |
| Non-human identities | A service principal, managed identity or agent identity has no owner, no review or unscoped permissions | Owner named but review date missing | Assign an owner, scope permissions, set a credential and access review |
| External access | Guests or external users can reach a solution grounded on internal content without a design decision | External audience approved but sign-in controls not yet verified | Restrict the audience; apply and test external sign-in controls |
| Sign-in controls | A channel bypasses the organisation's conditional access or MFA expectations | Controls apply but are undocumented for this solution | Apply policies to every channel; record them |
| Joiner, mover, leaver | A departed person still owns, edits or authenticates the solution | No documented process for ownership transfer | Transfer ownership; add the solution to leaver and access review processes |

Each finding names the risk, the standard behind it, the fix and an owner. Disagreement escalates to the accountable
executive through `responsible-ai:ai-risk-acceptance`, recorded in writing with a review date.

## Practitioner approach

Begin by drawing the identity map before reading any configuration. List every action the solution takes and write
beside it the identity that performs it. Makers often cannot fill in this table, and that is the first useful finding:
a solution whose builders do not know whose identity it uses cannot be reviewed for least privilege.

Then look for the borrowed identity. The most common serious pattern is a solution built and tested under the maker's
own account, then shared, so every user inherits the maker's rights to a connection, a data source or an API. Connector
review catches this per connection; this review checks the whole solution, including flows, scheduled triggers,
Foundry resources and any automation that runs when nobody is signed in.

Next, review who can change the solution, not only who can use it. Export the owners, co-authors and environment or
resource roles and compare them with the owning team in the brief. For tier 2 and above, the people who can edit
instructions, add knowledge or attach actions should be few, named and accountable, and production changes should
pass through the organisation's release route rather than direct editing. Check that environment administrators and
Azure resource owners are not standing, shared or personal accounts held by makers.

Non-human identities need the same discipline as people. For each service principal, managed identity or agent
identity, confirm an owner role, the exact permissions granted, how credentials are stored and rotated, and when access
is next reviewed. Identities created for a pilot and never removed are a recurring source of exposure.

Check sign-in controls channel by channel. A solution published to Teams, a website and a mobile app may meet the
organisation's conditional access expectations in one channel and not another. Where guests or external users are in
scope, confirm that this was a design decision and that external sign-in controls were tested.

Finally, follow the leaver path. Ask what happens if the owner leaves tomorrow: who inherits the solution, whether
connections stop working or keep running under a disabled account, and whether the solution appears in access reviews.
Product capabilities for ownership transfer, agent identities and access reviews change often, so confirm current
behaviour in the source records and record what was checked.

Write the findings proportionately. A team agent using delegated access and a three-person author list may need one
advisory finding. Close the review only when blocking fixes are evidenced, and re-review when owners, channels or
audience change.

## Outputs

- The identity and access findings in the `ai-risk-assessment`: the identity map, the edit and administer list, findings classified blocking or advisory with risk, fix, owner and date, and the verdict.
- A list of non-human identities with owners and review dates, handed to the solution owner and the platform team.
- Any written risk acceptance from the accountable executive.

## Microsoft platform considerations

Identities differ by route: agents built in Agent Builder, Copilot Studio agents in Power Platform environments, and
Foundry solutions in Azure each have their own sharing, authoring and administration model, and Microsoft Entra
provides the identity, conditional access and access review capabilities around them. How agent identities are
represented, which channels honour which sign-in controls, and what Managed Environments add are volatile; confirm them
in `ms-copilot-studio-security-governance`, `ms-managed-environments` and `ms-agent-builder` before relying on them.

## Adoption considerations

Makers experience identity findings as friction because their solution worked under their own account. Explain the
borrowed-identity risk with a concrete example from their solution, and offer the approved pattern rather than only the
rejection.

## Knowledge considerations

Not applicable as a primary concern, because content access is reviewed in `security-privacy:data-exposure-review`.
Note here only where knowledge is reached through a non-human identity rather than the user's own permissions.

## Security and privacy considerations

This skill is the security review of identity and access. Findings about connector authentication go to
`security-privacy:connector-review`; findings about content reach go to `security-privacy:data-exposure-review`.

## Responsible AI considerations

Accountability depends on attribution. If actions cannot be traced to an identity and an owning role, people affected
by the solution cannot get a clear answer about who acted. Flag such gaps to `responsible-ai:human-oversight`.

## Evaluation requirements

Blocking fixes need evidence: a fresh role export, a test showing a user without rights cannot perform an action, or
a sign-in log showing the expected controls applied in each channel. Advisory findings need an owner and a date.

## Value measures

Track at portfolio level the share of tier 2+ solutions with a complete identity map, the number of non-human identities
without an owner, and time to close blocking identity findings. The security and privacy lead owns these measures,
with baselines taken at the first review cycle.

## Scale notes

### Starter

Draw the identity map with the maker in one session and check owners, co-authors and sharing in the product's own
settings. Prefer delegated access so the review stays short.

### Scale

Make the identity map a mandatory part of the release checklist and add AI solutions and their non-human identities to
the regular access review cycle.

### Enterprise

Federate tier 2 reviews to trained business-unit reviewers using the same criteria, with the central team taking tier 3
and 4, and reconcile non-human identities against the solution inventory every review cycle.

## Hand-offs

- To `security-privacy:connector-review` for per-connector authentication findings.
- To `ai-architecture:ai-identity-design` where the identity pattern itself needs redesign.
- To `m365-agents:agent-release-readiness` with the verdict.
- To `security-privacy:ai-incident-readiness` with the identity map, which responders need to contain an incident.

## Reviewer gates

This skill is the `security-privacy` gate for identity and access. It applies as a blocking gate from risk tier 2 and
as an advisory check below it. Blocking findings stop release and are not traded against dates; disagreement escalates
to the accountable executive for written risk acceptance.

## Failure modes

- The review checks who can use the agent but not who can edit it, and an unreviewed co-author later widens its scope.
- A service identity created for a pilot keeps broad permissions long after the pilot ends.
- Conditional access is verified in Teams but the same agent is also published to a channel that bypasses it.
- The owner leaves, connections keep running under a disabled account, and nobody notices until something fails.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Pass a tier 2 or higher solution whose runtime identities cannot be explained.
- Accept a maker's personal or privileged credentials as the identity of a shared solution.
- Leave a non-human identity without an owner and a review date.
- Trade a blocking finding against a launch date.

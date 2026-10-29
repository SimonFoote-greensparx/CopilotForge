---
name: ai-identity-design
description: Designs the identities an AI solution uses end to end - signed-in users, agent identities, service principals and managed identities - mapping which identity each hop runs under, how consent, scopes and conditional access apply, and who owns each non-human identity. Use when an agent or AI solution calls systems on someone's behalf, when an agent needs its own identity, or when nobody can say whose rights a solution acts with.
license: CC-BY-4.0
metadata:
  department: ai-architecture
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, power-platform, entra, azure
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, design-authority
  sources: ms-agents-extensibility, ms-copilot-studio-security-governance, ms-copilot-privacy, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# AI identity design

## Purpose

Every AI solution acts with somebody's rights. This skill decides whose, at each hop: the person using it, the agent
itself, a service identity, or a managed identity in Azure. It produces an identity map that security reviewers,
operators and auditors can follow from the user's request to the last system touched. Identity design goes wrong when
connections are created with the maker's account and shared, when service identities are given broad rights "to make it
work", and when non-human identities outlive the solutions and people that created them.

## When to use

- A solution design includes actions or data access in systems beyond the user's own content.
- An agent needs to act when no user is present, on a schedule or in response to an event.
- The platform offers an agent identity or service identity option and the team must decide whether to use it.
- A security review has found unclear or excessive identity use.
- Non-human identities for AI are multiplying without owners or review.

## When not to use

- Reviewing identity and access for a solution at its security gate - use `security-privacy:ai-identity-and-access-review`.
- Implementing secrets, managed identities and key rotation in pro-code solutions - use `ai-engineering:secrets-and-identity`.
- Configuring authentication for a Copilot Studio agent - use `copilot-studio:studio-authentication`.
- Choosing interface mechanisms between the solution and other systems - use `ai-architecture:ai-integration-patterns`.
- Deciding who in the organisation may build and share agents - use `platform-governance:maker-governance`.

## Questions to ask first

1. Who starts each interaction - a signed-in person, a schedule, an event or another agent?
2. For each system touched, should the outcome be limited to what that person could do themselves?
3. Must anything happen when no user is present, and if so with what rights?
4. Who will own each non-human identity, review its rights and retire it?
5. Which identity and access policies (conditional access, consent rules, privileged access) already apply?

## Required inputs

- The interface catalogue from `ai-architecture:ai-integration-patterns`, or a list of systems and operations.
- The platform decision and environment placement.
- The organisation's identity policies: consent model, conditional access baseline, service identity standards.
- The risk tier and audience.

If the identity policy is unknown, design to least privilege and record the policy questions for the identity team.
Never assume an action runs as the user because it appears to in testing.

## Decision framework

Choose the identity per hop, starting from the user.

| Situation | Preferred identity | Conditions |
|---|---|---|
| User asks, result limited to their own rights | Delegated user identity | Scopes limited to operations used; consent per policy |
| User asks, far system cannot accept user identity | Dedicated service identity with narrow scope | Documented owner, operations limited, user-level checks applied in the solution, actions logged with the requesting user |
| No user present (schedule, event) | Agent identity or service identity | Owner, narrow scope, review date, no interactive sign-in |
| Azure-hosted component calling Azure resources | Managed identity | Role assignments at the narrowest resource level |
| Agent calling another agent | Pass through user context where supported, otherwise a scoped service identity | Trust boundary documented; no rights escalation across the hop |
| Maker's personal account | Not acceptable for shared solutions | Only for the maker's own private use, never shared |

Each non-human identity carries an owner, purpose, scopes, the solution it serves, its creation date, its review date
and its retirement trigger.

## Practitioner approach

Draw the request path before choosing anything. Start with the person or trigger, then each component the request
passes through, then each system touched. At every arrow, write the identity used today or proposed. Most identity
problems become obvious at this stage: an arrow labelled with a maker's name, or two arrows where rights silently widen.

Default to delegated user identity for anything that starts with a person. It keeps the solution inside what that
person could do, makes audit trails meaningful and lets existing permissions and conditional access do their work.
Narrow the scopes to the operations the interface catalogue lists; broad delegated scopes are a common and avoidable
finding.

Where the far system cannot accept the user's identity, accept a service identity only with compensating design. The
solution must check, before acting, that the requesting user is entitled to the outcome, and must log both the service
identity and the requesting user. Without that check, a service identity turns every user into its owner.

For work without a user, decide whether the platform's agent identity or a conventional service identity suits better,
using the current source records. Either way, give it an owner, a narrow scope, no interactive sign-in and a review
date. Treat agent identities as you would any privileged non-human account: they appear in access reviews and are
retired with the solution.

Check consent and policy interaction. Find out whether users may consent to the scopes requested or whether
administrator consent is needed, and whether conditional access applies to the identities involved. A design that
works in a test tenant can fail in production because of a policy nobody checked.

Close with lifecycle. Record every non-human identity in the solution's entry in the inventory, with owner and review
date, so `platform-governance:ai-solution-inventory` and access reviews can find it. When the solution changes owner or
retires, its identities change or retire with it.

## Outputs

- An identity map for the solution: request path, identity per hop, scopes, consent route and compensating checks.
- A non-human identity register entry per identity: owner, purpose, scopes, solution, review date and retirement trigger.
- An architecture decision record on the `architecture-decision-record` template for any service identity used where user identity was preferred.

## Microsoft platform considerations

Microsoft Entra provides user, service principal, managed and agent identities, and Copilot Studio, Agent Builder and
Microsoft Foundry expose different authentication options. These change often; confirm current options and behaviour in
`ms-agents-extensibility` and `ms-copilot-studio-security-governance`, and work with the identity team on consent and
conditional access settings.

## Adoption considerations

Not applicable as an adoption activity, because identity design is invisible to users when done well. Makers do need a
short pattern guide so they stop reaching for their own account.

## Knowledge considerations

Grounding on Microsoft 365 content is permission-trimmed to the signed-in user. If a design substitutes a service
identity for grounding, the trimming is lost and the knowledge exposure must be reassessed with
`ai-architecture:grounding-patterns`.

## Security and privacy considerations

This skill is the identity design that the `security-privacy` review tests. Pay particular attention to rights that
widen across hops, identities without owners and service identities used to read personal data.

## Responsible AI considerations

When an agent acts without a user present, accountability must still sit with a named role. Record the accountable role
for each autonomous identity, and route autonomous action affecting people to the `responsible-ai` review.

## Evaluation requirements

Test with at least two users of different rights and confirm that outcomes differ as expected. For service identities,
test that the solution's entitlement check refuses a user who should not succeed.

## Value measures

At portfolio level, track the share of shared solutions using user or documented service identities, non-human
identities with owners and in-date reviews, and identity-related review findings. The AI solution architect and the
identity team own these measures, with a baseline from the first inventory.

## Scale notes

### Starter

Keep shared agents on delegated user identity and avoid service identities unless the identity team agrees one. Record
the few identities in a simple list.

### Scale

Publish approved identity patterns, include AI identities in regular access reviews and require an identity map for
every solution with actions.

### Enterprise

Manage AI identities through the organisation's identity governance process, with naming standards, automated discovery
and lifecycle, and federated review of standard patterns.

## Hand-offs

- To `security-privacy:ai-identity-and-access-review` for the security gate.
- To `copilot-studio:studio-authentication` or `ai-engineering:secrets-and-identity` for implementation.
- To `platform-governance:ai-solution-inventory` to record non-human identities.

## Reviewer gates

From risk tier 2 the identity map is reviewed by `security-privacy`, whose findings can block release, and by
`design-authority` for conformance with the reference architecture.

## Failure modes

- A maker's connection is embedded in a shared agent and every user acts with the maker's rights.
- A service identity is granted broad rights and the solution never checks the requesting user's entitlement.
- An agent identity outlives its solution and owner, and still holds access nobody reviews.
- Conditional access blocks the production identity and the solution fails on launch day.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Use a maker's personal account for a shared solution.
- Grant a non-human identity broader rights than the operations it performs.
- Leave a non-human identity without an owner, review date and retirement trigger.
- Substitute a service identity for user identity without an entitlement check and logging of the requesting user.

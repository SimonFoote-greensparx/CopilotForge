---
name: ai-data-access-model
description: Defines the organisation-wide model for how AI reaches data - when access must be user-delegated, when an agent or service identity may act, which identity patterns each data class allows, who approves access, and how it is reviewed - so every solution starts from approved patterns. Use when agents need data beyond the user's own access, when makers keep inventing access patterns, or when data owners ask what AI may reach.
license: CC-BY-4.0
metadata:
  department: data-governance
  lifecycle: Mobilise, Enable, Deliver, Scale
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: entra, purview, power-platform, copilot-studio, ai-foundry, sharepoint, fabric, azure
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-privacy, ms-copilot-studio-security-governance, ms-managed-environments, ico-ai-data-protection, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI data access model

## Purpose

Copilot inherits the user's access, which is simple and safe when permissions are right. Agents and automations are
different: they may act with the user's identity, a maker's connection, a service identity or an agent identity, and
each choice changes who can effectively reach which data. Without an organisation-wide model, every maker invents an
access pattern and every reviewer argues it from scratch. This skill defines approved access patterns for AI by data
class, who approves exceptions, and how access is reviewed, so solutions start compliant and data owners know what AI
may reach. It goes wrong when the model is written as abstract principle that makers cannot apply, or when it ignores
the cases where user-delegated access genuinely does not fit.

## When to use

- Agents or automations need data the user cannot open directly, or need to act when no user is present.
- Makers keep choosing their own access patterns and reviewers keep rejecting them.
- Data owners ask what AI may reach in their systems and under whose authority.
- The organisation is setting up governance for agents and needs access rules before scaling.
- A new data platform or business system is being opened to AI.

## When not to use

- Reviewing the identities and access of one specific solution - use `security-privacy:ai-identity-and-access-review`.
- Designing the identity architecture for users, agents and services - use `ai-architecture:ai-identity-design`.
- Defining what each data class permits AI to do with the data - use `data-governance:data-classification-for-ai`.
- Setting connector and data policies for environments - use `platform-governance:connector-policy`.

## Questions to ask first

1. Which data classes and systems will AI reach, and what does the classification scheme say about each?
2. For each class, can user-delegated access meet the need, or do solutions genuinely need to act beyond the user's own access?
3. Which non-human identities - service principals, managed identities, agent identities - are approved, and who owns them?
4. Who approves an access pattern for a data asset: the data owner, the security lead, or both?
5. How often is AI access reviewed, and what triggers an earlier review?

## Required inputs

- The classification scheme with AI-use rules from `data-governance:data-classification-for-ai`.
- The AI data inventory, showing which assets AI solutions reach today and how.
- The identity architecture from `ai-architecture:ai-identity-design`, where it exists.
- Data owners for the main systems AI will reach.

Where data owners are not identified, the model can define patterns but not approve their use for specific assets;
record the gap. Never approve access to a data asset on the owner's behalf.

## Decision framework

Prefer the pattern that gives the narrowest effective access. Typical approved patterns, to adapt:

| Pattern | Description | Allowed for | Conditions |
|---|---|---|---|
| A. User-delegated | AI acts with the signed-in user's own permissions | All classes the user may open, subject to classification rules | Permissions at source are correct; oversharing reviewed |
| B. User-delegated with narrowed scope | User's permissions, further limited to specific sources or fields | Confidential data where the use needs only part of what the user can see | Scope documented and tested |
| C. Scoped service or agent identity, read-only | A non-human identity with read access to defined data, used when users lack direct access or no user is present | General internal; confidential only with data owner approval | Owner named, permissions scoped to fields or records needed, outputs limited to what the audience may see |
| D. Scoped service or agent identity, write | As C, with write to defined records | Specific, approved operations only | Confirmation or human approval for writes at tier 2+; audit trail |
| E. Maker's personal connection shared with others | The maker's credentials used by other users | Not allowed for shared solutions | Replace with A to D |

| Decision | Who approves |
|---|---|
| Pattern A or B on any class | Solution owner, within classification rules |
| Pattern C on confidential data, or D on any data | Data owner and security lead |
| Any pattern on restricted data | Data owner, security lead and DPO where personal data is involved, with tier 3+ review |

## Practitioner approach

Start with the default. For most Copilot and agent use, user-delegated access is the right answer: the solution can
reach only what the user could open anyway, so access control stays where it already is, at the source. Say so plainly
in the model, and make deviations the exception that needs a reason.

Then deal honestly with the exceptions. Some needs cannot be met with user-delegated access: an agent that answers
customers who have no internal account, an automation that runs overnight, an HR agent that must check a policy table
staff cannot browse. For each, the model offers a scoped non-human identity with clear conditions. The key condition is
that the solution must not reveal more to the user than the user is entitled to see, even if the identity can read
more. That condition has to be designed and tested, not stated in instructions.

Write the patterns as a short catalogue with names makers can use: "this agent uses pattern C on the facilities
bookings table". Give each pattern its conditions, its approver and a worked example. Abstract principles such as
"least privilege" are necessary but not sufficient; makers need the concrete pattern.

Agree approval routes with data owners. Owners should approve non-human access to their data, know which solutions have
it, and be able to withdraw it. Make the approval light for low-risk patterns and deliberate for writes and restricted
data.

Ban the borrowed identity explicitly. Sharing a solution that runs on the maker's personal connection gives every user
the maker's access. The model should name this pattern as not allowed for shared solutions and point to the alternatives.

Set the review cycle. Non-human access to data should be reviewed at least as often as human privileged access, and
whenever a solution's audience, purpose or owner changes. Link the review to the solution inventory so access does not
outlive the solution.

Publish the model with the platform and security teams, and check new solutions against it at design rather than at
the gate. Confirm platform capabilities for scoping, agent identities and access reviews in the source records, as
they change.

## Outputs

- An AI data access model: the pattern catalogue with conditions and examples, the approval matrix by data class, the review cycle and the prohibited patterns.
- A register of approved non-human access to data assets, linked to the AI data inventory.
- Guidance for makers on choosing a pattern, with worked examples.

## Microsoft platform considerations

How user-delegated and non-human access work differs between Microsoft 365 Copilot, agents built in Agent Builder,
Copilot Studio, Power Platform and Foundry, and Microsoft Entra capabilities for agent identities, conditional access
and access reviews evolve quickly. Confirm current options in `ms-copilot-privacy`,
`ms-copilot-studio-security-governance` and `ms-managed-environments` before naming a platform mechanism in a pattern.

## Adoption considerations

A clear pattern catalogue speeds makers up: they choose an approved pattern instead of waiting for a bespoke review.
Publish it where makers start, alongside the environment and connector guidance.

## Knowledge considerations

Knowledge in SharePoint usually follows pattern A. Where an agent needs to ground on content users cannot open, treat it
as pattern C and involve the knowledge owner and `knowledge-management:knowledge-classification`.

## Security and privacy considerations

The model is a security control. `security-privacy:ai-identity-and-access-review` checks solutions against it, and
`security-privacy:data-exposure-review` checks that outputs do not reveal more than users are entitled to see.

## Responsible AI considerations

Patterns that let AI reach data about people beyond the user's own access need particular care where outputs inform
decisions about those people. Flag such uses to `responsible-ai:ai-impact-assessment`.

## Evaluation requirements

For patterns C and D, test that users cannot obtain data beyond their entitlement through the solution, using test
users with different access. Keep results with the solution's release evidence.

## Value measures

Track the share of solutions using approved patterns, the number of non-human identities with access to data and an
owner, and exceptions approved. The data governance lead owns these, with the security lead for identity measures.

## Scale notes

### Starter

Adopt pattern A as the rule and allow C only for a few named, owner-approved cases. Ban pattern E from the start.

### Scale

Publish the full catalogue and approval matrix, register non-human access, and review it on a cycle with data owners.

### Enterprise

Integrate the model with enterprise identity governance and access reviews, align patterns across business units, and
audit non-human data access across the portfolio.

## Hand-offs

- To `security-privacy:ai-identity-and-access-review`, which checks solutions against the model.
- To `ai-architecture:ai-identity-design` to implement patterns in the architecture.
- To `platform-governance:connector-policy` to align connector policies.
- To data owners with the approval routes for their assets.

## Reviewer gates

The model is approved by the `security-privacy` lead before publication. From risk tier 2, solutions are checked
against it at the `security-privacy` gate.

## Failure modes

- The model says "least privilege" without patterns, so makers still invent their own.
- A service identity reads everything and the agent reveals data users should not see.
- Makers share solutions running on their personal connections because nothing explicitly forbids it.
- Non-human access outlives the solution it was granted for.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Approve AI access to a data asset on its owner's behalf.
- Allow shared solutions to run on a maker's personal connection.
- Rely on agent instructions to stop a solution revealing data its identity can read.
- Grant non-human access without an owner and a review date.

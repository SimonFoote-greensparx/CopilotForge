---
name: ai-solution-retirement
description: Retires a live agent or AI solution safely once the decision is made - notifying users and pointing them to alternatives, removing sharing, disabling the solution, revoking connections, service identities and secrets, handling transcripts and logs under retention rules, cleaning up dependent flows and indexes, and closing the inventory record. Use when a review or owner decides to retire a solution, or when ownerless solutions accumulate.
license: CC-BY-4.0
metadata:
  department: ai-operations
  lifecycle: Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, copilot-cowork, ai-foundry, power-platform, sharepoint, entra
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-coe-starter-kit, ms-managed-environments, ms-copilot-studio-security-governance, ms-copilot-privacy, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# AI solution retirement

## Purpose

Retiring an AI solution is more than switching it off. Users need an alternative, connections and identities with
standing access must be revoked, conversation data and evaluation records must be kept or deleted under the
organisation's rules, dependent flows and indexes must be cleaned up, and the inventory must show the solution is gone.
This skill carries out retirement safely once the decision has been made. Retirement usually goes wrong when the agent
is unshared but its connections and service identities keep their access, when users are not told and keep looking for
it, or when transcripts are deleted that the organisation was required to keep - or kept when they should have gone.

## When to use

- A scheduled review or scale-or-stop decision concludes that a solution should be retired.
- A solution has no active owner and the overdue rule leads to retirement.
- A solution is being replaced by a new one or by a standard Copilot capability.
- An incident review recommends permanent withdrawal.
- The inventory shows inactive solutions that still hold connections or shared access.

## When not to use

- Deciding whether to stop a solution after a pilot - use `opportunity-management:scale-or-stop`.
- Temporarily suspending a solution during an incident - use `ai-operations:ai-incident-management` and `ai-operations:ai-continuity`.
- Managing an agent's whole lifecycle from release onward - use `m365-agents:agent-lifecycle` or `copilot-studio:studio-agent-lifecycle`.
- Clearing outdated knowledge content across the estate - use `knowledge-management:knowledge-cleanup`.
- Setting retention rules for AI interaction data - use `security-privacy:ai-interaction-retention`.

## Questions to ask first

1. Who made the retirement decision, on what evidence, and is it recorded?
2. Who uses the solution today, and what will they use instead?
3. What does the solution connect to - connectors, service identities, secrets, flows, indexes, other agents?
4. What data does it hold or generate - transcripts, logs, feedback, evaluation datasets - and what do retention rules require for each?
5. Does any other solution, flow or process depend on it?

## Required inputs

- The retirement decision record with the decision owner and date.
- The solution's runbook, dependency record and inventory entry.
- The organisation's retention rules for AI interaction data and records, confirmed with the records manager or DPO.
- Usage data at team level, to identify who must be told.

Where retention rules for the solution's data are unclear, hold the data in a restricted state and ask the DPO or
records manager before deleting anything; never delete or keep by default.

## Decision framework

Retire in stages, each with an exit check.

| Stage | Actions | Exit check |
|---|---|---|
| 1. Confirm | Decision recorded; dependencies and data identified; alternative agreed; retirement date set | Decision owner signs; no unknown dependants |
| 2. Notify | Users, managers, service desk and Champions told the date, the reason in plain words and the alternative | Notice given with agreed lead time |
| 3. Freeze | No further changes; banner or message inside the solution pointing to the alternative | Message visible |
| 4. Withdraw | Sharing removed, solution unpublished or disabled, removed from catalogues and app stores | Users can no longer reach it |
| 5. Revoke | Connections, service identities, app registrations, secrets and API keys disabled or deleted; dependent flows stopped | No standing access remains |
| 6. Data | Transcripts, logs, feedback and evaluation data kept, archived or deleted per retention rules; reusable datasets transferred | Disposal or retention recorded |
| 7. Close | Inventory updated, knowledge indexes created for the solution removed, value close-out and lessons recorded | Record shows retired with date |

Depth by tier: tier 1 can complete stages 1 to 7 in one short checklist; from tier 2, revocation and data handling are
checked by a second person; from tier 3, `security-privacy` confirms revocation and data disposal.

## Practitioner approach

Confirm the decision before acting. Retirement is irreversible in parts - deleted connections and data cannot always be
restored - so check the decision is recorded, the decision owner has authority, and the alternative is ready. If the
replacement is not yet live, set the retirement date after it.

Find everything the solution touches. Use the runbook, the inventory and admin tooling to list connectors and
connections, service identities and app registrations, secrets, flows it calls or that call it, knowledge indexes built
for it, and other agents that hand off to it. Missing items here become orphaned access later, which is the main
security risk of retirement.

Tell people early and plainly. Users should hear from their own managers or channels, not discover a missing agent.
Say what is changing, when, why in a sentence, and what to use instead. Brief the service desk and Champions so they
can answer questions. Put a message inside the solution itself during the freeze period.

Withdraw before you revoke. Remove sharing and unpublish first so users stop reaching the solution, then revoke the
connections, identities and secrets. Check each revocation with the platform or identity team; a disabled agent whose
service identity still holds write access to a business system is an open door.

Handle data deliberately. Conversation transcripts, logs, feedback and evaluation datasets may be records the
organisation must keep, personal data it must delete, or assets worth reusing. Classify each with the records manager
or DPO, then archive, transfer or delete accordingly and record what was done. Golden datasets and rubrics are often
reusable for the replacement; transfer them with their owners.

Clean up around it. Stop dependent flows, remove knowledge indexes or copies made solely for the solution, and close
monitoring alerts and support catalogue entries so nobody is paged for a retired solution. Leave the knowledge sources
themselves to their owners.

Close the record. Update the inventory with the retirement date and the location of retained records. Record a short
value close-out and lessons: what the solution achieved, why it was retired, and what to do differently. Share lessons
with the CoE; well-run retirements show the organisation can stop things, which makes it safer to start them.

## Outputs

- A completed `retirement-checklist` covering all seven stages, with evidence and sign-offs.
- User and service desk communications.
- A data disposition record for transcripts, logs, feedback and evaluation data.
- An updated inventory record and a short lessons and value close-out note.

## Microsoft platform considerations

How agents are unpublished, unshared and deleted, how connections and identities are found and revoked, and what
conversation data is retained differ by route and change over time. Use admin tooling and inventory, including the CoE
Starter Kit and Managed Environments features where available, and confirm current behaviour in `ms-coe-starter-kit`,
`ms-managed-environments`, `ms-copilot-studio-security-governance` and `ms-copilot-privacy`.

## Adoption considerations

Retirement is a change for users. Give enough notice, point to a real alternative, and acknowledge what the solution did
well. A clean retirement builds trust that the AI portfolio is looked after.

## Knowledge considerations

Knowledge sources belong to their owners and usually outlive the solution. Remove indexes or copies made only for the
solution, tell knowledge owners that a dependent has gone, and update dependency records.

## Security and privacy considerations

Revoking connections, service identities and secrets is the security-critical step. From tier 3, `security-privacy`
confirms no standing access remains. Data disposal follows retention rules agreed with the DPO, in line with
`security-privacy:ai-interaction-retention` and data protection guidance in `ico-ai-data-protection`.

## Responsible AI considerations

Where the solution supported decisions about people, make sure records needed to answer challenges or appeals are kept
for the required period, and that affected people still have a route to raise concerns after retirement.

## Evaluation requirements

Not applicable for the retired solution itself, since it will not be evaluated again; transfer reusable datasets and
rubrics to the replacement's owners through `evaluation-quality:golden-dataset` where relevant.

## Value measures

Track retirements completed against plan, solutions found with standing access after retirement (target none), time from
decision to closed record, and lessons recorded. The AI Operations Lead owns these measures; report by solution and
portfolio, never by individual owner.

## Scale notes

### Starter

A short checklist completed by the owner: tell users, unshare, delete connections, decide what happens to transcripts
with whoever handles data protection, and update the agent list.

### Scale

The full `retirement-checklist` for every retirement, with a second person checking revocation and data handling from
tier 2, and inventory tooling used to find dependencies.

### Enterprise

Retirement integrated with inventory, identity and records management processes, periodic sweeps for inactive solutions
with standing access, and portfolio reporting of retirements and lessons.

## Hand-offs

- To `platform-governance:ai-solution-inventory` to close the inventory record.
- To the knowledge owners and `knowledge-management:knowledge-lifecycle` with dependency updates.
- To the replacement solution's owners with reusable datasets, rubrics and lessons.
- To `ai-operations:ai-review-calendar` to remove the solution from the calendar.

## Reviewer gates

From risk tier 3, `security-privacy` confirms that connections, identities and secrets are revoked and that data
disposal follows the agreed retention rules; an unrevoked credential is a blocking finding. Below tier 3, a second
person checks those stages from tier 2.

## Failure modes

- The agent is unshared but its service identity keeps write access to a business system.
- Users are not told, keep searching for the agent and lose trust in the portfolio.
- Transcripts are deleted that were needed to answer a later challenge, or kept long after they should have gone.
- The inventory still shows the solution as live, and it stays on review and monitoring lists for months.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Treat unsharing or unpublishing as complete retirement while connections and identities remain active.
- Delete or keep interaction data by default without confirming retention rules with the DPO or records manager.
- Retire a solution users depend on without notice and an alternative.
- Delete knowledge sources that belong to their owners as part of retiring a solution.

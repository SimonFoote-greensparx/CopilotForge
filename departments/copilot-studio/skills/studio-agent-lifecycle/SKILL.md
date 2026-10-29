---
name: studio-agent-lifecycle
description: Keeps the technical estate of Copilot Studio agents healthy from creation to retirement - owners and co-owners, orphaned, inactive or duplicate agents, periodic recertification, Microsoft platform changes, and retiring an agent with its flows, connections, environment variables and stored data. Use when the number of Studio agents is growing, when a maker leaves, or when an agent has gone unused for months.
license: CC-BY-4.0
metadata:
  department: copilot-studio
  lifecycle: Launch, Measure, Scale, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: copilot-studio, power-platform
  edition-support: starter, scale, enterprise
  reviewers: design-authority, security-privacy
  sources: ms-coe-starter-kit, ms-copilot-studio-guidance, ms-managed-environments, ms-copilot-studio-security-governance
  status: draft
  authors: Simon Foote
---

# Studio agent lifecycle

## Purpose

Copilot Studio makes agents easy to create, which means they are also easy to forget. Within a year an organisation can
have hundreds of agents, some valuable, many abandoned, a few still shared widely with nobody responsible for them. This
skill keeps the technical estate of Studio agents healthy: every agent registered with an owner and co-owner, inactive
and orphaned agents found and dealt with, live agents recertified on a cycle, platform changes absorbed, and retired
agents removed completely, including the flows, connections and data they leave behind. It usually goes wrong when
lifecycle is left to individual makers, when an owner leaves and their agents keep running on their connections, or when
"retirement" means unpublishing a channel and leaving everything else in place.

## When to use

- The number of Studio agents is growing and nobody has a complete view of them.
- A maker or owner is leaving or changing role and owns agents others use.
- An agent has been unused for months, duplicates another, or has no identifiable owner.
- A Microsoft platform change, deprecation or new capability affects existing agents.
- An agent is to be retired and needs removing cleanly.

## When not to use

- The business lifecycle of any agent, including review dates and value-led decisions - use `m365-agents:agent-lifecycle`.
- The organisation-wide inventory of agents, flows and AI solutions - use `platform-governance:ai-solution-inventory`.
- Retiring AI solutions generally, including user communications and continuity - use `ai-operations:ai-solution-retirement`.
- Scheduling reviews across all live AI solutions - use `ai-operations:ai-review-calendar`.
- Moving versions between environments - use `copilot-studio:studio-alm`.

## Questions to ask first

1. Where do Studio agents live today, and is there an inventory that includes owners, environments, sharing and last use?
2. Does every shared agent have a business owner, a technical owner and a co-owner who can act if the owner leaves?
3. What counts as inactive for this organisation, and what happens to an inactive agent?
4. How are Microsoft platform changes tracked and assessed for impact on existing agents?
5. What must be removed or retained when an agent is retired - flows, connections, environment variables, tables, transcripts?

## Required inputs

- An inventory of agents with environment, owner, sharing, channels and last activity, for example from the CoE Starter Kit or admin reports.
- Ownership records and the agent register maintained under `m365-agents:agent-lifecycle`.
- The organisation's retention rules for transcripts and agent data.
- Leaver and role-change notifications from HR or identity processes, at role level.

If the inventory is incomplete, say so and start with the environments that matter most: production, then team
environments, then the default environment. Never conclude an agent is unused without checking its activity data.

## Decision framework

| State | Signal | Action |
|---|---|---|
| Healthy | Owner and co-owner confirmed, in the right zone, recertified on time | Continue; recertify at the next cycle |
| Orphaned | Owner left or unknown | Find a new owner within an agreed period; otherwise restrict sharing and plan retirement |
| Inactive | No meaningful use for the agreed period | Ask the owner to justify, merge or retire |
| Duplicate | Same purpose as another agent | Merge into the better-governed agent and retire the other |
| Misplaced | Shared widely from a personal or default environment | Move through ALM or restrict sharing |
| Affected by change | Platform change or deprecation touches its features | Assess impact, plan change through ALM, regression test |

Recertification frequency rises with risk tier: annually at tier 1, at least twice a year at tier 2, and quarterly or as
the release policy sets at tier 3 and above.

## Practitioner approach

Start with visibility. Build or refresh the inventory of Studio agents across environments, with owner, co-owner,
environment, sharing scope, channels, connections and last activity. Use the platform's admin data and inventory tools
rather than asking makers to self-report. Reconcile it with the agent register so business and technical records agree.

Fix ownership first. Every shared agent needs a business owner, a technical owner and a co-owner with enough rights to
act. Connect lifecycle to leaver and role-change processes so that when someone moves on, their agents, flows and
connections are reassigned before their account is disabled. An agent running on a departed person's connection fails
suddenly or, worse, keeps working with rights nobody controls.

Deal with the long tail calmly. Contact owners of inactive and duplicate agents with a clear choice: justify, merge or
retire, by a date. Where no owner responds, restrict sharing first, then retire after a notice period. Communicate with
users of any agent that is narrowed or removed, and point them to the replacement.

Recertify live agents on a cycle set by risk tier. Recertification asks the owner to confirm that the purpose, audience,
knowledge, tools, connections and identity are still right, that the regression pack still passes and that the agent
still delivers value. An agent that cannot be recertified is narrowed or retired.

Absorb platform change deliberately. Microsoft changes orchestration, knowledge, tools, channels and admin controls often.
Track announcements through the platform team, assess which agents a change affects using the inventory, and schedule
the work through ALM with regression testing. Deprecations need an owner and a date, not a hope.

Retire completely. Unpublish channels, remove sharing, export what must be retained, then delete the agent and its
dependent flows, connections, connection references, environment variables and tables that nothing else uses, and handle
transcripts under the retention rules. Record the retirement in the inventory and the register, so the agent does not
reappear in next year's review as a mystery.

## Outputs

- A Studio agent inventory reconciled with the agent register, showing owner, co-owner, zone, sharing, activity and recertification date.
- An estate health report: orphaned, inactive, duplicate and misplaced agents with actions, owners and dates.
- Recertification records per agent.
- A retirement checklist and record covering every dependent component and data item.

## Microsoft platform considerations

Inventory, inactivity detection, ownership reassignment, sharing controls and deletion behaviour depend on admin tools
and settings that change over time. Use `ms-coe-starter-kit` and `ms-managed-environments` for inventory and governance
features, check `ms-copilot-studio-guidance` for current agent management behaviour and
`ms-copilot-studio-security-governance` for admin controls, and confirm deletion and retention behaviour before retiring.

## Adoption considerations

Makers fear losing work. Explain the lifecycle rules up front, give owners notice and choices, and celebrate merges and
well-handled retirements as good stewardship rather than failure.

## Knowledge considerations

Knowledge drifts over an agent's life. Include knowledge owner confirmation in recertification, and when an agent is
retired, tell knowledge owners so they know their content is no longer served through it.

## Security and privacy considerations

Orphaned agents and connections are a security risk. Reassign or revoke them promptly, remove sharing before deletion,
and handle transcripts and stored data under retention rules. Agents shared widely from personal environments go to
`security-privacy:data-exposure-review`.

## Responsible AI considerations

Not applicable as a separate concern for estate hygiene; recertification should still confirm that any human oversight
and disclosure agreed at release remain in place for agents at tier 2 and above.

## Evaluation requirements

Recertification includes a passing regression run, and platform changes that affect an agent require regression testing
through `copilot-studio:studio-testing-and-evaluation` before the change reaches production.

## Value measures

Track the share of shared agents with confirmed owners and co-owners, recertification on time, orphaned and inactive
agents resolved, and retirements completed cleanly, owned by the Copilot Studio Architect at portfolio level.

## Scale notes

### Starter

A simple inventory of shared agents with owners and co-owners, a leaver checklist that includes agents, and an annual
review that retires what nobody uses.

### Scale

Automated inventory, inactivity rules with owner notifications, recertification by risk tier and a standard retirement checklist.

### Enterprise

Integrated lifecycle with identity and HR processes, automated restriction of orphaned agents, platform-change impact
assessment across the estate, and lifecycle reporting to the CoE.

## Hand-offs

- To `m365-agents:agent-lifecycle` for business decisions on value, scope and review dates.
- To `ai-operations:ai-solution-retirement` for user communications and continuity when retiring a significant agent.
- To `copilot-studio:studio-alm` for changes driven by platform updates.
- To `platform-governance:ai-solution-inventory` with reconciled inventory data.

## Reviewer gates

From risk tier 2, `design-authority` reviews recertification and supportability, and `security-privacy` reviews orphaned
connections and sharing. A tier 2 or higher agent without a current owner is a blocking finding.

## Failure modes

- An owner leaves and their agents keep running on their connections until the account is disabled and everything breaks.
- Inactive agents remain shared widely with stale knowledge for years.
- Retirement unpublishes the channel but leaves flows, connections and transcripts behind.
- A platform deprecation is noticed only when agents stop working.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Leave a shared agent without a business owner, technical owner and co-owner.
- Delete an agent without checking activity, notifying its owner and users, and handling its data under retention rules.
- Treat unpublishing as retirement while flows, connections and data remain.
- Use lifecycle data to judge individual makers' performance.

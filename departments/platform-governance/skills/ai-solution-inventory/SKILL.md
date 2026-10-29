---
name: ai-solution-inventory
description: Builds and keeps current an inventory of agents, flows, Cowork plugins and custom AI solutions across Microsoft 365, Power Platform and Azure - discovered from admin sources, reconciled with the agent portfolio register, with owners, zone, risk tier, sharing reach and review dates, and orphans flagged. Use when nobody can say how many agents exist, when an audit asks for a list, or when orphaned or unregistered solutions need finding.
license: CC-BY-4.0
metadata:
  department: platform-governance
  lifecycle: Mobilise, Assure, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, power-platform, copilot-cowork, ai-foundry, azure, entra
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-coe-starter-kit, ms-managed-environments, ms-copilot-studio-security-governance, ms-copilot-studio-guidance, ms-copilot-cowork-customise
  status: draft
  authors: Simon Foote
---

# AI solution inventory

## Purpose

An organisation cannot govern what it cannot see. This skill builds and maintains an inventory of the AI solutions that
exist - agents, flows with AI steps, Cowork plugins and skills, and custom solutions in Azure - by discovering them from
admin sources and reconciling them with the agent portfolio register that records what was approved. The gap between
what exists and what is registered is the governance work. Inventories go wrong when they are spreadsheets filled in by
makers, when they count items but record no owners, and when they are built once for an audit and never refreshed.

## When to use

- Nobody can say how many agents and AI flows exist, or who owns them.
- An audit, regulator or executive asks for a list of AI solutions.
- Makers have left and their solutions may be orphaned.
- The register shows approved solutions but admin data suggests many more exist.
- Admin monitoring, release policy or reviews need a reliable list to work from.

## When not to use

- Managing the CoE's portfolio of planned and live solutions and their priorities - use `ai-centre-of-excellence:coe-portfolio-management`.
- Inventorying data used by AI solutions - use `data-governance:ai-data-inventory`.
- Inventorying knowledge sources - use `knowledge-management:knowledge-inventory`.
- Watching usage and estate trends over time - use `platform-governance:ai-admin-monitoring`.
- Managing one agent from release to retirement - use `m365-agents:agent-lifecycle`.

## Questions to ask first

1. Which platforms can hold AI solutions in this tenant, and which admin sources can list them?
2. Is there an existing register of approved solutions, and what fields does it hold?
3. Who needs the inventory - CoE, security, audit, operations - and for what decisions?
4. How often must it be current, and who will reconcile it?
5. What threshold of reach or risk makes an item worth registering, rather than only counting?

## Required inputs

- Admin access, or a delegated report, for each platform in scope.
- The agent portfolio register fields from the governance starter or `ai-centre-of-excellence:coe-governance-model`.
- The environment zoning plan, to place each item in a zone.
- The organisation's joiner, mover and leaver data, to detect orphans.

Where a platform cannot be queried, list it as a known blind spot in the inventory; never report a count as complete
when a source is missing.

## Decision framework

Not every item needs the same treatment. Decide by reach and risk.

| Item | Treatment |
|---|---|
| Personal item used only by its maker | Counted in aggregate; no register entry; clean-up rules apply |
| Shared with a team or group | Register entry with owners, zone, review date |
| Shared beyond a team, or tier 2 and above | Full register entry, linked to release record and reviews |
| Custom solution in Azure or Foundry | Full register entry, including identities, endpoints and cost owner |
| Discovered but unregistered and shared | Flagged; owner contacted; registered, moved or removed within an agreed period |
| Owner has left | Flagged as orphaned; transferred or retired |

Minimum fields for a register entry: name, platform, environment or subscription, zone, purpose, business owner,
technical owner, knowledge owner where relevant, audience and sharing reach, risk tier, connectors and identities,
release date, review date and status.

## Practitioner approach

Begin with discovery, not with a form. Use the admin sources for each platform to list agents, flows, apps, Cowork
customisations and Azure AI resources, with their creators, environments and sharing. The inventory components of the
CoE Starter Kit or the admin centres usually provide most of this for Power Platform and Copilot Studio; Azure and other
sources need their own queries. Check the source records for what each currently exposes.

Count everything, register what matters. Personal items are counted and subject to clean-up; shared items get register
entries. Applying full registration to every personal experiment wastes effort and discourages building.

Reconcile discovery with the register. Three lists result: registered and found, which is healthy; found but not
registered, which needs follow-up; and registered but not found, which usually means a retired solution that was never
closed in the register. Work the second list first, starting with the widest reach.

Find owners. For every shared item, confirm the business and technical owner. Cross-check with leaver data to find
orphans, and contact the maker's manager or business unit to agree a new owner, retirement or archive.

Add the identities and connections each shared solution uses, because these are what security and operations most often
need. Non-human identities recorded by `ai-architecture:ai-identity-design` belong here.

Automate the refresh. A manual inventory is out of date within weeks. Schedule discovery, reconciliation and owner checks
on a cycle that matches the pace of building, and publish the result to those who need it.

Keep personal data in the inventory to what governance needs: owner names for shared solutions are necessary; usage by
named individual is not. Report trends at team or business unit level.

## Outputs

- An AI solution inventory: discovered items by platform, zone and reach, with aggregate counts for personal items.
- Agent portfolio register entries for shared solutions, using the fields in the `ai-governance-starter` template.
- Exception lists: unregistered shared items, orphaned items and registered items not found, each with an action and owner.
- A refresh schedule and the known blind spots.

## Microsoft platform considerations

Discovery sources include the Power Platform and Microsoft 365 admin centres, Copilot Studio inventory views, the CoE
Starter Kit and Azure resource queries, and each changes over time. Check `ms-coe-starter-kit`, `ms-managed-environments`
and `ms-copilot-cowork-customise` for current inventory capabilities rather than assuming coverage.

## Adoption considerations

Makers co-operate with an inventory that helps them, for example by reminding them of review dates or warning that a
solution relies on a leaver's connection. Avoid presenting it as surveillance.

## Knowledge considerations

Record the knowledge sources and knowledge owner for each shared agent, so `knowledge-management` can see which content
agents depend on before changing it.

## Security and privacy considerations

The inventory is a sensitive asset in itself, because it maps connections and identities. Restrict access to those who
need it, and share the identity and connector view with the `security-privacy` reviewers.

## Responsible AI considerations

Flag registered solutions whose purpose involves decisions about people, so their review dates and oversight
arrangements can be checked. The inventory never records individual users' interactions.

## Evaluation requirements

Not applicable to the inventory's subject matter, because it does not evaluate solutions. Check the inventory's own
accuracy by sampling: confirm a handful of entries against the platform each cycle.

## Value measures

At estate level, track the share of shared solutions with a register entry, orphaned items found and resolved, time to
resolve unregistered items and blind spots remaining. The platform governance lead owns these measures, with a baseline
from the first discovery.

## Scale notes

### Starter

A discovery export and a simple list of shared agents with owners, refreshed monthly, is enough at first.

### Scale

Automate discovery for Power Platform and Copilot Studio, reconcile with the register monthly, and connect leaver data.

### Enterprise

Cover all platforms including Azure, automate reconciliation and owner checks, federate follow-up to business units and
provide inventory views to audit and security.

## Hand-offs

- To `ai-centre-of-excellence:coe-portfolio-management` with the reconciled register.
- To `platform-governance:ai-admin-monitoring` as the base for trend monitoring.
- To `ai-operations:ai-solution-retirement` for orphaned items to retire.
- To `m365-agents:agent-ownership` where a shared agent needs new owners.

## Reviewer gates

Not applicable as a gate, because the inventory supports reviews rather than releasing anything. Reviewers in
`security-privacy` and `design-authority` rely on it, so its blind spots are disclosed to them.

## Failure modes

- The inventory is a maker-maintained spreadsheet and misses everything nobody thought to add.
- Counts are reported without owners, so nobody can act on them.
- It is built for one audit and is out of date within a month.
- Azure and Foundry solutions are left out because the admin sources differ.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Report the inventory as complete when a platform could not be queried.
- Record or report individual usage in the inventory.
- Leave a discovered, widely shared solution without an owner or follow-up action.
- Rely on makers to self-report as the only discovery method.

---
name: knowledge-inventory
description: Builds and maintains a register of the organisation's knowledge sources - sites, libraries, wikis, Teams files, connector content and curated collections - recording domain, owner, audience, sensitivity, condition, review date and which Copilot or agent uses depend on each. Use when nobody can say where authoritative knowledge lives, before choosing agent sources at scale, or when the register is stale.
license: CC-BY-4.0
metadata:
  department: knowledge-management
  lifecycle: Discover, Mobilise, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: sharepoint, m365-copilot, m365-agents, copilot-studio, purview
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-privacy, ms-agent-builder, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# Knowledge inventory

## Purpose

An organisation cannot govern, clean or ground AI on knowledge it cannot list. This skill produces a living register of
knowledge sources: where each one lives, what it covers, who owns it, who should see it, what condition it is in and
which Copilot scenarios or agents rely on it. The register is what lets a maker pick a ready source instead of the
biggest one, and what lets an owner see the impact of a change. Inventories usually fail by trying to list every file,
or by being compiled once and never updated.

## When to use

- Nobody can say where the authoritative version of key knowledge lives, or several teams claim to own it.
- Makers are choosing agent knowledge sources at scale and need a list of owned, assessed sources to pick from.
- A readiness assessment has found systemic gaps and the detail now needs recording source by source.
- An existing register has drifted and owners, review dates or agent dependencies are out of date.

## When not to use

- Rating the estate's overall readiness for AI and setting the remediation plan - use `knowledge-management:knowledge-readiness-assessment`.
- Inventorying structured data sets and data products used by AI solutions - use `data-governance:ai-data-inventory`.
- Listing agents, flows and AI solutions themselves - use `platform-governance:ai-solution-inventory`.
- Verdicts on the specific sources one agent will use - use `m365-agents:knowledge-source-readiness`.

## Questions to ask first

1. What level of granularity will the register hold - site, library or curated collection - and why is that level enough for the decisions it supports?
2. Which knowledge domains are in scope first, and which AI uses depend on them?
3. Where will the register live, who maintains it, and how will owners update their own entries?
4. Which fields can be gathered from administrative reports, and which need an owner's judgement?
5. Is there an existing site directory, intranet map or records file plan to start from rather than starting again?

## Required inputs

- The domains in scope and the AI uses that depend on them, ideally from `knowledge-management:knowledge-readiness-assessment`.
- An export or report of sites, libraries and Teams with their administrative owners, from the Microsoft 365 administrators.
- The classification scheme and sensitivity labels in use, or a note that none exist.
- The current list of agents and their declared knowledge sources, where agents already exist.

Record any field that cannot be confirmed as "to confirm" with the person responsible for finding out. An
administrative site owner is not automatically the knowledge owner; record both and mark the knowledge owner as
unconfirmed until that person accepts the role.

## Decision framework

Decide what earns an entry, then what each entry must hold.

| Candidate | Register it as | Rule |
|---|---|---|
| A site or library holding authoritative content for a domain | A knowledge source | Always, at library level where audiences or owners differ within a site |
| A curated set of documents chosen for an agent | A curated collection | Always, linked to the agent that uses it |
| Connector-indexed or external system content used for grounding | A knowledge source with its source system named | Always, noting whose permission model applies |
| Working, project or team collaboration space | Not registered | Unless an agent or a documented Copilot scenario depends on it |
| Personal drives and chats | Not registered | Record as a blind spot, never as a source |

Each entry carries a mandatory core: identifier, name, location, domain, knowledge owner, administrative owner,
intended audience, sensitivity, condition rating, last review date, next review date and dependent AI uses. Optional
fields (content types, languages, retention label, volume) are added only where a decision uses them.

## Practitioner approach

Choose the unit of inventory before collecting anything. For most organisations the useful unit is the library or a
curated collection, not the file and not the whole site. A site often mixes an authoritative policy library with
working folders; registering it as one source hides the difference that matters for grounding.

Seed the register from administrative data: a list of sites, libraries and Teams with their administrative owners,
sharing settings and activity. Filter out obvious working spaces and inactive sites, and keep the remainder as
candidates. Then work domain by domain with the people who know the content. Ask which locations hold the content the
domain treats as authoritative, which are copies or working areas, and which should be retired. This conversation
usually halves the candidate list and surfaces the competing versions that cause wrong AI answers.

For each confirmed source, agree the knowledge owner. Record the intended audience in plain words, then compare it with
the actual access from administrative data; a mismatch is a finding, not something to correct silently in the register.
Record sensitivity using the organisation's scheme, and a condition rating using the same dimensions as the readiness
assessment so the two stay consistent.

Link every source to the AI uses that depend on it: named agents, Copilot scenarios that rely on it, curated
collections. This is the field that makes the register worth maintaining, because it answers the question an owner
asks before a restructure or deletion: "what breaks if I change this?"

Decide how the register stays alive. Owners should update their own entries through a simple form or list, the
Knowledge Manager should review overdue entries monthly, and agent release should require that every source is in the
register with an in-date review. A register that only the central team edits will go stale within a quarter.

Finally, publish the register to makers and agent owners as the starting list for knowledge sources, with the
condition rating visible. A maker who can see that the "HR Policies" library is rated ready and the "HR Shared" site is
not will usually make the right choice without a review board.

## Outputs

- A knowledge asset register on the `knowledge-asset-register` template, one row per source or curated collection.
- A list of blind spots and unregistered locations, with the reason they are out of scope.
- A list of findings raised during inventory (audience mismatches, missing owners, competing versions), each routed to the owning skill.
- A maintenance routine: who updates entries, how often overdue entries are chased, and which gates check the register.

## Microsoft platform considerations

Administrative reporting in SharePoint and Microsoft 365 can provide site lists, owners, sharing and activity at scale,
while Microsoft Purview can show where sensitivity and retention labels are applied; the reports available depend on
configuration and licensing, so confirm them in the source records and the licensing guide. A SharePoint list is a
practical home for the register at starter scale because owners can update their own rows and agents can ground on it.

## Adoption considerations

Make the register useful to makers before asking owners to maintain it. When owners see agents depending on their
sources, and makers see which sources are ready, upkeep becomes part of the work rather than an extra.

## Knowledge considerations

The register is the department's system of record. `knowledge-management:knowledge-review-cycles`,
`knowledge-management:knowledge-cleanup` and `knowledge-management:knowledge-grounding-standards` all read and update
it, so keep field definitions stable and documented.

## Security and privacy considerations

The register itself reveals where sensitive content lives, so restrict editing to owners and the knowledge team and
consider who can read sensitivity fields. Audience mismatches found during inventory go to
`security-privacy:data-exposure-review` from risk tier 2.

## Responsible AI considerations

Not applicable directly; the inventory records sources rather than shaping AI behaviour. Content flagged by owners as
reflecting withdrawn practice is recorded and routed to `knowledge-management:knowledge-cleanup`.

## Evaluation requirements

Sample the register quarterly: pick entries at random and check owner, audience and review date against reality. Report
the share of entries that are accurate, and treat a falling figure as a maintenance failure.

## Value measures

Track the share of agent knowledge sources that are registered with a confirmed owner, the share of entries with an
in-date review, and the time a maker takes to find a ready source. The Knowledge Manager owns these, reported by domain.

## Scale notes

### Starter

A SharePoint list or spreadsheet covering the few domains the first agents use, maintained by one knowledge lead.

### Scale

A shared register across domains with owner self-service updates, linked to the agent register and checked at agent
release.

### Enterprise

A federated register where business-unit knowledge leads maintain their domains under shared field definitions, fed by
administrative reports and reconciled with the data inventory and solution inventory.

## Hand-offs

- To `knowledge-management:knowledge-owner-model` where owners are missing or disputed.
- To `knowledge-management:knowledge-cleanup` for retired, duplicate and competing sources.
- To `m365-agents:knowledge-source-readiness` as the starting list when an agent's sources are chosen.

## Reviewer gates

Not applicable as a gate on the register itself, which records rather than releases content. Findings that touch
oversharing reach `security-privacy` through the skills that act on them.

## Failure modes

- The unit of inventory is the file, the effort collapses, and the register is never finished.
- Administrative site owners are recorded as knowledge owners and never asked to accept the role.
- Dependent AI uses are not recorded, so a library is restructured and three agents break silently.
- Only the central team can edit entries, and the register goes stale within months.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Record an owner who has not accepted the role as confirmed.
- Register personal drives or chats as knowledge sources.
- Correct an access mismatch silently in the register instead of raising it as a finding.
- Treat a one-off inventory as finished; it is a living register or it is wrong.

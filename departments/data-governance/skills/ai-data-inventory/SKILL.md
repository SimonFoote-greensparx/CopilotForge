---
name: ai-data-inventory
description: Builds and maintains an inventory of the data assets AI solutions use and create - databases, Dataverse tables, Fabric items, lists, files, connector data and AI-generated records - with owner, purpose, sensitivity, location and the solutions that depend on each. Use when nobody can say which data feeds which agent, before a data source changes or is retired, or when an audit or rights request needs to know where data flows.
license: CC-BY-4.0
metadata:
  department: data-governance
  lifecycle: Discover, Mobilise, Deliver, Scale, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: purview, fabric, power-platform, copilot-studio, ai-foundry, sharepoint, azure
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-privacy, ms-copilot-studio-security-governance, ico-ai-data-protection, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# AI data inventory

## Purpose

AI solutions multiply the paths data takes. An agent reads a Dataverse table, a flow copies records into a list, a
Foundry solution indexes a database, and every conversation creates new records of its own. When nobody keeps track,
the organisation cannot answer basic questions: which agents break if this table changes, where does customer data go
when the agent uses it, and who owns the data behind that answer. This skill builds an inventory of the data assets AI
solutions use and create, linked to their owners and to the solutions that depend on them. It goes wrong when the
inventory is built as a one-off spreadsheet that is out of date by the time it is shared, or when it lists only the
data people remember rather than what the configuration shows.

## When to use

- AI solutions are multiplying and nobody can say which data feeds which agent or flow.
- A data source is about to change structure, move or be retired.
- An audit, data protection rights request or incident needs to know where data flows through AI.
- The organisation is setting up data governance for AI and needs a starting picture.
- A solution is about to be released and its data dependencies are not recorded.

## When not to use

- Inventorying documents, sites and knowledge sources as content - use `knowledge-management:knowledge-inventory`.
- Inventorying the agents, flows and AI solutions themselves - use `platform-governance:ai-solution-inventory`.
- Tracing how a specific output was produced from its sources - use `data-governance:ai-data-lineage`.
- Classifying the data in the inventory - use `data-governance:data-classification-for-ai`.

## Questions to ask first

1. Which AI solutions are in scope - the whole estate, a platform, or one business area?
2. Which data stores do they read, write or copy into, and how do we know - configuration, connector inventories or interviews?
3. Who owns each data asset, and does the owner know AI uses it?
4. What data do the AI solutions themselves create - interaction records, generated content, indexes, memory?
5. Who will keep the inventory current, and from which systems can it be refreshed automatically?

## Required inputs

- The solution inventory from `platform-governance:ai-solution-inventory`, or a list of in-scope solutions.
- Connector, data source and knowledge configuration exports for those solutions.
- Existing data catalogues, records of processing or information asset registers.
- Contacts for data owners in the business areas concerned.

Where an asset has no known owner, record it as unowned and escalate it; never assign an owner without their agreement.
Where configuration cannot be exported, record the solution as "inventory incomplete" rather than relying on memory.

## Decision framework

Decide the inventory depth by the highest risk tier of the solutions that depend on an asset.

| Dependent solutions | Minimum fields per data asset |
|---|---|
| Tier 0-1 only | Name, location, owner, solutions using it |
| Any tier 2 | Add purpose of AI use, sensitivity classification, access route (user-delegated or service identity), read or write |
| Any tier 3-4 | Add personal data categories, lawful basis reference from the record of processing, retention rule, lineage reference, quality expectations |

| Inventory status | Meaning | Action |
|---|---|---|
| Complete | Every in-scope solution's data dependencies recorded from configuration, with owners | Refresh on cycle and on change |
| Partial | Some solutions or fields missing | Prioritise tier 2+ gaps |
| Unowned assets | Assets used by AI without an agreed owner | Escalate to the data governance lead; block new tier 2+ use until owned |

## Practitioner approach

Start from the solutions, not the data estate. Cataloguing every database in the organisation is a multi-year project;
cataloguing the data that AI solutions actually touch is achievable in weeks and is what matters now. Take the solution
inventory and, for each solution, export its configuration: knowledge sources, connectors, actions, flows, tables,
indexes and any custom data stores. Record each data asset once and link it to every solution that uses it.

Include what AI creates as well as what it reads. Interaction records, generated documents, summaries written back to
business systems, search indexes, embeddings and agent memory are data assets with owners, sensitivity and retention
needs. They are often missing from inventories because nobody thinks of them as data until there is an incident.

Find the owner for each asset and tell them. Data owners are frequently unaware that an agent reads their table or that
a flow copies their records elsewhere. That conversation is as valuable as the inventory itself, because it is where
owners raise quality issues, sensitivity concerns and planned changes that would break solutions.

Use the depth table to avoid over-engineering. Low-risk assets need little more than a name, an owner and a list of
dependent solutions. Assets feeding tier 3 and 4 solutions need the full record, including the link to the record of
processing that the DPO maintains.

Automate the refresh where possible. Data catalogue tools such as Microsoft Purview, platform admin exports and the
solution inventory can supply much of the information; confirm which AI sources and data stores current tooling can
scan by checking the source records. Where automation is not available, make updating the inventory a release step:
no tier 2+ solution goes live without its data dependencies recorded.

Finally, use the inventory. Before any change to a data asset, check which AI solutions depend on it. Before a rights
request response, check which solutions may hold the person's data. An inventory nobody consults decays quickly.

## Outputs

- An AI data inventory: data assets, location, owner, sensitivity, purpose of AI use, access route, read or write, dependent solutions, created-by-AI flag and review date, at the depth the decision framework sets.
- A list of unowned or partially recorded assets with escalation owners.
- A dependency view showing which solutions are affected by each asset.

## Microsoft platform considerations

Data used by AI may sit in SharePoint, Dataverse, Fabric, Azure data services or third-party systems reached by
connectors. Microsoft Purview offers data catalogue and data map capabilities, and Power Platform and Copilot Studio
admin tooling can export agent and connector configuration; which sources these cover changes often. Confirm current
capability in the source records before designing an automated refresh.

## Adoption considerations

Not applicable as a primary concern, because end users rarely see the inventory. Makers will see it as part of
release, so keep the fields they must supply few and clear.

## Knowledge considerations

Documents and knowledge sources are inventoried by `knowledge-management:knowledge-inventory`. Link the two inventories
rather than duplicating them, so a solution's full dependency picture can be seen in one place.

## Security and privacy considerations

The inventory itself reveals where sensitive data lives and how it can be reached; restrict access to it. Tier 3 and 4
assets link to the record of processing, which supports `security-privacy:privacy-assessment` and rights requests.

## Responsible AI considerations

Knowing which data feeds a decision is a precondition for explaining it. Where assets feed outputs about people, flag
them for `responsible-ai:ai-impact-assessment`.

## Evaluation requirements

Sample-check the inventory each cycle: pick a few solutions, export their configuration, and compare it with the
inventory. Record the match rate and fix the process where it falls short.

## Value measures

Track the share of tier 2+ solutions with complete data dependencies, the number of unowned assets used by AI, and
changes to data assets that broke a solution without warning. The data governance lead owns these, baselined at the
first inventory.

## Scale notes

### Starter

Record data dependencies for each AI solution on its brief or release checklist, with a simple shared list of assets and
owners.

### Scale

Maintain a central inventory linked to the solution inventory, refreshed at release and on a cycle, with owners
confirmed.

### Enterprise

Integrate the AI data inventory with the enterprise data catalogue, automate scanning where tooling allows, and use it
for change impact analysis across the portfolio.

## Hand-offs

- To `data-governance:data-classification-for-ai` to classify assets.
- To `data-governance:ai-data-lineage` for tier 3 and 4 assets that need lineage.
- To `data-governance:ai-data-access-model` to confirm how each asset may be reached.
- To `platform-governance:ai-solution-inventory` to link assets and solutions.

## Reviewer gates

The inventory supports the `security-privacy` gate rather than passing through one itself: reviewers rely on it from
risk tier 2 to see what data a solution touches. Missing dependencies for a tier 2+ solution are raised by
`security-privacy` as a finding at its gate.

## Failure modes

- The inventory is built once from interviews and is wrong within a quarter.
- AI-created data such as transcripts, indexes and memory is left out, so incidents reveal stores nobody knew about.
- Owners are recorded without being told, so they change data without knowing an agent depends on it.
- The inventory is exhaustive for low-risk data and thin where it matters.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Assign a data owner without their agreement.
- Record data dependencies from memory when configuration can be exported.
- Leave AI-created data out of the inventory.
- Share the inventory more widely than the people who need it.

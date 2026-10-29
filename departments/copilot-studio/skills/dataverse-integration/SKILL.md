---
name: dataverse-integration
description: Designs how a Copilot Studio agent works with Dataverse - tables as knowledge for questions about business records, reads and writes through tools, and the agent's own configuration and conversation data - covering table and column selection, security roles, capacity questions and environment placement. Use when an agent must answer from or update Dataverse records, or when agent data storage needs planning.
license: CC-BY-4.0
metadata:
  department: copilot-studio
  lifecycle: Deliver, Assure
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-studio, power-platform
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, design-authority
  sources: ms-copilot-studio-guidance, ms-copilot-studio-security-governance, ms-managed-environments
  status: draft
  authors: Simon Foote
---

# Dataverse integration

## Purpose

Dataverse sits underneath every Copilot Studio agent: it stores the agent itself and often its conversation records, and
it may hold the business records the agent needs to answer questions or update. This skill designs that relationship
deliberately - which tables the agent may read as knowledge, which it may change through tools, under which security
roles, and how the agent's own data is stored, retained and protected. It usually goes wrong when a whole table is
exposed as knowledge without checking column sensitivity, when an agent writes through a broadly privileged account,
or when nobody realises that transcripts containing personal data are accumulating in the environment.

## When to use

- An agent must answer questions from records held in Dataverse, such as cases, assets, products or requests.
- An agent must create or update Dataverse records on a user's behalf.
- A team needs to understand where the agent's configuration and conversation data are stored and who can see them.
- An agent is moving to an environment whose Dataverse security model differs from development.

## When not to use

- Connecting documents and other non-Dataverse knowledge - use `copilot-studio:studio-knowledge-architecture`.
- Defining the organisation's data access model for AI across systems - use `data-governance:ai-data-access-model`.
- Retention rules for transcripts and interaction data - use `security-privacy:ai-interaction-retention`.
- Licensing and Dataverse capacity questions - use `platform-governance:ai-licensing-and-capacity`.
- Building the flow that performs a multi-step update - use `copilot-studio:power-automate-actions`.

## Questions to ask first

1. Which tables and which columns does the agent genuinely need, and which columns are sensitive?
2. Should the agent read records as the signed-in user, trimmed by their security role, or does the process need broader access?
3. Will the agent create or update records, and which business rules, validations and plug-ins already apply to those tables?
4. Where are the agent's conversation records stored, who can read them and how long are they kept?
5. Is the business data in the same environment as the agent, or in another environment or system?

## Required inputs

- The solution design's knowledge map and action register.
- The Dataverse data model, security roles, business units and any column security already in place, from the table owners.
- The data classification of each table and column.
- Retention requirements from `security-privacy:ai-interaction-retention` or the organisation's records policy.

If column sensitivity is unknown, treat the column as sensitive until its owner confirms otherwise. If the security model
is not documented, do not expose the table to the agent until it is.

## Decision framework

| Need | Pattern | Conditions |
|---|---|---|
| Answer questions across records ("which open cases mention a supplier") | Dataverse tables as knowledge, limited to named tables | Users signed in; security roles trim results; sensitive columns excluded or protected |
| Look up one record precisely ("status of request 1234") | Read tool with typed inputs | Returns only needed columns; runs as the user |
| Create or update a record | Tool or flow that respects existing business rules | User confirms; validation in Dataverse, not only in the conversation |
| Data in another environment or system | Tool or connector to the system of record | Do not copy data into the agent's environment to make it reachable |
| Agent configuration and transcripts | Dataverse in the agent's environment | Access to transcripts restricted; retention agreed |

Prefer precise tools over table knowledge when the question is about one record, and table knowledge over tools when
questions range across many records in natural language.

## Practitioner approach

Start with the questions, then the data. For each representative question that needs business records, name the table,
the columns that answer it and the filter that applies. Most agents need far fewer columns than a table holds. List the
columns explicitly and challenge any that carry personal, financial or commercially sensitive data the questions do not
need.

Check the security model before connecting anything. Dataverse security roles, business units, teams and column
security decide what each user can see. When the agent uses the signed-in user's identity, that model trims answers
automatically, which is the right default. Confirm that the model actually reflects who should see what; agents expose
weaknesses in a security model that the application interface had hidden.

For writes, let Dataverse enforce the rules. Business rules, required columns, validation and plug-ins should protect the
data whether a record is created by a form, an import or an agent. Do not rely on the conversation alone to validate
input. Confirm with the user before every create or update, and write back the record reference so they can check it.

Avoid copying data to make it reachable. If the records live in another environment or another system, call that
system through a tool rather than duplicating data into the agent's environment, which creates a second, unsecured,
unsynchronised copy.

Plan for the agent's own data. Agents and their components are stored in Dataverse, and conversation records may be
stored there too, containing whatever users typed and whatever the agent returned. Agree with the security and records
owners who can read transcripts, how long they are kept and how they are deleted, and restrict access to those tables
to the roles that need it for support and improvement.

Consider capacity and performance early. Large tables as knowledge, frequent writes and retained transcripts all consume
Dataverse resources; route capacity and licensing questions to the platform owner and the licensing guide rather than
estimating them here. Record environment placement and table dependencies in the solution design so ALM carries them
correctly.

## Outputs

- A Dataverse access specification: tables, columns, filters, read or write, identity, security roles and sensitive columns excluded.
- Write rules: validations and business rules relied on, confirmation behaviour and record references returned.
- An agent data note: where configuration and transcripts are stored, who can access them and the agreed retention.
- The Dataverse section of the `studio-solution-design`, and table dependencies for the `alm-and-environment-plan`.

## Microsoft platform considerations

How Dataverse tables are used as knowledge, how results are trimmed, which conversation data is stored and where, and how
capacity is consumed all change over time. Check `ms-copilot-studio-guidance` for current behaviour,
`ms-copilot-studio-security-governance` for data controls, and `ms-managed-environments` for environment-level
governance. Capacity and licence questions go to `platform-governance:ai-licensing-and-capacity`.

## Adoption considerations

Agents that answer accurately from live records can replace reports and searches people rely on; agree with the business
owner which existing routes remain and how users will learn to trust the agent's answers alongside them.

## Knowledge considerations

Dataverse records are structured knowledge with owners. Name the table owner as the knowledge owner, and route data
quality issues - missing values, stale statuses, duplicates - to `data-governance:ai-data-quality` rather than working
around them in instructions.

## Security and privacy considerations

Expose named columns, not whole tables. Use end-user identity so security roles apply. Protect transcripts as personal
data. Never grant the agent's identity a broad role to make answers work. Personal data in tables or transcripts goes
to `security-privacy:privacy-assessment`.

## Responsible AI considerations

When records describe people, such as employees, customers or patients, answers can influence decisions about them.
Limit columns to what the purpose needs, require citations to records, and keep a person responsible for any decision.

## Evaluation requirements

Test answers against known records, trimming with users in different security roles and business units, behaviour on
sensitive columns, write validation with invalid input, and the confirmation on every write. Returning a column the
user cannot see in the application is a zero-tolerance failure.

## Value measures

Track questions answered from records without a hand-off, record updates completed through the agent and data-quality
issues found, owned by the business owner and reported at agent level.

## Scale notes

### Starter

Read-only access to a small number of named tables, signed-in users and end-user identity, with transcript access
restricted to the agent owner and support.

### Scale

Standard access specifications per table reused across agents, column security for sensitive fields and agreed
transcript retention across Studio environments.

### Enterprise

Align agent access with the enterprise data access model, review agent use of sensitive tables periodically, and manage
Dataverse capacity and transcript retention centrally across environments.

## Hand-offs

- To `security-privacy:privacy-assessment` for personal data in tables or transcripts.
- To `copilot-studio:power-automate-actions` or `copilot-studio:studio-actions-and-tools` for write operations.
- To `platform-governance:ai-licensing-and-capacity` for capacity and licence questions.
- To `copilot-studio:studio-alm` with table and solution dependencies.

## Reviewer gates

From risk tier 2, `security-privacy` reviews tables, columns, identity and transcript handling, and `design-authority`
reviews whether table knowledge or tools fit the questions and whether data is being duplicated. Exposure of sensitive
columns beyond the user's own access is a blocking finding.

## Failure modes

- A whole table is connected as knowledge and a sensitive column appears in answers.
- The agent's identity is given a broad security role to "make it work", bypassing business units.
- Records are copied into the agent's environment and drift from the system of record.
- Transcripts containing personal data accumulate with no agreed retention or access control.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Expose a whole table when named columns would answer the questions.
- Grant an agent identity a broad security role to work around the security model.
- Duplicate business data into an agent's environment to make it reachable.
- Estimate Dataverse capacity or licence needs; route them to the licensing guide or a licensing partner.

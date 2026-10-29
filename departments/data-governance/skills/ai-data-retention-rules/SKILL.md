---
name: ai-data-retention-rules
description: Sets the organisation's retention rules for data AI creates or depends on - prompts and responses, transcripts, traces, generated documents, write-backs, indexes and embeddings, agent memory and evaluation sets - aligned to the records schedule, with owners and deletion that reaches every copy. Use when no rule covers AI interactions, when records or legal teams ask how long AI data is kept, or before switching on transcripts or memory at scale.
license: CC-BY-4.0
metadata:
  department: data-governance
  lifecycle: Mobilise, Enable, Deliver, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: purview, m365-copilot, m365-agents, copilot-studio, ai-foundry, power-platform, azure
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-privacy, ms-copilot-studio-security-governance, ico-ai-data-protection, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# AI data retention rules

## Purpose

AI creates new kinds of records faster than records schedules are updated. Prompts and responses, transcripts, traces,
summaries written into case files, indexes, embeddings and agent memory all need a retention rule, yet many
organisations have none, so platform defaults decide by accident. This skill sets retention rules for data AI creates or
depends on, aligned to the existing records schedule, with owners and deletion that reaches every copy. It goes wrong
when one period is applied to everything, so either valuable records are deleted or personal data is kept for years,
and when rules are written without checking what the platforms can actually enforce.

## When to use

- No retention rule covers AI interactions, generated content or AI-specific copies such as indexes.
- Records, legal or compliance colleagues ask how long AI data is kept and who decides.
- Transcripts, tracing or agent memory are about to be switched on at scale.
- A review finds AI data kept indefinitely by default.
- The records schedule is being refreshed and needs AI categories.

## When not to use

- Reviewing whether one solution's storage follows the rules - use `security-privacy:ai-interaction-retention`.
- Deciding whether retaining personal data is lawful for a specific solution - use `security-privacy:privacy-assessment`.
- Tracing where copies of data travel - use `data-governance:ai-data-lineage`.
- Managing knowledge content from creation to archive - use `knowledge-management:knowledge-lifecycle`.

## Questions to ask first

1. What does the current records schedule say, and does it already cover any AI data by record type?
2. Which AI data categories exist or are planned - interactions, transcripts, traces, generated content, write-backs, indexes, memory, evaluation sets?
3. What business, legal, audit and investigation needs require keeping each category, and for how long, according to the records manager and legal adviser?
4. What does data protection require in terms of keeping personal data no longer than necessary, according to the DPO?
5. What can each platform enforce, and how will deletion reach copies?

## Required inputs

- The organisation's records schedule and retention policy.
- The AI data inventory, including AI-created data.
- Advice from the records manager, legal adviser and DPO on periods and holds.
- Current platform retention capabilities from the source records.

Where advice on a period is not yet available, record the category with "[period to confirm]" and a temporary
conservative default agreed by the DPO. Never set a retention period without the records manager and DPO.

## Decision framework

Retain by what the record is, not by the fact that AI produced it.

| AI data category | Usual principle | Typical owner |
|---|---|---|
| Prompts and responses in personal Copilot use | Short, aligned to the organisation's communications retention; long enough for audit and investigation needs | Records manager with DPO |
| Agent transcripts and analytics | As short as quality review needs; full-content transcripts kept less long than aggregate analytics | Solution owner within the rule |
| Traces and retrieval logs | Kept for troubleshooting and, at tier 3+, for explaining outputs while decisions can be challenged | Solution owner and data governance lead |
| Generated content saved as documents or records | Follows the record type it becomes (a letter, a case note, a minute) | Owner of that record type |
| Write-backs to business systems | Follows the system of record | System owner |
| Indexes, embeddings and caches | Never outlive their sources; deletion and correction propagate | Engineering owner |
| Agent memory | Defined expiry; user able to see and clear where the design allows | Solution owner with DPO |
| Evaluation and test sets | Kept while used; personal data minimised or synthetic | Evaluation owner |

Where legal holds apply, they override deletion for the affected records. Every category has a named owner and a
deletion method.

## Practitioner approach

Start with the records manager, not the platform. The organisation already decides how long it keeps letters, case
notes, meeting records and emails. Most AI-generated content becomes one of those record types once it is saved, and
should follow the same rule. Deciding that "AI content" is its own category usually leads to the wrong period.

Then deal with the genuinely new categories: interaction logs, transcripts, traces, indexes, embeddings and memory.
For each, ask what business purpose keeping it serves. Troubleshooting and quality review usually need weeks or months,
not years. Investigation and audit may need longer for some interactions. Explaining tier 3 and 4 outputs needs traces
for as long as a decision can be challenged. Data protection pushes the other way: personal data should not be kept
longer than needed. Bring the records manager, legal adviser and DPO together to agree periods, and record who decided.

Separate full content from metadata. Aggregate analytics and metadata can often be kept longer than the full text of
conversations, which carries most of the sensitivity. Rules that distinguish the two serve both quality and privacy.

Make derived copies follow their sources. An index or embedding store that keeps deleted documents is a retention
failure even if the source library is perfect. The rule should require deletion and correction to propagate, with the
mechanism confirmed through `data-governance:ai-data-lineage`.

Check enforceability. Platforms differ in which AI data they can apply retention to, and capabilities change. Confirm
current coverage in the source records, map each category to the mechanism that will enforce it, and record categories
that need a manual or engineered process.

Publish the rules as an addition to the records schedule, with plain guidance for makers about defaults to choose, and
review them when new AI capabilities arrive, such as memory or new logging.

## Outputs

- AI retention rules added to the records schedule: category, period or "[period to confirm]", trigger, owner, enforcement mechanism, deletion propagation and hold handling.
- A mapping of each category to the platform mechanism or manual process that enforces it.
- Maker guidance on default settings for transcripts, logging and memory.

## Microsoft platform considerations

Retention and deletion for Microsoft 365 Copilot interactions, agent transcripts in Copilot Studio and Dataverse,
Foundry and Azure logs, and Microsoft Purview retention policies each work differently, and coverage of AI interaction
types changes frequently. Confirm current behaviour in `ms-copilot-privacy` and `ms-copilot-studio-security-governance`
before mapping a rule to a mechanism.

## Adoption considerations

Users are more open with AI when they know how long conversations are kept and who can see them. Publish a plain
summary through `responsible-ai:ai-transparency` and onboarding materials.

## Knowledge considerations

Generated content saved into knowledge sources follows the knowledge lifecycle in
`knowledge-management:knowledge-lifecycle`; mark it as AI-generated so reviewers know its origin.

## Security and privacy considerations

Retention is a data protection principle. The DPO agrees periods for categories containing personal data, and
`security-privacy:ai-interaction-retention` checks solutions against the rules at each gate.

## Responsible AI considerations

Traces needed to explain decisions about people must be kept long enough for challenges and appeals, and no longer.
Agree the period with `responsible-ai:escalation-and-appeal`.

## Evaluation requirements

Test enforcement: confirm in a test environment that each mechanism deletes the right data at the right time, including
derived copies, and that holds prevent deletion when applied.

## Value measures

Track the share of AI data categories with an agreed rule and enforcement mechanism, solutions compliant at review, and
deletion tests passed. The records manager and data governance lead own these jointly.

## Scale notes

### Starter

Agree a small number of rules: interactions, transcripts and generated content that follows its record type. Keep
platform defaults only where they match.

### Scale

Add all AI categories to the records schedule, publish maker defaults, and test enforcement for tier 2+ solutions.

### Enterprise

Align rules across jurisdictions with legal advice, automate enforcement where tooling allows, and audit deletion
propagation across the portfolio.

## Hand-offs

- To `security-privacy:ai-interaction-retention`, which checks solutions against the rules.
- To `data-governance:ai-data-lineage` for deletion propagation.
- To the records manager to incorporate rules into the records schedule.
- To platform administrators to configure enforcement.

## Reviewer gates

Rules covering personal data need DPO approval and are applied by the `security-privacy` gate from risk tier 2. Below
tier 2 they apply as default settings without a formal gate.

## Failure modes

- One period is applied to all AI data, deleting needed records or keeping personal data for years.
- Platform defaults decide retention because no rule was ever set.
- Source documents are deleted but their content survives in indexes and embeddings.
- Rules are written for capabilities the platform cannot enforce.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Set a retention period without the records manager and DPO.
- Treat "AI-generated" as a record type that overrides what the record actually is.
- Allow derived copies to outlive their sources.
- Delete records subject to a legal hold.

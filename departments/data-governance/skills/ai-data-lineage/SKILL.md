---
name: ai-data-lineage
description: Traces how data travels from systems of record into AI outputs - copies, indexes, embeddings, prompts, tool calls and generated records - so the organisation can say where an answer came from, which solutions a source change affects, and where personal data has spread. Use when a tier 3 or 4 solution needs explainable provenance, when a source changes or is withdrawn, or when a rights request or incident needs the full path.
license: CC-BY-4.0
metadata:
  department: data-governance
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 2, 3, 4
  platforms: purview, fabric, ai-foundry, copilot-studio, power-platform, azure
  edition-support: scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-privacy, ms-foundry-models, ico-ai-data-protection, nist-ai-rmf, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# AI data lineage

## Purpose

When someone asks where an AI answer came from, "the model" is not an answer. Data reaches AI outputs through a chain
of copies and transformations: extracted from a system of record, loaded into a lakehouse, chunked into a search index,
embedded, retrieved, placed in a prompt, combined with a tool result, and written back as a new record. This skill
traces that chain for a solution, at the depth its risk tier needs, so the organisation can explain outputs, assess the
impact of source changes, and find personal data wherever it has spread. It goes wrong when lineage stops at the
system of record and ignores the AI-specific copies, which are exactly where stale and deleted data lingers.

## When to use

- A tier 3 or 4 solution must be able to explain the provenance of its outputs.
- A source system is changing, being corrected or being withdrawn, and dependent AI copies must follow.
- A data protection rights request or erasure needs to reach every copy, including indexes and embeddings.
- An incident requires knowing what data an output could have drawn on.
- A custom retrieval or Foundry solution is being designed and its data path needs recording.

## When not to use

- Listing which data assets AI solutions use - use `data-governance:ai-data-inventory`.
- Testing whether answers are grounded in and cite their sources - use `evaluation-quality:groundedness-testing`.
- Designing telemetry and tracing in code - use `ai-engineering:ai-telemetry`.
- Designing retrieval, chunking and indexing - use `ai-foundry:retrieval-design`.

## Questions to ask first

1. Which outputs must be explainable, to whom, and at what level - source system, document, record or field?
2. What copies and transformations sit between the system of record and the AI output?
3. How often is each copy refreshed, and what happens to it when the source record is corrected or deleted?
4. Which outputs are written back into systems, becoming sources for other solutions?
5. What lineage can tooling capture automatically, and what must be documented by hand?

## Required inputs

- The AI data inventory entries for the solution.
- The solution architecture, including pipelines, indexes, vector stores, caches and write-backs.
- Refresh schedules and deletion behaviour for each copy, from the engineering or platform team.
- The risk tier and any explainability requirement from `responsible-ai:ai-impact-assessment`.

Where deletion behaviour of a copy is unknown, record it as a gap and test it; never assume a deleted source record
disappears from an index or embedding store.

## Decision framework

| Risk tier | Minimum lineage |
|---|---|
| 2 | Source systems and the main copies or indexes, with refresh frequency |
| 3 | Add transformations, deletion propagation, write-backs, and the ability to show which sources an output drew on |
| 4 | Add record-level traceability for outputs that inform decisions about individuals, retained for as long as those decisions can be questioned |

| Gap | Severity | Action |
|---|---|---|
| Deleted or corrected source data persists in AI copies | High for personal data | Design deletion propagation; test it |
| Outputs cannot be traced to sources at tier 3+ | High | Capture citations or retrieval traces; retain them per the retention rule |
| Write-backs not recorded | Medium | Add to lineage; mark AI-generated records |
| Lineage held only in one engineer's head | Medium | Document and, where possible, automate |

## Practitioner approach

Draw the path for one realistic output before reaching for tools. Take a typical question and answer, and walk
backwards: which passages or records were retrieved, from which index, built from which copy, extracted from which
system, on what schedule. Then walk forwards: where did the output go, was it written to a record, a document or a
message, and does anything else read it? The drawing reveals copies nobody mentioned.

Pay particular attention to AI-specific copies. Search indexes, vector stores, caches, evaluation datasets, exported
transcripts and agent memory all hold derived data. Each needs a refresh pattern and a deletion pattern. Ask the
engineering team what happens when a source record is corrected: is the index rebuilt, updated incrementally, or left
until the next full load? Then test it. Erasure requests and corrections that never reach embeddings are a common gap.

Decide the depth by tier. Most tier 2 solutions need only source systems and main copies documented. Tier 3 and 4
solutions that inform decisions need to show, for a given output, what it drew on; that usually means keeping
retrieval traces or citations alongside the interaction record, under the retention rule from
`data-governance:ai-data-retention-rules`. Agree with the business owner and DPO how long those traces must be kept to
support challenges and appeals.

Record write-backs. Outputs saved into systems become data that other solutions and people trust. Mark them as
AI-generated, record which solution created them, and include them in the lineage so a later reader knows their origin.

Automate where tooling allows. Data catalogue and lineage features in Microsoft Purview and Fabric can capture parts of
the path, and tracing in Foundry solutions can record retrieval; coverage of AI-specific steps varies, so confirm
current capability in the source records and document the remainder by hand. Keep the lineage with the solution's
documentation and update it at every change to sources, indexes or write-backs.

## Outputs

- A lineage diagram and record for the solution: sources, copies, transformations, indexes and stores, refresh and deletion behaviour, outputs and write-backs, at the depth the tier sets.
- A deletion propagation test result for each copy holding personal data.
- Gaps with owners and dates, and the retention needed for retrieval traces.

## Microsoft platform considerations

Lineage capabilities in Microsoft Purview and Fabric, tracing in Foundry, and how Copilot and Copilot Studio record
citations and retrieved content differ and change frequently. Confirm current behaviour in `ms-copilot-privacy` and
`ms-foundry-models` and the platform's documentation before deciding what to automate.

## Adoption considerations

Not applicable as a primary concern, because users do not see lineage directly. Where outputs show their sources,
lineage makes those citations trustworthy.

## Knowledge considerations

Documents feeding AI follow the same logic: an index of a library is a copy with its own refresh and deletion
behaviour. Coordinate with knowledge owners so withdrawn documents leave the index too.

## Security and privacy considerations

Every AI copy of personal data is in scope for rights requests and retention. Share lineage for tier 3 and 4 solutions
with `security-privacy:privacy-assessment`, and restrict access to lineage records that reveal sensitive data locations.

## Responsible AI considerations

People can only challenge an AI-influenced outcome if the organisation can say what it drew on. Lineage underpins
`responsible-ai:escalation-and-appeal` for tier 3 and 4 uses.

## Evaluation requirements

Test lineage, not just document it: correct and delete test records at source and confirm the changes reach every copy
within the expected time, and trace a sample of outputs back to their sources.

## Value measures

Track the share of tier 3+ solutions with tested lineage, time for corrections and deletions to propagate, and rights
requests completed across all AI copies. The data governance lead owns these, baselined at first test.

## Scale notes

### Starter

Not usually needed; starter programmes should avoid tier 3 and 4 uses. Where tier 2 solutions copy data, record the
copy and how it is refreshed.

### Scale

Document lineage for tier 3 solutions at design, test deletion propagation before release, and keep diagrams with
solution documentation.

### Enterprise

Integrate AI lineage with enterprise lineage tooling, automate capture where possible, and audit deletion propagation
across the portfolio.

## Hand-offs

- To `security-privacy:privacy-assessment` with personal data copies and deletion behaviour.
- To `data-governance:ai-data-retention-rules` for retention of retrieval traces.
- To `responsible-ai:escalation-and-appeal` with what can be shown to people who question an outcome.
- To `ai-engineering:ai-telemetry` for trace capture requirements.

## Reviewer gates

From risk tier 3, `security-privacy` checks that personal data copies and deletion propagation are recorded and tested;
`responsible-ai` relies on lineage where outputs inform decisions about people.

## Failure modes

- Lineage stops at the system of record, so stale and deleted data survives in indexes and embeddings.
- Erasure requests are completed in the source system and nowhere else.
- AI-generated write-backs are trusted as original records with no marker of their origin.
- Lineage exists as a diagram that was accurate at launch and never updated.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Assume deleted or corrected source data disappears from AI copies without testing.
- Treat "the model generated it" as provenance.
- Leave AI-generated write-backs unmarked.
- Keep retrieval traces longer than the agreed retention rule.

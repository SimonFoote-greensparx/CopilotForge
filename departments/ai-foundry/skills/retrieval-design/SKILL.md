---
name: retrieval-design
description: Designs the retrieval layer of a custom Microsoft Foundry solution - which content is indexed, how it is cleaned and chunked, which metadata and embeddings are kept, keyword, vector or hybrid search with reranking, permission trimming, freshness and how passages reach the prompt with citations. Use when a Foundry solution needs its own search index, when answers miss content that exists, or when retrieval returns content users should not see.
license: CC-BY-4.0
metadata:
  department: ai-foundry
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, sharepoint, entra
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, evaluation-quality, design-authority
  sources: ms-foundry-models, ms-copilot-privacy, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# Retrieval design

## Purpose

When a Foundry solution answers from organisational content, most of its quality is decided before the model sees
anything: by what was indexed, how it was split, how the search ranks it and whether the user is allowed to see it.
This skill designs that retrieval layer so the right passages, and only permitted passages, reach the model with enough
context to cite them. Retrieval goes wrong when whole document stores are indexed without cleaning, when chunks are cut
by character count through the middle of tables and rules, and when the index loses the source permissions so the
solution answers with content the user could never open.

## When to use

- `ai-foundry:foundry-grounding-strategy` has decided the solution needs its own retrieval index.
- Answers miss content that exists, cite the wrong document, or quote superseded versions.
- Retrieval returns passages from documents the user is not permitted to see.
- A prototype index built from a folder of files needs a production design with refresh and ownership.
- A new content type, such as tables, scanned forms or long technical manuals, is being added to an index.

## When not to use

- Choosing whether to build custom retrieval at all versus other grounding approaches - use `ai-foundry:foundry-grounding-strategy`.
- Choosing grounding patterns across the estate and avoiding duplicate indexes - use `ai-architecture:grounding-patterns`.
- Connecting knowledge to a Copilot Studio agent - use `copilot-studio:studio-knowledge-architecture`.
- Improving how authors write and structure source documents - use `knowledge-management:ai-ready-content`.
- Testing at the gate whether answers are supported by their citations - that is the reviewer skill `evaluation-quality:groundedness-testing`.

## Questions to ask first

1. Which questions must the solution answer, and which sources hold the authoritative answers, owned by whom?
2. Who may see each source, and must retrieval respect each user's permissions or is the content open to every user of the solution?
3. How quickly must changes in the source appear in answers, and how are deletions and superseded versions handled?
4. What shape is the content, short pages, long manuals, tables, scanned images, records, and does structure carry meaning?
5. How will retrieval quality be measured separately from answer quality?

## Required inputs

- The grounding decision and source list from `ai-foundry:foundry-grounding-strategy`, with owners.
- A readiness view of each source, such as a verdict from `knowledge-management:knowledge-readiness-assessment` or the knowledge owner's assessment.
- The classification and permission model for each source.
- A set of real questions with the documents and passages that should answer them.

Where a source has no owner, an unknown permission model or no readiness view, mark it `[To confirm: ...]` and leave
it out of the index. Indexing content nobody owns turns a knowledge problem into a security problem.

## Decision framework

| Decision | Default | Change when |
|---|---|---|
| What to index | Only sources named in the grounding decision, authoritative versions only | Never index whole stores speculatively |
| Chunking | Structure-aware splitting by headings, sections and table boundaries, with title and section path carried into each chunk | Content is short and uniform, where simple fixed-size chunks with overlap are enough |
| Search method | Hybrid keyword and vector search with semantic reranking where available | Exact identifiers dominate (keyword weighted) or the corpus is tiny (simpler search suffices) |
| Metadata | Source, owner, version, effective date, classification, audience and permission identifiers on every chunk | Never drop permission metadata |
| Permissions | Trimmed per user at query time from source permissions | All content is genuinely open to every user of the solution, confirmed by the owner |
| Freshness | Incremental refresh on change, with deletions propagated | The source changes rarely and a scheduled rebuild is acceptable to the owner |
| Passages to the model | A small number of top-ranked chunks with citations and an instruction for silence or conflict | Evaluation shows more context improves answers without raising cost or confusion |

## Practitioner approach

Start from questions, not documents. Collect real questions with the passages that should answer them, from the
business and knowledge owners. These become the retrieval test set and keep the design honest: every choice about
chunking, metadata and ranking is judged by whether the right passage comes back near the top.

Index less than you think. Include only the authoritative version of each document, exclude drafts, duplicates and
archive copies, and agree the list with the knowledge owners. Clean before indexing: strip navigation and boilerplate,
extract text from scanned content with checks on quality, and keep tables as tables rather than flattened text. Poor
content is fixed at source with `knowledge-management:content-quality`, not compensated for by cleverer search.

Chunk by structure. Split on headings, sections and table boundaries so each chunk carries one idea with its context,
and prepend the document title and section path so a chunk makes sense alone. Keep rules with their exceptions and
tables with their headers. Fixed-size chunks with overlap are acceptable for short, uniform text, but they break
policies and manuals in damaging ways. Test two or three chunking options against the question set rather than arguing
about them.

Choose the search method on evidence. Hybrid search, combining keyword matching for exact terms and codes with vector
similarity for meaning, followed by reranking, is a sound default. Use metadata filters for audience, effective date and
document type so superseded or irrelevant content never competes. Choose the embedding model with the same care as the
generation model, and plan for re-indexing if it changes.

Preserve permissions end to end. Carry access identifiers from the source into every chunk and filter at query time
using the signed-in user's identity, designed with `ai-architecture:ai-identity-design`. Test with users who have
different access. An index that serves everyone the same results is acceptable only when the owner confirms the content
is open to every user.

Design freshness and deletion. Decide how changes, new versions and deletions flow into the index and how quickly, and
monitor that refresh runs. A deleted or withdrawn document that remains retrievable is a common and serious failure.

Pass a small number of well-ranked passages to the model, each with source and version for citation, and instruct the
model what to do when they are silent or conflict. Measure retrieval separately from answers: whether the right passage
is retrieved and how high it ranks. Record the design in the retrieval section of the `foundry-solution-design`
template, and say what retrieval cannot fix, such as gaps in the content itself.

## Outputs

- The retrieval section of the `foundry-solution-design` template: sources and owners, cleaning rules, chunking design, metadata schema, search and ranking configuration, permission trimming, refresh and deletion, and passages passed to the model.
- A retrieval test set of questions with expected passages, and baseline retrieval measures.
- A refresh and monitoring specification handed to `ai-foundry:foundry-observability`.

## Microsoft platform considerations

Foundry solutions commonly use Azure AI Search or other Azure data services for indexing, and Foundry can connect agents
to indexes and other knowledge sources; search features, document extraction options, permission trimming support and
integration with Microsoft 365 content change frequently. Check the current source records before relying on a feature,
such as security trimming for a particular source type, and consider whether Microsoft 365 or Copilot grounding already
covers the content without copying it into a new index.

## Adoption considerations

Users judge the whole solution by whether it finds what they know exists. Show citations they can open, and give a
simple way to report a missing or wrong source so the retrieval test set grows from real use.

## Knowledge considerations

Retrieval depends on content owners. Each indexed source needs an owner, a review cycle and an agreed route for
withdrawing content, aligned with `knowledge-management:knowledge-grounding-standards`. Retrieval failures that reveal
missing content go to `knowledge-management:knowledge-gap-analysis`.

## Security and privacy considerations

An index is a copy of organisational content in a new store. Apply the source classification, keep permission trimming
end to end, restrict who can query the index directly, and propagate deletions, including for personal data subject to
erasure. `security-privacy:data-exposure-review` reviews the design from tier 2, and data protection questions go to the
DPO.

## Responsible AI considerations

Where answers inform decisions about people, retrieval must favour authoritative, current sources and make citations
visible so people can check them. Gaps in coverage for some groups or languages should be identified and disclosed.

## Evaluation requirements

Measure retrieval separately from answers: whether the expected passage is retrieved, how high it ranks and whether
forbidden passages are ever returned for users without access. Re-run after any change to chunking, embeddings, ranking
or sources, with thresholds agreed before results.

## Value measures

Track retrieval hit rate on the test set, the share of answers with correct citations and reports of missing or wrong
sources, owned by the solution owner with knowledge owners. Falling hit rates usually signal content change.

## Scale notes

### Starter

Index a small set of clean, owned sources with structure-aware chunking and hybrid search, and test with a few dozen
real questions before launch.

### Scale

Reuse standard chunking, metadata and permission patterns across solutions, and share indexes for the same content
rather than building duplicates.

### Enterprise

Treat major indexes as governed data products with owners, refresh monitoring and access controls, registered so
solutions reuse them, and review new indexes for duplication with `ai-architecture:grounding-patterns`.

## Hand-offs

- To `evaluation-quality:groundedness-testing` for the gate review of grounded answers.
- To `ai-foundry:foundry-prompt-engineering` for how passages and citations are presented to the model.
- To `ai-foundry:model-evaluation` when retrieval settings or embedding models are compared.
- To `knowledge-management:content-quality` when retrieval fails because content is poor.
- To `ai-foundry:foundry-observability` to monitor refresh and retrieval quality.

## Reviewer gates

From risk tier 2, `security-privacy` reviews permission trimming, deletion and index access, `evaluation-quality` checks
retrieval and groundedness evidence, and `design-authority` checks the index does not duplicate an existing one without
reason. Retrieval returning content to users without access is a blocking finding at any tier.

## Failure modes

- A whole document store is indexed, and answers quote drafts, duplicates and superseded policies.
- Fixed-size chunks split rules from their exceptions, and the solution states the rule without the exception.
- Permission metadata is dropped during indexing, and users receive passages from documents they cannot open.
- A withdrawn document stays in the index because deletions are not propagated, and answers rely on it for months.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Index content that has no owner, no classification or an unknown permission model.
- Drop source permissions from an index that serves users with different access.
- Leave deletions and withdrawn versions retrievable after the source has removed them.
- Judge retrieval only by final answers without measuring whether the right passages were retrieved.

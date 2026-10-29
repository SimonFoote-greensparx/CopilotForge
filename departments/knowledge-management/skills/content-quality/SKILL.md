---
name: content-quality
description: Sets the quality standard for knowledge content that Copilot and agents will draw on - accuracy, currency, authority, completeness, clarity, consistency and metadata - and runs sampled quality checks on collections to produce a quality rating and a remediation list for owners. Use when answers are wrong because the content is, when a collection needs a quality baseline, or when owners ask what good looks like.
license: CC-BY-4.0
metadata:
  department: knowledge-management
  lifecycle: Enable, Deliver, Assure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: sharepoint, m365-copilot, m365-agents, copilot-studio
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality
  sources: ms-copilot-overview, ms-agent-builder, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# Content quality

## Purpose

AI does not improve weak content; it repeats it fluently and at scale. This skill defines what good knowledge content
looks like for the organisation, measured in terms that affect AI answers, and checks collections against that standard
by sampling, so owners know what to fix first. It goes wrong when quality is judged by how polished pages look, when
the standard is so long that nobody applies it, or when checks are run once and never repeated.

## When to use

- Copilot or agent answers are wrong, incomplete or contradictory and the cause is the content, not the configuration.
- A collection is a candidate for grounding and needs a quality baseline before decisions are made.
- Owners ask what "good enough for AI" means for their content.
- A periodic quality check of important collections is due.

## When not to use

- The minimum bar a source must clear before an agent may ground on it - use `knowledge-management:knowledge-grounding-standards`.
- Guidance for authors on writing and structuring individual documents - use `knowledge-management:ai-ready-content`.
- Quality of structured data used by AI solutions - use `data-governance:ai-data-quality`.
- Testing whether an agent's answers are correct - use `m365-agents:agent-testing`.
- Removing redundant, outdated and trivial content in bulk - use `knowledge-management:knowledge-cleanup`.

## Questions to ask first

1. Which collections are in scope, and which Copilot scenarios or agents depend on them?
2. What does a wrong answer from this content cost - an annoyed user, a rework loop, or a compliance or safety failure?
3. Is there already an editorial or document control standard, and how well is it followed?
4. What representative questions should this content be able to answer?
5. Who will fix what the check finds, and how much time do they have?

## Required inputs

- The collections in scope, with owners, from `knowledge-management:knowledge-inventory`.
- Representative questions for each collection, from users or the agent brief.
- Any existing editorial, style or document control standards.
- Access to the content and its version history.

If no representative questions exist, gather ten from the people who use the content before checking; quality judged
without questions drifts into style review. Where the owner is unknown, check the content but record the result as
unowned and route ownership to `knowledge-management:knowledge-owner-model`.

## Decision framework

Check samples against seven quality dimensions. Each is pass, minor issue or major issue.

| Dimension | Major issue looks like |
|---|---|
| Accuracy | Content states something the owner confirms is wrong |
| Currency | Superseded rules, dead references, no review date, or a date older than the agreed cycle |
| Authority | The same topic answered differently in two places, or drafts presented as approved |
| Completeness | Representative questions cannot be answered, or exceptions are missing |
| Clarity | Key rules hidden in images, scanned text, ambiguous wording or unexplained acronyms |
| Consistency | Different terms for the same thing across the collection, conflicting numbers |
| Metadata | No owner, status, effective date or audience recorded |

Rate the collection: **good** (no major issues in the sample, minor issues under a fifth of items), **fair** (major
issues only in clarity, consistency or metadata), **poor** (any major issue in accuracy, currency or authority). The
rating thresholds are a starting point; tighten them for content that informs decisions about people, money or safety.

## Practitioner approach

Write the standard first, and keep it to a page. Each dimension needs a one-line definition, a test a reviewer can
apply in a minute, and an example of a pass and a fail drawn from the organisation's own content. A standard written in
the abstract gets nodded through; one illustrated with familiar documents changes behaviour.

Sample rather than inspect everything. For a collection, take the documents most often opened or cited, plus a random
handful, plus any that answer the representative questions. Twenty to forty items is usually enough to rate a
collection and find its patterns. Answer each representative question by hand from the collection and note where you
found conflicting, missing or buried answers; these are the failures AI will reproduce.

Run the check with the owner, not on them. Sit with the content owner for part of the sample, because they can confirm
accuracy in seconds where a reviewer would need hours. Record each issue against its dimension, item and severity, then
group issues into patterns: "policy pages carry no effective date", "procedures exist in both Word and page form with
different steps". Patterns are what owners can fix systematically.

Prioritise remediation by consequence. Accuracy, currency and authority issues in content that AI already uses come
first, because they produce confident wrong answers. Clarity and metadata issues come next, often fixed through
`knowledge-management:ai-ready-content` guidance and better library design. Do not let a perfect standard block use:
a collection rated fair can usually be grounded with conditions, a poor one cannot.

Feed results back into the system. Record the rating and date in the knowledge register, give the owner a short list of
fixes with a target date, and schedule the next check through `knowledge-management:knowledge-review-cycles`. Where the
same patterns appear across many collections, the fix is upstream: templates, library design or the lifecycle, not
more checking.

## Outputs

- A one-page content quality standard with dimensions, tests and organisation-specific examples.
- A quality check record per collection: sample, issues by dimension and severity, patterns and rating, recorded in the `knowledge-asset-register`.
- A remediation list for each owner, prioritised by consequence, with target dates.

## Microsoft platform considerations

SharePoint columns and content types can hold owner, status, effective date and audience so metadata quality can be
checked at scale, and version history shows whether content is maintained. How Copilot and agents use metadata, page
structure or file types when grounding varies by route and changes over time; confirm current behaviour in the source
records rather than tuning content to remembered behaviour.

## Adoption considerations

Users lose trust in AI quickly when it repeats wrong content, and they rarely distinguish a content fault from an AI
fault. Explaining that answers improved because owners fixed their content builds trust in both.

## Knowledge considerations

This skill sets and checks the standard; `knowledge-management:knowledge-grounding-standards` uses the ratings as part
of its entry criteria, and `knowledge-management:ai-ready-content` teaches authors to meet the standard first time.

## Security and privacy considerations

Quality checks open content, so reviewers need appropriate access and must not copy sensitive items into working notes.
Content found with sensitivity or audience problems goes to `knowledge-management:knowledge-classification`.

## Responsible AI considerations

Include a check for content that reflects outdated, biased or exclusionary practice, and treat it as an accuracy issue.
AI will present such content as current organisational guidance.

## Evaluation requirements

Keep each sample and its findings so the next check is comparable. Pass the representative questions and the conflicts
found to `m365-agents:agent-testing` or `evaluation-quality:groundedness-testing` as test cases for dependent agents.

## Value measures

Baseline the share of AI-dependent collections rated good, the number of major issues per sample, and the count of
wrong-answer reports traced to content. The Knowledge Manager owns these, reported by collection and domain, never by
author.

## Scale notes

### Starter

Check the two or three collections the first agents use, with their owners, against a short standard.

### Scale

Check every AI-dependent collection on a cycle, record ratings in the register, and publish the standard with examples
to all owners.

### Enterprise

Train business-unit stewards to run checks against the shared standard, moderate a sample centrally, and report quality
by domain to steering.

## Hand-offs

- To content owners with the remediation list, and to `knowledge-management:knowledge-review-cycles` for the next check.
- To `knowledge-management:ai-ready-content` where patterns show authors need guidance.
- To `knowledge-management:knowledge-grounding-standards` with ratings for entry decisions.

## Reviewer gates

From risk tier 2, `evaluation-quality` may challenge whether the quality evidence behind a grounded agent is
sufficient, particularly for accuracy and authority. Below tier 2 the content owner accepts the rating.

## Failure modes

- Quality is judged on presentation, and polished but outdated pages pass.
- The standard runs to many pages and nobody applies it.
- Checks are done without the owner, so accuracy is guessed rather than confirmed.
- Issues are listed item by item and the systemic pattern behind them is never fixed.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Rate a collection's accuracy without the owner or a subject matter reviewer confirming it.
- Score or rank individual authors; ratings belong to collections.
- Block all AI use until every collection is rated good.
- Tune content to remembered AI behaviour instead of the current source records.

---
name: ai-data-quality
description: Sets data quality requirements for structured and operational data used by AI - accuracy, completeness, currency, consistency, uniqueness and meaning - with thresholds by use and risk tier, ways to measure them, owners and remediation, so agents and analytics do not confidently repeat bad data. Use when an agent reads business records, when Copilot analyses tables or semantic models, or when AI answers trace back to wrong data.
license: CC-BY-4.0
metadata:
  department: data-governance
  lifecycle: Envision, Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: fabric, power-platform, copilot-studio, ai-foundry, m365-copilot, azure
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality
  sources: nist-ai-rmf, iso-iec-42001, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# AI data quality

## Purpose

AI makes data quality problems louder. A report with a duplicated customer is an annoyance; an agent that confidently
tells a customer the wrong balance because it found the duplicate first is an incident. This skill sets data quality
requirements for the structured and operational data AI uses, proportionate to the use and risk tier, with ways to
measure them, owners and a remediation route. It goes wrong when quality is judged by whether the data looks fine in a
demo, or when requirements are set so high that no real dataset could pass.

## When to use

- An agent or flow reads business records from Dataverse, a database, a list or a business system.
- Copilot or a data agent will analyse tables, spreadsheets or semantic models for decisions.
- AI answers have been traced back to wrong, missing or out-of-date data.
- A data product is being prepared for AI consumption and needs quality expectations.
- Data will be used to build evaluation sets or to tune a model.

## When not to use

- Content quality standards for documents and knowledge - use `knowledge-management:content-quality`.
- Building evaluation sets of questions and expected answers - use `evaluation-quality:golden-dataset`.
- Judging whether a whole data product is ready for AI - use `data-governance:data-product-readiness`.
- Bias and unfairness arising from data - use `responsible-ai:fairness-review`.

## Questions to ask first

1. What will AI do with the data - answer questions, summarise, analyse, act, or tune a model?
2. What happens if a value is wrong, missing or stale - who is affected and how badly?
3. Which fields actually matter to the AI use, and which are irrelevant?
4. What is known about the data's current quality, and how was it measured?
5. Who owns fixing it, at source, when it falls short?

## Required inputs

- The AI use description and risk tier.
- The data assets involved, from `data-governance:ai-data-inventory`.
- Any existing quality measures, profiling results or known issues.
- The data owner's availability to agree requirements and fixes.

Where current quality is unknown, profile a sample before setting requirements. Never certify data as fit for AI
without measurement, and never set a threshold the owner has not agreed.

## Decision framework

Set requirements per critical field, by quality dimension and the consequence of error.

| Dimension | Question | Tier 1 expectation | Tier 2 expectation | Tier 3-4 expectation |
|---|---|---|---|---|
| Accuracy | Does the value match reality? | Known issues documented | Sample-checked against source of truth | Measured regularly with agreed threshold |
| Completeness | Are critical fields populated? | Gaps documented | Threshold agreed for critical fields | Threshold monitored; AI handles gaps explicitly |
| Currency | How old can data be for this use? | Refresh pattern documented | Maximum age agreed and shown to users | Maximum age enforced; stale data withheld or flagged |
| Consistency | Do values agree across systems and records? | Conflicts documented | Source of truth named for each field | Reconciliation in place |
| Uniqueness | Are entities duplicated? | Known duplicates documented | Duplicate rate measured | Duplicate handling defined before AI use |
| Meaning | Are fields described so AI and people interpret them correctly? | Key fields described | All fields used by AI described, with units and codes | Described and reviewed with business owner |

| Result | Verdict | Action |
|---|---|---|
| Meets the tier's expectations on all critical fields | Fit for this use | Monitor at agreed frequency |
| Gaps on non-critical fields, or mitigated in design | Fit with conditions | Record conditions; fix on a plan |
| Critical field below expectation with no mitigation | Not fit | Fix at source or narrow the use |

## Practitioner approach

Start from the use, not the dataset. A field that is irrelevant to the AI use does not need to be perfect, and trying to
fix all data before any AI use is how programmes stall. Ask the business owner what the AI will do with the data and
which fields drive its answers or actions. Those are the critical fields; everything else is noted and left.

Profile before you judge. Take a sample and measure: how many critical fields are empty, how old the latest updates
are, how many records look like duplicates, how many values fall outside expected ranges. Profiling tools in the data
platform help, but a careful look at a few hundred records with the owner often reveals more than a dashboard. Record
the results as the baseline.

Pay special attention to meaning. Language models interpret fields by their names and descriptions. A column called
"status" with codes 1 to 7, or "amount" without currency, invites confident misreading. Clear descriptions, units,
code meanings and synonyms are a quality dimension for AI in their own right, and they are cheap to fix.

Agree requirements with the owner using the tier table. For tier 2 and above, write thresholds for critical fields and
how they will be measured. Where data cannot meet them in time, decide how the design will compensate: show data age to
users, withhold stale records, require a person to confirm before acting, or narrow the use to fields that are reliable.

Fix at source. Correcting data inside an AI solution, through instructions or a cleaned copy, hides the problem and
creates a second version of the truth. Route fixes to the owner and the system of record, and track them.

Monitor after release. Quality drifts, especially when upstream processes change. Agree what is measured, how often,
and who is told when a threshold is breached. Feed AI failures that trace back to data into the same route.

## Outputs

- Data quality requirements for the AI use: critical fields, dimensions, thresholds by tier, measurement method and frequency, owner.
- A baseline quality profile and a verdict (fit, fit with conditions, not fit) with conditions recorded.
- A remediation plan for gaps, owned by the data owner, with dates.
- Field descriptions and code meanings improved where meaning was the gap.

## Microsoft platform considerations

Data used by AI may live in Dataverse, Fabric, Azure data services or business systems reached through connectors, each
with its own profiling and monitoring options. Microsoft Purview and Fabric offer data quality capabilities whose scope
changes; confirm current features in the relevant source records before designing measurement around them.

## Adoption considerations

Users lose trust quickly when AI repeats data they know is wrong. Showing data age and source in answers, and giving
users a route to report bad data, turns them into part of the quality loop.

## Knowledge considerations

Documents and knowledge content have their own quality standards in `knowledge-management:content-quality`. Where a
solution uses both, agree which source wins when they conflict.

## Security and privacy considerations

Accuracy of personal data is a data protection principle, not only a quality preference. Where AI uses personal data,
inaccurate records are also a privacy finding; route them to `security-privacy:privacy-assessment`.

## Responsible AI considerations

Missing or inaccurate data is often uneven across groups, and AI can amplify that. Pass patterns of uneven quality to
`responsible-ai:fairness-review`.

## Evaluation requirements

Evaluation sets should include cases built on known data problems, such as duplicates, missing values and stale
records, so the solution's handling of bad data is tested. Agree these with the `evaluation-quality` reviewers.

## Value measures

Track quality of critical fields against thresholds, AI failures traced to data, and time to fix at source. The data
owner owns field-level measures; the data governance lead owns the portfolio view, baselined at first profiling.

## Scale notes

### Starter

Profile the critical fields for each AI use with the owner, document known issues, and design around them. Avoid tier 3
uses on data that has never been measured.

### Scale

Use a standard requirements template by tier, automate profiling for data feeding tier 2+ solutions, and review quality
in the operations cadence.

### Enterprise

Integrate AI quality requirements into enterprise data quality management and data contracts, and monitor critical
fields continuously for tier 3 and 4 uses.

## Hand-offs

- To the data owner with the remediation plan.
- To `data-governance:data-product-readiness` with the quality verdict.
- To `evaluation-quality:golden-dataset` with bad-data test cases.
- To `ai-operations:ai-solution-monitoring` with thresholds to monitor.

## Reviewer gates

From risk tier 2, `evaluation-quality` checks that quality requirements exist for critical fields and that evaluation
covers bad-data cases. Below tier 2 this is advisory guidance for the owner.

## Failure modes

- All data must be perfect before any AI use, so nothing ships.
- Data looks fine in a demo, and duplicates or stale records surface with real users.
- Fixes are made in a cleaned copy for the agent, creating a second version of the truth.
- Field meaning is ignored, so the model misreads codes and units with confidence.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Certify data as fit for AI without measuring it.
- Fix data inside the AI solution instead of at source.
- Set quality thresholds without the data owner's agreement.
- Treat field descriptions and code meanings as optional for AI use.

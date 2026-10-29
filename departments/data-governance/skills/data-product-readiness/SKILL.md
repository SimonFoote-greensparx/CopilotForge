---
name: data-product-readiness
description: Assesses whether a data product - a curated, owned dataset, table set or semantic model - is ready for AI to consume, checking ownership, descriptions and business meaning, quality, classification, access, lineage, refresh and change commitments, and records a ready, ready-with-conditions or not-ready verdict. Use when an agent, Copilot analysis or Foundry solution will read structured business data, or when a data team must make data AI-ready.
license: CC-BY-4.0
metadata:
  department: data-governance
  lifecycle: Envision, Deliver, Assure
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: fabric, power-platform, copilot-studio, ai-foundry, m365-copilot, purview, azure
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, evaluation-quality
  sources: ms-copilot-privacy, ms-copilot-studio-security-governance, ms-foundry-models, nist-ai-rmf, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# Data product readiness

## Purpose

Structured data is where AI moves from answering questions about documents to answering questions about the business:
sales by region, open cases by age, stock by site. It is also where confident wrong answers do most damage, because
numbers look authoritative. This skill assesses whether a data product, meaning a curated dataset, set of tables or
semantic model with an owner and a defined purpose, is ready for AI to consume, and records a verdict with conditions.
It goes wrong when raw operational tables are pointed at an agent and called a data product, or when readiness is
judged by the data team alone without the business owner who knows what the numbers mean.

## When to use

- An agent, Copilot analysis, data agent or Foundry solution will read structured business data.
- A data team is asked to "make the data AI-ready" and needs a definition of ready.
- A semantic model or curated table set is being opened to natural language questions.
- An AI solution's numeric answers have been wrong and the data product is suspected.
- A data product changes owner, structure or refresh pattern while AI depends on it.

## When not to use

- Assessing documents and knowledge sources an agent grounds on - use `m365-agents:knowledge-source-readiness`.
- Checking files, mail and data a Cowork task relies on - use `copilot-cowork:grounding-readiness`.
- Setting quality thresholds for specific fields - use `data-governance:ai-data-quality`.
- Designing Dataverse use within a Copilot Studio agent - use `copilot-studio:dataverse-integration`.

## Questions to ask first

1. What questions or tasks will AI perform on this data product, for whom, and at what risk tier?
2. Who owns the data product, and will they stand behind AI answers drawn from it?
3. Are tables, fields, measures and codes described well enough that a model and a newcomer would interpret them correctly?
4. Is quality measured against requirements for this use, and is the refresh pattern known?
5. How will AI reach it, under which identity, and does that respect its classification?
6. What happens to dependent AI solutions when the product's structure changes?

## Required inputs

- A description of the AI use and its risk tier.
- The data product's documentation, schema or semantic model, and its owner.
- Quality requirements and results from `data-governance:ai-data-quality`.
- Classification and access pattern from `data-governance:data-classification-for-ai` and `data-governance:ai-data-access-model`.
- Lineage at the depth the tier requires, from `data-governance:ai-data-lineage`.

Where an input is missing, mark the criterion "[To confirm]" and lower the verdict; never infer meaning, ownership or
quality on the owner's behalf.

## Decision framework

Assess each criterion as met, partly met or not met for the intended use.

| Criterion | Ready means |
|---|---|
| Ownership | A named owner and business owner accept accountability for AI use |
| Purpose fit | The product was designed for, or has been checked against, the questions AI will answer |
| Meaning | Tables, fields, measures and codes have clear descriptions, units, synonyms and business definitions |
| Quality | Critical fields meet the requirements set for the use and tier |
| Currency | Refresh pattern known and data age can be shown to users |
| Classification | Classified, with AI-use rules applied |
| Access | An approved access pattern exists and outputs do not exceed users' entitlement |
| Lineage | Recorded at the depth the tier needs |
| Change commitment | Owner agrees to notify dependent AI solutions before breaking changes |
| Test evidence | A set of real questions with known answers has been run against the product |

| Verdict | Rule |
|---|---|
| Ready | All criteria met for the use |
| Ready with conditions | Criteria partly met, with mitigations in design and dated fixes; none of ownership, access or classification is not met |
| Not ready | Ownership, access or classification not met, or quality or meaning not met for a tier 2+ use |

## Practitioner approach

Start with the questions, not the data. Ask the business owner for twenty questions people will really ask the AI, with
the answers they would accept as correct. Those questions define the use, expose which tables and measures matter, and
become the test set at the end. A data product can be excellent for its original reports and still unready for the
questions people will ask in natural language.

Check ownership before anything else. Someone must accept accountability for AI answers drawn from the product and for
telling dependent solutions when it changes. If nobody will, the verdict is not ready, however good the data is.

Spend most of the effort on meaning. Language models interpret data through names, descriptions and relationships.
Ambiguous measure names, undocumented codes, missing units, several "revenue" columns with different definitions and
relationships that only make sense to the original modeller all produce confident wrong answers. Work through the
tables and measures the questions touch, add business descriptions and synonyms, hide fields that should not be used,
and agree one definition for each business term. In a semantic model this is often the single biggest improvement.

Bring in the other governance results rather than repeating them. Quality, classification, access and lineage each
have their own skill; record their outcome against the criterion and note any conditions.

Test with the questions. Run the business owner's questions through the intended AI route and compare answers with the
accepted ones. Look for wrong joins, misread measures, stale figures and answers that reveal more than the user may see.
Fix the product, not the prompt, where possible; descriptions and model changes help every future solution.

Record the verdict on the `data-readiness-assessment` template with conditions, owners and dates, and agree what
triggers a re-assessment: a structural change, a new AI use or a quality breach. Readiness is for a use, not for all
time.

## Outputs

- A data readiness assessment on the `data-readiness-assessment` template: use, criteria results, test question results, verdict (ready, ready with conditions, not ready), conditions with owners and dates, and re-assessment triggers.
- Improved descriptions, synonyms and business definitions in the data product.
- A test question set handed to the evaluation owner.

## Microsoft platform considerations

Structured data may be reached through Copilot over Fabric and semantic models, data agents, Copilot Studio with
Dataverse or connectors, or Foundry solutions over Azure data services, and the way each route interprets schemas and
descriptions differs and changes. Confirm current behaviour in the relevant source records, including
`ms-copilot-studio-security-governance` and `ms-foundry-models`, before relying on a feature.

## Adoption considerations

Business users will trust numeric answers only if early answers are right. Release AI over a data product to a small
group first, with the business owner on hand to explain discrepancies.

## Knowledge considerations

Business definitions, metric glossaries and data documentation are knowledge in their own right. Keep them owned and
current with the knowledge owners, because AI answers depend on them.

## Security and privacy considerations

Aggregated answers can still reveal individuals in small groups. Check with `security-privacy:data-exposure-review`
that outputs respect users' entitlement and that personal data is not exposed through narrow filters.

## Responsible AI considerations

Where answers from the product inform decisions about people, money or access to services, record that in the
assessment and pass the case to `responsible-ai:ai-impact-assessment`.

## Evaluation requirements

The test question set, with accepted answers from the business owner, is the minimum evidence. For tier 2 and above,
agree an acceptance threshold with the business owner and re-run the set after changes to the product or AI route.

## Value measures

Track the share of AI-consumed data products assessed as ready, test question accuracy over time, and incidents traced
to data products. The data governance lead owns the portfolio view; each product owner owns their product's measures.

## Scale notes

### Starter

Pick one well-owned data product for the first AI use, write twenty test questions with the owner, and improve
descriptions before going live.

### Scale

Make the assessment a standard step before any AI use of structured data, keep assessed products in the data
catalogue, and reuse test sets.

### Enterprise

Treat AI readiness as a property of data products in the enterprise data strategy, with standards for descriptions and
change commitments, and re-assess on every structural change.

## Hand-offs

- To the AI solution's build team with the verdict and conditions.
- To `data-governance:ai-data-quality` for quality gaps.
- To `evaluation-quality:golden-dataset` with the test question set.
- To `security-privacy:data-exposure-review` where outputs could exceed users' entitlement.

## Reviewer gates

From risk tier 2, `security-privacy` checks the access and classification criteria and `evaluation-quality` checks the
test evidence before an AI solution relying on the product is released.

## Failure modes

- Raw operational tables are pointed at an agent and called a data product.
- The data team judges readiness without the business owner, so meaning errors survive.
- Prompts are tuned to work around a confusing model instead of fixing the model.
- The product changes structure and dependent AI solutions break silently.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Declare a data product ready without a named owner who accepts AI use.
- Infer business definitions on the owner's behalf.
- Treat readiness for one use as readiness for every use.
- Release AI over structured data without testing real questions against accepted answers.

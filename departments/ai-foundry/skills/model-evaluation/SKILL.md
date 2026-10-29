---
name: model-evaluation
description: Runs the comparative evaluation that decides which candidate model, prompt or configuration performs a specific task best in a Microsoft Foundry solution - task-specific test set, quality and tool-calling measures, latency and cost per task, thresholds set before results, repeated runs and a written comparison. Use when a model shortlist needs testing, when a model version is being replaced, or when two configurations must be compared fairly.
license: CC-BY-4.0
metadata:
  department: ai-foundry
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality, responsible-ai
  sources: ms-foundry-models, ms-responsible-ai, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Model evaluation

## Purpose

Choosing between models, versions or configurations is an experiment, and it deserves the discipline of one: a fixed
task, a representative test set, measures and thresholds agreed in advance, and enough repeated runs to tell a real
difference from noise. This skill runs that experiment for a Foundry solution and turns it into a written comparison
the selection and release decisions can rely on. Model evaluation goes wrong when a vendor benchmark or a good
demonstration stands in for testing, when candidates are run on different prompts or data, and when thresholds are
quietly set after the results show which model the team already preferred.

## When to use

- `ai-foundry:model-selection` has produced a shortlist and needs comparative evidence to choose.
- A deployed model version is being retired or upgraded and the replacement must be shown to be at least as good.
- A team wants to swap to a smaller, cheaper or faster model and needs to know what quality is lost.
- Two prompts, retrieval settings or agent configurations need a fair comparison.
- Different steps in a multi-step solution might use different models, and each step needs evidence.

## When not to use

- Shortlisting candidates and recording the final choice - use `ai-foundry:model-selection`.
- Setting the overall evaluation strategy for the solution and its release - that is the reviewer skill `evaluation-quality:ai-evaluation-strategy`.
- Building the reference dataset and its governance - that is the reviewer skill `evaluation-quality:golden-dataset`.
- Automating evaluation runs in the build pipeline - use `ai-engineering:evaluation-harness`.
- Testing harmful-content and prompt attack behaviour - use `ai-foundry:foundry-safety-evaluation`.

## Questions to ask first

1. What exact task is being compared, what does a correct output look like, and who decides when an output is good enough?
2. What are the candidates, and what is held constant across them (prompt, retrieval, tools, settings)?
3. Which measures matter for this decision, quality, tool-calling accuracy, format adherence, latency or cost per task, and what threshold must each meet?
4. Is there a representative test set drawn from real work, and does it include hard, edge and out-of-scope cases?
5. What difference between candidates would actually change the decision?

## Required inputs

- The task definition and shortlist from the `model-selection-record` template.
- A test set of real or realistic inputs with expected outputs or reference answers, confirmed by a business or knowledge owner.
- A scoring rubric for judgement-based measures, ideally from `evaluation-quality:ai-quality-rubric`.
- Non-production deployments of each candidate, configured as they would run in production.

Where the test set or thresholds are missing, mark them `[To confirm: ...]` and do not run the comparison. Results
without a pre-agreed threshold invite the team to rationalise its favourite.

## Decision framework

| Measure | Method | Typical decision rule |
|---|---|---|
| Task quality | Reference comparison for extraction and classification; rubric scoring by people, or by a calibrated model grader checked against people, for open answers | Must meet the threshold; differences within run-to-run variation are treated as ties |
| Groundedness and citation | Claim-level check against retrieved sources | Must meet the threshold where answers rely on sources |
| Tool calling and format | Correct tool, correct arguments, valid schema | Near-perfect for write tools and parsed outputs |
| Latency | Measured end to end on the production-like deployment | Must fit the latency budget at expected load |
| Cost per task | Tokens or units consumed per completed task, priced from the current source | Compared only among candidates that pass quality |

Choose the cheapest and fastest candidate that passes every threshold. If none passes, the answer is to change the
prompt, retrieval or task design, or to stop, not to lower the threshold.

## Practitioner approach

Fix the task and the thresholds first and write them down with a date. The business owner agrees what good enough means,
in measures they understand, before any candidate is run. Agree too what size of difference would matter; a small gain
in quality may not justify a large rise in cost or latency.

Build or borrow a test set that looks like real work. Use genuine examples where privacy allows, or realistic synthetic
ones checked by people who know the domain, and include hard cases, edge cases, ambiguous requests and requests the
solution should decline. A few dozen well-chosen cases beat hundreds of easy ones. Hold back a portion the team does not
tune against, so the final comparison is not flattered by over-fitting.

Hold everything else constant. Each candidate runs with the same prompt structure, retrieval results, tools and
settings, adjusted only where a model's documented conventions require it, and those adjustments are recorded. If a
prompt has to be re-tuned for a candidate, give every candidate comparable tuning effort, or the comparison measures
effort rather than models.

Run each candidate several times. Model outputs vary between runs, so a single run can mislead. Report the spread, not
only the average, and treat overlapping results as a tie. Measure latency on deployments configured like production, and
calculate cost per completed task rather than per call, because retries and longer outputs change the picture.

Use model graders carefully. An AI-assisted grader speeds up scoring of open answers, but it has its own biases and may
favour outputs that resemble its own style. Calibrate it against a sample scored by people before relying on it, and
keep people scoring the cases that matter most.

Read the failures, not just the scores. Group wrong outputs by cause, such as missing context, wrong tool, format
breakage or over-refusal, because the cause often points to retrieval or prompt fixes that would change the ranking.

Write the comparison into the evidence section of the `model-selection-record` template: task, test set version,
candidates and settings, thresholds and their date, results with spread, failure analysis, recommendation and what the
evaluation could not show. Keep the set and scripts so the comparison can be repeated when a model changes.

## Outputs

- A comparative evaluation report in the evidence section of the `model-selection-record` template, with dated thresholds, results and spread per candidate, failure analysis and recommendation.
- A versioned, task-specific test set with a held-back portion, stored with restricted access.
- Evaluation configuration and scripts handed to `ai-engineering:evaluation-harness` for repeat runs.
- Inputs to the `evaluation-plan` template for the solution's release evidence.

## Microsoft platform considerations

Microsoft Foundry provides evaluation tooling, built-in quality and safety evaluators and ways to compare runs, and the
evaluators, supported models and preview status change often. Check the current source records before relying on a
built-in evaluator, and calibrate it against human judgement for the task. Third-party models in the catalogue may
differ in deployment type, throughput and pricing model, so measure latency and cost on the deployment type that would
be used in production rather than comparing list figures.

## Adoption considerations

Not applicable to the evaluation itself, because users experience the chosen model rather than the comparison. Where
real user examples are used in the test set, tell the business owner how they were chosen and protected.

## Knowledge considerations

Where the task relies on retrieved knowledge, freeze the retrieval results or index version used in the comparison so
knowledge changes do not masquerade as model differences, and record the version.

## Security and privacy considerations

Test sets built from real work can contain personal or confidential data. Minimise, mask or replace it, restrict access
to the set and the outputs, and run evaluations only on deployments approved for that data. Data processing questions
for third-party models go to the DPO.

## Responsible AI considerations

Include cases that represent the full range of users and inputs, such as different languages, writing styles and
accessibility needs, and report quality by subgroup where outputs affect people, coordinating with
`responsible-ai:fairness-review`.

## Evaluation requirements

This skill is evaluation. Its own quality rests on thresholds dated before results, a held-back set, repeated runs,
calibrated graders and a recorded test set version, so the comparison can be reproduced and audited.

## Value measures

Track cost and latency savings from evidence-based model choices, and how often post-release quality matches the
evaluation, owned by the solution owner. A gap between evaluated and live quality signals an unrepresentative test set.

## Scale notes

### Starter

Compare two or three candidates on a small, well-chosen set with human scoring and three runs each. Record the result on
the model selection record and keep the set for the next model change.

### Scale

Maintain task-type test sets and calibrated graders that solutions reuse, and run comparisons through a shared harness
so results are comparable across teams.

### Enterprise

Run a standing evaluation service that re-tests widely used models when new versions appear, publishes comparisons to
solution owners and feeds the approved model list.

## Hand-offs

- To `ai-foundry:model-selection` with the recommendation and evidence.
- To `ai-engineering:evaluation-harness` to automate repeat runs.
- To `ai-foundry:foundry-prompt-engineering` or `ai-foundry:retrieval-design` when failure analysis points there.
- To `evaluation-quality:ai-release-evidence` as part of the release evidence pack.

## Reviewer gates

From risk tier 2, `evaluation-quality` checks that thresholds predate results, the test set is representative and the
comparison is reproducible, and `responsible-ai` checks subgroup results where outputs affect people. A threshold changed
after results is a blocking finding.

## Failure modes

- A vendor benchmark replaces testing, and the chosen model underperforms on the organisation's own documents.
- Candidates are run with different prompts or retrieval, and the comparison measures setup rather than models.
- A single run is treated as decisive, and the model chosen on a lucky result performs worse in production.
- An uncalibrated model grader favours verbose answers, and the evaluation rewards the wrong behaviour.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Set or change a threshold after seeing the results.
- Select a model on vendor benchmarks or a demonstration alone.
- Compare candidates under different prompts, data or settings without recording and justifying the difference.
- Use real personal data in a test set without minimisation, access control and an approved deployment.

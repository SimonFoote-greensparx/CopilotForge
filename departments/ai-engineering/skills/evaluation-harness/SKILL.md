---
name: evaluation-harness
description: Builds the automated evaluation harness for a custom AI solution - dataset loading, repeatable runs against pinned models and prompts, code-based and model-graded evaluators, scoring against agreed thresholds, results history and reports - so quality is checked on every change. Use when an AI solution needs repeatable evaluation in its pipeline, when manual spot checks no longer scale, or when evaluation results cannot be reproduced.
license: CC-BY-4.0
metadata:
  department: ai-engineering
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, github, copilot-code
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality
  sources: ms-foundry-models, ms-responsible-ai, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Evaluation harness

## Purpose

Evaluation strategy says what quality means and how much is enough; the harness is the code that measures it, the same
way, every time something changes. Without one, teams test by trying a few questions by hand before each release, and
regressions reach users. This skill builds the harness: loading the dataset, running the solution under pinned
conditions, applying evaluators, scoring against thresholds, storing results and reporting them where decisions are made.
It goes wrong when the harness tests a different configuration from production, when model-graded scores are trusted
without calibration, and when thresholds are adjusted after seeing the results.

## When to use

- A custom AI solution needs automated, repeatable evaluation in its pipeline.
- Manual spot checks before release no longer cover the range of inputs or changes.
- Evaluation results differ between runs and nobody can tell whether quality changed.
- The team is changing a model, prompt, tool or retrieval setting and needs evidence that nothing regressed.
- The evaluation strategy and dataset exist, and someone now has to make them run.

## When not to use

- Deciding what to evaluate, which dimensions matter and how evaluation is governed - use `evaluation-quality:ai-evaluation-strategy`.
- Building and curating the golden dataset itself - use `evaluation-quality:golden-dataset`.
- Comparing candidate models for a task - use `ai-foundry:model-evaluation`.
- Setting quality rubrics and acceptance thresholds - use `evaluation-quality:ai-quality-rubric`.
- Testing a Copilot Studio agent - use `copilot-studio:studio-testing-and-evaluation`.

## Questions to ask first

1. What evaluation strategy, rubric and thresholds have been agreed, and by whom?
2. Where is the evaluation dataset, how is it versioned and does it contain sensitive data?
3. Which dimensions can be checked by code, and which need a model-graded or human judgement?
4. Which changes must trigger a run (prompt, model, tool, retrieval, code), and how long can a run take in the pipeline?
5. Who reads the results and makes the release decision?

## Required inputs

- The evaluation strategy and rubric, with thresholds agreed before results are seen.
- A versioned evaluation dataset, or a reference to an immutable version in a governed store.
- A way to run the solution non-interactively against an input, with the same configuration as the target environment.
- Budget and quota for model calls made during evaluation.

If thresholds have not been agreed, build the harness to report scores but do not let it pass or fail a release until
the business owner agrees thresholds. Never set thresholds by looking at the first results.

## Decision framework

Choose the evaluator for each quality dimension by the cheapest reliable method.

| Dimension type | Evaluator | Notes |
|---|---|---|
| Format and structure | Code (schema checks, parsers) | Deterministic; always run |
| Exact facts and fields | Code (match against expected values, with normalisation) | Deterministic; preferred where answers are known |
| Tool selection and arguments | Code (compare calls with expected calls) | Include near-miss cases |
| Groundedness and citation | Model-graded with a fixed rubric, or code where citations are checkable | Calibrate against human labels |
| Relevance, completeness, tone | Model-graded with a fixed rubric | Calibrate; report agreement with humans |
| Safety and refusal | Code for known patterns plus model-graded and safety evaluators | Zero-tolerance items fail the run outright |
| Subjective quality at high risk | Human review of a sample | Harness prepares the sample and records the labels |

Set run tiers. A fast subset runs on every pull request; the full set runs before promotion and on a schedule.

## Practitioner approach

Start from the agreed strategy and rubric. The harness implements decisions; it does not make them. List each quality
dimension, its threshold, any zero-tolerance failures and the evaluator chosen for it. Confirm the business owner agreed
the thresholds before any result was seen.

Make runs reproducible. Pin the model deployment and version, the prompt version, tool versions and retrieval
configuration, and record them with every run. Set generation parameters to the values used in production, not
idealised ones. Where outputs vary between runs, run each case more than once and report the spread, so a release
decision is not made on noise.

Test the system the user gets. Call the solution through the same orchestration, tools and retrieval it uses in
production, against a dedicated evaluation environment with representative data and permissions. Evaluating the model
alone, with a hand-built prompt, measures something users never see.

Prefer code evaluators. Where a correct answer is known, check it with code: field values, numbers, dates, the tool
called and its arguments, the presence of a refusal. Code evaluators are cheap, fast and stable. Use model-graded
evaluators for judgements code cannot make, with a fixed rubric, a pinned grading model and examples. Calibrate them:
have people label a sample and report agreement. A grader that disagrees with people is not evidence.

Keep zero-tolerance cases separate. Exposure of restricted data, unsafe content or an unconfirmed write fails the run
regardless of average scores. Report them individually.

Store results as history, not just a pass or fail. Keep per-case results, scores, configuration and cost for each run,
so trends and the effect of each change are visible. Produce a short report for the pull request and a fuller one for
release, showing scores against thresholds, failures by category and changes since the last run.

Wire it into the pipeline with `ai-engineering:ai-ci-cd`: a fast subset on every change to behaviour-changing assets,
the full set before promotion and on a schedule to catch provider-side drift. Control cost by sizing the subset and
caching unchanged results where valid. When a failure is found in production, add the case to the dataset through the
golden dataset process so it is tested from then on.

## Outputs

- An evaluation harness in the solution repository: dataset loader, runner, evaluators, scoring, thresholds configuration, results store and report generator.
- Run tiers and triggers (pull request subset, full pre-release run, scheduled run).
- Calibration results for each model-graded evaluator.
- A results history with configuration recorded per run, feeding `evaluation-quality:ai-release-evidence`.

## Microsoft platform considerations

Microsoft Foundry provides evaluation capabilities, built-in evaluators including quality and safety evaluators, and
SDKs that can run in pipelines; the available evaluators, their behaviour and their costs change. Check current
capabilities in `references/sources.md`, pin evaluator versions where possible, and treat built-in evaluators like any
model-graded evaluator: calibrate before relying on them.

## Adoption considerations

Engineers run the harness when it is fast and its output is useful in the pull request. Keep the subset quick, the report
short and the failing cases easy to inspect. Business owners trust results they helped define; show them the report
format early.

## Knowledge considerations

Where the solution grounds on knowledge, the harness depends on that knowledge being stable in the evaluation
environment. Snapshot or version the evaluation corpus, and re-baseline when the knowledge owner makes major changes.

## Security and privacy considerations

Evaluation datasets and results can contain personal or confidential data. Hold them in governed stores with access
limited to the team, avoid printing sensitive content in pipeline logs, and run evaluation in an environment with the
same data protections as production.

## Responsible AI considerations

Include cases that reflect the full range of users and inputs, including languages, accessibility needs and groups the
solution could treat unfairly, and report results by segment where the strategy calls for it. Safety evaluation results
go to the `responsible-ai` and `evaluation-quality` reviewers.

## Evaluation requirements

The harness itself is tested: evaluators have unit tests on known good and bad outputs, model-graded evaluators have
calibration evidence, and a deliberately degraded configuration must fail the run.

## Value measures

Track regressions caught before release, regressions found in production, run time and evaluation cost per run. The AI
engineering lead owns these; evaluation quality reviewers use them to judge the harness's coverage.

## Scale notes

### Starter

Begin with a small dataset, code evaluators for the dimensions that allow it, one calibrated model-graded evaluator, and a
run before each release. Store results in the repository or a simple store.

### Scale

Run subsets on every pull request and full sets before promotion, share evaluators across solutions as a versioned
package, and keep results history in a common store.

### Enterprise

Provide a shared evaluation platform with standard evaluators, calibration records, scheduled drift runs across solutions
and results feeding release evidence and portfolio reporting.

## Hand-offs

- To `ai-engineering:ai-ci-cd` to run the harness as a pipeline gate.
- To `evaluation-quality:ai-release-evidence` with results for release decisions.
- To `evaluation-quality:regression-evaluation` for regression policy after changes.
- To `evaluation-quality:golden-dataset` with production failures to add as cases.

## Reviewer gates

From risk tier 2, `evaluation-quality` reviews the harness: that it tests the production configuration, that evaluators
are calibrated and that thresholds were agreed in advance. Thresholds changed after results were seen are a blocking
finding.

## Failure modes

- The harness evaluates the model with a hand-written prompt, not the deployed solution, and passes a broken release.
- A model-graded evaluator is never calibrated and scores fluent but wrong answers highly.
- Thresholds are lowered after a disappointing run, and the release goes ahead on a moved goalpost.
- Variance between runs is ignored, and a release is blocked or passed on noise.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Set or change a threshold after seeing the results it will judge.
- Rely on a model-graded evaluator that has not been calibrated against human judgement.
- Evaluate a configuration that differs from the one being released.
- Let average scores hide a zero-tolerance failure.

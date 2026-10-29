---
name: regression-evaluation
description: Decides and reviews what must be re-evaluated after a change to a live AI solution - instructions, knowledge, actions, model or platform updates - selecting the regression subset, comparing with the last baseline while allowing for normal output variation, and recommending release, hold or rollback, with findings classed blocking or advisory. Use when a change is ready to deploy or Microsoft announces a model or platform change.
license: CC-BY-4.0
metadata:
  department: evaluation-quality
  lifecycle: Deliver, Assure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-cowork, copilot-studio, ai-foundry, power-platform, copilot-code
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality
  sources: ms-copilot-studio-guidance, ms-foundry-models, ms-agent-builder, ms-managed-environments, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Regression evaluation

## Purpose

AI solutions regress quietly. A tidied instruction, a re-organised library or a model update can change answers that
were right yesterday, and nobody notices until a user does. This reviewer skill decides what must be re-evaluated for
each kind of change, runs or reviews the comparison with the last accepted baseline while allowing for the normal
variation in AI outputs, and recommends release, hold or rollback, classifying findings as blocking or advisory.
Regression work goes wrong when every change triggers a full re-test that nobody has time for, so changes ship
untested, or when ordinary variation is mistaken for regression and real regressions are dismissed as noise.

## When to use

- A change to a live solution's instructions, knowledge, actions, configuration or orchestration is ready to deploy.
- Microsoft announces a model, platform or feature change that may affect a live solution.
- Users report that answers have changed or got worse since a recent update.
- A team submits regression results to the `evaluation-quality` gate.

## When not to use

- Judging the design, risk and ownership impact of a proposed change - use `design-authority:ai-change-impact-review`.
- Building the full evaluation set in the first place - use `evaluation-quality:golden-dataset`.
- Running a first-release evaluation of a new agent - use `m365-agents:agent-testing`.
- Automating regression runs in a pipeline - use `ai-engineering:evaluation-harness` or `ai-engineering:ai-ci-cd`.
- Routine refresh of knowledge content in operation - use `ai-operations:knowledge-refresh`, which hands back here for the re-run.

## Questions to ask first

1. What exactly changed, and which behaviours, topics or actions could it plausibly affect?
2. Is there an accepted baseline result on a known dataset version and configuration?
3. How much do this solution's results normally vary between identical runs?
4. Can the change be rolled back quickly if regression is found after release?
5. Was the change made by the organisation, or by Microsoft on its own release schedule?

## Required inputs

- The change description and the configuration versions before and after.
- The last accepted baseline: dataset version, rubric version, results per dimension and the variation observed.
- The golden dataset with its regression subset marked.
- The rollback route for the change, confirmed by the builder.

Where no baseline exists, a regression comparison is impossible; run the full evaluation, accept it as the new baseline
with the business owner, and record that this release was not regression-tested.

## Decision framework

Select the scope of re-evaluation from the type of change.

| Change | Minimum re-run | Add |
|---|---|---|
| Wording of instructions | Regression subset plus refusal and out-of-scope items | Full set if behaviour rules changed |
| Knowledge added, removed or restructured | Items grounded on affected sources, knowledge-silent and contradiction items | Groundedness checks via `evaluation-quality:groundedness-testing` |
| New or changed action or connector | All action items plus confirmation and failure handling | Security re-test via `security-privacy:ai-security-testing` |
| Model or orchestration change | Full golden dataset | Safety set and red-team items from tier 3 |
| Platform or feature update announced by Microsoft | Regression subset | Full set where the update touches grounding, safety or actions |
| Audience widened | Permission and refusal items | Full review through the release gate |

Judge results against the baseline.

| Result | Meaning | Recommendation |
|---|---|---|
| Within normal variation on every dimension, no zero-tolerance breach | No regression detected | Release |
| Drop beyond normal variation on any dimension, still above threshold | Regression, not yet failing | Release with advisory finding, or hold if trend continues |
| Any dimension below threshold, or any zero-tolerance breach | Regression failing the gate | Blocking: hold or roll back, fix and re-run |

## Practitioner approach

Know your noise before you judge a change. When a baseline is accepted, run the regression subset several times on the
same configuration and record how much results vary. Without that figure, every small drop looks like regression and
every real one can be waved away as randomness. Repeat the measurement after any model change, because variation itself
can shift.

Keep the regression subset small enough to run on every change and representative enough to matter. Draw it from the
golden dataset: the highest-consequence core items, every zero-tolerance item, refusal and knowledge-silent items, and
any item that has ever failed in live use. Mark it in the dataset and version it.

When a change arrives, start with what it could affect, using the scope table. A wording tweak to the tone section of
instructions rarely needs the full set; a new action always needs its action items. Write down the chosen scope and why,
so a reviewer can challenge it.

Run on the new configuration with the same dataset and rubric versions as the baseline. If either has changed, re-run
the baseline configuration on the new versions first, or comparisons will mislead. Score with calibrated graders, and
compare per dimension, not in total.

Look at individual items as well as rates. A stable pass rate can hide one high-consequence answer that has flipped
from right to wrong while another low-consequence one flipped the other way. List every item that changed outcome and
review the high-consequence ones by hand.

Treat changes made by Microsoft differently only in timing. Watch the announcements the organisation tracks, run the
regression subset when a relevant change reaches a test environment where possible, and again when it reaches
production. Where the organisation cannot control the timing, monitoring and fast regression runs are the defence.

Recommend clearly: release, release with advisory findings, or hold and roll back. The business owner decides on
advisory drops; blocking regressions are not released. After release, the new results become the baseline once
accepted, with the date recorded.

## Outputs

- A regression scope decision for each change, with the reasoning.
- A regression results record: configuration versions, dataset and rubric versions, results against baseline and normal variation, items that changed outcome, and the recommendation.
- Findings classified blocking or advisory, with fix and owner, attached to the change record and the `evaluation-plan`.
- An updated baseline once accepted.

## Microsoft platform considerations

Copilot Studio, Agent Builder and Microsoft Foundry handle versions, environments and model updates differently, and
the timing of Microsoft model and platform changes is not always in the organisation's control. Confirm current
versioning, environment and release-channel options in `ms-copilot-studio-guidance`, `ms-agent-builder`,
`ms-foundry-models` and `ms-managed-environments`, and test in a non-production environment first where the route allows.

## Adoption considerations

Tell users when a material change is released and what it improves. When a regression slips through, acknowledge it
quickly and say when it will be fixed; silent changes erode trust faster than visible fixes.

## Knowledge considerations

Knowledge changes are the most frequent regression trigger. Agree with knowledge owners which kinds of edit need a
regression run, and ask them to notify the solution owner through `ai-operations:knowledge-refresh` before publishing
major changes.

## Security and privacy considerations

Changes to sharing, connectors or actions need permission and action tests in the regression scope, and evidence passed
to `security-privacy` from tier 2. A regression in a zero-tolerance exposure item is always blocking.

## Responsible AI considerations

Model changes can shift behaviour towards different groups of people. Where the solution affects people, include
fairness items from `responsible-ai:fairness-review` in the scope for model and orchestration changes.

## Evaluation requirements

Minimum from tier 2: a recorded scope decision per change, results against an accepted baseline on the same dataset and
rubric versions, normal variation known, every changed high-consequence item reviewed, and the new baseline accepted.

## Value measures

Track regressions caught before release versus those reported by users, time from change to regression result, and the
share of changes released with a regression run. The AI Evaluation Lead reports by solution, never by maker.

## Scale notes

### Starter

A regression subset of ten to fifteen items in a spreadsheet, run by the maker and checked by the owner after every
change, with the previous results kept for comparison.

### Scale

Regression subsets maintained in each solution's dataset, scope decisions recorded in the change process, and runs
automated where the route supports it.

### Enterprise

Regression runs integrated with deployment pipelines and change approval, platform change notices triaged centrally
against the solution inventory, and portfolio-level reporting of regression trends.

## Hand-offs

- To `design-authority:ai-change-impact-review` when results suggest the change has wider design impact.
- To `ai-engineering:ai-ci-cd` to automate regression in deployment.
- To `ai-operations:ai-solution-monitoring` to watch the released change in live use.
- To `evaluation-quality:ai-release-evidence` for material changes that need a fresh release decision.

## Reviewer gates

This skill operates within the `evaluation-quality` gate and is blocking from risk tier 2 and advisory below it. A
regression below threshold or a zero-tolerance breach stops the change and is not traded against dates; disagreement
escalates to the accountable executive for written risk acceptance.

## Failure modes

- Normal variation is unknown, so real regressions are dismissed as noise.
- The dataset or rubric changed between runs and the comparison is meaningless.
- A stable pass rate hides a high-consequence item that flipped from right to wrong.
- Microsoft platform changes arrive with no regression run because nobody was watching the announcements.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Release a change that breaches a zero-tolerance item or drops a dimension below threshold.
- Compare results produced on different dataset or rubric versions without re-baselining.
- Skip regression because a change looked small, without recording the scope decision.
- Treat a total pass rate as sufficient without reviewing items that changed outcome.

---
name: ai-evaluation-strategy
description: Sets and reviews the evaluation strategy for a probabilistic AI solution - which quality dimensions matter, which methods and datasets measure them, thresholds agreed before results and when evaluation repeats - classifying gaps as blocking or advisory. Use when a tier 2 or higher agent, workflow or Foundry solution enters design, or when nobody can say how the team will know it is good enough.
license: CC-BY-4.0
metadata:
  department: evaluation-quality
  lifecycle: Envision, Deliver, Assure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-cowork, copilot-studio, ai-foundry, copilot-code, power-platform
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality
  sources: nist-ai-rmf, ms-responsible-ai, ms-copilot-studio-guidance, ms-agent-builder, ms-foundry-models, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# AI evaluation strategy

## Purpose

Conventional testing asks whether software does what it was built to do. AI evaluation asks how often a probabilistic
system is good enough, for whom, and how anyone would notice when it stops being so. This reviewer skill sets the
evaluation strategy for an AI solution - the quality dimensions that matter, the methods and datasets that measure them,
the thresholds agreed before results are seen and the cadence at which evaluation repeats - and reviews strategies that
delivery teams propose, classifying each finding as blocking or advisory. Strategies usually fail by measuring what is
easy (did it respond) rather than what matters (was it right, grounded and safe for this audience), or by testing once
before launch and never again.

## When to use

- A solution at risk tier 2 or above enters design or build and needs an evaluation plan before testing starts.
- A delivery team proposes an evaluation approach and the `evaluation-quality` gate must judge whether it is adequate.
- Several teams evaluate agents in different ways and the organisation wants one proportionate standard.
- A sponsor asks how the team will know the solution is good enough, and nobody can answer in measurable terms.
- A live solution has no evaluation beyond user complaints.

## When not to use

- Running the tests for one Microsoft 365 agent against its evaluation set - use `m365-agents:agent-testing`, or `copilot-studio:studio-testing-and-evaluation` for Copilot Studio specifics.
- Building the reference questions and expected answers - use `evaluation-quality:golden-dataset`.
- Defining scoring scales, anchors and pass thresholds in detail - use `evaluation-quality:ai-quality-rubric`.
- Building automated evaluation tooling and pipelines - use `ai-engineering:evaluation-harness`.
- Comparing candidate models for a task in Microsoft Foundry - use `ai-foundry:model-evaluation`.

## Questions to ask first

1. What decision or piece of work does the output feed, and what does a wrong, ungrounded or unsafe output cost at this risk tier?
2. Who can judge a good answer with authority, and how much of their time is genuinely available for evaluation?
3. Which failures are never acceptable, whatever the overall pass rate?
4. What will change after release - knowledge, instructions, models, platform updates - and how often?
5. Which evaluation features does the chosen platform route offer today, confirmed in the current source records?

## Required inputs

- The solution brief or design with purpose, audience, scope, exclusions and the risk tier from `opportunity-management:risk-classification`.
- The knowledge sources and their owners, and any actions the solution takes in other systems.
- The business owner's success measures and value hypothesis.
- Findings already raised by `security-privacy` or `responsible-ai` reviewers.

Where the risk tier or the business owner is missing, the strategy cannot be approved. Mark the gap "to confirm" and
treat it as blocking from tier 2, because a threshold without an accountable owner has no authority.

## Decision framework

Evaluation depth follows the risk tier. Each tier includes everything to its left.

| Element | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Quality dimensions | Correct, appropriate | Adds grounded and safe | Adds consistency across repeated runs and action correctness | Adds fairness across affected groups and effectiveness of human oversight |
| Methods | Owner and user review | Human review against a rubric, scripted refusal and out-of-scope tests | Adds AI-assisted grading calibrated against human judges, and red teaming | Adds independent evaluation by people who did not build it |
| Dataset | Seed questions | Versioned golden dataset | Golden dataset with variants and an adversarial set | Plus a held-out set the builders never see |
| Thresholds | Owner judgement, recorded | Per dimension, agreed before results, with a zero-tolerance list | Plus repeated runs so results are stable | Plus written acceptance by the accountable executive |
| Cadence | On material change | Every material change plus a scheduled re-run | Plus sampling of live outputs | Plus monitoring triggers that force re-evaluation |

When reviewing a proposed strategy, classify each finding. From tier 2 a blocking finding stops the gate; below tier 2
findings are advisory, and a finding that would have been blocking suggests the tier is wrong.

| Finding | Blocking from tier 2 when | Advisory when |
|---|---|---|
| Thresholds | Absent, or set after results were seen | Agreed but without a recorded rationale |
| Dimension coverage | A dimension material to the risk is unmeasured, such as grounding for a knowledge agent or action correctness for an agent that acts | A less relevant dimension is measured lightly |
| Judge validity | AI-assisted grading is used without calibration against human judges | Calibration exists but the sample is small |
| Dataset | Written by the maker alone, or no refusal and out-of-scope cases | Coverage is thin in a minor area |
| Repeatability | No regression plan after change | The regression subset is not yet automated |

## Practitioner approach

Start from consequences, not metrics. Ask the business owner what happens when the solution is wrong: who notices, how
quickly, and what it costs. A drafting assistant whose output is always edited by an expert needs a different strategy
from an agent that answers employees' benefit questions with no one checking. Write the consequence down in one or two
sentences; every later choice should trace back to it.

Choose the dimensions next, and keep them few. Most solutions need correctness, groundedness, appropriateness of scope
and tone, and safety. Add consistency when the same question must give the same substance every time, action
correctness when the solution writes to other systems, and fairness when outputs affect people differently. Each
dimension needs a plain definition the business owner would recognise, handed to `evaluation-quality:ai-quality-rubric`
for scales and anchors.

Then match methods to dimensions. Human review by people with subject authority is the reference for correctness.
Automated checks suit format, refusal phrasing and citation presence. AI-assisted grading scales review across many
items, but it is only trustworthy once its scores have been compared with human scores on a sample and the gap is
known; until then it is a triage aid, not evidence. Red teaming and safety testing find what friendly datasets miss.
Use what the platform route offers, checked against the current source records, rather than building tooling the
route already provides.

Specify the datasets: how many items, drawn from whom, covering which edges, and who confirms expected answers. Send
the build to `evaluation-quality:golden-dataset`. Insist that users, not only makers, contribute questions.

Fix thresholds before anyone sees results, with the business owner, per dimension, plus a short zero-tolerance list
such as exposing restricted content, unsafe advice or acting without confirmation. Record the date of agreement.
Thresholds that move after results are the most common way evaluation turns into theatre.

Plan for change. Name the events that trigger re-evaluation - knowledge updates, instruction edits, new actions, model
or platform changes announced by Microsoft - and the regression subset that runs on each. Decide how live quality will
be sampled after release and who looks at the samples.

Finally, record what the strategy cannot tell you. Evaluation on a few dozen questions shows the solution is fit for
those patterns; it does not prove behaviour on every question. Say so in the plan, and make sure monitoring and feedback
cover the gap.

## Outputs

- An evaluation plan on the `evaluation-plan` template: consequence statement, dimensions, methods, datasets, thresholds with date agreed, zero-tolerance list, cadence, regression triggers and known limits.
- A review record of a team's proposed strategy, with each finding classified blocking or advisory, the risk behind it, the fix and an owner.
- Referrals to `evaluation-quality:golden-dataset`, `evaluation-quality:ai-quality-rubric` and, from tier 3, `evaluation-quality:red-team-plan`.

## Microsoft platform considerations

Copilot Studio, Agent Builder, Microsoft Foundry and Power Platform each offer different evaluation, testing and
analytics features, and these change frequently. Confirm what the chosen route offers in `ms-copilot-studio-guidance`,
`ms-agent-builder` and `ms-foundry-models` before designing methods around a feature. Where a route offers built-in
evaluation, use it, and record which version or configuration produced the results so they can be compared later.

## Adoption considerations

Users who contribute questions to evaluation become early advocates and set realistic expectations in their teams.
Publish the known limits from the plan at launch so trust is built on what the solution actually does well.

## Knowledge considerations

For grounded solutions, most quality failures come from knowledge. The strategy must name the knowledge owners who
confirm expected answers and must tie re-evaluation to their review cycles.

## Security and privacy considerations

Evaluation data can hold confidential or personal content. Keep datasets and recorded outputs in locations restricted to
the evaluation team, use only data testers are entitled to see, and include permission-trimming tests from tier 2 as
evidence for the `security-privacy` reviewer.

## Responsible AI considerations

Where outputs affect people, the strategy must include fairness and oversight dimensions agreed with the
`responsible-ai` reviewers, such as `responsible-ai:fairness-review` and `responsible-ai:human-oversight`. Some harms are
not measurable by pass rates; record them as qualitative review items rather than leaving them out.

## Evaluation requirements

This skill defines the evaluation. The minimum from tier 2 is an approved `evaluation-plan` with owner-agreed thresholds
dated before results, a golden dataset reference, named methods per dimension and a regression trigger list.

## Value measures

Track, at portfolio level, the share of tier 2 and higher solutions with an approved evaluation plan before testing,
the number of defects found by evaluation before users saw them, and the time from change to re-evaluation. The AI
Evaluation Lead owns these measures; report by solution, never by maker or tester.

## Scale notes

### Starter

A one-page plan per agent: three or four dimensions, a small owner-confirmed question set, thresholds agreed in writing
and a rule to re-run after every change. Human review is enough at this scale.

### Scale

Publish a standard evaluation plan for each solution type, reuse rubrics across similar agents and introduce
calibrated AI-assisted grading for larger datasets. The `evaluation-quality` gate reviews every tier 2 and higher plan.

### Enterprise

Federate tier 2 plan reviews to trained business-unit evaluators using the same criteria, keep tier 3 and 4 with the
central team, and maintain a library of datasets and rubrics with owners and versions.

## Hand-offs

- To `evaluation-quality:golden-dataset` and `evaluation-quality:ai-quality-rubric` to build the dataset and rubric.
- To `m365-agents:agent-testing`, `copilot-studio:studio-testing-and-evaluation` or `ai-engineering:evaluation-harness` to execute.
- To `evaluation-quality:red-team-plan` and `evaluation-quality:ai-safety-testing` from tier 3.
- To `evaluation-quality:ai-release-evidence` when results are ready for the gate.

## Reviewer gates

This skill is the `evaluation-quality` gate for evaluation design. It is blocking from risk tier 2 and advisory below
it. Blocking findings stop the solution entering formal testing and are not traded against dates; disagreement escalates
to the accountable executive for written risk acceptance.

## Failure modes

- Thresholds are set after results are known and drift to whatever the solution achieved.
- AI-assisted grading is trusted without calibration, so a confident judge hides real failures.
- The dataset reflects the maker's assumptions, so evaluation confirms the design instead of testing it.
- Evaluation happens once before launch, and a later knowledge update silently breaks answers.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Approve a tier 2 or higher strategy whose thresholds were not agreed before results were seen.
- Treat uncalibrated AI-assisted grading as evidence of quality.
- Let the maker define, run and pass their own evaluation alone.
- Claim that evaluation proves behaviour beyond the patterns it tested.

---
name: workflow-validation
description: Validates a Copilot Cowork task design or shared workflow before people rely on it, by running it on representative and deliberately awkward cases, planting errors before checkpoints and checking outputs against the definition of done, then recording a fit-to-rely verdict. Use when a task design is about to be shared or reused, when a step is moving from drafting to acting, or after a material change to a skill or its sources.
license: CC-BY-4.0
metadata:
  department: copilot-cowork
  lifecycle: Assure, Launch, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3
  platforms: copilot-cowork, m365-copilot
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality
  sources: ms-copilot-cowork-customise, ms-responsible-ai, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Workflow validation

## Purpose

A Cowork task that worked once has proved very little. It may have worked because the sources happened to be tidy that
week, because the delegator quietly fixed the output, or because the awkward case never came up. This skill gathers
enough evidence to decide whether a task design or shared workflow can be relied on: representative runs, awkward cases,
planted errors before checkpoints and an honest comparison with the definition of done. The result is a fit-to-rely
verdict with conditions. It goes wrong when validation is a demonstration on the best case rather than a test on the
cases that break things.

## When to use

- A task design is about to be published to a shared library or reused by a team.
- A delegated part is moving from drafting (D2) to acting with approval (D3).
- A skill, custom instruction, plugin or major source behind a workflow has changed.
- Users report that a previously reliable workflow has started producing poor results.

## When not to use

- Reviewing one finished output before it is used - use `copilot-cowork:delegated-work-review`.
- Testing a reusable agent's answers before release - use `m365-agents:agent-testing`.
- Designing the organisation's evaluation strategy for probabilistic systems - use `evaluation-quality:ai-evaluation-strategy`.
- Re-running evaluation after changes to a production AI solution - use `evaluation-quality:regression-evaluation`.
- Validating an application built with Copilot Code - use `copilot-code:application-validation`.

## Questions to ask first

1. What is the definition of done, and could two reviewers apply it to the same output and agree?
2. Which real instances of the work are typical, and which are the awkward ones: missing data, conflicting sources, unusual requests?
3. Who will rely on the workflow, and will they run it with the same access and sources as the person who built it?
4. Where are the checkpoints, and what error should each one catch?
5. What level of rework would the business owner accept before the workflow is judged not worth using?

## Required inputs

- The task design on the `cowork-task-design` template, including the delegation map, step outline, context and checkpoints.
- Source verdicts from `copilot-cowork:grounding-readiness`.
- The planted-error test list from `copilot-cowork:human-checkpoint-design`.
- A business owner willing to agree the acceptance threshold.

If no definition of done exists, stop and send the design back to `copilot-cowork:task-context-design`. Never validate
against a threshold the business owner has not agreed.

## Decision framework

Run a small, deliberate test set and judge against agreed criteria.

| Test set component | Minimum | Purpose |
|---|---|---|
| Typical cases | Three to five real instances | Shows ordinary performance |
| Awkward cases | Two or three: missing source, conflicting sources, unusual request | Shows behaviour at the edges |
| Planted errors | One per checkpoint | Shows each checkpoint catches what it should |
| Reuser run | At least one run by someone other than the designer | Shows the design works with different access and habits |

| Verdict | Criteria |
|---|---|
| Fit to rely | All typical cases meet the definition of done with edits within the agreed threshold; awkward cases are flagged rather than invented over; every planted error is caught |
| Fit with conditions | Minor misses with a named fix and a re-test date; no planted error missed |
| Not fit | Any planted error missed at a pre-effect checkpoint, invented content on an awkward case, or typical cases routinely beyond the threshold |

Scale the test set with risk tier: tier 1 needs the minimum; tier 2 and above adds more awkward cases and an independent
reviewer.

## Practitioner approach

Choose test cases from real work. Ask the team for the last five instances of the task and for the two that caused the
most trouble. Typical cases show whether the workflow helps; awkward cases show whether it is safe. A design tested only
on tidy cases will meet its first messy one in production.

Write down what a good output looks like for each case before running it, using the definition of done. This avoids the
common trap of judging the output by how plausible it reads. For awkward cases the expected behaviour is often a flag
rather than an answer: "sources disagree on the delivery date" is a pass, a confident date is a fail.

Plant errors deliberately. Before each checkpoint, introduce something the approver should catch: a wrong recipient, a
figure from a superseded file, a draft that names an individual it should not. Run the workflow and see whether the
checkpoint makes the error visible and whether the approver notices it. A checkpoint that misses a planted error in a
test will miss a real one when people are busy.

Have someone other than the designer run it. Designers unconsciously compensate for gaps they know about, and they often
have broader access than the people who will reuse the workflow. A run by a typical reuser exposes missing context,
different sources and unclear checkpoints.

Record what happened against each case: met, met with edits (and how much), flagged correctly, or failed. Count edits
honestly; a workflow whose outputs always need heavy rework may still be useful, but the business owner should decide
that with the evidence in front of them. Compare against the agreed threshold and give the verdict.

Feed failures back to the right design skill rather than patching wording: a missed source goes to grounding readiness,
a wrong judgement to the step outline, an unnoticed planted error to checkpoint design. Re-test after fixes. Store the
test cases with the task design so they can be re-run when a skill, plugin, custom instruction or key source changes,
and set a re-validation date.

## Outputs

- A validation record in the `cowork-task-design` template: test cases, expected behaviour, results, planted-error results, reuser run notes and edit levels.
- A fit-to-rely verdict (fit, fit with conditions, not fit) with conditions, owners and re-test dates.
- A reusable test set stored with the task design for re-validation after change.

## Microsoft platform considerations

Cowork behaviour can change with product updates and with changes to the plugins, skills and custom instructions it uses.
Keep test sets so they can be re-run after such changes, and check the source records (`ms-copilot-cowork-customise`)
for announced changes that may affect behaviour. Do not treat a past validation as permanent.

## Adoption considerations

A validated design is easier to promote and trust. Publish the verdict with the design so reusers know what was tested
and what conditions apply. Involve reusers in testing; they become credible advocates.

## Knowledge considerations

Many failures trace to sources rather than to Cowork. Record source-related failures separately and route them to
`copilot-cowork:grounding-readiness` and the source owners.

## Security and privacy considerations

Use test cases that do not expose personal or confidential data to people who should not see it. Where real cases contain
sensitive data, run tests within the intended audience or use cleaned copies, and remove test outputs afterwards.

## Responsible AI considerations

Awkward cases should include situations where the workflow could invent content about people or overstate certainty. A
design that invents rather than flags on such cases is not fit, whatever its typical performance.

## Evaluation requirements

This skill is the evaluation for Cowork task designs. From risk tier 2, its method and threshold are aligned with the
organisation's approach in `evaluation-quality:ai-evaluation-strategy` and quality criteria in `evaluation-quality:ai-quality-rubric`.

## Value measures

Track, at team level, the share of shared task designs validated before use, first-time acceptance in validation, and
how often re-validation finds a regression. Never use validation results to judge the people who ran the tests.

## Scale notes

### Starter

Five real cases, two awkward ones, one planted error per checkpoint and one run by a colleague is enough for most shared
designs.

### Scale

Make validation a requirement for the shared library, keep test sets with designs, and re-run them on a schedule and after
material changes.

### Enterprise

Business units validate their own designs to the shared standard; designs at risk tier 2 or above, and organisational
skills used widely, are validated with an independent reviewer from the evaluation function.

## Hand-offs

- To `copilot-cowork:cowork-governance` to publish a validated design to the shared library.
- To `copilot-cowork:delegated-work-review` with the review standard for live use.
- Back to `copilot-cowork:task-context-design`, `copilot-cowork:multi-step-work-design` or `copilot-cowork:human-checkpoint-design` with failures.
- To `evaluation-quality:ai-quality-rubric` from risk tier 2.

## Reviewer gates

From risk tier 2, `evaluation-quality` reviews the test set, threshold and results before a design is relied on.
Findings are blocking or advisory; a missed planted error at a pre-effect checkpoint is blocking.

## Failure modes

- Validation is a demonstration on the best case, so the first awkward real case fails in use.
- The designer runs every test with broader access than reusers, hiding missing context.
- Outputs are judged by how plausible they read rather than against the definition of done.
- A past validation is treated as permanent after a skill, plugin or source has changed.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Declare a workflow fit to rely on without awkward cases and planted errors.
- Move a delegated part to acting with approval without validation evidence.
- Expose real personal or confidential data to testers outside its intended audience.
- Use test results to assess the individuals who ran them.

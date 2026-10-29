---
name: ai-quality-rubric
description: Writes and reviews the quality rubric used to score AI outputs - dimensions with plain definitions, anchored scoring levels, zero-tolerance failures, pass thresholds agreed with the business owner before results, and calibration of human and AI-assisted graders - with findings classed blocking or advisory. Use when evaluators disagree on scores, when thresholds are being set, or when a rubric is submitted to the gate.
license: CC-BY-4.0
metadata:
  department: evaluation-quality
  lifecycle: Deliver, Assure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-cowork, copilot-studio, ai-foundry, copilot-code
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality
  sources: nist-ai-rmf, ms-responsible-ai, ms-foundry-models, ms-copilot-studio-guidance, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# AI quality rubric

## Purpose

Two reviewers looking at the same AI answer will often disagree on whether it is good, and an AI-assisted grader will
disagree with both in ways nobody has measured. A rubric turns "good enough" into dimensions with plain definitions,
anchored scoring levels, a short list of failures that are never acceptable and thresholds the business owner agrees
before seeing results. This reviewer skill writes rubrics and reviews those submitted by teams, classifying each finding
as blocking or advisory. Rubrics go wrong when the levels are vague ("mostly accurate"), when there are so many
dimensions that scoring becomes guesswork, or when the threshold is chosen after the results are in.

## When to use

- An evaluation plan names quality dimensions and they need scoring scales and thresholds.
- Human evaluators disagree on scores for the same outputs.
- A team proposes AI-assisted grading and needs a rubric the grader and humans can both apply.
- A rubric and threshold are submitted to the `evaluation-quality` gate.
- A business owner asks what pass rate is acceptable and wants help deciding.

## When not to use

- Choosing which dimensions and methods the solution needs at all - use `evaluation-quality:ai-evaluation-strategy`.
- Building the items to be scored - use `evaluation-quality:golden-dataset`.
- Detailed checks of whether claims are supported by sources and citations - use `evaluation-quality:groundedness-testing`.
- Measuring the business effect of AI on quality of work, rework and error rates - use `value-realisation:quality-measurement`.
- Assessing people's skills or evidence for learning - use `learning-and-skills:learning-evidence-rubric`.

## Questions to ask first

1. For each dimension, what does an unacceptable, acceptable and excellent output look like, in an example the business owner recognises?
2. Which failures must count as an automatic fail regardless of the overall score?
3. Who will score - subject experts, users, an AI-assisted grader or a mix - and how will their agreement be checked?
4. What pass rate per dimension would the business owner accept for release, and why that figure?
5. Does any dimension need to be scored separately for different user groups or content types?

## Required inputs

- The evaluation plan with dimensions, risk tier and consequence statement.
- A sample of real outputs from the solution, including some poor ones, to anchor the levels.
- The business owner, available to agree thresholds before results are seen.
- Behaviour rules from the brief, including refusal and tone requirements.

Where no real outputs exist yet, draft anchors from the brief and mark them provisional; recalibrate after the first run
before any threshold decision.

## Decision framework

Use few dimensions with three or four anchored levels. More levels add disagreement, not precision.

| Dimension | Fail | Partial | Pass |
|---|---|---|---|
| Correct | Wrong in substance, or would mislead a reasonable user | Right in substance but missing an element the user needed | Right and complete for the question asked |
| Grounded | Claims not supported by any permitted source | Supported, but citation missing or imprecise | Supported, with a citation to the right source |
| Appropriate | Out of scope, wrong tone, or answers what it should redirect | In scope with minor tone or format issues | In scope, right tone, refuses and redirects as specified |
| Safe | Harmful, restricted or unsafe content | Not applicable; safety is pass or fail | No harmful, restricted or unsafe content |

Add dimensions only when the evaluation plan requires them, such as action correctness or consistency across runs.

Thresholds and zero-tolerance rules:

| Rule | Guidance |
|---|---|
| Threshold per dimension | A pass rate per dimension, not one blended score, so a weak dimension cannot hide behind a strong one |
| Zero-tolerance list | A single occurrence fails the run, for example exposing restricted content, unsafe advice, acting without confirmation |
| Agreement before results | Thresholds signed and dated by the business owner before the first scored run |
| Grader calibration | Human graders agree on a shared sample before scoring alone; an AI-assisted grader is compared with human scores and its disagreement recorded |

When reviewing a submitted rubric, classify each finding.

| Finding | Blocking from tier 2 when | Advisory when |
|---|---|---|
| Anchors | Levels undefined or defined only by adjectives | Anchors lack examples for one dimension |
| Thresholds | Blended single score, or set after results | Rationale for a threshold not recorded |
| Zero-tolerance | Absent for a solution that acts, handles restricted content or advises on safety | List exists but omits a lower-impact case |
| Calibration | AI-assisted scores used as evidence without comparison to human scores | Human calibration sample small |

## Practitioner approach

Write the rubric with real outputs on the table. Take a handful of answers from the solution, including clearly poor
ones, and ask the business owner and a subject expert to sort them into fail, partial and pass for each dimension.
Turn their reasons into the anchor wording. Anchors written in the abstract drift; anchors written from examples hold.

Keep the scoring unit clear. Decide whether a multi-part answer is scored as a whole or per part, whether repeated runs
of the same item are scored separately, and how a correct answer with a wrong citation is treated. Write each rule into
the rubric so two graders reach the same result.

Calibrate the graders before they score alone. Give every human grader the same small sample, compare scores, discuss
the disagreements and tighten the anchors where they caused confusion. Repeat until agreement is good enough for the
risk tier, and record the result. If an AI-assisted grader will be used, give it the same rubric and compare its scores
with the calibrated human scores. Record where it is lenient or harsh. Use it to scale review only where its
disagreement is understood, and keep a human-scored sample in every run.

Set thresholds with the business owner, per dimension, before results. Anchor the conversation in the consequence
statement: if wrong answers are always checked by an expert, a lower correctness threshold may be acceptable; if users
act directly on answers, it must be higher. Do not import thresholds from another solution without that conversation.
Agree the zero-tolerance list in the same meeting and record the date.

Present results per dimension, with the zero-tolerance breaches listed separately and the grader agreement shown
alongside. A pass rate without the agreement figure invites false confidence.

Revisit the rubric when the solution's purpose or audience changes, when graders start disagreeing again, or when live
feedback shows the rubric is passing answers users find unhelpful. Version it alongside the golden dataset so results
remain comparable.

## Outputs

- A quality rubric: dimensions, plain definitions, anchored levels with examples, scoring rules and zero-tolerance list, recorded in the `evaluation-plan`.
- Thresholds per dimension, signed and dated by the business owner before the first scored run.
- A calibration record for human graders and any AI-assisted grader.
- A rubric review record with findings classified blocking or advisory, the fix and an owner.

## Microsoft platform considerations

Copilot Studio and Microsoft Foundry offer evaluation features that can apply criteria or AI-assisted graders to
outputs; what they measure and how they are configured changes over time. Map platform metrics to the rubric's
dimensions explicitly, confirm current behaviour in `ms-copilot-studio-guidance` and `ms-foundry-models`, and do not
assume a platform metric means the same as a rubric dimension of the same name.

## Adoption considerations

Share the rubric's plain definitions with users at launch. When people know what "good" means for the solution, their
feedback becomes far more useful.

## Knowledge considerations

Groundedness and correctness anchors depend on which sources are authoritative. Name them in the rubric so graders
do not reward answers drawn from superseded or unofficial content.

## Security and privacy considerations

The safety dimension must include exposure of restricted or personal content as a zero-tolerance failure from tier 2,
aligned with `security-privacy:data-exposure-review`. Graders see real outputs, so limit grading to people entitled to
the underlying content.

## Responsible AI considerations

Where outputs affect people, add a dimension or zero-tolerance rule agreed with `responsible-ai:fairness-review`, and
score samples across the groups affected. Rubrics measure outputs, not individuals; never adapt one to score staff.

## Evaluation requirements

This skill defines how evaluation is scored. Minimum from tier 2: anchored levels per dimension, per-dimension thresholds
dated before results, a zero-tolerance list, and a calibration record for every grader whose scores count as evidence.

## Value measures

Track grader agreement over time, the share of releases where thresholds were agreed before results, and the rate of
live complaints about answers the rubric passed. The AI Evaluation Lead owns these measures at solution level; never
report individual graders' accuracy.

## Scale notes

### Starter

Three dimensions with three levels, one example per level, and thresholds agreed by email with the business owner
before testing. Two people calibrate on ten outputs.

### Scale

A shared rubric library by solution type with standard anchors, local examples and a calibration step at the start of
each evaluation cycle. AI-assisted grading introduced only with a recorded comparison.

### Enterprise

Central rubric standards owned by the `evaluation-quality` department, federated graders trained to them, periodic
cross-unit calibration and a recorded comparison for every AI-assisted grader in use.

## Hand-offs

- To `m365-agents:agent-testing`, `copilot-studio:studio-testing-and-evaluation` or `ai-engineering:evaluation-harness` to apply the rubric.
- To `evaluation-quality:groundedness-testing` and `evaluation-quality:ai-safety-testing` for specialist dimensions.
- To `evaluation-quality:ai-release-evidence` with the thresholds and calibration record.

## Reviewer gates

This skill operates within the `evaluation-quality` gate. From risk tier 2 a rubric with blocking findings cannot be
used to support release; below tier 2 findings are advisory. Disagreement over thresholds escalates to the accountable
executive for written risk acceptance; the maker cannot lower a threshold.

## Failure modes

- Levels described by adjectives only, so graders score by mood and results cannot be repeated.
- A blended score lets an unsafe or ungrounded answer pass because the others were good.
- An AI-assisted grader is lenient on fluent but wrong answers, and nobody checked.
- The threshold is lowered quietly after the first run to match the result.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Accept a threshold set or changed after results were seen.
- Combine dimensions into a single score that lets a safety or grounding failure pass.
- Use an AI-assisted grader as evidence without a recorded comparison against human scores.
- Use a solution rubric to score or rank the people who built or tested it.

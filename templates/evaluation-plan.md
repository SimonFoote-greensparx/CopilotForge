# Evaluation plan

Template id: `evaluation-plan`

Responsible skill: `evaluation-quality:ai-evaluation-strategy`. The dataset section is completed with
`evaluation-quality:golden-dataset`, the rubric and thresholds with `evaluation-quality:ai-quality-rubric`, and the
results summary is reviewed with `evaluation-quality:ai-release-evidence`.

Complete this plan before formal testing starts, and update it after every material change. Every fact the organisation
must supply is marked `[To confirm: ...]`. Example rows are fictional. Thresholds must be agreed and dated before any
results are seen; a threshold changed after results is a blocking finding at the `evaluation-quality` gate from risk
tier 2.

## 1. Solution and consequence

| Field | Entry |
|---|---|
| Solution name and reference | [To confirm] |
| Route (for example Agent Builder, Copilot Studio, Microsoft Foundry, Cowork workflow) | [To confirm] |
| Risk tier and date classified | [To confirm] |
| Business owner (role) | [To confirm] |
| Evaluation lead (role) | [To confirm] |
| Configuration version under evaluation | [To confirm] |
| Consequence statement - what happens when the solution is wrong, who notices and how quickly | [To confirm] |

Fictional example consequence statement: "Staff act directly on leave entitlement answers without checking; a wrong
answer can lead to an incorrect booking that HR must reverse."

## 2. Quality dimensions and methods

| Dimension | Plain definition | Method (human review, automated check, calibrated AI-assisted grading, red team) | Who judges |
|---|---|---|---|
| Correct | [To confirm] | [To confirm] | [To confirm: role] |
| Grounded | [To confirm] | [To confirm] | [To confirm: role] |
| Appropriate | [To confirm] | [To confirm] | [To confirm: role] |
| Safe | [To confirm] | [To confirm] | [To confirm: role] |
| Other required by tier (consistency, action correctness, fairness) | [To confirm, or not applicable with reason] | [To confirm] | [To confirm] |

## 3. Dataset

| Item | Entry |
|---|---|
| Golden dataset name, version and location (restricted) | [To confirm] |
| Size and items per category (core, edge, refusal, knowledge silent, contradiction, adversarial, held out) | [To confirm] |
| Share of items sourced from real users | [To confirm] |
| Expected answers confirmed by (role) and date | [To confirm] |
| Regression subset identified | [To confirm] |
| Personal or confidential data handling | [To confirm: for example fictional details only; access limited to evaluators] |

## 4. Rubric, thresholds and zero-tolerance failures

| Dimension | Rubric version | Pass threshold | Rationale |
|---|---|---|---|
| Correct | [To confirm] | [To confirm] | [To confirm] |
| Grounded | [To confirm] | [To confirm] | [To confirm] |
| Appropriate | [To confirm] | [To confirm] | [To confirm] |
| Safe | [To confirm] | [To confirm] | [To confirm] |

| Item | Entry |
|---|---|
| Zero-tolerance failures | [To confirm: for example exposing restricted content, unsafe advice, acting without confirmation] |
| Thresholds agreed by (business owner role) | [To confirm] |
| Date thresholds agreed (must precede first scored run) | [To confirm] |
| Grader calibration approach and record location | [To confirm] |

## 5. Specialist testing

| Test | Required at this tier? | Owner | Record location |
|---|---|---|---|
| Groundedness testing | [To confirm] | [To confirm] | [To confirm] |
| Safety testing | [To confirm] | [To confirm] | [To confirm] |
| Red-team exercise (tier 3 and 4) | [To confirm] | [To confirm] | [To confirm] |
| Permission-trimming tests (evidence for security and privacy) | [To confirm] | [To confirm] | [To confirm] |
| Fairness items agreed with responsible AI reviewers | [To confirm, or not applicable with reason] | [To confirm] | [To confirm] |

## 6. Cadence and regression triggers

| Item | Entry |
|---|---|
| Events that trigger re-evaluation | [To confirm: for example instruction change, knowledge change, new action, model or platform change] |
| Scope of re-run per event | [To confirm] |
| Normal variation between identical runs | [To confirm: measured at baseline] |
| Scheduled re-evaluation | [To confirm: frequency] |
| Live quality sampling after release (size, frequency, who scores) | [To confirm] |

## 7. Known limits

What this evaluation does not show, and how monitoring and feedback will cover it.

[To confirm]

## 8. Results summary

| Run date | Configuration version | Dataset version | Correct | Grounded | Appropriate | Safe | Zero-tolerance breaches | Decision |
|---|---|---|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

Fictional example row: "Run 3; config v1.4; dataset v2; correct 91%, grounded 94%, appropriate 98%, safe 100%; no
breaches; meets thresholds."

## 9. Review and sign-off

| Role | Decision | Date |
|---|---|---|
| Evaluation lead | Plan approved / Changes required | [To confirm] |
| Business owner | Thresholds agreed | [To confirm] |
| `evaluation-quality` reviewer (tier 2 and above) | Pass / Pass with advisory findings / Blocked | [To confirm] |

| Finding | Blocking or advisory | Fix | Owner | Status |
|---|---|---|---|---|
| [To confirm] | Blocking / Advisory | [To confirm] | [To confirm] | [To confirm] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

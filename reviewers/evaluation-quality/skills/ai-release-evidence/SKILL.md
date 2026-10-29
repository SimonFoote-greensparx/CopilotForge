---
name: ai-release-evidence
description: Assembles and reviews the evaluation evidence pack an AI solution needs at its release gate - plan, dataset and rubric versions, thresholds dated before results, results per dimension, groundedness, safety and red-team outcomes, known limits and monitoring baseline - and gives the evaluation-quality verdict with findings classed blocking or advisory. Use when a tier 2 or higher solution or material change seeks release.
license: CC-BY-4.0
metadata:
  department: evaluation-quality
  lifecycle: Assure, Launch
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-cowork, copilot-studio, ai-foundry, copilot-code, power-platform
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality
  sources: nist-ai-rmf, iso-iec-42001, ms-responsible-ai, ms-copilot-studio-guidance, ms-foundry-models, ms-coe-starter-kit
  status: draft
  authors: Simon Foote
---

# AI release evidence

## Purpose

At the release gate, someone has to decide whether the evaluation behind an AI solution is good enough to rely on.
That decision is only as good as the evidence in front of them. This reviewer skill assembles the evaluation evidence
pack - what was tested, how, against what thresholds, with what results and what remains unknown - and gives the
`evaluation-quality` verdict, classifying each finding as blocking or advisory. Release evidence goes wrong when it is a
summary slide that says "testing passed", when thresholds and results cannot be tied to a dataset version, or when
known limits are left out because they look bad.

## When to use

- A solution at tier 2 or above is ready for its release decision and needs the `evaluation-quality` verdict.
- A material change to a live solution needs a fresh release decision.
- A solution's audience is about to widen into a higher risk tier.
- An auditor, risk committee or accountable executive asks what evidence supported a release.

## When not to use

- Running the overall release gate across owner, support, sharing and all reviewers - use `m365-agents:agent-release-readiness`.
- Setting the organisation's release rules by risk tier - use `platform-governance:ai-release-policy`.
- Executive acceptance of residual risk - use `responsible-ai:ai-risk-acceptance`.
- Producing the underlying evaluation results - use `m365-agents:agent-testing` or the relevant `evaluation-quality` testing skill.
- Deciding whether to scale or stop after a pilot - use `opportunity-management:scale-or-stop`.

## Questions to ask first

1. What exactly is being released - which configuration, knowledge, actions and audience - and at which risk tier?
2. Which evaluation plan applied, and was it approved before testing started?
3. Were thresholds agreed and dated before results were seen, and by whom?
4. What does the evidence not cover, and how will monitoring cover that gap after release?
5. Which other reviewer gates apply, and has their evidence been cross-referenced?

## Required inputs

- The approved `evaluation-plan` with thresholds and zero-tolerance list.
- Dataset, rubric and configuration versions used for the results.
- Results per dimension, groundedness and safety records, and red-team findings at tier 3 and 4.
- Regression results for material changes.
- The monitoring baseline and live sampling plan from operations.

Where any required item is missing for the tier, the verdict is "blocked - evidence incomplete". Never infer a pass from
a summary, and never accept evidence promised for after release.

## Decision framework

The pack must contain these items for the tier.

| Evidence | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Evaluation plan approved before testing | Recommended | Required | Required | Required |
| Thresholds dated before results | Owner note | Required | Required | Required, accepted by executive |
| Dataset, rubric and configuration versions | Recommended | Required | Required | Required |
| Results per dimension with grader calibration | Owner sign-off | Required | Required | Required, independent evaluators |
| Groundedness record | Not required | Required for grounded solutions | Required | Required |
| Safety record | Not required | Required for broad audiences | Required | Required |
| Red-team findings log and coverage | Not required | Not required | Required | Required, independent members |
| Known limits statement | Recommended | Required | Required | Required, published to users |
| Monitoring baseline and sampling plan | Not required | Required | Required | Required with triggers |

The verdict is one of: pass; pass with advisory findings; blocked.

| Finding | Blocking from tier 2 when | Advisory when |
|---|---|---|
| Missing evidence | A required item for the tier is absent | A recommended item is absent |
| Threshold integrity | Thresholds dated after results or changed without owner agreement | Rationale for a threshold not recorded |
| Results | Any dimension below threshold, or any zero-tolerance breach unresolved | Dimension above threshold but trending down across runs |
| Traceability | Results cannot be tied to dataset, rubric and configuration versions | Version recorded but change log incomplete |
| Known limits | Material limits omitted from the statement | Limits stated but hard for users to find |

## Practitioner approach

Assemble the pack from primary records, not summaries. For each item, attach or link the actual plan, dataset version,
rubric, results sheet, groundedness and safety records and red-team log. A reviewer must be able to open any figure and
trace it to the items and outputs behind it.

Check integrity before quality. Confirm the evaluation plan was approved before testing, and that thresholds carry a
date and an owner earlier than the first scored run. Confirm results were produced on the configuration being released;
a pass on last week's configuration is not evidence for this week's. Check that grader calibration is recorded for every
grader whose scores count, including any AI-assisted grader.

Then read the results. Compare each dimension with its threshold, list every zero-tolerance breach and its resolution,
and look at trends across runs rather than only the latest. For grounded solutions, check that claim-level support and
silence handling were tested, not just citation presence. For tier 3 and 4, confirm blocking red-team findings were
fixed and re-tested.

Write the known limits statement in plain language: topics the solution handles poorly, questions it will refuse, the
kinds of error seen in testing and how users should check important answers. This statement is for users as much as
for the gate. Omitting a limit because it looks bad is itself a blocking finding.

Confirm that operations can see what evaluation could not. The monitoring baseline should name the live quality signals
and the sampling plan that will catch failures the dataset missed, with an owner.

Cross-reference the other gates. Note the `security-privacy` evidence used (permission tests, action tests) and the
`responsible-ai` outcomes from tier 3, without re-reviewing them; your verdict covers evaluation only.

Give the verdict with each finding classified, the risk behind it, the specific fix and an owner. Be proportionate: a
tier 2 agent with complete evidence and two thin areas passes with advisory findings. Record the verdict on the release
checklist, and keep the pack with the solution's record so the next owner or an auditor can see what was known at
release.

## Outputs

- A release evidence pack indexed against the tier table, with links to primary records and the results section of the `evaluation-plan`.
- The `evaluation-quality` verdict - pass, pass with advisory findings, or blocked - with classified findings, fixes and owners.
- The test evidence section of the `agent-release-checklist` for agents, completed or verified.
- A plain-language known limits statement for users.

## Microsoft platform considerations

Evaluation results exported from Copilot Studio, Microsoft Foundry or other routes should be stored with the
configuration and version they were produced on; platform reports change format and retention over time. Confirm
current export and retention options in `ms-copilot-studio-guidance` and `ms-foundry-models`, and use the solution
inventory, for example one built with the CoE Starter Kit (`ms-coe-starter-kit`), to link evidence to the solution record.

## Adoption considerations

The known limits statement is an adoption asset. Users who know where a solution is weak use it well; users who discover
weaknesses for themselves stop using it.

## Knowledge considerations

Record the knowledge versions the evidence reflects. If knowledge changes between evaluation and release, the evidence
is stale for affected topics and a regression run is needed.

## Security and privacy considerations

The pack may contain real outputs with confidential content; store it with access limited to reviewers and owners.
Reference `security-privacy` evidence rather than copying sensitive detail into the pack.

## Responsible AI considerations

From tier 3, the pack is an input to `responsible-ai:ai-risk-acceptance`. Make residual evaluation uncertainty explicit
so the accountable executive accepts a known risk rather than an assumed pass.

## Evaluation requirements

This skill reviews the evaluation as a whole. The minimum is every required item for the tier present, traceable to
versions, with thresholds dated before results and no unresolved zero-tolerance breach.

## Value measures

Track the share of releases with complete evidence at first submission, time from submission to verdict, and live
incidents in areas the pack declared as tested. The AI Evaluation Lead reports by solution and portfolio, never by
maker or reviewer.

## Scale notes

### Starter

One page per release listing the evaluation set, thresholds with date, results, known limits and owner sign-off,
attached to the agent release checklist.

### Scale

A standard evidence pack index across solutions, reviewed in the CoE release cadence, with packs stored against the
solution inventory.

### Enterprise

Evidence packs held in a managed repository linked to the inventory and risk register, sampled by internal audit, with
federated reviewers for tier 2 and central review for tier 3 and 4.

## Hand-offs

- To `m365-agents:agent-release-readiness` or the relevant release gate with the verdict.
- To `responsible-ai:ai-risk-acceptance` from tier 3 with residual uncertainty.
- To `ai-operations:ai-solution-monitoring` with the monitoring baseline and known limits.
- Back to the testing skills with blocking findings to resolve.

## Reviewer gates

This skill is the `evaluation-quality` release verdict. It is blocking from risk tier 2 and advisory below it. Blocking
findings stop release and are not traded against dates; disagreement escalates to the accountable executive for written
risk acceptance, recorded with the pack.

## Failure modes

- A summary saying "testing passed" is accepted without the records behind it.
- Results came from an earlier configuration and the released version was never evaluated.
- Known limits are left out, users discover them in live use and trust collapses.
- The verdict is treated as the whole release decision, and other gates are skipped.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Pass a tier 2 or higher release on summaries without primary records.
- Accept evidence produced on a different configuration from the one being released.
- Omit known limits from the pack or the user statement.
- Accept a promise that evidence will be supplied after release.

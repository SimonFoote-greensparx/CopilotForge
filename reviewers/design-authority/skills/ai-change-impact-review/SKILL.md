---
name: ai-change-impact-review
description: Reviews the impact of a proposed change to a live AI solution - instructions, knowledge, model, actions, identity, audience, channel or platform - classifying the change as minor, material or re-design, naming the re-tests and re-reviews triggered, and recording findings as blocking or advisory. Use when a live agent or solution is about to change, when Microsoft retires a model or feature it depends on, or when audience is widening.
license: CC-BY-4.0
metadata:
  department: design-authority
  lifecycle: Improve, Assure, Scale
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, power-platform, copilot-cowork, azure
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-foundry-models, ms-copilot-studio-guidance, ms-agents-extensibility, ms-declarative-agents, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI change impact review

## Purpose

AI solutions change more often and more subtly than ordinary software. A sentence added to instructions, a new knowledge
source, a model version retired by the provider or an audience widened by sharing can each change behaviour across every
conversation. This reviewer skill assesses a proposed change to a live solution, classifies it as minor, material or
re-design, names the re-tests and re-reviews it triggers, and records findings as blocking or advisory. Change reviews
go wrong when instruction and knowledge changes are treated as content edits rather than behaviour changes, and when
model updates are applied without regression evaluation.

## When to use

- A live agent's instructions, knowledge sources, actions or model are about to change.
- Microsoft or a model provider is retiring a model, version or feature a solution depends on.
- A solution's audience or channels are about to widen.
- An incident fix needs a change to a live solution.
- Several small changes have accumulated since the last review.

## When not to use

- Running regression evaluation after a change - use `evaluation-quality:regression-evaluation`.
- Re-classifying the risk tier - use `opportunity-management:risk-classification`.
- Setting the organisation's release and change rules - use `platform-governance:ai-release-policy`.
- Keeping knowledge current as routine operation - use `ai-operations:knowledge-refresh`.
- Reviewing a new solution's design - use `design-authority:ai-design-review`.

## Questions to ask first

1. What exactly is changing, and why?
2. Which users, conversations or actions could behave differently after the change?
3. Does the change alter audience, data reached, actions taken, identity used or autonomy?
4. What evidence from before the change can be compared with after - evaluation set, monitoring baseline?
5. How would the change be rolled back if it goes wrong?

## Required inputs

- The change request: what, why, who requested it and the proposed date.
- The solution's current design record, risk tier and release record.
- The evaluation set and thresholds, and recent monitoring data.
- Any provider notice of retirement or change, with its date, from the source records.

If the solution has no evaluation set, any change beyond minor is reviewed as material until one exists; never accept
"it looked fine in testing" as regression evidence from tier 2.

## Decision framework

Classify the change, then apply the triggers.

| Class | Typical changes | Triggers |
|---|---|---|
| Minor | Wording fixes in instructions with no scope change; replacing a document with its newer version from the same owned source; cosmetic changes | Owner sign-off; spot-check against the evaluation set |
| Material | New or removed knowledge source; instruction change affecting scope, tone or refusal; model or version change; new or changed action; changed identity; audience widened within the tier | Regression evaluation against thresholds; re-review by affected gates; release per policy |
| Re-design | Risk tier changes; new channel outside the organisation; new autonomy; platform change; actions affecting people | Re-classification; full design review; all gates for the new tier |

Findings:

| Finding | Blocking when (tier 2 and above) | Advisory when |
|---|---|---|
| Misclassified change | A material or re-design change is presented as minor | Classification arguable, with tests that cover both |
| Regression evidence | No comparison against the evaluation set for a material change | Evaluation run, minor drops within tolerance explained |
| Re-review | An affected gate (security, responsible AI) is not re-engaged | Re-engaged but not yet concluded for a low-risk element |
| Rollback | No way to restore the previous version | Rollback manual but documented |
| Provider retirement | The solution will stop working on a known date with no plan | Plan exists but is not yet tested |

Disagreement escalates to the accountable executive for written risk acceptance.

## Practitioner approach

Start by describing the change in behavioural terms, not technical ones. "Adding the procurement policy library" becomes
"the agent will now answer purchasing questions for all staff, using content previously available only to procurement".
The behavioural description usually makes the classification obvious.

Check the change against the dimensions that raise risk: audience, data reached, actions, identity and autonomy. A change
that touches any of them is at least material; one that changes the risk tier is a re-design. Instruction changes
deserve particular care, because a single sentence can widen scope or remove a refusal.

Treat model and version changes as material by default. Even when a provider describes a new version as an improvement,
behaviour on the organisation's own questions can change. Require regression evaluation against the existing set and
thresholds, and compare refusal and groundedness, not only overall quality.

Plan for provider retirements early. Keep an eye on notices for models and features the portfolio depends on, through
the source records. A retirement date is a deadline for a material change, and leaving it late turns a planned change
into an incident.

Re-engage the gates that the change affects, not all of them. A new knowledge source needs the security exposure check
and knowledge readiness; a new action needs the connector review; a widened audience needs re-classification. Record
which gates were re-engaged and why the others were not.

Confirm rollback. Before a material change goes live, the owner should be able to restore the previous version of the
instructions, knowledge configuration or model deployment. Where the platform makes this hard, record the manual
procedure.

Watch accumulation. Several minor changes can add up to a material one. Where many changes have been made since the
last review, look at the cumulative effect against the original design.

Record the classification, triggers, findings and verdict, and update the solution's design record so the next review
starts from the current state.

## Outputs

- A change impact record, using the change section of the `design-review-record`: change, behavioural description, classification, triggers, findings classified as blocking or advisory with fix and owner, and verdict.
- A list of gates re-engaged and evaluation required.
- An updated design record and release log entry.

## Microsoft platform considerations

Model catalogues, versions, retirement schedules and agent features change frequently. Use `ms-foundry-models` for
model lifecycle and retirement, and `ms-copilot-studio-guidance`, `ms-agents-extensibility` and `ms-declarative-agents`
for agent changes and ALM, and check them at the time of each review.

## Adoption considerations

Users notice behaviour changes. For material changes, tell users what has changed and why, so a new refusal or a new
capability does not undermine trust.

## Knowledge considerations

Knowledge changes are the most frequent material change. Coordinate with knowledge owners so routine updates within an
owned source stay minor, and additions of new sources are reviewed.

## Security and privacy considerations

New sources, actions, identities or audiences re-engage the `security-privacy` review. Data exposure can change without
any change to the agent, for example when source permissions change; share such signals with the solution owner.

## Responsible AI considerations

Changes that affect how a solution treats people, or that increase autonomy, re-engage the `responsible-ai` review from
tier 3 and may change the risk tier.

## Evaluation requirements

Material changes require regression evaluation against the existing set and thresholds, run through
`evaluation-quality:regression-evaluation`, with results compared to the last release.

## Value measures

At portfolio level, track changes by class, incidents following changes, changes released without required evaluation,
and provider retirements handled before their date. The design authority chair owns these measures, with a baseline
from the first quarter.

## Scale notes

### Starter

The owner classifies changes using the table and asks the CoE lead for a second view on anything material.

### Scale

Route material changes through the design authority with lightweight review, and keep a change log per solution.

### Enterprise

Integrate with enterprise change management, automate regression evaluation in pipelines, and track provider retirements
across the portfolio centrally.

## Hand-offs

- To `evaluation-quality:regression-evaluation` for regression testing.
- To `opportunity-management:risk-classification` when the change may alter the tier.
- To `design-authority:ai-design-review` for re-design changes.
- To `platform-governance:ai-release-policy` for release of the changed solution.

## Reviewer gates

This skill is part of the `design-authority` gate for live solutions, blocking from risk tier 2 for material and
re-design changes and advisory below. It re-engages `security-privacy`, `evaluation-quality` and `responsible-ai` as the
change requires. Disagreement escalates to the accountable executive for written risk acceptance.

## Failure modes

- An instruction change is treated as a content edit, widens the agent's scope and goes live untested.
- A model version is updated automatically and refusal behaviour changes without anyone noticing.
- A provider retirement date arrives with no plan, and the solution fails.
- Many minor changes accumulate into a different solution that was never reviewed.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Treat a model or version change as minor without regression evidence.
- Release a material change without a way to roll back.
- Let audience or autonomy widen through a change without re-classifying the risk tier.
- Trade a blocking finding against a change date.

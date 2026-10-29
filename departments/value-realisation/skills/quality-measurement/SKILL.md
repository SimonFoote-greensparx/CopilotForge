---
name: quality-measurement
description: Measures how AI-assisted work changes business quality after launch - accuracy, rework, errors reaching customers, compliance exceptions and consistency - through sampled review against a rubric, operational defect data and comparison with unassisted work. Use when a sponsor asks whether AI-assisted work is better or only faster, when rework or complaints rise after launch, or when productivity gains need a quality guard.
license: CC-BY-4.0
metadata:
  department: value-realisation
  lifecycle: Deliver, Launch, Measure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-code, copilot-studio, ai-foundry
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality
  sources: nist-ai-rmf, ms-responsible-ai, ms-copilot-studio-guidance, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# Quality measurement

## Purpose

AI can make work faster and worse at the same time, and speed is much easier to see. This skill measures the quality of
the business output that people produce with AI assistance - letters, case decisions, summaries, code, reports - in
live operation, against the same standard applied to unassisted work. It turns quality into a benefit where it improves
and a guard where it might slip. It goes wrong when quality is assumed from release testing, when nobody looks at
errors that reach customers, and when sampled review is so small or so informal that it proves nothing.

## When to use

- A benefit claims better accuracy, consistency or fewer errors and needs a measurement method.
- A productivity benefit needs a quality guard so speed is not bought with mistakes.
- Rework, complaints or compliance exceptions rise after an AI-assisted process goes live.
- A sponsor asks whether AI-assisted work is better or just faster.
- A solution has passed release evaluation and the organisation wants to know how it performs in real work.

## When not to use

- Evaluating an agent or model before release against a test set - use `evaluation-quality:ai-evaluation-strategy`.
- Building the rubric and thresholds for release evaluation - use `evaluation-quality:ai-quality-rubric`.
- Checking the quality of data an AI solution consumes - use `data-governance:ai-data-quality`.
- Measuring time and throughput effects - use `value-realisation:productivity-measurement`.
- Collecting and acting on user feedback about a live solution - use `ai-operations:ai-feedback-loop`.

## Questions to ask first

1. What does "good" look like for this output today, and is it written down anywhere (a checklist, a standard, an audit criterion)?
2. Where do errors surface now - reviewer corrections, rework, complaints, audit findings, reopened cases - and are they recorded?
3. What is the current error and rework rate for unassisted work, and from which baseline design?
4. Who is qualified to judge quality, and can they review a sample without knowing whether AI was used?
5. What is the cost of an error reaching a customer, a regulator or a decision about a person?

## Required inputs

- The registered quality benefit or the productivity benefit needing a guard, from `value-realisation:benefit-hypothesis`.
- The baseline error and rework rates from `value-realisation:baseline-design`.
- A written quality standard for the output, or agreement from the owner to create one.
- The solution's release evaluation results and rubric, where one exists.
- Access to defect, complaint, correction and audit data, agreed with its owner.

Where no written standard exists, draft a short rubric with the owner before measuring anything, and record it as
provisional. Never infer live quality from release test results alone.

## Decision framework

Choose measures from at least two of the four sources, and set a guard threshold for any quality measure attached to a
productivity benefit.

| Source | Typical measures | Notes |
|---|---|---|
| Sampled expert review | Share of outputs meeting the rubric; severity of errors found | Blind where feasible; same rubric for assisted and unassisted work |
| Operational defects | Rework rate, reopened cases, corrections before issue, first-time-right rate | Usually already recorded; check the definition is stable |
| Downstream impact | Complaints, appeals upheld, audit findings, incidents | Lagging but closest to real harm |
| Consistency | Variation in outputs for similar inputs; adherence to templates and policy | Often a genuine AI benefit; measure it explicitly |

| Situation | Sample and threshold approach |
|---|---|
| Tier 0-1, internal drafts | Small periodic sample; guard is "no worse than baseline" |
| Tier 2, shared or customer-facing | Regular sample sized with the owner; guard set as a maximum error rate agreed in advance |
| Tier 3-4, informs decisions about people, money or safety | Larger, more frequent sample including severity grading; any severe error triggers review |

## Practitioner approach

Start with the definition of good. Ask the owner and an experienced practitioner to write down what makes this output
acceptable, in five to ten criteria, and what makes an error minor, significant or severe. Use the organisation's
existing standards where they exist. If release evaluation used a rubric, reuse it so live and release quality can be
compared, but check it covers the business consequences, not only answer correctness.

Measure assisted and unassisted work against the same rubric. Draw a sample of each from the same period and, where
possible, have reviewers grade them without knowing which is which. Without this comparison the organisation learns how
good AI-assisted work is, but not whether AI made it better or worse.

Use the defect data the organisation already has. Reopened cases, corrections at approval, returned documents and
complaints are often recorded, and they are cheaper and less biased than new review. Check that their definitions did
not change at launch, and watch for a hidden effect: if reviewers correct AI drafts before issue, the error rate at
issue may look fine while correction effort rises. Measure both.

Look for consistency effects. One of the most reliable benefits of AI-assisted drafting is that outputs follow the
template, cite the right policy and use the same language. Measure that explicitly; it is often worth more than speed
in regulated or customer-facing work.

Set guard thresholds before launch and act on them. A guard is the maximum quality decline the owner will accept in
exchange for a productivity gain, and for high-impact work that may be none at all. When a guard is breached, the
productivity benefit is suspended until the cause is found, and the solution owner is told. Route model or knowledge
causes to the solution team and its evaluation owner, and process causes, such as skipped verification, to the owner
and the adoption team.

Keep reviews about outputs, not people. Report results by team, scenario or solution, never by named author, and
avoid any design that would let a manager reconstruct individual error rates.

Finally, report quality beside productivity in every value report. A dashboard that shows hours released without
quality lets the organisation discover the cost through complaints instead.

## Outputs

- A quality measurement plan per benefit or guard: rubric reference, sources, sample design, frequency, reviewers (roles) and guard threshold.
- Results recorded in the `benefits-register`: assisted versus unassisted quality, error severity profile, consistency measures and confidence.
- A guard breach log with cause, routing and outcome.
- A provisional rubric where no quality standard existed.

## Microsoft platform considerations

Copilot Studio and Microsoft Foundry provide analytics and evaluation capabilities that help explain why quality moves,
for example unanswered questions or citation behaviour. They describe the AI component, not the business output after
human editing, so they complement this skill rather than replace it. Capability and availability change; check
`references/sources.md`.

## Adoption considerations

Falling quality is often an adoption symptom: people accept drafts without checking once they become familiar. Share
team-level findings with the adoption lead so verification habits are reinforced, without blaming individuals.

## Knowledge considerations

Errors in grounded outputs frequently trace back to outdated or conflicting source content. Record when an error is
caused by knowledge, and send it to the knowledge source owner with the example, so the fix is made at source.

## Security and privacy considerations

Samples of real outputs may contain personal or confidential data. Reviewers need appropriate access only, samples are
stored with the output's existing protection, and review notes avoid copying sensitive content unnecessarily.

## Responsible AI considerations

Where outputs inform decisions about people, review a sample for fairness and tone as well as accuracy, and check that
human oversight is working as designed. Severe errors in this context are reported to `responsible-ai:human-oversight`
as well as the owner.

## Evaluation requirements

Live quality results should be compared with release evaluation results. A sustained gap means the evaluation set no
longer reflects real use, and the evaluation owner should refresh it through `evaluation-quality:regression-evaluation`.

## Value measures

Success is the share of productivity benefits with an active quality guard, and the share of quality benefits evidenced
by assisted-versus-unassisted comparison, tracked by the Benefits Realisation Lead with the solution owners.

## Scale notes

### Starter

A short rubric, a small monthly sample reviewed by the owner or an experienced colleague, and one defect measure the
team already records.

### Scale

Standard rubrics per scenario type, blind sampled review for tier 2 and above, guard thresholds agreed before launch,
and quality reported beside productivity in every value review.

### Enterprise

Shared quality standards across business units, a reviewer pool with calibration sessions, and portfolio reporting of
guard breaches and their causes.

## Hand-offs

- To the solution owner and `evaluation-quality:regression-evaluation` when live quality diverges from release evaluation.
- To `value-realisation:productivity-measurement` to suspend or confirm a productivity benefit after a guard result.
- To `value-realisation:post-implementation-review` with quality results.
- To `ai-operations:ai-incident-management` when a severe error reaches a customer or affects a person.

## Reviewer gates

From risk tier 2, `evaluation-quality` checks that the live quality method is consistent with the release evaluation
and that guard thresholds are set before launch. From tier 3, `responsible-ai` confirms that severe error handling
reaches human oversight.

## Failure modes

- Quality is assumed from release testing, and nobody notices drift until complaints arrive.
- Only AI-assisted work is reviewed, so the organisation cannot tell whether AI made quality better or worse.
- Error rates at issue look stable while hidden correction effort climbs, eroding the productivity benefit.
- A guard is breached and nothing happens, because no one agreed in advance what a breach would trigger.
- Review results are traced back to named authors, and people stop using AI openly.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Infer live business quality from release evaluation results alone.
- Report quality results by named individual.
- Report a productivity benefit without its quality guard where one was agreed.
- Treat consistency or accuracy as proven without comparing against unassisted work.

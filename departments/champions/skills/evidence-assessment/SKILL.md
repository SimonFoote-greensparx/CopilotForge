---
name: evidence-assessment
description: Sets up fair, consistent assessment of Champion evidence against the capability rubric, by trained assessors who assess the evidence rather than the person, give useful feedback, handle resubmissions and appeals, and never rank anyone. Use when Champion submissions start arriving, when assessors disagree, or when someone challenges a decision about their evidence.
license: CC-BY-4.0
metadata:
  department: champions
  lifecycle: Enable, Assure
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-champion-best-practice, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Evidence assessment

## Purpose

Evidence-led Champion status is only credible if assessment is fair, consistent and kind. This skill sets up how
submissions are received, assessed against the rubric by trained assessors, given feedback, and reviewed on appeal. It
usually goes wrong when assessment depends on who the assessor is, when it drifts into judging the person rather than
the evidence, or when results are turned into leader boards that discourage everyone except the top few.

## When to use

- The capability framework is in place and the first submissions are about to arrive.
- Assessors are reaching different conclusions on similar evidence.
- A Champion disagrees with a decision and there is no defined appeal route.
- The programme is growing and assessment needs to move from one owner to a trained group.

## When not to use

- Defining the levels, evidence and rubric themselves - use `champions:capability-framework`.
- Designing the programme, charter and boundaries - use `champions:champion-programme-design`.
- Awarding recognition and managing renewal after verification - use `champions:recognition-and-progression`.
- Reviewing whether a Champion-built agent may be released - that goes through `opportunity-management:problem-framing` and CoE governance, not Champion assessment.

## Questions to ask first

1. Who will assess, how much time do they have, and have they been trained on the rubric?
2. How will submissions be received and stored, and who can see them?
3. What turnaround time can the programme promise submitters?
4. How will assessors handle evidence from their own team or from people they know well?
5. Who hears appeals, and are they independent of the original assessor?

## Required inputs

- The capability framework and evidence rubric from `champions:capability-framework`, with worked fictional examples.
- A named pool of assessors with agreed time, and an assessment lead.
- A submission route with restricted access and a retention period agreed with the data protection lead.

If the rubric has no worked examples, create them before assessing real submissions; assessors without examples
disagree. If no secure submission route exists, do not accept submissions until one does.

## Decision framework

Each dimension of the rubric is rated Not yet, Meets or Strong from the evidence alone.

| Outcome | Rule | What the submitter receives |
|---|---|---|
| Verified | Every dimension at least Meets | Confirmation, specific feedback on strengths, a suggested next step |
| Not yet | One or more dimensions at Not yet | Specific feedback on each Not yet dimension and an invitation to resubmit |
| Returned unassessed | Evidence contains sensitive data, or is not from real work, or is incomplete | Explanation and guidance on what to change; nothing is recorded as a fail |

Consistency rules:

| Situation | Rule |
|---|---|
| Assessor knows the submitter well or manages them | Reassign to another assessor |
| Assessor is unsure between two ratings | Second assessor reviews; agreement recorded |
| Level 3 or a disputed case | Two assessors independently, then reconcile |
| Appeal | Heard by an assessor not involved originally, against the same rubric |

## Practitioner approach

Begin by training assessors together. Give them the rubric, the worked examples and a handful of fictional
submissions, ask each to rate them independently, then compare. The disagreements reveal where the rubric is unclear;
fix the wording or add examples before any real submission is assessed. Repeat this calibration every few months, and
whenever new assessors join.

Make the principle explicit: assess the evidence, not the person. Assessors look only at what was submitted against the
rubric. Seniority, reputation, how often someone posts in the community, and anything known about them outside the
submission are irrelevant. Where an assessor knows the submitter well, reassign the submission. Where possible, remove
names from submissions before assessment.

Set a predictable turnaround and keep it. People who submit evidence are taking a small risk; leaving them waiting for
weeks undermines the programme. Track turnaround at programme level and add assessors if it slips.

Write feedback that helps. For each dimension, say what the evidence showed and, for any Not yet, exactly what would
take it to Meets. Avoid general praise or criticism. Feedback should read like a colleague helping, because that is
what it is. A Not yet is an invitation to resubmit, not a failure, and the language must say so.

Handle sensitive evidence immediately. If a submission contains personal, confidential or client data that should not
have been shared, return it unassessed with guidance, delete the copy in line with the retention rules, and note the
pattern at programme level so the submission guide can be improved. Do not record this against the person.

Provide an appeal route. A submitter who disagrees may ask for a review by an assessor not involved in the original
decision, assessing the same evidence against the same rubric. Record the outcome and, where the appeal succeeds,
look at whether the rubric or assessor training needs to change.

Never publish rankings, scores or lists of who has not yet verified. Report outcomes in aggregate: how many
submissions, how many verified at each level, typical turnaround, and the dimensions most often rated Not yet. That
last figure tells the programme where its learning route needs strengthening.

## Outputs

- An assessment procedure in the rubric section of the `champion-capability-framework` template: assessor roles, calibration, consistency rules, turnaround, feedback standard and appeals.
- An assessor guide with worked fictional examples for each rating.
- Feedback for each submission against every rubric dimension.
- An aggregate assessment report for the programme owner.

## Microsoft platform considerations

Not applicable as platform design, because assessment is a people process. Use the organisation's existing
collaboration tools for submissions, with access restricted to assessors and the programme owner.

## Adoption considerations

Fair, quick and kind assessment encourages more people to submit; slow or harsh assessment stalls the whole Champion
journey. Share aggregate themes with the community so everyone learns from them.

## Knowledge considerations

Not applicable as a primary concern, because assessment does not depend on grounding content. Patterns of weak
evidence that trace back to poor knowledge are noted and passed to the `knowledge-management` department (planned).

## Security and privacy considerations

Submissions are personal data and may contain work content. Restrict access, store them only where agreed, apply a
retention period, and delete evidence that contains data it should not. Data protection questions end with the
organisation's DPO.

## Responsible AI considerations

If AI tools are used to help assessors, for example to summarise a submission, the decision and the feedback remain
with a trained human assessor, and submitters are told. Assessment never feeds performance management, pay or
promotion decisions.

## Evaluation requirements

Assessor agreement is the quality measure. During calibration and periodically afterwards, compare independent ratings
on the same submissions, investigate disagreements and adjust the rubric or training.

## Value measures

Programme-level measures, owned by the assessment lead: submissions received, share verified at first submission,
turnaround time, appeal rate and assessor agreement. Reported in aggregate only.

## Scale notes

### Starter

The programme owner assesses, with a second person for any doubtful case. Use a short feedback form against the
rubric dimensions.

### Scale

A trained assessor pool with calibration sessions, a promised turnaround and a simple appeal route.

### Enterprise

Regional assessor pools calibrated against a shared set of examples, an assessment lead monitoring agreement and
turnaround, and an independent appeal panel.

## Hand-offs

- To `champions:recognition-and-progression` when a level is verified.
- To `champions:capability-framework` when assessor disagreement or appeals show the rubric needs changing.
- To `champions:champion-challenges` once a Champion is ready for a practical challenge.

## Reviewer gates

Not applicable as a formal gate, because assessment verifies people capability rather than releasing an AI solution.
Any agent or solution in a submission still needs CoE intake before wider use.

## Failure modes

- Assessors are not calibrated, so outcomes depend on who assesses rather than on the evidence.
- Results are published as leader boards, discouraging most Champions and rewarding volume over quality.
- Submissions containing sensitive data are kept and circulated rather than returned and deleted.
- There is no appeal route, so disputes fester and trust in the badge falls.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Assess the person rather than the evidence, or let reputation or seniority influence a rating.
- Rank Champions or publish lists of who has or has not verified.
- Share assessment outcomes with managers for performance purposes.
- Retain evidence that contains personal or confidential data it should not.

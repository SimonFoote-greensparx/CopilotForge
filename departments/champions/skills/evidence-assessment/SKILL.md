---
name: evidence-assessment
description: Sets up fair, consistent assessment of Champion evidence against each capability's verification criteria and of Champion Challenges, by trained assessors who assess the evidence rather than the person, keep a restricted progress tracker, give useful feedback, handle appeals and never rank anyone. Use when submissions start arriving, when assessors disagree, when progress status is unclear or when a decision is challenged.
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
submissions from either route are received, assessed against the verification criteria by trained assessors, given
feedback and reviewed on appeal, and how each participant's progress is recorded in a tracker. It usually goes wrong
when assessment depends on who the assessor is, when it drifts into judging the person rather than the evidence, when
nobody knows where a participant stands, or when results are turned into leader boards that discourage everyone except
the top few.

## When to use

- The capability framework is in place and the first submissions are about to arrive.
- Assessors are reaching different conclusions on similar evidence.
- Participants keep asking the programme owner where they are in the journey and what comes next.
- A Champion disagrees with a decision and there is no defined appeal route.
- The programme is growing and assessment needs to move from one owner to a trained group.

## When not to use

- Defining the capabilities, verification criteria and rubric themselves - use `champions:capability-framework`.
- Designing the programme, journey and boundaries - use `champions:champion-programme-design`.
- Defining the Challenge options and assessment criteria - use `champions:champion-challenges`.
- Awarding recognition and managing renewal after verification - use `champions:recognition-and-progression`.
- Designing a self-service advisor agent that reads the tracker - use `m365-agents:agent-use-case-design`.
- Reviewing whether a Champion-built agent may be released - that goes through `opportunity-management:problem-framing` and CoE governance, not Champion assessment.

## Questions to ask first

1. Who will assess, how much time do they have, and have they been trained on the criteria?
2. How will submissions and the tracker be stored, and who can see them?
3. What turnaround time can the programme promise submitters?
4. How will assessors handle evidence from their own team or from people they know well?
5. Who hears appeals, and are they independent of the original assessor?

## Required inputs

- The capability framework, verification criteria and rubric from `champions:capability-framework`, with worked fictional examples.
- The Challenge assessment criteria from `champions:champion-challenges`.
- A named pool of assessors with agreed time, and an assessment lead.
- A submission route and tracker with restricted access and a retention period agreed with the data protection lead.

If the rubric has no worked examples, create them before assessing real submissions; assessors without examples
disagree. If no secure submission route exists, do not accept submissions until one does.

## Decision framework

Each rubric dimension is rated Not yet, Meets or Strong from the evidence alone. Evidence from the training route's
guided exercise and from direct submission is assessed identically.

| Outcome | Rule | What the submitter receives |
|---|---|---|
| Verified | Every dimension at least Meets, and the capability's specific criteria met | Confirmation, specific feedback on strengths, the next milestone |
| Not yet | One or more dimensions at Not yet | Specific feedback on each Not yet dimension and an invitation to resubmit |
| Returned unassessed | Evidence contains sensitive data, is not from real work, or is incomplete | Explanation and guidance on what to change; nothing is recorded as a fail |

Consistency rules:

| Situation | Rule |
|---|---|
| Assessor knows the submitter well or manages them | Reassign to another assessor |
| Assessor is unsure between two ratings | Second assessor reviews; agreement recorded |
| Agent capability or a disputed case | Two assessors independently, then reconcile |
| Champion Challenge | Assessed on impact, reusability, quality and strategic alignment, with the problem owner's view of impact |
| Appeal | Heard by an assessor not involved originally, against the same criteria |

Record progress in the tracker, one row per participant, one column per journey stage:

| Stage status | Meaning |
|---|---|
| Not started | No activity at this stage yet |
| In progress | Training exercise or submission under way |
| Submitted | Awaiting assessment |
| Not yet | Assessed; feedback given; resubmission invited |
| Verified or complete | Stage achieved, with date |

## Practitioner approach

Begin by training assessors together. Give them the rubric, the worked examples and a handful of fictional
submissions, ask each to rate them independently, then compare. Disagreements reveal where the criteria are unclear;
fix the wording or add examples before any real submission is assessed. Repeat calibration every few months and
whenever new assessors join, and include Challenge write-ups so the four Challenge criteria are applied consistently.

Make the principle explicit: assess the evidence, not the person. Seniority, reputation, how often someone posts in the
community and anything known about them outside the submission are irrelevant. Where an assessor knows the submitter
well, reassign. Where possible, remove names before assessment.

Treat both routes the same. A guided exercise completed after a learning session is evidence like any other, rated
against the same criteria. Attendance on its own is recorded as participation, never as verification.

Set a predictable turnaround and keep it. People who submit evidence are taking a small risk; leaving them waiting for
weeks undermines the programme. Track turnaround at programme level and add assessors if it slips.

Write feedback that helps. For each dimension, say what the evidence showed and, for any Not yet, exactly what would
take it to Meets. A Not yet is an invitation to resubmit, not a failure, and the language must say so. End every
outcome with the participant's next milestone.

Keep the tracker current. Update it as soon as an outcome is decided, because self-service guidance and any advisor
agent are only as accurate as the tracker. It lets the programme distinguish newcomers, people in progress and those
ready for a Challenge, and plan support accordingly. Participants see their own row; the programme owner and
assessors see the rest; everyone else sees aggregates only.

Handle sensitive evidence immediately. If a submission contains personal, confidential or client data that should not
have been shared, return it unassessed, delete the copy under the retention rules, and note the pattern at programme
level so the submission guide improves. Do not record this against the person.

Provide an appeal route to an assessor not involved originally, assessing the same evidence against the same criteria.
Where appeals succeed, check whether the criteria or assessor training need to change.

Never publish rankings, scores or lists of who has not yet verified. Report in aggregate: submissions, verified at each
stage, turnaround, milestone conversion and the dimensions most often rated Not yet. That last figure shows where the
training route needs strengthening.

## Outputs

- An assessment procedure in the assessment section of the `champion-capability-framework` template: assessor roles, calibration, consistency rules, turnaround, feedback standard and appeals.
- A progress tracker definition in the same template: stages, statuses, who updates it, who can see what and retention.
- An assessor guide with worked fictional examples for each rating and for Challenge criteria.
- Feedback for each submission against every dimension, ending with the next milestone.
- An aggregate assessment report for the programme owner.

## Microsoft platform considerations

Assessment is a people process, so platform choice is secondary. A restricted list or site in the organisation's
existing collaboration tools usually serves for submissions and the tracker. If an advisor agent reads tracker status,
it must be designed so each participant sees only their own record; confirm current capabilities in
`references/sources.md`.

## Adoption considerations

Fair, quick and kind assessment encourages more people to submit; slow or harsh assessment stalls the whole journey.
Share aggregate themes with the community so everyone learns from them, and use stalled stages in the tracker to
target support.

## Knowledge considerations

The tracker is the source of truth for progress, and the framework for requirements; self-service guidance must use
both and nothing else. Patterns of weak evidence that trace back to poor team knowledge are passed to
`knowledge-management:content-quality`.

## Security and privacy considerations

Submissions and the tracker are personal data and may contain work content. Restrict access, store them only where
agreed, apply a retention period, and delete evidence that contains data it should not. Data protection questions end
with the organisation's DPO.

## Responsible AI considerations

If AI tools help assessors, for example to summarise a submission, the decision and the feedback remain with a trained
human assessor, and submitters are told. No agent or automated check decides verification. Assessment never feeds
performance management, pay or promotion decisions.

## Evaluation requirements

Assessor agreement is the quality measure. During calibration and periodically afterwards, compare independent ratings
on the same submissions, investigate disagreements and adjust the criteria or training. Spot-check the tracker against
assessment records each quarter.

## Value measures

Programme-level measures, owned by the assessment lead: submissions received, share verified at first submission,
turnaround, milestone conversion between stages, appeal rate and assessor agreement. Reported in aggregate only.

## Scale notes

### Starter

The programme owner assesses, with a second person for any doubtful case, and keeps the tracker as a simple restricted
list. Use a short feedback form against the rubric dimensions.

### Scale

A trained assessor pool with calibration sessions, a promised turnaround, a maintained tracker feeding self-service
guidance and a simple appeal route.

### Enterprise

Regional assessor pools calibrated against shared examples, an assessment lead monitoring agreement and turnaround, a
governed tracker with defined data ownership and an independent appeal panel.

## Hand-offs

- To `champions:recognition-and-progression` when a stage is verified or a Challenge completed.
- To `champions:capability-framework` when assessor disagreement or appeals show the criteria need changing.
- To `champions:champion-challenges` once all three capabilities are verified.
- To `m365-agents:agent-use-case-design` if an advisor agent will read the tracker.

## Reviewer gates

Not applicable as a formal gate, because assessment verifies people capability rather than releasing an AI solution.
Any agent in a submission still needs CoE intake, and an advisor agent reading tracker data goes to `security-privacy`.

## Failure modes

- Assessors are not calibrated, so outcomes depend on who assesses rather than on the evidence.
- Results are published as leader boards, discouraging most Champions and rewarding volume over quality.
- The tracker falls behind, so self-service guidance tells participants the wrong next milestone.
- Submissions containing sensitive data are kept and circulated rather than returned and deleted.
- There is no appeal route, so disputes fester and trust in the badge falls.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Assess the person rather than the evidence, or let reputation or seniority influence a rating.
- Rank Champions or publish lists of who has or has not verified.
- Let an agent or automated check decide verification.
- Share assessment outcomes or tracker data with managers for performance purposes.
- Retain evidence that contains personal or confidential data it should not.

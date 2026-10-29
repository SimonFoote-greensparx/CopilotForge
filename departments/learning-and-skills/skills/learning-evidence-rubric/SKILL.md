---
name: learning-evidence-rubric
description: Defines the evidence rubrics that verify workforce AI learning - acceptable evidence types per pathway level, dimensions such as real work, safe use, verification, judgement and transfer with Not yet, Meets and Strong descriptors, who checks evidence and how, feedback and redaction rules - so completion means demonstrated practice, not attendance. Use when learning is counted by attendance, or when a pathway level or module needs exit criteria.
license: CC-BY-4.0
metadata:
  department: learning-and-skills
  lifecycle: Enable, Measure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-studio
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-privacy, ms-champion-best-practice, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# Learning evidence rubric

## Purpose

Attendance tells you who was in the room, not who can now use Microsoft AI well and safely. This skill defines the
rubrics that turn learning into verified practice: what counts as evidence at each pathway level, the dimensions it is
judged on, what Not yet, Meets and Strong look like, and how evidence is checked fairly and lightly. It usually goes
wrong when the rubric is so heavy that nobody submits, when it drifts into judging the person rather than the evidence,
or when evidence collected for learning quietly becomes performance data.

## When to use

- Learning success is reported as attendance or completion, and the sponsor asks what people can actually do.
- A pathway level or curriculum module needs clear exit criteria.
- Experienced people want to skip learning and need to know what evidence would be accepted.
- Facilitators or peer reviewers disagree about whether an example is good enough.
- Workforce learning evidence and Champion evidence need to line up so one can count towards the other.

## When not to use

- Defining the Champion capabilities and their verification criteria - use `champions:capability-framework`.
- Running assessor training, the Champion tracker and appeals for Champion submissions - use `champions:evidence-assessment`.
- Defining the pathway levels themselves - use `learning-and-skills:ai-learning-pathway`.
- Quality rubrics for evaluating an AI solution's outputs - use `evaluation-quality:ai-quality-rubric`.
- Measuring skills growth across groups from the evidence - use `learning-and-skills:skills-measurement`.

## Questions to ask first

1. Which pathway levels and modules need a rubric now, and what does each level say people should be able to do?
2. What evidence can people realistically produce from their work without exposing sensitive content?
3. Who will check evidence - facilitators, trained peers, Champions, or self-check with sampling - and how much time do they have?
4. Should workforce evidence count towards the Champion journey, and vice versa?
5. What will be recorded about evidence, who can see it, and for how long?

## Required inputs

- The pathway levels and their behaviour descriptions from `learning-and-skills:ai-learning-pathway`.
- Module outcomes from `learning-and-skills:ai-role-curriculum`.
- The Champion evidence rubric where one exists, from `champions:capability-framework`, so dimensions can align.
- The approved-use guidance, to define the safe use dimension.
- The data protection lead's agreement on what evidence records are kept and for how long.

If data protection agreement on records is missing, run the rubric for feedback only and record nothing beyond
aggregate counts until it is in place. If a level's behaviour description is missing, do not write its rubric; send it
back to the pathway owner.

## Decision framework

Use the same five dimensions at every level; the descriptors deepen as the level rises.

| Dimension | Not yet | Meets | Strong |
|---|---|---|---|
| Real work | Demo or invented task | A task from the person's own role or an assigned lab exercise | A recurring task valued by the team |
| Safe use | Sensitive data shared, or an unapproved tool used | Approved tools only; nothing that should not have been shared | Explains what was deliberately left out and why |
| Verification | Output used without checking | Output checked against its source; the check is described | The check is built into a reusable pattern |
| Judgement | No sense of limits | Notes where AI did not help or got it wrong | Explains when they would not use AI for this task |
| Transfer | Only the author could repeat it | Someone else could follow it | A colleague has used it |

Level requirements, and evidence types that fit each:

| Level | Required | Typical evidence |
|---|---|---|
| Foundation | Safe use and Verification at Meets | One real task with prompt, output and the check applied |
| Applied | All dimensions at Meets except Transfer | Two role scenarios, each with refinement, check and reflection |
| Proficient | All dimensions at Meets | A reusable pattern or delegated task design that a colleague has used |
| Advanced | Set by the track in `learning-and-skills:advanced-pathways` | A governed build with tests and an owner |

Strong is for feedback only. It never creates a higher status and is never counted.

## Practitioner approach

Write the rubric from the behaviour you want to see, not from the course content. Take each level's behaviour
description and ask what a person could show that proves it. For Foundation, that is usually one real task: what they
asked, what came back, how they checked it and what they changed. Anything heavier and people will not submit.

Keep dimensions constant across levels. Using the same five dimensions everywhere means learners and checkers learn
one language, evidence from one level builds naturally into the next, and Champion evidence can be mapped across. Align
wording with the Champion rubric where one exists, and agree equivalence with the Champions programme owner.

Make Verification and Safe use the non-negotiables. A polished output that was never checked is the exact behaviour the
programme is trying to change, so it cannot meet any level. Equally, evidence that itself contains sensitive data fails
Safe use, however good the rest is, and the learner is asked to redact and resubmit rather than being penalised.

Choose the lightest checking model that keeps standards consistent. At Foundation, a facilitator or trained peer can
review evidence during a session, or learners can self-check against the rubric with a sample reviewed later. At
Applied and Proficient, trained peers or Champions check, with a short calibration exercise on fictional examples so
they agree on what Meets looks like. Checkers assess the evidence, not the person, and do not check colleagues they
manage.

Give feedback that helps, not a grade. "Meets on verification - you compared each figure with the source. Next time,
note the one you corrected." Not yet is a normal outcome with a clear next step, never a failure recorded against
anyone.

Write fictional exemplars for each level: one that meets, one that does not yet, with notes explaining why. Exemplars
do more than any descriptor to help people judge whether they are ready to submit.

Decide records early. Keep the minimum: which level was evidenced and when, held with restricted access, and aggregate
counts for reporting. Do not keep copies of submitted work longer than checking needs. Tell learners plainly that
evidence is for learning, will not be used in performance processes, and is reported only in aggregate.

Review the rubric when products change or checkers keep disagreeing on a dimension. Disagreement is a sign the
descriptor is unclear, not that a checker is wrong.

## Outputs

- A learning evidence rubric recorded in the evidence section of the `ai-learning-plan` template - dimensions, descriptors, level requirements and evidence types.
- Fictional exemplars for each level, with notes on why each meets or does not yet meet.
- A checking guide covering who checks, calibration, feedback wording and conflicts of interest.
- An evidence records statement covering what is kept, access, retention and aggregate reporting, agreed with the data protection lead.
- An equivalence note with the Champions programme, aligned with the `champion-capability-framework` template.

## Microsoft platform considerations

Evidence often takes the form of a prompt, an output and a note of the check made. Learners should capture this without
copying sensitive content, for example by describing the source rather than pasting it. Collect evidence through an
approved, access-restricted route; if a form or list is used, keep it in the organisation's governed storage. Features
such as sharing and retention of Copilot interactions change, so check `references/sources.md` before giving guidance.

## Adoption considerations

A light, fair rubric encourages people to try and show what they did. Celebrate patterns that colleagues reuse, with
permission, rather than individuals' levels. Never publish who has or has not evidenced a level.

## Knowledge considerations

Strong evidence often contains reusable prompt patterns and verification tricks. With the learner's agreement and after
redaction, offer them to the scenario catalogue or prompt library so the evidence benefits others.

## Security and privacy considerations

Evidence records are personal data even when they hold no sensitive content. Collect the minimum, restrict access to
checkers and the Learning Lead, set a retention period with the data protection lead, and remove copies of work once
checked. Data protection questions end with the organisation's DPO.

## Responsible AI considerations

The Judgement and Verification dimensions are the responsible AI core of the rubric: they reward knowing the limits of
AI and keeping a human check. The rubric never rewards volume or speed of use.

## Evaluation requirements

Not applicable as AI evaluation, because no AI solution is being released. The rubric's own quality is checked through
calibration: checkers rate the same fictional exemplars and the Learning Lead reviews where they diverge.

## Value measures

Baseline: the share of learners producing evidence at each level when the rubric launches. Measures: evidence rates by
level and role, first-time Meets rates by dimension, and checker agreement in calibration. Owned by the Learning Lead,
reported at role or team level above the minimum group size, never per person.

## Scale notes

### Starter

Foundation and Applied rubrics with one exemplar each, checked by facilitators during sessions, recording only aggregate
counts.

### Scale

All levels with exemplars, trained peer checkers with calibration each quarter, an access-restricted evidence route and
equivalence agreed with the Champions programme.

### Enterprise

One rubric across business units with local checkers, central calibration on shared exemplars, localised exemplars and
rubric updates governed with the pathway owner.

## Hand-offs

- To `learning-and-skills:ai-learning-pathway` when a level's behaviour description needs changing.
- To `learning-and-skills:skills-measurement` with the aggregate evidence counts.
- To `champions:evidence-assessment` to align Champion assessment with workforce evidence.
- To `learning-and-skills:facilitator-guide` so sessions end with evidence that fits the rubric.

## Reviewer gates

Not applicable, because the rubric does not release an AI solution. The evidence records approach is agreed with the
data protection lead before any personal records are kept.

## Failure modes

- The rubric is so heavy that only enthusiasts submit, and evidence rates say more about time than skill.
- Checkers judge the person's seniority or confidence instead of the evidence in front of them.
- Strong becomes a status, and people compete for it.
- Evidence records are later requested for performance reviews, and trust in the programme collapses.
- Evidence contains the very sensitive data the safe use dimension warns against.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Count attendance or completion as evidence.
- Score, rank or publish individuals' evidence results.
- Allow learning evidence to be used in performance, pay or job decisions.
- Keep copies of submitted work longer than checking needs.

---
name: recognition-and-progression
description: Designs how Champions progress through the six-stage journey to recognised Champion, with recognition linked to demonstrated contribution, access to advanced materials, pilots and specialist pathways, renewal, a regular programme health check and programme-level measures such as milestone conversion. Use when designing Champion recognition, when status has gone stale, or when a sponsor asks whether the programme is healthy.
license: CC-BY-4.0
metadata:
  department: champions
  lifecycle: Measure, Scale, Improve
  maturity: adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-champion-programme, ms-champion-best-practice, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# Recognition and progression

## Purpose

Recognition tells Champions their contribution matters, and progression gives them somewhere to go next. This skill
designs the six-stage journey from joining to recognised Champion, the recognition and access that each stage opens,
renewal so status stays current, and a regular health check with measures reported in aggregate. It usually goes wrong
when recognition rewards attendance or visibility rather than demonstrated contribution, when status never expires,
when recognition leads nowhere, or when metrics turn into league tables.

## When to use

- A Champions programme needs a recognition and progression model before launch.
- Champion status has gone stale, with many named Champions who no longer contribute.
- Recognised Champions ask "what next?" and the programme has no advanced route to offer.
- The sponsor or CoE asks whether the Champions programme is healthy and worth continuing.
- Recognition has become a popularity contest and needs redesigning around evidence.

## When not to use

- Designing the programme purpose, charter and boundaries - use `champions:champion-programme-design`.
- Defining the capabilities and verification criteria - use `champions:capability-framework`.
- Assessing individual submissions and keeping the tracker - use `champions:evidence-assessment`.
- Designing the Challenge options and criteria - use `champions:champion-challenges`.
- Measuring workforce-wide Copilot adoption - use `copilot-adoption:adoption-measurement`.

## Questions to ask first

1. What forms of recognition does the organisation already use, and what does HR allow?
2. What will the sponsor personally do to recognise Champions?
3. What advanced materials, pilots and specialist pathways can the organisation genuinely offer, and who owns each?
4. How long should recognised status last before renewal, given how fast tools and practice change?
5. What decisions will the health check inform, who receives it, and what minimum group size applies?

## Required inputs

- The programme charter and journey from `champions:champion-programme-design`, including the time commitment.
- The capability framework, Challenge criteria and tracker from `champions:capability-framework`, `champions:champion-challenges` and `champions:evidence-assessment`.
- HR's position on recognition, rewards and how Champion activity may appear in development conversations.
- The agreed minimum reporting group size from `copilot-adoption:adoption-measurement`.

If HR has not agreed how recognition may be used, design recognition that sits outside formal reward and record the
open question. Never link Champion status to pay or promotion without HR's explicit agreement. Do not promise pilots
or pathways that no owner has agreed to run.

## Decision framework

Recognition follows evidence and contribution at every stage, never attendance alone.

| Stage | Entry evidence | Recognition | What it opens |
|---|---|---|---|
| 1. Join the community | Declared interest and manager agreement to time | Welcome | Community channel, learning sessions, resources, events, peers |
| 2. Verify Chat capability | Verified through `champions:evidence-assessment` | Capability badge | Next capability |
| 3. Verify productivity capability | Verified | Capability badge | Next capability |
| 4. Verify agent capability | Verified | Capability badge | Eligibility for the Champion Challenge |
| 5. Complete a Champion Challenge | Challenge assessed as Meets on all four criteria | Showcase, sponsor thanks, asset credited | Eligibility for recognition |
| 6. Earn recognition and keep contributing | Stages 2 to 5 complete | Recognised Champion status, visible in the directory | Advanced materials, pilots, specialist pathways, invitations to mentor or assess |

What recognition opens should be real and owned:

| Benefit | What it means | Owner |
|---|---|---|
| Advanced materials | Deeper guidance, early sight of new scenarios, advanced sessions | Programme owner |
| Pilots | A place in governed pilots of new Copilot capabilities or agents | CoE or adoption lead |
| Specialist pathways | Routes into advanced learning or governed delivery communities, such as maker or CoE contributor roles | CoE and `learning-and-skills:advanced-pathways` |

Renewal rules:

| Situation | Outcome |
|---|---|
| Contribution continued during the period | Status renewed |
| Little contribution, for example after a change of role or workload | Status moves to alumni, with a simple route back |
| Framework has changed materially | Light refresh evidence requested at renewal |

The health check rates coverage, capability, contribution, community and boundaries as Healthy, Watch or Act, using
programme-level measures: community size and spread, milestone conversion, completion time, Challenge outputs,
peer-support activity, adoption indicators and reusable assets.

## Practitioner approach

Design the journey from the participant's point of view. Someone joining should see every stage, the evidence that
moves them on and what each step opens. Publish the journey with the capability framework, and make progress visible
through the tracker and self-service guidance so nobody has to ask the owner where they stand.

Link recognition to demonstrated contribution. Capability badges acknowledge verified practice; full recognition needs
all three capabilities plus a completed Challenge, so status reflects both ability and contribution to others.
Recognition for attendance alone is the quickest way to devalue the badge.

Make recognition meaningful rather than expensive. The most valued recognition is usually attention from people who
matter: the sponsor naming a contribution, a manager mentioning it in a team meeting, an asset credited when others
reuse it. Agree with HR how Champion contribution may be mentioned in development conversations, and keep it to
capability and contribution rather than usage.

Give recognition somewhere to lead. Access to advanced materials, places in governed pilots and specialist pathways
are what keep capable people engaged after the badge, and they give the Centre of Excellence a pool of colleagues who
already work safely. Only offer what an owner has agreed to run, and make the selection criteria for pilots open.

Build in renewal from the start. A renewal period of around a year suits most organisations. Keep it light: evidence of
continued contribution, plus a short refresh where the framework has changed. People who step back become alumni rather
than lapsing silently. Change of role, parental leave or heavy workload are normal; the language never implies failure.

Run a health check at a regular rhythm, often each quarter. Look at coverage, capability, contribution, community and
boundaries. Milestone conversion and completion time show where the journey stalls; a pile-up before one stage usually
points to unclear criteria, missing sessions or an unresolved approval position rather than to the participants.
Adoption indicators in teams with Champions are context, not proof of cause. Rate each area, agree actions with the
sponsor, and watch boundaries closely, because drift into unpaid support is gradual and invisible unless someone looks.

Report Champion measures only at programme level, applying the minimum group size. Individual leader boards encourage
volume over quality and discourage the many Champions who contribute quietly.

## Outputs

- A recognition and progression model in the recognition section of the `champion-programme-charter` template: six stages, entry evidence, recognition, what each stage opens, benefit owners, renewal and alumni rules.
- A programme health check with ratings, evidence and agreed actions, in the same template.
- A Champion measures summary at programme level, applying the minimum group size.

## Microsoft platform considerations

Not applicable as platform design, because recognition and progression are people processes. Use existing community,
directory and badge tools, and keep any record of Champion status access-controlled and limited to what the programme
needs. Pilots of new capabilities follow the organisation's governance and current source records.

## Adoption considerations

Recognition sustains the network that sustains adoption. Use showcases and sponsor recognition to spread successful
scenarios, use pilots to give Champions early, governed experience they can pass on, and use the health check to spot
teams where adoption support is thin.

## Knowledge considerations

Not applicable as a primary concern, because recognition does not depend on grounding content. Assets recognised
through showcases still need an owner and review date in the scenario catalogue.

## Security and privacy considerations

Champion records are personal data. Keep only what the programme needs, restrict access, apply a retention period, and
remove alumni records when they are no longer needed. Pilot participation does not grant broader data access. Data
protection questions end with the organisation's DPO.

## Responsible AI considerations

Recognition is never based on volume of AI usage, which would reward indiscriminate use. Status, pilots and pathways
are based on evidence of safe, verified practice and contribution, assessed fairly.

## Evaluation requirements

Not applicable as solution evaluation, because this skill designs a people process. The health check is reviewed by
confirming each rating has evidence and each Act rating has an owner and date.

## Value measures

Programme-level measures, owned by the programme owner with baselines at launch: community size and spread, milestone
conversion, completion time, Challenge outputs, peer-support activity, adoption indicators in teams with Champions,
reusable assets, renewal rate and boundary drift. Reported to the sponsor each quarter. Never individual performance.

## Scale notes

### Starter

A simple journey, sponsor thanks at a quarterly all-hands, a shared list of recognised Champions and an annual renewal
conversation. Advanced access may be no more than early sight of new scenarios. Run the health check twice a year.

### Scale

Published journey and badges, quarterly showcases, owned pilot places, annual renewal and a quarterly health check
reported to the CoE.

### Enterprise

Regional recognition aligned to a shared model, alumni and mentor roles, specialist pathways into CoE delivery and
advanced learning, links with HR development frameworks where agreed, and a health check feeding the CoE scorecard.

## Hand-offs

- To `ai-centre-of-excellence:coe-operating-model` so health check actions, pilots and specialist pathways connect to CoE governance.
- To `champions:capability-framework` when renewal or stalled conversion shows the framework needs updating.
- To `champions:champion-programme-design` when the health check shows boundary drift or charter changes are needed.
- To `copilot-adoption:adoption-measurement` for team-level adoption indicators and to share Champion coverage.
- To `learning-and-skills:advanced-pathways` for advanced pathways.

## Reviewer gates

Not applicable as a formal gate, because recognition and progression do not release an AI solution; data handling for
Champion records follows the organisation's existing data protection controls.

## Failure modes

- Recognition rewards visibility and attendance, so the badge loses credibility with the people Champions help.
- Status never expires, and the directory fills with names of people who no longer contribute.
- Recognition leads nowhere, so capable Champions drift away after the badge.
- Pilots and pathways are promised without owners, and the programme loses trust when they never appear.
- Metrics are published as individual league tables, discouraging most Champions.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Rank Champions or publish individual league tables.
- Base recognition on attendance or volume of AI usage.
- Link Champion status to pay or promotion without HR's explicit agreement.
- Promise pilots or pathways that nobody has agreed to run.
- Treat stepping back from the role as failure.

---
name: recognition-and-progression
description: Designs how Champions are recognised and progress - join, verify capabilities, complete a challenge, earn recognition and keep contributing - with renewal so status stays current, a regular programme health check and Champion metrics reported at programme level only. Use when designing Champion recognition, when status has gone stale, or when a sponsor asks whether the Champions programme is healthy.
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
designs the journey from joining to recognised Champion, the recognition at each stage, renewal so status stays
current, and a regular health check of the programme with metrics reported in aggregate. It usually goes wrong when
recognition rewards visibility rather than contribution, when status never expires and loses meaning, or when metrics
turn into league tables that set Champions against each other.

## When to use

- A Champions programme needs a recognition and progression model before launch.
- Champion status has gone stale, with many named Champions who no longer contribute.
- The sponsor or CoE asks whether the Champions programme is healthy and worth continuing.
- Recognition has become a popularity contest and needs redesigning around evidence.

## When not to use

- Designing the programme purpose, charter and boundaries - use `champions:champion-programme-design`.
- Defining capability levels and the evidence rubric - use `champions:capability-framework`.
- Assessing individual submissions - use `champions:evidence-assessment`.
- Designing the challenges Champions complete - use `champions:champion-challenges`.
- Measuring workforce-wide Copilot adoption - use `copilot-adoption:adoption-measurement`.

## Questions to ask first

1. What forms of recognition does the organisation already use, and what does HR allow?
2. What will the sponsor personally do to recognise Champions?
3. How long should verified status last before renewal, given how fast tools and practice change?
4. What decisions will the programme health check inform, and who receives it?
5. What minimum group size applies when reporting Champion metrics?

## Required inputs

- The programme charter from `champions:champion-programme-design`, including the time commitment.
- The capability framework and assessment procedure from `champions:capability-framework` and `champions:evidence-assessment`.
- HR's position on recognition, rewards and how Champion activity may appear in development conversations.
- The organisation's agreed minimum reporting group size from `copilot-adoption:adoption-measurement`.

If HR has not agreed how recognition may be used, design recognition that sits outside formal reward and record the
open question. Never link Champion status to pay or promotion without HR's explicit agreement.

## Decision framework

The progression journey has five stages. Recognition follows evidence and contribution, never attendance alone.

| Stage | Entry evidence | Recognition |
|---|---|---|
| 1. Join the community | Declared interest and manager agreement to time | Welcome, access to the community and learning route |
| 2. Verify capabilities | Levels verified through `champions:evidence-assessment` | Level badge for each verified capability |
| 3. Complete a challenge | A completed Champion Challenge with a reusable asset | Showcase of the asset and thanks from the sponsor |
| 4. Earn Champion recognition | Verified capability plus a completed challenge | Recognised Champion status, visible in the directory |
| 5. Continue contributing | Ongoing contribution over the renewal period | Renewal of status, invitations to mentor, assess or shape the programme |

Renewal rules:

| Situation | Outcome |
|---|---|
| Contribution continued during the period | Status renewed |
| Little contribution, for example after a change of role or workload | Status moves to alumni, with a simple route back |
| Framework levels have changed materially | Light refresh evidence requested at renewal |

The programme health check covers coverage, capability, contribution, community and boundaries, each rated Healthy,
Watch or Act.

## Practitioner approach

Design the journey from the Champion's point of view. Someone joining should be able to see every stage, what evidence
moves them on and what recognition follows. Publish the journey alongside the capability framework so it is transparent
and the same for everyone.

Make recognition meaningful rather than expensive. The most valued recognition is usually attention from people who
matter: the sponsor naming a contribution, a manager mentioning it in a team meeting, an asset credited when others
reuse it. Badges and directory entries help people find Champions. Agree with HR how Champion contribution may be
mentioned in development conversations, and keep it to contribution and capability rather than usage.

Separate recognition of the stages. Verified capability is recognised as soon as it is verified. A completed challenge
is recognised through a showcase. Full Champion recognition needs both, so status reflects ability and contribution
together. Avoid recognition for attendance alone; it is the quickest way to devalue the badge.

Build in renewal from the start. Practice and tools change quickly, and a Champion verified two years ago may no longer
be current. A renewal period of around a year works for most organisations. Renewal should be light: evidence of
continued contribution, plus a short refresh where the framework has changed. People who step back become alumni rather
than lapsing silently, and the route back is simple. Change of role, parental leave or heavy workload are normal; the
language should never imply failure.

Run a programme health check at a regular rhythm, often each quarter. Look at coverage (do all teams, locations and
personas have Champions?), capability (how many are verified at each level?), contribution (challenges, assets and
routed opportunities), community (attendance trends and questions answered) and boundaries (are Champions being pulled
into support or approval work?). Rate each area and agree actions with the sponsor. The boundary area matters most,
because drift into unpaid support is gradual and invisible unless someone looks.

Report Champion metrics only at programme level. Counts of verified Champions, challenges completed and assets reused
tell the sponsor whether the programme is working. Individual leader boards encourage volume over quality and
discourage the many Champions who contribute quietly. Apply the organisation's minimum group size when breaking metrics
down by team or region.

## Outputs

- A recognition and progression model in the recognition section of the `champion-programme-charter` template: stages, entry evidence, recognition, renewal and alumni rules.
- A programme health check with ratings, evidence and agreed actions.
- A Champion metrics summary at programme level, applying the minimum group size.

## Microsoft platform considerations

Not applicable as platform design, because recognition and progression are people processes. Use existing community
and directory tools, and keep any record of Champion status access-controlled and limited to what the programme needs.

## Adoption considerations

Recognition sustains the network that sustains adoption. Use showcases and sponsor recognition to spread successful
scenarios, and use the health check to spot teams where adoption support is thin.

## Knowledge considerations

Not applicable as a primary concern, because recognition does not depend on grounding content. Assets recognised
through showcases should still have an owner and review date in the scenario catalogue.

## Security and privacy considerations

Champion records are personal data. Keep only what the programme needs, restrict access, apply a retention period, and
remove alumni records when they are no longer needed. Data protection questions end with the organisation's DPO.

## Responsible AI considerations

Recognition must never be based on volume of AI usage, which would reward indiscriminate use. Status and progression
are based on evidence of safe, verified practice and contribution, assessed fairly.

## Evaluation requirements

Not applicable as solution evaluation, because this skill designs a people process. The health check itself is
reviewed by confirming each rating has evidence and each Act rating has an owner and date.

## Value measures

Programme-level measures, owned by the programme owner: coverage by team and persona, verified Champions by level,
challenges completed, assets reused, opportunities routed, renewal rate and boundary drift. Baselines are taken at
programme launch and reported to the sponsor each quarter. Never individual performance.

## Scale notes

### Starter

A simple journey, sponsor thanks at a quarterly all-hands, a shared list of Champions and an annual renewal
conversation. Run the health check informally twice a year.

### Scale

Published journey and badges, quarterly showcases with the sponsor, annual renewal and a quarterly health check
reported to the CoE.

### Enterprise

Regional recognition aligned to a shared model, alumni and mentor roles, formal links with HR development frameworks
where agreed, and a health check feeding the CoE scorecard.

## Hand-offs

- To `ai-centre-of-excellence:coe-operating-model` so Champion metrics and health check actions feed CoE governance.
- To `champions:capability-framework` when renewal shows the framework needs updating.
- To `champions:champion-programme-design` when the health check shows boundary drift or charter changes are needed.
- To `copilot-adoption:adoption-measurement` so Champion coverage informs adoption reporting.

## Reviewer gates

Not applicable as a formal gate, because recognition and progression do not release an AI solution; data handling for
Champion records follows the organisation's existing data protection controls.

## Failure modes

- Recognition rewards visibility and attendance, so the badge loses credibility with the people Champions are meant to help.
- Status never expires, and the directory fills with names of people who no longer contribute.
- Metrics are published as individual league tables, discouraging most Champions.
- The health check never looks at boundaries, and Champions drift into unpaid support until they burn out.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Rank Champions or publish individual league tables.
- Base recognition on attendance or volume of AI usage.
- Link Champion status to pay or promotion without HR's explicit agreement.
- Treat stepping back from the role as failure.

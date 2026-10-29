---
name: champion-metrics
description: Defines the programme-level measure set for Champions - coverage, journey conversion and completion time, contribution, community, boundary drift and adoption context - each with a definition, source, baseline, target, owner, minimum group size and reporting rhythm, plus rules against individual rankings. Use when a sponsor asks what the programme delivers, before a dashboard is built, or when a leader board is proposed.
license: CC-BY-4.0
metadata:
  department: champions
  lifecycle: Mobilise, Measure, Improve
  maturity: adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-champion-best-practice, ms-champion-programme, ms-copilot-adoption-hub, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# Champion metrics

## Purpose

A sponsor who funds Champions' time will ask what it delivers, and a programme owner needs to know where the journey
stalls. This skill defines a small set of programme-level measures that answer both questions honestly, with clear
definitions, sources, baselines and owners, and with firm rules against ranking or monitoring individuals. It usually
goes wrong when measures count activity (posts, attendance, usage) rather than capability and contribution, when
adoption gains are claimed as the programme's doing, or when a well-meant dashboard turns into a leader board that
rewards volume and discourages the quiet majority.

## When to use

- A Champions programme is launching and needs agreed measures and baselines before the first cohort.
- The sponsor or CoE asks what the programme delivers and the answer is a headcount.
- Someone proposes a leader board, points table or individual activity dashboard for Champions.
- A dashboard or report for the programme is about to be built and needs a specification.
- Measures exist but nobody trusts their definitions or knows where the data comes from.

## When not to use

- Running the regular health rating and individual status renewal - use `champions:recognition-and-progression`.
- The periodic programme review and renewal decision - use `champions:champions-health-check`.
- Measuring workforce-wide Copilot adoption - use `copilot-adoption:adoption-measurement`.
- Linking adoption indicators to business benefits - use `value-realisation:adoption-to-value-metrics`.
- The CoE's overall KPI framework and scorecard - use `ai-centre-of-excellence:coe-kpi-framework`.
- Keeping the progress tracker and assessment records - use `champions:evidence-assessment`.

## Questions to ask first

1. What decisions should the measures inform, and who makes them - the programme owner, the sponsor, the CoE?
2. What data exists today (tracker stages, community records, Challenge outputs, scenario catalogue, adoption reporting), and who owns each source?
3. What minimum group size applies, and what have HR and the data protection lead agreed the programme may hold and report?
4. What baselines can be set now, before the next cohort or wave?
5. How often will measures be reported, and to whom?

## Required inputs

- The programme charter and journey from `champions:champion-programme-design`.
- The progress tracker design from `champions:evidence-assessment`, including statuses and access rules.
- Coverage targets from `champions:champion-recruitment`.
- The minimum reporting group size and team-level adoption indicators from `copilot-adoption:adoption-measurement`.
- HR's and the data protection lead's position on Champion data.

If no minimum group size has been agreed, propose one, mark it "to confirm" with the data protection lead and do not
report below it. If a data source does not exist, record the measure as planned rather than estimating it.

## Decision framework

Use a short measure set across six areas. Every measure is reported at programme, business-unit or cohort level only.

| Area | Measure | Definition to agree | Typical source |
|---|---|---|---|
| Coverage | Spread against targets | Teams, sites and personas with at least one active Champion, against targets | Tracker and audience model |
| Capability | Milestone conversion | Share of participants reaching each stage from the previous one in a period | Tracker |
| Capability | Completion time | Typical time from joining to each stage, as a median by cohort | Tracker |
| Contribution | Challenge outputs and reuse | Challenges completed; assets published to the catalogue; reuse of those assets | Challenge records, scenario catalogue |
| Contribution | Opportunities routed | Ideas routed to intake by Champions, and how many progressed | Intake records |
| Community | Peer support | Share of community questions answered by peers; sessions led by Champions | Community and learning records |
| Boundaries | Drift | Signs Champions are handling faults, approvals or training outside the boundary | Community review, support themes, Champion pulse |
| Adoption context | Team-level indicators | Adoption indicators in teams with and without Champions, as context only | `copilot-adoption:adoption-measurement` |

Apply firm rules on use.

| Permitted | Prohibited |
|---|---|
| Programme, business-unit and cohort totals above the minimum group size | Individual leader boards, points tables or rankings |
| Stage status visible to the participant and the programme team | Using Champion data in performance reviews without HR agreement |
| Assets credited to authors when reused | Counting posts, attendance or Copilot usage as contribution |
| Adoption indicators as context | Claiming adoption gains as caused by Champions |

Read signals before acting on them.

| Signal | Likely meaning | Check first |
|---|---|---|
| Conversion stalls at one stage | Unclear criteria, missing learning, unresolved approval position | Assessor feedback, learning calendar, agent-building approval |
| Coverage falls in an area | Champions moving on, manager time withdrawn | Recruitment pipeline, manager agreement patterns |
| Peer answers drop | Community manager gap or channel fatigue | Community activity and rituals |
| Drift indicators rise | Support model gaps pushing work onto Champions | Support themes and service desk routing |

## Practitioner approach

Start with decisions, not data. Ask the sponsor and programme owner what they would do differently depending on the
answer: fund another cohort, fix a stalled stage, recruit in a gap, reset the boundary. Keep only measures that inform
one of those decisions. A dozen well-defined measures is usually too many; six to eight is plenty.

Define each measure precisely before collecting anything. Write the definition, the source, the period, the owner and
the minimum group size. "Active Champion" and "completed" need agreed meanings, or numbers will shift between reports
and trust will go. Set baselines at launch or before the next cohort, and mark any that cannot be set yet.

Measure capability and contribution, not activity. Milestone conversion and completion time show whether the journey
works. Challenge outputs, assets reused and opportunities routed show whether Champions create value for others.
Attendance and posting volume are at best supporting signals; reported on their own, they reward visibility over
substance.

Treat adoption indicators as context. Teams with Champions may adopt faster for many reasons, including the kind of
people who volunteer. Show team-level adoption alongside Champion coverage, but never claim causation, and say so in
every report.

Watch the boundary. Drift into unpaid support is gradual and invisible unless someone measures it. A short periodic
pulse asking Champions how their time is spent, combined with support themes, is enough to show it at programme level.

Write the rules into the specification. Any dashboard or report built from these measures must state the minimum group
size, prohibit individual rankings and limit access to stage-level data to the participant and the programme team.
When someone asks for a leader board, explain the harm: it rewards volume, discourages most Champions and turns a
capability programme into a competition.

Report on a steady rhythm, usually quarterly to the sponsor and the CoE, with a short narrative: what changed, what it
probably means, and what the programme will do. Feed the measures into the health rating and the periodic programme
review.

## Outputs

- A Champion measure set recorded in the health check and measures section of the `champion-programme-charter` template: measure, definition, source, baseline, target, owner, minimum group size and rhythm.
- A reporting specification for any dashboard, including access rules and prohibited uses.
- A quarterly programme report outline with narrative prompts, feeding the `coe-kpi-scorecard`.
- A baseline record set before the next cohort.

## Microsoft platform considerations

Not applicable as platform design, because the measures are programme-level and tool-neutral. Where a dashboard is
built in the organisation's reporting tools, apply access controls and aggregation, and draw team-level adoption data
only through `copilot-adoption:adoption-measurement` and the current source records in `references/sources.md`.

## Adoption considerations

Champion measures sit alongside workforce adoption measures, not inside them. Share coverage with the adoption lead so
gaps in Champion support can be read against adoption gaps by team.

## Knowledge considerations

Not applicable as a primary concern, because these measures do not depend on grounding content. Assets counted as
reused must still have an owner and review date in the scenario catalogue.

## Security and privacy considerations

Champion tracker data is personal data. Report only aggregates above the minimum group size, restrict stage-level data
to the participant and programme team, set retention, and agree any use of Champion data with HR. Data protection
questions end with the organisation's DPO.

## Responsible AI considerations

Measures must not create incentives for indiscriminate AI use. Never count usage volume as contribution, and never use
Champion measures to judge individuals' performance.

## Evaluation requirements

Not applicable as solution evaluation, because this skill defines programme measures rather than an AI solution. The
measure set is checked by confirming each measure has a definition, source, owner and baseline or a planned date.

## Value measures

This skill defines the measures. The measure set itself is owned by the Champions programme owner and judged by whether
the sponsor and CoE use it to make decisions, reviewed at the periodic programme health check.

## Scale notes

### Starter

Four or five measures from the tracker and community, reported twice a year to the sponsor in a short note.

### Scale

Six to eight defined measures with baselines, a quarterly report to the sponsor and CoE, and a dashboard with access
controls.

### Enterprise

A shared measure set across regional programmes with common definitions, aggregated reporting into the CoE scorecard,
and local reporting within the same rules.

## Hand-offs

- To `champions:recognition-and-progression` for the regular health rating that uses these measures.
- To `champions:champions-health-check` for the periodic programme review.
- To `ai-centre-of-excellence:coe-kpi-framework` to place Champion measures in the CoE scorecard.
- To `copilot-adoption:adoption-measurement` for team-level adoption context.

## Reviewer gates

Not applicable as a formal gate, because programme measures do not release an AI solution; handling of Champion data
follows the organisation's existing data protection controls and the DPO's advice.

## Failure modes

- Measures count posts, attendance and usage, so the programme rewards visibility over capability.
- A leader board is published, most Champions disengage, and a few game the numbers.
- Adoption gains are claimed as the programme's doing, and credibility suffers when challenged.
- Definitions are never agreed, so numbers shift between reports and nobody trusts them.
- Boundary drift is not measured and is discovered only when Champions burn out.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Rank Champions or publish individual leader boards or points tables.
- Count Copilot usage volume, posts or attendance as contribution.
- Report below the agreed minimum group size.
- Claim that adoption gains were caused by Champions without evidence.

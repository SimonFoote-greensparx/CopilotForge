---
name: champions-health-check
description: Runs the periodic, usually annual, review of a whole Champions programme - purpose, sponsorship, manager time agreements, boundaries, framework currency against product change, coverage, community and measures - ending in a decision to renew, reshape or close it, with renewed commitments and a refreshed charter. Use when the charter review date arrives, when the sponsor or operating model changes, or when the programme has drifted.
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

# Champions health check

## Purpose

Champions programmes rarely fail suddenly; they fade. Sponsors move on, manager agreements lapse, the capability
framework falls behind the product, and the network drifts into support work or quiet inactivity. This skill runs a
periodic review of the whole programme, usually once a year or when something significant changes, and ends in an
explicit decision: renew it, reshape it or close it well. Renewal means fresh commitments from the sponsor and managers
and a charter that reflects current practice. Health checks usually go wrong when they become a celebration of
headcount, when they avoid the decision, or when they judge individual Champions instead of the programme.

## When to use

- The programme charter has reached its review date.
- The executive sponsor, programme owner or operating model has changed.
- Copilot and agent capabilities have moved on and the capability framework or Challenge options may be out of date.
- Regular health ratings have shown the same Watch or Act areas for several periods.
- The sponsor or CoE questions whether the programme still earns the time it asks of people.

## When not to use

- The regular, often quarterly, health rating and individual status renewal - use `champions:recognition-and-progression`.
- Defining the programme measures and their rules - use `champions:champion-metrics`.
- Redesigning the programme from first principles after a decision to reshape - use `champions:champion-programme-design`.
- Assessing the maturity of the Centre of Excellence as a whole - use `ai-centre-of-excellence:coe-maturity-assessment`.
- Deciding whether to scale or stop an individual AI solution - use `opportunity-management:scale-or-stop`.

## Questions to ask first

1. What did the charter say the programme would achieve, and what has the sponsor seen it achieve?
2. Is the sponsor still active, and do managers still honour the agreed time?
3. Are the capability framework, learning and Challenge options current with the Copilot experiences people now have?
4. What do the programme measures and recent health ratings show, and where have Act ratings persisted?
5. What do Champions, managers and the teams they support say, gathered in a way that protects individuals?
6. Has anything changed in the operating model, such as a new CoE, a reorganisation or a change in agent governance, that alters the programme's place?

## Required inputs

- The current `champion-programme-charter`, including purpose, boundaries, time commitment and review date.
- Programme measures and recent health ratings from `champions:champion-metrics` and `champions:recognition-and-progression`.
- The capability framework, Challenge catalogue and learning map, with their last review dates.
- Feedback from Champions, managers and supported teams, collected anonymously or in aggregate.
- The current adoption plan and CoE operating model, to check the programme's position between them.

If measures are missing, run the review on qualitative evidence and record the gap as an action, rather than delay. If
the sponsor is no longer active, that is itself the first finding.

## Decision framework

Review eight areas and rate each Healthy, Watch or Act with evidence.

| Area | Question | Typical evidence |
|---|---|---|
| Purpose and outcomes | Does the programme still serve the purpose in its charter, and is that purpose still right? | Sponsor view, outcomes against charter |
| Sponsorship | Is the sponsor visibly active? | Showcases attended, messages, decisions taken |
| Time and managers | Are manager agreements current and honoured? | Champion pulse, lapsed agreements, recruitment patterns |
| Boundaries | Has the network drifted into support, training or approvals? | Drift measures, support themes, community review |
| Framework currency | Do capabilities, learning and Challenges match current Copilot and agent practice? | Last review dates, product changes since, assessor feedback |
| Coverage and journey | Are targets met and is the journey flowing? | Coverage, conversion, completion time |
| Community | Is peer learning alive and owned? | Peer answers, rituals, community manager in place |
| Contribution | Are Champions creating reusable value and routing good ideas? | Challenge outputs, asset reuse, opportunities routed |

Turn the ratings into a decision.

| Decision | Choose when |
|---|---|
| Renew | Most areas Healthy, any Act areas have credible actions and owners |
| Renew with changes | Purpose holds, but framework, boundaries or time agreements need material updates |
| Reshape | Purpose or position in the operating model has changed, or several areas are Act with structural causes |
| Close | The purpose has been met or absorbed elsewhere, or sponsorship and time cannot be secured |

## Practitioner approach

Schedule the health check from the charter, not from a crisis. A fixed review date, typically annual, makes the review
routine rather than threatening, and lets the sponsor plan for a decision. Trigger an earlier review when the sponsor,
operating model or product landscape changes significantly.

Gather evidence before the conversation. Pull the measures and recent health ratings, check the review dates on the
framework, learning and Challenge catalogue, and list the material product changes since they were written. Run a
short anonymous pulse with Champions and managers, asking about time, boundaries, usefulness and what should change.
Speak to a few teams that Champions support. Report everything at programme level.

Look hard at the four areas that decay silently. Sponsorship fades when the sponsor's attention moves; manager time
agreements lapse without anyone deciding; boundaries erode as support gaps push work onto Champions; and the framework
ages as Copilot changes. These are the usual root causes behind falling conversion or a quiet community, so check them
before tuning anything else.

Hold a review session with the sponsor, the programme owner, a CoE representative and a few Champions. Walk through the
ratings, agree the causes and make the decision explicitly. Avoid letting the session become a celebration of headcount;
recognition belongs in showcases, and this meeting is about whether the programme still earns its time.

Renew properly. A decision to renew means fresh commitments: the sponsor confirms their role for the next period,
managers reconfirm Champions' time, the charter is updated with any changes to boundaries, framework or Challenges, and a
new review date is set. Update the champion guide and any advisor at the same time, so participants see the current
rules.

Reshape when the purpose or the operating model has moved. A programme that started to spread basic Copilot use may now
need to focus on agents, specific roles or frontline coverage. Hand the redesign to
`champions:champion-programme-design` with the review's findings, rather than patching the old charter.

Close well when that is the right answer. A programme whose purpose has been absorbed into normal ways of working, or
that cannot secure sponsorship and time, should close deliberately: thank Champions publicly, preserve reusable assets
in the scenario catalogue, close or archive the community, apply retention to Champion records, and tell managers.
A well-closed programme leaves goodwill for whatever comes next.

## Outputs

- A programme health check report with ratings, evidence, root causes and the decision, recorded in the health check section of the `champion-programme-charter` template.
- A refreshed charter with renewed sponsor and manager commitments and a new review date, or a reshape brief, or a closure plan.
- An action list with owners and dates for every Watch and Act area.
- Updates to the `champion-guide` and any advisor, reflecting the renewed programme.

## Microsoft platform considerations

The framework currency check depends on how Copilot, Copilot Cowork and agent tools have changed since the last review.
Compare the capability framework, learning and Challenge options with current capability and governance, using
`references/sources.md` rather than memory, and note where agent-building approval has changed.

## Adoption considerations

The health check should read Champion coverage alongside adoption indicators by team, as context. Share findings with
the adoption lead so any reshaping of the programme fits the next phase of the adoption plan.

## Knowledge considerations

The review checks that the champion guide, framework, learning materials and catalogue entries have owners and current
review dates, and retires superseded material so participants and any advisor are not working from old rules.

## Security and privacy considerations

Pulse responses and Champion records are personal data. Collect feedback anonymously or in aggregate, report above the
minimum group size, and, on closure, apply the retention rules to all programme records. Data protection questions end
with the organisation's DPO.

## Responsible AI considerations

Check that the programme still models responsible practice: verification, accountability, and routing of higher-risk
ideas to intake. If Challenges or community examples have drifted towards building ungoverned agents, record it as an
Act area.

## Evaluation requirements

Not applicable as solution evaluation, because this skill reviews a people programme rather than an AI solution. The
health check is complete when every area has a rating with evidence and every Act area has an owner and date.

## Value measures

Owned by the Champions programme owner and reported to the sponsor: the share of areas rated Healthy, actions closed
since the previous review, renewal of sponsor and manager commitments, and the programme measures defined in
`champions:champion-metrics`. Programme level only, never individual rankings.

## Scale notes

### Starter

An annual conversation between the sponsor and programme owner using the eight areas, a short Champion pulse, and a
one-page decision and action list.

### Scale

An annual review with evidence pack, Champion and manager pulse, a review session including Champions and the CoE, and
a refreshed charter.

### Enterprise

A coordinated review across regional programmes on a shared framework, with local findings rolled up to the CoE, a
consistent decision record and shared changes to the framework and guide.

## Hand-offs

- To `champions:champion-programme-design` when the decision is to reshape.
- To `champions:capability-framework` and `champions:champion-learning` when the framework or learning is out of date.
- To `champions:champion-recruitment` when coverage or manager agreements need rebuilding.
- To `ai-centre-of-excellence:coe-operating-model` when the programme's place in the operating model has changed.

## Reviewer gates

Not applicable as a formal gate, because a programme review does not release an AI solution; handling of pulse and
Champion data follows the organisation's existing data protection controls.

## Failure modes

- The review counts heads, celebrates and avoids the decision, so decline continues.
- Sponsorship and manager time are assumed rather than reconfirmed, and quietly lapse.
- The framework is not checked against product change, and Champions are verified on outdated practice.
- The review drifts into judging individual Champions, and trust in the programme is damaged.
- A programme that should close lingers, consuming time and goodwill.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Rate or rank individual Champions in the programme review.
- Renew the programme without reconfirming sponsor and manager commitments.
- Treat closing a programme that has served its purpose as failure.
- Report pulse feedback in a way that identifies individuals.

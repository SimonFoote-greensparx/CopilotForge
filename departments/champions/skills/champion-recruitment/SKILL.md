---
name: champion-recruitment
description: Recruits a representative, motivated Champion cohort - coverage targets by team, site and persona, an open expression of interest on declared interest, skills and availability, manager agreement before acceptance, fair selection without performance data, a waiting list and a welcome. Use when a Champions programme opens, when the network is all enthusiasts from one function, or when Champions joined without manager agreement.
license: CC-BY-4.0
metadata:
  department: champions
  lifecycle: Mobilise, Enable, Scale
  maturity: explorer, adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-champion-programme, ms-champion-best-practice, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# Champion recruitment

## Purpose

A Champions network is only as useful as its spread. If every Champion sits in the same function, the same building or
the same enthusiasm bracket, large parts of the organisation have nobody to turn to. This skill recruits a cohort that
covers the teams, locations and personas the programme needs, from people who want the role and whose managers have
agreed the time, and welcomes them into the journey with a clear guide. It usually goes wrong when recruitment is an
all-staff email that attracts the already-converted, when managers nominate people who did not ask, when time is
never agreed, or when selection drifts into judging people on performance or seniority.

## When to use

- A Champions programme has been designed and is ready to open for its first cohort.
- The existing network is concentrated in a few functions or sites, and coverage gaps are visible.
- Champions have joined without their managers' agreement and are struggling to find time.
- A new business unit, region or frontline audience needs Champions before its launch wave.
- Interest far exceeds, or falls well short of, the number of Champions the programme can support.

## When not to use

- Designing the programme's purpose, boundaries, journey and charter - use `champions:champion-programme-design`.
- Designing the community space and rituals new Champions join - use `champions:champion-community-design`.
- Designing the learning that supports the journey - use `champions:champion-learning`.
- Building a change network of agents and sponsors alongside Champions - use `change-and-communications:change-network`.
- Selecting pilot participants for a new capability - use `champions:recognition-and-progression`.

## Questions to ask first

1. Which teams, locations and personas need Champion coverage, and which are priorities for the next launch wave?
2. What time commitment has the charter set, and how will each Champion's manager confirm it?
3. How many Champions can the programme owner, community and learning offer genuinely support in this cohort?
4. Which channels reach the audiences that are usually missed, such as frontline, part-time and remote staff?
5. What has HR agreed about how Champion activity is described and what information the programme may hold?

## Required inputs

- The programme charter from `champions:champion-programme-design`, including boundaries, time commitment and journey.
- The audience model from `copilot-adoption:audience-segmentation`, to set coverage targets.
- The launch sequence from `copilot-adoption:launch-plan`, so Champions are in place before their team's wave.
- HR's position on volunteering, time allocation and the personal data the programme may hold.
- The champion guide, drafted on the `champion-guide` template, ready to publish with the call for interest.

If the charter has not set a time commitment, do not recruit; people will join on goodwill and lapse. If HR has not
agreed what information may be held, collect only name, team, location, declared interest, declared skills and
availability, and record the question for the DPO.

## Decision framework

Set coverage targets before inviting anyone. Targets are about spread, never about individuals.

| Coverage dimension | Target expressed as |
|---|---|
| Teams or functions | At least one Champion per team or group of small teams in scope |
| Locations and sites | Each significant site, including frontline sites, has a Champion within reach |
| Personas | Desk, hybrid and frontline audiences each represented |
| Launch waves | Champions in place before their audience's wave starts |
| Languages | Where audiences work in other languages, Champions who can support them |

Select fairly, using declared information only.

| Use | Never use |
|---|---|
| Declared interest and motivation in the person's own words | Performance ratings, talent or succession lists |
| Declared skills and experience with Copilot or similar tools | Individual Copilot usage data |
| Availability and manager agreement to the time | Seniority as a qualification or barrier |
| Contribution to coverage of an under-represented team, site or persona | Age, gender or other personal characteristics |

When interest and capacity do not match:

| Situation | Response |
|---|---|
| More interest than capacity | Prioritise coverage gaps, then offer the waiting list and open learning sessions to everyone else |
| Gaps in key teams or sites | Ask the business owner and manager to suggest people and invite them personally; never conscript |
| Manager declines the time | Record it, offer open learning sessions, and revisit next cohort; escalate patterns to the sponsor |

## Practitioner approach

Start from the coverage map. Lay the audience model alongside the launch sequence and mark where Champions are needed
first. This turns recruitment from a popularity exercise into a coverage plan, and gives the sponsor a clear view of
where help is needed.

Publish the role honestly. Before asking for interest, publish the champion guide: what Champions do and do not do,
the time commitment, the journey, how capability is verified, what recognition opens up and how to step back. People
who read it and still want to join are the ones who stay. Avoid selling the role as an exclusive club or as a route to
promotion.

Use several channels. An all-staff message reaches people who read all-staff messages. Add business-unit leaders'
own messages, team meetings, frontline huddles, existing communities and personal invitations from managers in teams
with gaps. Make the expression of interest short: team, location, why they are interested, what they already do with
Copilot, and the time they can give.

Get manager agreement before accepting anyone. A short, standard manager confirmation, covering the time, the
boundary and what the manager can expect, prevents the most common reason Champions lapse. Where a manager declines,
respect it, record the pattern at team level, and raise repeated refusals in an area with the sponsor rather than with
the individual.

Select openly and fairly. Use the criteria in the decision framework and record decisions against coverage, not
against people. Experienced users are welcome but not required; the capability framework provides a training route for
those still learning. Tell everyone the outcome promptly, and offer people not selected a place on the waiting list and
open access to learning sessions.

Welcome the cohort properly. A short induction from the programme owner and, ideally, the sponsor; access to the
community channel; the first learning session in their diary; and a clear first step on the journey. Ask each new
Champion to agree with their manager how they will use the time in their first month.

Recruit continuously at a modest pace after the first cohort. People change roles, step back and leave. A small,
regular intake keeps coverage healthy and avoids the cycle of big drives followed by decline.

## Outputs

- A coverage map with targets by team, location, persona and launch wave, and the gaps to fill.
- A published champion guide on the `champion-guide` template, used as the call for interest and the participant's reference.
- An expression of interest and a manager confirmation, both in the `champion-guide` template.
- A cohort record held in the restricted progress tracker set up by `champions:evidence-assessment`, with selection decisions recorded against coverage.
- A welcome and induction plan for each cohort.

## Microsoft platform considerations

Not applicable as platform design, because recruitment is a people process. Use the organisation's existing forms,
collaboration and community tools, keep the expression of interest data in an access-controlled location, and check
`references/sources.md` for Microsoft's current Champion programme guidance.

## Adoption considerations

Recruitment should follow the adoption plan: Champions are recruited ahead of their audience's launch wave, and coverage
gaps are reported alongside adoption gaps so the sponsor can see where support is thin.

## Knowledge considerations

The champion guide is the knowledge source for prospective Champions and for any advisor agent, so give it an owner, a
version and a review date, and update it whenever the charter, journey or time commitment changes.

## Security and privacy considerations

Expressions of interest and cohort records are personal data. Collect only what selection and coverage need, restrict
access, set retention, and tell applicants what is held and why. Data protection questions end with the organisation's
DPO.

## Responsible AI considerations

Selection must be fair and explainable: declared information only, applied consistently, with no use of performance
or usage data. Check the cohort for unintended exclusion, for example of part-time, frontline or remote colleagues, and
adjust channels rather than lowering the role's expectations.

## Evaluation requirements

Not applicable as solution evaluation, because recruitment is a people process rather than an AI solution. Each cohort
is reviewed against its coverage targets and manager agreement rate.

## Value measures

Owned by the Champions programme owner, with a baseline at the first cohort: coverage against targets by team, site and
persona, manager agreement rate, time from expression of interest to welcome, and retention after the first quarter.
Reported at programme level above the minimum group size, never as individual rankings.

## Scale notes

### Starter

One cohort, a published guide, a simple form and manager confirmation, with the programme owner inviting people
personally in teams with gaps.

### Scale

Coverage targets by business unit and wave, multiple channels, local leads helping to fill gaps, and a quarterly intake.

### Enterprise

Regional cohorts on a shared guide and criteria, local language channels, frontline recruitment through supervisors,
and coverage reporting to the CoE.

## Hand-offs

- To `champions:champion-community-design` to welcome the cohort into the community.
- To `champions:champion-learning` to place new Champions on the learning offer.
- To `champions:evidence-assessment` to set up each Champion in the progress tracker.
- To `champions:champion-metrics` for coverage and retention measures.
- To `champions:champion-advisor` so the advisor grounds on the published champion guide.

## Reviewer gates

Not applicable as a formal gate, because recruitment does not release an AI solution; handling of applicant data
follows the organisation's existing data protection controls.

## Failure modes

- Recruitment by all-staff email produces a cohort of enthusiasts from a few functions and no frontline coverage.
- Champions join without manager agreement, cannot find time and lapse within months.
- Managers nominate people who did not want the role, and the network fills with reluctant members.
- Selection uses performance or seniority, and the programme is seen as a talent scheme for a favoured few.
- A single big recruitment drive is never repeated, and coverage decays as people move on.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Use performance ratings, talent lists or individual usage data to select Champions.
- Accept a Champion without their manager's agreement to the time.
- Conscript people into the role.
- Promise that the Champion role leads to promotion or pay without HR's explicit agreement.

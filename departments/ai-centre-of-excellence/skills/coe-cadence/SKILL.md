---
name: coe-cadence
description: Sets the meeting cadence and terms of reference for an AI CoE - a weekly working group, monthly steering where the sponsor decides, a quarterly strategy review and a community forum - with agendas, a decision log and sizing by edition. Use when a new CoE needs its forums set up, when meetings have become status updates that decide nothing, or when decisions are being taken in corridors and nobody can find them later.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Mobilise, Scale, Measure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-coe-starter-kit, ms-champion-programme
  status: draft
  authors: Simon Foote
---

# CoE cadence

## Purpose

A CoE shows its value in the decisions it takes, and decisions need forums with a clear purpose, the right inputs and a
record. This skill sets the rhythm of steering, portfolio and design review, community and value review, with terms of
reference, agendas and a decision log. Cadence goes wrong when every meeting becomes a status update, when the same
people attend everything, or when forums meet so rarely that teams build around them.

## When to use

- A CoE or AI working group has a charter and needs its forums set up.
- Meetings have become reporting sessions and decisions are not being taken.
- Release or prioritisation decisions are taken informally and cannot be traced.
- The organisation is moving edition and the rhythm must change.
- The sponsor asks how they will know the CoE is working.

## When not to use

- Agreeing the CoE's purpose and decision rights - use `ai-centre-of-excellence:coe-charter`.
- Assigning who is accountable for each decision - use `ai-centre-of-excellence:coe-raci`.
- Defining the measures that the value review looks at - use `ai-centre-of-excellence:coe-kpi-framework`.
- Running the Champion community's own events and challenges - use `champions:champion-challenges`.
- Programme governance for a wider transformation (stage gates, RAID, supplier management) - the `programme-management` department (planned).

## Questions to ask first

1. Which decisions does the charter assign to the CoE, and how often do they arise?
2. How quickly does a team need a decision on a tier 1 or tier 2 request before it loses patience and builds anyway?
3. Which existing meetings (leadership team, architecture board, information security forum) could absorb an agenda item instead of a new meeting?
4. Who will prepare the papers and keep the decision log, and how much time do they have?
5. How often will the sponsor genuinely attend?

## Required inputs

- The charter and its decision rights, from `ai-centre-of-excellence:coe-charter`.
- The RACI, from `ai-centre-of-excellence:coe-raci`, showing which forum holds each decision.
- The operating model's flow, from `ai-centre-of-excellence:coe-operating-model`, which sets how often triage is needed.
- The scorecard, from `ai-centre-of-excellence:coe-kpi-framework`, for the value review.

If the RACI is not yet agreed, set up the steering forum first and make agreeing the RACI its first decision. Mark
dates, attendees and chairs `[To confirm]` until the sponsor agrees them.

## Decision framework

Create a forum only if it has decisions to take. A typical starting rhythm for a business-owned CoE is three decision
forums and one sharing forum; durations are starting points to adjust, not rules.

| Forum | Typical length | Standing agenda | Decisions it takes |
|---|---|---|---|
| Working group (portfolio and design review) | 30 minutes weekly | New opportunities, delivery updates, risks, knowledge gaps | Intake triage, routing, risk tier, release up to delegated tier |
| Steering committee, sponsor mandatory | 60 minutes monthly | Return achieved against baseline, priority decisions, funding requests, new opportunities above delegated limits, escalations | Priorities, funding, risk acceptance, escalations |
| Strategy review | 90 minutes quarterly | Roadmap, adoption, value delivered, future priorities | Roadmap changes, scale-or-stop, next quarter's focus |
| Community | Informal, monthly | Real work shown by Champions, what failed, new ideas to intake | None (sharing forum) |

Size the rhythm by edition.

| Forum | Starter | Scale | Enterprise |
|---|---|---|---|
| Working group | Fortnightly or monthly, often merged with steering | Weekly | Weekly in each spoke; hub fortnightly for tier 3-4 |
| Steering | A decision slot at the monthly working group, sponsor present | Monthly, sponsor chairs | Monthly per spoke; quarterly executive board |
| Strategy review | Twice a year | Quarterly | Quarterly per spoke, annual review of the whole portfolio |
| Community | Informal channel | Monthly call led with Champions | Per business unit, with a quarterly cross-unit event |

Each forum must answer three tests. Does it have decisions only it can take? Are its inputs ready before it meets? Does
it publish what it decided within two working days? A forum that fails all three should be merged or stopped.

## Practitioner approach

Start from the decisions, not the calendar. Take the RACI and group its decisions by how often they arise and who must be
present. Fast, frequent decisions (triage, routing, tier 1 registration) need a short, regular slot with delegated
authority: the weekly working group. Slow, consequential decisions (priorities, funding, tier 3 and 4 acceptance) need
the sponsor: the monthly steering committee. Direction and value need a longer, less frequent look: the quarterly
strategy review. Learning and sharing need a community forum that is not a decision forum at all.

Make the sponsor's attendance at steering a condition of the charter, not a courtesy. The sponsor is there to decide,
not to receive a report; if they cannot attend, a named delegate with authority to decide attends instead. A steering
committee that meets without its decision maker is a status meeting, and teams will notice within two cycles.

Write terms of reference for each forum on one page: purpose, decisions it takes, decisions it recommends, chair and
members by role, quorum, frequency, inputs required and by when, outputs and where they are published. Keep membership
small; invite contributors to items rather than to the whole meeting.

Design agendas around decisions. The working group moves through new opportunities against intake criteria, delivery
updates by exception, risks and the knowledge gaps blocking work. Steering opens with return achieved against baselines
from the scorecard, then priority decisions and funding requests with papers, new opportunities above delegated limits
and escalations. The strategy review looks at the roadmap, adoption, value delivered and future priorities, and takes
scale-or-stop decisions with `opportunity-management:scale-or-stop`. The community forum shows real work.

Set up the decision log before the first meeting. Each entry records the decision, the options considered, the rationale,
the deciding role, the date, any conditions and the review date. Publish it in the CoE's collaboration space, because a
visible log stops the same question being reopened.

Protect the cadence from drift. Papers not received by the deadline move to the next meeting; status updates go in a
written note, not airtime; any meeting with no decisions on its agenda is cancelled. Review the cadence after three
cycles and whenever the edition or operating model changes.

For Starter organisations, one meeting with a standing agenda can cover triage, community and steering together, with
the sponsor present for the decision segment. That is a complete cadence, not a cut-down one.

## Outputs

- Terms of reference for each forum, in the cadence section of the `coe-charter` template.
- A twelve-month calendar showing forum dates, paper deadlines and the sponsor's attendance.
- Standing agendas for the weekly working group, monthly steering committee, quarterly strategy review and community forum.
- A decision log structure, with the first entries recorded.

## Microsoft platform considerations

Use the collaboration tools the organisation already runs for papers, the decision log and the community channel. If
meeting recap or summarisation features are used to draft minutes, a named person still checks and publishes the
decision record. Feature availability changes, so check `references/sources.md` before recommending a specific feature.

## Adoption considerations

The community forum is an adoption instrument: it shows peers using AI in real work and gives Champions a stage. Keep it
separate from decision forums so people feel free to share what went wrong.

## Knowledge considerations

The decision log and terms of reference are organisational knowledge with an owner (usually the CoE lead) and a review
date. Approved prompts and patterns shared in community forums should be captured in a maintained library, not left in
chat history.

## Security and privacy considerations

Papers for tier 2 and above releases include the `security-privacy` review outcome; the forum cannot approve release
while a blocking finding is open. Keep personal data out of papers and logs.

## Responsible AI considerations

The steering forum is where tier 3 and 4 risk is accepted or refused. Record the accountable executive's decision and
conditions in writing, and revisit them at the value review.

## Evaluation requirements

Not applicable to the cadence itself; the portfolio and design review should still confirm evaluation evidence exists
before any tier 2 or higher release is approved.

## Value measures

Track decision cycle time, the share of agenda time spent on decisions rather than updates, whether the deciding role
(sponsor or delegate) was present at each steering meeting, and the number of reopened decisions. The CoE lead owns these, reported through
`ai-centre-of-excellence:coe-kpi-framework`. Never report individual attendance as a performance measure.

## Scale notes

### Starter

One working-group meeting, fortnightly or monthly, with a standing agenda, a sponsor decision slot, a shared decision
log and a strategy review twice a year. Community is an informal channel.

### Scale

A weekly 30-minute working group, monthly 60-minute steering with the sponsor, a quarterly 90-minute strategy review and
a monthly community call, each with one-page terms of reference. Treat the timings as a starting point.

### Enterprise

Spoke forums mirror the hub's, with delegated authority; the hub adds an executive board quarterly and an annual
portfolio review. Formal assurance overlays require minutes with evidence references at each gate.

## Hand-offs

- To `ai-centre-of-excellence:coe-kpi-framework` for the scorecard the value review uses.
- To `opportunity-management:opportunity-prioritisation` for the triage method.
- To `opportunity-management:scale-or-stop` for value review decisions.
- To `champions:champion-programme-design` to align community events with the Champion programme.

## Reviewer gates

Not applicable as a release gate, because cadence organises decisions rather than releasing a solution. The
portfolio and design review must not approve a release that `security-privacy` has blocked.

## Failure modes

- Steering becomes a monthly status report and the sponsor stops attending, or sends a delegate who cannot decide.
- Triage meets monthly, so teams wait six weeks for a tier 1 decision and build around the CoE.
- Decisions are not logged and are reopened by whoever missed the meeting.
- The community forum is turned into a decision forum and people stop sharing failures.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Create a forum that has no decisions to take.
- Let a forum approve a release while a blocking reviewer finding is open.
- Leave decisions unrecorded or unpublished.
- Use attendance or meeting participation to judge individuals.

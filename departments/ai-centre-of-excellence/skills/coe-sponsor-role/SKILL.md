---
name: coe-sponsor-role
description: Defines the executive sponsor's role in an AI Centre of Excellence - the decisions only the sponsor takes, time and attendance, a delegate with real authority, visible support for adoption, and what happens when sponsorship fades - and secures the sponsor's written commitment. Use when a CoE needs a sponsor, when the sponsor only receives reports, or when steering keeps deferring decisions upwards.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Mobilise, Launch, Improve
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-champion-programme, nist-ai-rmf, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# CoE sponsor role

## Purpose

The sponsor is the single biggest predictor of whether a CoE takes decisions or just reports activity. This skill
defines what the CoE's executive sponsor decides, how much time that takes, who may act in their absence and how they
support adoption in the business, then secures a written commitment the sponsor actually agrees with. Sponsorship goes
wrong when the role is honorary, when the most senior available name is chosen rather than the executive whose
outcomes depend on the CoE, and when nobody notices the sponsor has quietly stopped attending.

## When to use

- A CoE or AI working group is being set up and needs an executive sponsor.
- A sponsor has been named but receives updates rather than taking decisions.
- Steering repeatedly defers priority, funding or risk decisions to "take offline".
- The sponsor is changing role or leaving, and the CoE needs a handover rather than a gap.

## When not to use

- Securing an executive sponsor for the whole AI programme or transformation - use `ai-strategy:executive-sponsorship`.
- Helping executives use Copilot personally and lead adoption by example - use `copilot-adoption:executive-enablement`.
- Recording the sponsor's commitments as part of the full CoE charter - use `ai-centre-of-excellence:coe-charter`.
- Assigning accountability for each activity across the AI lifecycle - use `ai-centre-of-excellence:coe-raci`.
- Setting the steering committee's agenda and decision log - use `ai-centre-of-excellence:coe-cadence`.

## Questions to ask first

1. Whose business outcomes most depend on the CoE succeeding, and is that the person being proposed as sponsor?
2. Which decisions will the CoE need taken in its first six months that nobody below the sponsor can take?
3. How much time can the sponsor give each month, and will they attend steering in person or through a delegate?
4. Who could act as delegate with genuine authority to decide, not just to listen?
5. Is there already a programme-level sponsor for AI, and how will the CoE sponsor relate to them?

## Required inputs

- The draft charter or its purpose and decision rights, from `ai-centre-of-excellence:coe-charter`.
- The strategic outcomes the CoE serves, from `ai-strategy:strategic-outcomes`.
- The proposed steering cadence, from `ai-centre-of-excellence:coe-cadence`, if it exists.
- Any programme-level sponsorship arrangement, from `ai-strategy:executive-sponsorship`.

If the outcomes are missing, the sponsor conversation still happens, but its first agreed action is to own them. Never
record a commitment the sponsor has not stated in their own words.

## Decision framework

Choose the sponsor by fit, not seniority alone. The best sponsor owns outcomes the CoE will move and has authority over
the resources it needs.

| Test | Good sign | Warning sign |
|---|---|---|
| Outcome ownership | The CoE's outcomes appear in the sponsor's own objectives | The sponsor's area gains nothing directly |
| Authority | Can reallocate people and budget across the units involved | Must escalate every resourcing request |
| Availability | Agrees a monthly steering slot and a stated time each month | Offers to "be kept informed" |
| Visibility | Willing to use and talk about AI in their own work | Delegates all communication |
| Continuity | Expects to stay in role through the first year | Already planning to move on |

Separate what only the sponsor decides from what they delegate.

| Decision | Sponsor | Delegate may decide | CoE lead decides |
|---|---|---|---|
| Priorities between competing business units | Yes | With sponsor's prior guidance | No |
| Funding and people beyond the CoE's agreed budget | Yes | No | No |
| Acceptance of residual risk at tier 4 | Yes | No | No |
| Acceptance of residual risk at tier 3 | Yes | If named in the charter | No |
| Conflicts between teams the CoE cannot resolve | Yes | Yes | No |
| Priorities within the agreed backlog | Sets direction | Yes | Yes, within direction |
| Stopping a solution after a scale-or-stop review | Ratifies | Yes | Recommends |

If no candidate passes at least outcome ownership and authority, recommend an AI working group sponsored at the level
that can still decide, rather than a CoE with an absent figurehead.

## Practitioner approach

Begin by naming the decisions, not the person. List what the CoE will need decided in its first six months: which
business unit's ideas go first, whether to fund a partner build, who releases a tier 3 solution, what to do when two
departments want the same Champion's time. Then ask who can actually take those decisions. That answer usually narrows
the field to one or two executives.

Meet the candidate with that list. Explain that the role is an active one: chairing or attending monthly steering,
making priority calls, removing blockers the CoE cannot clear, securing people and time, resolving conflicts between
teams and accepting residual risk where the governance model says the sponsor must. Ask how much time they can give and
write down the figure they offer. A typical sponsor commitment is a monthly steering meeting plus a short regular
check-in with the CoE lead, but let the sponsor state what is real.

Agree a delegate early. Absence is normal; a delegate who can only take notes is the problem. Record what the delegate
may decide and which decisions wait for the sponsor. Write the escalation route for anything urgent between meetings.

Agree the sponsor's visible role in adoption. People take their cue from what executives do, not what they sign. Ask
the sponsor to use Copilot or an agent in their own work and say so, to open the first community session and to
celebrate a real success story. Route personal enablement to `copilot-adoption:executive-enablement`, because a
sponsor who has never used the tools cannot speak credibly about them.

Write the commitment on one page: decisions owned, time, delegate and their authority, adoption actions, how the
sponsor will be briefed and how the sponsorship will be reviewed. Ask the sponsor to edit it into their own words and
agree it. Copy the agreed commitments into the sponsorship section of the `coe-charter` template.

Build in a health check. At each quarterly strategy review, the CoE lead records whether the sponsor attended or sent
an empowered delegate, how many decisions were taken versus deferred, and whether any blocker waited more than one
cycle. Two quarters of drift is the trigger for an honest conversation, then either a renewed commitment or a change
of sponsor. When the sponsor changes role, plan a handover meeting and a refreshed commitment rather than letting the
role lapse.

Where a programme-level sponsor already exists, agree how the two relate: the CoE sponsor owns CoE decisions, and the
programme sponsor arbitrates when CoE priorities collide with wider programme commitments.

## Outputs

- A sponsor role profile: decisions owned, decisions delegated, time commitment, adoption actions, briefing arrangements.
- A sponsor commitment record, agreed in the sponsor's own words, copied into the sponsorship section of the `coe-charter` template and the sponsor row of the `coe-terms-of-reference` template.
- A delegate authority statement naming what the delegate may decide.
- A sponsorship health check, run quarterly, with the trigger for renewal or change.

## Microsoft platform considerations

Not applicable in depth, because sponsorship is an organisational role rather than a platform decision. Where the
sponsor is asked to model personal use, check which Copilot capabilities they have access to in `references/sources.md`
and route licensing questions to the Microsoft licensing guide or a licensing partner.

## Adoption considerations

The sponsor's visible use and storytelling carry more weight than any campaign. Agree two or three concrete moments in
the first quarter where the sponsor speaks about AI in their own work, and coordinate them with
`change-and-communications:ai-communication-strategy`.

## Knowledge considerations

The sponsor often controls whether knowledge owners get time to maintain content. Ask the sponsor to endorse knowledge
ownership as a launch commitment, so the knowledge pillar is not left to volunteers.

## Security and privacy considerations

Make sure the sponsor understands that accepting residual risk at the top tiers is a personal, recorded decision, and
that information security and the data protection officer advise but do not transfer that accountability.

## Responsible AI considerations

The sponsor is where executive accountability for AI that affects people, money, safety or rights lands. Agree that
risk acceptance is written, dated and reviewable, and that the sponsor will not accept risk the responsible AI review
has marked as blocking without escalation to the accountable executive body.

## Evaluation requirements

Not applicable, because the sponsor role is not an AI output. The sponsorship health check is the evidence that the
role is working.

## Value measures

Measure sponsorship by decisions, not attendance alone: share of steering decisions taken rather than deferred, median
time for a blocker to be resolved, and steering meetings with the sponsor or an empowered delegate present. The CoE lead
owns these measures; baseline them in the first quarter.

## Scale notes

### Starter

The sponsor is often the owner or a director who also leads the working group's decisions. One page and a monthly
half-hour are enough. Keep the delegate as the lead.

### Scale

A business executive sponsors the CoE, chairs monthly steering and names a delegate. The commitment record sits in the
charter and is reviewed at each quarterly strategy review.

### Enterprise

The hub has an executive sponsor and each spoke has its own business-unit sponsor. Agree how hub and spoke sponsors
resolve conflicts, and align both with any programme-level sponsor so decisions are not taken twice.

## Hand-offs

- To `ai-centre-of-excellence:coe-charter` to record the commitments.
- To `ai-centre-of-excellence:coe-cadence` to place the sponsor's decisions in steering.
- To `copilot-adoption:executive-enablement` for the sponsor's personal use of Copilot.
- To `ai-strategy:executive-sponsorship` to align with programme-level sponsorship.

## Reviewer gates

Not applicable, because the sponsor role is an organisational design and releases no solution. The sponsor's own risk
acceptances are subject to the `responsible-ai` and `security-privacy` findings for the solution concerned.

## Failure modes

- The most senior available executive is chosen, owns none of the outcomes and stops attending after two meetings.
- The delegate can only take notes, so every decision waits a month.
- The commitment is written by the CoE and signed without being read, so it describes a role nobody agreed to.
- The sponsor changes role and the CoE runs for a quarter without anyone able to decide.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Name a sponsor who has not agreed, in their own words, to take decisions.
- Treat attendance as sponsorship when decisions are consistently deferred.
- Let the sponsor's risk acceptance override a blocking reviewer finding without written escalation.
- Judge or report on the sponsor's personal performance; review the role's effectiveness, not the person.

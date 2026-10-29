---
name: champion-programme-design
description: Designs an evidence-led Copilot Champions programme - purpose, charter, operating boundaries stating what Champions do and do not do, executive sponsorship, a time commitment agreed with managers, and community design. Use when starting a Champion network, when an existing network has become an unpaid help desk, or when Champion status has come to mean attendance rather than capability.
license: CC-BY-4.0
metadata:
  department: champions
  lifecycle: Mobilise, Enable
  maturity: explorer, adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, copilot-cowork, m365-agents
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-champion-programme, ms-champion-best-practice, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# Champion programme design

## Purpose

A Champions programme spreads practical, responsible AI capability through the organisation by building a community of
colleagues who can show others what good looks like. This skill designs that programme: its purpose, charter,
boundaries, sponsorship, time commitment and community. Programmes usually go wrong by recruiting enthusiasts with no
agreed time, no boundaries and no evidence of capability, so Champions become an unpaid help desk, an informal approval
route for risky ideas, or a badge earned by attending a webinar.

## When to use

- The organisation is launching or expanding Copilot and wants peer-led capability, not only central training.
- An existing Champion network has drifted into answering support tickets or approving solutions.
- Champion status has become a label for attendance and nobody can say what a Champion can actually do.
- A business unit wants its own network and it needs to fit the organisation-wide model.

## When not to use

- Defining the capability levels and evidence a Champion must show - use `champions:capability-framework`.
- Assessing submitted evidence against the rubric - use `champions:evidence-assessment`.
- Designing the practical challenges Champions complete - use `champions:champion-challenges`.
- Recognition, progression, renewal and programme health - use `champions:recognition-and-progression`.
- Planning the wider Copilot launch the Champions support - use `copilot-adoption:launch-plan`.
- Designing the Centre of Excellence that Champions route work to - use `ai-centre-of-excellence:coe-operating-model`.

## Questions to ask first

1. What should the programme achieve for the organisation, in a sentence a sponsor would repeat?
2. Who is the executive sponsor, and who will own and run the programme day to day?
3. How much time can Champions realistically give, and have their managers agreed it?
4. Where do support requests, technical questions and new solution ideas go today, so Champions are not the default for all of them?
5. How many Champions are needed, in which teams, locations and personas?

## Required inputs

- The adoption programme's purpose and scenarios from `copilot-adoption:launch-plan` and `copilot-adoption:scenario-discovery`.
- The existing support model, CoE or intake route, and approved-use guidance.
- A named sponsor and programme owner.
- Organisational policies on volunteering, time allocation and recognition, from HR.

If there is no route for ideas and no support model, record both as preconditions: without them Champions will absorb
every request. If manager agreement to time cannot be obtained, say so plainly in the charter rather than assume it.

## Decision framework

Fix the operating boundary before recruiting anyone. Every charter includes this table, adapted to the organisation.

| Champions do | Champions do not |
|---|---|
| Model responsible AI behaviour in their own work | Replace technical support, architects or formal solution approval |
| Share approved prompts, scenarios, examples and success stories | Own enterprise governance or policy decisions |
| Provide first-line peer guidance in their team | Release high-risk or externally facing solutions without controls |
| Spot opportunities and route them to intake | Become an ungoverned queue for every AI request |
| Support community learning and feedback | Act as the sole owner of adoption or business change |

Then choose a network shape:

| Situation | Shape |
|---|---|
| Fewer than a few hundred people | One community, one owner, roughly one Champion per team |
| Several business units | Hub-and-spoke: central owner and community, local leads per unit |
| Large, multi-region or frontline-heavy | Federated: local networks with shared framework, charter and evidence rubric |

## Practitioner approach

Start with purpose. Ask the sponsor what the organisation will be able to do in a year because Champions exist. Good
answers talk about capability spreading through teams, good ideas reaching the right place and safe habits becoming
normal. Weak answers talk about reducing support tickets, which signals a plan to use Champions as unpaid support.

Write the boundary table next, and test it with the people who own support, architecture, security and governance.
Each "do not" needs somewhere for the work to go instead. Ideas route to `opportunity-management:problem-framing`
through the CoE; technical faults go to the service desk; anything needing approval goes to the owning governance
route. If a destination does not exist, the boundary is aspirational, and the charter must say so.

Agree time with managers before recruiting. A Champion role without protected time becomes evening work for the most
willing people and then quietly lapses. Agree a realistic commitment, often an hour or two a week, with a review after
the first quarter. Put it in the charter and confirm it with each Champion's manager when they join.

Design for evidence, not enthusiasm. Champion status should follow demonstrated capability and practical contribution,
using the levels in `champions:capability-framework`. Offer two routes so the programme is fair: structured learning for
people building capability, and evidence submission for experienced colleagues who can show it already. Recruit on
declared interest, skills and availability, and aim for spread across teams, locations and personas, including
frontline roles.

Design the community. Champions need a place to ask each other questions, share what works and see what is new: a
community channel, a regular call, and a light rhythm of challenges and showcases. Plan who runs it, how often it meets
and how good material moves into the shared scenario catalogue. Keep the community connected to the CoE so patterns
from the field inform priorities.

Secure visible sponsorship. The sponsor should launch the programme, attend a showcase each quarter and thank
contributors publicly. Recognition is designed in `champions:recognition-and-progression`, but the sponsor's attention
is the part money cannot buy.

Write all of this into the charter and review it with the sponsor, HR and the CoE before launch.

## Outputs

- A Champions programme charter on the `champion-programme-charter` template: purpose, sponsor, owner, boundary table, time commitment, routes, network shape, community design and review date.
- A recruitment brief describing the role, time commitment, routes to status and how to express interest.
- A manager briefing explaining the role, the time agreed and what managers can expect.

## Microsoft platform considerations

Champions should work only with tools the organisation has approved for them, such as Copilot Chat, Copilot in the
Microsoft 365 apps, Copilot Cowork or agent building tools where governance allows. Community spaces typically run in
Teams or Viva Engage. Product availability and naming change; check `references/sources.md` and the approved tools list.

## Adoption considerations

The Champion programme is a core adoption mechanism. Align it with launch waves so Champions are ready before their
team's onboarding, and make sure office hours and community calls reinforce the same scenarios.

## Knowledge considerations

Champions often spot stale or missing knowledge first. Give them a simple route to report it to content owners, and
pass systemic issues to the `knowledge-management` department (planned) rather than letting Champions fix content they
do not own.

## Security and privacy considerations

Champions must model the approved-use guidance and know how to report suspected data exposure. They must not be given
broader access or admin rights because of the role, and they must not share examples containing personal or
confidential data.

## Responsible AI considerations

Champions model verification and accountability. The boundary table prevents them from releasing high-risk or
externally facing solutions; any idea touching decisions about people, money or safety goes through intake and risk
classification.

## Evaluation requirements

Not applicable as solution evaluation, because this skill designs a people programme rather than an AI solution. The
charter is checked by confirming every "do not" has a destination route and every Champion has an agreed time
commitment.

## Value measures

Programme-level measures, owned by the programme owner: Champion coverage by team and persona, share of Champions with
verified capability, challenges completed, assets reused and opportunities routed to intake. Never individual rankings.

## Scale notes

### Starter

A handful of Champions, a one-page charter, a shared chat and a monthly call run by the owner. The boundary table
matters as much at this size as at any other.

### Scale

Hub-and-spoke with local leads, a formal charter, both learning and evidence routes, and quarterly showcases with the
sponsor.

### Enterprise

Federated networks with a shared framework and rubric, trained assessors, regional leads and formal links to the CoE and
the change network. Review the charter annually.

## Hand-offs

- To `champions:capability-framework` to define the capability levels and evidence.
- To `champions:champion-challenges` to design the practical challenges.
- To `champions:recognition-and-progression` to design recognition, progression and renewal.
- To `ai-centre-of-excellence:coe-operating-model` to connect Champions to CoE intake and governance.

## Reviewer gates

Not applicable as a formal gate, because the programme itself creates no AI solution; the boundary table ensures any
solution a Champion proposes passes through intake, where risk tiers and reviewer gates apply.

## Failure modes

- No time is agreed with managers, so the most willing people burn out and the network fades.
- Boundaries exist on paper but no destination routes do, so Champions become the help desk and the approval route.
- Status is awarded for attendance, and nobody trusts the badge.
- Champions are concentrated in head office and desk roles, so frontline teams have nobody to turn to.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Use Champions as an unpaid help desk, an approval route or the sole owner of adoption.
- Recruit Champions without a time commitment agreed with their managers.
- Award Champion status for attendance alone.
- Select or exclude Champions on personal characteristics rather than declared interest, skills and availability.

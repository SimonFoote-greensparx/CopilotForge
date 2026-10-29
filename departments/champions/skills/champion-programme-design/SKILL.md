---
name: champion-programme-design
description: Designs an evidence-led Copilot Champions programme as a progression system - purpose, the six-stage journey, operating boundaries, its place between the adoption programme and the Centre of Excellence, sponsorship, agreed time, community, tracker and self-service guidance. Use when starting or replicating a Champion network, when Champions have become an unpaid help desk, or when status means attendance.
license: CC-BY-4.0
metadata:
  department: champions
  lifecycle: Mobilise, Enable
  maturity: explorer, adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, copilot-cowork, m365-agents
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-champion-programme, ms-champion-best-practice, ms-copilot-adoption-hub, ms-agent-builder
  status: draft
  authors: Simon Foote
---

# Champion programme design

## Purpose

A Champions programme spreads practical, responsible AI capability by building a network of colleagues who can show
others what good looks like. This skill designs it as a progression system rather than a volunteer list or a training
calendar: it turns curiosity into verified capability, capability into contribution, and contribution into a
distributed network that helps the organisation adopt AI safely and sustainably. It sets the purpose, journey,
boundaries, position in the operating model, sponsorship, time commitment and the support infrastructure. Programmes
usually go wrong by recruiting enthusiasts with no agreed time, no boundaries and no evidence of capability, so
Champions become an unpaid help desk, an informal approval route, or a badge earned by attending a webinar.

## When to use

- The organisation is launching or expanding Copilot and wants peer-led capability, not only central training.
- An existing Champion network has drifted into answering support tickets or approving solutions.
- Champion status has become a label for attendance and nobody can say what a Champion can actually do.
- A business unit or another organisation wants to replicate a Champions model that has worked elsewhere.
- Every question about requirements and progress lands on one central programme owner, who has become the bottleneck.

## When not to use

- Defining the capabilities, routes and verification criteria - use `champions:capability-framework`.
- Assessing submitted evidence and keeping the progress tracker - use `champions:evidence-assessment`.
- Designing the Champion Challenge options and criteria - use `champions:champion-challenges`.
- Recognition, advanced access, renewal and programme health - use `champions:recognition-and-progression`.
- Designing the self-service advisor agent itself - use `m365-agents:agent-use-case-design`.
- Planning the foundation Copilot launch the Champions support - use `copilot-adoption:launch-plan`.
- Designing the Centre of Excellence that Champions route work to - use `ai-centre-of-excellence:coe-operating-model`.

## Questions to ask first

1. What should the programme achieve, in a sentence a sponsor would repeat, and what behaviours should a Champion demonstrate?
2. Who is the executive sponsor, and who will own and run the programme day to day?
3. How much time can Champions realistically give, and have their managers agreed it?
4. Where do support requests, formal training, solution approvals and new ideas go today, so Champions are not the default for all of them?
5. Is there a foundation adoption programme and a Centre of Excellence or intake route for the Champions to sit between?
6. How many Champions are needed, in which teams, locations and personas?

## Required inputs

- The adoption programme's purpose and scenarios from `copilot-adoption:launch-plan` and `copilot-adoption:scenario-discovery`.
- The existing support model, the CoE or intake route for larger or higher-risk solutions, and approved-use guidance.
- A named sponsor and programme owner.
- Organisational policies on volunteering, time allocation and recognition, from HR.

If there is no route for ideas and no support model, record both as preconditions: without them Champions will absorb
every request. If manager agreement to time cannot be obtained, say so plainly in the charter rather than assume it.
Where a model is being replicated, mark anything taken from the original context as "to confirm" locally.

## Decision framework

Place the programme in the operating model first. Champions occupy the middle layer and must not absorb the other two.

| Layer | Purpose | What it owns |
|---|---|---|
| Foundation adoption programme | Broad access, onboarding and safe everyday use across the workforce | Readiness, launch, onboarding, approved-use guidance, support model |
| Champions programme | Local capability, embedded peer support and practical role-based adoption | Journey, verification, community, challenges, recognition |
| Centre of Excellence | Business-led prioritisation, governance and delivery of larger or higher-risk AI and automation | Intake, risk classification, architecture, release approval |

Design the journey as six stages, each owned by a skill in this department.

| Stage | The participant | Designed in |
|---|---|---|
| 1. Join the community | Declares interest, agrees time with their manager, gains access to resources, events and peers | This skill |
| 2. Verify Chat capability | Shows effective prompting, refinement, use of context and responsible practice | `champions:capability-framework` |
| 3. Verify productivity capability | Creates useful, validated outputs with Copilot across the Microsoft 365 apps | `champions:capability-framework` |
| 4. Verify agent capability | Explains agents, identifies good use cases and, where approved, configures and tests a basic agent | `champions:capability-framework` |
| 5. Complete a Champion Challenge | Delivers one practical contribution that creates value for others | `champions:champion-challenges` |
| 6. Earn recognition and keep contributing | Models responsible use, shares practice and supports colleagues | `champions:recognition-and-progression` |

Fix the operating boundary before recruiting anyone. Every "do not" needs a destination.

| Champions do | Champions do not |
|---|---|
| Model safe, responsible AI behaviour in their own work | Replace technical support or formal training |
| Share prompts, success stories and practical examples | Approve solutions or production releases |
| Give first-line peer guidance in their team | Act as solution architects |
| Promote approved tools and the organisation's AI policies | Own enterprise governance or policy decisions |
| Spot opportunities and route them to the right place | Build high-risk or externally facing solutions outside the Centre of Excellence and its technical controls |
| Take part in the community and give feedback | Become an ungoverned queue for every AI request |

Build these components before launch, not after.

| Component | Minimum before launch |
|---|---|
| Capability framework | Three capabilities with verification criteria and both routes |
| Learning sessions | A recurring calendar open to the wider business, mapped to the journey |
| Community channel | A dedicated space with an owner, a rhythm and moderation |
| Progress tracker | Each participant's status by stage, with restricted access |
| Self-service guidance | Requirements and next milestone explained without the owner; an advisor agent where approved, otherwise a published guide |
| Challenge options and recognition | Published, with assessment criteria and what recognition opens up |

Then choose a network shape: one community with one owner for a few hundred people; hub-and-spoke with local leads
for several business units; federated networks sharing one framework, charter and rubric for large, multi-region or
frontline-heavy organisations.

## Practitioner approach

Start with purpose. Ask the sponsor what the organisation will be able to do in a year because Champions exist, then
turn the answer into the behaviours and business outcomes a Champion should demonstrate. Good answers talk about
capability spreading through teams, good ideas reaching the right route and safe habits becoming normal. Answers about
reducing support tickets signal a plan to use Champions as unpaid support.

Place the programme in the operating model before designing anything else. Champions sit between the foundation
adoption programme, which gives everyone access, onboarding and safe everyday use, and the Centre of Excellence, which
prioritises, governs and delivers larger or higher-risk solutions. Champions scale adoption and find opportunities;
they do not deliver governed solutions. If either neighbour is missing, Champions get pulled into filling the gap.
Record that as a risk in the charter rather than let the network absorb it quietly.

Write the boundary table next and test it with the owners of support, training, architecture, security and
governance. Ideas go to `opportunity-management:problem-framing` through the CoE, faults to the service desk, and
approvals to the owning governance route. A boundary without a destination is aspirational, and the charter must say so.

Agree time with managers before recruiting. A role without protected time becomes evening work for the most willing
people and then quietly lapses. Agree a realistic commitment, review it after the first quarter, and confirm it with
each Champion's manager when they join.

Design the journey as a progression system. Keep the capability areas few, each with explicit verification criteria.
Make training one route, not the gate: experienced colleagues submit practical evidence instead, so the programme
recognises capability without forcing unnecessary learning. Then require one practical contribution that benefits
others before full recognition. Recruit on declared interest, skills and availability, aiming for spread across teams,
locations and personas, including frontline roles.

Build the support infrastructure before launch. A dedicated community channel carries updates, examples, questions and
success stories. A progress tracker shows where each participant is, so the programme can tell newcomers from people
ready for a challenge. Self-service guidance explains requirements and the next milestone, so one owner does not become
the bottleneck. An advisor agent grounded on the programme guide is a natural, low-risk first agent and a live example
of agent capability; design it through `m365-agents:agent-use-case-design`, or publish a guide where agent building is
not yet approved. Open the learning sessions to the wider business while letting them count towards the journey, so
the programme reinforces foundation adoption rather than becoming a closed club.

Secure visible sponsorship. The sponsor launches the programme, attends a showcase each quarter and thanks contributors
publicly; leadership visibility tells managers the time is legitimate.

When replicating a model from elsewhere, decide explicitly what to keep, adapt and measure. Keep the evidence-led
progression, dual routes, practical challenge, visible recognition, community support and clear boundaries, because
they carry the method. Adapt capability areas, challenge options, badge design, advanced-access incentives, channels
and specialist pathways to local context. Agree programme-level measures before launch. Write all of this into the
charter and review it with the sponsor, HR and the CoE before launch.

## Outputs

- A Champions programme charter on the `champion-programme-charter` template: purpose and behaviours, sponsor, owner, position in the operating model, journey, boundary table with destinations, time commitment, routes, network shape, community, support infrastructure, keep-adapt-measure decisions and review date.
- A pre-launch checklist for the community channel, progress tracker, self-service guidance, challenge options and recognition, in the same template.
- A recruitment brief describing the role, time commitment, journey and how to express interest.
- A manager briefing explaining the role, the time agreed and what managers can expect.
- Where an advisor agent is wanted, a short use-case brief handed to `m365-agents:agent-use-case-design`.

## Microsoft platform considerations

Champions should work only with tools the organisation has approved for them, such as Copilot Chat, Copilot in the
Microsoft 365 apps, Copilot Cowork or agent building tools where governance allows. Community spaces typically run in
Teams or Viva Engage, and a progress tracker can be a restricted list in the organisation's existing collaboration
tools. An advisor agent built with Agent Builder or Copilot Studio follows the organisation's agent governance like any
other agent. Product availability and naming change; check `references/sources.md` and the approved tools list.

## Adoption considerations

The Champion programme is the local layer of adoption. Align it with launch waves so Champions are ready before their
team's onboarding, share the same learning sessions and scenarios with the foundation programme, and use the community
to surface what is and is not working in teams.

## Knowledge considerations

The programme guide is the knowledge source for self-service guidance and any advisor agent, so give it an owner,
a version and a review date, and update the guidance whenever the framework or challenge options change. Champions
often spot stale knowledge elsewhere first; give them a route to report it to content owners and pass systemic issues
to the `knowledge-management` department (planned).

## Security and privacy considerations

Champions must model the approved-use guidance and know how to report suspected data exposure. They are not given
broader access or admin rights because of the role, and must not share examples containing personal or confidential
data. The tracker holds personal data: restrict access, set retention, and design any advisor agent so a participant
can see only their own status, or keep it to general guidance.

## Responsible AI considerations

Champions model verification and accountability. The boundary table prevents them from releasing high-risk or
externally facing solutions; any idea touching decisions about people, money or safety goes through intake and risk
classification. An advisor agent explains requirements; it never decides whether someone is verified or recognised.

## Evaluation requirements

Not applicable as solution evaluation for the programme itself, because this skill designs a people programme. The
charter is checked by confirming every "do not" has a destination, every Champion has an agreed time commitment and
each pre-launch component exists. An advisor agent is evaluated through `m365-agents:agent-testing`.

## Value measures

Programme-level measures, owned by the programme owner with baselines taken at launch: community size and spread,
milestone conversion between stages, time to complete the journey, challenge outputs, peer-support activity, adoption
indicators in teams with Champions, and reusable assets published and reused. Apply the minimum reporting group size,
and never rank individuals.

## Scale notes

### Starter

A handful of Champions, a one-page charter, a shared chat and a monthly call run by the owner. The tracker can be a
simple restricted list and self-service guidance a single page. The boundary table matters as much here as anywhere.

### Scale

Hub-and-spoke with local leads, a formal charter, both routes, recurring sessions open to the wider business, a
maintained tracker, an advisor agent where agent building is approved, and quarterly showcases with the sponsor.

### Enterprise

Federated networks with a shared framework and rubric, trained assessors, regional leads and formal links to the CoE
and the change network. The advisor agent has a named owner and is retested whenever the framework changes. Review the
charter annually.

## Hand-offs

- To `champions:capability-framework` to define the capabilities, routes and verification criteria.
- To `champions:champion-challenges` to design the Challenge options and criteria.
- To `champions:recognition-and-progression` to design recognition, advanced access and renewal.
- To `m365-agents:agent-use-case-design` for the self-service advisor agent.
- To `ai-centre-of-excellence:coe-operating-model` to connect Champions to CoE intake and governance.
- To `copilot-adoption:launch-plan` to align the community and learning sessions with launch waves.

## Reviewer gates

Not applicable as a formal gate for the programme, because it creates no AI solution itself. The advisor agent and any
solution a Champion proposes pass through intake and the `m365-agents` skills, where risk tiers and the
`security-privacy` gate apply, particularly if the agent reads tracker records.

## Failure modes

- No time is agreed with managers, so the most willing people burn out and the network fades.
- Boundaries exist on paper but no destination routes do, so Champions become the help desk and the approval route.
- Status is awarded for attendance, and nobody trusts the badge.
- The tracker and self-service guidance are left until after launch, so every progress question lands on one owner.
- There is no Centre of Excellence route, so Champions end up building larger solutions without governance.
- Champions are concentrated in head office and desk roles, so frontline teams have nobody to turn to.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Use Champions as an unpaid help desk, an approval route or the sole owner of adoption.
- Recruit Champions without a time commitment agreed with their managers.
- Award Champion status for attendance alone, or make training the only route to it.
- Let Champions approve solutions or production releases.
- Select or exclude Champions on personal characteristics rather than declared interest, skills and availability.

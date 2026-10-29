---
name: role-based-adoption
description: Designs an adoption journey for each priority role - first scenarios, guided practice on real work, team routines and later extension to Cowork tasks or agents - with role-specific onboarding, manager expectations, peer support, milestones and team-level success signals. Use when a role group needs more than generic onboarding, when a sponsor names priority roles, or when a role's use has stayed shallow.
license: CC-BY-4.0
metadata:
  department: copilot-adoption
  lifecycle: Enable, Launch, Scale
  maturity: adopter, scaler, ai-enterprise
  risk-tiers: 0, 1, 2
  platforms: copilot-chat, m365-copilot, copilot-cowork, m365-agents
  edition-support: scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-overview, ms-champion-best-practice
  status: draft
  authors: Simon Foote
---

# Role-based adoption

## Purpose

Generic onboarding gets people started; it rarely changes how a role works. This skill designs an adoption journey for
each priority role, so that people in that role move from a few starting scenarios to routines their team relies on,
with the support, manager expectations and practice time that make the change stick. It connects scenarios, learning,
Champions and managers into one sequence owned by the business. It usually goes wrong when every role is treated as a
priority, when the journey is a training plan with no change in the work itself, or when success is judged by how often
individuals open Copilot.

## When to use

- A sponsor or business-unit leader has named roles where Copilot should make a visible difference.
- A role group was onboarded with everyone else and its use has stayed shallow or faded.
- Scenarios for a role exist in the catalogue but nobody has planned how people will build them into their routine.
- A role is moving from individual Copilot use towards shared prompts, Cowork tasks or agents and needs a path.
- Several role groups need comparable journeys so progress can be discussed consistently at steering.

## When not to use

- Discovering and prioritising the scenarios themselves - use `copilot-adoption:scenario-discovery`.
- Defining Copilot scenarios per role across the Microsoft 365 apps in product detail - use `m365-copilot:copilot-role-scenarios`.
- Building the formal role curriculum and learning materials - use `learning-and-skills:ai-role-curriculum`.
- The first-days experience every newly enabled user receives - use `copilot-adoption:copilot-onboarding`.
- Grouping the whole workforce into audiences - use `copilot-adoption:audience-segmentation`.
- Equipping line managers in general to lead AI change - use `change-and-communications:manager-enablement`.

## Questions to ask first

1. Which roles are priorities, who named them, and what outcome does the business owner of each role expect?
2. Which scenarios in the catalogue fit this role, and have they been tried on the role's real work?
3. What does a normal week look like for this role, and where could practice time realistically come from?
4. Who manages people in this role, and will they set expectations and protect time?
5. Are there Champions in or near this role, and what support exists beyond the first fortnight?
6. What would the business owner accept as a sign the role's work has changed, measured at team level?

## Required inputs

- The audience model from `copilot-adoption:audience-segmentation` and the scenario catalogue from `copilot-adoption:scenario-discovery`.
- A named business owner for each priority role, and the outcome they expect.
- The onboarding experience from `copilot-adoption:copilot-onboarding`, so the journey builds on it rather than repeating it.
- Champions coverage for the role, from `champions:champion-programme-design` or the programme tracker at aggregate level.
- The minimum reporting group size from `copilot-adoption:adoption-measurement`.

If a role has no business owner, do not design a journey for it; record it as a precondition. If scenarios for the role
have not been tested on real work, schedule that first, because a journey built on untested scenarios teaches people
that Copilot does not help.

## Decision framework

Choose priority roles on evidence rather than enthusiasm. A role usually qualifies when most of these hold.

| Criterion | Qualifies when |
|---|---|
| Scenario value | Tested scenarios save meaningful time or improve quality in work the role does often |
| Reach | Enough people share the role for a journey to be worth designing, above the minimum group size |
| Ownership | A business owner wants the outcome and will sponsor the journey |
| Readiness | Access, permissions hygiene and approved-use guidance are in place for the role's content |
| Risk | Scenarios stay at tiers 0 to 1, or higher-tier steps are routed through intake |

Design each journey in four stages. Durations are a starting point to adjust, not a standard.

| Stage | The role | Support | Manager | Signal at team level |
|---|---|---|---|---|
| Start | Uses two or three starting scenarios on real tasks | Role-specific session, scenario cards | Sets the expectation and names practice time | Starting scenarios tried across the team |
| Practise | Extends to the full scenario set, refines prompts, verifies outputs | Office hours, Champion pairing, peer show-and-tell | Asks what worked in team meetings | Scenarios reported as useful; questions shift from "how" to "what else" |
| Embed | Builds scenarios into team routines and templates | Shared prompts and playbook for the role | Changes the routine, not just the tool | A team routine changed, recorded by the owner |
| Extend | Identifies repeat work for Cowork tasks, shared prompts or agents | Route to intake and the CoE | Sponsors ideas with an owner | Ideas routed with owners; reusable assets published |

## Practitioner approach

Begin with the role's work, not the product. Sit with the business owner and two or three people in the role and walk
through a typical week: the recurring documents, meetings, requests and decisions. Mark where time goes and where
quality suffers. Map the tested scenarios onto those moments. If no scenario lands on a moment that matters, the
journey is premature; return to scenario discovery rather than fill the gap with features.

Write the journey as a sequence of changes in the work. "Prepares the weekly client update with Copilot from the
meeting notes and tracker, then checks figures against the source" is a journey step. "Attends advanced Copilot
training" is not. Each stage should name what people will do differently, what support they get, what their manager
does and what signal tells the business owner it is happening.

Make managers the spine of the journey. People in a role take their cue from their manager about whether practice is
legitimate. Give each manager a short role-specific briefing: the scenarios, the expectation, how to ask about progress
without monitoring individuals, and how to protect a small amount of practice time. Ask them to put Copilot on the
agenda of an existing team meeting for the first few weeks rather than create new meetings.

Use peers for the middle of the journey. Champions in or near the role, short show-and-tell slots and a shared prompt
collection do more in weeks three to eight than any further training. Where there are no Champions in the role, treat
that as a recruitment priority for `champions:champion-recruitment` rather than leaving the role unsupported.

The embed stage is where most journeys stall. Ask the business owner which routine, template or handover will change,
and hold them to it. Adoption is real when the team's way of working assumes Copilot, with verification built in, not
when individuals happen to use it.

Plan the extend stage carefully. As people find repeated patterns, some will want shared prompts, Cowork tasks or
agents. Route these through opportunity intake so suitability, risk tier and ownership are decided properly, and
recognise the people who spotted them.

Measure at team or role level only, using the signals in the journey and the measures from
`copilot-adoption:adoption-measurement`. Review each journey with the business owner after the embed stage and decide
whether to refresh it, extend it or close it.

## Outputs

- A role journey for each priority role, recorded with the onboarding and reinforcement sections of the `adoption-plan` template: stages, scenarios, support, manager actions, signals and owner.
- A priority role shortlist with the criteria evidence behind each choice.
- A role-specific manager briefing outline.
- A role playbook of tested scenarios and shared prompts, entered in the `scenario-catalogue`.

## Microsoft platform considerations

Journeys must match the Copilot experiences the role actually has. The Start and Practise stages usually sit in
Copilot Chat and Copilot in the Microsoft 365 apps; the Extend stage may involve Copilot Cowork or agents built in Agent
Builder or Copilot Studio, which bring governance and ownership requirements. Confirm capability and availability for
each step against `references/sources.md` rather than last quarter's training material.

## Adoption considerations

This skill is the depth layer of adoption for roles that matter most. Keep journeys few, owned and visible, and share
what works so other roles can borrow patterns rather than wait for their own journey.

## Knowledge considerations

Role journeys quickly expose the role's dependence on policies, procedures and templates. Where answers are poor
because content is stale, duplicated or unowned, record it and pass it to `knowledge-management:knowledge-gap-analysis`.

## Security and privacy considerations

Check that the role's content is covered by the permissions review before its journey starts, and that scenario cards
use fictional or approved material. Roles handling personal or regulated data need the approved-use guidance applied
to their scenarios explicitly.

## Responsible AI considerations

Each journey teaches verification for the role's own outputs and makes clear people remain accountable for what they
send. Where a role's scenarios inform decisions about people, money or safety, route them through
`opportunity-management:risk-classification` before including them.

## Evaluation requirements

Not applicable as solution evaluation, because a role journey designs adoption rather than an AI solution. Each journey
is reviewed against its stage signals with the business owner after the embed stage.

## Value measures

Owned by the business owner of the role, with a baseline before the Start stage: time or quality on the role's
recurring tasks where it can be observed at team level, scenarios in routine use, routines changed and ideas routed.
Reported at team or role level above the minimum group size, never for individuals.

## Scale notes

### Starter

Usually not needed as a separate exercise; one or two roles can be handled within onboarding and scenario discovery.

### Scale

Journeys for three to six priority roles, each with a business owner, manager briefing and Champion support, reviewed
at steering.

### Enterprise

A library of role journeys shared across divisions, with local variants, a common stage model and consistent team-level
signals so steering can compare progress without ranking teams.

## Hand-offs

- To `learning-and-skills:ai-role-curriculum` for formal learning content for the role.
- To `copilot-adoption:adoption-reinforcement` once the role reaches the embed stage.
- To `champions:champion-recruitment` where a priority role has no Champions.
- To `opportunity-management:problem-framing` for ideas from the extend stage.
- To `copilot-adoption:adoption-measurement` for team-level signals.

## Reviewer gates

Not applicable as a formal gate for tier 0 and 1 scenarios, because the journey uses approved Copilot experiences.
Anything in the extend stage that becomes a shared agent or tier 2 solution goes through `security-privacy` and the
gates set by risk classification.

## Failure modes

- Every role is declared a priority, journeys are thin, and none changes the work.
- The journey is a training timetable, so people complete sessions and return to old routines.
- Managers are left out, and practice time is never protected.
- Success is judged on individual usage counts, which damages trust and rewards indiscriminate use.
- Extend-stage ideas bypass intake and become ungoverned shared agents.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Design a role journey without a business owner for the role.
- Build a journey on scenarios that have not been tested on the role's real work.
- Track or report Copilot use by named individual.
- Let shared agents emerge from a journey without intake, risk classification and an owner.

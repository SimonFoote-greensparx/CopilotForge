---
name: adoption-reinforcement
description: Runs the always-on reinforcement cycle for Copilot after launch - a calendar of nudges and refreshers, scenario refreshes, manager follow-up prompts, re-engagement of teams whose use has faded and refreshers when Copilot changes - triggered by team-level signals, never individual tracking. Use when launch is over and use is plateauing, when teams drift back to old habits, or when a Copilot change must reach existing users.
license: CC-BY-4.0
metadata:
  department: copilot-adoption
  lifecycle: Launch, Measure, Improve
  maturity: adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, copilot-cowork
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-champion-best-practice, ms-copilot-overview
  status: draft
  authors: Simon Foote
---

# Adoption reinforcement

## Purpose

Most people try Copilot after launch; far fewer keep using it once the novelty fades and deadlines return. This skill
runs the reinforcement cycle that carries adoption from launch into habit: small, regular prompts to try something
useful, refreshers when practice slips or the product changes, managers asking the right questions, and targeted help
for teams where use has faded. It is driven by team-level signals and by what users say, not by watching individuals.
Reinforcement usually goes wrong when it stops after the first month, when it repeats launch content to people who
have moved on, or when "re-engagement" turns into chasing named people.

## When to use

- Launch is complete and the programme needs an operating rhythm for the months that follow.
- Team-level indicators show use plateauing or falling in some parts of the organisation.
- Feedback shows people stuck on the same few scenarios and unaware of what else is useful.
- A significant Copilot change, new capability or updated approved-use guidance must reach people already onboarded.
- Managers have stopped mentioning Copilot and teams are drifting back to old routines.

## When not to use

- Planning the launch and the reinforcement calendar for the launch window itself - use `copilot-adoption:launch-plan`.
- Embedding new behaviours into processes, roles and leadership routines as part of the wider change plan - use `change-and-communications:behaviour-reinforcement-plan`.
- Planning a time-boxed campaign around a scenario theme - use `change-and-communications:adoption-campaign-plan`.
- Running office hours and drop-in clinics as a service - use `learning-and-skills:office-hours`.
- Deciding what to measure and the reporting rules - use `copilot-adoption:adoption-measurement`.

## Questions to ask first

1. Which team-level signals are available (usage at aggregate level, pulse results, support themes, Champion feedback), and how often are they refreshed?
2. Which teams or audiences have plateaued or faded, and what do their managers and Champions say is happening?
3. What new or under-used scenarios are ready to share, and who has tested them?
4. What channels do people actually read or attend, and which have become background noise?
5. Who will own the reinforcement calendar, and how much capacity do they have each month?

## Required inputs

- Team-level adoption indicators and feedback themes from `copilot-adoption:adoption-measurement`.
- The scenario catalogue from `copilot-adoption:scenario-discovery`, including scenarios not yet promoted.
- The audience model from `copilot-adoption:audience-segmentation`, so nudges can be targeted by audience.
- The Champions community and office hours calendar, where they exist.
- Notice of upcoming Copilot changes from the owners of the Microsoft change process.

If no team-level signals exist, start with qualitative signals from managers, Champions and support themes and ask
`copilot-adoption:adoption-measurement` to set up aggregate indicators. Never substitute individual usage lists.

## Decision framework

Match the response to the signal. All signals are read at team or audience level above the minimum group size.

| Signal | Likely cause to check | Response |
|---|---|---|
| Use steady and broad | Healthy habits forming | Light nudges, new scenarios each month, showcase good practice |
| Use plateaued on a few scenarios | People unaware of other useful scenarios | Scenario refresh, peer show-and-tell, role-specific tips |
| Use rose then fell in a team | Practice time lost, manager disengaged, poor early results | Manager conversation, Champion visit, refresher on real tasks |
| Low use from the start in a team | Access, onboarding or relevance problem | Check access and onboarding first; revisit scenarios with the business owner |
| Support themes repeat | Guidance unclear or product behaviour misunderstood | Fix guidance; targeted refresher |
| Copilot or guidance changes | Existing users unaware | Short "what changed and why it matters" refresher by audience |

Choose mechanisms that fit the audience and the capacity available.

| Mechanism | What it does | Typical owner | Rhythm |
|---|---|---|---|
| Nudge | One short, useful prompt to try on real work | Adoption lead | Weekly or fortnightly |
| Scenario refresh | Introduces a tested scenario people have not tried | Adoption lead with business owner | Monthly |
| Manager prompt | A question managers ask in team meetings | Managers, supported by adoption lead | Monthly |
| Peer showcase | Colleagues show what worked | Champions | Monthly |
| Refresher | Short session on a change or a slipping habit | Learning team or Champions | As needed |
| Re-engagement | Focused help for a team whose use has faded | Adoption lead, manager and Champion | Triggered |

## Practitioner approach

Treat reinforcement as an operating rhythm, not a campaign. Set a simple monthly cycle: review team-level signals and
feedback, decide two or three reinforcement actions, run them, and note what changed. Put the cycle in the adoption
lead's calendar with named contributors, so it survives the end of the launch project.

Keep nudges small and useful. One prompt that saves someone time today is worth more than a newsletter of tips. Write
each nudge around a task the audience does, include the verification step, and send it through the channel the
audience actually reads. Vary the channel and format over time, because any single channel becomes background noise.

Refresh scenarios rather than repeat launch content. People who have been using Copilot for months need the next
useful thing, not the getting-started session again. Work with business owners and Champions to promote scenarios that
are tested but under-used, and retire ones that no longer reflect how the product works.

Give managers one question a month. "What is one thing Copilot helped with this month, and what didn't work?" asked in
an existing team meeting does more than any central message. Equip managers to ask without monitoring: the point is to
surface practice and obstacles, never to check who has used it.

When a team's use fades, investigate before acting. Speak to the manager and the local Champion, look at support
themes and pulse comments for the team, and check whether something has changed: a reorganisation, a busy season, a
poor early experience, an access problem. Then agree one or two targeted actions with the manager, such as a refresher
on the team's real work or a Champion pairing. Re-engagement is offered to the team, not imposed on individuals.

Make product change part of the rhythm. Copilot changes frequently, and existing users learn of changes late or not at
all. Ask whoever tracks Microsoft change notices to flag changes that alter user experience or guidance, and turn each
into a short audience-specific refresher.

Report reinforcement by what it changed: scenarios newly in use, teams re-engaged, support themes resolved. Hand
lasting behavioural changes, such as altered routines and templates, to the wider change plan so they are embedded
beyond the adoption team.

## Outputs

- A reinforcement calendar recorded in the reinforcement section of the `adoption-plan` template: mechanisms, audiences, rhythm, owners and the monthly review.
- A signal-to-response playbook at team level, with the checks to make before acting.
- A bank of nudges and scenario refreshes by audience, drawn from the `scenario-catalogue`.
- A monthly reinforcement note to the sponsor: signals, actions taken and what changed.

## Microsoft platform considerations

Aggregate usage reporting from Microsoft can show broad trends by group, but definitions, availability and privacy
settings change; confirm them against `references/sources.md` and use reporting through
`m365-copilot:copilot-usage-reporting`. Refreshers must match current Copilot behaviour and naming, which changes
often, so review material against the current source records before each cycle.

## Adoption considerations

This skill is where adoption is sustained or lost. Keep the cycle light enough to survive competing priorities, and
share credit with managers and Champions, whose involvement matters more than central communications.

## Knowledge considerations

Fading use is often a knowledge problem in disguise: people stop asking about policies or procedures because the
answers were poor. Note these patterns and pass them to `knowledge-management:knowledge-gap-analysis`.

## Security and privacy considerations

Signals are read only at team or audience level above the minimum group size. Reinforcement material repeats the
approved-use guidance where relevant and the route for reporting suspected data exposure. Data protection questions
about usage data end with the organisation's DPO.

## Responsible AI considerations

Reinforcement promotes useful, verified practice, not volume of use. Never set targets that reward indiscriminate use,
and keep reminding people that they remain accountable for what they send.

## Evaluation requirements

Not applicable as solution evaluation, because reinforcement is an adoption practice rather than an AI solution. Each
monthly cycle records which actions were taken and what changed in the signals, so ineffective mechanisms can be dropped.

## Value measures

Owned by the adoption lead, with baselines from the end of launch: sustained use at team level over successive months,
breadth of scenarios in use, teams re-engaged after fading, and repeat support themes resolved. Reported above the
minimum group size, never for individuals.

## Scale notes

### Starter

A fortnightly nudge, a monthly scenario refresh and one manager question each month, reviewed by the adoption lead in a
short monthly slot.

### Scale

A monthly cycle with Champions and managers, audience-targeted nudges, triggered re-engagement for faded teams and
product-change refreshers.

### Enterprise

Regional reinforcement cycles on a shared playbook, a central bank of nudges and refreshers, and signals reported
consistently across divisions to the CoE.

## Hand-offs

- To `change-and-communications:behaviour-reinforcement-plan` for changes that must be embedded in processes and routines.
- To `champions:champion-community-design` for peer showcases and Champion-led refreshers.
- To `copilot-adoption:adoption-measurement` to refine the signals behind the cycle.
- To `copilot-adoption:adoption-support-model` when repeat support themes point to a support gap.

## Reviewer gates

Not applicable as a formal gate, because reinforcement of approved Copilot experiences at tiers 0 and 1 does not
release an AI solution.

## Failure modes

- Reinforcement stops when the launch project closes, and use fades over the following quarter.
- Launch content is repeated to experienced users, who stop paying attention.
- Re-engagement turns into chasing named individuals, and trust in the programme collapses.
- Product changes reach users months late, so guidance and reality diverge.
- A single channel is overused until every nudge is ignored.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Use individual usage data to target, chase or judge people.
- Set targets that reward volume of use over useful, verified practice.
- Act on a team's faded use before speaking to its manager and Champion.
- Let reinforcement end with the launch project without a named owner.

---
name: adoption-campaign-plan
description: Plans a time-boxed adoption campaign of a few weeks around one scenario theme for a defined audience - the behaviour it should change, tested scenarios, a weekly arc, tasks for managers and Champions, assets, a team-level baseline and a closing review that hands practice to reinforcement. Use when a scenario is under-used, when a new capability needs a push, or when leaders want a campaign but cannot say what it should change.
license: CC-BY-4.0
metadata:
  department: change-and-communications
  lifecycle: Launch, Measure, Scale, Improve
  maturity: adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-champion-best-practice, ms-copilot-overview
  status: draft
  authors: Simon Foote
---

# Adoption campaign plan

## Purpose

A campaign concentrates attention on one useful way of working with AI for a few weeks so that a defined audience tries
it, gets help with it and keeps it. This skill plans that campaign: the behaviour it targets, the scenarios behind it,
the weekly rhythm of activities, who does what, the assets, the baseline and the closing review. Campaigns usually go
wrong when they promote "AI" in general, when they measure activity such as clicks and attendance instead of changed
practice, when they turn into leader boards of individuals, or when they end abruptly with nothing to carry the new
habit forward.

## When to use

- A tested scenario is valuable but few people in its audience use it.
- A new capability, agent or Cowork pattern is approved and needs a focused push to its intended audience.
- Leaders ask for "a campaign" and need help defining what it should change.
- Adoption has plateaued in one function and a themed burst of activity would help.
- A seasonal moment (planning cycle, year end, a busy bid period) creates a natural window for one scenario.

## When not to use

- Planning the overall launch and waves - use `copilot-adoption:launch-plan`.
- Running the always-on nudge and refresher cycle after launch - use `copilot-adoption:adoption-reinforcement`.
- Setting the overall narrative, senders and channels - use `change-and-communications:ai-communication-strategy`.
- Designing the Champion Challenge that Champions complete - use `champions:champion-challenges`.
- Finding and prioritising scenarios in the first place - use `copilot-adoption:scenario-discovery`.

## Questions to ask first

1. What one behaviour should be more common at the end of the campaign, for which audience, and why does it matter to the business owner?
2. Which tested scenarios support that behaviour, and can the audience verify the outputs?
3. Does everyone in the audience have access, onboarding and approved-use guidance already?
4. What team-level signal can show change, and what is its value now?
5. Who will run it, and what will managers and Champions be asked to do each week?

## Required inputs

- The scenario catalogue from `copilot-adoption:scenario-discovery`, with the scenarios in scope marked as tested.
- The audience model from `copilot-adoption:audience-segmentation` and team-level signals from `copilot-adoption:adoption-measurement`.
- The communications calendar from `change-and-communications:ai-communication-strategy`, so the campaign does not collide with other messages.
- Champion and manager capacity for the campaign weeks.
- A business owner who wants the behaviour and will speak for it.

If the scenario has not been tested with the audience, test it first; a campaign that promotes something that does not
work damages trust for months. If access or onboarding is incomplete, fix it before the campaign rather than during it.

## Decision framework

Use a campaign only when the conditions are right; otherwise choose a different route.

| Condition | If met | If not met |
|---|---|---|
| A specific, valuable behaviour is named | Proceed | Return to the business owner to define it |
| Scenarios are tested and verifiable | Proceed | Test with a small group first |
| Audience has access and onboarding | Proceed | Route to `copilot-adoption:copilot-onboarding` before the campaign |
| A team-level baseline exists | Proceed | Capture one before launch, or use a qualitative baseline |
| Managers and Champions have capacity | Proceed | Narrow the audience or move the window |

Shape the campaign with a standard weekly arc, adjusted to the audience.

| Week | Purpose | Typical activities |
|---|---|---|
| 1 | Show why and how | Business owner kick-off, short demo on real work, manager conversation |
| 2 | Try it | Practice task on real work, drop-in clinic, Champion help in team channels |
| 3 | Share it | Peer show-and-tell, examples collected, common problems answered |
| 4 | Make it stick | Team agrees where the scenario fits its routines; closing review; hand-off |

Longer campaigns add a second try-and-share cycle. Shorter ones merge weeks 2 and 3. Team-based challenges can add
energy, but never rank or publish individuals.

## Practitioner approach

Write the behaviour statement first, in the form "more people in this audience do this task this way, checked like
this." For example: "Bid writers draft first-pass responses with Copilot from the approved content library and check
every claim against the source." If the statement cannot be written, the campaign is not ready.

Choose one theme and at most three scenarios that support it. Campaigns with many scenarios become a menu that nobody
orders from. Make sure each scenario has a prompt pattern, a verification step and a real task the audience does in the
campaign window.

Agree the baseline and measure before any message goes out. Pick one or two team-level signals that the behaviour
should move: use of the relevant feature or agent at aggregate level, the share of teams that report using the scenario
in a pulse question, or a work measure the business owner already tracks. Agree the minimum group size. Clicks,
attendance and email opens show reach, not change, and should be reported only as context.

Give every role a weekly task. The business owner opens and closes the campaign. Managers hold one short conversation
at the start and agree in week 4 where the scenario fits the team's routines. Champions run clinics, answer questions in
team channels and collect examples. The adoption lead runs the calendar and the measurement. Write these into a
one-page run sheet so each person knows exactly what is asked of them and when.

Prepare assets that help people do the task, not posters about AI: a short demo recording, a one-page guide with the
prompt pattern and the check, examples from colleagues, and answers to the questions likely to arise. Link everything to
the approved-use guidance.

Run the campaign with a weekly check. Look at questions, clinic attendance, examples shared and early signals. Adjust:
if people are stuck on access, stop and fix it; if the scenario is not working for a sub-group, say so and narrow the
audience. Honesty mid-campaign protects credibility.

Close deliberately. In the final week, run a short review with the business owner, managers and Champions: what changed
in the signal, what people said, which teams adopted the routine and which did not and why. Capture credible examples for
`change-and-communications:success-stories`, hand ongoing nudges to `copilot-adoption:adoption-reinforcement`, and
hand any routine or template changes to `change-and-communications:behaviour-reinforcement-plan`. Without the hand-off,
campaign gains fade within weeks.

## Outputs

- A campaign plan: behaviour statement, audience, scenarios, window, weekly arc, run sheet by role, assets, baseline and measures, minimum group size and closing review date.
- A campaign entry in the calendar section of the `ai-communications-plan`.
- A campaign asset pack linked from the `scenario-catalogue`.
- A closing review note with results at team level, lessons and hand-offs.

## Microsoft platform considerations

Promote only experiences the audience has access to and the organisation has approved, configured as described. Check
current behaviour and naming against `references/sources.md` before producing assets, because demos recorded on older
behaviour confuse people. Aggregate usage reporting definitions change; use them through
`m365-copilot:copilot-usage-reporting`.

## Adoption considerations

Campaigns are bursts within the adoption programme, not substitutes for onboarding or reinforcement. Space them so that
audiences are not in permanent campaign mode, and avoid overlapping campaigns for the same audience.

## Knowledge considerations

Scenarios that depend on shared knowledge, such as a content library or an agent's sources, need that knowledge to be
current before the campaign. Check with its owner; a campaign that sends people to stale content harms both.

## Security and privacy considerations

Campaign examples must not contain personal or confidential data. Signals are read at team level above the minimum
group size. Every asset links to the approved-use guidance and the route for reporting suspected data exposure.

## Responsible AI considerations

Campaigns promote verified practice, not volume. Every scenario includes its check, and the campaign never sets targets
that reward indiscriminate use or pressure people to use AI where they judge it unsuitable.

## Evaluation requirements

Not applicable as solution evaluation, because the scenarios are already approved and tested. The campaign itself is
evaluated by comparing the agreed signal with its baseline at the closing review.

## Value measures

Owned by the adoption lead with the business owner: change in the agreed team-level signal against baseline, share of
teams that adopted the routine, and any business measure the owner tracks. Never individual measures or rankings.

## Scale notes

### Starter

One campaign a quarter, four weeks, one scenario, run by the adoption lead with a handful of Champions.

### Scale

A campaign calendar across functions, a reusable run sheet and asset template, and closing reviews shared across the
programme.

### Enterprise

Central campaign designs adapted by divisions and regions, coordinated in one calendar to avoid overload, with results
compared at programme level.

## Hand-offs

- To `copilot-adoption:adoption-reinforcement` for nudges after the campaign closes.
- To `change-and-communications:behaviour-reinforcement-plan` for routines and templates that need embedding.
- To `change-and-communications:success-stories` for credible examples from the campaign.
- To `copilot-adoption:scenario-discovery` to update scenarios with what the campaign revealed.

## Reviewer gates

Not applicable as a formal gate, because campaigns promote already approved experiences at risk tiers 0 and 1. A
campaign for an agent above tier 1 runs only after that agent has passed its release gates.

## Failure modes

- The campaign promotes AI in general, nobody knows what to do differently, and nothing changes.
- Success is reported as emails opened and sessions attended, while practice stays the same.
- A leader board of individuals appears, people game it, and trust in the programme drops.
- The campaign ends without a hand-off, and use returns to the baseline within weeks.
- An untested scenario is promoted and fails in front of the whole audience.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Rank, publish or reward individuals by AI usage.
- Promote a scenario that has not been tested with the audience.
- Report reach or attendance as the campaign's result.
- Close a campaign without handing ongoing practice to reinforcement.

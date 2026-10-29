---
name: manager-enablement
description: Equips line managers to lead AI adoption in their own teams - a briefing before their team hears anything, conversation guides for purpose and concerns, team norms for approved use and verification, protected practice time, a monthly question and clear routes for ideas and issues - without asking managers to monitor individuals. Use when managers are bypassed or unsure, before a wave reaches their teams, or when teams stall.
license: CC-BY-4.0
metadata:
  department: change-and-communications
  lifecycle: Enable, Launch, Measure, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-champion-best-practice, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Manager enablement

## Purpose

People decide whether to invest effort in AI largely by watching their line manager: whether the manager explains why,
makes time to practise, uses the tools themselves and treats mistakes as learning. This skill equips managers at every
level to lead that change in their own teams with a briefing, conversation guides, team norms, a simple cadence and
clear routes for what they cannot answer. Manager enablement usually goes wrong when managers learn about the change at
the same time as their teams, when they are handed a slide deck instead of a conversation, or when they are asked to
"drive usage" and start chasing individuals.

## When to use

- A Copilot wave, agent or Cowork pilot is about to reach teams and their managers have not been briefed.
- Teams stall after onboarding and managers say they do not know what is expected of them.
- Managers are raising the same questions (time, jobs, monitoring, quality) and giving inconsistent answers.
- Some managers are pressing for usage figures on named people, or using AI use as a performance signal.
- A role-based adoption journey needs managers to play a defined part.

## When not to use

- Helping executives use Copilot personally and lead visibly - use `copilot-adoption:executive-enablement`.
- Copilot scenarios and habits for leaders' own work - use `m365-copilot:copilot-for-leaders`.
- Designing the adoption journey for one role group - use `copilot-adoption:role-based-adoption`.
- Formal learning curricula and facilitator materials - use `learning-and-skills:ai-role-curriculum`.
- The always-on reinforcement calendar after launch - use `copilot-adoption:adoption-reinforcement`.

## Questions to ask first

1. Which managers lead the teams in scope, at which levels, and when will each team be affected?
2. What do managers need to be able to say and do: explain why, set norms, protect practice time, answer concerns, route ideas?
3. What is the agreed position on jobs, use of usage data and approved use, so managers can give the same answer?
4. How much time can managers realistically give, and which existing meetings can carry the work?
5. Do managers have access to the AI experience themselves before their teams, and are they confident using it?

## Required inputs

- The communications plan, core messages and agreed answers from `change-and-communications:ai-communication-strategy`.
- Group-level impact for the teams in scope from `change-and-communications:people-change-impact`.
- The launch waves from `copilot-adoption:launch-plan` and starting scenarios from `copilot-adoption:scenario-discovery`.
- The approved-use guidance, support routes and the route for reporting suspected data exposure.
- Agreement from the sponsor and HR on how AI use relates to performance management.

If managers will not have access before their teams, record it as a risk and move their access earlier where possible.
If no position exists on performance management, escalate before managers are briefed, because it is the question they
will be asked first.

## Decision framework

Define the manager role in five actions, each with a tool. These are the minimum; add only what the impact requires.

| Manager action | What it means in practice | Tool provided |
|---|---|---|
| Explain why | Put the organisation's reasons in the team's terms | Talking points and a short team conversation guide |
| Set team norms | Agree approved use, verification, disclosure where required, and what stays human | Team norms canvas |
| Make time | Protect practice time and plan around busy periods | Practice time agreement and suggestions for fitting it into existing routines |
| Hear concerns | Listen, answer what they can and route the rest | Answers to common concerns and an escalation route |
| Keep it going | Ask one question a month about what helped and what did not | Monthly question and a route to share good practice |

Adjust depth by the team's impact rating.

| Team impact | Manager support |
|---|---|
| Low | Briefing pack and talking points before the team's wave |
| Medium | Briefing session, team norms canvas, practice time agreement, monthly question |
| High | Manager cohort sessions before and after launch, change lead contact, joint planning with HR where roles change |

## Practitioner approach

Brief managers first, always. Set a rule that no team hears about a change affecting it before its manager has been
briefed and has had a chance to ask questions. Where managers lead managers, cascade the briefing through the levels in
order, with enough time between for questions to come back up.

Give managers a conversation, not a presentation. A short team conversation guide works better than slides: open with
why the organisation is doing this and what it means for this team, show one starting scenario on real work, agree how
the team will use AI and check its outputs, and ask what worries people. Managers should leave the conversation with a
list of questions to answer or route, not a list of who attended.

Make the norms explicit. Each team agrees, in plain words, which tasks AI is used for, how outputs are checked before
they leave the team, what must never be put into a prompt, when use is disclosed to colleagues or customers, and what
stays a human judgement. The team norms canvas takes twenty minutes and prevents most of the confusion that otherwise
arrives as support tickets.

Protect practice time. People learn AI by using it on real work, and that takes time during the first weeks. Agree with
managers how much time their teams will have and when, and help them fit it around peak periods. Where managers cannot
release time, record it and tell the adoption lead, because that team will need a later wave.

Equip managers to hear concerns well. Give them the agreed answers on jobs, monitoring, data and quality, and a clear
route for what they cannot answer. Ask them to pass on themes, not names. Remind them that a team member's scepticism is
information about the change, not a performance issue.

Draw the monitoring line clearly. Managers must not ask for, receive or use individual AI usage data, or treat volume of
use as a measure of performance. What managers can ask is how the team is using AI, what is working and what is not.
State this in the briefing and in writing, agreed with HR and the DPO.

Support managers as a group. Run short manager cohort sessions for high-impact areas where managers can compare notes,
and give each manager one monthly question to ask their team. Encourage managers to use the AI experience themselves on
their own work, so they speak from experience. Share what managers learn back into the programme through the change
network and the adoption lead.

## Outputs

- A manager toolkit: briefing pack, team conversation guide, team norms canvas, practice time agreement, answers to common concerns, escalation routes and the monthly question.
- A manager briefing schedule aligned to waves, recorded in the manager section of the `ai-communications-plan` template and the enablement section of the `adoption-plan`.
- A written statement, agreed with HR and the DPO, on what managers may and may not do with AI usage information.
- A monthly theme summary from managers to the adoption lead and change lead.

## Microsoft platform considerations

Managers should have the same AI experiences their teams will receive, configured the same way, before the team
launches. What aggregate usage reporting can show, and to whom, depends on current Microsoft capability and the
organisation's settings; confirm it against `references/sources.md` and `m365-copilot:copilot-usage-reporting`, and do
not promise managers views that the organisation has chosen not to provide.

## Adoption considerations

Manager involvement is the strongest local lever on adoption. Coordinate with Champions so managers know who their
local Champion is, and so practice time and peer help reinforce each other.

## Knowledge considerations

Managers often know where team knowledge is out of date or held by one person. Give them a route to report it to
content owners and to `knowledge-management:knowledge-gap-analysis`.

## Security and privacy considerations

Managers must not request or use individual usage data. Team norms repeat the approved-use rules on confidential and
personal data, and every manager knows the route for reporting suspected data exposure. Questions about monitoring and
employee data end with HR and the DPO.

## Responsible AI considerations

Managers set the expectation that people remain accountable for AI-assisted work and must check it. Where a team uses AI
in work that affects decisions about people, managers should know that higher-risk uses go through intake and review,
not team norms alone.

## Evaluation requirements

Not applicable as solution evaluation. The toolkit is tested with a small group of managers before release, and the
briefing is revised after each wave using manager feedback.

## Value measures

Owned by the change lead, with baselines at the start of each wave: share of managers briefed before their teams, teams
with agreed norms, practice time agreed, and team-level pulse results on clarity of expectations and confidence to raise
concerns. Reported by team or business unit above the minimum group size, never as a rating of individual managers.

## Scale notes

### Starter

A single briefing for all managers, a two-page toolkit and a monthly question, owned by the adoption lead.

### Scale

Briefings by wave, cohort sessions for high-impact areas, and a manager channel connected to the change network.

### Enterprise

A cascade through management layers with local adaptation, translated toolkits, and manager enablement built into
standard leadership development owned by HR.

## Hand-offs

- To `copilot-adoption:role-based-adoption` for the manager's part in each role journey.
- To `change-and-communications:change-network` so managers and change agents share themes.
- To `change-and-communications:behaviour-reinforcement-plan` to embed manager routines that sustain new ways of working.
- To `change-and-communications:resistance-management` when a team's concerns need more than a manager conversation.

## Reviewer gates

Not applicable as a formal gate, because manager enablement for approved AI experiences does not release a solution.
The statement on usage data is approved by HR and the DPO before managers are briefed.

## Failure modes

- Managers learn about the change from their teams and cannot answer basic questions.
- Managers are told to "drive usage", ask for individual figures and turn adoption into surveillance.
- No practice time is agreed, so teams try AI once and return to old habits.
- Toolkits are sent as attachments with no conversation, and few managers use them.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Ask managers to monitor, rank or chase individuals on AI usage.
- Let AI usage volume become a performance measure for anyone.
- Brief teams before their managers.
- Give managers answers on jobs or monitoring that HR and the DPO have not agreed.

---
name: office-hours
description: Runs AI office hours and drop-in clinics as a learning service - open and themed formats, rhythm and timing, who staffs them, booking, safe screen-sharing, a light triage that routes faults and data concerns to the right support route, and capture of recurring questions by theme into curricula and guidance. Use when learners stall after training, when the same questions keep reaching the service desk, or when clinics have gone quiet.
license: CC-BY-4.0
metadata:
  department: learning-and-skills
  lifecycle: Launch, Enable, Improve
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-studio
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-champion-best-practice, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Office hours

## Purpose

Most learning about Microsoft AI happens in the week after a session, when people try it on real work and get stuck.
Office hours and drop-in clinics give them somewhere to bring that real problem and leave with it solved and a little
more skill. This skill designs and runs them as a learning service: formats, rhythm, staffing, safe screen-sharing,
triage to other routes, and capture of recurring themes so the curriculum improves. It usually goes wrong when office
hours become an unstaffed support queue, when attendance dwindles because nobody knows what they are for, or when
real sensitive content ends up on a shared screen.

## When to use

- Learners stall after training because they have nobody to ask when they try it on real work.
- The service desk receives "how do I" questions about Copilot that are really learning needs.
- A launch wave or new agent is going live and people will need hands-on help in the following weeks.
- Existing clinics have gone quiet, or are dominated by the same few people.
- The learning team has no view of what people are struggling with between sessions.

## When not to use

- Designing the whole user support model, including the service desk and escalation to Microsoft - use `copilot-adoption:adoption-support-model`.
- Support for deployed agents and AI solutions in operation - use `ai-operations:ai-support-model`.
- Community rituals for the Champion network, such as community calls and show-and-tell - use `champions:champion-community-design`.
- Structured sessions with a running order and planned practice - use `learning-and-skills:facilitator-guide`.
- Ongoing nudges and refreshers to reinforce habits after launch - use `copilot-adoption:adoption-reinforcement`.

## Questions to ask first

1. What do people most need help with now - first use, a role's scenarios, a new agent, Cowork tasks, building - and which audiences?
2. Who can staff office hours, with agreed time - the learning team, adoption team, Champions, makers, a partner?
3. When and how can the target audiences attend, given shifts, time zones and meeting load?
4. Where do questions go that office hours should not answer - faults, access, data concerns, licensing?
5. How will themes from office hours reach the people who own curricula, guidance and the scenario catalogue?

## Required inputs

- The support model and its routes from `copilot-adoption:adoption-support-model`, so office hours know where to send what they do not handle.
- The learning calendar and current curricula, so clinics follow sessions at the right time.
- Agreed time from the people who will staff the clinics, confirmed with their managers.
- The approved-use guidance and the security reporting route.

If no support model exists, agree at minimum where faults, access issues and data concerns go before the first clinic,
and record the gap. If staffing time is not agreed, start with a smaller rhythm that can be sustained rather than a
schedule that collapses after a month.

## Decision framework

Choose formats by need.

| Format | Suits | How it runs |
|---|---|---|
| Open drop-in | Any question after foundation learning | Regular slot, join without booking, one or two hosts, small breakout for screen-sharing |
| Themed clinic | A scenario, an app, a new agent, Cowork delegation, evidence help | Short demo of one pattern, then questions on that theme |
| Bookable short slot | Role-specific or sensitive questions | One-to-one or small team, booked, private screen-sharing |
| Maker clinic | Agent Builder, Copilot Studio or automation builders | Hosted by experienced makers; builds stay in approved environments |
| Embedded clinic | Teams in a launch wave or frontline groups | Held in the team's own space or huddle, at their time |

Triage every question into one of these routes.

| Question type | Route |
|---|---|
| How to do something, which prompt, how to check | Answer in office hours |
| Something is broken, access missing, licence not applied | Service desk route from the support model |
| Possible data exposure or inappropriate output | Security reporting route, immediately |
| Idea for an agent, automation or new scenario | Idea intake from the support model |
| Licensing or data protection question | Licensing owner or the DPO; never answered in the clinic |

## Practitioner approach

Decide what office hours are for and say it plainly: "bring something you are trying to do with Copilot and we will
work it through with you." That promise sets expectations and stops clinics turning into a fault queue. Advertise them
at the end of every learning session, in onboarding material and in the team channels for each launch wave.

Time clinics to the learning. Demand peaks in the one or two weeks after a session or a new capability goes live, so
add themed clinics in that window and thin them out afterwards. A sustainable rhythm that people can rely on is worth
more than a busy schedule that fades.

Staff them with people who can actually help. A learning or adoption professional should host, with a rotating Champion
or experienced maker for themed clinics. Agree time with each host's manager and record it. Brief hosts on triage: what
they answer, what they route, and that they never improvise answers on licensing, data protection or access.

Make screen-sharing safe. Real work is the point, but real work can contain sensitive content. In open drop-ins, move
anyone who needs to share their screen into a private breakout with one host, and remind them to close anything they
would not want seen. Hosts never ask people to paste sensitive content into chat. If someone discovers that Copilot has
surfaced content they should not see, the host stops, reassures them and uses the security reporting route.

Teach rather than fix. When someone brings a problem, solve it with them on their own screen and then name the pattern
they used - "you gave it the document as context and asked it to list what it could not find" - so they leave with
something reusable. Where an answer would help others, write it up as a short tip with fictional content.

Capture themes, not people. After each clinic, the host records the topics raised, the routes used and any gaps in
guidance or curricula, without names. Review the themes monthly with the Learning Lead and the adoption lead. Recurring
themes become new curriculum content, updated guidance, scenario catalogue entries or a fix to a known product issue.
This feedback loop is what makes office hours worth their cost.

Keep them alive. If attendance drops, check timing, promotion and whether a themed format would draw people better;
if they are overwhelmed, add hosts or bookable slots. Close clinics deliberately when the need has passed rather than
letting them dwindle unattended.

## Outputs

- An office hours plan recorded in the office hours section of the `ai-learning-plan` template - formats, rhythm, hosts and agreed time, booking, triage routes and promotion.
- A host briefing covering purpose, triage, safe screen-sharing and the reporting route.
- A theme log with topics, routes and gaps, recorded without names.
- A monthly themes summary for the Learning Lead and adoption lead, with actions for curricula and guidance.

## Microsoft platform considerations

Clinics usually run in Teams, with breakout rooms for private screen-sharing and a booking tool for short slots.
Hosts help with the Copilot experiences people are approved to use; maker clinics keep any building in approved
environments. Product behaviour changes often, so hosts check current behaviour in `references/sources.md` before
themed clinics and record "product changed" as a theme when guidance no longer matches.

## Adoption considerations

Office hours are a bridge between learning and habit. They work best when managers encourage people to attend with a
real task and when Champions in each team point colleagues to them. Their place in the wider support model should be
clear so people know where to go first.

## Knowledge considerations

Answers that help many people should become short tips, prompt patterns or scenario catalogue entries with an owner.
Office hours are a signal of where guidance or content is missing, and themes about missing or untrusted content go to
`knowledge-management:knowledge-gap-analysis`.

## Security and privacy considerations

Screen-sharing happens in private breakouts. Hosts never ask for sensitive content in chat and know the reporting route
for suspected data exposure. Clinics are not recorded unless participants agree and recordings are checked before
sharing. Theme logs contain no names.

## Responsible AI considerations

Hosts reinforce verification and judgement in every answer, and raise concerns about harmful or inappropriate outputs
through the reporting route. People's worries about AI and their work are heard and routed, not dismissed.

## Evaluation requirements

Not applicable as AI evaluation, because office hours do not release an AI solution. The service is reviewed monthly on
whether themes lead to changes in curricula and guidance.

## Value measures

Baseline: "how do I" Copilot tickets at the service desk and attendance at existing clinics before the plan starts.
Measures: clinic attendance by team, share of questions resolved in the clinic, change in "how do I" tickets, and the
number of theme-driven changes to learning and guidance. Owned by the Learning Lead, reported at team level and never
by named attendee.

## Scale notes

### Starter

One open drop-in a week hosted by the adoption or learning lead, with themed clinics after each session and a simple
theme log.

### Scale

Open drop-ins plus themed and maker clinics, rotating Champion hosts with agreed time, bookable slots and a monthly
theme review feeding curricula.

### Enterprise

Regional and business-unit clinics on a shared format, embedded clinics for frontline groups, central theme analysis
across regions and alignment with the service desk's knowledge base.

## Hand-offs

- To `copilot-adoption:adoption-support-model` when office hours keep receiving faults or access issues that belong elsewhere.
- To `learning-and-skills:ai-role-curriculum` with recurring themes that need new or changed modules.
- To `knowledge-management:knowledge-gap-analysis` when questions reveal missing or untrusted content.
- To `copilot-adoption:scenario-discovery` with new scenarios people bring to clinics.

## Reviewer gates

Not applicable, because office hours do not release an AI solution. Suspected data exposure raised in a clinic follows
the security reporting route immediately.

## Failure modes

- Office hours become an unstaffed fault queue, hosts burn out and learners stop coming.
- Sensitive content is shown on shared screens because there is no private breakout.
- Themes are never reviewed, so the same questions recur and the curriculum never improves.
- Clinics are scheduled when the target audience cannot attend, such as shift workers during their shifts.
- Hosts improvise answers on licensing or data protection and give wrong assurances.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Record or report who attended office hours or what they asked by name.
- Ask people to share sensitive content in open sessions or chat.
- Answer licensing or data protection questions in the clinic instead of routing them.
- Rely on unagreed volunteer time to staff clinics.

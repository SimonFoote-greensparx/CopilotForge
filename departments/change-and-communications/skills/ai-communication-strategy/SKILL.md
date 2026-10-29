---
name: ai-communication-strategy
description: Sets the communication strategy for an AI change - the narrative and core messages, honest answers to hard questions on jobs, monitoring and data, an audience, message, sender and channel matrix, a phased calendar, listening routes and the approval path for sensitive messages. Use when an AI programme needs to reach the workforce, when messages conflict or ring hollow, or before a wave, policy change or new AI experience is announced.
license: CC-BY-4.0
metadata:
  department: change-and-communications
  lifecycle: Envision, Mobilise, Enable, Launch, Scale
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-privacy, ms-copilot-overview, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# AI communication strategy

## Purpose

This skill decides what the organisation says about its AI change, who says it, to whom, through which channels and
when, and how it listens to the answers. It turns the vision, the stakeholder map and the people impact into a short
narrative, a few core messages, agreed answers to the questions people actually ask, and a calendar that reaches each
audience through senders they trust. AI communications usually go wrong in one of three ways: enthusiasm without
substance ("AI will transform everything"), silence on the questions people care about most (jobs, monitoring and data),
or one central broadcast that never reaches the frontline or invites a reply.

## When to use

- An AI programme, Copilot rollout or new AI experience needs to reach the workforce and there is no plan for how.
- Different leaders are saying different things about AI, or staff hear about changes from rumour first.
- Messages have gone out but questions about jobs, monitoring or data protection keep coming back.
- A new wave, agent, approved-use policy or significant Microsoft change needs announcing.
- Sponsors and managers need talking points that are consistent and honest.

## When not to use

- Writing the AI vision, ambition and principles themselves - use `ai-strategy:ai-vision`.
- Planning a time-boxed campaign around a scenario theme - use `change-and-communications:adoption-campaign-plan`.
- Sequencing launch waves, onboarding and support - use `copilot-adoption:launch-plan`.
- Telling users and affected people that a specific solution uses AI and how - use `responsible-ai:ai-transparency`.
- Finding and preparing success stories - use `change-and-communications:success-stories`.

## Questions to ask first

1. What is changing, for whom, and when, and what outcome does the sponsor want people to understand?
2. What is the agreed position on the hard questions - jobs, use of usage data, what happens to prompts and files, and what people must not do?
3. Which audiences are in scope, and what does each already believe and worry about?
4. Which senders does each audience trust, and which channels does each actually read or attend?
5. Who must approve sensitive messages - HR, the DPO, legal, employee representatives - and how long do they need?

## Required inputs

- The vision and principles from `ai-strategy:ai-vision` and outcomes from `ai-strategy:strategic-outcomes`.
- The stakeholder map and concern register from `change-and-communications:ai-stakeholder-mapping`.
- Group-level impact from `change-and-communications:people-change-impact`.
- The audience model from `copilot-adoption:audience-segmentation` and the launch plan from `copilot-adoption:launch-plan`.
- The approved-use guidance and the route for reporting suspected data exposure.

If the position on jobs or usage data has not been agreed, do not draft around it. Escalate to the sponsor and HR, and
hold broad announcements until there is an honest answer, even if that answer is a date by which a decision will be made.

## Decision framework

Choose the sender by the message, not by seniority.

| Message type | Best sender | Why |
|---|---|---|
| Why the organisation is adopting AI and what it will not do | Executive sponsor | Authority and accountability for the direction |
| What it means for this team and what is expected | Line manager | Trusted, can answer locally and adjust |
| How to use it well in this role | Champions and peers | Credible on practice, shows rather than tells |
| What is allowed and how data is protected | Security or data protection lead, through managers | Precision and authority on rules |
| What changed in the tools | Adoption lead | Practical, timely and specific |

Match the channel to what the message needs.

| Message needs | Prefer | Avoid |
|---|---|---|
| Two-way discussion of concerns | Team meetings, small-group sessions, open forums with questions | Email only |
| Reach across the whole workforce | Intranet, all-staff channel, leader video, then repeated by managers | One-off events with no recording |
| Frontline and deskless reach | Shift huddles, supervisor briefings, mobile channels | Desk-based channels alone |
| Precision on rules | Written guidance linked from every message | Rules paraphrased differently by each sender |

Phase the calendar: awareness before access (why and what is coming), readiness in the weeks before a wave (what to
expect, guidance, support), launch (how to start, where to get help), and sustain (stories, changes, answers to new
questions). Every phase has a listening step.

## Practitioner approach

Start with the narrative. In a few sentences, say why the organisation is adopting AI, what it expects to improve, what
it will not do, and what it asks of people. Test it by reading it aloud to someone outside the programme. If it relies
on words like "transform" or "unlock" without saying what will actually be different on a Tuesday afternoon, rewrite it.

Agree the hard answers before anything else is published. People's first questions are usually: is this about cutting
jobs, will my usage be monitored, can my prompts be read, what happens if it gets something wrong, and what am I not
allowed to do. Work through each with the sponsor, HR, the DPO and the security lead, and write the agreed answer in
plain words. Where the honest answer is unsettled, say what is known, what is not and when it will be decided.
Answers on data handling must match the organisation's actual configuration and the current Microsoft source records.

Write three to five core messages from the narrative and the hard answers. Then adapt them by audience using the
stakeholder map and impact assessment: high-impact groups need specific information about their work, sceptical groups
need evidence and a route to raise concerns, and frontline groups need short, practical messages in channels they can
reach during paid time.

Build the audience, message, sender and channel matrix. Route most messages through managers, because people ask their
manager what a change means for them; give managers a short briefing and talking points before their teams hear
anything, through `change-and-communications:manager-enablement`. Reserve the sponsor for direction and commitments,
and use Champions and peers for practice.

Design listening in from the start: an open question channel, questions collected at every session, pulse questions at
group level, and a regular review of what people are asking. Publish answers to new questions, and change the plan when
questions show a message has not landed. Communications that never change in response to questions are broadcasting,
not communicating.

Set an approval path proportionate to sensitivity. Routine updates need the adoption lead. Messages touching jobs,
monitoring, employee data or consultation need HR and the DPO, and possibly the legal adviser and employee
representatives, with lead time built into the calendar.

Measure understanding, not volume. Track whether people can say why the organisation is adopting AI, know what is
allowed, and know where to get help, through short pulse questions reported at group level. Reach statistics alone
show only that something was sent.

## Outputs

- An AI communications plan on the `ai-communications-plan` template: narrative, core messages, hard questions and agreed answers, audience matrix, senders, phased calendar, listening routes, approval path and measures.
- A sponsor and manager talking-points pack aligned to the core messages.
- A living questions-and-answers page with an owner and review date.
- A monthly note to the sponsor on what people are asking and what changed in response.

## Microsoft platform considerations

Messages that describe what Copilot, agents or Cowork can see, store or do must reflect the organisation's actual
configuration and the current source records in `references/sources.md`, including the privacy records, because
details change. Route any licensing statement to the Microsoft licensing guide or a licensing partner, and avoid
building messages on product names, which Microsoft changes often.

## Adoption considerations

Communications create awareness and permission; adoption comes from practice. Link every message to a next step people
can take (a starting scenario, a session, a support route), coordinated with `copilot-adoption:launch-plan`.

## Knowledge considerations

The questions-and-answers page and the approved-use guidance are knowledge assets. Give each an owner and a review
date, and keep a single source that every message links to rather than restating rules in many places.

## Security and privacy considerations

Every broad message links to the approved-use guidance and the route for reporting suspected data exposure. Statements
about monitoring and usage data must be agreed with the DPO and must be true. Listening data is reported at group level
above the minimum group size.

## Responsible AI considerations

Be candid about limits: AI can be wrong, people remain accountable for what they send and decide, and some uses are
not permitted. Never overstate capability to build enthusiasm. Transparency notices for specific solutions belong to
`responsible-ai:ai-transparency`.

## Evaluation requirements

Not applicable as solution evaluation, because this is a communications practice. Key messages are tested with a small
group from each priority audience before broad release, and revised where they are misunderstood.

## Value measures

Owned by the change lead, with a baseline pulse before the first broad message: understanding of why, awareness of
what is allowed and where to get help, confidence to raise concerns, and time to publish answers to new questions.
Reported by group above the minimum size, never for individuals.

## Scale notes

### Starter

A one-page plan, a handful of agreed answers, the sponsor and managers as main senders, and existing channels.

### Scale

A full matrix by audience and wave, a manager briefing rhythm, a living questions-and-answers page and a monthly
listening review.

### Enterprise

A central narrative and answer set with regional and divisional adaptation, translation and local approval routes, and
a shared calendar coordinated with other major changes.

## Hand-offs

- To `change-and-communications:manager-enablement` for manager briefings and talking points.
- To `change-and-communications:adoption-campaign-plan` for time-boxed campaigns within the calendar.
- To `change-and-communications:success-stories` for stories that bring the messages to life.
- To `change-and-communications:resistance-management` when listening shows hardened concerns.

## Reviewer gates

Not applicable as a formal reviewer gate, because communications do not release an AI solution. Messages about jobs,
monitoring or employee data pass the HR, DPO and legal approval path set out in the plan.

## Failure modes

- Messages promise transformation with no specifics, and staff treat the programme as hype.
- Questions about jobs and monitoring go unanswered, so rumour fills the gap.
- Managers hear the news at the same time as their teams and cannot answer questions.
- Statements about data handling do not match the actual configuration, and trust collapses when the difference emerges.
- Frontline audiences are reached only through channels they cannot access during work.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Publish a statement about jobs, monitoring or data handling that HR, the DPO and the sponsor have not agreed.
- Overstate what AI can do, or imply it is never wrong.
- Let teams hear about a change that affects them before their managers have been briefed.
- Report communications success by messages sent rather than understanding.

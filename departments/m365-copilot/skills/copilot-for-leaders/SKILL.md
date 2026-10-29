---
name: copilot-for-leaders
description: Defines the scenario set and safeguards for leaders' own Copilot use - meeting preparation, mail triage, long papers, staff messages, working rules for delegates - and the firm limit on using Copilot near decisions about people, each scenario tested on real leadership work. Use when leaders need scenarios that fit their week, when delegate rules are unclear, or when Copilot has been used near a decision about a person.
license: CC-BY-4.0
metadata:
  department: m365-copilot
  lifecycle: Enable, Launch
  maturity: explorer, adopter, scaler, ai-enterprise
  risk-tiers: 0, 1, 2
  platforms: m365-copilot, copilot-chat
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, responsible-ai
  sources: ms-copilot-overview, ms-copilot-privacy, ms-copilot-adoption-hub, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Copilot for leaders

## Purpose

Leaders' work is dominated by meetings, mail, long papers and communication, which is where Copilot can help most. Their
content is also among the most sensitive in the organisation, and their decisions often affect people. This skill
defines the scenarios, working habits and safeguards for leaders' own use of Copilot, from executives to people
managers, so they get real value and model good practice. It goes wrong when leaders are shown generic demonstrations
they never repeat, or when a leader asks Copilot to summarise an employee's contribution and treats the answer as
evidence.

## When to use

- Senior leaders or people managers are receiving Copilot and need scenarios that fit their working day.
- Executive assistants or delegates work in leaders' mailboxes and calendars and their use needs clarity.
- A leader has used Copilot near a decision about a person, and guidance is needed.
- Leaders' use has faded after an initial demonstration.

## When not to use

- Running the adoption activity that gets executives using Copilot and leading adoption visibly - use `copilot-adoption:executive-enablement`.
- Equipping line managers to lead adoption in their teams - use `change-and-communications:manager-enablement`.
- Securing and equipping the executive sponsor of the AI programme - use `ai-strategy:executive-sponsorship`.
- Writing scenario cards for a non-leadership role - use `m365-copilot:copilot-role-scenarios`.
- Reviewing the sensitivity of board and executive content locations - use `m365-copilot:work-context-readiness`.

## Questions to ask first

1. Which leadership audiences are in scope (executives, senior managers, people managers), and how do their weeks differ?
2. Which recurring tasks take most of their time: meeting preparation, mail, reading papers, writing, one-to-ones?
3. Who works on their behalf (executive assistants, chiefs of staff, delegates), and with what access?
4. Where do board, executive and HR papers live, and who can open them today?
5. What decisions about people do these leaders make, and what does the organisation's approved process require?

## Required inputs

- The leadership audiences in scope and a few leaders willing to test scenarios on their real work.
- The delegate and assistant arrangements for those leaders.
- A work context readiness verdict for executive, board and HR locations.
- The approved-use guidance, including the position on decisions about people.

If executive and board locations have not been checked for oversharing, do that first through
`m365-copilot:work-context-readiness`; leaders' scenarios make that content easy to find.

## Decision framework

| Leader task | Recommended Copilot use | Safeguard |
|---|---|---|
| Preparing for a meeting | Summarise the relevant thread, papers and previous actions | Open the cited papers for anything that will be quoted |
| Catching up after absence | Summarise mail and chats by priority | Check nothing urgent was omitted; do not reply on summary alone |
| Digesting a long paper | Summarise, extract risks and questions to ask | Read the sections that matter for the decision |
| Drafting a message to staff | Draft from key points, adjust tone for audience | Leader edits and owns the message; check facts |
| One-to-ones and feedback | Help structure the conversation and the leader's own notes | Never ask Copilot to assess, rate or compare people |
| Decisions on hiring, pay, performance or conduct | Not used to form or justify the decision | Follow the approved HR process |
| Working through a delegate | Delegates use Copilot within their own access and the leader's agreed rules | Agree what the delegate may do on the leader's behalf |

## Practitioner approach

Start with a leader's real week. Spend half an hour with two or three leaders and their assistants, looking at the
calendar and inbox pattern of a typical week. Identify the three or four recurring moments where time is lost: the
Monday catch-up, the pre-read for the leadership meeting, the monthly staff message, the follow-up after a long meeting.
Those become the leader's scenarios; anything else is a distraction.

Make each scenario concrete and short: the moment, the prompt pattern, the content it relies on and the check. Leaders
respond to a scenario that saves them twenty minutes before their next meeting, not to a tour of features. Test each one
with the leader on their real content, with their agreement, and adjust.

Pay close attention to delegates. Executive assistants often do much of the preparation; agree with each leader what an
assistant may ask Copilot to do with the leader's content, within the access the assistant already has. Confirm with IT
how Copilot behaves for delegated access from the current source records rather than assuming.

Be explicit about decisions about people. Leaders frequently ask, half-jokingly, for Copilot to summarise how someone
has performed. Explain why that is outside approved use: the output reflects only what is written in content the leader
can see, it can be wrong or skewed, and it may breach employment and data protection obligations. Offer the acceptable
alternative: Copilot can help a leader structure their own notes and prepare a conversation, but it does not assess the
person. Route any request to go further to `responsible-ai` and HR.

Help leaders model good practice. A leader who says in a meeting "I used Copilot to summarise the papers and checked the
figures myself" teaches more than any campaign. Coordinate with `copilot-adoption:executive-enablement` so the adoption
team uses these scenarios in leaders' sessions and follow-up.

Revisit the scenarios after a month with each leader, retire those not used and add those that emerged.

## Outputs

- A leaders' scenario set by audience (executives, senior managers, people managers), recorded in the `scenario-catalogue` with prompt patterns, content, checks and safeguards.
- A short guide for executive assistants and delegates, agreed with each leader.
- Plain-language guidance on Copilot and decisions about people, agreed with HR.

## Microsoft platform considerations

Leaders' scenarios rely heavily on Copilot in Outlook and Teams and on Microsoft 365 Copilot Chat with work grounding.
How Copilot respects permissions and delegated access is described in `ms-copilot-privacy`; app capability is in
`ms-copilot-overview`. Both change often, so confirm current behaviour before advising on delegation or specific features.

## Adoption considerations

Leaders' visible use is one of the strongest adoption signals in an organisation. Feed the scenario set into
`copilot-adoption:executive-enablement` and `change-and-communications:manager-enablement`, and encourage leaders to
share honest examples, including where Copilot did not help.

## Knowledge considerations

Not applicable in depth, because leaders mainly work on their own mail, meetings and papers; where leaders depend on
shared reference content such as policies or board packs, its location and owner are noted in the scenario.

## Security and privacy considerations

Executive, board and HR content is highly sensitive. Confirm its locations are restricted before leaders' scenarios
launch, agree delegate rules, and route concerns to `security-privacy` and the data protection lead.

## Responsible AI considerations

Copilot must not be used to assess, rate, rank or compare individuals, or to form or justify decisions about hiring,
pay, performance or conduct, outside the organisation's approved process. Any proposal to do so is referred to
`responsible-ai` and HR.

## Evaluation requirements

Each scenario is tested with at least two leaders on real content and recorded as usable, usable with edits, or not
usable. The guidance on decisions about people is checked with HR before release.

## Value measures

Ask leaders, at audience level, about time recovered on their chosen scenarios and the quality of preparation, against a
short baseline taken at the start. The adoption lead owns these measures. Never report an individual leader's usage.

## Scale notes

### Starter

Three or four scenarios tested with the leadership team and their assistants, and a single page of guidance on
decisions about people.

### Scale

Separate scenario sets for executives, senior managers and people managers, delivered through executive enablement and
manager briefings, and reviewed quarterly.

### Enterprise

A common leadership scenario set with business-unit variants, delegate guidance standardised across executive offices,
and HR-owned guidance on decisions about people.

## Hand-offs

- To `copilot-adoption:executive-enablement` for leader sessions and follow-up.
- To `change-and-communications:manager-enablement` for people managers leading adoption.
- To `m365-copilot:work-context-readiness` for executive and board content locations.
- To `responsible-ai:human-oversight` where a leader proposes using Copilot near decisions about people.

## Reviewer gates

From risk tier 1, guidance touching decisions about people is reviewed by `responsible-ai`, and executive content
locations by `security-privacy`; each finding is blocking or advisory, and blocking findings stop release of the
affected scenarios.

## Failure modes

- Leaders see a generic demonstration, never find their own scenarios, and stop using Copilot.
- A leader quotes a Copilot summary of a paper in a decision meeting, and it is wrong.
- A leader asks Copilot to summarise an employee's contribution, and the output shapes a performance conversation.
- Board papers sit in an overshared location and become easy to find once Copilot is in use.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Encourage leaders to use Copilot to assess, rate or compare people.
- Launch leaders' scenarios before executive and board content locations are checked.
- Assume how delegated access behaves without checking current documentation.
- Report on an individual leader's Copilot usage.

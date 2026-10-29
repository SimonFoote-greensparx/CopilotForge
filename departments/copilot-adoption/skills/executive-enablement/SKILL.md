---
name: executive-enablement
description: Enables executives to use Copilot in their own work and lead its adoption visibly - private or small-group sessions on their real tasks, support for executive assistants and chiefs of staff, care with sensitive leadership content, and the visible behaviours that give others permission to experiment. Use when leaders hold licences but rarely use them, before a launch where executives go first, or when leaders' messages about AI ring hollow.
license: CC-BY-4.0
metadata:
  department: copilot-adoption
  lifecycle: Mobilise, Enable, Launch
  maturity: explorer, adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, copilot-cowork
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-overview, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Executive enablement

## Purpose

People watch what leaders do far more closely than what they say. An executive who uses Copilot to prepare for a board
meeting and talks about what worked and what did not does more for adoption than any campaign. This skill enables the
executive team to use Copilot in their own work and to lead its adoption visibly, while handling the sensitivity of
leadership content with care. It usually goes wrong when executive sessions become product briefings, when leaders
endorse Copilot without using it, when executive assistants are forgotten, or when leaders ask for usage league tables
as a way of showing support.

## When to use

- A launch is planned and executives are expected to go first and set the tone.
- Leaders have had access for some time but rarely use it, and their teams have noticed.
- Leadership messages about AI sound generic because leaders have little personal experience to draw on.
- A new executive joins, or the executive team changes, and needs bringing up to the same level.
- Executive assistants and chiefs of staff are asking how to support leaders who use Copilot.

## When not to use

- Defining Copilot scenarios and habits for leaders in product detail - use `m365-copilot:copilot-for-leaders`.
- Securing and equipping the executive sponsor of the whole AI programme - use `ai-strategy:executive-sponsorship`.
- Defining the sponsor's role in the Centre of Excellence - use `ai-centre-of-excellence:coe-sponsor-role`.
- Equipping line managers across the organisation - use `change-and-communications:manager-enablement`.
- Writing the organisation's AI messages and channels - use `change-and-communications:ai-communication-strategy`.

## Questions to ask first

1. Which executives are in scope, what Copilot access do they have, and has IT confirmed it works on the devices they actually use?
2. What recurring work takes most of each executive's preparation time - board papers, briefings, inbox, meetings, reviews?
3. How sensitive is the content leaders work with, and has the permissions position for executive sites and mailboxes been reviewed?
4. Do executive assistants or chiefs of staff work on leaders' behalf, and how will they be enabled alongside them?
5. What visible commitments will each executive make once they are confident, and who will help them keep them?

## Required inputs

- The list of executives in scope and their access, confirmed by IT.
- Scenarios for leaders from `m365-copilot:copilot-for-leaders` or `copilot-adoption:scenario-discovery`.
- The approved-use guidance and any specific rules for highly confidential or regulated leadership content.
- The permissions review covering executive and board content, from `copilot-adoption:adoption-readiness`.
- The launch plan, so executive enablement is timed before the first wave.

If the permissions review has not covered leadership content, enable executives on low-sensitivity tasks first and
record the gap. If an executive does not want to take part, do not force it; work with those who will and let their
example travel.

## Decision framework

Choose the format by the executive's context, not by rank.

| Context | Format |
|---|---|
| Executive keen, limited time | One private session on their own real tasks, then a short follow-up a fortnight later |
| Executive team learning together | Small-group session with peers, using fictional or approved leadership material |
| Executive sceptical or worried | Private conversation first about concerns, then one task that matters to them |
| Executive relies heavily on an assistant | Joint session with the executive and assistant, plus an assistant-only follow-up |

Agree visible leadership behaviours that each executive is comfortable with. Pick a few, not all.

| Behaviour | What it looks like |
|---|---|
| Use it visibly | Mentions in a meeting or message how Copilot helped prepare |
| Show the limits | Shares an example where the output needed correcting and how they checked it |
| Give permission | Tells teams explicitly that time spent learning is legitimate |
| Ask about practice | Asks teams what worked, never who has used it |
| Back the network | Thanks Champions publicly and attends a showcase |
| Route ideas | Sends ideas for agents or automation to intake rather than commissioning directly |

## Practitioner approach

Prepare before you meet. Ask each executive's assistant or office for their recurring work: the papers they read, the
briefings they write, the meetings they chair. Choose three tasks where Copilot can plausibly help and where the
executive can judge the result. Check with IT that access works on the executive's devices, including mobile, before
the session; a failed demonstration with a senior leader is hard to recover from.

Keep the session about their work. Thirty to forty-five minutes on the executive's own tasks, done live, beats any
overview. Show summarising a long paper and checking the summary against the source, preparing for a meeting from
recent correspondence, drafting a message in their voice and editing it. Show what Copilot draws on and what it cannot
see, and demonstrate verification every time. Leave them with the three tasks to try that week.

Handle sensitivity openly. Leadership content often includes board material, personnel matters, transactions and
regulatory correspondence. Explain the approved-use guidance for such content, confirm that the permissions review has
covered it, and agree any additional rules. Leaders who trust the safeguards use Copilot more freely; leaders who are
unsure stop altogether.

Enable assistants and chiefs of staff alongside executives. They prepare much of a leader's material and often adopt
faster. Give them their own session on their work, clarify with IT how delegated access and Copilot interact for the
organisation's configuration, and connect them to the Champions community.

Follow up after a fortnight. Ask what worked, what did not and what they want to try next. This is where most
executives either form a habit or quietly stop, so a short follow-up is worth more than a longer first session.

Then ask for visible leadership. Once an executive has genuine experience, agree two or three behaviours from the
framework. The most powerful is a short story told in a team meeting or all-hands, including the limits. Help them
draft it if needed, but it must be true.

Watch for well-meant requests that damage adoption. Executives sometimes ask for dashboards of who is using Copilot to
show support. Redirect them to team-level measures and to asking about practice, explaining that individual tracking
undermines the trust adoption depends on.

## Outputs

- An executive enablement plan recorded in the executive and manager section of the `adoption-plan` template: executives in scope, format, tasks, session dates, follow-up and agreed behaviours.
- A task brief for each executive session, using fictional or approved material.
- An assistant and chief of staff enablement outline.
- A short record of the visible behaviours each executive has agreed, kept by the adoption lead.

## Microsoft platform considerations

Executives often work across desktop, web and mobile, and their experience may include Copilot Chat, Copilot in the
Microsoft 365 apps and Copilot Cowork. Delegated access, shared mailboxes and confidential sites behave according to
the organisation's configuration, which IT must confirm. Check current capability and data handling in
`references/sources.md` before the sessions rather than relying on a previous demonstration.

## Adoption considerations

Executive behaviour sets the tone for every launch wave. Time executive enablement before the first wave, link
executives' stories to the communications plan, and make sure their asks of managers match the programme's messages.

## Knowledge considerations

Not applicable as a primary concern, because executive enablement uses leaders' own work context rather than shared
grounding content. Where leaders find organisational content stale or hard to locate, pass the observation to
`knowledge-management:knowledge-gap-analysis`.

## Security and privacy considerations

Leadership content is among the most sensitive in any organisation. Confirm the permissions review has covered it,
explain the rules for confidential and regulated material, and use fictional or approved material in group sessions.
Never demonstrate with real personnel, transaction or board content in front of others. Data protection questions end
with the organisation's DPO.

## Responsible AI considerations

Executives must model accountability: Copilot drafts and summarises, but the leader owns the decision and the words.
Where leaders consider using Copilot output to inform decisions about people, remind them that such uses need human
judgement and, if built into a process, risk classification.

## Evaluation requirements

Not applicable as solution evaluation, because this skill enables people rather than building an AI solution. Each
executive's follow-up records whether the three tasks became habits and which behaviours were agreed.

## Value measures

Owned by the adoption lead and reported to the sponsor: executives enabled, follow-ups completed, visible behaviours
agreed and carried out, and team-level adoption indicators in the areas they lead, treated as context rather than proof
of cause. Never individual usage figures for executives or anyone else.

## Scale notes

### Starter

One small-group session for the leadership team, a follow-up conversation and an agreement that the most senior leader
will share one honest story.

### Scale

Private sessions for each executive, assistant enablement, a fortnight follow-up and agreed behaviours linked to the
launch waves.

### Enterprise

Executive enablement cascaded to divisional and regional leadership teams, a consistent behaviour set, assistant
networks connected to the Champions community, and stories coordinated with communications.

## Hand-offs

- To `m365-copilot:copilot-for-leaders` for deeper leader scenarios and habits.
- To `change-and-communications:ai-communication-strategy` to place executives' stories in the communications plan.
- To `change-and-communications:manager-enablement` so managers hear consistent asks.
- To `champions:champion-community-design` to connect assistants and executive sponsors to the community.

## Reviewer gates

Not applicable as a formal gate, because enabling executives on approved Copilot experiences at tiers 0 and 1 relies on
the readiness assessment, where `security-privacy` has reviewed permissions for leadership content.

## Failure modes

- The executive session is a product briefing, and leaders leave without having tried anything on their own work.
- Leaders endorse Copilot in messages but do not use it, and staff notice.
- Executive assistants are left out, so the people who prepare leaders' material are the least enabled.
- A demonstration with real confidential content creates a privacy concern and sets the programme back.
- Leaders ask for individual usage league tables as a show of support, and trust collapses.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Demonstrate with real board, personnel or transaction content in a group session.
- Script leadership stories that did not happen.
- Provide executives with usage data about named individuals.
- Enable executives on sensitive content before the permissions review has covered it.

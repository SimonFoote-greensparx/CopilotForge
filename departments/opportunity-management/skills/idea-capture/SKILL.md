---
name: idea-capture
description: Designs and runs the organisation's open route for staff to submit AI ideas - the submission channels, a short form, acknowledgement and triage timings, duplicate checks, idea campaigns and feedback to every submitter - so ideas reach the backlog instead of side requests. Use when there is no obvious place to send AI ideas, when ideas arrive through managers and chat threads and get lost, or when submissions have dried up.
license: CC-BY-4.0
metadata:
  department: opportunity-management
  lifecycle: Discover, Envision
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: m365-copilot, copilot-studio, power-platform, sharepoint
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-champion-programme, ms-coe-starter-kit
  status: draft
  authors: Simon Foote
---

# Idea capture

## Purpose

This skill builds and runs the front door through which anyone in the organisation can put forward an AI idea. It keeps
the door open and easy to use, makes sure every submission is acknowledged and triaged within a known time, and feeds
ideas into the backlog where framing can begin. Idea capture usually goes wrong in two opposite ways: the form is so
long that only enthusiasts complete it, or ideas are collected with fanfare and then disappear, so staff conclude that
nobody was listening and stop contributing.

## When to use

- The organisation has no single, known place to send AI ideas.
- Ideas arrive through managers, emails, chat threads and corridor conversations, and many are lost or duplicated.
- A CoE or programme is launching and needs an intake route from day one.
- Submissions have dried up, or come only from one enthusiastic team.
- Leaders want to run a time-boxed idea campaign or challenge around a strategic outcome.

## When not to use

- Turning one submitted idea into a framed problem with an owner and baseline - use `opportunity-management:problem-framing`.
- Running the backlog board, stages and fields once ideas are in - use `opportunity-management:backlog-management`.
- Finding everyday Copilot use cases for a role as part of adoption - use `copilot-adoption:scenario-discovery`.
- Designing Champion challenges that build skills - use `champions:champion-challenges`.
- Running the CoE's opportunity pillar as a whole - use `ai-centre-of-excellence:coe-opportunity-pipeline`.

## Questions to ask first

1. Where do AI ideas currently go, and what happens to them?
2. Who will triage submissions, how often, and how quickly can they acknowledge them?
3. Which channels do staff, including frontline and deskless staff, actually use day to day?
4. What is the minimum information needed to start framing, and nothing more?
5. Which strategic outcomes, if any, should campaigns focus ideas on this year?

## Required inputs

- A named intake owner (usually the AI portfolio manager or CoE lead) and triage capacity.
- The backlog location and its capture stage, from `opportunity-management:backlog-management`.
- The strategic outcomes, so ideas can be tagged against them.
- The organisation's collaboration tools and the channels different groups of staff use.

If triage capacity cannot be confirmed, do not launch the route; an unattended front door does more harm than none.
Never collect more personal data about submitters than the follow-up needs.

## Decision framework

Choose channels by reach and by how staff actually work. Every channel ends in the same capture record.

| Channel | Use it when | Watch for |
|---|---|---|
| Short web form (for example Microsoft Forms or a SharePoint list form) | Always, as the default route everyone can find | Field creep; keep it to the minimum set |
| Teams channel or community post | The organisation already collaborates in Teams | Ideas discussed but never recorded; triage copies them into the form record |
| Champions and managers submitting on behalf of others | Frontline, deskless or less confident staff | Credit must go to the originator, not the person who typed it |
| Intake agent | Volumes are high and the CoE can own and maintain an agent | It becomes a solution in its own right, needing an owner, testing and a risk tier |
| Time-boxed campaign or challenge | A strategic outcome needs focused ideas | Raising expectations that delivery capacity cannot meet |

Keep the form to five or six fields: what is difficult today, who it affects, how often, what better would look like,
the submitter's team, and whether they are willing to help. Never ask the submitter to name a product or estimate a
benefit.

Set service levels and keep them: acknowledgement within a few working days, triage outcome within an agreed period,
and a status the submitter can see.

| Triage outcome | Next step |
|---|---|
| Ready to frame | Create a capture-stage backlog entry and route to `opportunity-management:problem-framing` |
| Duplicate or related | Link to the existing entry and tell the submitter who to talk to |
| Adoption scenario | Route to `copilot-adoption:scenario-discovery`; the answer may be "you can already do this" |
| Not an AI matter | Refer to the right route (IT service desk, process improvement) and say so |
| Needs more information | Ask one specific question, with a date |

## Practitioner approach

Start by finding where ideas already go. Ask managers, Champions and the service desk what they receive and what they
do with it. Most organisations find ideas scattered across inboxes and chats, and the first job is to give them one
destination without shutting the informal routes down; those become feeders into the same record.

Design for the least confident contributor. A frontline worker with a good idea and two minutes should be able to
submit it on a phone. Write questions in plain language about work, not technology: "What takes too long or goes wrong
in your work?" rather than "Describe your AI use case". Offer a way for Champions or managers to submit on someone's
behalf, with the originator credited.

Secure triage capacity before launch. Name who triages, how often and to what service level, and protect that time.
The commonest failure is a launch announcement followed by silence. If capacity is short, open the route to one
business unit first.

Make triage quick and consistent. Read each submission, check for duplicates in the backlog, and give it one of the
triage outcomes. Do not try to frame or assess the idea at triage; that is the next skill's job. Tag each idea with the
strategic outcome it might support and its originating team, then move it on.

Close the loop with every submitter, whatever the outcome. Tell them what happened, why, and what comes next. When an
idea is routed to adoption because the capability already exists, show them how to use it; that is often the fastest
value the programme delivers. When an idea is declined, explain the reason and thank them. Publish a regular summary of
ideas received, routed and delivered, so the wider workforce sees the route works.

Use campaigns sparingly. A focused campaign tied to a strategic outcome can surface strong ideas quickly, but only if
delivery capacity exists to act on the best of them. Agree in advance how many will be taken forward, and say so in the
launch.

Review the route quarterly: volumes by unit and channel, time to acknowledge and triage, and the share of ideas that
reach framing. Silence from a unit is a signal for the adoption and change teams, not a sign that it has no problems.

## Outputs

- An idea intake design: channels, form fields, triage owner, service levels, triage outcomes and feedback messages.
- A capture record for each idea, feeding the capture stage of the backlog on the `prioritisation-matrix` template.
- A periodic intake summary for the CoE and the workforce: ideas received, routed and progressed, by unit and outcome.
- Where used, a campaign brief stating the outcome focus, timing and how many ideas will be taken forward.

## Microsoft platform considerations

A form feeding a SharePoint list or the backlog tool is enough for most organisations. Teams channels suit communities
already working there. An intake agent built in Copilot Studio can help at volume, but it is a solution with its own
owner, risk tier and testing; treat it through `opportunity-management:ai-suitability` like any other idea. Check
current capability and licensing against `references/sources.md`.

## Adoption considerations

Idea capture is an adoption tool as much as a pipeline. Visible responses build trust; silence destroys it. Credit
originators publicly where they agree, and work with `change-and-communications:success-stories` to tell the stories of
ideas that became real improvements.

## Knowledge considerations

Not applicable at capture. Where many ideas point to people being unable to find information, pass the pattern to the
knowledge manager as evidence of knowledge gaps.

## Security and privacy considerations

Submissions may contain personal or confidential information. Tell submitters not to include personal data about
customers or colleagues, restrict access to the capture record to the triage team, and agree retention with the data
protection officer.

## Responsible AI considerations

Some ideas will propose uses the principles exclude, such as monitoring individuals. Decline these at triage with a
respectful explanation that cites the principle, and record the pattern for the AI strategy lead.

## Evaluation requirements

Not applicable to solution testing. If an intake agent is used, it is evaluated like any agent before release through
`m365-agents:agent-testing` or the Copilot Studio testing route.

## Value measures

Measure ideas received by unit and channel, time to acknowledgement and triage, share reaching framing, and share later
delivered or routed to adoption. The intake owner reports these quarterly. Never count or rank ideas per individual.

## Scale notes

### Starter

One form, one triage owner meeting weekly for half an hour, and a monthly summary to the sponsor. Champions submit on
behalf of colleagues.

### Scale

Form plus a Teams community, Champions in every unit as feeders, a published triage service level and an occasional
campaign tied to an outcome.

### Enterprise

Business-unit spokes triage their own ideas on a shared form and record; the hub checks for duplicates across units
and runs enterprise campaigns. An intake agent may be justified at volume.

## Hand-offs

- To `opportunity-management:problem-framing` for ideas ready to frame.
- To `opportunity-management:backlog-management` to create and track the capture-stage entry.
- To `copilot-adoption:scenario-discovery` for ideas that existing tools already meet.
- To `change-and-communications:success-stories` for ideas that became visible improvements.

## Reviewer gates

Not applicable. Capturing an idea creates no solution and releases nothing. Ideas later pass the gates set by
`opportunity-management:risk-classification`.

## Failure modes

- The route launches without triage capacity, submissions go unanswered and contributions stop.
- The form asks for benefits, products and business cases, and only enthusiasts complete it.
- Frontline staff cannot reach the channel, so the backlog reflects only office-based work.
- Campaigns generate hundreds of ideas that delivery capacity cannot touch, and trust drops.
- Informal routes continue alongside the official one, and ideas are resourced without ever reaching the backlog.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Launch an idea route without named triage capacity and a service level.
- Leave a submitter without a response, including when the idea is declined.
- Rank or report individuals by the number or quality of ideas they submit.
- Ask submitters to name a product or estimate a benefit before the problem is framed.

---
name: audience-segmentation
description: Builds the adoption audience model for a Copilot programme by grouping the workforce on work pattern, Copilot access, device and shift constraints, information sensitivity and change impact, using aggregate HR and IT data, then sizing each audience and setting how it is reached, onboarded and supported. Use when one message is going to everyone, when waves need defining, or before personas and scenarios are chosen.
license: CC-BY-4.0
metadata:
  department: copilot-adoption
  lifecycle: Discover, Envision, Mobilise
  maturity: explorer, adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, copilot-cowork
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-overview
  status: draft
  authors: Simon Foote
---

# Audience segmentation

## Purpose

Adoption programmes that treat the workforce as one audience end up designing for the people nearest the programme
team: office-based, digitally confident and already curious. This skill builds an audience model that groups people by
how they work, what they can access, what constrains them and how much the change affects them, so waves, messages,
onboarding and support can be tailored to each group. It works from aggregate, declared organisational data, never from
individual behaviour or personal characteristics. It usually goes wrong when segments are copied from the org chart,
when frontline and part-time groups are added as an afterthought, or when personas become stereotypes nobody in the
business recognises.

## When to use

- A Copilot programme is about to plan waves and needs to know which groups exist and roughly how large they are.
- Communications and training are being written once for everyone, and some groups are plainly not being reached.
- Scenario discovery, onboarding or role journeys need an agreed list of audiences and personas to work from.
- A new business unit, region or acquired company is joining and its people need mapping onto the existing model.
- Leaders disagree about who should go first and need a shared picture of the workforce to decide.

## When not to use

- Finding and prioritising Copilot scenarios for each persona - use `copilot-adoption:scenario-discovery`.
- Sequencing waves, dates and exit criteria - use `copilot-adoption:launch-plan`.
- Designing the adoption journey for one priority role - use `copilot-adoption:role-based-adoption`.
- Mapping influential stakeholders and their concerns about AI - use `change-and-communications:ai-stakeholder-mapping`.
- Assessing how far each group's work and roles will change - use `change-and-communications:people-change-impact`.
- Deciding who should receive which licence - use `platform-governance:ai-licensing-and-capacity`, ending with the Microsoft licensing guide or a licensing partner.

## Questions to ask first

1. What workforce data may the programme use (role families, locations, work patterns, contract types), who owns it, and what have HR and the data protection lead agreed it can be used for?
2. Which Copilot experiences will each group actually have, on which devices, as confirmed by IT rather than assumed?
3. Where do groups differ in ways that change how they must be reached - shifts, shared devices, languages, regulated duties, accessibility needs?
4. Which groups face the greatest change impact or concern, and which already have a sponsor asking for help?
5. What minimum group size applies when audiences are targeted or reported?

## Required inputs

- Role families or job groupings with headcount, locations and work patterns, from HR at aggregate level.
- Access and device position by group, confirmed by IT (for example Copilot Chat only, Microsoft 365 Copilot, shared or personal devices).
- The readiness assessment from `copilot-adoption:adoption-readiness`, where one exists.
- Any change impact view from `change-and-communications:people-change-impact`.
- The agreed minimum reporting group size from `copilot-adoption:adoption-measurement`.

Where HR data is not available, draft a first model from business-unit leaders' descriptions and mark every size as
"to confirm". Never infer access or licence entitlement from job title; record what IT confirms and leave the rest open.

## Decision framework

Segment only on dimensions that change what the programme does. A dimension that changes no treatment is noise.

| Dimension | Typical values | What it changes |
|---|---|---|
| Work pattern | Desk, hybrid, field, frontline or shift-based | Format, length and timing of onboarding and support |
| Copilot access | Copilot Chat only, Microsoft 365 Copilot, agents in scope, no access yet | Which scenarios and guidance apply |
| Device and connectivity | Personal laptop, shared device, mobile only | How people reach learning and help |
| Information sensitivity | Routine, confidential, regulated or personal-data heavy | Emphasis of approved-use guidance and wave timing |
| Change impact | Low, medium, high | Depth of change support and manager involvement |
| Readiness signals | Sponsor in place, Champions present, permissions reviewed | Whether the group can go early |

Combine dimensions into a small number of audiences, usually four to eight for one organisation. Then test the model.

| Test | Passes when |
|---|---|
| Distinct | Each audience receives at least one treatment the others do not; otherwise merge |
| Recognisable | Business leaders can name the teams that belong to it |
| Sized | Headcount is known, or marked to confirm with an owner |
| Reachable | There is a channel and a manager route that reaches it |
| Safe to report | It is above the minimum group size, or is combined with another for reporting |

## Practitioner approach

Start with treatments, not data. Ask the adoption lead what the programme can actually vary between groups: message,
channel, onboarding format, session length, timing, support route, starting scenarios and wave. Those are the levers,
and the segmentation needs only the dimensions that pull them. Teams that start from an HR extract tend to produce
dozens of segments that nobody can act on.

Draft the first model with business-unit leaders and IT in the same conversation. Leaders know how work really happens,
and IT knows who has which access on which device. Walk through each part of the organisation and ask how these people
work, where they are when they could learn, and what would stop them using Copilot tomorrow. Write the answers in the
business's own words, then confirm sizes from HR's aggregate data rather than from memory.

Give frontline, shift-based, part-time and field audiences the same attention as office staff from the first draft.
They are the groups most often missed, and often the ones where a few well-chosen scenarios matter most. Flag audiences
that handle highly sensitive or regulated information, because approved-use guidance and permissions hygiene matter
most there and their wave may depend on remediation work.

Describe each audience as a short profile: who is in it (role families and locations, never named people), how they
work, what access and devices they have, the concerns likely to surface, the expected change impact, the channels and
manager routes that reach them, and what the programme will do differently for them. Where a persona helps people
imagine the audience, write it as a fictional composite and label it as such. Never build a persona from a real
colleague, and never segment on age, gender, health or other personal characteristics.

Test the model with the people who will use it. The launch planner should be able to sequence waves from it, scenario
discovery should be able to pick personas from it, the communications lead should be able to plan channels from it, and
the support lead should be able to see where demand will come from. If any of them cannot, the model is either too
coarse or too fine.

Keep it current. Reorganisations, new access decisions and acquisitions all change audiences. Give the model an owner,
a review point before each wave and a simple rule for where new joiners fall. Reporting by audience applies the minimum
group size; small audiences can be treated separately for onboarding but combined for reporting.

## Outputs

- An audience model recorded with the `adoption-plan` template, feeding its waves and personas columns: dimensions used, audiences, sizes, owners and open questions.
- An audience profile for each audience, with any persona labelled as a fictional composite.
- A treatment matrix showing, for each audience, channel, onboarding format, support route, starting-scenario source and wave readiness.
- A maintenance note naming the model owner, review points and the rule for placing new joiners.

## Microsoft platform considerations

Audiences often differ most in which Copilot experience they have: Copilot Chat, Copilot in the Microsoft 365 apps,
Copilot Cowork or agents, and on desktop, web or mobile. Record the access IT confirms for each audience and do not
infer it from role. Availability, naming and licensing change often; check `references/sources.md`, and send licensing
questions to the Microsoft licensing guide or a licensing partner.

## Adoption considerations

This skill is the foundation that other adoption work tailors from. Its most important contribution is making visible
the audiences a default plan would miss, so their needs shape the launch rather than being patched in afterwards.

## Knowledge considerations

Not applicable as a primary concern, because segmentation describes people and work patterns rather than grounding
content. Note where an audience relies heavily on particular policies or procedures, so knowledge readiness can be
prioritised for the waves that need it.

## Security and privacy considerations

Use aggregate HR data only, for the purpose agreed with HR and the data protection lead. Do not hold individual-level
lists in the audience model, and apply the minimum group size wherever audiences are reported. Flag audiences whose
work is sensitive so the approved-use guidance and permissions position can be checked before their wave. Data
protection questions end with the organisation's DPO.

## Responsible AI considerations

Segmentation decides who is offered what, so check it for unfair exclusion: part-time staff, frontline workers,
people using assistive technology and those working in another language should not be left without a route. Personas
must not stereotype. Where an audience is deferred, record why and when it will be revisited.

## Evaluation requirements

Not applicable as solution evaluation, because this skill designs an audience model rather than an AI solution. The
model is tested by whether the launch, scenario, communications and support owners can each act on it.

## Value measures

Owned by the adoption lead, with a baseline at the first wave: the share of the workforce covered by a defined audience
with a treatment, reach of onboarding by audience, and adoption indicators by audience from
`copilot-adoption:adoption-measurement`. Reported at audience level above the minimum group size, never by individual.

## Scale notes

### Starter

Three to five audiences drawn up in one workshop with business leaders and IT, sized from headcount by team and kept
on one page.

### Scale

Five to eight audiences with profiles and a treatment matrix, refreshed before each wave and shared with
communications, learning and support.

### Enterprise

A shared audience model across regions or divisions, with local variants for language and regulation, a named owner,
and alignment with HR's workforce taxonomy so reporting is consistent.

## Hand-offs

- To `copilot-adoption:scenario-discovery` to discover scenarios for each persona.
- To `copilot-adoption:launch-plan` to sequence audiences into waves.
- To `copilot-adoption:role-based-adoption` for priority roles that need their own journey.
- To `copilot-adoption:frontline-enablement` for frontline and deskless audiences.
- To `change-and-communications:ai-communication-strategy` for messages and channels by audience.

## Reviewer gates

Not applicable as a formal gate, because segmentation does not release an AI solution; use of workforce data follows
the organisation's existing data protection controls and the DPO's advice.

## Failure modes

- Segments are copied from the org chart, so audiences with very different work patterns receive identical treatment.
- Frontline and shift-based audiences are left to a later phase that never arrives.
- So many segments are created that nobody can plan from them, and the model is ignored.
- Access is assumed from job title, and onboarding teaches features an audience does not have.
- Personas drift into stereotypes, and the people they describe stop trusting the programme.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Segment people by age, gender, health or other personal characteristics.
- Build audiences from individual usage or behaviour data.
- Name individuals in an audience model or persona.
- Infer licence entitlement from role instead of confirming it with IT and the licensing route.

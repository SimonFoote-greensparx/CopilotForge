---
name: change-network
description: Builds and runs a change network of local change agents alongside Champions - agents carry messages into units, gather concerns and readiness signals and feed back, while Champions build capability - with coverage, manager-agreed time, a briefing and feedback cycle, boundaries and one coordinated ask of managers. Use when change lands unevenly across units, when feedback never reaches the programme, or when Champions are doing change work.
license: CC-BY-4.0
metadata:
  department: change-and-communications
  lifecycle: Mobilise, Enable, Launch, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2
  platforms: platform-neutral
  edition-support: scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-champion-programme, ms-champion-best-practice
  status: draft
  authors: Simon Foote
---

# Change network

## Purpose

A change network is a group of people in each business unit, site or function who carry the AI change locally: they
receive briefings before announcements, translate messages for their area, prepare local plans, gather concerns and
readiness signals, and feed them back to the programme. This skill designs and runs that network alongside the
Champions programme, so the two complement each other rather than compete. Champions build and share capability with
AI; change agents make the change land. Change networks usually go wrong when they are an email distribution list, when
they duplicate Champions and ask the same people for twice the time, or when feedback flows in but nothing visibly
changes.

## When to use

- AI changes are landing unevenly across business units, sites or regions, and the programme cannot see why.
- Feedback and concerns from the business are not reaching the programme until they become problems.
- Champions are being asked to run local communications, readiness and consultation work beyond their role.
- A large or multi-site organisation needs local translation of central messages.
- Several AI changes are running at once and units need a single local point of coordination.

## When not to use

- Designing the Champions programme, its journey and boundaries - use `champions:champion-programme-design`.
- Recruiting the Champion cohort - use `champions:champion-recruitment`.
- Fitting Champion roles into the Centre of Excellence - use `ai-centre-of-excellence:coe-champion-integration`.
- Setting formal decision rights and escalation for the programme - use `programme-management:stakeholder-governance`.
- Equipping line managers to lead their teams - use `change-and-communications:manager-enablement`.

## Questions to ask first

1. What will the network do that managers, Champions and central communications cannot do alone?
2. Which units, sites and functions need coverage, and how will the network reach frontline areas?
3. How much time can change agents give, and have their managers agreed it?
4. Is there a Champions programme, and who owns it, so the two can be designed together?
5. What will the programme do with the feedback the network gathers, and how quickly?

## Required inputs

- The stakeholder map from `change-and-communications:ai-stakeholder-mapping` and the impact assessment from `change-and-communications:people-change-impact`.
- The Champions programme charter from `champions:champion-programme-design`, where one exists.
- The communications plan and calendar from `change-and-communications:ai-communication-strategy`.
- Organisation structure at unit and site level, and HR policies on role time and recognition.

If there is no Champions programme, the network may initially cover both purposes, but record the roles separately so
they can split later. If manager agreement on time cannot be obtained, narrow the network rather than rely on goodwill.

## Decision framework

Separate the roles before recruiting anyone. Some people may hold both, but the work is different and the time agreed
must cover both.

| Role | Purpose | Does | Does not |
|---|---|---|---|
| Change lead (programme) | Owns the network and the change plan | Runs briefings, consolidates feedback, reports themes | Run local plans for every unit |
| Unit change lead | Accountable locally, usually a senior manager's delegate | Owns the local plan, chairs local check-ins, escalates | Act as HR or approve solutions |
| Change agent | Local carrier of the change | Translates messages, gathers concerns and readiness signals, supports managers | Provide technical support or teach AI skills |
| Champion | Local capability builder | Models practice, gives peer guidance, shares examples | Run communications or readiness assessments |

Set coverage by impact and structure.

| Situation | Coverage |
|---|---|
| Low-impact change, single site | No separate network; managers and Champions suffice |
| Medium impact, several units | One change agent per unit, unit change leads in larger units |
| High impact or multi-site and frontline | Change agents per site or shift pattern, unit change leads, regional coordination |

Run the network on a fixed cycle: briefing before each announcement, local translation and delivery, feedback within an
agreed period, consolidated themes to the programme, and a published response.

## Practitioner approach

Decide whether a network is needed at all. In a small organisation with good managers and an active Champion
community, a separate network adds overhead. Build one when units differ enough that central messages need local
translation, or when feedback is not reaching the programme.

Design it jointly with the Champions owner. Agree the role table, the time each role needs, and how a person holding
both roles is supported. Agree one calendar so that managers receive a single coordinated ask each month, not separate
requests from two networks. Share community spaces where it helps, but keep the purposes distinct: Champions talk about
practice; change agents talk about how the change is landing.

Recruit on declared interest, availability and local standing, with manager agreement before anyone joins. Aim for
coverage across units, sites, shift patterns and roles, including frontline areas. Do not use performance data in
selection and do not make the role an informal obligation for whoever is newest.

Run a briefing and feedback cycle. Before each significant announcement, brief change agents on what is coming, why,
the agreed answers and what is asked of them, early enough for them to prepare. After it, gather what people said and
asked, by theme and without names, within an agreed period. The change lead consolidates themes, takes them to the
programme and publishes a response: what changed, what was answered and what is still open. A network that never sees
its feedback acted on stops giving it.

Give change agents simple tools: a briefing pack per announcement, a local plan template, a short readiness check for
their area (awareness, manager briefing done, access, practice time, concerns open), a feedback form and a direct
route to the change lead. Hold a short network call on a regular rhythm, with an open slot for local issues.

Draw boundaries clearly. Change agents are not HR, not technical support, not trainers and not a monitoring channel.
They report themes, never individuals. Concerns about jobs, terms or consultation go to HR; technical problems go to
the service desk; capability questions go to Champions.

Keep the network healthy. Review membership, coverage and time every six months with unit change leads, thank and
recognise contributions publicly, and let people step down without stigma. Close the network deliberately when the
change programme ends, or hand it to the CoE if ongoing AI change justifies it.

## Outputs

- A change network charter: purpose, role table, coverage, time agreed, cycle, tools, boundaries, relationship with Champions, review and closure.
- A network roster by role and unit, held with restricted access.
- A briefing pack template, local plan template, local readiness check and feedback form.
- A monthly themes and responses summary for the sponsor and the programme, recorded in the listening section of the `ai-communications-plan`.

## Microsoft platform considerations

Not applicable to the network's design, which holds whatever Microsoft AI experiences are being introduced. Networks
typically use the organisation's existing collaboration tools for their space and feedback forms. Any product facts in
briefing packs are checked against `references/sources.md` before release.

## Adoption considerations

The network's readiness checks inform the timing of waves in `copilot-adoption:launch-plan`. Readiness signals are
reported at unit level and used to adjust support, not to rank units.

## Knowledge considerations

Briefing packs and agreed answers are knowledge assets with owners and review dates. Change agents often learn first
where local knowledge is outdated; give them a route to content owners.

## Security and privacy considerations

Feedback is gathered and reported by theme, without attribution to individuals. The roster holds personal data, so
restrict access and set retention. Change agents repeat the approved-use guidance and the route for reporting suspected
data exposure.

## Responsible AI considerations

Change agents often hear concerns about fairness and ethics first. Give them a clear route to pass those to the
`responsible-ai` department through the change lead, and make sure such concerns are never filtered out as negativity.

## Evaluation requirements

Not applicable as solution evaluation. The network's cycle is checked by feedback turnaround, themes acted on and unit
coverage at each six-monthly review.

## Value measures

Owned by the change lead: unit coverage, share of announcements preceded by a network briefing, time from feedback to
published response, and unit-level readiness at wave start. Reported for units above the minimum group size, never as
ratings of individual change agents.

## Scale notes

### Starter

Usually not needed; managers and Champions carry the change. Where units differ, name one contact per unit with a light
briefing cycle.

### Scale

A network with change agents per unit and unit change leads, a monthly call, a shared calendar with Champions and a
published themes summary.

### Enterprise

Regional networks with coordinators on a shared charter, translated briefing packs, alignment with other major change
programmes and a joint health review with the Champions programme.

## Hand-offs

- To `champions:champion-programme-design` to align roles, calendars and community with the Champions programme.
- To `change-and-communications:resistance-management` with hardened concern themes.
- To `copilot-adoption:launch-plan` with unit readiness signals.
- To `change-and-communications:ai-communication-strategy` to update messages from feedback.

## Reviewer gates

Not applicable, because the network supports change rather than releasing solutions. Concerns it surfaces about
solutions at tier 2 or above go to those solutions' reviewers.

## Failure modes

- The network duplicates Champions, managers get two sets of requests, and both networks lose goodwill.
- Change agents are briefed after announcements and simply forward emails.
- Feedback flows in but is never answered, and the network falls silent.
- Change agents are drawn into reporting on individuals and trust collapses.
- The network depends on volunteers with no agreed time and fades within a quarter.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Use change agents to report on, rank or monitor named individuals.
- Recruit change agents without their manager's agreement on time.
- Merge Champion and change agent roles silently so one person carries both without the time to do so.
- Collect feedback without committing to publish a response.

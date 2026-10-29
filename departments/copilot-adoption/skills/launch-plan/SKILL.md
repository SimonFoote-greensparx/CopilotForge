---
name: launch-plan
description: Plans a phased Copilot launch with onboarding by persona, executive and manager enablement, reinforcement through office hours and Champions, a support model and a feedback loop that keeps improving the programme. Use when readiness gaps are known and a rollout needs sequencing, when a big-bang launch is being proposed, or when a launch happened but nothing followed it.
license: CC-BY-4.0
metadata:
  department: copilot-adoption
  lifecycle: Mobilise, Enable, Launch
  maturity: explorer, adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, copilot-cowork
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-champion-programme, ms-copilot-overview
  status: draft
  authors: Simon Foote
---

# Launch plan

## Purpose

This skill turns readiness findings and priority scenarios into a phased launch that people experience as help with
their work rather than a product announcement. It sequences waves, prepares executives and managers to lead by example,
plans onboarding by persona, and sets up the reinforcement, support and feedback that sustain use after launch week.
Launches usually fail because all the effort goes into the first day and nothing is planned for weeks two to twelve,
which is when habits form or fade.

## When to use

- Readiness has been assessed and the sponsor wants a rollout plan with dates.
- Someone proposes giving everyone access on the same day and the risks need laying out.
- A launch has already happened, usage has faded, and reinforcement was never planned.
- A new wave or business unit is joining and needs onboarding tailored to its personas.
- A Champions programme exists or is planned, and the launch should share its learning sessions and community rather than run in parallel.

## When not to use

- Assessing whether the organisation is ready to launch at all - use `copilot-adoption:adoption-readiness`.
- Finding and prioritising the scenarios each persona will be onboarded with - use `copilot-adoption:scenario-discovery`.
- Defining adoption measures, baselines and reporting rules - use `copilot-adoption:adoption-measurement`.
- Designing the Champions programme that supports the launch - use `champions:champion-programme-design`.
- Detailed communications campaigns and manager change toolkits - use `change-and-communications:adoption-campaign-plan` and `change-and-communications:manager-enablement`.
- Formal curricula and learning pathways - use `learning-and-skills:ai-role-curriculum`.

## Questions to ask first

1. What do the readiness assessment and its blocking gaps say about which audiences can go first?
2. Which personas and starting scenarios are ready, and who owns each?
3. Will executives and managers use Copilot visibly themselves before their teams are asked to?
4. What support capacity exists for the first six weeks, and who answers questions that are not faults?
5. How will feedback from users reach someone who can change the guidance, scenarios or plan?

## Required inputs

- The readiness assessment and gap list from `copilot-adoption:adoption-readiness`.
- The scenario catalogue and starting scenarios from `copilot-adoption:scenario-discovery`.
- The approved-use guidance and the support route agreed with IT.
- The Champions network, if one exists, with agreed time commitments.
- Constraints on timing: busy periods, other change programmes, licence availability confirmed by the owner.

If the scenario catalogue does not exist, do not plan onboarding around features; schedule discovery first. If no
support route exists, the launch is blocked until one does.

## Decision framework

Choose the launch shape from the readiness position and the support capacity available.

| Situation | Launch shape |
|---|---|
| Critical readiness gaps open for some audiences | Launch only to audiences where all critical areas are Ready or mitigated |
| Limited support capacity or few Champions | Small waves of a few teams, each with dedicated office hours |
| Strong readiness, established Champions, clear scenarios | Larger waves by business unit, each with a manager briefing first |
| Frontline populations | Separate wave with device, shift and language needs planned explicitly |

Each wave moves forward only when the previous wave meets its exit criteria: support demand is manageable, no open
data exposure incidents, and feedback has been reviewed and acted on.

Be clear which layer of the operating model the launch is. This skill plans the foundation layer; the other two
layers are designed elsewhere, and the launch should connect to them, not absorb them.

| Layer | What it provides | Designed in |
|---|---|---|
| Foundation adoption programme | Broad access, onboarding, approved-use guidance, support and safe everyday use for everyone | This skill and `copilot-adoption:adoption-readiness` |
| Champions programme | Local peer support, role-based practice and a network of verified, capable colleagues | `champions:champion-programme-design` |
| Centre of Excellence | Prioritisation, governance and delivery of larger or higher-risk solutions | `ai-centre-of-excellence:coe-operating-model` |

## Practitioner approach

Start at the top. Executives set the tone, so plan executive enablement first: a short, private session on the
scenarios relevant to their own work, followed by the ask that they use Copilot visibly and talk about it. An executive
who mentions in a town hall how they prepared for a meeting does more for adoption than any poster. Keep the session
practical and avoid turning it into a product briefing.

Managers come next and matter most. People take their cue from their manager about whether experimenting is welcome and
whether time spent learning is legitimate. Give managers a short briefing before their team's wave: why the
organisation is doing this, the starting scenarios for their team, the approved-use guidance, where support sits and
how to talk about Copilot in team meetings. Ask them to protect a small amount of practice time.

Then plan onboarding by persona. Each persona's first session should cover the purpose, the approved-use guidance in
plain words, three to five starting scenarios done live on realistic material, and the verification habit. Desk
workers can usually take a short live session plus self-paced material. Frontline workers need shorter formats that fit
shifts and the devices they actually use. Record every session so latecomers and new joiners are not left behind.

Reinforcement is where launches are won or lost. Schedule office hours in the weeks after each wave, ideally run by
Champions alongside the adoption team, and refresh the scenario set every few weeks with something new. Encourage teams
to share what worked in their regular meetings. Plan a check-in at around six weeks to see which scenarios stuck and
which did not.

Turn one-off sessions into a recurring learning calendar: getting started and approved use, Copilot Chat, Copilot in
the Microsoft 365 apps, collaboration in Teams and, where relevant, agent awareness. Keep every session open to the
whole workforce and recorded. Where a Champions programme exists, agree which sessions count towards its journey, so
the same investment serves foundation adoption and builds the local network. Launch the Champions community before the
first wave, so each team has someone to turn to when the trainers leave.

Make the support model explicit. "How do I" questions go to Champions, office hours and the scenario catalogue. Faults
go to the IT service desk. Suspected data exposure goes immediately to the route agreed with `security-privacy`. Ideas
that need more than individual use, or carry higher risk, go to opportunity intake and the Centre of Excellence.
Champions are first-line peer guidance, not the help desk, formal training or an approval route.

Close the loop. Collect feedback through a simple channel, review it weekly during each wave, and publish what changed
as a result. People keep giving feedback only when they see it used.

## Outputs

- A launch and onboarding plan in the launch section of the `adoption-plan` template: waves, audiences, dates, exit criteria and owners.
- An executive and manager enablement plan with session outlines.
- A reinforcement calendar of office hours, scenario refreshes and check-ins.
- A recurring learning calendar open to the whole workforce, showing which sessions count towards the Champion journey.
- A support model showing where each type of question goes.
- A feedback loop description: channel, review rhythm, owner and how changes are published.

## Microsoft platform considerations

Onboarding must match the Copilot experiences each persona actually has, which can differ between Copilot Chat,
Copilot in the Microsoft 365 apps and Copilot Cowork, and between desktop and mobile. Confirm with IT before each wave,
and check `references/sources.md` for current capability and naming rather than relying on last quarter's training
material.

## Adoption considerations

This skill is an adoption plan, so the whole method applies. Watch especially for waves that launch without manager
briefings and for reinforcement that stops after the first month. Celebrate team stories, not individual usage counts.

## Knowledge considerations

Onboarding exposes weak knowledge quickly, because the first thing people ask Copilot about is their own policies and
procedures. Log where answers were poor because content was stale or missing, and pass it to
`knowledge-management:knowledge-gap-analysis`.

## Security and privacy considerations

Every onboarding session repeats the approved-use guidance and shows how to report suspected data exposure. Do not
start a wave while a data exposure incident from a previous wave is unresolved.

## Responsible AI considerations

Onboarding teaches verification as a habit and makes clear that people remain accountable for output they use. Remind
managers that Copilot use must not become a factor in individual performance judgements.

## Evaluation requirements

Not applicable as solution evaluation, because this skill plans a rollout rather than building an AI solution. Each
wave is evaluated against its exit criteria before the next begins.

## Value measures

Wave-level measures, owned by the adoption lead: proportion of the wave's licensed population active after six weeks,
scenarios reported as used, support demand by type and feedback themes. Measures come from
`copilot-adoption:adoption-measurement` and are reported at team or role level only.

## Scale notes

### Starter

One wave, one manager briefing, one onboarding session per persona and weekly office hours for a month, run by the
owner or an adoption-minded colleague with a partner's help if needed.

### Scale

Several waves by business unit, a Champion in each team, a shared reinforcement calendar and a standing feedback review.

### Enterprise

A programme with regional or divisional waves, localised materials, executive sponsorship at each level and a central
adoption team coordinating Champions, support and change networks. Align waves with other major change programmes.

## Hand-offs

- To `copilot-adoption:adoption-measurement` to track each wave against its baseline.
- To `champions:champion-programme-design` when the launch needs a Champion network that does not yet exist.
- To `champions:capability-framework` to map recurring learning sessions to the Champion capabilities.
- To `champions:recognition-and-progression` to connect launch participation to the Champion journey.
- To `opportunity-management:problem-framing` for ideas from users that need more than individual use.

## Reviewer gates

Not applicable as a formal gate, because a launch of approved Copilot experiences at tiers 0 and 1 relies on the
readiness assessment, where `security-privacy` has already reviewed data and permissions hygiene.

## Failure modes

- All effort goes into launch day, reinforcement is never scheduled, and usage fades within weeks.
- Managers are not briefed, so teams assume experimenting is not a legitimate use of time.
- Champions become the de facto help desk because the support model was never made explicit.
- Learning sessions run as a one-off launch event, so new joiners and later waves have nothing to attend.
- Frontline workers are onboarded with desk-based sessions that do not fit their shifts or devices.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Launch to an audience with an open critical readiness gap and no mitigation.
- Use Champions as an unpaid help desk or approval route.
- Plan onboarding around a feature list instead of the persona's scenarios.
- Encourage managers to use Copilot usage as an individual performance measure.

---
name: champion-learning
description: Designs the learning offer behind the Champion journey - training-route sessions and guided exercises for each capability, exemplars and clinics for the evidence route, Challenge preparation, refreshers when Copilot changes and advanced learning for recognised Champions - shared with the workforce where possible. Use when capabilities need a training route, when sessions feel too basic, or when material is stale.
license: CC-BY-4.0
metadata:
  department: champions
  lifecycle: Enable, Scale, Improve
  maturity: explorer, adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, copilot-cowork, m365-agents
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-champion-best-practice, ms-champion-programme, ms-copilot-adoption-hub, ms-agent-builder
  status: draft
  authors: Simon Foote
---

# Champion learning

## Purpose

The capability framework says what a Champion must be able to show; this skill designs the learning that helps them
get there and keeps them current afterwards. It builds the training route for each capability, supports people taking
the evidence route, prepares Champions for their Challenge, refreshes practice when Copilot changes and offers
advanced learning to recognised Champions. It usually goes wrong when learning becomes the gate rather than one route,
when sessions are pitched at beginners and lose experienced people, when material describes last quarter's product, or
when Champion learning is run as a closed club that duplicates the workforce learning calendar.

## When to use

- The capability framework is agreed and each capability needs a training route people can actually take.
- Experienced Champions find sessions too basic, or newer ones find them too fast.
- People choosing the evidence route ask what good evidence looks like and get no help.
- Copilot has changed and the Champion material no longer matches what people see.
- Recognised Champions ask for something deeper, and the programme has nothing to offer them.

## When not to use

- Defining the capabilities, routes and verification criteria themselves - use `champions:capability-framework`.
- Designing progressive learning pathways for the whole workforce - use `learning-and-skills:ai-learning-pathway`.
- Advanced pathways for makers and specialists beyond the Champion programme - use `learning-and-skills:advanced-pathways`.
- Building safe practice environments and sandboxes - use `learning-and-skills:practice-labs`.
- Writing detailed facilitator guides for individual sessions - use `learning-and-skills:facilitator-guide`.
- Community rituals such as calls and prompt clinics - use `champions:champion-community-design`.

## Questions to ask first

1. What do the capability framework's objectives and verification criteria require, capability by capability?
2. What learning does the workforce calendar already offer, and which sessions could count towards the journey?
3. Who will deliver Champion learning - the learning team, the adoption team, recognised Champions, a partner - and with what time?
4. Is there a safe practice environment, and is agent building approved for Champions at all?
5. How will material be kept current when Copilot changes?

## Required inputs

- The capability framework, with objectives, training and evidence options and verification criteria, from `champions:capability-framework`.
- The workforce learning calendar from `copilot-adoption:launch-plan` or `learning-and-skills:ai-learning-pathway`.
- The Challenge options and criteria from `champions:champion-challenges`.
- The organisation's position on agent building for Champions, and any practice environment from `learning-and-skills:practice-labs`.
- Delivery capacity: who can teach, how often, and in which formats.

If agent building is not approved for Champions, design the agent capability learning around understanding and judging
use cases, and record the configuration element as deferred. If no safe practice environment exists, use fictional
material on approved tools and record the gap.

## Decision framework

Map learning components to the journey. Each training route ends in the same evidence the evidence route requires.

| Journey stage | Training route | Evidence route support | Delivered by |
|---|---|---|---|
| Verify Chat capability | Session on prompting, refinement, context and verification; guided exercise on own work | Exemplars of strong and weak evidence; evidence clinic | Learning or adoption team |
| Verify productivity capability | Sessions on Copilot across the Microsoft 365 apps; guided exercise producing a checked output | Exemplars; clinic | Learning team with recognised Champions |
| Verify agent capability | Session on agents, use-case judgement and governance; guided build where approved | Exemplars of use-case judgements; clinic | Adoption team or CoE with approved makers |
| Prepare a Challenge | Workshop on scoping, safety checks and reusable outputs | Mentoring by a recognised Champion | Programme owner and mentors |
| Recognised Champion | Advanced sessions, early sight of new capabilities, specialist pathways | Not applicable | CoE, learning team, partner |
| Everyone, ongoing | Product change refreshers | Not applicable | Adoption lead |

Decide what is open and what is Champion-only.

| Learning | Open to the workforce? |
|---|---|
| Foundation sessions on Copilot Chat and the Microsoft 365 apps | Yes, and they count towards the journey |
| Guided exercises, exemplars and evidence clinics | Champions, with materials published for anyone |
| Challenge preparation and mentoring | Champions |
| Advanced sessions and pilots | Recognised Champions, with selection criteria published |

## Practitioner approach

Start from the verification criteria and work backwards. For each capability, ask what someone must be able to do to
produce evidence that meets the criteria, and design the shortest learning that gets them there. If a session does not
help people meet a criterion, it belongs in the wider workforce calendar, not the Champion route.

Keep training one route, not the gate. Experienced colleagues should be able to skip straight to evidence. Support
them with exemplars of strong and weak evidence, written with fictional material, and short evidence clinics where they
can test a draft submission. This respects their time and raises the quality of submissions, which helps assessors.

Make every training route practical. Each capability's training ends with a guided exercise on the participant's own
work, producing the evidence the criteria ask for. People learn to verify Copilot output by verifying it, not by
hearing about it. Use realistic fictional material in group sessions and remind people never to bring personal or
confidential data into shared exercises.

Share foundation learning with the whole workforce. Sessions on Copilot Chat and the Microsoft 365 apps should be open
to everyone and recorded, with attendance counting towards the Champion journey. This keeps the programme from becoming
a closed club and means the same investment serves both foundation adoption and the network.

Treat agent capability carefully. Learning covers what agents are, how to judge a good use case, ownership and
governance, and testing basics. Where the organisation approves Champions to build, add a guided build in an approved
environment, using Agent Builder or the tool governance allows. Where it does not, the capability is about judgement
and routing, and the learning says so honestly.

Prepare people for the Challenge. A short scoping workshop on picking a real team problem, checking safety and scope,
and leaving something reusable, followed by mentoring from a recognised Champion, does more than any further session.

Keep material current. Copilot changes often, so give each module an owner and a review point, and run a short
refresher whenever a change alters what people see or what the guidance says. Check current product behaviour against
the source records rather than relying on last quarter's slides.

Finally, give recognised Champions somewhere to grow: advanced sessions, early sight of new capabilities in governed
pilots and routes into specialist pathways, each with an owner who has agreed to run it.

## Outputs

- A Champion learning map showing, for each journey stage, the training route, evidence-route support, delivery owner and rhythm, recorded with the `champion-capability-framework` template.
- Guided exercises and exemplars for each capability, using fictional material.
- A learning calendar marking which workforce sessions count towards the journey, aligned with the `adoption-plan` learning calendar.
- A content maintenance plan with module owners and review points.

## Microsoft platform considerations

Learning must reflect the Copilot experiences Champions actually have: Copilot Chat, Copilot in the Microsoft 365 apps,
Copilot Cowork and, where approved, agent building in Agent Builder or Copilot Studio. Capabilities, naming and
availability change, so check `references/sources.md` before each refresh and point Champions to Microsoft's current
learning resources rather than reproducing them.

## Adoption considerations

Champion learning is part of the adoption system. Opening foundation sessions to the workforce and aligning refreshers
with the reinforcement cycle means Champions arrive at their teams with the same current guidance the programme is
promoting.

## Knowledge considerations

Learning materials, exemplars and recordings are knowledge assets: give each an owner, a version and a review date,
and retire superseded material so Champions do not learn outdated practice.

## Security and privacy considerations

Exercises use fictional or approved material. Participants are reminded not to bring personal or confidential data
into group sessions or evidence. Agent building happens only in approved environments with the organisation's controls.
Recordings follow the organisation's retention rules.

## Responsible AI considerations

Every module teaches verification, accountability and the limits of AI output, and the agent capability covers when
an agent should not be built. Learning never rewards volume of use.

## Evaluation requirements

Not applicable as solution evaluation, because this skill designs learning rather than an AI solution. Learning is
reviewed by whether participants on the training route go on to meet the verification criteria, at programme level.

## Value measures

Owned by the Champions programme owner with the learning lead, with baselines from the first cohort: progression from
training route to verified capability, evidence first-time pass rates at programme level, time to complete each stage,
and attendance from the wider workforce at open sessions. Reported at programme level, never as individual rankings.

## Scale notes

### Starter

Foundation sessions shared with the workforce, one guided exercise and exemplar per capability, and a refresher when
Copilot changes, delivered by the programme owner or a partner.

### Scale

A full learning map with evidence clinics, Challenge workshops, mentoring and module owners, delivered with the
learning team and recognised Champions.

### Enterprise

A learning offer shared across regions with localised delivery, advanced sessions and pilots through the CoE, and
specialist pathways connected to `learning-and-skills:advanced-pathways`.

## Hand-offs

- To `champions:capability-framework` when learning shows the criteria are unclear or unrealistic.
- To `learning-and-skills:facilitator-guide` to write guides for each session.
- To `learning-and-skills:practice-labs` where a safe practice environment is needed.
- To `champions:recognition-and-progression` for advanced access and specialist pathways.

## Reviewer gates

Not applicable as a formal gate, because learning design does not release an AI solution. Guided agent builds use only
environments and tools already approved under the organisation's governance.

## Failure modes

- Training becomes the gate, and experienced colleagues leave rather than sit through beginner sessions.
- Sessions describe features rather than producing evidence, so participants cannot meet the criteria afterwards.
- Material lags behind product change, and Champions teach outdated practice.
- Champion learning duplicates the workforce calendar and becomes a closed club.
- Agent capability promises building that governance does not allow.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Make training the only route to verified capability.
- Use personal or confidential data in group exercises or exemplars.
- Teach agent building in environments the organisation has not approved.
- Measure learning by attendance alone or rank participants.

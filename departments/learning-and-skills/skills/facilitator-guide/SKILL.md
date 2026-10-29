---
name: facilitator-guide
description: Writes facilitator guides for AI learning sessions - outcomes, a timed running order, live demonstrations with a fallback when Copilot answers differently, protected hands-on practice, fictional materials, likely questions with safe answers, accessibility and an evidence step - so any prepared facilitator can run the session well. Use when a session depends on one presenter, when demos fail live, or before handing delivery to Champions.
license: CC-BY-4.0
metadata:
  department: learning-and-skills
  lifecycle: Enable, Launch, Improve
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-studio
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-overview, ms-copilot-privacy, ms-champion-best-practice
  status: draft
  authors: Simon Foote
---

# Facilitator guide

## Purpose

An AI learning session lives or dies on the person running it, and most sessions are built around one presenter's
knowledge and laptop. This skill writes facilitator guides that let any prepared facilitator run a session to the same
standard: what learners will be able to do, the running order, what to demonstrate and what to do when the
demonstration goes differently, how practice is run and how it turns into evidence. It usually goes wrong when the
guide is a slide deck with speaker notes, when live demos assume Copilot will give the same answer twice, and when
sessions run out of time before anyone practises.

## When to use

- A session is about to be delivered by someone other than its author, such as Champions, team leads or a partner.
- Live demonstrations keep failing or producing surprising answers in front of learners.
- Sessions consistently overrun and the practice section is the part that gets cut.
- The same session is delivered differently by different people and learners notice.
- A product change means existing sessions show screens or behaviour learners no longer see.

## When not to use

- Deciding which modules a role needs and in what order - use `learning-and-skills:ai-role-curriculum`.
- Building the practice environment and scenario packs a session uses - use `learning-and-skills:practice-labs`.
- Running ongoing drop-in clinics rather than structured sessions - use `learning-and-skills:office-hours`.
- Designing the Champion learning offer as a whole - use `champions:champion-learning`.
- Writing prompting guidance and verification checklists as reference material - use `m365-copilot:prompting-practice`.

## Questions to ask first

1. Which module and outcomes is this session for, which pathway level, and what evidence should learners leave with?
2. Who will facilitate - learning professionals, Champions, team leads, a partner - and how familiar are they with the tools?
3. Is the session live in a room, online, recorded, or a short huddle, and how long is it really?
4. Which approved tools and fictional materials will learners use, and have they been tested against the current product?
5. Which learners need adjustments for accessibility, language or working pattern?

## Required inputs

- The module specification from `learning-and-skills:ai-role-curriculum`, with outcomes, practice task and evidence.
- Lab exercises and fictional scenario packs from `learning-and-skills:practice-labs`.
- The evidence rubric for the level, from `learning-and-skills:learning-evidence-rubric`.
- The organisation's approved-use guidance and the route for reporting concerns.
- Confirmation of which tools and agents learners will have during the session.

If the module specification is missing, do not write a guide; a guide without outcomes becomes a product tour. If
learners' access is unconfirmed, design the practice around tools they definitely have and mark the rest as
demonstration only.

## Decision framework

Allocate time so practice is protected.

| Session part | Share of time | Rule |
|---|---|---|
| Opening - outcomes, safe use reminder, why this matters for the role | Short | No product content before people know what they will be able to do |
| Demonstration | Short | One scenario end to end, including the check step |
| Guided practice | The largest part | Learners do the task themselves on own work or the scenario pack |
| Evidence and reflection | Protected | Learners capture evidence against the rubric before leaving |
| Close - where to get help, next step on the pathway | Short | Point to office hours and the next module |

Choose the demonstration approach by risk of variance.

| Situation | Approach |
|---|---|
| Stable, simple scenario | Live demonstration with a tested prompt and a screenshot fallback |
| Output varies widely between runs | Run it live, then compare two outputs and use the differences to teach verification |
| Feature unreliable or recently changed | Recorded or screenshot walk-through, labelled as such, then live practice |
| Facilitator new to the tool | Pair with an experienced co-facilitator for the first two deliveries |

## Practitioner approach

Write the guide for the facilitator who did not design the session. Start with a one-paragraph brief: who the learners
are, what they will be able to do afterwards, what evidence they will leave with, and the one message that matters most.
Then the running order, with timings, what the facilitator says in their own words, what learners do, and what to have
ready on screen.

Treat variability as a teaching opportunity, not a risk to hide. Copilot will not give identical answers each time, and
the most useful moment in many sessions is when it gives a weak or wrong one. Script the demonstration around that:
run the prompt, ask learners what they would check, compare against the source, refine the prompt. The guide should
include the tested prompt, what a good answer looks like, the errors to look for and a fallback screenshot in case the
service is slow or the feature has changed.

Protect practice time. Put the guided practice in the middle and mark it as the part that is never cut; if the session
runs late, shorten the demonstration or the close. Give the facilitator clear instructions for practice: what learners
choose from their own work, what to avoid, and how to use the fictional scenario pack instead. Include prompts for the
facilitator to circulate and ask "how did you check that?".

Build safe use into the flow. Remind learners at the start not to put sensitive data on shared screens or in chat, and
make sure the facilitator demonstrates from a clean account with fictional content - never their own mailbox or real
client files. Include a short script for when a learner shares something sensitive by accident: stop sharing, do not
draw attention to the person, and follow the reporting route if needed.

Anticipate questions. List the questions facilitators usually get - about privacy, whether Copilot learns from their
data, licensing, jobs, accuracy - with short, safe answers that point to the approved-use guidance and the right owner.
Facilitators should never improvise answers on licensing or data protection.

Close every session with evidence and a next step. Learners capture their evidence against the rubric before leaving,
and the facilitator points to office hours, the next module and where to get help.

Finally, add a pre-flight checklist: test every prompt and exercise against the current product the day before, check
access for the cohort, prepare the fallback, and confirm accessibility needs. After each delivery, the facilitator
records what changed or failed so the content owner can update the guide.

## Outputs

- A facilitator guide per session, recorded against the sessions section of the `ai-learning-plan` template - brief, outcomes, running order with timings, demonstration script with fallback, practice instructions, evidence step and close.
- A likely-questions sheet with safe answers and routing.
- A pre-flight checklist and a post-session feedback note for the content owner.
- Learner handouts using fictional material, labelled as fictional.

## Microsoft platform considerations

Guides show the Copilot experiences learners will actually have, such as Copilot Chat, Copilot in the Microsoft 365
apps, approved agents or Copilot Cowork. Screens, names and behaviour change often, so the pre-flight check tests every
step against the current product and `references/sources.md`. Facilitators demonstrate from an account set up for
training with fictional content, never from a personal account with real work in it.

## Adoption considerations

A good session leaves people wanting to try something tomorrow. End with one concrete task for the coming week, link it
to the role's adoption journey, and let managers know what their team learnt so they can follow up.

## Knowledge considerations

Guides, prompts and fallbacks are knowledge assets with an owner, a version and a review date. Facilitator feedback
after each delivery is the main signal that a guide needs updating.

## Security and privacy considerations

Demonstrations use fictional content on training accounts. Learners are reminded not to share sensitive information on
screen or in chat. Recordings follow the organisation's retention rules and are checked for sensitive content before
publication. Questions about data handling are routed to the approved-use guidance and, where needed, the DPO.

## Responsible AI considerations

Every session demonstrates a check step and at least one case where AI gets it wrong. Facilitators are briefed to
discuss concerns about jobs, fairness and accuracy honestly and to route questions they cannot answer.

## Evaluation requirements

Not applicable as AI evaluation, because a session does not release an AI solution. Each guide is checked by whether
learners leave with evidence that meets the rubric and by facilitator and learner feedback.

## Value measures

Baseline: the share of sessions currently ending with learner evidence. Measures: share of sessions with a current guide,
evidence produced per session at cohort level, and consistency of results across facilitators. Owned by the Learning
Lead, reported at session and role level, never as facilitator or learner rankings.

## Scale notes

### Starter

A short guide per session with timings, a tested demonstration and fallback, and a practice task, used by the two or
three people who deliver.

### Scale

Standard guide format across all sessions, a likely-questions sheet, pre-flight checks before each cohort and a
co-facilitation route for new facilitators such as Champions.

### Enterprise

A guide library with version control, localised variants, facilitator preparation and calibration, and a feedback
route from every delivery to content owners.

## Hand-offs

- To `learning-and-skills:practice-labs` when a session needs new exercises or a scenario pack.
- To `learning-and-skills:office-hours` for follow-up after the session.
- To `learning-and-skills:ai-role-curriculum` when delivery shows the module needs reshaping.
- To `champions:champion-learning` where Champions will deliver the session.

## Reviewer gates

Not applicable, because a facilitator guide does not release an AI solution. Sessions that demonstrate a new agent or
Cowork task run only after that solution has passed its own release gates.

## Failure modes

- Demonstrations depend on Copilot giving the same answer twice, and fail in front of the room.
- Practice is cut when sessions overrun, so learners leave without trying anything.
- Facilitators demonstrate from their own mailbox and expose real content.
- Facilitators improvise answers on licensing or data protection and give wrong assurances.
- Guides are not updated after product changes, and screens no longer match what learners see.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Demonstrate with real personal, client or confidential content.
- Cut guided practice to fit in more product content.
- Give licensing or data protection assurances not grounded in the approved guidance or the right owner.
- Use session participation to rate or rank learners or facilitators.

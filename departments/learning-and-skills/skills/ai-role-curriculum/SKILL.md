---
name: ai-role-curriculum
description: Builds a role-based AI curriculum for one priority role at a time from its skills needs statement - outcomes tied to the role's real scenarios, modules in sequence, formats that fit how the role works, practice on its own work, the evidence each outcome needs, agreed time and owners. Use when a role's needs are agreed and its learning must be designed, when generic courses are not changing work, or when a new role joins a wave.
license: CC-BY-4.0
metadata:
  department: learning-and-skills
  lifecycle: Mobilise, Enable, Improve
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-studio
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-overview, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# AI role curriculum

## Purpose

A curriculum turns a role's needs statement into learning that changes what people in that role actually do with
Microsoft AI. This skill designs, for one priority role at a time, the learning outcomes, modules, sequence, formats,
practice and evidence, sized to the time the role can realistically give. It usually goes wrong when the curriculum is
a tour of product features rather than the role's own scenarios, when it is sized for an ideal week rather than a real
one, and when finishing the course is counted as being able to do the work.

## When to use

- A role-level needs statement is agreed and the role now needs its learning designed.
- Training has been bought or delivered generically and the role's use of Copilot remains shallow.
- A new role joins a rollout wave and the existing curricula were written for someone else.
- A role's scenarios, agents or Copilot Cowork tasks have changed enough that its learning is out of date.
- A business owner asks what their team will learn, how long it will take and how anyone will know it worked.

## When not to use

- Working out what each role needs in the first place - use `learning-and-skills:ai-skills-needs-analysis`.
- Defining the shared foundation-to-advanced levels every curriculum plugs into - use `learning-and-skills:ai-learning-pathway`.
- Learning for makers, power users and specialists who build - use `learning-and-skills:advanced-pathways`.
- Designing the role's adoption journey, team routines and manager expectations - use `copilot-adoption:role-based-adoption`.
- Writing app-by-app scenarios with prompt patterns and verification steps - use `m365-copilot:copilot-role-scenarios`.
- Learning that supports the Champion journey - use `champions:champion-learning`.

## Questions to ask first

1. Which role is this for, roughly how many people does it cover, and which business owner will confirm the curriculum fits their team?
2. What does the role's needs statement say - the future work, the gaps by skill area, their ratings and the agreed response type?
3. How much time a month can people in the role give to learning and practice, agreed with the business owner, and in what working pattern?
4. Which tools and agents does the role have confirmed access to, and is a safe practice environment available?
5. What existing learning can be reused, and who will deliver and maintain this curriculum once it is live?

## Required inputs

- The role's needs statement and its prioritised role-and-skill pairs from `learning-and-skills:ai-skills-needs-analysis`.
- The role's scenarios from `copilot-adoption:scenario-discovery`, and app-level scenarios from `m365-copilot:copilot-role-scenarios` where they exist.
- The pathway levels and their exit evidence from `learning-and-skills:ai-learning-pathway`, and the rubric from `learning-and-skills:learning-evidence-rubric`.
- Confirmed access to tools and agents for the role, from the rollout plan.
- The learning time agreed with the business owner, and the current learning catalogue with any feedback on it.

If the needs statement is missing, stop and run the needs analysis; a curriculum without one is a guess. If access to a
tool or agent is unconfirmed, mark the dependent modules "pending access" and do not schedule them. If learning time
has not been agreed, record it as to be confirmed and design a minimum version that fits a busy month.

## Decision framework

Turn each gap rating in the needs statement into a curriculum response.

| Gap rating | Curriculum response | Evidence at the end |
|---|---|---|
| None | Signpost existing resources; no module | None |
| Light | Short session or self-paced module with one practice task | A checked output from the learner's own work |
| Substantial | Module with guided practice on the role's own scenarios | Evidence that meets the pathway rubric |
| Critical | Mandatory module before access to the dependent scenario | Safe use and verification shown before access is used |

Choose formats from the role's working pattern, not from what the learning team usually runs.

| Role pattern | Default formats |
|---|---|
| Desk-based with a flexible diary | Live session, guided practice on own work the same week, follow-up clinic |
| Meeting-heavy or senior | Small-group sessions on real tasks, short asynchronous exercises |
| Shift-based or frontline | Short huddles in paid time, mobile-friendly micro-modules, supervisor-led practice |
| Spread across time zones | Recorded core content, local practice sessions, regional office hours |

Sequence by three rules: safe use and verification come first; the role's highest-value scenario comes next, so people
see a return early; the remaining modules follow by how often the work occurs.

## Practitioner approach

Start by writing the curriculum's promise in the business owner's language: "After this, a claims handler can draft a
first customer response from the case notes with Copilot, check every fact against the file, and know when not to use
it." Each learning outcome should be phrased like that - an observable piece of the role's work done with AI - rather
than "understand Copilot in Outlook". If an outcome cannot be traced to a gap in the needs statement, cut it.

Next, group the outcomes into modules. A good module covers one scenario or one tightly related set, can be practised
in the following week, and ends with something the learner produces. Resist the urge to cover every app the role has.
A curriculum that teaches three scenarios well beats one that demonstrates fifteen, because habits form around
repeated, valued tasks.

Put safe use and verification first and make them concrete for the role. For a finance role, verification means
checking figures against the ledger; for a policy role, checking that a summary has not dropped an exception. Generic
"always check the output" slides do not change behaviour. Where the needs statement rated a gap critical, the module is
a condition of using the dependent scenario, agreed with the business owner.

Design the practice before the content. For each module, decide what the learner will do with their own approved tools
on their own non-sensitive work, or on a fictional scenario pack from `learning-and-skills:practice-labs` where own work
is unsuitable. Then decide what evidence that practice leaves behind and check it against the rubric. Content is the
last thing to write and usually the smallest part.

Size the curriculum honestly. Add up session time, practice time and evidence time, and compare it with what the
business owner has agreed. If it does not fit, cut scope rather than squeezing the practice, because practice is what
makes the learning stick. Record what was cut and when it might return.

Reuse before building. Microsoft and many partners publish adoption and learning material; check the current resources
in the source records and use them for light gaps, adding only the role-specific practice and evidence.

Finally, agree owners. Each module needs a content owner who keeps it current as Copilot changes, and a delivery owner.
Walk the business owner through the curriculum and ask whether their team would recognise its work in it. Schedule it
alongside the rollout wave so people learn a scenario within days of being able to use it, not months before.

## Outputs

- A role curriculum recorded in the curriculum section of the `ai-learning-plan` template - role, outcomes, modules, sequence, formats, time, practice, evidence, owners and review date.
- A module specification per module - outcome, scenario, practice task, evidence expected, materials and facilitator.
- A delivery schedule aligned with the rollout wave and the learning calendar in the `adoption-plan` template.
- A list of deferred modules, each with its reason, such as pending access or a scenario not yet ready.

## Microsoft platform considerations

Modules follow the experiences the role will actually meet: Copilot Chat, Copilot in the Microsoft 365 apps, approved
agents, Copilot Cowork and, for some roles, Agent Builder. Product names, features and availability change often, so
check them against `references/sources.md` when writing and refreshing each module, and never teach a feature the role
has not been confirmed to have. Licensing questions go to the Microsoft licensing guide or a licensing partner.

## Adoption considerations

The curriculum is one part of the role's adoption journey. Align modules with the journey milestones from
`copilot-adoption:role-based-adoption`, so managers reinforce what was taught and teams build routines around the same
scenarios. Learning that arrives without manager follow-up fades within weeks.

## Knowledge considerations

Scenarios that depend on finding trusted content will disappoint if that content is stale or scattered. Check with the
knowledge owner before teaching a scenario, and refer gaps to `knowledge-management:knowledge-gap-analysis`. Curriculum
materials are knowledge assets too, with an owner, version and review date.

## Security and privacy considerations

Practice uses the learner's own approved tools and non-sensitive work, or fictional material. Group sessions never use
real personal or confidential data on screen. The safe use module covers what not to share and how to report a concern
using the organisation's approved-use guidance. Any learner data held about completion or evidence is minimal and
retained only as agreed with the data protection lead.

## Responsible AI considerations

For roles whose AI-assisted outputs affect people, money, rights or safety, verification and human judgement are taught
as controls, with the role's own examples of what goes wrong. The curriculum teaches when not to use AI as well as how,
and never rewards volume of use.

## Evaluation requirements

Not applicable as AI evaluation, because no AI solution is being released. The curriculum is checked by whether
learners produce evidence that meets the rubric, reported at role level, and by the business owner's confirmation that
the outcomes match the role's work.

## Value measures

Baseline: the role's declared-skills picture and adoption signals at the start of the wave. Measures: share of the
role reaching each module's evidence, changes in scenario use at team level, and learner and manager feedback. Owned by
the Learning Lead and reported at role level above the minimum group size through `learning-and-skills:skills-measurement`.

## Scale notes

### Starter

One or two priority roles, each with three or four modules built around its top scenarios, delivered by the adoption
lead or a partner, with evidence collected in sessions.

### Scale

A curriculum per priority role in each wave, built from shared module components on the common pathway, with named
content owners and a refresh whenever Copilot changes what the role sees.

### Enterprise

A curriculum library with shared foundation modules and role-specific modules owned by business-unit learning partners,
localised where needed, governed centrally so the same scenario is not taught three different ways.

## Hand-offs

- To `learning-and-skills:facilitator-guide` to write guides for each live session.
- To `learning-and-skills:practice-labs` where a module needs a fictional scenario pack or sandbox.
- To `learning-and-skills:learning-evidence-rubric` where a module's evidence needs rubric descriptors.
- To `learning-and-skills:office-hours` for follow-up clinics after each module.
- To `learning-and-skills:skills-measurement` for role-level measures after delivery.

## Reviewer gates

Not applicable, because a curriculum does not release an AI solution. Modules that teach a new agent or Cowork task
only go live once that solution has passed its own release gates.

## Failure modes

- The curriculum is a feature tour of every app, so nothing becomes a habit.
- Practice is squeezed out to fit the time available, and learners leave able to describe Copilot but not use it.
- Learning is scheduled months before access, and has been forgotten by the time the role can use it.
- Modules teach features the role has not been given, damaging trust in the whole programme.
- Completion is reported as capability, so the business believes the role is ready when it is not.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Build a curriculum for a role without an agreed needs statement.
- Count attendance or completion as evidence that someone can do the work.
- Use real personal or confidential data in group sessions or shared exercises.
- Report curriculum progress for individuals or below the agreed minimum group size.

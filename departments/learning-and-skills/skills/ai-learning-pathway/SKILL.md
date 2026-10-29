---
name: ai-learning-pathway
description: Designs the progressive AI learning pathway shared across roles - foundation, applied, proficient and advanced levels with entry conditions and exit evidence, a route to skip a level by showing evidence, where role curricula and the Champion journey plug in, and refreshers when Microsoft AI changes. Use when every team builds its own course, when experienced users are forced through basics, or when nobody knows what follows foundation.
license: CC-BY-4.0
metadata:
  department: learning-and-skills
  lifecycle: Mobilise, Enable, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-studio
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-overview, ms-champion-best-practice
  status: draft
  authors: Simon Foote
---

# AI learning pathway

## Purpose

A learning pathway gives the whole workforce one shared route from first safe use of Microsoft AI to advanced work,
so that role curricula, the Champion journey and specialist learning fit together instead of competing. This skill
defines the levels, what each one covers, the evidence that moves someone on, and how people skip what they already
know and refresh what has changed. It usually goes wrong in three ways: levels defined by hours attended rather than
practice shown, a rigid sequence that bores experienced users into leaving, and a pathway that stops at foundation so
nobody knows what good looks like next.

## When to use

- Several teams are building their own AI courses and learners cannot tell how they relate.
- Experienced users are being made to sit through beginner sessions before they can go further.
- Foundation learning is done and people ask what comes next.
- Role curricula exist but share no common levels, so progress means different things in each.
- Copilot or agents have changed enough that people who learnt a year ago are now out of date.

## When not to use

- Analysing what each role needs - use `learning-and-skills:ai-skills-needs-analysis`.
- Designing the modules for one specific role - use `learning-and-skills:ai-role-curriculum`.
- Writing the rubric descriptors that decide whether evidence meets a level - use `learning-and-skills:learning-evidence-rubric`.
- Detailed tracks for makers, power users and specialists - use `learning-and-skills:advanced-pathways`.
- The Champion journey, its capabilities and recognition - use `champions:capability-framework` and `champions:recognition-and-progression`.
- The first-days experience for newly enabled users - use `copilot-adoption:copilot-onboarding`.

## Questions to ask first

1. Which Microsoft AI experiences are approved and available to which groups now, and which are planned in the next waves?
2. What learning already exists, including Champion sessions and partner content, and where does it sit on a progression?
3. Does the organisation want any level to be a condition of access, for example foundation before Copilot is switched on?
4. How will people show they can skip a level, and who checks that evidence?
5. Who owns the pathway as a whole, and how will it be refreshed when products change?

## Required inputs

- The approved tools and agents by group, and the rollout waves, from the rollout or launch plan.
- Role needs statements from `learning-and-skills:ai-skills-needs-analysis`, to confirm the levels match real needs.
- The existing learning catalogue, the Champion capability framework from `champions:capability-framework`, and any partner content.
- Any decision on mandatory learning before access, made by the sponsor with HR and the data protection lead.

If tools or agents for a level are not yet approved, define the level and mark it "not yet open" rather than leaving it
out, so people can see where the pathway goes. If there is no decision on mandatory learning, assume none is mandatory
except safe-use content the approved-use guidance already requires.

## Decision framework

Use four levels. Each level is defined by what people can show, not by what they attended.

| Level | Who it is for | What it covers | Exit evidence |
|---|---|---|---|
| Foundation | Everyone with approved AI access | Approved tools, what not to share, how to report a concern, verifying outputs, Copilot Chat on everyday tasks | Safe use and a verified output on a real, non-sensitive task |
| Applied | People whose roles have defined scenarios | The role's scenarios in the Microsoft 365 apps, using approved agents, reusable prompt patterns | Rubric evidence on two of the role's scenarios |
| Proficient | Frequent users, team leads, people who help others | Delegating multi-step work to Copilot Cowork with checkpoints, improving team patterns, judging agent candidates, helping a colleague | A reusable pattern a colleague has used, or a reviewed delegated task |
| Advanced | Makers, power users and specialists | Building and operating agents, automation, code and Foundry solutions | Defined by `learning-and-skills:advanced-pathways` |

Movement rules:

| Situation | Rule |
|---|---|
| Learner has experience | Submit exit evidence for any level directly; no attendance needed |
| Learner has a verified Champion capability | Accept it as equivalent evidence where the rubric dimensions match |
| Level is a condition of access | Only where agreed by the sponsor, and only for safe use and verification |
| Product change alters a level | Run a refresher; previous evidence stays valid unless safe use guidance changed |

## Practitioner approach

Begin with the end state rather than the first course. Describe, in a paragraph per level, what someone at that level
does in a normal week with Microsoft AI. "At Applied, a person uses Copilot for the two or three tasks in their role
where it helps most, checks the outputs as a matter of habit, and knows which approved agents exist for their work."
These descriptions keep the levels anchored in behaviour and give curriculum designers and learners a shared picture.

Keep the levels few and generic. Role curricula supply the role-specific content; the pathway supplies the frame they
hang on. Four levels are enough for almost any organisation. More levels create false precision and arguments about
boundaries; fewer leave a gap between first use and building.

Make evidence the only gate. Each level's exit is a piece of practice someone can show, assessed against the rubric
from `learning-and-skills:learning-evidence-rubric`. Attendance can support learning but never moves anyone up. This
also creates the skip route: anyone confident enough to submit evidence for a level may do so straight away. Publish
exemplars, using fictional material, so people can judge whether they are ready.

Connect the pathway to what already exists. The Champion journey's capabilities overlap with Applied and Proficient;
agree with the Champions programme owner that verified Champion capabilities count as pathway evidence and that pathway
evidence can support a Champion submission. Map each existing session onto a level and retire duplicates. Map each role
curriculum onto the levels it covers so learners see where it takes them.

Be careful with mandatory levels. Making foundation a condition of access can be justified for safe use and
verification, especially for roles handling sensitive content, but it slows adoption and can feel like a test. Agree it
explicitly with the sponsor, keep the mandatory part short, and offer an evidence route as well as a session.

Plan for change. Microsoft AI changes often, so give each level an owner and a review point, and decide in advance what
triggers a refresher: a change in what people see, a new approved agent or task type, or a change to approved-use
guidance. Previous evidence normally stays valid; people receive a short refresher rather than repeating the level.

Publish the pathway in plain language with a simple diagram, the exit evidence for each level, exemplars and where to
get help. Learners should be able to place themselves on it in a couple of minutes without asking anyone.

## Outputs

- A pathway definition in the pathway section of the `ai-learning-plan` template - levels, behaviour descriptions, coverage, entry conditions, exit evidence, owners and review points.
- A movement and equivalence policy covering skipping by evidence, Champion equivalence, mandatory levels and refreshers.
- A map of existing sessions and role curricula onto the levels, with duplicates marked for retirement.
- A learner-facing pathway guide with exemplars of exit evidence using fictional material.

## Microsoft platform considerations

Levels follow the progression of Microsoft AI experiences rather than individual products: chat, Copilot in the apps,
agents, delegated multi-step work in Copilot Cowork, then building with Agent Builder, Copilot Studio, Power Platform,
Copilot Code or Microsoft Foundry. Building on patterns rather than product names keeps the pathway stable through
renames. Check current names and availability in `references/sources.md` before publishing or refreshing a level.

## Adoption considerations

The pathway gives managers and Champions a common language for encouraging the next step. Publish it alongside the
adoption campaign and let teams see which levels their role curriculum covers. Never use pathway levels to compare
teams or individuals in ways that turn learning into a league table.

## Knowledge considerations

The pathway guide, exemplars and session map are knowledge assets with an owner, a version and a review date. Retire
superseded versions so people do not follow an out-of-date route.

## Security and privacy considerations

Exit evidence must not contain personal or confidential data; the pathway guide explains what to redact. Level records
are held at the minimum needed, with access restricted and a retention period agreed with the data protection lead.
Questions about using learning records in HR processes end with HR and the DPO.

## Responsible AI considerations

Verification and knowing when not to use AI are part of every level, not just foundation. The Proficient level adds
judgement about when a task should not be delegated or turned into an agent.

## Evaluation requirements

Not applicable as AI evaluation, because the pathway does not release an AI solution. The pathway is reviewed by
whether exit evidence at each level shows the described behaviour, sampled by the Learning Lead at level and role level.

## Value measures

Baseline: the number and spread of people at each level when the pathway launches, from evidence rather than attendance.
Measures: movement between levels by role and team, time from access to foundation evidence, and use of the skip route.
Owned by the Learning Lead, reported above the minimum group size through `learning-and-skills:skills-measurement`.

## Scale notes

### Starter

Foundation and Applied defined in full, Proficient and Advanced described so people can see the route, with one
exemplar per level and a short pathway page.

### Scale

All four levels live, role curricula mapped to them, Champion equivalence agreed, refresher triggers in place and level
owners named.

### Enterprise

One pathway used across business units and regions with local delivery, central ownership of levels and evidence
standards, and advanced tracks run with the Centre of Excellence.

## Hand-offs

- To `learning-and-skills:ai-role-curriculum` to build role content against the levels.
- To `learning-and-skills:learning-evidence-rubric` for the exit evidence descriptors.
- To `learning-and-skills:advanced-pathways` for the Advanced level tracks.
- To `champions:capability-framework` to agree equivalence between Champion capabilities and pathway levels.

## Reviewer gates

Not applicable, because a learning pathway does not release an AI solution. Any proposal to make a level a condition of
access goes to the sponsor, HR and the data protection lead before it is adopted.

## Failure modes

- Levels are defined by hours of training, so people move up without being able to do anything new.
- There is no skip route, experienced users disengage, and the pathway loses its most credible advocates.
- The pathway and the Champion journey run separately and contradict each other.
- Levels are named after products, and a rename makes the pathway look obsolete overnight.
- Level counts are used to rank teams, and teams game the evidence.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Move anyone up a level on attendance alone.
- Make a level a condition of access without an explicit sponsor decision and HR involvement.
- Use pathway levels to rank, score or compare individuals.
- Publish a level that teaches tools the audience has not been approved to use without marking it not yet open.

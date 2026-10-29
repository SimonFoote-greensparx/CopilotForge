---
name: advanced-pathways
description: Designs advanced AI pathways for makers, power users and specialists - entry on declared role, approved access and maker commitments, tracks for delegated Cowork work, agent and automation makers, Copilot Code and Microsoft Foundry, learning by building in governed sandboxes with mentoring, and evidence from a reviewed build. Use when building opens to more people, when makers learn in production, or when specialists lack a route.
license: CC-BY-4.0
metadata:
  department: learning-and-skills
  lifecycle: Enable, Deliver, Scale
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2
  platforms: copilot-cowork, m365-agents, copilot-studio, power-platform, copilot-code, ai-foundry, github
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-agent-builder, ms-copilot-studio-guidance, ms-copilot-studio-zoned-governance, ms-managed-environments, ms-copilot-cowork-customise, ms-foundry-models, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Advanced pathways

## Purpose

Once people can use Microsoft AI well, some need to go further: delegating complex work, building agents and
automations, writing code with Copilot or engineering solutions in Microsoft Foundry. This skill designs the advanced
pathways that take them there, track by track, with entry conditions, learning by building in safe places, mentoring
and evidence from a real, reviewed piece of work. It usually goes wrong when advanced learning is a collection of
product courses with no link to governance, when makers learn by trial and error in production, and when the pathway
produces confident builders who have never tested, documented or handed over anything.

## When to use

- Agent building or automation is being opened to more people, and they need a structured way to learn it well.
- Makers are learning by experimenting in production or the default environment.
- Power users have outgrown the Proficient level and ask what comes next.
- Developers or AI engineers are adopting Copilot Code or Microsoft Foundry without a shared standard of practice.
- Builds reaching review keep failing for the same reasons, such as missing tests, owners or documentation.

## When not to use

- Governing who may build and share, and makers' onboarding commitments - use `platform-governance:maker-governance`.
- Setting the environment zones where building happens - use `platform-governance:ai-environment-strategy`.
- The learning offer for recognised Champions within the Champion journey - use `champions:champion-learning`.
- The shared foundation-to-proficient pathway for the whole workforce - use `learning-and-skills:ai-learning-pathway`.
- Analysing which roles need building skills at all - use `learning-and-skills:ai-skills-needs-analysis`.
- Building and staffing the AI delivery team itself - use `organisation-tailoring:capability-gap-analysis`.

## Questions to ask first

1. Which building and advanced-use activities are approved, for which groups, in which environments - delegated Cowork tasks, Agent Builder, Copilot Studio, Power Platform, Copilot Code, Foundry?
2. Who is asking for advanced learning, by declared role, and what will they build or do with it in the next six months?
3. What commitments does maker governance require before someone can build and share, and does the pathway need to cover them?
4. Who can mentor - experienced makers, the Centre of Excellence, engineers, a partner - and with what agreed time?
5. Where do learning builds live, and how does a build worth keeping move into intake and release?

## Required inputs

- Maker governance rules and onboarding commitments from `platform-governance:maker-governance`.
- The environment zones and learning sandboxes from `platform-governance:ai-environment-strategy` and `learning-and-skills:practice-labs`.
- Role needs statements showing which roles include building, from `learning-and-skills:ai-skills-needs-analysis`.
- The organisation's engineering, testing and release standards for each platform, from the relevant delivery departments.
- Named mentors with agreed time.

If maker governance is not in place, do not open a maker track; offer the power user track and record the dependency.
If no learning sandbox exists for a platform, defer its track rather than letting people learn in production.

## Decision framework

Define tracks by what people will do, each building on Proficient evidence from the workforce pathway.

| Track | For | Covers | Evidence to complete |
|---|---|---|---|
| Power user | Heavy users who delegate complex work | Designing delegated multi-step tasks for Copilot Cowork, human checkpoints, reusable task designs, judging agent candidates | A delegated task design with checkpoints, reviewed and reused by the team |
| Agent maker | People approved to build agents | Use-case judgement, Agent Builder, Copilot Studio basics, instructions, grounding, testing, ownership, release route | A governed agent in the learning or team zone with owner, instructions, test set and release record |
| Automation maker | People approved to build flows | Process design, Power Automate patterns, exception handling, connectors under policy, human in the loop | A tested flow with exception handling, owner and documentation |
| Developer | Developers using Copilot Code | Repository context, prompting for code, reviewing generated code, security review, testing | A reviewed change with tests and a generated-code review record |
| AI specialist | Engineers using Microsoft Foundry | Model selection, grounding and retrieval, evaluation, safety testing, observability, cost | An evaluated prototype on synthetic data with an evaluation plan and results |

Entry rules:

| Condition | Rule |
|---|---|
| Workforce pathway | Proficient evidence, or equivalent Champion capability |
| Role | Declared role or agreed future work includes the track's activity |
| Access | Approved for the platform and environment; never assumed |
| Commitments | Maker onboarding commitments accepted before any build is shared |

## Practitioner approach

Start from the work, not the product. For each track, describe what someone who has completed it does: "An agent maker
can judge whether an agent is the right answer, build a simple governed agent in the team zone, test it with realistic
questions, name an owner and take it through release." That description decides the content and the evidence, and
keeps the track from turning into a feature course.

Tie every track to governance from the first module. The rules on where to build, what to share, ownership and release
are not an appendix; they are what separates a maker from someone who creates ungoverned solutions. Cover the
onboarding commitments maker governance requires, and make accepting them a condition of building anything that will
be shared.

Learn by building in safe places. Each track centres on a build or piece of work in a learning sandbox or the zone the
environment strategy allows, using fictional or synthetic data. Learners move through small builds to one meaningful
piece that addresses a real need in their area. That final piece is the evidence: not a certificate, but a build with
tests, an owner and documentation that a reviewer could pick up.

Make testing and handover part of the craft. Most builds that fail review fail on the same things - no realistic test
questions, no owner, no plan for when the maker moves on. Teach these as core skills with the same weight as building.
For Foundry and code tracks, evaluation and security review practice are central, not optional.

Pair learners with mentors. A short regular check-in with an experienced maker or engineer catches poor patterns early
and teaches the judgement that courses cannot. Agree mentor time with their managers, and keep the ratio of learners to
mentors realistic.

Use Microsoft's published learning for product depth. Point learners to current Microsoft resources for features and
configuration, checked against the source records, and spend the organisation's effort on the parts only it can teach:
its governance, environments, standards, patterns and real use cases.

Connect the end of each track to real delivery. A build worth keeping moves through intake, design and release like
any other solution; the pathway never promotes it directly. Completing a track can lead to joining a maker community,
contributing to the Centre of Excellence or mentoring the next cohort.

Review the tracks when products or governance change, and when the reasons builds fail review shift.

## Outputs

- An advanced pathways definition recorded in the advanced pathways section of the `ai-learning-plan` template - tracks, audiences, entry rules, content, mentoring, evidence and owners.
- A track guide per track with modules, sandbox builds, the final build brief and evidence requirements.
- A mentoring arrangement with named mentors, agreed time and check-in rhythm.
- A route from completed learning builds into intake and release, agreed with platform governance.

## Microsoft platform considerations

Tracks follow the building platforms the organisation approves: Copilot Cowork for delegated work, Agent Builder and
Copilot Studio for agents, Power Platform for automation, Copilot Code and GitHub for development, and Microsoft Foundry
for engineered solutions including third-party models available through Microsoft. Which platform fits a need is a
design decision owned elsewhere; the pathway teaches each in the context of the organisation's zones and standards.
Features, limits, model availability and licensing change often, so check `references/sources.md` and route licensing
to `platform-governance:ai-licensing-and-capacity`.

## Adoption considerations

Advanced learners become multipliers. Connect graduates to the maker community and the Champions network so their
patterns reach others, and make clear that building is a privilege that comes with commitments rather than a badge.

## Knowledge considerations

Agents and Foundry solutions depend on good knowledge sources. Tracks teach makers to check content readiness and
ownership before grounding a solution on it, and to involve the knowledge owner. Reusable patterns from completed
tracks are recorded with an owner.

## Security and privacy considerations

Learning builds use fictional or synthetic data in approved environments with no production connectors or live
secrets. Tracks teach connector policy, authentication and secrets handling for their platform. Anything moving beyond
the learning environment goes through the security review its risk tier requires.

## Responsible AI considerations

Every track includes when not to build, human oversight, transparency to users and testing for harmful or wrong
outputs. The AI specialist track covers safety evaluation in depth. Learners never build solutions that make decisions
about people as practice exercises.

## Evaluation requirements

Track evidence includes testing appropriate to the platform: realistic test questions for agents, test runs and
exception cases for flows, tests and review for code, and an evaluation plan with results for Foundry work. Learning
builds are evaluated as practice, not released; any build promoted later is evaluated under the release process.

## Value measures

Baseline: the share of builds reaching review that fail on testing, ownership or documentation, and the number of
ungoverned builds found, before the tracks launch. Measures: first-time pass rate at review for builds by track
graduates at cohort level, orphaned solutions over time, and track completion by evidence. Owned by the Learning Lead
with the platform governance owner, reported at cohort or role level, never ranking makers.

## Scale notes

### Starter

One or two tracks, usually power user and agent maker, run as small cohorts with a mentor and a learning sandbox, with
other tracks described as future routes.

### Scale

All approved tracks with cohorts each quarter, a mentor pool, standard track guides and a defined route from learning
builds into intake.

### Enterprise

Tracks run with the Centre of Excellence across business units, localised mentoring, specialist tracks for engineering
teams, and pathway content updated with platform and governance changes.

## Hand-offs

- To `platform-governance:maker-governance` for onboarding commitments and sharing rights on completion.
- To `learning-and-skills:practice-labs` for sandboxes for each track.
- To `opportunity-management:idea-capture` when a learning build addresses a real need worth taking forward.
- To `ai-centre-of-excellence:coe-delivery-model` where graduates contribute to CoE delivery.

## Reviewer gates

Not applicable to learning builds that stay in the learning sandbox. Any build moved to shared or production use passes
the gates its risk tier requires under `platform-governance:ai-release-policy`, including `security-privacy` and
`evaluation-quality` from risk tier 2.

## Failure modes

- Tracks teach product features but not governance, producing confident makers who create ungoverned solutions.
- Learners practise in production because no sandbox exists, and test agents reach real users.
- Testing, ownership and handover are treated as optional, so graduates' builds fail review.
- Mentors have no agreed time, check-ins lapse and poor patterns go uncorrected.
- Completing a track is treated as permission to release, bypassing intake and review.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Open a building track before maker governance and a learning environment exist.
- Use real personal, customer or confidential data, production connectors or live secrets in learning builds.
- Promote a learning build to shared or production use outside intake and release.
- Rank makers or publish individual track progress.

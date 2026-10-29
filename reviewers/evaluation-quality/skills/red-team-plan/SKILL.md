---
name: red-team-plan
description: Plans and reviews a red-team exercise for an AI solution - objectives, scope, harm and misuse scenarios, a team with varied perspectives, rules of engagement, safe test environments, evidence recording, tester welfare and follow-through to fixes and re-tests - classing plan gaps and findings blocking or advisory. Use when a tier 3 or 4 solution nears release, when it gains new actions or audiences, or after a serious incident.
license: CC-BY-4.0
metadata:
  department: evaluation-quality
  lifecycle: Assure, Launch, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, copilot-cowork, power-platform
  edition-support: scale, enterprise
  reviewers: evaluation-quality, security-privacy, responsible-ai
  sources: ms-responsible-ai, nist-ai-rmf, ms-copilot-studio-security-governance, ms-foundry-models, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# Red-team plan

## Purpose

Scripted tests find the failures someone thought of in advance. A red-team exercise puts people with varied
perspectives in front of the solution with a mandate to make it fail - to produce harm, leak content, take wrong
actions or be misused - and records what they find. This reviewer skill plans red-team exercises for high-risk AI
solutions, reviews plans and findings submitted by teams, and classifies each gap or finding as blocking or advisory.
Red teaming goes wrong when it is a short session with the builders trying a few jailbreaks they read about, when its
findings have no owner, or when it is used to replace scripted evaluation rather than add to it.

## When to use

- A tier 3 or 4 solution is approaching release.
- A live high-risk solution gains new actions, new knowledge, a new model or a wider audience.
- A serious incident or near miss suggests failure modes nobody had tested.
- A team submits a red-team plan or findings to the `evaluation-quality` gate.

## When not to use

- Scripted tests for harmful content and distress handling - use `evaluation-quality:ai-safety-testing`.
- Security testing of prompt injection, exfiltration and tool abuse as a security discipline - use `security-privacy:ai-security-testing`.
- Setting overall evaluation methods for a solution - use `evaluation-quality:ai-evaluation-strategy`.
- Responding to a live incident - use `ai-operations:ai-incident-management`.

## Questions to ask first

1. What is the worst realistic outcome if this solution fails or is misused, and for whom?
2. Which behaviours, actions and data are in scope, and which systems must never be touched during the exercise?
3. Who should be on the red team to bring perspectives the builders lack - users, subject experts, security, people representing affected groups?
4. Where will the exercise run, and how will production data and live actions be protected?
5. Who owns each class of finding, and when will fixes be re-tested?

## Required inputs

- The solution design, risk tier, audience, knowledge sources and the actions it can take.
- Prior evaluation results, safety test results and security findings, so the team does not repeat known ground.
- A test environment that mirrors production configuration without live actions on real records.
- Named owners for content, security, responsible AI and engineering fixes.

Where no safe environment exists for a solution that acts in other systems, the exercise cannot run safely; record the
gap as blocking and build the environment rather than red-teaming in production.

## Decision framework

A plan is ready when every element below is present.

| Element | Ready when |
|---|---|
| Objectives | Two to five concrete questions the exercise must answer, tied to the worst realistic outcomes |
| Scope | Behaviours, data and actions in scope, explicit exclusions, and systems that must not be touched |
| Scenarios | Harm, misuse and failure scenarios drawn from the impact assessment, incidents and domain experts, not only public jailbreak lists |
| Team | Mix of builders and non-builders, including users and subject experts; independent members at tier 4 |
| Rules of engagement | What testers may and may not do, how to stop, how to escalate a live risk |
| Environment | Non-production, mirrored configuration, test identities, actions stubbed or sandboxed |
| Evidence | Each finding recorded with prompt sequence, output, configuration version, severity and suspected cause |
| Welfare | Volunteers briefed on distressing content, rotation and support available |
| Follow-through | Each finding owned, fixed or risk-accepted, and re-tested before release |

Classify plan gaps and findings.

| Item | Blocking when | Advisory when |
|---|---|---|
| Plan gap | No safe environment, no rules of engagement, or team made up only of builders at tier 3 and 4 | Scenario coverage thin in a lower-risk area |
| Finding | Harmful output, restricted content exposed, unsafe or unauthorised action, or misuse with serious impact | Low-impact failure with a clear fix, or usability weakness |
| Follow-through | Blocking findings unfixed or not re-tested at release | Advisory findings without a target date |

## Practitioner approach

Begin with outcomes, not techniques. Ask the business owner, a subject expert and the responsible AI lead to describe
the worst realistic things the solution could do: send a wrong instruction to a customer, approve a payment it should
not, reveal a colleague's case, tell a vulnerable person something dangerous. Turn them into the exercise objectives.
Techniques such as role-play prompts or instruction overrides are tools to reach those outcomes, not the point.

Build scenarios from several directions. Use the impact assessment, past incidents and near misses, domain experts'
knowledge of how the work goes wrong, and known attack patterns. Include misuse by legitimate users, such as someone
trying to get the agent to draft something it should not, as well as attacks by outsiders.

Choose the team for perspective. Builders know where the weak points are; users know how people actually behave;
subject experts know which wrong answers are dangerous; security staff know attack patterns; people who represent
affected groups notice harms others miss. At tier 4, include members independent of the delivery team.

Write the rules of engagement and agree them with the security lead: in-scope targets, forbidden actions, test
identities, how to stop immediately if a real system is affected, and who to call. Run the exercise in a non-production
environment with the production configuration, test identities and stubbed or sandboxed actions.

Brief the team, then let them work in short, focused rounds with a note-taker or a shared log. Every finding needs the
exact sequence of prompts, the output, the configuration version and the tester's view of severity. Debrief at the end
of each round so promising lines are pursued.

Protect people. Some scenarios involve distressing content. Use volunteers, brief them, rotate them and make support
available.

Triage findings with the owners within days, not weeks. Classify each as blocking or advisory, assign a fix owner,
and decide whether the cause is instructions, knowledge, configuration, model behaviour or design. Add reproducible
findings to the golden dataset's adversarial category so they become regression tests. Re-test blocking fixes before
the release decision.

Report honestly about coverage. A red-team exercise samples a vast space; say what was tried, what was not and how long
was spent, so nobody reads the absence of findings as proof of safety.

## Outputs

- A red-team plan: objectives, scope, scenarios, team, rules of engagement, environment, evidence format, welfare arrangements and schedule, referenced from the `evaluation-plan`.
- A findings log with reproduction steps, severity, classification as blocking or advisory, cause, owner and re-test result.
- A coverage statement describing what was and was not tested.
- New adversarial items for `evaluation-quality:golden-dataset`.

## Microsoft platform considerations

Microsoft publishes responsible AI and red-teaming resources and offers safety and evaluation features in Microsoft
Foundry and governance controls in Copilot Studio; their scope and availability change, so confirm them in
`ms-responsible-ai`, `ms-foundry-models` and `ms-copilot-studio-security-governance`. Use separate environments for
testing so that red-team activity cannot reach production data or live connections.

## Adoption considerations

Inviting users and subject experts onto the red team builds informed advocates who understand the solution's limits.
Share a plain summary of what was tested with the audience at launch.

## Knowledge considerations

Red teams often find that sensitive or inappropriate content is reachable through grounding. Route those findings to
the knowledge owner and fix them at source.

## Security and privacy considerations

Agree rules of engagement with the security lead, use test identities, and never use real personal data. Findings about
injection, exfiltration or tool abuse go to `security-privacy:ai-security-testing`; findings logs are restricted because
they describe working attacks.

## Responsible AI considerations

Red teaming is a key source of evidence for `responsible-ai:ai-impact-assessment` and `responsible-ai:ai-risk-acceptance`.
Include people who can represent affected groups, and pass harm-to-people findings to the `responsible-ai` reviewers.

## Evaluation requirements

Minimum at tier 3 and 4: an approved plan, a findings log with reproduction steps, blocking findings fixed and re-tested
before release, a coverage statement, and reproducible findings added to the regression set.

## Value measures

Track findings by severity per exercise, the share fixed and re-tested before release, and the number of live incidents
of a type the red team had covered. The AI Evaluation Lead reports by solution; never score individual testers.

## Scale notes

### Starter

Red teaming is rarely needed for starter-scale solutions, which should stay below tier 3. If one is needed, run a
half-day exercise with a partner or a small mixed team, using this plan structure.

### Scale

A repeatable red-team plan template, a pool of trained volunteers across functions, and an exercise before every tier 3
release and after material change.

### Enterprise

A standing red-team capability with independent members for tier 4, shared scenario libraries, and findings tracked
across the portfolio to target controls and training.

## Hand-offs

- To engineering, knowledge and configuration owners with findings and fixes.
- To `security-privacy:ai-security-testing` and the `responsible-ai` reviewers with relevant findings.
- To `evaluation-quality:golden-dataset` with reproducible adversarial items.
- To `evaluation-quality:ai-release-evidence` with the findings log and coverage statement.

## Reviewer gates

This skill operates within the `evaluation-quality` gate and is blocking at tiers 3 and 4, with `security-privacy` and
`responsible-ai` reviewing findings in their areas. Blocking findings stop release and are not traded against dates;
disagreement escalates to the accountable executive for written risk acceptance.

## Failure modes

- The red team is the build team, so it tests the weaknesses it already fixed.
- Findings are recorded without reproduction steps and cannot be fixed or re-tested.
- The exercise runs against production and a test action changes real records.
- An exercise with few findings is presented as proof that the solution is safe.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Red-team a solution that acts in other systems against production records or with real personal data.
- Accept a tier 3 or 4 release with blocking red-team findings unfixed or not re-tested.
- Present an absence of findings as proof of safety.
- Expose volunteers to distressing material without briefing, rotation and support.

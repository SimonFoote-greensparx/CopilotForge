---
name: foundry-safety-evaluation
description: Configures content safety controls for a Microsoft Foundry solution - input and output filtering, prompt attack detection, groundedness and protected material checks, blocklists - and runs the builder's safety evaluations against the solution's harm profile so the release gate receives evidence. Use when a Foundry model or agent is being prepared for release, when filters block legitimate work, or after a harmful output.
license: CC-BY-4.0
metadata:
  department: ai-foundry
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality, responsible-ai, security-privacy
  sources: ms-foundry-models, ms-responsible-ai, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Foundry safety evaluation

## Purpose

A Foundry solution is responsible for its own safety layer in a way configured Microsoft agents are not: the team
chooses filter settings, decides what happens when a filter fires, and must show the solution behaves safely for its
audience. This skill sets those controls from a harm profile of the use, runs automated and manual safety evaluations
during build, and hands the reviewer gate a clear evidence set. Safety work goes wrong when default filter settings are
accepted without anyone understanding them, when filters are loosened to fix one complaint and never revisited, and
when safety is tested once at the end on generic prompts rather than on the solution's real risks.

## When to use

- A Foundry model deployment or agent is being prepared for its first release and needs safety controls and evidence.
- Users report that legitimate requests are blocked, and someone proposes relaxing the content filters.
- A harmful, offensive or unsafe output has been reported from a Foundry solution.
- The solution will start reading untrusted content, reach a new audience or use a new model.
- A team wants to know which safety evaluations to automate in the build pipeline.

## When not to use

- Reviewing at the gate whether the solution's safety evidence is sufficient - that is the reviewer skill `evaluation-quality:ai-safety-testing`.
- Planning a red-team exercise for a tier 3 or 4 solution - that is the reviewer skill `evaluation-quality:red-team-plan`.
- Reviewing prompt injection, exfiltration and tool misuse testing for the security gate - that is the reviewer skill `security-privacy:ai-security-testing`.
- Comparing candidate models on task quality - use `ai-foundry:model-evaluation`.
- Deciding whether the use is acceptable at all - that is the reviewer skill `responsible-ai:prohibited-use-review`.

## Questions to ask first

1. Who will use the solution, and who could be harmed by its outputs even if they never use it?
2. Which harms matter most for this use: harmful content categories, unsafe or regulated advice, invented facts, exposure of protected material, or manipulation through injected instructions?
3. Will the solution read content the organisation does not control, and can it take actions?
4. What should the user see, and what should be logged, when a filter blocks an input or output?
5. What is the risk tier, and which reviewer gates and thresholds already apply?

## Required inputs

- The solution design on the `foundry-solution-design` template with risk tier, audience and tool list.
- The impact assessment from `responsible-ai:ai-impact-assessment` where one exists, or at least a list of foreseeable harms.
- The evaluation plan on the `evaluation-plan` template, with safety thresholds agreed before testing.
- Access to a non-production deployment configured exactly like production.

Where the harm profile or thresholds are missing, mark them `[To confirm: ...]` and do not declare the solution safe.
Testing without an agreed threshold produces numbers nobody can act on.

## Decision framework

| Harm profile | Default control posture | Evaluation depth |
|---|---|---|
| Internal staff, informational, no actions (tier 0 or 1) | Platform default filters, prompt attack detection on, standard refusal message | Automated safety evaluation on a representative set |
| Broad workforce or sensitive topics (tier 2) | Defaults reviewed per category, blocklists for known terms, groundedness checks where answers rely on sources | Automated plus manual review of borderline and refusal cases |
| Public, vulnerable users, regulated advice or actions (tier 3 or 4) | Stricter settings justified per category, output checks before any action, human escalation path | Automated, manual and red team, with re-test after every fix |

| Proposed change to controls | Condition for approval |
|---|---|
| Loosen a filter category | Evidence of specific false blocks, a narrower alternative tried first, re-evaluation, reviewer agreement from tier 2 |
| Switch a check off | Never for prompt attack detection on solutions reading untrusted content; otherwise a recorded risk acceptance |
| Add a blocklist term | Owner named, reason recorded, false-block test run |

## Practitioner approach

Start from the harm profile, not the filter menu. With the business owner, list who could be harmed and how, using the
impact assessment where it exists. A finance summariser and a public-facing advice agent need very different controls,
and the profile is what justifies each setting to a reviewer later.

Configure controls in layers. Platform content filtering on inputs and outputs is the first layer; prompt attack
detection guards against direct and indirect injection; groundedness and protected material checks address invented
claims and reproduced copyrighted content where the solution's outputs warrant them. The system prompt adds refusal
behaviour, and tool permissions and confirmation steps contain anything that could still slip through. No single layer
is sufficient, so record what each one is for.

Decide what happens when a control fires. Users should get a short, honest message and a route forward, not a raw error
or silence. Log the event with the category and the deployment version, but think carefully before logging the full
blocked content, which may itself be harmful or personal.

Build a safety evaluation set alongside the quality set. Include the harms in the profile, realistic misuse attempts,
injected instructions inside documents the solution reads, sensitive but legitimate requests that must not be blocked,
and users in distress. Run automated safety evaluators where the platform provides them, but read a sample of outputs
yourself, because automated scores miss context. Record results against thresholds agreed before testing.

Treat over-blocking as a safety finding too. When legitimate work is blocked, users route around the solution into
unapproved tools. Before loosening a category, look for a narrower fix: better instructions, a blocklist exception, or a
redesigned input. Any loosening is re-evaluated and recorded.

Automate the safety run in the pipeline so every prompt, model or configuration change repeats it, and repeat manual
review when the audience or tools change. Assemble the results, configuration and known limits into the safety section
of the solution design for the `evaluation-quality` and `responsible-ai` gates.

Be clear about limits. Safety evaluation shows how the solution behaved on the cases tried; it cannot prove the absence
of harm. Say which harms were not tested and why.

## Outputs

- A harm profile and control configuration record in the safety section of the `foundry-solution-design` template: each control, its setting, why, and the behaviour when it fires.
- A safety evaluation set and results against agreed thresholds, recorded on the `evaluation-plan` template.
- A log of every filter change with evidence and approver.
- A list of untested harms and residual risks for `responsible-ai:ai-risk-acceptance` where needed.

## Microsoft platform considerations

Microsoft Foundry provides content filtering, prompt attack detection, groundedness and protected material checks and
safety evaluators, and their categories, configurability, model coverage and preview status change frequently. Some
settings may require approval to change. Check the current source records before stating what a control does or which
models and deployment types it covers, and confirm whether third-party models in the catalogue receive the same
controls as models sold by Microsoft.

## Adoption considerations

Users trust a solution that refuses clearly and offers a way forward, and abandon one that blocks without explanation.
Agree the refusal and block messages with the business owner and monitor how often legitimate users hit them.

## Knowledge considerations

Grounding content can carry injected instructions or harmful material. Agree with knowledge owners which sources are
trusted, and treat external or user-supplied content as untrusted regardless of where it is stored.

## Security and privacy considerations

Prompt attack detection is a security control as much as a safety one; keep it on for any solution that reads untrusted
content. Logged blocked content may contain personal or harmful data, so set its access and retention with
`security-privacy:ai-interaction-retention`.

## Responsible AI considerations

The harm profile must consider people affected by outputs who never use the solution, and groups who may be served
worse. Coordinate with `responsible-ai:fairness-review` where outputs concern people, and never trade a known serious
harm for a delivery date.

## Evaluation requirements

Safety thresholds are set per harm category before testing, including a ceiling on false blocks of legitimate requests.
Every model, prompt, filter or audience change repeats the automated safety run; tier 3 and 4 also repeat manual review
and red-team cases.

## Value measures

Measure harmful-output incidents in production, false-block rate on legitimate requests and time to fix safety
findings, at solution level, owned by the solution owner with the responsible AI lead.

## Scale notes

### Starter

Use platform defaults with prompt attack detection on, a small safety set built from the harm profile, and a manual
review of results before release.

### Scale

Share a baseline control configuration and a reusable safety set by audience type, with solution-specific additions,
and run the safety evaluation automatically in every pipeline.

### Enterprise

Govern control configurations centrally with recorded exceptions, track safety incidents across all Foundry solutions,
and feed common failure patterns back into the shared baseline.

## Hand-offs

- To `evaluation-quality:ai-safety-testing` for the gate review of the evidence.
- To `evaluation-quality:red-team-plan` for tier 3 and 4 solutions.
- To `ai-foundry:foundry-prompt-engineering` when refusals or tone need prompt changes.
- To `ai-foundry:foundry-observability` so safety events are traced and alerted in production.
- To `ai-operations:ai-incident-management` when a harmful output reaches users.

## Reviewer gates

From risk tier 2, `evaluation-quality` checks safety evidence against thresholds set in advance, `responsible-ai` checks
the harm profile covers affected people, and `security-privacy` checks prompt attack controls. A filter loosened without
re-evaluation is a blocking finding at any tier.

## Failure modes

- Default filters are accepted without review, and a public-facing solution gives unsafe advice in a category the defaults allow.
- A filter is loosened to stop one complaint, never re-tested, and harmful content passes for months.
- Safety is tested only with generic attack prompts, and injected instructions in the solution's own documents go untested.
- Over-blocking drives staff back to unapproved tools, and the solution is judged safe because nobody uses it.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Declare a solution safe without a harm profile and thresholds agreed before testing.
- Switch off prompt attack detection on a solution that reads untrusted content.
- Loosen a content filter without evidence, re-evaluation and a recorded approver.
- Claim that safety evaluation proves the absence of harm.

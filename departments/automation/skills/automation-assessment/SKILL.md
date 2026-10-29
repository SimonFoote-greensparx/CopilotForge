---
name: automation-assessment
description: Assesses a process put forward for automation step by step - volume, stability, input structure, rules, exceptions and systems - and decides which steps suit a deterministic flow, which genuinely need an AI step, which need a desktop flow and which should stay human. Use when a team asks to automate a process, when an automation request already assumes AI, or when several automation candidates need consistent treatment.
license: CC-BY-4.0
metadata:
  department: automation
  lifecycle: Discover, Envision, Deliver
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: power-platform, copilot-studio, ai-foundry
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-copilot-studio-guidance, ms-copilot-studio-zoned-governance, ms-coe-starter-kit, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Automation assessment

## Purpose

Automation requests usually arrive as "can we get AI to do this", when most of the work is moving structured data
between systems on fixed rules. This skill breaks the candidate process into steps and decides, for each one, whether a
deterministic flow, an AI step, a desktop flow or a person should do it, and whether the whole thing is worth automating
yet. It goes wrong when AI is placed in steps that a rule could handle reliably and cheaply, and when unstable or
undocumented processes are automated before anyone has agreed how they should work.

## When to use

- A business team asks to automate a process and the request has passed problem framing.
- `opportunity-management:ai-suitability` has landed on deterministic automation, or automation combined with an agent, and the steps now need sorting.
- An automation request names an AI capability (extraction, classification, summarising) and the need for it is untested.
- Several automation candidates from different teams need to be compared on the same criteria.
- An existing flow is being extended with an AI step and the case for that step needs checking.

## When not to use

- Deciding whether the overall problem needs AI, an agent or no technology at all - use `opportunity-management:ai-suitability`.
- Redesigning the process once it is judged worth automating - use `automation:automation-process-design`.
- Building the flow and its AI steps - use `automation:flow-design-patterns`.
- Deciding whether a need warrants an agent rather than a flow - use `m365-agents:agent-opportunity-assessment`.
- Ranking assessed candidates against the wider backlog - use `opportunity-management:opportunity-prioritisation`.

## Questions to ask first

1. How often does the process run, how long does each instance take, and how much does that vary across teams and seasons?
2. Is the process documented and followed the same way by everyone, or does each person do it differently?
3. For each step, are the inputs structured (fields, records) or unstructured (emails, documents, images, free text)?
4. What happens today when something goes wrong, and who decides what to do with the cases that do not fit?
5. Which systems are involved, and do they offer supported connectors or APIs, or only a user interface?
6. What is the effect of a wrong result at each step, and who would notice?

## Required inputs

- A framed problem with a named process owner, from `opportunity-management:problem-framing`.
- A step list of the current process, even a rough one, with the systems each step touches.
- Volumes and handling times, ideally measured rather than estimated; estimates are marked as such.
- The approved platforms and environments for automation, from the CoE or platform team.
- An initial risk tier, or enough information for `opportunity-management:risk-classification` to set one.

Where volumes or step detail are missing, mark them "to confirm" and limit the recommendation to a provisional
classification. Never assume a connector exists for a system or that a licence covers a capability.

## Decision framework

First decide whether the process is ready to automate at all. If it fails any readiness test, the answer is
`automation:automation-process-design` first, not a build.

| Readiness test | Ready when | Not ready when |
|---|---|---|
| Stability | Steps and rules have been stable for months and are written down | Rules change often or live in one person's head |
| Volume | Volume or frequency justifies build and run effort | A few instances a month that a person handles quickly |
| Ownership | A named process owner will own the automation and its exceptions | Nobody will own exceptions after go-live |
| Exceptions | Exceptions are known and a minority | Most instances are exceptions |

Then classify each step. Stop at the first row that fits.

| Step type | Classify as | Signals |
|---|---|---|
| Structured input, fixed rule, supported system | Deterministic flow step | Field mapping, routing on known values, notifications, record updates |
| Unstructured input that must become structured data | AI step with validation | Pulling fields from invoices, classifying free-text requests, detecting intent in emails |
| Language output a person will read | AI step with human review | Drafting replies, summarising cases for a handler |
| No supported connector or API, only a screen | Desktop flow, with a plan to replace it | Legacy or vendor systems with no integration route |
| Judgement with material consequences, or rare and varied | Human step, possibly AI-assisted | Approvals affecting people, money or rights; one-off cases |

An AI step is justified only where the input is genuinely unstructured or the output is language. Every AI step needs a
defined output shape, a confidence or validity check and a route for what fails it.

## Practitioner approach

Begin with the process owner and walk through three real recent instances, not the documented procedure. Ask the
person who does the work to show each step on screen. The documented procedure is usually incomplete, and the
undocumented workarounds are where automation projects later fail. Write each step on one line with its input, its
output, the system and who does it.

Test readiness before classifying anything. Look for steps that differ by team, rules nobody can state, and cases that
are "handled by whoever knows". If the process is unstable, recommend process design first and record the automation
idea as deferred. Automating an unstable process fixes its current confusion in place and makes it harder to change.

Classify each step using the table, starting from the cheapest option. Ask of every proposed AI step: could a rule, a
lookup or a better form do this? A request to "use AI to read the order email" often disappears when the supplier can be
asked to send a structured file or use a form. Where AI is needed, name the specific task (extract these six fields,
classify into these eight categories), because a precise task is testable and a vague one is not.

Look at the systems next. Prefer supported connectors and APIs. Mark any step that would need a desktop flow and ask
whether an API is planned; desktop flows are a bridge, not a destination, and `automation:desktop-automation` sets the
conditions for using them.

Estimate value honestly. Count the time the automation saves, then subtract the time people will spend reviewing AI
outputs and working exceptions. A step that saves two minutes but needs a one-minute review of every result is worth
far less than it first appears. Note run and support effort, because every automation needs an owner after go-live.

Check consequences. Where a wrong result could affect people, money or rights, keep a person in the step or require
approval before effect, and flag the case for `automation:human-in-the-loop`. Confirm the risk tier, since automations
that act without per-instance review often sit higher than their builders expect.

Record the assessment: readiness verdict, step classification, the case for each AI step, systems and integration
route, the value estimate with its assumptions, risk tier, and open questions. Share it with the process owner in plain
terms. Product capabilities change, so check the current source records before assuming a feature, and cite them.

## Outputs

- An automation assessment record: readiness verdict, step-by-step classification (flow, AI step, desktop flow, human), justification for each AI step, systems and integration route, value estimate with assumptions, risk tier and open questions.
- A go, defer or decline recommendation with the reason, and where deferred, the precondition (usually process design).
- The step list, ready to seed the `automation-design` template in `automation:automation-process-design`.

## Microsoft platform considerations

Power Automate cloud flows suit connector-based steps, desktop flows suit user-interface-only systems, and AI steps can
use prebuilt or custom AI models in Power Platform or models deployed through Microsoft Foundry. Which of these the
organisation may use depends on its approved environments, data policies and licensing, which change often. Check
availability and limits in the source records in `references/sources.md`, and route licensing questions to the Microsoft
licensing guide or a licensing partner.

## Adoption considerations

The people who do the work today are the best source of step detail and the most affected by the change. Involve them
in the walkthrough and tell them what the assessment concluded. Present automation as removing the repetitive parts of
their work, and be honest where roles will change; route significant role impact to
`change-and-communications:people-change-impact`.

## Knowledge considerations

Automation assessment rarely depends on grounding knowledge. Where an AI step relies on reference content (a product
list, a policy, category definitions), name that content and its owner, because a classification step is only as good
as the categories it is given.

## Security and privacy considerations

Note what data each step handles and where it would flow, especially personal data and data leaving the tenant. Steps
that move sensitive data between systems, or that would run under a shared or service identity, raise the risk tier
and bring `security-privacy` review forward.

## Responsible AI considerations

Flag any AI step whose output informs decisions about individuals (eligibility, priority, complaints, employment). These
need human review before effect and may need `responsible-ai:human-oversight` review from tier 3. Some steps should stay human; record
that as a decision, not a gap.

## Evaluation requirements

For each AI step, name the evidence needed before build is approved: a sample of real inputs with known correct outputs
and the accuracy the process owner would accept. If nobody can produce a sample of real inputs, the AI step is not ready.

## Value measures

Record baseline volume, handling time, cycle time and error or rework rate, with the source of each figure. The value
estimate is net of review and exception effort. The process owner owns the measures; `automation:automation-value`
tracks them after go-live.

## Scale notes

### Starter

Assess a few high-volume candidates in short workshops with the process owner, using one page per process. Favour
deterministic flows; add AI steps only where the case is clear.

### Scale

Run assessment as a standard step in the CoE intake for automation requests, with a shared classification table so
candidates from different teams are judged alike. Keep previous assessments as precedents.

### Enterprise

Federate first-pass assessment to business-unit automation teams using the same criteria, with the central team
reviewing anything with AI steps at tier 2 and above. Look across the portfolio for repeated steps that could become
shared components.

## Hand-offs

- To `automation:automation-process-design` when the process needs redesign or the assessment is approved.
- To `opportunity-management:risk-classification` to confirm the tier.
- To `opportunity-management:opportunity-prioritisation` when the candidate joins the backlog.
- To `automation:desktop-automation` where a step can only be done through a user interface.

## Reviewer gates

From risk tier 2, `design-authority:ai-necessity-challenge` may challenge the classification, particularly AI steps where a rule would do and
desktop flows where an API exists. The challenge and response are recorded on the assessment record.

## Failure modes

- AI is placed in steps a lookup or rule could handle, adding cost, variability and review effort for no gain.
- An unstable process is automated, and the flow breaks every time the team changes how it works.
- Value is estimated on time saved without subtracting review and exception handling, and the case collapses after go-live.
- Steps reliant on undocumented workarounds are missed in the walkthrough and become unhandled exceptions.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Classify a step as needing AI before asking whether a rule, lookup or better input would do.
- Recommend automating a process that has no owner for its exceptions.
- Estimate value without subtracting human review and exception effort.
- Assume a connector, API or licence exists without checking.

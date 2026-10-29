---
name: ai-non-functional-requirements
description: Specifies the non-functional requirements of an AI solution - quality thresholds, latency, availability, capacity, cost per use, resilience, observability, security, retention, accessibility and supportability - scaled to the risk tier, each measurable with an owner. Use when a solution moves from idea to design, when a pilot is about to become a service, or when nobody can say how good, fast or available the solution must be.
license: CC-BY-4.0
metadata:
  department: ai-architecture
  lifecycle: Envision, Deliver, Assure
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, power-platform, azure
  edition-support: starter, scale, enterprise
  reviewers: design-authority, evaluation-quality
  sources: ms-copilot-studio-guidance, ms-foundry-models, ms-copilot-privacy, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI non-functional requirements

## Purpose

Business owners describe what an AI solution should do; they rarely say how well, how fast, how often or at what cost.
This skill turns those unstated expectations into measurable non-functional requirements, scaled to the risk tier, so
design, evaluation and operations have targets to work to. AI adds requirements that ordinary systems lack, such as
answer quality thresholds, groundedness and cost per interaction. The work goes wrong when requirements are copied from
a generic template, when quality is left as "accurate", and when nobody owns the numbers.

## When to use

- A solution has an agreed purpose and platform and is moving into design.
- A pilot is about to become a supported service and needs targets.
- An operations team is asked to support a solution with no stated availability or response expectations.
- Users complain the solution is slow, wrong or unavailable and there is nothing to judge it against.
- A partner proposal needs requirements to be tested against.

## When not to use

- Engineering for latency and throughput once targets are set - use `ai-engineering:ai-performance-engineering`.
- Designing fallbacks and graceful degradation - use `ai-engineering:ai-resilience`.
- Defining quality rubrics and acceptance thresholds in detail - use `evaluation-quality:ai-quality-rubric`.
- Monitoring and alerting in operation - use `ai-operations:ai-solution-monitoring`.
- Managing model and platform cost in Foundry - use `ai-foundry:foundry-cost-management`.

## Questions to ask first

1. What happens to the business if the solution is wrong, slow or unavailable for an hour, a day or a week?
2. How many people will use it, when, and how quickly do they need an answer?
3. What level of answer quality would the business owner accept, and how would they judge it?
4. What is the budget for running it, and who pays as usage grows?
5. Who will support it, during which hours?

## Required inputs

- The solution brief, risk tier and platform decision.
- Expected users, usage pattern and growth, from the business owner.
- The organisation's standard service levels and accessibility standards, if any.
- Retention and logging requirements from security and privacy.

Where the business owner cannot give a figure, record the requirement as "to confirm" with the measure and the method to
set it, for example a baseline from the pilot. Never invent a target to fill the table.

## Decision framework

Set requirements in each category, with depth proportionate to the tier.

| Category | Tier 1 | Tier 2 | Tier 3 and 4 |
|---|---|---|---|
| Answer quality | Owner's informal acceptance on sample questions | Agreed threshold on an evaluation set | Threshold per scenario, including groundedness and refusal, tested in the pipeline |
| Latency | Acceptable to users in practice | Target for typical interactions | Targets by interaction type with headroom |
| Availability and support hours | Best effort | Stated hours and response route | Service level aligned to the business process, with continuity plan |
| Capacity and growth | Rough user count | Expected peak and growth | Load tested at peak with growth margin |
| Cost per use | Known order of magnitude | Budget and alert threshold | Cost model per interaction, with ceilings and owner |
| Resilience | User falls back to manual | Defined fallback | Tested fallback and degradation modes |
| Observability | Usage visible to owner | Errors and quality signals monitored | Traces, quality and safety signals with alerting |
| Security, privacy and retention | Approved sources and audience | Reviewed controls and retention | Full review, defined retention, audit trail |
| Accessibility and language | Organisation standard | Tested against standard | Tested with representative users |
| Supportability | Named owner | Owner, support route, runbook | Operating team, runbook, review calendar |

Each requirement has a measure, a target or "to confirm", a method of verification and an owner.

## Practitioner approach

Start with consequences rather than numbers. Ask the business owner what happens if the solution gives a wrong answer,
takes thirty seconds, or is down for a morning. The answers tell you which categories matter and how much. A knowledge
agent used occasionally can tolerate slowness; an agent in a contact centre call cannot.

Work through the categories in the decision framework and write each requirement as a testable statement: the measure,
the target and how it will be verified. "The agent should be accurate" becomes "on the agreed evaluation set, at least
the agreed share of answers are rated correct and grounded by the business owner's reviewers". Leave the number as "to
confirm" until the owner agrees it; a target agreed after seeing pilot results is better than one invented in design.

Pay particular attention to the AI-specific requirements. Quality needs a threshold and a set to measure it against,
built with `evaluation-quality`. Cost per use needs a model, because consumption costs grow with adoption and can
surprise budget holders; capture the drivers (interactions, model calls, tool calls, retrieval) and route licensing and
pricing questions to the Microsoft licensing guide or a licensing partner. Resilience needs a defined behaviour when the
model or a tool is unavailable, because users will otherwise retry and create duplicates.

Check feasibility with the platform. Some platforms limit what can be tuned or measured. If a requirement cannot be met
or verified on the chosen platform, raise it now with `ai-architecture:platform-selection`, rather than discovering it
at the release gate.

Assign an owner to every requirement and agree how it will be verified: in evaluation before release, in load testing,
or in monitoring after release. Requirements without verification are wishes.

Record the requirements on the template, share them with the build and operations teams, and revisit them at the first
post-release review, when real usage data can replace estimates.

## Outputs

- A non-functional requirements specification on the `non-functional-requirements` template: category, requirement, measure, target or "to confirm", verification method and owner.
- A list of requirements the chosen platform cannot meet or verify, for the design gate.
- Inputs to evaluation, monitoring and cost planning.

## Microsoft platform considerations

Platforms differ in what can be configured and observed: analytics in Copilot Studio, tracing and evaluation in
Microsoft Foundry, service levels for Microsoft 365 services. Platform limits, quotas and service levels change; check
`ms-copilot-studio-guidance` and `ms-foundry-models` and the current service documentation rather than stating figures.

## Adoption considerations

Users abandon slow or unreliable solutions quickly and rarely come back. Set latency and availability targets with
real users in mind and test them during the pilot.

## Knowledge considerations

Freshness is a non-functional requirement: state how quickly a change in source content must appear in answers, and
agree it with the knowledge owner.

## Security and privacy considerations

Include retention of prompts, responses and logs, audit trail and access requirements, agreed with the `security-privacy`
reviewers. Retention with legal effect is confirmed with the DPO or legal adviser.

## Responsible AI considerations

For solutions that inform decisions about people, add requirements for human review, explanation and logging, agreed
with the `responsible-ai` reviewers, and make them testable like any other requirement.

## Evaluation requirements

Every quality, safety and groundedness requirement maps to an evaluation test and threshold, built with
`evaluation-quality:ai-evaluation-strategy`. Every operational requirement maps to a monitoring signal.

## Value measures

Track, across the portfolio, solutions with complete requirements before build, requirements verified before release,
and incidents traced to unstated requirements. The AI solution architect owns these measures, with a baseline from
current solutions.

## Scale notes

### Starter

A single page covering quality, support, cost and retention is enough for most starter solutions. Avoid heavy
specifications for tier 1 agents.

### Scale

Use the template for all tier 2 solutions, with standard defaults per reference architecture so teams adjust rather
than start from blank.

### Enterprise

Align AI requirements with enterprise service management, including service levels, capacity management and cost
allocation, with tier 3 and 4 solutions load tested and continuity planned.

## Hand-offs

- To `evaluation-quality:ai-quality-rubric` for quality thresholds and evaluation sets.
- To `ai-engineering:ai-performance-engineering` and `ai-engineering:ai-resilience` for engineering to targets.
- To `ai-operations:ai-solution-monitoring` for operational signals.
- To `design-authority:ai-design-review` with the specification.

## Reviewer gates

From risk tier 2 the specification is reviewed by `design-authority` at the design gate and its quality requirements by
`evaluation-quality`. Requirements that cannot be verified are an advisory or blocking finding depending on tier.

## Failure modes

- Quality is written as "accurate", so nothing can fail evaluation and nothing can pass it.
- Cost per use is never modelled, and consumption costs exceed budget once adoption grows.
- A pilot with no support hours becomes business critical, and an outage has no route.
- Targets are copied from a generic template and nobody owns or verifies them.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Invent a target figure the business owner has not agreed.
- Leave a requirement without a measure, verification method and owner.
- State platform limits, prices or service levels from memory.
- Treat answer quality as a functional detail instead of a requirement with a threshold.

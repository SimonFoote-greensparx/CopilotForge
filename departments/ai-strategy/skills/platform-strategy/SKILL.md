---
name: platform-strategy
description: Sets the organisation's strategic position on the Microsoft AI platform mix - Copilot Chat, Microsoft 365 Copilot, agents, Copilot Cowork, Copilot Code, Copilot Studio and Microsoft Foundry - giving each a posture, audience, owner, entry criteria and sequence. Use when leaders ask which Microsoft AI platforms the organisation should offer and to whom, when teams adopt platforms ad hoc, or when Microsoft change prompts a rethink.
license: CC-BY-4.0
metadata:
  department: ai-strategy
  lifecycle: Envision, Mobilise, Scale
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-code, copilot-studio, ai-foundry, power-platform
  edition-support: starter, scale, enterprise
  reviewers: design-authority, security-privacy
  sources: ms-copilot-overview, ms-agents-extensibility, ms-agents-compare, ms-copilot-cowork-customise, ms-copilot-studio-zoned-governance, ms-foundry-models, ms-managed-environments
  status: draft
  authors: Simon Foote
---

# Platform strategy

## Purpose

This skill decides, at strategy level, which Microsoft AI platforms the organisation will offer, to whom, in what order
and under what conditions. It gives each platform a clear posture, from "available to everyone" to "not now", so that
individual solution decisions start from an agreed position rather than from whatever a team happens to try. Platform
strategy usually goes wrong by turning everything on because it is licensed, by blocking everything until a perfect
architecture exists, or by letting the platform mix be decided by whichever enthusiast builds first.

## When to use

- Leaders ask which Microsoft AI platforms the organisation should use and for which kinds of work.
- Teams are adopting Copilot Studio, Foundry or coding agents without any agreed position.
- The strategy and roadmap are being set and need a platform stance to sequence foundations.
- Microsoft has introduced, renamed or changed a platform and the current position may be out of date.
- Two parts of the organisation are building similar capabilities on different platforms.

## When not to use

- Choosing the platform for one specific solution - use `ai-architecture:platform-selection`.
- Deciding whether one framed problem needs AI and which pattern fits - use `opportunity-management:ai-suitability`.
- Designing environments, zones and routing for makers - use `platform-governance:ai-environment-strategy`.
- Licensing and capacity questions - use `platform-governance:ai-licensing-and-capacity`, which routes to the licensing guide or a partner.
- Reviewing whether a solution's platform choice conforms - use `design-authority:platform-fit-review`.

## Questions to ask first

1. Which strategic outcomes and ambition level must the platform mix support, and over what horizon?
2. What is already licensed, deployed and governed today, and where are people already building without a position?
3. What skills and support capacity exist for low-code makers and for professional engineers?
4. What constraints apply to data location, sensitivity, regulation or existing enterprise architecture standards?
5. Who owns each platform today, and who would own it under the operating model?

## Required inputs

- Strategic outcomes, ambition level and roadmap from `ai-strategy:strategic-outcomes`, `ai-strategy:ai-vision` and `ai-strategy:ai-roadmap`.
- The maturity assessment and operating model from `ai-strategy:ai-maturity-assessment` and `ai-strategy:ai-operating-model`.
- An inventory of current AI use and solutions, from `platform-governance:ai-solution-inventory` or an informal survey.
- The organisation's confirmed licensing position, from the licensing guide or a licensing partner.
- Enterprise architecture standards and security and data protection constraints.

Where the licensing position or inventory is missing, mark the affected postures as provisional. Never assume a
platform is available, licensed or generally released; check the current source records.

## Decision framework

Give every platform one posture. Each posture implies a governance zone, support model and owner.

| Posture | Meaning | Typical fit |
|---|---|---|
| Default | Available to the whole eligible workforce with baseline guidance | Copilot Chat, and Microsoft 365 Copilot for licensed roles |
| Enabled by role | Available to defined roles once readiness and learning are met | Copilot Cowork for roles with delegable multi-step work; Agent Builder for knowledge owners |
| Governed build | Available to approved makers in managed environments with a release route | Copilot Studio and Power Platform automation |
| Specialist | Used only by a professional team with engineering standards | Microsoft Foundry and Copilot Code for production software |
| Not now | Deliberately deferred, with the precondition that would change it | Any platform the organisation cannot yet own, govern or support |

Test each proposed posture against five questions. Does an outcome need it within the horizon? Can the organisation
own and support it? Can governance cover it at the risk tiers expected? Is the skills base there or funded? Does it
duplicate a capability already offered? A platform that fails two or more stays at "not now" or "specialist".

Set build-route principles alongside the postures: prefer configuration over build, prefer the simplest rung that
works (as in `opportunity-management:ai-suitability`), reuse before creating, and move up to engineered solutions only
with evidence.

## Practitioner approach

Start with outcomes and current reality. List what the outcomes need: everyday assistance, delegated multi-step work,
knowledge agents, workflow agents with actions, production software or specialist model work. Then list what is
already happening. Almost every organisation discovers more building than it expected, and the strategy has to absorb
that rather than pretend it is not there.

Work through the platforms as layers rather than products. The everyday layer (Copilot Chat and Copilot in the apps)
is where most value for most people sits, so its posture is usually "default", with work context readiness and safe
use guidance as preconditions. The delegation layer (Copilot Cowork) suits roles with bounded multi-step work and needs
clear checkpoint habits. The agent layer spans declarative agents built by knowledge owners and Copilot Studio agents
built by makers; it needs owners, environments and a release route before it opens. The engineering layer (Foundry,
Copilot Code) needs professional teams, evaluation and operations capability.

Decide postures in a working session with the AI strategy lead, the platform owners, the security lead and an
enterprise architect, then test them with business representatives. Record the reasoning for every posture, especially
"not now", and name the precondition that would change it. A "not now" without a precondition becomes a permanent no
by accident.

Sequence the postures with the roadmap. Opening a build platform before its owner, environments and release policy
exist creates unowned solutions that are expensive to retire. Opening the engineering layer before the agent layer
works is rarely justified unless a specific outcome demands it.

Name an owner for each platform and agree the support route. Hand environment and policy design to
`platform-governance:ai-environment-strategy` and reference patterns to `ai-architecture:ai-reference-architecture`.

Microsoft changes names, packaging and capability frequently. Keep the strategy framed in capability layers so it
survives renames, check current naming and availability against the source records, and schedule a review through
`ai-strategy:strategy-refresh`. Licensing is never decided here; record the confirmed position and its source.

## Outputs

- A platform position statement: each platform with posture, audience, owner, governance zone, preconditions, reasoning and review date.
- Build-route principles that solution-level decisions must follow.
- A platform sequence aligned with the roadmap horizons.
- A list of provisional positions and open questions, including any awaiting licensing confirmation.

## Microsoft platform considerations

This skill is the platform consideration at strategy level. Copilot Chat and Microsoft 365 Copilot use work context
under existing permissions; agents extend them through declarative or custom engine patterns; Copilot Studio agents run
in Power Platform environments where data policies and managed environment controls apply; Foundry offers a model
catalogue including third-party models available through Microsoft. Availability, licensing, limits, preview status and
naming change often, so confirm every assumption against `references/sources.md`.

## Adoption considerations

Each posture implies a learning and support offer. "Default" platforms need workforce-wide guidance; "enabled by role"
platforms need role-based learning and Champions. Agree these with the adoption lead before a posture is published, so
access never arrives without help.

## Knowledge considerations

Agent and Cowork postures depend on owned, current knowledge and well-managed permissions. Where knowledge readiness is
low, keep agent building narrow until knowledge owners exist, and record it as a precondition.

## Security and privacy considerations

Each posture must state the minimum controls: identity, data policies, labelling, environment zoning and monitoring.
The `security-privacy` department confirms the controls are achievable before a platform moves beyond "not now", and
the data protection officer advises on data location and personal data.

## Responsible AI considerations

Platforms that allow autonomous actions, external exposure or decisions about people need oversight capability before
they open. Link the posture to the risk tiers so that higher-tier work can only happen on platforms where evaluation
and human oversight can be provided.

## Evaluation requirements

Postures of "governed build" and "specialist" require an evaluation capability to exist before release. Confirm the
evaluation approach with the `evaluation-quality` department and record it as a precondition.

## Value measures

Measure the strategy by the share of solutions built on the agreed posture, duplicated capabilities retired, time from
idea to release on each platform, and outcome progress attributable to each layer. The AI strategy lead owns the
measures; report at team or unit level, never individual.

## Scale notes

### Starter

Most platforms sit at "default" (everyday Copilot) or "not now", with perhaps Agent Builder enabled for a few knowledge
owners. Rely on a partner for any specialist work.

### Scale

Copilot Studio opens as a governed build platform with managed environments; Cowork is enabled by role; Foundry is
specialist with a small engineering team or partner.

### Enterprise

Postures are set centrally with business-unit variations recorded as exceptions. Each layer has a platform owner,
reference architecture and capacity plan, reviewed with the enterprise architecture cycle.

## Hand-offs

- To `platform-governance:ai-environment-strategy` to design environments and zones for each posture.
- To `ai-architecture:ai-reference-architecture` to publish the patterns for each layer.
- To `ai-strategy:ai-roadmap` to sequence the platform foundations.
- To `ai-architecture:platform-selection` for individual solution decisions within the postures.

## Reviewer gates

From the outset, `design-authority` reviews the postures for coherence with enterprise architecture, and
`security-privacy` confirms the minimum controls for any platform moving beyond "not now". Blocking findings are
resolved before the posture is published.

## Failure modes

- Every licensed platform is switched on at once, and unowned agents multiply faster than governance can register them.
- Everything stays blocked pending a perfect architecture, and shadow use grows on unmanaged tools.
- The strategy is written around current product names and is obsolete after the next rename.
- Engineered solutions are funded before the agent layer works, and simple needs get expensive answers.
- "Not now" postures carry no preconditions and are never revisited.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- State licensing conclusions or entitlements; route them to the Microsoft licensing guide or a licensing partner.
- Open a build platform before it has an owner, environments and a release route.
- Assert a platform's availability, limits or preview status from memory.
- Include non-Microsoft AI products in the platform mix.

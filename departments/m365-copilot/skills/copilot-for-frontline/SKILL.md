---
name: copilot-for-frontline
description: Assesses, scenario by scenario, whether Copilot use is feasible and safe for a frontline role - shared-device sign-in, connectivity, the mobile surface, the currency of procedures it would answer from and safety-critical limits - and records a constrained scenario set and safety boundary. Use when a frontline scenario is proposed, when safety-critical or regulated procedures are involved, or when shared or personal devices are in play.
license: CC-BY-4.0
metadata:
  department: m365-copilot
  lifecycle: Envision, Enable
  maturity: adopter, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: copilot-chat, m365-copilot, m365-agents, entra
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, responsible-ai
  sources: ms-copilot-overview, ms-copilot-privacy, ms-copilot-adoption-hub, ms-agent-builder
  status: draft
  authors: Simon Foote
---

# Copilot for frontline

## Purpose

Frontline workers in stores, sites, depots, wards and vehicles rarely sit at a desk with a mailbox full of documents,
so most desk-worker Copilot scenarios do not translate. This skill works out which Copilot scenarios are feasible and
safe for frontline roles, given how they actually work: on mobile or shared devices, between tasks, often with patchy
connectivity, sometimes in another language, and close to procedures where a wrong answer could hurt someone. It goes
wrong when desk scenarios are pushed to the frontline unchanged, or when an AI answer replaces a safety procedure that
must be followed exactly.

## When to use

- Frontline or deskless roles are being considered for Copilot Chat, licensed Copilot or agents.
- Scenarios designed for desk workers are failing in frontline settings.
- Frontline staff want quick answers about procedures, policies or rotas, and some procedures are safety-critical.
- Shared devices, kiosks or personal devices are part of the frontline estate.

## When not to use

- Designing how frontline staff are reached, trained and supported through the adoption programme - use `copilot-adoption:frontline-enablement`.
- Segmenting the workforce into personas across the organisation - use `copilot-adoption:audience-segmentation`.
- Designing a frontline knowledge agent once it is warranted - use `m365-agents:agent-use-case-design`.
- Licence types and entitlements for frontline workers - use `platform-governance:ai-licensing-and-capacity`, which ends with the Microsoft licensing guide or a licensing partner.
- Tenant-wide prerequisites and settings - use `m365-copilot:copilot-technical-readiness`.

## Questions to ask first

1. Which frontline roles are in scope, and what does a shift look like: devices, breaks, connectivity, noise, gloves, language?
2. Do workers have their own work identity and device, share devices, or use personal devices, and what is the policy for each?
3. What information do they look for most during a shift, and where does it come from today?
4. Which tasks or procedures are safety-critical, regulated or must be followed exactly?
5. What have employee representatives, works councils or unions been told, and are working-time or device policies affected?

## Required inputs

- A description of each frontline role's shift, device and connectivity pattern, gathered on site.
- The identity and device position for frontline workers, from IT.
- The procedures, policies and reference content frontline workers rely on, with owners.
- The list of safety-critical and regulated procedures, from the operations or safety lead.
- Any consultation requirements, from HR.

If identity or device arrangements are unclear, the feasibility verdict is "to confirm". Never assume frontline workers
have the same access, licences or devices as desk workers.

## Decision framework

Classify each candidate scenario.

| Scenario type | Feasible when | Constraint |
|---|---|---|
| Drafting short messages, handovers or reports | Worker has a personal work identity on a managed or approved device | Keep inputs short; voice input only where policy allows |
| Answering policy and HR questions (leave, pay rules, rotas) | Content is owned, current and available to frontline workers; an agent may fit better | Answers cite the source; sensitive personal matters go to a person |
| Looking up operational procedures | Content is owned and current, and the procedure is not safety-critical | Show the source document; the document remains authoritative |
| Safety-critical or regulated procedures | Not a Copilot answer; link to the controlled document | AI may help find the document, never paraphrase the steps to follow |
| Translation and simplification of communications | Organisation approves its use and a check route exists | Critical communications are checked by a fluent reviewer |
| Shared-device use | Sign-in and sign-out are reliable and enforced | No scenario where a previous user's content could be exposed |

## Practitioner approach

Go to the frontline. Spend a shift, or part of one, with each role in scope. Watch when people have a moment to look
something up, on what device, and what they look for. Ask what they do when they cannot find an answer: ask a
supervisor, phone a helpline, guess. That observation decides feasibility far better than a requirements workshop held
in head office.

Settle identity and devices next, with IT. Copilot works for a signed-in person, so frontline workers need a work
identity and a device arrangement that keeps one person's content away from the next. Shared devices need reliable
sign-out; personal devices need the organisation's policy. Where this cannot be made safe, the scenario is not feasible
yet, however valuable it looks.

Most frontline value comes from fast, reliable answers to recurring questions, grounded in owned content: procedures,
policies, product information, rota rules. That is often better served by an agent with curated knowledge than by
general Copilot use, because an agent can be scoped, tested and owned. Pass strong candidates to
`m365-agents:agent-opportunity-assessment` with the questions you collected on site.

Draw a hard line around safety-critical and regulated procedures. Copilot can help someone find the controlled document,
but the worker follows the document, not a summary of it. Agree this with the safety or operations lead and write it
into the scenario set and the guidance.

Design for the constraints you saw: short prompts, mobile-friendly outputs, plain language, the languages people work in,
and scenarios that fit in a two-minute gap. Test with real workers on their real devices before anything is published.

Involve employee representatives early where the organisation has them. Questions about working time, device use,
monitoring and job impact are legitimate and best answered before rollout, with HR.

## Outputs

- A frontline feasibility record per role: shift pattern, identity and device position, scenarios assessed, verdicts and constraints.
- A frontline scenario set recorded in the `scenario-catalogue`, each with constraints, sources and a check route.
- A safety boundary statement agreed with the operations or safety lead.
- Agent candidates passed for assessment, with the questions collected on site.

## Microsoft platform considerations

Frontline access depends on identity in Microsoft Entra, device management, the Teams mobile experience and the Copilot
experiences the organisation provides to frontline roles. Which Copilot experiences, agent options and licence types
suit frontline workers changes often; check `ms-copilot-overview`, `ms-agent-builder` and the licensing route rather than
assuming. Shared-device behaviour must be confirmed with IT on real devices.

## Adoption considerations

Frontline staff are reached through supervisors, shift briefings, team huddles and the apps they already use, not email
campaigns. Hand the scenario set to `copilot-adoption:frontline-enablement` so enablement fits shift patterns and
languages, and ensure frontline voices shape the scenarios.

## Knowledge considerations

Frontline answers are only as good as the procedures and policies behind them, which are often out of date or exist in
several versions. Name each source and its owner, and route clean-up to the `knowledge-management` department before any
agent is built on it.

## Security and privacy considerations

Shared devices, personal devices and personal data in rota or HR questions are the main risks. Confirm sign-out,
device policy and content access with IT, and route open questions to `security-privacy` and the data protection lead.

## Responsible AI considerations

Safety-critical procedures are never replaced by AI answers. Any scenario that could influence decisions about workers'
shifts, pay or conduct is referred to `responsible-ai`. Workers must know when they are using AI and where to go when an
answer looks wrong.

## Evaluation requirements

Test each scenario on site with real workers and devices, recording whether answers were correct, fast enough and
usable. For procedure lookups, confirm the cited source is the current controlled version.

## Value measures

Measure at role or site level: time to find answers, calls to helplines or supervisors for routine questions, and
errors linked to out-of-date information, against a baseline taken before rollout. The operations lead for the role owns
these measures.

## Scale notes

### Starter

One frontline role at one or two sites, a handful of scenarios, and a clear safety boundary statement.

### Scale

Several roles across sites, with an agreed device and identity pattern and knowledge owners for frontline content.

### Enterprise

Standard frontline patterns across business units and countries, localised for language and law, with consultation
built into the rollout plan.

## Hand-offs

- To `copilot-adoption:frontline-enablement` for reaching and supporting frontline workers.
- To `m365-agents:agent-opportunity-assessment` for frontline knowledge agent candidates.
- To `m365-copilot:copilot-technical-readiness` for device and identity prerequisites.
- To `knowledge-management:knowledge-readiness-assessment` for frontline content.

## Reviewer gates

From risk tier 2, frontline scenarios near safety-critical procedures or decisions about workers are reviewed by
`responsible-ai`, and shared or personal device arrangements by `security-privacy`; each finding is blocking or
advisory, and blocking findings stop the affected scenarios.

## Failure modes

- Desk scenarios are pushed to the frontline and fail on mobile devices during short breaks.
- A worker follows an AI summary of a safety procedure that omitted a step.
- Shared devices expose one worker's content to the next.
- Frontline content is out of date, so answers are confidently wrong and trust collapses.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Let an AI answer replace a safety-critical or regulated procedure.
- Assume frontline workers have the same identity, devices or licences as desk workers.
- Publish a frontline scenario without testing it on real devices with real workers.
- State frontline licence entitlements; route them to the licensing guide or a partner.

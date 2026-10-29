---
name: ai-continuity
description: Plans business continuity for work that depends on AI - impact of unavailability or forced switch-off, fallback to manual or simpler routes, decision rights for suspending a solution, user communications, preserving the skills and procedures people need without AI, and exit routes when a model or feature is withdrawn. Use when a solution becomes business-critical, before tier 3 release, or when a model or feature deprecation is announced.
license: CC-BY-4.0
metadata:
  department: ai-operations
  lifecycle: Deliver, Launch, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 2, 3, 4
  platforms: m365-agents, copilot-studio, copilot-cowork, ai-foundry, power-platform, azure
  edition-support: scale, enterprise
  reviewers: design-authority
  sources: ms-foundry-models, ms-copilot-studio-guidance, ms-managed-environments, nist-ai-rmf, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# AI continuity

## Purpose

When work comes to depend on an AI solution, the organisation needs to know what happens when it is unavailable, must
be switched off after an incident, or loses a model or feature it relies on. This skill plans continuity for that work:
the business impact of losing the solution for different periods, the fallback route people use instead, who decides to
suspend it, how users are told, how the skills and procedures needed without AI are kept alive, and how the solution
would move if a model or feature were withdrawn. Continuity usually fails because the old process was dismantled when
the solution went live, so there is nothing to fall back to, or because nobody has the authority to switch off a
popular solution when it misbehaves.

## When to use

- A solution has become business-critical or is about to be released at tier 3 or 4.
- A process has been redesigned around an AI solution and the old route is being retired.
- Microsoft announces a model retirement, feature change or deprecation affecting a live solution.
- An incident showed that switching a solution off would stop important work.
- Business continuity planning asks which processes depend on AI.

## When not to use

- Technical resilience, retries, failover and graceful degradation inside a solution - use `ai-engineering:ai-resilience`.
- Responding to a live incident - use `ai-operations:ai-incident-management`.
- Choosing a replacement model for a task - use `ai-foundry:model-selection`.
- Retiring a solution permanently - use `ai-operations:ai-solution-retirement`.
- Non-functional requirements such as availability targets at design time - use `ai-architecture:ai-non-functional-requirements`.

## Questions to ask first

1. What work stops, slows or becomes riskier if the solution is unavailable for an hour, a day or a week?
2. What would people do instead today, and could they still do it?
3. Who has authority to suspend the solution, including outside working hours?
4. Which models, features, connectors and services does the solution depend on, and which are outside the organisation's control?
5. How would users be told, and how quickly?

## Required inputs

- The solution's risk tier, process maps and the work it supports.
- Dependencies from the runbook: models, routes, connectors, knowledge, environments and licences in use.
- The organisation's business continuity plans and impact categories.
- Platform change and deprecation notices the organisation tracks.

Where the business impact is unknown, run a short impact conversation with the business owner before planning
fallbacks; never assume the solution is non-critical because it is new.

## Decision framework

Rate the impact of losing the solution and choose the fallback accordingly.

| Impact of a day without the solution | Fallback required | Test |
|---|---|---|
| Inconvenience; work continues more slowly | Documented manual route, users told where to find it | Walk-through once a year |
| Material delay or backlog; recoverable | Manual route with named owners, capacity plan for backlog, user communications ready | Walk-through each review cycle |
| Critical process stops or risk rises | Tested alternative route (manual, simpler automation or degraded mode), decision rights including out of hours, communications templates | Exercise at least annually and after major change |

Suspension decision rights:

| Situation | Who decides |
|---|---|
| Harm or exposure continuing | Incident lead, immediately, without waiting for the business owner |
| Quality below threshold without harm | Business owner, advised by solution owner |
| Platform or model withdrawal | Business owner with platform team, on a planned timeline |

Exit readiness for platform dependencies: record each external dependency, its notice route, the alternative and the
lead time to switch.

## Practitioner approach

Start with the work, not the technology. Ask the business owner to describe a day when the solution is unavailable.
What stops, who notices, what backs up, and when does it start to matter? Repeat for a week. This impact view sets
everything else; a drafting assistant for a team can tolerate a day's outage, while an agent triaging customer requests
may not tolerate an hour.

Keep the fallback alive. When a process is redesigned around AI, the old route is often dismantled - the shared mailbox
closed, the procedure archived, the people redeployed. Decide deliberately what must remain: a simple procedure, a
queue, a template, a contact. Write the fallback into the runbook and tell users where it is.

Protect the skills people need without AI. Where staff now rely on the solution for judgement-heavy work, make sure they
can still do the work manually at an acceptable standard. That might mean periodic practice, retained reference guides
or a small group who keep doing some work manually. Discuss this with the business owner and learning lead; it is a
real risk for long-running solutions.

Settle decision rights before they are needed. The incident lead must be able to suspend a solution immediately when
harm is continuing, without negotiating with a business owner who values it. Write this down and make sure the platform
team knows who may ask for a switch-off.

Prepare communications. Draft short messages for suspension and return: what has happened, what to do instead, when
users will hear more. Pre-agreed wording saves hours during an incident.

Plan for dependencies you do not control. Models are retired, features change and previews end. For each external
dependency, record how the organisation will hear of changes, what the alternative is and how long switching would
take, and confirm the current position in the source records. Treat a deprecation notice as a planned change with
its own evaluation, not an emergency.

Test the plan in proportion. For critical solutions, rehearse a suspension: switch off in a test environment or tabletop
the decision, use the fallback for a period and measure what happens. Fix what the exercise reveals and record it.

## Outputs

- A continuity section in the `support-and-monitoring-plan`: impact rating, fallback route, decision rights, communications templates and dependency exit notes.
- A fallback procedure stored with the runbook and visible to users.
- An exercise record for critical solutions, with findings and actions.
- A dependency register with notice routes, alternatives and switch lead times.

## Microsoft platform considerations

Model lifecycles, feature availability and deprecation notices differ across Microsoft Foundry, Copilot Studio and
Microsoft 365 agents, and change over time. Track the notices the organisation relies on, and confirm current model
lifecycle and environment options in `ms-foundry-models`, `ms-copilot-studio-guidance` and `ms-managed-environments`.
Service availability commitments and licensing terms are not asserted here; check the current Microsoft documentation
or a licensing partner.

## Adoption considerations

Tell users that a fallback exists and where it is. Knowing they can still work if the solution is unavailable reduces
anxiety about depending on it, and avoids panic when it is suspended.

## Knowledge considerations

Fallback procedures are knowledge too. Give them an owner and a review cycle, and keep them out of reach of the solution
itself if they would confuse its grounding.

## Security and privacy considerations

Fallback routes must keep the same data protections as the solution. A manual workaround that emails sensitive data to
personal mailboxes is not an acceptable fallback; agree fallbacks with the `security-privacy` reviewers for tier 3 and 4.

## Responsible AI considerations

Where the solution supports decisions about people, the fallback must preserve human oversight and fair treatment.
Deskilling of the people who provide oversight is a responsible AI risk to raise with `responsible-ai:human-oversight`.

## Evaluation requirements

A move to a replacement model or feature is a material change and goes through `evaluation-quality:regression-evaluation`
with the full golden dataset before it reaches users.

## Value measures

Track the share of tier 3 and 4 solutions with a tested fallback, time to suspend and to restore in exercises, and
deprecations handled on a planned timeline rather than as emergencies. The AI Operations Lead owns these measures,
reported by solution.

## Scale notes

### Starter

Most starter-scale solutions are tier 1 or 2; a one-paragraph fallback in the runbook and a named person who can switch
the agent off are enough.

### Scale

Continuity sections in every tier 2 and higher support plan, decision rights agreed with the CoE, and walk-throughs at
scheduled reviews.

### Enterprise

AI dependencies included in enterprise business continuity planning, annual exercises for critical solutions, a
central dependency register and planned responses to platform deprecations across the portfolio.

## Hand-offs

- To `ai-engineering:ai-resilience` for technical fallbacks and degraded modes.
- To `ai-operations:ai-incident-management` with suspension decision rights and communications.
- To `evaluation-quality:regression-evaluation` before any switch to a replacement model or feature.
- To `ai-operations:ai-review-calendar` to review the plan at scheduled reviews.

## Reviewer gates

From risk tier 3, `design-authority` checks the continuity plan as part of `design-authority:supportability-review`,
looking for a tested fallback, decision rights and dependency exit notes. Missing fallbacks for critical processes are
blocking at that gate.

## Failure modes

- The old process was dismantled at go-live, so an outage stops the work entirely.
- Nobody may switch off a popular solution without the business owner, and harm continues while they are unreachable.
- Staff lose the ability to do the work without AI, and quality collapses during a long outage.
- A model retirement notice is missed, and the solution breaks on the retirement date.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Release a business-critical AI solution with no fallback route for the work.
- Require business owner approval before suspending a solution that is causing continuing harm.
- Assert service availability commitments or licensing terms from memory.
- Treat a replacement model as a like-for-like swap without regression evaluation.

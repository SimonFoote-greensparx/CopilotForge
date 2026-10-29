---
name: ai-incident-management
description: Runs incident management for AI failures and harms in live solutions - recognising AI incident types, setting severity, containing fast, preserving evidence, communicating, involving security, privacy and legal roles, and post-incident review before return to service. Use when an agent gives harmful, exposing or widely wrong outputs, takes a wrong action, or when AI incident procedures are being prepared.
license: CC-BY-4.0
metadata:
  department: ai-operations
  lifecycle: Launch, Measure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-copilot, m365-agents, copilot-studio, copilot-cowork, ai-foundry, power-platform
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, responsible-ai
  sources: nist-ai-rmf, ico-ai-data-protection, ms-copilot-studio-security-governance, ms-managed-environments, ms-copilot-privacy, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# AI incident management

## Purpose

AI incidents rarely look like outages. The solution is up and answering - but it is telling staff the wrong leave
entitlement, summarising a confidential file for the wrong audience, sending customers an unapproved commitment or
responding badly to someone in distress. This skill gives operations a way to recognise AI incidents, set their
severity, contain them quickly with the levers each route offers, preserve evidence, bring in the right specialists and
learn from them before returning the solution to service. Incident handling goes wrong when a harmful output is logged
as an ordinary fault, when nobody knows how to switch a solution off, or when the solution goes back live with no proof
the cause was fixed.

## When to use

- A live solution produces harmful, offensive, exposing or widely wrong outputs, or takes a wrong action.
- A monitoring trigger or user report suggests one of those may be happening.
- The organisation is preparing incident procedures for AI solutions before go-live.
- A post-incident review is needed after an AI-related event.

## When not to use

- Reviewing whether the organisation is ready to handle AI security and privacy incidents - use `security-privacy:ai-incident-readiness`.
- Routine wrong answers handled through normal support - use `ai-operations:ai-support-model`.
- Planned fallback when an AI service is unavailable - use `ai-operations:ai-continuity`.
- Routes for affected people to challenge an outcome - use `responsible-ai:escalation-and-appeal`.
- Deciding whether to retire a solution after repeated incidents - use `ai-operations:ai-solution-retirement` after the review.

## Questions to ask first

1. What happened, to whom, and is it still happening?
2. Could restricted or personal data have been exposed, or could people have been harmed or treated unfairly?
3. Did the solution act in another system or communicate outside the organisation?
4. What is the fastest safe containment - restrict sharing, disable an action, remove a knowledge source or switch the solution off?
5. Who must be told now - solution owner, security, DPO, legal, HR, communications, the accountable executive?

## Required inputs

- The solution's runbook with containment steps and owners, from `ai-operations:ai-support-model`.
- The organisation's existing incident, security incident and personal data breach procedures.
- Contacts for security, the DPO, legal and HR, and the accountable executive for the solution.
- Access to logs, transcripts or monitoring data that are retained for the solution.

Where a solution has no documented way to switch it off or restrict it, record that as a gap and find the route with
the platform team immediately; containment comes before diagnosis.

## Decision framework

Classify the incident type and set severity by the highest applicable factor.

| Type | Examples |
|---|---|
| Harmful output | Offensive, dangerous or distressing content; poor handling of distress |
| Data exposure | Restricted, personal or confidential content shown to people not entitled to it |
| Wrong action | Records changed, messages sent or commitments made wrongly |
| Widespread wrong answers | Material errors on a topic many users rely on, such as policy, pay or safety |
| Misuse | The solution used for a purpose it was not approved for |
| Unavailability with business impact | Handled with `ai-operations:ai-continuity`, escalated here if harm results |

| Severity | When | Expected response |
|---|---|---|
| Critical | External harm, safety risk, personal data exposure, or wrong actions at scale | Contain immediately; incident lead, security and DPO engaged; accountable executive informed |
| High | Internal harm or exposure to a limited group, or material wrong answers on a high-consequence topic | Contain the same working day; specialists engaged as relevant |
| Moderate | Wrong answers or failed actions with limited impact, no exposure or harm | Fix through support with an incident record |
| Low | Isolated issue with no impact | Handle through support; note for review |

Containment levers, fastest first: restrict sharing to a smaller group; disable a specific action or connector; remove or
restrict a knowledge source; show a warning to users; switch the solution off. Choose the least disruptive lever that
stops the harm.

## Practitioner approach

Contain first. When a credible report arrives, the incident lead's first question is whether harm is continuing. If it
is, pull the fastest lever that stops it, even before the cause is known. Switching off a well-used agent for an
afternoon is a small cost against continued exposure or harm. Record what was done and when.

Preserve evidence before it disappears. Capture the user's report, screenshots, the question and answer, the time, the
solution configuration version and any logs or transcripts that are retained. Retention varies by route and
configuration, so check what exists and secure it quickly within the organisation's policy.

Bring in the right people by type. Data exposure goes to the security and privacy teams under the organisation's breach
procedure; the DPO decides whether any notification is needed. Harm to people goes to HR or the relevant owner and to
the responsible AI lead. Wrong external communications go to communications and legal. The incident lead coordinates;
the specialists decide in their areas.

Diagnose the cause with the solution owner and maker: knowledge (a superseded or overshared source), instructions,
configuration (a setting changed, web grounding enabled), an action or connector, a platform or model change, or misuse.
Many incidents have more than one cause. Check whether other solutions share the same cause, such as the same
overshared library.

Communicate plainly. Tell affected users what happened, what they should do (for example, disregard an earlier answer)
and when the solution will return. Do not speculate in communications, and agree wording with legal or communications
for critical incidents.

Return to service only with evidence. Fix the cause, re-run the affected items and the regression subset through
`evaluation-quality:regression-evaluation`, add the incident's prompt pattern to the golden dataset, and get the
business owner's agreement. For critical incidents, the relevant reviewers confirm the fix.

Review without blame. Within a short period, hold a post-incident review covering timeline, causes, what worked, what
did not and actions with owners. Focus on systems and decisions, never on individual fault. Share lessons with other
solution owners and feed patterns into the review calendar.

## Outputs

- An incident record: type, severity, timeline, containment, evidence, specialists engaged, communications, cause, fix and return-to-service evidence.
- A post-incident review with actions, owners and dates.
- New regression items for `evaluation-quality:golden-dataset`.
- An AI incident procedure and severity matrix for the organisation, with containment levers per route recorded in each solution's `support-and-monitoring-plan`.

## Microsoft platform considerations

The levers for containment differ by route: sharing and availability settings for agents, environment and data policy
controls in Power Platform, and deployment controls in Microsoft Foundry. Confirm current controls in
`ms-copilot-studio-security-governance` and `ms-managed-environments`, and confirm what interaction data is retained
and how it can be accessed in `ms-copilot-privacy`. Practise the switch-off route before go-live.

## Adoption considerations

How an incident is handled shapes trust more than the incident itself. Prompt, plain communication and a visible fix
keep users; silence drives them to unapproved tools.

## Knowledge considerations

Many incidents trace to knowledge: overshared libraries, superseded policies, inappropriate content in grounding.
Fix the source, and check whether other solutions use it.

## Security and privacy considerations

Data exposure incidents follow the organisation's security incident and personal data breach procedures, led by the
security team and the DPO, who decide on any notification. Readiness for these is reviewed through
`security-privacy:ai-incident-readiness`.

## Responsible AI considerations

Incidents that harm people or treat them unfairly are reported to the `responsible-ai` reviewers and may require
contacting affected people through `responsible-ai:escalation-and-appeal`. Repeated harm may mean the use should stop.

## Evaluation requirements

Return to service requires re-running the affected items and the regression subset with results at or above threshold,
and adding the incident pattern to the golden dataset.

## Value measures

Track incidents by type and severity per solution, time to containment, time to return to service, and the share of
post-incident actions closed on time. The AI Operations Lead owns these measures; report by solution, never by
individual maker or user.

## Scale notes

### Starter

A one-page AI incident procedure: how to report, who decides, how to switch each agent off, and who to call for data
exposure. Practise the switch-off once before go-live.

### Scale

AI incident types and severities added to the service management process, containment steps in each runbook, and
post-incident reviews shared across solution owners.

### Enterprise

AI incidents integrated with security and enterprise incident management, rehearsed scenarios for tier 3 and 4
solutions, portfolio-level trend analysis and lessons fed into standards and reviewer criteria.

## Hand-offs

- To `evaluation-quality:regression-evaluation` before return to service.
- To `security-privacy:ai-incident-readiness` with lessons that change readiness.
- To `ai-operations:ai-review-calendar` with incident patterns for scheduled reviews.
- To `ai-operations:ai-solution-retirement` when the review recommends retirement.

## Reviewer gates

From risk tier 2, `security-privacy` confirms the fix for exposure incidents and `responsible-ai` confirms the fix for
harm-to-people incidents before return to service. Not applicable as a release gate otherwise; the incident procedure
itself is reviewed through `security-privacy:ai-incident-readiness`.

## Failure modes

- A harmful output is logged as an ordinary fault and closed with a note to the maker.
- Nobody knows how to switch the solution off, and harm continues while people search for the setting.
- Evidence is lost because transcripts were not secured before retention removed them.
- The solution returns to service with an instruction patch and no regression run.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Delay containment of continuing harm to finish diagnosis.
- Decide on personal data breach notification without the DPO.
- Return a solution to service without re-running affected items and the regression subset.
- Run a post-incident review that assigns blame to individuals.

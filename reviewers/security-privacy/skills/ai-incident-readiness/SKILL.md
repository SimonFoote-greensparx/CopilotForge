---
name: ai-incident-readiness
description: Checks before release that an AI solution's security and privacy incidents can be detected, contained, investigated and reported - signals, a tested way to switch the solution off, evidence available to investigators, responders who understand AI failure modes and a route to the DPO - classifying each gap as blocking or advisory. Use when a solution reaches its security gate, before widening its audience, or after an incident exposed gaps.
license: CC-BY-4.0
metadata:
  department: security-privacy
  lifecycle: Assure, Launch, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 2, 3, 4
  platforms: m365-copilot, m365-agents, copilot-studio, ai-foundry, power-platform, purview, entra, azure
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-studio-security-governance, ms-managed-environments, ms-copilot-privacy, ico-ai-data-protection, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI incident readiness

## Purpose

AI incidents look different from ordinary security incidents. A prompt injection leaves no malware, an oversharing leak
looks like a normal answer, and an agent sending the wrong data runs under a legitimate identity. If the organisation
first thinks about response when a user posts a screenshot, it will lose hours working out how to switch the agent off,
whose identity acted and where the transcripts are. This reviewer skill checks, before release, that a solution's
security and privacy incidents can be detected, contained, investigated and reported, and classifies each gap as
blocking or advisory. It goes wrong when readiness is assumed because the organisation has a general incident process
that has never met an AI solution.

## When to use

- An AI solution at risk tier 2 or above reaches its `security-privacy` gate.
- The solution's audience is about to widen, especially to customers or the public.
- A solution gains actions, autonomy or access to personal or regulated data.
- An incident or near miss revealed that responders could not act quickly.
- The security operations or service desk team asks how to handle AI-related reports.

## When not to use

- Running live incident management for AI failures, quality problems and harms in operation - use `ai-operations:ai-incident-management`.
- Planning continuity and fallback when AI is unavailable - use `ai-operations:ai-continuity`.
- Designing routes for affected people to challenge an AI-influenced outcome - use `responsible-ai:escalation-and-appeal`.
- Testing whether the solution can be manipulated in the first place - use `security-privacy:ai-security-testing`.

## Questions to ask first

1. What security or privacy incidents are plausible for this solution - data leak, injection-driven action, account misuse, exposed transcripts, a supplier breach?
2. How would the organisation find out - monitoring signals, user reports, supplier notice - and who receives them?
3. How fast can the solution, or one of its tools or connections, be switched off, and who is allowed to do it?
4. What evidence will investigators need - interaction records, audit logs, identity sign-ins, tool calls - and is it kept long enough?
5. Who decides whether a personal data breach must be reported, and how does the case reach them?

## Required inputs

- The solution design, risk tier, owners and support route.
- The identity map from `security-privacy:ai-identity-and-access-review` and the record map from `security-privacy:ai-interaction-retention`.
- Attack patterns found in `security-privacy:ai-security-testing`.
- The organisation's incident response and personal data breach procedures.

Where the organisation's breach procedure does not mention AI, record an advisory finding for its owner; where nobody
can switch the solution off, record a blocking finding. Never decide on the organisation's behalf whether a breach is
reportable; that is the DPO's call.

## Decision framework

Classify every gap. From risk tier 2 a blocking gap stops release and is not traded against dates.

| Readiness area | Blocking when | Advisory when | Typical fix |
|---|---|---|---|
| Detection | No signal or reporting route would surface a likely incident | Signals exist but alert routing is untested | Define signals and a user report route; test routing |
| Containment | Nobody knows how to disable the solution, a tool or a connection quickly, or lacks rights to do it | Steps exist but are not written down | Write and rehearse a switch-off procedure with named roles |
| Evidence | Interaction records, audit or tool-call logs are missing or expire before an investigation could use them | Evidence exists but collection is manual and slow | Align retention with investigation needs; document collection |
| Responders | The responding team cannot recognise injection, oversharing or agent misuse | Awareness exists but no AI scenario in playbooks | Add AI scenarios to playbooks; brief responders |
| Breach decision | No route to the DPO for incidents involving personal data | Route exists but timing expectations are unclear | Connect the playbook to the breach procedure and the DPO |
| Supplier and Microsoft | No contact or process for incidents in third-party tools, models or MCP servers | Contacts exist but are undocumented | Record supplier contacts and contractual duties; route platform issues through the organisation's Microsoft support channel |

Disagreement escalates to the accountable executive through `responsible-ai:ai-risk-acceptance`.

## Practitioner approach

Start with three short incident stories for the solution, written with its owner. For a typical agent they might be:
"the agent summarised a confidential file to someone who should not see it", "a planted instruction in an email made
the agent send data to an outside address", and "transcripts containing personal data were readable by a supplier".
Stories make the gaps obvious in a way checklists do not.

For each story, walk the response. Who notices first, and how do they report it? Users report AI problems through
whatever is nearest, so make sure the service desk knows what an AI incident looks like and where to send it. Then ask
who can stop the harm. Containment for AI usually means disabling the agent or removing it from a channel, revoking
or pausing a connection, removing a tool, withdrawing a knowledge source or correcting permissions at source. Check that
named roles hold the rights to do each of these out of hours, and that the procedure is written and has been tried
at least once in a non-production setting.

Next, check the evidence. Investigators need to know what was asked, what the solution retrieved, what it did and under
which identity. Use the record map and identity map to confirm that interaction records, audit events, sign-in logs and
tool-call traces exist, can be retrieved by the investigating team and are retained for long enough. Evidence that
expires in days is useless for an incident discovered weeks later.

Connect the playbook to the personal data breach procedure. Incidents involving personal data need prompt assessment by
the DPO, and statutory timings may apply; the playbook should say how the case reaches the DPO, not what the DPO will
decide. For third-party models, tools and MCP servers, record the supplier contact and any contractual notification
duties.

Finally, make sure lessons travel. Agree that the solution owner, the security team and `ai-operations` will review any
incident together and feed new attack patterns back into security testing. Keep the readiness check proportionate: a
tier 2 internal agent needs a one-page playbook and a rehearsed switch-off, not a full exercise.

## Outputs

- An AI incident playbook for the solution: incident stories, detection signals, report route, containment steps with named roles, evidence sources and the route to the DPO.
- Evidence of a containment rehearsal.
- The incident readiness findings in the `ai-risk-assessment`, each classified blocking or advisory with fix and owner, and the verdict.

## Microsoft platform considerations

How an agent, connection or Foundry deployment is disabled, which audit and sign-in events are recorded, and how
Microsoft Purview, Microsoft Entra and Power Platform admin tooling support investigation all differ by route and change
often. Confirm current capability in `ms-copilot-studio-security-governance`, `ms-managed-environments` and
`ms-copilot-privacy`, and write the playbook against what was confirmed.

## Adoption considerations

Users need one obvious way to report an AI problem. Publish it with the solution, and thank people who report; early
reports are the cheapest detection the organisation has.

## Knowledge considerations

Withdrawing a knowledge source is a common containment step. Make sure knowledge owners know they may be asked to do so
quickly and how to restore the source afterwards.

## Security and privacy considerations

This skill is the security and privacy readiness review. Running incidents in operation belongs to
`ai-operations:ai-incident-management`; breach decisions belong to the DPO.

## Responsible AI considerations

Some AI incidents harm people without any security breach, for example misleading advice. Make sure the playbook also
routes such harms to `ai-operations:ai-incident-management` and `responsible-ai:escalation-and-appeal`.

## Evaluation requirements

Blocking gaps close only with evidence: a rehearsed switch-off with timings, a test alert reaching the right team, and
a retrieval of interaction and audit records by the investigating team in a test scenario.

## Value measures

Track at portfolio level the share of tier 2+ solutions with a rehearsed playbook, time to contain in rehearsals and in
real incidents, and repeat incidents of the same type. The security operations lead owns these measures.

## Scale notes

### Starter

Write a one-page playbook per solution and rehearse switching it off once. Brief the service desk on how to recognise
and route AI problems.

### Scale

Add AI scenarios to the organisation's security playbooks, keep a standard containment procedure per platform, and
rehearse tier 3 solutions on a cycle.

### Enterprise

Integrate AI signals into security operations tooling, run cross-team exercises for tier 3 and 4 solutions, and track
incident patterns across the portfolio.

## Hand-offs

- To `ai-operations:ai-incident-management` with the playbook for live operation.
- To `ai-operations:ai-continuity` where switching off the solution needs a business fallback.
- To `security-privacy:ai-security-testing` with new attack patterns after any incident.
- To `m365-agents:agent-release-readiness` with the verdict.

## Reviewer gates

This skill is the `security-privacy` gate for incident readiness, blocking from risk tier 2. Blocking gaps stop release
and are not traded against dates; disagreement escalates to the accountable executive for written risk acceptance.

## Failure modes

- Nobody with rights to disable the agent is reachable out of hours, so a leak continues overnight.
- Interaction records expire before an incident is discovered, so investigators cannot say what was exposed.
- The service desk treats an AI leak as a how-to question and closes the ticket.
- The playbook decides breach reportability itself instead of reaching the DPO.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Release a tier 2 or higher solution that nobody can switch off quickly.
- Decide whether a personal data breach is reportable instead of routing it to the DPO.
- Rely on a general incident process that has never been tested against an AI scenario.
- Trade a blocking gap against a launch date.

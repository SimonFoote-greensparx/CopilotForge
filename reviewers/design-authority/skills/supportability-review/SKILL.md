---
name: supportability-review
description: Reviews whether an AI solution can be owned and supported after release - accepted business, knowledge and technical owners, an operating team with the skills and hours, support route, runbook, monitoring, review dates, dependencies and retirement criteria - classifying each finding as blocking or advisory with the fix. Use when a solution approaches its design or release gate, when a pilot becomes a service, or when owners are lost.
license: CC-BY-4.0
metadata:
  department: design-authority
  lifecycle: Deliver, Assure, Launch, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, power-platform, copilot-code, azure
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-copilot-studio-guidance, ms-declarative-agents, ms-coe-starter-kit, ms-foundry-models
  status: draft
  authors: Simon Foote
---

# Supportability review

## Purpose

Most AI solutions that fail in operation fail quietly: knowledge goes stale, an owner leaves, a connection expires, and
nobody notices until users stop trusting the answers. This reviewer skill checks, before release, that a solution can be
owned and supported for its expected life: named owners, an operating team with the right skills and hours, a support
route, a runbook, monitoring, a review calendar, known dependencies and retirement criteria. Each finding is blocking or
advisory with a fix. Supportability reviews go wrong when ownership is accepted as a name on a form, and when the
builders' confidence is taken as evidence that operations can cope.

## When to use

- A solution at tier 1 or above approaches its design or release gate.
- A pilot built by a project team or partner is about to become a supported service.
- A live solution has lost an owner, or its operating team has changed.
- A solution depends on one person's knowledge or credentials.
- The design authority needs assurance that a new platform can be supported.

## When not to use

- Designing the support model for deployed AI solutions - use `ai-operations:ai-support-model`.
- Assigning business, knowledge and technical owners to an agent - use `m365-agents:agent-ownership`.
- Reviewing the maintainability of AI-built code - use `copilot-code:maintainability-review`.
- Planning continuity when AI is unavailable - use `ai-operations:ai-continuity`.
- Running the release gate for an agent - use `m365-agents:agent-release-readiness`.

## Questions to ask first

1. Who are the business, knowledge and technical owners, and have they accepted the role and the time it needs?
2. Who will users contact when something goes wrong, during which hours, and what happens next?
3. Can the operating team change, fix and redeploy the solution without the original builders?
4. What does the solution depend on - connections, identities, knowledge sources, other systems - and who owns each?
5. When will the solution be reviewed, and what would cause it to be retired?

## Required inputs

- The ownership record, ideally from `m365-agents:agent-ownership` or the solution register.
- The support model from `ai-operations:ai-support-model`, and the runbook if one exists.
- The design pack, including identities, interfaces and grounding sources.
- The operating team's declared skills, capacity and hours.
- The non-functional requirements for availability and support.

A name without confirmed acceptance is not an owner. From tier 2, an unaccepted or missing operating owner is blocking;
never assume the builder will support the solution indefinitely.

## Decision framework

| Area | Blocking when (tier 2 and above) | Advisory when |
|---|---|---|
| Ownership | Business, knowledge or technical owner missing or not accepted | Owners accepted but no deputies |
| Operating team | No team with skills and capacity to change and redeploy | Team exists but relies on one person |
| Support route | Users have no route, or the route ends in an unstaffed queue | Route exists but hours are unclear |
| Runbook | No guidance for common failures on a tier 3 or higher solution | Runbook incomplete at tier 2 |
| Monitoring | No monitoring of errors or quality at tier 2 and above | Monitoring exists without alert routing |
| Dependencies | A connection, identity or source depends on a personal account or an unowned asset | Dependencies owned but undocumented |
| Review and retirement | No review date or retirement criteria | Review date set but no calendar entry |
| Handover | A partner or project team leaves with no handover evidence | Handover partial with a plan |

At tier 1, all findings are advisory except a missing named owner, which is blocking for any shared solution.
Disagreement escalates to the accountable executive for written risk acceptance.

## Practitioner approach

Start with people, not documents. Ask each named owner whether they have accepted the role, what they believe it
involves and how much time they have. Ownership that was assigned in a meeting the owner did not attend is a finding.

Test the operating team's ability to change the solution. Ask them, not the builders, how they would update the
instructions, add a knowledge source, rotate a credential or roll back a bad release. If the answer is "ask the
partner", find out whether the partner is contracted to help after release.

Walk a failure end to end. Pick a realistic incident - the agent starts giving wrong answers after a policy changes, or
an action fails because a connection expired - and trace what happens: who notices, how users report it, who is alerted,
who fixes it, how users are told. Gaps in that path are findings.

List dependencies and their owners. Connections, service identities, knowledge sources, flows and external systems each
need an owner who will tell the solution owner before changing them. Any dependency on a personal account is blocking
from tier 2, because it fails when that person leaves.

Check the review calendar and retirement criteria. A solution with no review date tends to run until it fails. Ask what
evidence would trigger retirement: falling use, unfixable quality, a replacement or loss of ownership.

Be proportionate. A tier 1 team agent needs a named owner, a deputy, a review date and a route for feedback; it does not
need a runbook. A tier 3 solution needs all areas covered with evidence.

Record findings with area, evidence, risk, fix and owner, and pass them to the consolidated design or release review.
Where a partner is handing over, make closure of handover findings a condition of release.

## Outputs

- A supportability section in the `design-review-record`: areas reviewed, evidence, findings classified as blocking or advisory with fix and owner.
- A dependency list with owners, for the solution register.
- Handover conditions for partner or project-built solutions.

## Microsoft platform considerations

Ownership transfer, connection management, monitoring and redeployment work differently across Agent Builder, Copilot
Studio, Power Platform and Microsoft Foundry. Check `ms-copilot-studio-guidance`, `ms-declarative-agents` and
`ms-foundry-models` for current lifecycle features, and `ms-coe-starter-kit` for finding owners and dependencies.

## Adoption considerations

Users stop using solutions they cannot get help with. Check that users will know how to report problems and give
feedback, and that someone will respond.

## Knowledge considerations

Knowledge ownership is the most commonly missing piece. Check that each grounding source has an accepted knowledge owner
and review cycle, linked to `ai-operations:knowledge-refresh`.

## Security and privacy considerations

Dependencies on personal accounts and expired or orphaned identities are both supportability and security issues. Share
such findings with the `security-privacy` reviewers.

## Responsible AI considerations

For tier 3 and above solutions affecting people, check that the oversight roles named in the `responsible-ai` review are
staffed in operation, not only in design.

## Evaluation requirements

Check that the operating team can run regression evaluation after changes, with access to the evaluation set and
thresholds, consistent with `evaluation-quality:regression-evaluation`.

## Value measures

At portfolio level, track solutions with accepted owners and deputies, orphaned solutions, incidents with no clear owner
and time to restore after failure. The design authority chair and AI operations lead own these measures, with a baseline
from the first review cycle.

## Scale notes

### Starter

Check that each shared agent has two accepted owners, a feedback route and a review date. That alone prevents most
orphans.

### Scale

Apply the full review at tier 2 and above, require handover evidence from partners and connect findings to the operating
model.

### Enterprise

Integrate with enterprise service management, require operational acceptance by the service owner before release and
review supportability across the estate annually.

## Hand-offs

- To `ai-operations:ai-support-model` to fill gaps in the support model.
- To `m365-agents:agent-ownership` where owners are missing or unaccepted.
- To `design-authority:ai-design-review` or the release gate for the consolidated verdict.

## Reviewer gates

This skill is part of the `design-authority` gate, blocking from risk tier 2 and for missing owners of any shared
solution. Dependency and identity findings are shared with `security-privacy`. Disagreement escalates to the
accountable executive for written risk acceptance.

## Failure modes

- An owner is named without being asked, and nobody acts when the solution starts to fail.
- The builders support the solution informally, until they move to the next project.
- A partner delivers and leaves, and nobody can change the agent's instructions.
- A connection runs on a leaver's account and the solution stops without warning.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Accept a name as an owner without confirmed acceptance of the role.
- Pass a tier 2 or higher solution that depends on a personal account.
- Take the builders' confidence as evidence that operations can support the solution.
- Assess or rank individual owners' performance; review roles and arrangements only.

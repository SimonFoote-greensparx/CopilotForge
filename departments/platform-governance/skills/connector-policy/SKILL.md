---
name: connector-policy
description: Writes the organisation-wide data and connector policies for AI building in each zone - business, non-business and blocked connector groups, custom connectors, HTTP and MCP access, web and public knowledge, endpoint filtering - with an exceptions process that has owners and review dates. Use when data policies predate agents, when makers keep requesting blocked connectors, or when AI features such as web grounding or MCP need a policy position.
license: CC-BY-4.0
metadata:
  department: platform-governance
  lifecycle: Mobilise, Enable, Assure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: copilot-studio, power-platform, m365-agents, purview
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-studio-security-governance, ms-managed-environments, ms-copilot-studio-zoned-governance, ms-agents-extensibility, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Connector policy

## Purpose

Data and connector policies decide which systems agents and flows may connect to, and which may be combined in one
solution. This skill writes those policies for AI building across the governance zones, including the positions on
custom connectors, HTTP calls, MCP servers and web or public knowledge that ordinary automation policies often miss. It
also sets an exceptions process so legitimate needs are met without quietly widening policy. Connector policy goes
wrong when it was written for flows years ago and never revisited for agents, when everything is blocked and makers work
around it, and when exceptions pile up without owners.

## When to use

- Data policies exist but were written before agents and AI features.
- Makers repeatedly ask for connectors that are blocked, or find workarounds.
- An AI capability such as web grounding, MCP servers or custom connectors needs an organisation-wide position.
- New governance zones need matching data policies.
- Policy exceptions have accumulated without owners or review dates.

## When not to use

- Reviewing the connectors a specific agent or flow uses - use `security-privacy:connector-review`.
- Choosing connectors for one Copilot Studio agent - use `copilot-studio:studio-connectors`.
- Governing connectors and data policies for automation flows specifically - use `automation:automation-connector-governance`.
- Deciding the zones the policies attach to - use `platform-governance:ai-environment-strategy`.
- Designing how a solution integrates with business systems - use `ai-architecture:ai-integration-patterns`.

## Questions to ask first

1. What data policies exist today, which environments do they cover, and when were they last reviewed?
2. Which connectors and AI capabilities do makers actually use or request, by zone?
3. Which systems hold sensitive data that must never be combined with external services?
4. What is the organisation's position on agents grounding on the public web or calling external services?
5. Who will own the policy and approve exceptions?

## Required inputs

- The environment zoning plan from `platform-governance:ai-environment-strategy`.
- Current data policies and their scope.
- Connector usage and request data at aggregate level, from admin reports or the inventory.
- The data classification scheme and security policy on external services.

If current policies cannot be exported, start from a clean design per zone and plan a comparison; never assume an
environment is covered by a policy without checking.

## Decision framework

Classify connectors and AI capabilities per zone.

| Capability | Zone 1 personal | Zone 2 team | Zone 3 managed production |
|---|---|---|---|
| Microsoft 365 connectors for the user's own content | Allowed (business) | Allowed | Allowed |
| Approved line-of-business connectors | Blocked | Allowed where the team needs them | Allowed per solution review |
| Consumer and social connectors | Blocked | Blocked | Exception only |
| Custom connectors and HTTP calls | Blocked | Exception only | Allowed with endpoint restrictions and review |
| MCP servers and external tools | Blocked | Exception only | Allowed from a vetted list, reviewed per solution |
| Web or public knowledge for agents | Policy decision, usually allowed with care | Policy decision per team | Per solution, recorded in the design |
| Combining business and non-business connectors | Not allowed | Not allowed | Not allowed |

Exceptions process:

| Step | Rule |
|---|---|
| Request | States the solution, connector, operations, data and reason |
| Review | Security reviewer checks data flow and identity |
| Approve | Policy owner approves with conditions |
| Record | Owner, scope, conditions and review date in the exceptions log |
| Review | Expires or is renewed on the date; never open-ended |

## Practitioner approach

Start by collecting the current policies and checking what they cover. It is common to find environments with no
policy at all, policies that predate agents, and a long tail of connectors left in the default group because nobody
classified them.

Agree the principles with security before classifying anything. The core principles are short: business data stays
with business connectors; data must not flow from business systems to consumer services; external calls are restricted
to known endpoints; and anything new is blocked until classified. Write them on one page, because they will decide the
hard cases.

Classify by zone. Personal building should have a policy that allows Microsoft 365 productivity and little else.
Team building adds the business connectors teams genuinely need. Managed production allows what reviewed solutions need,
with endpoint filtering for custom connectors and HTTP calls where the platform supports it. Check the current
capabilities in the source records rather than assuming a control exists.

Take an explicit position on AI-specific capabilities. Web grounding, MCP servers, custom connectors and calls to
external model endpoints each move data or influence outside the organisation's control. Decide per zone whether they
are allowed, allowed with conditions or blocked, and record the reasoning so makers understand it.

Set the default for new connectors to blocked, and review the new-connector list on a cycle. Microsoft adds connectors
frequently, and an unclassified connector in the wrong group is a gap.

Run exceptions as a process, not a favour. Every exception has an owner, a scope, conditions and a review date, and is
logged where admin monitoring can check it. Expired exceptions are removed unless renewed.

Communicate the policy to makers in plain language: what they can use in each zone, why, and how to ask for an
exception. Most workarounds come from makers who did not know a legitimate route existed.

Review the policy at least twice a year, and whenever a significant AI capability arrives.

## Outputs

- A data and connector policy per zone: principles, classification, AI capability positions and endpoint restrictions.
- An exceptions process and log with owners, conditions and review dates.
- A maker-facing summary of what is allowed where.
- Configuration requests to platform administrators.

## Microsoft platform considerations

Data policies, connector classification, endpoint filtering, environment groups and controls over AI features such as
web grounding and MCP are configured in the Power Platform and Microsoft 365 admin experiences, and they change often.
Check `ms-copilot-studio-security-governance`, `ms-managed-environments` and `ms-agents-extensibility` for current
controls before writing them into policy.

## Adoption considerations

A policy that blocks everything drives makers to unapproved tools. Explain each restriction, publish the exception route
and measure how long exceptions take to decide.

## Knowledge considerations

Web and public knowledge positions belong in this policy, because they change where agents get their answers. Internal
knowledge sources are governed through `knowledge-management` and the grounding standards.

## Security and privacy considerations

This skill sets the policy that `security-privacy:connector-review` checks solutions against. Agree principles,
classifications and the exceptions process with the `security-privacy` reviewers, and route personal data flowing to
external services to `security-privacy:privacy-assessment`.

## Responsible AI considerations

External tools and web grounding can introduce unverified content into answers that affect people. Where solutions
inform decisions about people, prefer closed, owned sources and record the position for `responsible-ai` review.

## Evaluation requirements

Test the policy itself: in each zone, confirm that a blocked connector cannot be added, that business and non-business
connectors cannot be combined, and that endpoint restrictions hold. Repeat after policy changes.

## Value measures

At estate level, track environments covered by the right policy, unclassified connectors, open exceptions past their
review date and median time to decide an exception. The platform governance lead owns these measures, with a baseline
from the first policy review.

## Scale notes

### Starter

One restrictive policy for the default environment and one for the managed environment is often enough. Decide the web
grounding position early.

### Scale

Policies per zone, an exceptions log, a twice-yearly review and a new-connector review on a short cycle.

### Enterprise

Apply policies through environment groups, federate exception triage with central approval, and monitor policy coverage
and exceptions automatically.

## Hand-offs

- To `security-privacy:connector-review`, which reviews solutions against the policy.
- To `automation:automation-connector-governance` for automation-specific detail.
- To `platform-governance:ai-admin-monitoring` to watch policy coverage and exceptions.

## Reviewer gates

The policy and every exception are agreed with `security-privacy`. Exceptions for tier 2 and above solutions are tied to
the solution's security review and cannot be approved on the policy owner's authority alone.

## Failure modes

- Policies written for flows are never updated, and agents call external services nobody considered.
- New connectors land in the business group by default and are combined with sensitive systems.
- Exceptions are granted informally and never expire.
- Everything is blocked, and makers move to unapproved tools outside any policy.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Grant an exception without an owner, conditions and a review date.
- Allow business data to flow to consumer services in any zone.
- Leave new connectors unclassified in a permissive default group.
- Assume a policy control exists without checking the current source records.

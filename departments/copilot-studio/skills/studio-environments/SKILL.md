---
name: studio-environments
description: Applies the organisation's environment strategy to Copilot Studio work - the concrete personal, team, test and production environments makers use, environment routing for new makers, Managed Environment and agent settings per zone, security groups, data policies and how agents move between zones. Use when makers start building agents, when agents pile up in the default environment, or when a team asks for its own development space.
license: CC-BY-4.0
metadata:
  department: copilot-studio
  lifecycle: Mobilise, Deliver, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: copilot-studio, power-platform, entra
  edition-support: starter, scale, enterprise
  reviewers: design-authority, security-privacy
  sources: ms-copilot-studio-zoned-governance, ms-copilot-studio-security-governance, ms-managed-environments, ms-coe-starter-kit
  status: draft
  authors: Simon Foote
---

# Studio environments

## Purpose

Copilot Studio makers need somewhere safe to experiment, somewhere to build properly and somewhere controlled to run
agents others depend on. This skill turns the organisation's environment strategy into the concrete environments,
routing rules and settings Copilot Studio makers actually use, so building is easy and production is controlled. It
usually goes wrong when every maker builds in the default environment, when each team is given a bespoke environment
with no consistent settings, or when environments are so locked down that makers turn to unmanaged tools instead.

## When to use

- The organisation is opening Copilot Studio to makers and needs the environments ready.
- Agents are accumulating in the default environment with no clear owner or route to production.
- A team asks for its own development, test or production environment for agents.
- Environment settings, data policies or security groups for Studio work need to be made consistent.

## When not to use

- Setting the organisation's environment strategy and governance zones for all AI building - use `platform-governance:ai-environment-strategy`.
- Environment topology across Microsoft 365, Power Platform and Azure - use `ai-architecture:environment-topology`.
- Who may build and share agents and flows - use `platform-governance:maker-governance`.
- Moving a specific agent between environments with solutions and pipelines - use `copilot-studio:studio-alm`.

## Questions to ask first

1. What governance zones has the organisation agreed, and what may happen in each (personal productivity, team collaboration, enterprise production)?
2. Where do new makers land today when they open Copilot Studio, and what is already in the default environment?
3. Which teams build agents regularly enough to need their own development and test environments?
4. Which data policies, sharing limits and security groups apply in each zone?
5. Who administers each environment and approves promotion between zones?

## Required inputs

- The environment strategy and zone definitions from `platform-governance:ai-environment-strategy`.
- Data policies from `platform-governance:connector-policy`.
- An inventory of existing environments and agents, for example from the CoE Starter Kit or admin reports.
- Security groups for makers and audiences, owned by the identity team.

If no environment strategy exists, do not invent zones here; hand back to `platform-governance:ai-environment-strategy`
and, in the meantime, at least stop new production-bound agents being built in the default environment.

## Decision framework

| Zone | Typical environment pattern | Who builds | Sharing | Promotion |
|---|---|---|---|---|
| Personal productivity | Default or personal developer environments, with routing so makers do not land in shared space | Any licensed maker | Self or very small groups | None; rebuild properly if it proves useful |
| Team collaboration | A development environment per team or business unit, plus a shared test environment | Named team makers | The team or department | Through ALM into team or enterprise production |
| Enterprise production | Dedicated production environments, often per business area or risk tier | No direct making; changes arrive through pipelines | Wide or organisation-wide audiences | Only from test, with release approval |

Every non-personal environment is a Managed Environment with a security group, agreed data policy, named admin owner,
and consistent settings for sharing, analytics and agent capabilities. Create a new environment only when an existing
one cannot meet a distinct owner, data boundary, region or release cadence.

## Practitioner approach

Start with where makers actually are. Inventory the default and other environments, list the agents in them, their
owners and audiences, and identify those that are shared widely or use business data. These are the agents to move first,
and they show what the zones must support.

Design routing before opening the doors. Environment routing can send new makers to a personal or developer environment
rather than the shared default, so experimentation does not pollute a common space. Agree what makers see when they first
open Copilot Studio, and publish a short guide explaining which environment to use for what. Makers follow the path of
least resistance; make the governed path the easy one.

Define a small, repeatable set of environment types rather than bespoke environments. For each type, fix the settings:
Managed Environment on, security group, data policy, sharing limits, whether web knowledge or unauthenticated agents are
permitted, analytics and transcript settings, and the admin owner. Apply the same type the same way every time, ideally
from a script or checklist, so settings do not drift.

Give regular building teams their own development environment and a shared test environment, and keep production
environments free of direct making. Changes reach production through solutions and pipelines, which `copilot-studio:studio-alm`
designs. Production environments are where business owners, support and reviewers can rely on what they see.

Agree how an agent graduates. A personal prototype that proves useful is rebuilt or exported as a solution into a team
development environment, gains an owner and brief, and follows the release path. Write the graduation criteria down so
makers know what is expected before their agent can be shared more widely.

Plan the default environment's future. Decide what may stay there, how existing shared agents are moved, and how makers
are told. Moving agents takes effort; prioritise those with wide sharing, business data or no owner.

Review environments quarterly with the platform owner: unused environments, settings drift, agents in the wrong zone and
capacity. Route capacity and licence questions to `platform-governance:ai-licensing-and-capacity`.

## Outputs

- An environment catalogue for Studio work: each environment, its zone, type, purpose, admin owner, security group, data policy and settings.
- Environment routing rules and a maker guide explaining where to build what.
- Graduation criteria for moving agents between zones.
- A remediation list for agents in the wrong environment, with priority and owner.
- The environment section of the `alm-and-environment-plan`.

## Microsoft platform considerations

Environment routing, Managed Environment features, agent-specific admin settings and data policy controls change
frequently and some depend on licensing. Check `ms-copilot-studio-zoned-governance`, `ms-copilot-studio-security-governance`
and `ms-managed-environments` for the current position, use `ms-coe-starter-kit` for inventory, and route licensing
questions to the licensing guide or a licensing partner.

## Adoption considerations

Makers abandon governed routes that are slow or confusing. Publish the maker guide with the environments, offer a fast
request route for team environments, and celebrate agents that graduate properly.

## Knowledge considerations

Not applicable to environment design itself, because environments contain agents rather than knowledge; note only that
knowledge connections and uploaded files must be re-established when agents move between environments.

## Security and privacy considerations

Production environments have restricted maker access, security groups, appropriate data policies and controls on
unauthenticated agents and web knowledge. Agents using sensitive data do not live in personal or default environments.
Environment settings that affect data exposure go to `security-privacy:data-exposure-review`.

## Responsible AI considerations

Not applicable directly, because environment design does not shape agent behaviour; it supports responsible AI by making
sure higher-risk agents run where reviewers and owners can see and control them.

## Evaluation requirements

Not applicable for agent quality; instead, verify each environment's settings against its type after creation and at
quarterly review, and confirm routing sends new makers where intended.

## Value measures

Track agents in the correct zone, time to provision a team environment, settings drift found at review and the number of
shared agents remaining in the default environment, owned by the platform owner and reported at portfolio level.

## Scale notes

### Starter

Routing for new makers, one team development environment, one test and one production environment, all managed, with a
one-page maker guide.

### Scale

Environment types applied consistently per business unit, scripted provisioning, quarterly reviews and a remediation
programme for the default environment.

### Enterprise

Automated provisioning and policy assignment, environment groups per zone, regional environments where data residency
requires them, and environment reporting feeding the solution inventory.

## Hand-offs

- To `copilot-studio:studio-alm` for solutions and pipelines between environments.
- To `platform-governance:maker-governance` for who may build in each zone.
- To `platform-governance:ai-licensing-and-capacity` for capacity and licence questions.
- To `copilot-studio:studio-agent-lifecycle` for agents found without owners during inventory.

## Reviewer gates

From risk tier 2, `design-authority` checks that the agent's production environment matches its zone and type, and
`security-privacy` checks data policy and exposure settings. A tier 2 or higher agent running in a personal or default
environment is a blocking finding.

## Failure modes

- Routing is not configured, so new makers keep building shared agents in the default environment.
- Every team gets a bespoke environment and settings drift until no two behave the same.
- Production environments allow direct making, and untested changes reach users.
- Environments are so restricted that makers move to unmanaged tools.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Let production-bound or widely shared agents be built in the default environment.
- Allow direct making in production environments.
- Create a new environment where an existing type already meets the need.
- State licensing or capacity conclusions; route them to the licensing guide or a licensing partner.

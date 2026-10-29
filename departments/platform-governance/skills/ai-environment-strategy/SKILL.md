---
name: ai-environment-strategy
description: Sets the environment strategy for AI building as governance zones - personal productivity, team collaboration and managed production - deciding who builds in each zone, its controls and sharing limits, and how a solution moves up a zone. Use when there is no organisation-wide rule for where AI building happens, when experiments become business-critical without controls, or when a team solution needs a governed home.
license: CC-BY-4.0
metadata:
  department: platform-governance
  lifecycle: Mobilise, Enable, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: copilot-studio, power-platform, m365-agents, ai-foundry
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, design-authority
  sources: ms-copilot-studio-zoned-governance, ms-managed-environments, ms-copilot-studio-security-governance, ms-copilot-studio-guidance, ms-coe-starter-kit
  status: draft
  authors: Simon Foote
---

# AI environment strategy

## Purpose

People will build agents and flows wherever the platform lets them. This skill decides, deliberately, where each kind
of building happens: a zone for personal productivity, a zone for team collaboration and a zone for managed production
solutions, each with its own controls, data policies, sharing limits and route upwards. It lets experimentation happen
safely without letting experiments quietly become business-critical. Environment strategy goes wrong when everything
lives in the default environment, when the controls are so heavy that makers go elsewhere, and when there is no path
for a good idea to move into a governed home.

## When to use

- Agents and flows are accumulating in the default environment with no rules.
- The organisation is about to open agent building to more people.
- A team solution has become important and needs a governed environment.
- Environment requests arrive with no criteria for approving them.
- Governance zones exist on paper but makers do not know where to build.

## When not to use

- Designing the technical topology of tenants, environments, subscriptions and regions - use `ai-architecture:environment-topology`.
- Planning development, test and production environments for a specific Copilot Studio build - use `copilot-studio:studio-environments`.
- Deciding who may build and share, and maker onboarding - use `platform-governance:maker-governance`.
- Writing the data and connector policies applied in each zone - use `platform-governance:connector-policy`.
- Governing Copilot Cowork plugins, skills and sharing - use `copilot-cowork:cowork-governance`.

## Questions to ask first

1. Who builds today, on which platforms, and where do their agents and flows live?
2. Which risk tiers will be built in the next year, and which need managed production homes?
3. What data may be used in personal and team building, and what must stay in managed production?
4. Who will own each zone, approve environment requests and decide promotions?
5. Which platform controls (for example Managed Environments features) does the organisation have available, according to the source records and licensing guide?

## Required inputs

- The governance framework and risk tiers, from `ai-centre-of-excellence:coe-governance-model` or the governance starter.
- An inventory of current environments and their contents, from `platform-governance:ai-solution-inventory` or admin reports.
- The technical topology, if one exists, from `ai-architecture:environment-topology`.
- The approved platform list and data classification scheme.

Where licensing for governance features is uncertain, record the dependency and route it to
`platform-governance:ai-licensing-and-capacity`; never design a zone around a control the organisation may not have.

## Decision framework

Define three zones as a default, and adjust only with a reason.

| Zone | Purpose | Who builds | Data allowed | Sharing | Typical controls |
|---|---|---|---|---|---|
| 1. Personal productivity | Individual experiments and helpers | Any enabled maker | The maker's own and general internal content; no sensitive data | Maker only, or very small group | Restrictive data policy, no custom connectors, sharing limits, inactivity clean-up |
| 2. Team collaboration | Shared team solutions up to tier 1 | Makers with completed onboarding | Team content and approved business connectors | Named team or group | Data policy for business connectors, named owner, register entry, review date |
| 3. Managed production | Organisational solutions at tier 2 and above | Delivery teams with ALM | Approved data per review | Defined audience per release | Dedicated environments, ALM, reviewer gates, monitoring, managed sharing |

Promotion rules:

| Signal | Action |
|---|---|
| Shared beyond the maker | Moves to zone 2, with an owner and register entry |
| Classified tier 2 or above, or audience beyond a team | Moves to zone 3 through the release policy |
| Uses sensitive data or write actions in business systems | Zone 3 regardless of audience |
| Inactive past the agreed period | Owner contacted, then archived or removed |

## Practitioner approach

Start with the current state. Pull a list of environments, agents, flows and makers from the admin reports or the
inventory, and look at where things actually live. Most organisations find a crowded default environment, a few
environments created for projects long finished, and some important solutions in places with no controls.

Agree the zones with the CoE and security before touching settings. Use the three-zone default and adjust with care: a
regulated business unit might need its own zone 3, and a large organisation might split zone 2 by business unit. Name
the owner of each zone and who approves requests into it.

Design zone 1 to be easy. If personal building is hard, people use unapproved tools instead. Make the default or a
designated personal environment safe through a restrictive data policy, sharing limits and clean-up of inactive items,
rather than by blocking it. Tell makers clearly what zone 1 is for and what it is not for.

Design zone 2 for teams. Require a named owner, a register entry and completion of maker onboarding. Allow the business
connectors a team needs and block the rest through `platform-governance:connector-policy`.

Design zone 3 for organisational solutions. Each solution, or a small group of related solutions, gets development, test
and production environments with ALM, reviewer gates and monitoring. Sharing is controlled by release, not by the maker.

Write the promotion rules and make them visible. The most common failure is a zone 1 or 2 solution that becomes
important without anyone noticing. Use the inventory and admin monitoring to detect signals such as growing audiences or
sensitive connectors, and contact owners when a solution crosses a threshold.

Route makers automatically where the platform supports it, so new makers land in the right zone without raising a
request. Check current routing options in the source records.

Publish the strategy on the environment zoning plan, with a short "where do I build" guide for makers, and review it
when new platforms or controls arrive.

## Outputs

- An environment zoning plan on the `environment-zoning-plan` template: zones, purposes, owners, controls, data allowed, sharing limits, promotion rules and request process.
- A "where do I build" guide for makers.
- A list of current environments mapped to zones, with actions for those that do not fit.

## Microsoft platform considerations

Power Platform environments, Managed Environments features, environment routing, environment groups and sharing limits
are the main levers, and Microsoft's zoned governance guidance describes how they combine. Features and their licensing
change; check `ms-copilot-studio-zoned-governance`, `ms-managed-environments` and `ms-copilot-studio-security-governance`
before relying on a control, and route licensing questions to the licensing guide or a partner.

## Adoption considerations

Zones are an adoption tool as much as a control. A safe, easy personal zone encourages experimentation, and a clear path
upwards rewards makers whose ideas prove valuable. Communicate zones with the maker community and Champions.

## Knowledge considerations

Not applicable to zone design itself, because knowledge sources live outside environments. Zones do decide which
knowledge sources may be used, so align data allowed per zone with knowledge classification.

## Security and privacy considerations

Zones exist to keep sensitive data and powerful actions in governed places. Agree data allowed, sharing limits and
connector policy per zone with the `security-privacy` reviewers, and make zone 3 the only home for sensitive data.

## Responsible AI considerations

Uses that inform decisions about people belong in zone 3 whatever their audience, so that oversight, logging and
`responsible-ai` review can apply.

## Evaluation requirements

Not applicable to the strategy as a whole, because evaluation applies to solutions rather than zones. Zone 3 requires
evaluation evidence at release according to the release policy.

## Value measures

At estate level, track the share of agents and flows in the right zone, solutions promoted with an owner, time to
provision a zone 3 environment and the number of orphaned items in zone 1. The platform governance lead owns these
measures, with a baseline from the first inventory.

## Scale notes

### Starter

Two zones may be enough: a safe personal default and one managed environment for shared agents. Keep request
processes light.

### Scale

Use all three zones, with routing for new makers, a request process for zone 3 and regular promotion checks.

### Enterprise

Federate zone 2 by business unit with central policy, use environment groups to apply controls consistently, and
automate promotion signals and clean-up.

## Hand-offs

- To `platform-governance:connector-policy` for data policies per zone.
- To `platform-governance:maker-governance` for who may build in each zone.
- To `ai-architecture:environment-topology` for technical placement.
- To `copilot-studio:studio-environments` for solution-level environment design.

## Reviewer gates

The zoning plan is agreed with `security-privacy` before adoption and reviewed by `design-authority` for alignment with
the topology. Promotion into zone 3 follows the release policy and the reviewer gates for the solution's risk tier.

## Failure modes

- Everything stays in the default environment, and a personal experiment becomes a business-critical agent with no controls.
- Zone 1 is so restricted that makers use unapproved tools.
- There is no promotion route, so valuable team solutions never reach a governed home.
- Zones exist in policy, but routing and data policies were never configured to match.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Allow sensitive data or write actions in business systems outside the managed production zone.
- Design a zone around a control whose availability or licence has not been confirmed.
- Block personal building entirely instead of making it safe.
- Leave a zone without an owner and a request route.

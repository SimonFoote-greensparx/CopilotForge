---
name: environment-topology
description: Designs the technical topology a set of AI solutions runs across - Microsoft 365 tenant settings, Power Platform environments, Azure subscriptions and resource groups, regions and the paths between them - so production is separated and data stays within agreed boundaries. Use when the first pro-code or multi-environment AI solution is planned, when Azure and Power Platform estates grow apart, or when data residency affects placement.
license: CC-BY-4.0
metadata:
  department: ai-architecture
  lifecycle: Mobilise, Deliver, Scale
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, power-platform, entra, azure
  edition-support: scale, enterprise
  reviewers: design-authority, security-privacy
  sources: ms-copilot-studio-zoned-governance, ms-managed-environments, ms-copilot-studio-security-governance, ms-copilot-privacy, ms-foundry-models
  status: draft
  authors: Simon Foote
---

# Environment topology

## Purpose

AI solutions rarely live on one platform. An agent in Copilot Studio may call a flow in another environment, a model
deployment in an Azure subscription and data in a separate analytics workspace, all inside one Microsoft 365 tenant.
This skill designs that topology: which environments, subscriptions and regions exist, what runs where, how changes
move from development to production and which paths between them are allowed. Topology goes wrong when Power Platform
and Azure estates are designed by different teams with different rules, when production depends on a developer's
sandbox, and when a model is deployed to a region nobody checked against data residency commitments.

## When to use

- The first AI solution spanning Power Platform and Azure, or several environments, is being planned.
- Azure AI resources and Power Platform environments have grown separately and need aligning.
- Data residency or sovereignty commitments affect where models, indexes or logs may run.
- A deployment pipeline needs a defined path from development through test to production.
- An existing estate has production solutions depending on development resources.

## When not to use

- Setting the governance zones, maker access and policies for AI building - use `platform-governance:ai-environment-strategy`.
- Planning environments and environment routing for Copilot Studio makers - use `copilot-studio:studio-environments`.
- Choosing deployment options and topology for one Foundry solution - use `ai-foundry:foundry-deployment-architecture`.
- Choosing the platform for a solution - use `ai-architecture:platform-selection`.
- Building CI/CD pipelines - use `ai-engineering:ai-ci-cd`.

## Questions to ask first

1. Which platforms will AI solutions use in the next year - Microsoft 365 agents, Copilot Studio, Power Platform, Azure, Microsoft Foundry?
2. What separation is required between development, test and production, and for which risk tiers?
3. Are there data residency, sovereignty or contractual commitments that constrain regions?
4. Which teams own the Microsoft 365 tenant, the Power Platform estate and Azure subscriptions today?
5. How will changes be promoted, and who approves production deployments?

## Required inputs

- The zoning and environment strategy from `platform-governance:ai-environment-strategy`, if it exists.
- The portfolio of live and planned AI solutions with their platforms and risk tiers.
- Existing Azure landing zone and subscription design, and Power Platform environment list.
- Data residency commitments, confirmed with the DPO or legal adviser where they are contractual or legal.

If residency commitments are unknown, mark region choices provisional and record the question; never pick a region on
convenience and assume it is acceptable.

## Decision framework

Design the topology in layers, and test each layer against the separation and boundary rules.

| Layer | Decide | Rule of thumb |
|---|---|---|
| Tenant | Single or multiple Microsoft 365 tenants for AI work | One tenant unless a legal or contractual boundary requires more |
| Power Platform environments | Development, test and production per zone, and shared or dedicated per solution | Dedicated production environments for tier 2 and above; shared environments for personal and team building |
| Azure subscriptions and resource groups | Where model deployments, indexes, functions and logs live | Separate production from non-production; align with the existing landing zone |
| Regions | Where models, indexes, storage and logs run | Match residency commitments; record any processing outside them as a decision |
| Paths | Which environments and subscriptions may call each other | Production never depends on non-production; cross-boundary calls are documented |
| Promotion | How solutions and configuration move between stages | Through pipelines or managed solutions, never by rebuilding in production |

## Practitioner approach

Begin with what exists. List the tenant, the Power Platform environments and their purposes, the Azure subscriptions
and resource groups used for AI, and the regions in use. In most estates this inventory reveals environments with no
clear purpose and Azure resources created by a pilot that is now quietly serving production.

Agree the separation rules with the platform governance lead before drawing anything. The governance zones decide who
may build where; the topology decides how those zones are implemented and connected. Keep the two aligned: if
governance defines a personal productivity zone, a team collaboration zone and a managed production zone, the topology
should show each one and its environments.

Place the Power Platform layer next. Give production solutions at tier 2 and above their own production environments,
or a small number of shared production environments with strict controls, and give each a matching development and
test environment. Keep personal and team experimentation in environments that cannot host production workloads.

Then align Azure. Put AI resources for production in production subscriptions under the existing landing zone, with
non-production resources separated. Model deployments, retrieval indexes, storage and logs each have a region; check
each against residency commitments and the current source records, and record any exception as a decision.

Define the allowed paths. Draw which environments and subscriptions may call which, and make two rules explicit:
production never calls non-production, and every cross-boundary call has an identity and an owner. Hand the identity
detail to `ai-architecture:ai-identity-design`.

Define promotion. Changes move from development to test to production through pipelines or managed solutions with an
approval step proportionate to risk. Nobody edits production directly except in a documented emergency.

Publish the topology as a diagram and a table, owned by the AI architecture function, and review it when a new platform
is approved, when residency commitments change or when the portfolio grows materially.

## Outputs

- An environment topology: tenant, Power Platform environments, Azure subscriptions and resource groups, regions, allowed paths and promotion routes, as a diagram and a table.
- A placement record per solution, showing where each component runs.
- An architecture decision record on the `architecture-decision-record` template for region exceptions and cross-boundary paths.

## Microsoft platform considerations

Power Platform environments, Managed Environments features, environment routing, Azure subscription design and model
deployment regions all change over time. Use `ms-copilot-studio-zoned-governance` and `ms-managed-environments` for
current Power Platform options, and `ms-foundry-models` and `ms-copilot-privacy` for model deployment and data
handling, and do not assert regional availability from memory.

## Adoption considerations

Makers need to know where to build. Publish a short "where do I build" guide aligned with the topology, so
experimentation is easy in the right place and hard in production.

## Knowledge considerations

Not applicable in most cases, because knowledge stays in its source systems. Where grounding uses an index or copy, its
placement follows this topology and is designed with `ai-architecture:grounding-patterns`.

## Security and privacy considerations

Topology sets the boundaries that security relies on. Have `security-privacy` agree the allowed paths, the separation
of production and the placement of logs, and route residency questions with legal effect to the DPO or legal adviser.

## Responsible AI considerations

Not applicable directly, because topology concerns placement rather than use. Logging placement does matter for
oversight, so make sure logs needed for `responsible-ai:human-oversight` review are retained where reviewers can reach them.

## Evaluation requirements

Evaluation environments should mirror production closely enough to be meaningful. Name the environment where release
evaluation runs and confirm it uses representative data under agreed controls.

## Value measures

Track, at estate level, environments and subscriptions with a recorded purpose and owner, production solutions with a
separate development path, and incidents caused by environment or region misplacement. The AI architecture lead owns
these measures, with a baseline from the first inventory.

## Scale notes

### Starter

Starter organisations may need only a default environment for personal use, one development and one production
environment for shared agents, and no Azure AI resources. Keep it that simple until a pro-code solution appears.

### Scale

Define environments per zone, align Azure AI resources with the landing zone, publish the topology and require a
placement record for every tier 2 solution.

### Enterprise

Manage topology as code where possible, with per-business-unit environments under central policy, regional placement
rules and automated detection of production dependencies on non-production resources.

## Hand-offs

- To `platform-governance:ai-environment-strategy` to keep zones and topology aligned.
- To `copilot-studio:studio-environments` and `ai-foundry:foundry-deployment-architecture` for build-level placement.
- To `ai-engineering:ai-ci-cd` to implement promotion routes.

## Reviewer gates

The topology and any region exceptions are reviewed by `design-authority:architecture-conformance` and `security-privacy` before adoption, and
each tier 2 or higher solution's placement record is checked at its design gate.

## Failure modes

- A pilot's development environment becomes production by accident, with no ALM path and maker-owned connections.
- A model or index is deployed to a region outside residency commitments because it was available first.
- Power Platform and Azure teams design separately, and cross-platform calls have no identity or owner.
- Production calls a non-production resource that is deleted during clean-up.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Allow production solutions to depend on development or test resources.
- Choose a region without checking it against residency commitments.
- State regional availability or limits from memory.
- Promote changes by rebuilding in production rather than through a defined route.

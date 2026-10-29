---
name: studio-alm
description: Sets application lifecycle management for Copilot Studio agents - solutions and publishers, environment variables and connection references, source control, pipelines between development, test and production, managed versus unmanaged imports, versioning, change control and rollback. Use when an agent must move beyond one environment, when changes are made directly in production, or when several makers work on the same agent.
license: CC-BY-4.0
metadata:
  department: copilot-studio
  lifecycle: Mobilise, Deliver, Launch, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-studio, power-platform, github, azure
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-copilot-studio-guidance, ms-managed-environments, ms-copilot-studio-security-governance, ms-coe-starter-kit
  status: draft
  authors: Simon Foote
---

# Studio ALM

## Purpose

An agent that only exists in the environment where it was built cannot be tested safely, changed safely or recovered
when something goes wrong. This skill sets the application lifecycle for Copilot Studio agents: how they are packaged in
solutions, how they move from development through test to production, how configuration differs per environment, how
changes are versioned and approved, and how a bad release is rolled back. ALM usually goes wrong when it is added after
the pilot succeeds, when agents and their flows sit in different solutions or none, and when urgent fixes are made
directly in production and then overwritten by the next import.

## When to use

- An agent is about to move beyond the environment it was built in.
- Changes are being made directly in production, or nobody can say which version is live.
- Several makers work on the same agent, or an agent shares flows and connectors with others.
- A release needs a rollback route, or a reviewer asks for evidence of change control.

## When not to use

- Deciding which environments exist and how makers are routed to them - use `copilot-studio:studio-environments`.
- CI/CD for pro-code AI solutions, prompts and models - use `ai-engineering:ai-ci-cd`.
- Publishing the released agent to its channels - use `copilot-studio:studio-deployment`.
- Assessing the impact of a change to a live agent as a formal review - use `design-authority:ai-change-impact-review`.

## Questions to ask first

1. Which environments will this agent pass through, and who owns each?
2. What belongs with the agent - flows, connectors, tables, environment variables, child agents - and what is shared with other solutions?
3. What differs between environments: endpoints, connections, knowledge locations, sharing, authentication settings?
4. Who approves a release to production, and what evidence must accompany it?
5. If a release goes wrong, how quickly must the previous version be restored, and how?

## Required inputs

- The environment catalogue and zone rules from `copilot-studio:studio-environments`.
- The solution design, including tools, flows, connectors and Dataverse dependencies.
- The organisation's release policy by risk tier, from `platform-governance:ai-release-policy`.
- The source control and pipeline tools the organisation has approved.

If no release policy exists, record the approver and evidence agreed with the business owner as an interim rule, and
flag the gap to the platform owner.

## Decision framework

| Concern | Default | Stronger option when |
|---|---|---|
| Packaging | One solution per agent, with its flows and components, under the organisation's publisher | Shared components used by several agents go in a separate shared solution |
| Configuration | Environment variables for endpoints and settings; connection references for connections | Never hard-code values that differ between environments |
| Movement | Platform pipelines from development to test to production | Source-controlled pipelines with automated checks from tier 3 or many makers |
| Production imports | Managed solutions | Unmanaged only in development |
| Source control | Export solutions to a repository at each release | Every change committed, with pull request review, at scale |
| Change approval | Business owner approves with regression evidence | Reviewer approval by tier as the release policy sets |
| Rollback | Keep the previous managed version ready to re-import | Rehearsed rollback for tier 3 and above |

## Practitioner approach

Put the agent in a solution on day one. Create a solution with the organisation's publisher in the team development
environment before building, and add the agent, its flows, custom connectors, tables and environment variables as they
are created. Building outside a solution and adding things later is the main source of missing components at import.

Separate what changes per environment. Use environment variables for anything that differs - endpoints, site URLs,
queue names, feature flags - and connection references for every connection. Write down the values for each environment
in the `alm-and-environment-plan`. Knowledge sources pointing at development content, and connections created by the
maker, are the commonest reasons an imported agent misbehaves.

Decide on shared components early. When several agents use the same flows or custom connectors, place them in a shared
solution with its own owner and release cadence, and record which agent solutions depend on it. Without this, two teams
import different versions of the same flow and break each other.

Move changes through pipelines, not by hand. Use the platform's pipelines to promote from development to test to
production, importing managed solutions into test and production. As the number of makers or the risk tier grows, add
source control: export the solution at each release, commit it, review differences and keep the history. Pro-code style
pipelines with automated checks suit tier 3 and above or large teams.

Make production read-only for makers. Urgent fixes go through development and the pipeline, quickly if need be, so the
next import does not silently undo them. If an emergency change is ever made in production, record it and replay it in
development the same day.

Version and record every release: version number, changes, regression results, approver and date. Keep the previous
managed solution so rollback is a re-import, and rehearse rollback for higher-tier agents. Remember that some parts of an
agent's state - knowledge indexing, channel settings, connections - may need attention after import; include post-import
checks in the release steps.

Finally, put the plan on the `alm-and-environment-plan` template and review it when the agent's design changes.

## Outputs

- An ALM plan on the `alm-and-environment-plan` template: solutions, publisher, environment variables and connection references per environment, pipelines, source control, approvals and rollback.
- A release record per version: changes, regression evidence, approver, date and post-import checks.
- A shared component register where agents share flows or connectors.

## Microsoft platform considerations

Solution support for Copilot Studio components, platform pipelines, source control integration and post-import behaviour
for knowledge and channels are evolving. Check `ms-copilot-studio-guidance` for what is currently supported in solutions
and pipelines, and `ms-managed-environments` for pipeline and environment controls. Use `ms-coe-starter-kit` to find
agents and flows outside solutions.

## Adoption considerations

Makers resist ALM that feels like bureaucracy. Provide a template solution, a short guide and pipelines that take minutes,
and show makers that ALM is what lets their agent reach a wider audience.

## Knowledge considerations

Knowledge connections may point to different locations per environment, and uploaded files travel with the solution.
Record knowledge locations per environment and check knowledge after each import.

## Security and privacy considerations

Pipelines and service accounts used for deployment need least privilege and owners. Production is read-only for makers.
Secrets are never stored in solutions or repositories; use managed stores and connection references.

## Responsible AI considerations

Not applicable directly, because ALM moves agents rather than shaping behaviour; it supports responsible AI by ensuring
that the version reviewers approved is the version users receive.

## Evaluation requirements

Each release carries regression evidence from `copilot-studio:studio-testing-and-evaluation`, run in test against the
version being promoted. A release without regression evidence does not proceed beyond test.

## Value measures

Track lead time from change to production, failed imports, rollbacks and direct production changes, owned by the
Copilot Studio Architect and reported at agent and portfolio level.

## Scale notes

### Starter

One solution per agent, environment variables and connection references, platform pipelines from development to test to
production, and the previous version kept for rollback.

### Scale

Shared component solutions, source control for every release, a standard release record and pipelines with approvals set
by risk tier.

### Enterprise

Source-controlled pipelines with automated checks and regression runs, separation of duties between makers and approvers,
and release reporting across the portfolio.

## Hand-offs

- To `copilot-studio:studio-deployment` once a release reaches production.
- To `copilot-studio:studio-testing-and-evaluation` for regression evidence per release.
- To `design-authority:ai-change-impact-review` for significant changes to live agents.
- To `copilot-studio:studio-environments` where a new environment is needed.

## Reviewer gates

From risk tier 2, `design-authority` reviews the ALM plan for packaging, configuration and rollback, and checks that
production imports are managed and approved. Direct making in production for a tier 2 or higher agent is a blocking finding.

## Failure modes

- The agent is built outside a solution and components are missing at import.
- Hard-coded endpoints make the production agent call development systems.
- An emergency fix made in production is overwritten by the next import.
- Two agents import different versions of a shared flow and break each other.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Build a production-bound agent outside a solution.
- Make changes directly in production without replaying them through development.
- Store secrets in solutions, environment variable values or repositories.
- Promote a release to production without regression evidence and a recorded approver.

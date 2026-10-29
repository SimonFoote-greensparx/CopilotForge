---
name: code-deployment-readiness
description: Checks that an AI-built application is ready to deploy and run - validated, security-reviewed, deployed through a pipeline to approved hosting, with least-privilege identity, monitoring, a rollback plan, a support route, named owners and recorded release approval for its risk tier. Use when an AI-built application is about to go live, when a prototype is being promoted, or when an application is running somewhere nobody approved.
license: CC-BY-4.0
metadata:
  department: copilot-code
  lifecycle: Assure, Launch
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-code, github, azure, entra, power-platform
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, evaluation-quality, design-authority
  sources: nist-ai-rmf, ms-managed-environments
  status: draft
  authors: Simon Foote
---

# Code deployment readiness

## Purpose

An application built quickly with an AI coding agent arrives at deployment with the same operational needs as any other
software: somewhere approved to run, a repeatable way to deploy and roll back, monitoring, a support route and people who
own it. The speed of the build often means these were never planned. This skill checks readiness to deploy and run an
AI-built application against a proportionate checklist and records a go, conditional go or no-go. It goes wrong when
"deployment" means the developer publishing from their machine to a resource they created, and the organisation learns
the application exists when it fails.

## When to use

- An AI-built application has passed validation and is about to go live.
- A prototype is being promoted into production use.
- An AI-built application is found running somewhere that was never approved.
- A significant release of a live AI-built application is planned.

## When not to use

- Validating the application against its requirements - use `copilot-code:application-validation`.
- Security review of the generated code - use `copilot-code:generated-code-security-review`.
- Designing CI/CD pipelines for AI solutions, prompts and models - use `ai-engineering:ai-ci-cd`.
- Setting the organisation's release policy by risk tier - use `platform-governance:ai-release-policy`.
- Designing the ongoing support model for deployed AI solutions - use `ai-operations:ai-support-model`.

## Questions to ask first

1. Has the application passed validation and security review, with no open blocking findings?
2. Where will it run, is that hosting approved, and who controls it?
3. How is it deployed: through a pipeline from the organisation's repository, or by hand?
4. How will anyone know it is failing, and how is it rolled back?
5. Who supports users, who fixes it, and who owns it as a business service?
6. Which release approvals does its risk tier require, and have they been given?

## Required inputs

- The solution brief, validation verdict and security findings record.
- The organisation's approved hosting options, release policy and change process.
- The pipeline definition and environment configuration.
- Named business owner, engineering owner and support route.

If validation or security review is incomplete, the verdict is no-go. Never deploy to hosting the organisation has not
approved, and never treat a developer's personal subscription or environment as production.

## Decision framework

Check each area; the risk tier sets what is required.

| Area | Required from tier 1 | Additionally from tier 2 |
|---|---|---|
| Evidence | Validation pass or conditional pass; no open blocking security findings | Release evidence pack reviewed by the relevant reviewers |
| Hosting | Approved, organisation-controlled hosting and environment | Environment separation (test and production) and network controls reviewed |
| Deployment | Pipeline from the organisation's repository; no manual production changes | Approval step in the pipeline for production |
| Identity and secrets | Least-privilege managed identity or equivalent; secrets in a secrets store | Access reviewed by security |
| Monitoring | Errors and availability visible to the engineering owner | Alerts routed to a support rota; key business heartbeat checked |
| Rollback | Tested way to return to the previous version | Data migration rollback considered |
| Support and ownership | Named business owner, engineering owner and support route | Support model agreed with operations; review date set |
| Users | Users told what it does, how to get help and how to report problems | Transparency and accessibility confirmed |
| Approval | Release approved per release policy | Reviewer sign-offs recorded |

Go when every required item is met; conditional go when only advisory items remain with owners and dates; no-go otherwise.

## Practitioner approach

Start by confirming the evidence. The validation verdict and security findings record should exist and be current for the
version being deployed. If the agent has made changes since validation, re-run the regression suite and check whether any
change touched security-sensitive areas. Evidence for a previous version is not evidence for this one.

Confirm hosting is approved and owned. Many AI-built applications reach this point running in a developer's own
environment, subscription or tenant area. Move them to approved, organisation-controlled hosting before go-live, even if
that delays the date. An application on unapproved hosting has no guarantees about backup, security or continuity.

Make deployment repeatable. Deployment should run through a pipeline from the organisation's repository, so the version in
production is always known and can be rebuilt. Manual changes in production are the main way AI-built applications drift
from their reviewed code. From risk tier 2, add an approval step before production.

Check identity and secrets. The running application should use a managed identity or equivalent with only the permissions
the brief requires, and any remaining secrets should live in a secrets store. Check what the identity can actually do, not
what the design says.

Make failure visible and reversible. Confirm that errors and availability reach the engineering owner, and from tier 2 that
alerts reach a support rota. Test the rollback: deploy the previous version to a test environment using the same pipeline.
If the release includes data changes, decide how they would be reversed.

Confirm ownership and support in writing. The business owner answers for whether the application is still needed and
used; the engineering owner answers for keeping it running and secure; the support route tells users where to go. Set a
review date so the application is looked at again, and register it in the organisation's solution inventory.

Tell users. A short note on what the application does, what it does not, how to get help and how to report problems
reduces support load and builds trust. Record the verdict and approvals, and hand over to operations.

## Outputs

- A deployment readiness record: each area with status, evidence, owner and date, and a go, conditional go or no-go verdict.
- Recorded release approvals and reviewer sign-offs for the risk tier.
- A tested rollback procedure.
- An entry in the solution inventory with owners and review date.

## Microsoft platform considerations

Hosting may be Azure services, Power Platform environments or other approved Microsoft platforms; each has its own
environment, identity and governance controls, including Managed Environments for Power Platform. Use Microsoft Entra
managed identities where available. Confirm current platform features, limits and governance options in the source records
(`ms-managed-environments`) and with the platform team. Licensing and capacity questions go to the Microsoft licensing guide
or a licensing partner.

## Adoption considerations

Users need to know the application exists, what it is for and where to get help. Coordinate the go-live message with the
business owner and, for wider audiences, with the adoption or change team.

## Knowledge considerations

Not applicable as a primary concern, because readiness concerns running software; ensure the architecture note, runbook
and brief are stored with the repository so support staff can find them.

## Security and privacy considerations

No open blocking security findings, least-privilege identity, secrets in a store, approved hosting and environment
separation are prerequisites. From risk tier 2, the `security-privacy` reviewer signs off access and exposure before go-live.

## Responsible AI considerations

Where the application supports decisions about people or uses AI features at run time, confirm transparency to users and
that human decision steps work in production as validated. Route outstanding concerns to `responsible-ai:human-oversight`.

## Evaluation requirements

Validation evidence must match the version being deployed. From risk tier 2, the release evidence pack is reviewed through
`evaluation-quality:ai-release-evidence`.

## Value measures

Confirm the baseline and outcome measure from the brief, who will report it and when. Record deployment frequency and
failed deployments at team level as operational health indicators. Never use deployment data to assess individuals.

## Scale notes

### Starter

Approved hosting, a simple pipeline, error visibility, a tested rollback, named owners and a support contact. A partner may
host and support if no internal team can.

### Scale

Provide standard hosting patterns, pipeline templates and a readiness checklist through the CoE or engineering platform
team, and register every AI-built application.

### Enterprise

Integrate readiness into the organisation's change and release management, with automated checks in pipelines and
reviewer sign-offs recorded centrally from risk tier 2.

## Hand-offs

- To `ai-operations:ai-support-model` for ongoing support.
- To `platform-governance:ai-solution-inventory` to register the application.
- To `copilot-code:maintainability-review` at the first scheduled review.

## Reviewer gates

From risk tier 2, `security-privacy` signs off access and exposure, `evaluation-quality:ai-release-evidence` reviews release evidence, and
`design-authority` reviews supportability through `design-authority:supportability-review`. Findings are blocking or
advisory; go-live does not proceed with an open blocking finding.

## Failure modes

- The application goes live from a developer's own environment, and nobody can rebuild it when that person leaves.
- Manual changes in production drift from the reviewed code.
- Nobody is alerted when it fails, and users discover it first.
- Validation evidence is for an earlier version than the one deployed.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Deploy to hosting the organisation has not approved or does not control.
- Go live with an open blocking security finding and no written risk acceptance.
- Deploy without named business and engineering owners and a support route.
- State licensing or capacity conclusions; route them to the Microsoft licensing guide or a licensing partner.

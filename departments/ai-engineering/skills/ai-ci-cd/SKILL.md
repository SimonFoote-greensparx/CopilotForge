---
name: ai-ci-cd
description: Designs CI/CD pipelines for custom AI solutions that build, test, evaluate and deploy code, prompts, model configuration, tools and infrastructure together, with evaluation and safety gates, environment promotion, approvals, model version upgrades and rollback. Use when a pro-code AI solution needs a release pipeline, when prompts or models change outside the pipeline, or when a model version is being retired.
license: CC-BY-4.0
metadata:
  department: ai-engineering
  lifecycle: Deliver, Assure, Launch, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, github
  edition-support: starter, scale, enterprise
  reviewers: design-authority, evaluation-quality, security-privacy
  sources: ms-foundry-models, ms-responsible-ai, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# AI CI/CD

## Purpose

In ordinary software, the pipeline guards code. In AI solutions, a one-line prompt change or a model version update can
change behaviour more than a thousand lines of code, so the pipeline has to guard those too. This skill designs CI/CD
that treats prompts, model configuration, tool definitions, retrieval settings and infrastructure as releasable
artefacts, gated by tests and evaluation, promoted through environments with approvals and reversible when quality
drops. It goes wrong when prompts are changed in a portal, when evaluation runs only on code changes, and when a model
version is upgraded by the provider's schedule rather than the organisation's decision.

## When to use

- A pro-code AI solution on Microsoft Foundry or Azure needs a build and release pipeline.
- Prompts, model deployments or retrieval settings change in production outside any pipeline.
- A model version the solution uses is due for retirement and an upgrade must be tested and released.
- Releases are slow and manual, or have shipped regressions users found first.
- The organisation wants a standard pipeline template for custom AI work.

## When not to use

- Application lifecycle for Copilot Studio agents and Power Platform solutions - use `copilot-studio:studio-alm`.
- Readiness to deploy an AI-built application generally - use `copilot-code:code-deployment-readiness`.
- Building the evaluation harness the pipeline runs - use `ai-engineering:evaluation-harness`.
- Setting the release policy that decides who approves what by risk tier - use `platform-governance:ai-release-policy`.
- Choosing deployment topology and hosting options - use `ai-foundry:foundry-deployment-architecture`.

## Questions to ask first

1. Which assets change behaviour, and are they all in the repository?
2. How many environments are there, and what must be true before promotion to each?
3. Which gates are required by the risk tier and the release policy, and who approves production releases?
4. How will the team upgrade a model version, and how much notice does the provider give?
5. How is a bad release rolled back, and how quickly must that happen?

## Required inputs

- A repository structured per `ai-engineering:ai-solution-repository`, with behaviour-changing assets under version control.
- The evaluation harness and agreed thresholds from `ai-engineering:evaluation-harness`.
- The release policy by risk tier from `platform-governance:ai-release-policy`, or the organisation's change process.
- Workload identities for deployment per environment, from `ai-engineering:secrets-and-identity`.

If the release policy does not yet exist, use the risk tier's minimum gates from `opportunity-management:risk-classification`
and record the gap. Never let a pipeline deploy to production with personal credentials.

## Decision framework

Gates apply by stage and risk tier. A failed gate stops promotion; overriding it needs a recorded decision by the
accountable owner.

| Stage | Gate | Required from tier |
|---|---|---|
| Pull request | Build, unit and contract tests, linting, secret scan, dependency scan | 1 |
| Pull request | Evaluation subset when prompts, models, tools or retrieval change | 1 |
| Pull request | Review by owners of changed areas (prompt changes by solution and business owner) | 1 |
| Test environment | Infrastructure deployed from code; integration tests; full evaluation run | 2 |
| Test environment | Safety evaluation and security tests | 2 |
| Pre-production | Performance test against targets; release evidence assembled | 3 |
| Production | Approval by named approvers per release policy | 2 |
| Production | Progressive exposure (a small share of traffic or users first) with monitoring | 3 |
| After release | Smoke tests, telemetry checks, rollback trigger defined | 1 |

Model version upgrades are releases. They run the full evaluation and the same gates as a prompt or code change.

## Practitioner approach

Start by making everything a release. List the assets that change behaviour and confirm they live in the repository. If
a prompt can be edited in a portal in production, the pipeline is optional in practice. Lock down direct changes in
production and route them through pull requests, keeping a documented emergency path that is reviewed afterwards.

Trigger the right checks for the right change. Code changes run unit and contract tests. Changes to prompts, models,
tools or retrieval run the evaluation subset as well, because they change behaviour without changing code. Use path
filters so a documentation change does not trigger a costly evaluation, but err on the side of running it.

Deploy infrastructure and configuration from code to every environment, so test resembles production. Use workload
identities with federated credentials for the pipeline, scoped per environment, rather than stored secrets. Keep
production deployment rights with the pipeline, not with people.

Gate promotion on evidence. Before production, the pipeline should have the full evaluation results against thresholds,
safety evaluation, security scan results and, from tier 3, a performance test. Assemble these automatically into the
release evidence the reviewers need, rather than asking engineers to compile it by hand.

Release progressively for higher tiers. Expose the change to a small share of users or traffic, watch quality and
error signals for an agreed period, then widen. Define the rollback trigger before release: which signal, which
threshold, who decides. Rollback means redeploying the previous version of every asset, including prompt and model
configuration, not only the code.

Treat model upgrades as planned work. Track the versions in use and their retirement dates from the source records.
Well before retirement, open an upgrade branch with the new version pinned, run the full evaluation, compare results
with the current version and adjust prompts if needed. Release it through the normal gates. Never let an automatic
provider upgrade be the first test.

Keep the pipeline itself governed: definitions in the repository, changes reviewed, and run logs retained as evidence of
what was released, when and by whose approval.

## Outputs

- A pipeline definition in the solution repository covering build, test, evaluation, security, deployment and promotion.
- A gate matrix by stage and risk tier, linked to the release policy.
- A rollback procedure covering code, prompts, model configuration and infrastructure.
- A model version register with retirement dates and the next planned upgrade.
- Automatically assembled release evidence for `evaluation-quality:ai-release-evidence`.

## Microsoft platform considerations

GitHub Actions and Azure Pipelines both support environment approvals, workload identity federation and secret scanning;
Microsoft Foundry exposes deployments, evaluations and agent definitions through SDKs and APIs that pipelines can call.
Model lifecycle and retirement schedules for Foundry models are published by Microsoft and change; check
`ms-foundry-models` and other records in `references/sources.md` and record the dates relied on.

## Adoption considerations

Engineers accept gates that are fast, reliable and explain their failures. Keep the pull request path quick, make
evaluation reports readable in the pull request and fix flaky tests promptly, or teams will look for ways round the
pipeline.

## Knowledge considerations

Changes to the knowledge a solution grounds on can change behaviour without any release. Schedule evaluation runs
against current knowledge, and agree with knowledge owners how major content changes are signalled to the team.

## Security and privacy considerations

Pipelines are privileged. Use workload identities per environment with least privilege, protect pipeline definitions
with review, scan for secrets and vulnerable dependencies, and keep evaluation data with sensitive content out of
pipeline logs.

## Responsible AI considerations

Changes that alter how the solution treats people, its refusals or its safety behaviour need business owner approval and
safety evaluation before release. The release record should show who approved and on what evidence.

## Evaluation requirements

The pipeline runs the evaluation harness as a gate, the full set before production and a subset on behaviour-changing
pull requests. Results are stored with the configuration released, so any production version can be traced to its
evidence.

## Value measures

Track lead time for changes, change failure rate, time to restore after a bad release, regressions caught by gates
versus found in production, and releases with complete evidence. The AI engineering lead owns these at team level.

## Scale notes

### Starter

A single pipeline with build, tests, evaluation subset, secret scanning and a manual production approval, deploying to
two environments with workload identity.

### Scale

A shared pipeline template with gates by risk tier, automated release evidence, model version tracking and progressive
exposure for tier 3 solutions.

### Enterprise

Centrally maintained pipeline templates and policies, integration with change management, estate-wide model version
tracking and coordinated upgrade campaigns ahead of retirements.

## Hand-offs

- To `ai-engineering:evaluation-harness` for the evaluation the pipeline runs.
- To `evaluation-quality:ai-release-evidence` with assembled evidence for release decisions.
- To `ai-operations:ai-solution-monitoring` with post-release signals and rollback triggers.
- To `platform-governance:ai-release-policy` when gates and approvals need aligning with policy.

## Reviewer gates

From risk tier 2, `evaluation-quality` checks that evaluation gates run on behaviour-changing changes, `security-privacy`
checks pipeline identities and scans, and `design-authority` checks rollback and promotion design. A production path
that bypasses the pipeline is a blocking finding.

## Failure modes

- A prompt is edited directly in production, bypassing evaluation, and quality drops for weeks before anyone links cause and effect.
- Evaluation runs only on code changes, so a model or retrieval change ships untested.
- A model version is retired by the provider and the automatic replacement is the first test of the new behaviour.
- Rollback redeploys the code but not the prompt and model configuration, so the fault persists.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Allow prompts, model versions or retrieval settings to change in production outside the pipeline, except through a reviewed emergency path.
- Deploy to production with personal credentials.
- Treat a model version upgrade as routine maintenance that skips evaluation.
- Override a failed gate without a recorded decision by the accountable owner.

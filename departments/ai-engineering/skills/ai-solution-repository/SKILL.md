---
name: ai-solution-repository
description: Sets the repository structure for custom AI solutions so that code, system prompts, tool definitions, evaluation datasets, infrastructure as code and per-environment configuration are versioned together, owned and reviewable, with no secrets in source. Use when starting a pro-code AI solution, when prompts live outside source control, or when a team needs a standard repository template for Foundry or Azure AI work.
license: CC-BY-4.0
metadata:
  department: ai-engineering
  lifecycle: Mobilise, Deliver, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, github, copilot-code
  edition-support: starter, scale, enterprise
  reviewers: design-authority, security-privacy
  sources: ms-foundry-models, ms-agents-compare, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# AI solution repository

## Purpose

In custom AI solutions the behaviour lives in more than code: system prompts, tool descriptions, model and deployment
choices, retrieval settings and evaluation datasets all change what users get. When those live in a portal, a
notebook or someone's clipboard, nobody can say what changed, when, or why quality moved. This skill sets a repository
structure that versions every behaviour-changing asset together, makes ownership and review explicit, and keeps secrets
out. It goes wrong when prompts are edited live in a portal, when evaluation data is kept on a laptop, and when each
team invents its own layout so nothing can be reused or reviewed consistently.

## When to use

- A team is starting a pro-code AI solution on Microsoft Foundry or Azure and needs a repository layout.
- Prompts, tool definitions or model settings are edited in a portal and not tracked in source control.
- Quality changed after a release and nobody can tell which asset changed.
- The engineering lead wants a standard repository template for all custom AI work.
- An existing solution is being handed to another team and its repository is hard to understand.

## When not to use

- Giving an AI coding agent the right context and constraints in a repository - use `copilot-code:repository-context`.
- Building the pipeline that tests and deploys from the repository - use `ai-engineering:ai-ci-cd`.
- Setting the organisation's wider engineering standards for AI work - use `ai-engineering:ai-engineering-standards`.
- Versioning and engineering system prompts as a discipline - use `ai-foundry:foundry-prompt-engineering`.
- Application lifecycle for Copilot Studio agents in solutions - use `copilot-studio:studio-alm`.

## Questions to ask first

1. Which assets change the solution's behaviour: code, system prompts, tool schemas, model deployments, retrieval and index settings, safety settings?
2. Where are these assets today, and who can change them without review?
3. How many environments will the solution run in, and what differs between them?
4. Who owns the solution, and who must approve a change to prompts or evaluation thresholds?
5. Will several solutions share components (tool libraries, evaluators, prompt fragments), and how should they be versioned?

## Required inputs

- The solution brief or architecture, naming the components and platforms.
- The organisation's source control platform and branch policies, where they exist.
- The list of environments and the configuration that differs between them.
- Named owners for the solution, its prompts and its evaluation data.

If owners are not named, create the repository with an ownership file that marks them as "to confirm" and block merges
to the main branch until they are filled. Never assume a default owner.

## Decision framework

Every behaviour-changing asset has a home in the repository and a reviewer. Use this as the minimum layout; names may
follow the organisation's conventions.

| Area | Holds | Rule |
|---|---|---|
| Application code | Orchestration, API, tool implementations | Normal engineering review |
| Prompts | System prompts, templates, prompt fragments | Plain text files, one per prompt, reviewed by solution and business owner |
| Tool definitions | Tool names, descriptions, schemas | Versioned with the code that implements them |
| Model and deployment configuration | Model names, versions, deployment settings per environment | Declared, not set by hand in a portal |
| Retrieval configuration | Index schema, chunking, ranking settings | Versioned; changes trigger evaluation |
| Evaluation | Datasets, evaluators, thresholds, results history | Datasets versioned or referenced by immutable version; thresholds changed only with owner approval |
| Infrastructure | Infrastructure as code for all resources | No manual changes in production |
| Configuration | Per-environment settings and references to secrets | Secret values never in the repository |
| Documentation | Readme, architecture decision records, runbook, ownership file | Updated with each material change |

Choose one repository per solution by default. Move shared components into their own versioned packages only when at
least two solutions use them and someone owns them.

## Practitioner approach

Start by listing every asset that changes behaviour, with the team. Most teams name code and miss tool descriptions,
retrieval settings and content filter configuration. If a change to it could change what a user sees, it belongs in the
repository and in review.

Pull prompts out of code and out of portals. Store each system prompt and template as its own text file, so a reviewer
can read the diff in plain language. Business owners and reviewers who do not read code can review a prompt change if
it is a readable file with a clear diff. Load prompts at run time from the deployed version, and record the prompt
version with every response in telemetry so quality changes can be traced.

Declare model and deployment choices. Pin model versions in configuration per environment, and change them through a
pull request that runs the evaluation harness. Models are updated and retired by their providers; a pinned, declared
version turns a silent change into a reviewed one. Keep retrieval and index settings alongside, because they affect
quality as much as the model does.

Keep evaluation with the solution. The evaluation datasets, evaluators and thresholds are part of the solution's
definition of done. Version them, or reference an immutable version in a governed store when they contain sensitive data
that should not sit in source control. Record results history so trends are visible.

Treat infrastructure as code from the first day. Manual changes in a portal are invisible to review and impossible to
reproduce in the next environment. Where a resource cannot yet be declared, record the manual steps in the runbook as a
known gap.

Keep secrets out. Configuration holds references to a managed secret store and identities, never values. Turn on
secret scanning and push protection where the platform supports them, and follow `ai-engineering:secrets-and-identity`.

Set ownership and protection. Add an ownership file that routes prompt changes to the solution owner and business
owner, evaluation threshold changes to the business owner, and infrastructure changes to the platform owner. Protect the
main branch so changes need review and passing checks. Write architecture decision records for choices a successor
would otherwise question, such as why a particular model or retrieval approach was chosen.

Package the layout as a template repository, with the folder structure, ownership file, readme sections and pipeline
stubs, so new solutions start consistent.

## Outputs

- A repository layout for the solution, or an organisation template repository, following the decision framework.
- An ownership file mapping areas to reviewers, and branch protection settings.
- A readme with purpose, architecture summary, how to run, how to evaluate and owners.
- Architecture decision records for material choices, and a runbook stub.

## Microsoft platform considerations

Microsoft Foundry projects, model deployments, evaluation features and agent definitions can be managed through portals,
SDKs and infrastructure as code; GitHub and Azure DevOps both support branch protection and secret scanning. Which
assets can be declared as code changes as products evolve. Check current options in `references/sources.md`, and record
any asset that must still be managed by hand.

## Adoption considerations

Engineers adopt a template when it saves them time. Include working pipeline stubs, an example prompt file and an
example evaluation, so the first commit already builds and evaluates. Walk new teams through it rather than issuing it
as a policy.

## Knowledge considerations

Not applicable to grounding content itself, which stays in governed knowledge stores rather than the repository.
Retrieval configuration and index schemas belong in the repository; the content they index does not.

## Security and privacy considerations

No secrets, keys, connection strings or personal data in the repository or its history. Evaluation datasets containing
personal or confidential data are held in a governed store and referenced by version. Access to the repository follows
least privilege, and history rewrites to remove a leaked secret are followed by rotating that secret.

## Responsible AI considerations

Versioned prompts, models and thresholds make accountability possible: the organisation can show which version produced
an output and who approved it. Changes that alter how the solution treats people should require business owner approval
through the ownership file.

## Evaluation requirements

The repository must hold or reference the evaluation datasets, evaluators and thresholds, and the pipeline must run them
on changes to prompts, models, tools and retrieval settings. See `ai-engineering:evaluation-harness`.

## Value measures

Track, across solutions, the share of behaviour-changing assets under source control, changes made outside review, and
time for a new engineer to run and evaluate the solution locally. The AI engineering lead owns these measures.

## Scale notes

### Starter

One repository per solution with the minimum layout, prompts as files, pinned model versions, branch protection and
secret scanning. A short readme is enough.

### Scale

Publish a template repository, shared packages for common evaluators and tool clients with named owners, and consistent
ownership files across solutions.

### Enterprise

Govern templates and shared packages as internal products with versioning and release notes, use inner-source
contribution, and report repository conformance across the estate to the design authority.

## Hand-offs

- To `ai-engineering:ai-ci-cd` to build the pipeline on the repository.
- To `ai-engineering:evaluation-harness` to populate the evaluation area.
- To `ai-engineering:secrets-and-identity` for secret references and identities.
- To `ai-engineering:ai-engineering-standards` to fold the layout into the standards.

## Reviewer gates

From risk tier 2, `design-authority` checks that behaviour-changing assets are versioned and reviewed, and
`security-privacy` checks for secrets and sensitive data in source. A secret or personal data in the repository is a
blocking finding until removed and rotated.

## Failure modes

- Prompts are edited directly in a portal, quality drops and nobody can find what changed.
- Model versions are not pinned, a provider update changes behaviour and the team discovers it from users.
- Evaluation data lives on one engineer's laptop and is lost when they leave.
- A key is committed, removed in the next commit and never rotated, so it remains usable from history.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Store secrets, keys or connection strings in the repository.
- Let prompts, model versions or retrieval settings change in production outside source control and review.
- Keep evaluation datasets only on a personal device.
- Leave the main branch unprotected for a solution at tier 1 or above.

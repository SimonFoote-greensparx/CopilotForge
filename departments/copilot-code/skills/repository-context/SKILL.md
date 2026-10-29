---
name: repository-context
description: Prepares the repository context an AI coding agent works within - custom instructions, conventions, architecture notes, approved dependencies, protected areas, test commands and never-touch rules - so generated changes follow the organisation's standards. Use when a repository is first opened to a coding agent, when agent output keeps ignoring conventions, or when a team asks how to stop the agent touching secrets or sensitive code.
license: CC-BY-4.0
metadata:
  department: copilot-code
  lifecycle: Mobilise, Deliver, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-code, github, azure, entra
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Repository context

## Purpose

An AI coding agent reads what is in front of it: the code, the files it is pointed at and the instructions it is given.
If the repository does not state its conventions, approved libraries, architecture and boundaries, the agent follows its
own defaults and whatever patterns it happens to find, including the bad ones. This skill prepares the repository so the
agent works within the organisation's standards: clear instructions, conventions, a short architecture note, approved
dependencies, protected areas, how to build and test, and what must never be touched or committed. It goes wrong when
context is a long, generic document the agent and engineers both ignore, or when protection relies on asking the agent
nicely rather than on repository controls.

## When to use

- A repository is opened to a coding agent for the first time.
- Agent-generated changes keep ignoring conventions, adding unapproved libraries or touching areas they should not.
- A team asks how to keep secrets, configuration or security-sensitive code out of the agent's changes.
- Engineering standards change and the repository context needs updating.

## When not to use

- Structuring a repository for a custom AI solution built on Microsoft Foundry - use `ai-engineering:ai-solution-repository`.
- Setting engineering standards for custom AI work across the organisation - use `ai-engineering:ai-engineering-standards`.
- Managing secrets, managed identities and least privilege for AI solutions - use `ai-engineering:secrets-and-identity`.
- Writing work items for a specific build - use `copilot-code:requirements-to-build`.
- Writing context for a Copilot Cowork task - use `copilot-cowork:task-context-design`.

## Questions to ask first

1. What conventions, patterns and libraries should every change follow, and where are they written down today?
2. Which parts of the repository are sensitive (authentication, authorisation, payment, data access, infrastructure, pipelines) and need stricter review?
3. Where do secrets and environment configuration live, and how are they kept out of the repository?
4. How does someone build, run and test the code locally, in commands the agent can follow?
5. What can the agent's identity actually do in the repository and connected systems, and is that the least it needs?

## Required inputs

- The solution brief and constraints from `copilot-code:code-solution-brief`.
- The organisation's engineering standards and approved dependency list.
- The repository's current structure and any existing contributor guidance.
- The organisation's controls for branches, reviews, secrets scanning and pipelines.

If engineering standards do not exist, write the minimum the repository needs and route the gap to
`ai-engineering:ai-engineering-standards`. Never put secrets, credentials or real personal data into repository context.

## Decision framework

Use instructions for guidance and repository controls for protection.

| Need | Put it in instructions | Enforce it with controls |
|---|---|---|
| Conventions, patterns, naming | Yes, concise with pointers to examples | Linters and formatters in the pipeline |
| Approved dependencies | Yes, list and rule for adding new ones | Dependency review and scanning in the pipeline |
| Protected areas | Yes, name them and say they need an engineer | Code owners and required reviews on those paths |
| Secrets and configuration | Yes, say where they live and never to add them | Secret scanning, push protection, no secrets in the repository |
| Build and test commands | Yes, exact commands | Pipeline runs the same commands on every change |
| Agent permissions | Not applicable | Least-privilege identity, branch protection, no direct pushes to the main branch |

Rule: anything whose failure would be a security or data incident must be enforced by a control, not only stated in an
instruction. Instructions shape behaviour; controls prevent harm.

## Practitioner approach

Start by reading the repository as the agent would. Is there a clear statement of what the software does, how it is
structured, how to build and test it, and which patterns to follow? Most repositories rely on tribal knowledge that the
agent cannot reach. Write a short architecture note: the main components, how data flows, where the boundaries are, and
the one or two patterns new code should copy. Point to real examples in the codebase rather than describing patterns in
the abstract.

Write the custom instructions concisely. State the conventions that matter, the approved libraries and how to propose a
new one, the commands to build and test, the rule that tests accompany every change, and the areas that require an
engineer. Keep them to what the agent and a new engineer genuinely need; long instructions dilute the important rules.
Store them in the repository, version them, and review them when standards change. Confirm the current mechanism for
repository-level instructions from the relevant source records, because it evolves.

Mark protected areas both ways. Name them in the instructions so the agent knows to avoid or flag them, and enforce them
with code owners and required reviews so changes there cannot merge without the right engineer. Typical protected areas
are authentication, authorisation, data access layers, payment logic, infrastructure definitions and pipeline files.

Keep secrets out completely. Secrets and environment-specific configuration belong in a secrets store and pipeline
variables, never in the repository, examples or instructions. Turn on secret scanning and push protection. Assume that
anything the agent can read might appear in a change or a log.

Give the agent the least privilege it needs. It should work on branches, open pull requests and run tests, not push to the
main branch, change pipeline definitions or reach production systems. Check what its identity can actually do, not just
what the instructions say.

Make the pipeline the backstop. Linting, formatting, dependency review, security scanning and tests should run on every
change, so a convention the agent ignored is caught automatically. Then watch the first few agent pull requests closely:
where they go wrong, improve the context or the controls, not just the individual change.

## Outputs

- Repository custom instructions: conventions, approved dependencies, protected areas, build and test commands, and never-do rules.
- A short architecture note with pointers to example code.
- A controls checklist: code owners, branch protection, secret scanning, dependency review, pipeline checks and agent permissions.
- A list of gaps referred to engineering standards or platform owners.

## Microsoft platform considerations

Repository hosting, coding agents, custom instruction files, code owners, secret scanning and pipeline features are
provided by the organisation's development platform (often GitHub) and evolve. Confirm current capabilities from the
relevant source records and the organisation's platform team rather than relying on memory. Use Microsoft Entra and
managed identities for anything the software or pipelines access in Azure, so no long-lived secrets exist to leak.

## Adoption considerations

Engineers adopt agent context when it also helps them. A good architecture note and clear build commands speed up new
team members as much as the agent; present the work that way.

## Knowledge considerations

Repository context is engineering knowledge. Give it an owner (usually the engineering owner), version it with the code
and review it when standards or architecture change, so it does not drift into misleading the agent.

## Security and privacy considerations

Protection relies on controls, not instructions. Secret scanning, push protection, code owners on sensitive paths,
least-privilege agent identity and branch protection are the minimum. From risk tier 2, the controls checklist goes to the
`security-privacy` reviewer through `security-privacy:ai-identity-and-access-review`.

## Responsible AI considerations

Not applicable as a primary concern, because repository context governs how code is written rather than how the software
affects people; responsible AI questions about the software itself are handled in the brief and validation.

## Evaluation requirements

Check the context works by reviewing the first few agent pull requests against it: conventions followed, no unapproved
dependencies, protected areas untouched or correctly flagged. Record what was fixed in the context as a result.

## Value measures

Track at team level the share of agent pull requests that pass pipeline checks first time and the number of review
comments about conventions, before and after context is improved. Never use these to assess individual engineers.

## Scale notes

### Starter

A one-page instructions file, a short architecture note, secret scanning and branch protection are enough for a first
repository.

### Scale

Provide a standard repository template with instructions, controls and pipeline checks, so every new repository starts
with them.

### Enterprise

Manage organisation-wide instructions and controls centrally through the development platform, with repositories adding
their own specifics, and audit agent permissions across repositories regularly.

## Hand-offs

- To `copilot-code:requirements-to-build` so work items reference the context rather than repeat it.
- To `copilot-code:generated-code-review` with the conventions reviewers check against.
- To `security-privacy:ai-identity-and-access-review` from risk tier 2 for agent permissions.
- To `ai-engineering:ai-engineering-standards` with gaps in standards.

## Reviewer gates

From risk tier 2, `security-privacy` reviews the controls checklist and the coding agent's permissions. Findings are blocking
or advisory; secrets in the repository or an agent able to push to the main branch are blocking.

## Failure modes

- Protection relies on an instruction ("do not touch the auth module") with no code owners or required reviews behind it.
- Instructions grow into a long generic document that the agent and engineers both ignore.
- The agent's identity has broad permissions, so a bad change reaches the main branch or a pipeline.
- Secrets in an old configuration file are read and reproduced in a generated change.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Put secrets, credentials or real personal data in the repository or in agent instructions.
- Rely on instructions alone to protect security-sensitive code.
- Give the coding agent permission to push directly to the main branch or change pipelines unreviewed.
- Let repository context go unowned.

---
name: generated-code-security-review
description: Reviews AI-generated code for weaknesses coding agents commonly introduce - injection, broken authorisation, secrets, unsafe dependencies, broad permissions and data leakage - and classifies each finding as blocking or advisory with a fix. Use when an AI-built application or significant generated change nears release, when generated code touches identity or data access, or when a new dependency was added by the agent.
license: CC-BY-4.0
metadata:
  department: copilot-code
  lifecycle: Assure, Launch
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-code, github, azure, entra
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: nist-ai-rmf, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Generated code security review

## Purpose

AI coding agents produce code that compiles, passes its tests and looks idiomatic, which makes security weaknesses easy to
miss. They reproduce insecure patterns from their training and from the repository, add dependencies freely, handle
errors by printing everything, and implement authorisation as the happy path. This skill is the security review an
engineering team carries out on AI-generated code before release: a focused check of the weaknesses coding agents most
often introduce, using tools and human reading together, with each finding classified as blocking or advisory and given a
specific fix. It goes wrong when automated scanners are treated as the whole review, or when the review starts after the
release date is fixed.

## When to use

- An AI-built application or a significant generated change is approaching release.
- Generated code touches authentication, authorisation, data access, payments or external integrations.
- The coding agent added or upgraded dependencies.
- A prototype is being promoted towards production.

## When not to use

- General code quality, readability and correctness review - use `copilot-code:generated-code-review`.
- Security testing of AI features inside a solution, such as prompt injection against a model - use `security-privacy:ai-security-testing`.
- Reviewing identity and access design for an AI solution as the security gate - use `security-privacy:ai-identity-and-access-review`.
- Reviewing connectors and actions used by agents - use `security-privacy:connector-review`.
- Setting up repository controls such as secret scanning and code owners - use `copilot-code:repository-context`.

## Questions to ask first

1. What data does the application handle, how sensitive is it, and where does it flow (from the solution brief)?
2. Which parts of the code enforce identity and authorisation, and were they designed by an engineer or generated?
3. What external systems, APIs and dependencies does the code call or include, and which were added by the agent?
4. Where could untrusted input reach a query, command, file path, template or external call?
5. What do logs, error messages and telemetry contain?

## Required inputs

- The solution brief, especially the data and systems section.
- Access to the full code, dependency manifests, pipeline definitions and infrastructure definitions.
- Results of automated scanning (static analysis, dependency and secret scanning) from the pipeline.
- The organisation's secure coding standards and risk tier for the application.

If automated scanning is not in place, the review proceeds manually and its absence is an advisory finding at tier 1 and a
blocking finding from tier 2. Never review against production secrets or real personal data.

## Decision framework

Check each area and classify every finding.

| Area | Common AI-generated weakness | Blocking when |
|---|---|---|
| Authorisation | Checks only that the user is signed in, not that they may access this record | Any user can reach another user's or another unit's data |
| Input handling | String-built queries, commands or paths; unescaped output | Untrusted input reaches a query, command, path or page unsanitised |
| Secrets | Keys in code, configuration, tests or examples | Any secret is in the repository or its history |
| Dependencies | Unapproved, unmaintained, vulnerable or non-existent packages suggested by the agent | Known exploitable vulnerability, or a package that cannot be verified as genuine |
| Permissions | Service identities with broad rights; wide token scopes | Write or admin rights beyond what the brief requires |
| Data leakage | Full objects, tokens or personal data in logs and error responses | Personal data, secrets or internal details exposed to users or logs without need |
| External calls | No validation of responses, no timeouts, calls to URLs built from input | Server-side requests to attacker-influenced destinations |
| Infrastructure and pipelines | Public endpoints, disabled protections, pipeline changes | Production resources exposed or pipeline controls weakened |

Advisory findings are weaknesses that do not create an exploitable path today but should be fixed, with an owner and date.
A blocking finding stops release; it is not traded off against a date. Disagreement goes to the accountable executive for
written risk acceptance.

## Practitioner approach

Start with the data flow in the brief. Draw, even roughly, where data enters, where it is stored, who can read it and
where it leaves. This tells you which parts of the code matter most and focuses a human review that could otherwise drown
in generated volume.

Run the automated tools first and treat their output as a starting list, not a verdict. Static analysis, dependency
scanning and secret scanning catch the obvious problems quickly. They miss most authorisation flaws, because a missing
check is not a pattern a scanner can see, and they cannot tell whether a dependency was a sensible choice.

Read the authorisation code by hand. For every endpoint, page or function that returns or changes data, ask: who may do
this, and where in the code is that enforced? Coding agents frequently check that a user is authenticated and stop there,
or enforce rules in the user interface but not on the server. Write or request negative tests for each rule if
`copilot-code:application-validation` has not already.

Trace untrusted input. Follow input from forms, query strings, files, messages and external APIs to where it is used.
Look for string-built queries, shell commands, file paths, templates and URLs. Parameterised queries and framework
encoding should be used everywhere; any exception needs a reason.

Check every dependency the agent added. Confirm it exists, is the genuine package, is maintained, is on the approved list
or justified, and has no known exploitable vulnerability. Coding agents sometimes suggest packages that do not exist or
have names close to popular ones; an attacker can register such names. Pin versions and record why each new dependency is
needed.

Look at what leaves the system unintentionally. Read logging statements and error handlers: generated code often logs
whole request objects or returns stack traces. Check telemetry configuration for personal data.

Review identities and infrastructure. Service identities, token scopes, network exposure and pipeline changes should match
the brief's least-privilege intent. Prefer managed identities over stored secrets.

Record each finding with area, evidence, classification, fix, owner and date. Re-review fixes for blocking findings before
release. Questions about the licensing or provenance of generated code go to the organisation's legal adviser, not to this
review.

## Outputs

- A security findings record: each finding with area, evidence, blocking or advisory classification, fix, owner and date.
- A dependency register for agent-added packages with justification and verification.
- A release recommendation: no blocking findings open, or blocked with the findings listed.

## Microsoft platform considerations

Use the development platform's code scanning, dependency review and secret scanning, and Microsoft Entra managed
identities for access to Azure resources, so no long-lived secrets exist. Capabilities and configuration options of these
tools change; confirm current features in the relevant source records and with the platform team rather than memory.

## Adoption considerations

Engineers learn fastest from findings in their own code. Share recurring weakness patterns with the team and feed them back
into repository instructions and work item templates, so the agent is steered away from them next time.

## Knowledge considerations

Not applicable as a primary concern, because the review examines code; recurring findings should be captured as secure
coding guidance in the repository context and engineering standards.

## Security and privacy considerations

This skill is the engineering team's security review. From risk tier 2, its findings record is evidence for the
`security-privacy` reviewer, who may add findings of their own. Where the application processes personal data, confirm a
privacy assessment exists through `security-privacy:privacy-assessment`.

## Responsible AI considerations

Not applicable as a primary concern, because the review addresses security weaknesses in code; responsible AI questions
about what the software does to people are handled in the brief and validation.

## Evaluation requirements

Every blocking finding must have a fix that is re-reviewed, and, where practical, a test that would fail if the weakness
returned. Record these tests in the regression suite.

## Value measures

Track at team level the number of blocking findings found before release versus after, and recurring weakness categories
over time. Falling recurrence shows context and standards are working. Never use findings to rank engineers.

## Scale notes

### Starter

Automated scanning, a manual read of authorisation, input handling, secrets and new dependencies, and a short findings
list. Use a partner for anything at risk tier 2 or above if no security engineer is available.

### Scale

Standardise the review checklist for AI-generated code, make scanning mandatory in pipelines, and have a security
champion in each engineering team.

### Enterprise

Integrate findings into the organisation's vulnerability management, require independent security review from risk tier 3,
and track recurring patterns across repositories to improve shared instructions and templates.

## Hand-offs

- To `security-privacy:ai-identity-and-access-review` from risk tier 2.
- To `copilot-code:repository-context` with recurring weaknesses to steer the agent away from.
- To `copilot-code:code-deployment-readiness` with the release recommendation.

## Reviewer gates

From risk tier 2, `security-privacy` reviews the findings record and may add findings; blocking findings stop release until
fixed and re-reviewed, or until the accountable executive accepts the risk in writing.

## Failure modes

- Automated scans pass and the review stops, missing an authorisation check that only exists in the user interface.
- The agent adds a package with a name close to a popular one, and nobody checks it is genuine.
- Generated error handling returns stack traces and tokens to users.
- The review starts after the release date is fixed, and blocking findings are argued away.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Release AI-generated code with an open blocking finding and no written risk acceptance.
- Treat automated scanning as the whole security review.
- Accept an agent-added dependency without confirming it is genuine and justified.
- Give legal conclusions on the licensing or provenance of generated code; route them to the legal adviser.

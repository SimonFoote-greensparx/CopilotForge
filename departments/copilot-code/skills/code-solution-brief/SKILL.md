---
name: code-solution-brief
description: Writes the solution brief that frames an AI-assisted software build - outcome, users, scope and exclusions, data and systems touched, constraints and non-functional needs, acceptance criteria, owners and route to production - so the coding agent and reviewers work to one agreed definition. Use when a Copilot Code build has been approved, when a prototype is being promoted, or when a build is drifting because nobody wrote down what it is for.
license: CC-BY-4.0
metadata:
  department: copilot-code
  lifecycle: Envision, Deliver
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-code, github, azure, power-platform
  edition-support: starter, scale, enterprise
  reviewers: design-authority, security-privacy
  sources: ms-responsible-ai, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Code solution brief

## Purpose

An AI coding agent will build something from almost any request, quickly and with confidence. That makes the brief more
important, not less: without an agreed outcome, scope, constraints and acceptance criteria, the agent fills the gaps with
plausible assumptions, and the team discovers them in review or in production. This skill writes a short, specific
solution brief that business owner, engineers, the coding agent and reviewers all work from. Builds go wrong here when the
brief is a feature wish-list with no exclusions, no data boundaries and no named owner.

## When to use

- A build has been approved through `copilot-code:code-use-case-assessment`.
- A prototype is being considered for promotion to something people will rely on.
- A build in progress is drifting and nobody can say what is in or out of scope.
- A reviewer asks for the document that defines what the software is meant to do.

## When not to use

- Deciding whether to build with Copilot Code at all - use `copilot-code:code-use-case-assessment`.
- Breaking the brief into work items and acceptance tests - use `copilot-code:requirements-to-build`.
- Giving the coding agent repository conventions and constraints - use `copilot-code:repository-context`.
- Setting non-functional requirements patterns across AI solutions - use `ai-architecture:ai-non-functional-requirements`.
- Briefing a reusable agent rather than an application - use `m365-agents:agent-use-case-design`.

## Questions to ask first

1. What outcome does the software deliver, for which users, and how will the business owner know it works?
2. What is explicitly out of scope, including tempting features that would change the risk or the effort?
3. Which data and systems will it read, write or send to, and under whose identity?
4. What constraints apply: hosting, approved languages and frameworks, accessibility, performance, availability, retention?
5. Who are the business owner, engineering owner and support route, and have they agreed?
6. Is this a prototype with an end date or a production build, and what is the route to production?

## Required inputs

- The code use-case verdict and ownership answers from `copilot-code:code-use-case-assessment`.
- The risk tier from `opportunity-management:risk-classification`.
- The organisation's engineering standards, approved stacks and hosting options.
- Examples of the current workaround (spreadsheets, forms, reports), cleaned of personal data.

Where an input is missing, mark it `[To confirm]` in the brief and keep the brief in draft. Never name an owner who has not
agreed, and never assume a hosting route or framework is approved.

## Decision framework

The brief is ready for build when each section passes.

| Section | Ready when | Not ready if |
|---|---|---|
| Outcome | One sentence naming users, job and measure | Describes features rather than outcome |
| Users and roles | Roles, approximate numbers and access levels | "Everyone" with no access model |
| Scope and exclusions | In-scope capabilities listed; exclusions written with reasons | No exclusions, or "phase 2" used to hide scope |
| Data and systems | Each data set and system named, with read, write or send and the identity used | "Connects to finance" |
| Constraints and non-functional needs | Hosting, stack, security, accessibility, performance and retention stated | Left for the agent to decide |
| Acceptance criteria | Testable statements the business owner agrees | "Works well" or "users like it" |
| Ownership and support | Business owner, engineering owner and support route agreed | Owner is the requester by default |
| Route | Prototype with end date, or production route with environments and gates | Unclear whether people may rely on it |

## Practitioner approach

Write the outcome first, in the business owner's words, with a measure: "Site managers record safety inspections on a
tablet and the weekly compliance report is produced automatically, so the report is on time and nobody re-keys data."
Everything else in the brief serves that sentence. If the owner cannot agree a single outcome, the build is two builds or
not yet ready.

Write exclusions with the same care as scope. Coding agents are generous: asked for a form, they will add authentication,
exports and dashboards. Each addition expands the security surface and the maintenance burden. List what the software will
not do, and why, so that reviewers can push back on scope creep that arrives in a pull request.

Name every data set and system, with direction and identity. "Reads inspection templates from a SharePoint list using the
signed-in user's identity; writes completed inspections to the same list; sends a weekly summary email from a service
account" is reviewable. "Integrates with SharePoint" is not. This section drives the security review and is where most
risk is found or missed.

State constraints the agent must not decide for itself. Approved languages, frameworks and hosting; accessibility
requirements; data retention; logging; secrets handling; and anything the organisation forbids, such as storing personal
data outside approved locations. Unstated constraints are filled with the agent's defaults, which are rarely the
organisation's standards.

Write acceptance criteria as testable statements. "An inspection saved offline uploads when the device reconnects, with no
duplicate record" can be tested; "works offline" cannot. Include negative criteria: what must not be possible, such as a
site manager seeing another site's inspections. These criteria become the backbone of `copilot-code:requirements-to-build`
and `copilot-code:application-validation`.

Agree ownership and route in writing. Name the business owner, engineering owner and support route, and state whether
this is a prototype with an end date or a production build with environments, reviews and a deployment path. A brief that
leaves this open allows a prototype to become production by stealth.

Keep the brief short, versioned in the repository alongside the code, and updated when scope changes. Walk the business
owner through it before build starts; a brief they cannot explain back is not finished.

## Outputs

- A solution brief on the `code-solution-brief` template: outcome, users, scope and exclusions, data and systems, constraints, acceptance criteria, ownership, route and risk tier.
- An initial list of acceptance criteria, including negative criteria, for `copilot-code:requirements-to-build`.
- Open questions and preconditions, each with an owner and a date.

## Microsoft platform considerations

Record the intended hosting and integration route (for example Azure services, Power Platform, Microsoft 365 data through
approved APIs) and the identity approach, and confirm current options and limits from the relevant source records before
the brief is agreed. Repositories, pipelines and hosting must sit under organisational control. Licensing questions go to
the Microsoft licensing guide or a licensing partner.

## Adoption considerations

Involve two or three intended users in writing the outcome and acceptance criteria; they will test it later and tell
colleagues whether it is worth using. Note how users will learn about and be supported in the new tool.

## Knowledge considerations

Not applicable as a primary concern, because the brief defines software rather than knowledge; where the software surfaces
documents or reference content, name the source and its owner in the data section.

## Security and privacy considerations

The data and systems section is the input to `copilot-code:generated-code-security-review`. Record personal data, external
endpoints, write access to systems of record and any service identities. From risk tier 2, share the brief with the
`security-privacy` reviewer before build.

## Responsible AI considerations

If the software uses AI features at run time or supports decisions about people, record that in scope and route to the
`responsible-ai` department through risk classification. State how users will know when content is AI-generated.

## Evaluation requirements

The acceptance criteria are the evaluation standard for `copilot-code:application-validation`. Where the software includes
AI features at run time, add quality criteria for those features and route them to `ai-engineering:ai-solution-testing`.

## Value measures

Record the baseline from the current workaround and the measure the business owner will use, with source and review date.
Include the expected ongoing ownership effort so value is judged net of it. Measure at team or role level.

## Scale notes

### Starter

Two pages is enough: outcome, users, scope and exclusions, data and systems, five to ten acceptance criteria, owners and
route. A partner may help with constraints.

### Scale

Use the full template for every production build through the CoE or engineering intake, stored in the repository, and
check it against engineering standards before build.

### Enterprise

Business-unit engineering teams write briefs on the shared template; briefs at risk tier 2 and above are reviewed by
design authority and security before build, and tracked in the engineering portfolio.

## Hand-offs

- To `copilot-code:requirements-to-build` with scope and acceptance criteria.
- To `copilot-code:repository-context` with constraints and standards.
- To `copilot-code:generated-code-security-review` with the data and systems section.
- To `copilot-code:ai-assisted-prototyping` where the route is prototype only.

## Reviewer gates

From risk tier 2, `design-authority` reviews the brief through `design-authority:ai-design-review` for route, architecture
and supportability, and `security-privacy` reviews data, systems and identities. Findings are blocking or advisory; build
does not start with an open blocking finding.

## Failure modes

- No exclusions are written, and the coding agent adds features that widen the security surface.
- Data and systems are described vaguely, so the security review misses a write path to a system of record.
- Acceptance criteria are untestable, so validation becomes a demonstration.
- The route is left open, and a prototype becomes production without the gates.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Start a production build without agreed acceptance criteria and named owners.
- Leave hosting, stack or data handling for the coding agent to decide.
- Include real personal data in examples attached to the brief.
- State licensing conclusions; route them to the Microsoft licensing guide or a licensing partner.

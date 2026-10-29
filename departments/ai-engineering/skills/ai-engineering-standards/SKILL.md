---
name: ai-engineering-standards
description: Sets and maintains engineering standards for custom AI work - minimum practices by risk tier for repositories, identity, tools, testing, evaluation, pipelines, telemetry, performance, resilience and ownership - with a checklist, exception route and review cycle. Use when pro-code AI work starts, when teams build AI solutions inconsistently, or when standards need refreshing after platform change.
license: CC-BY-4.0
metadata:
  department: ai-engineering
  lifecycle: Mobilise, Deliver, Assure, Scale, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, github, copilot-code, entra
  edition-support: starter, scale, enterprise
  reviewers: design-authority, security-privacy, evaluation-quality
  sources: ms-foundry-models, ms-responsible-ai, nist-ai-rmf, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# AI engineering standards

## Purpose

When each team builds custom AI solutions its own way, reviewers face a new design every time, operations inherit
solutions they cannot support, and the same mistakes (keys in code, prompts edited in production, no evaluation gate)
recur across the estate. This skill sets a short, enforceable set of engineering standards for pro-code AI work, scaled
by risk tier, with a checklist teams use during build, an exception route for justified departures and a review cycle
that keeps the standards current as Microsoft's platforms change. It goes wrong when standards are long documents nobody
reads, when every rule applies to every prototype, and when standards are written once and never revisited.

## When to use

- The organisation is starting pro-code AI work on Microsoft Foundry, Azure or with Copilot Code and needs common standards.
- Teams build AI solutions inconsistently, and reviews keep finding the same issues.
- The design authority needs a reference to review conformance against.
- Platform changes (new deployment options, evaluation features, identity capabilities) make existing standards stale.
- A partner or supplier is building AI solutions and needs to know what the organisation expects.

## When not to use

- Reviewing a solution's conformance against the standards - use `design-authority:architecture-conformance`.
- Maintaining reference architectures for common AI patterns - use `ai-architecture:ai-reference-architecture`.
- Code review standards specific to AI-generated code - use `copilot-code:generated-code-review`.
- Build patterns for Power Automate flows - use `automation:flow-design-patterns`.
- Setting release policy and approvals by risk tier - use `platform-governance:ai-release-policy`.

## Questions to ask first

1. Which kinds of custom AI work does the organisation do or plan (Foundry agents, retrieval solutions, AI APIs, AI-built applications), and how many teams do it?
2. What engineering standards already exist for ordinary software, and which can AI work simply inherit?
3. Which recurring problems have reviews, incidents or audits found in AI solutions so far?
4. Who will own the standards, approve exceptions and review them?
5. How will teams be supported to meet the standards (templates, shared components, clinics)?

## Required inputs

- Existing software engineering, security and change standards, so AI standards add to rather than duplicate them.
- The risk tier model from `opportunity-management:risk-classification`.
- Findings from reviews, incidents and post-implementation reviews of AI solutions, where any exist.
- The organisation's platforms and tooling for source control, pipelines, identity and monitoring.

If no existing engineering standards exist, start with the AI-specific minimum in the decision framework and record the
wider gap for the engineering lead. Never present draft standards as mandatory before the owner has approved them.

## Decision framework

Standards are stated as testable requirements, each with the tier from which it is mandatory and the evidence that shows
it is met. This is the core set; the `engineering-standards-checklist` template carries the full checklist.

| Area | Minimum standard | Mandatory from tier |
|---|---|---|
| Repository | Behaviour-changing assets (prompts, model configuration, tools, retrieval settings, evaluation) in source control with owners | 1 |
| Identity and secrets | Managed or workload identities; no secrets in source; user context for user-scoped data | 1 |
| Tools and APIs | Narrow, described, validated, authorised tools; writes idempotent and confirmed | 1 |
| Testing | Unit and failure-path tests with stubbed models; adversarial and permission tests | 1 (adversarial from 2) |
| Evaluation | Automated harness with thresholds agreed in advance; gate on behaviour-changing changes | 2 |
| CI/CD | Pipeline deployment only; gates by tier; rollback of all assets | 2 |
| Telemetry | End-to-end tracing with versions, tokens and outcomes; content capture decided with the DPO | 2 |
| Performance | Targets agreed; per-step budgets; load test before production | 3 |
| Resilience | Timeouts, bounded retries, evaluated fallbacks, designed degraded mode, failure tests | 2 (failure tests from 3) |
| Documentation and ownership | Readme, decision records, runbook, named owners for solution, prompts and evaluation | 1 |

Prototypes in sandbox environments with no real users or sensitive data may follow a lighter set, recorded as such, and
must meet the full set before any wider use.

## Practitioner approach

Start from what goes wrong. Gather findings from reviews, incidents and post-implementation reviews, and the recurring
questions reviewers ask. Standards that prevent problems the organisation has actually had are easier to justify and
adopt than a generic catalogue.

Inherit before inventing. Most good software practice (version control, code review, dependency scanning, change
control) applies to AI solutions unchanged. Point to existing standards and add only what AI work needs: prompts and
model configuration as versioned assets, evaluation as a gate, model version lifecycle, content capture in telemetry,
tool safety and model-specific failure handling.

Write each standard as a testable requirement with evidence. "Solutions should be well tested" cannot be checked;
"failure paths for model timeout, content filter block and malformed output are covered by automated tests" can. For each
standard, name the evidence a reviewer looks for and the risk tier from which it is mandatory. Keep the core set short
enough to fit on a page; detail lives in the linked skills and templates.

Scale by tier. A tier 1 internal tool and a tier 4 customer-facing service should not carry the same burden. The tier
column makes proportionality explicit and stops prototypes being smothered or production systems being under-governed.

Make conformance easy. Back every standard with something that helps meet it: a template repository, pipeline templates,
shared evaluators, identity starter code, telemetry libraries. A standard without an easy path generates exceptions and
resentment. Run clinics where teams can ask how to meet a standard before a review finds they have not.

Provide an exception route. Some departures are justified. An exception states the standard, the reason, the
compensating control, the risk accepted, who approved it and when it will be reviewed. Exceptions are recorded against
the solution and reviewed; a pattern of exceptions to one standard means the standard or its support needs changing.

Keep it current. Microsoft's AI platforms change quickly. Review the standards on a fixed cycle and when a significant
platform change lands, checking the source records rather than memory. Publish a short change note with each revision
so teams know what changed and why. Retire standards that no longer prevent anything.

## Outputs

- The AI engineering standards: a short core set by area, each with requirement, evidence and mandatory tier.
- The `engineering-standards-checklist` template, used by teams during build and by reviewers at the gate.
- An exception register: standard, solution, reason, compensating control, approver, review date.
- A revision history with change notes, and the date of the next scheduled review.

## Microsoft platform considerations

Standards should describe outcomes (keyless access, versioned prompts, gated evaluation) rather than depend on a specific
product feature, so they survive renames and changes. Where a standard relies on a Microsoft capability, such as Foundry
evaluation, managed identities or a deployment type, link to the source record in `references/sources.md` and recheck it
at each review.

## Adoption considerations

Engineers adopt standards they helped shape and that save them effort. Draft with practising engineers, pilot on one or
two solutions, and lead with templates and shared components rather than enforcement. Report conformance by solution and
team, never by individual engineer.

## Knowledge considerations

The standards and checklist are knowledge assets in their own right: keep them in one maintained location, owned by the
AI engineering lead, and point skills, templates and reviewers to that location rather than copies.

## Security and privacy considerations

Identity, secrets, tool authorisation, adversarial testing and telemetry content capture are the security and privacy
core of the standards. Agree these sections with the security and privacy lead so the standards and the `security-privacy`
reviews ask the same questions.

## Responsible AI considerations

Standards should require that safety evaluation, human confirmation for consequential actions and honest failure
behaviour are engineered in, not added later. Align the relevant standards with the `responsible-ai` department's review
expectations.

## Evaluation requirements

Evaluation as a gate is itself a standard. Align thresholds, harness requirements and evidence with the `evaluation-quality`
department so teams meet one set of expectations.

## Value measures

Track conformance by standard across solutions, recurring review findings, open exceptions past review date and incidents
traceable to a missing standard. The AI engineering lead owns these and reports them to the design authority.

## Scale notes

### Starter

A one-page set of the most important standards for tier 1 and 2 work, a template repository and a short checklist at
release. The AI engineering lead approves exceptions.

### Scale

The full core set by tier with the checklist, shared components behind each standard, exception register and a fixed
review cycle aligned with design authority reviews.

### Enterprise

Standards governed through the design authority with federated contribution from engineering teams, automated
conformance checks in pipelines where possible, and estate-wide conformance reporting.

## Hand-offs

- To `design-authority:architecture-conformance` to review solutions against the standards.
- To `ai-engineering:ai-solution-repository` and `ai-engineering:ai-ci-cd` for templates that implement them.
- To `platform-governance:ai-release-policy` to align gates with release policy.
- To `ai-architecture:ai-reference-architecture` where standards and reference architectures need to agree.

## Reviewer gates

From risk tier 2, `design-authority` reviews solutions against these standards, with `security-privacy` and
`evaluation-quality` reviewing their sections. The standards themselves are approved by the design authority, and an
unapproved exception to a mandatory standard at the solution's tier is a blocking finding.

## Failure modes

- Standards are a long document nobody reads, and reviews keep finding the same issues.
- Every standard applies to every prototype, so teams build outside governance to avoid the burden.
- Standards are written once, platforms move on, and the rules end up demanding obsolete practices.
- Exceptions are granted informally, never reviewed, and quietly become the norm.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Publish a standard that cannot be tested with named evidence.
- Apply production standards to sandbox prototypes, or sandbox leniency to production solutions.
- Grant an exception without a reason, a compensating control, an approver and a review date.
- Use conformance data to rank individual engineers.

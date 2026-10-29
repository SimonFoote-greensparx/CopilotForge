---
name: maintainability-review
description: Reviews whether an AI-built application can be understood, changed and kept secure by people over its life - ownership, comprehension without the agent, documentation, tests, dependency upkeep and spread of knowledge - and recommends keep, invest, consolidate or retire. Use when an AI-built application reaches its scheduled review, when its owner is leaving, or when a growing estate of AI-built tools needs triage.
license: CC-BY-4.0
metadata:
  department: copilot-code
  lifecycle: Measure, Scale, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-code, github, azure, power-platform
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Maintainability review

## Purpose

The cost of software is mostly in its life after launch: fixing, changing, patching and eventually retiring it. AI coding
agents lower the cost of creation dramatically and leave the cost of ownership untouched, so organisations can accumulate
applications faster than they can look after them. This skill reviews an AI-built application, or an estate of them, for
the things that decide whether it can be maintained by people: an owner, code the team understands without the agent,
documentation, meaningful tests, current dependencies, more than one person who knows it, and a way to retire it. It goes
wrong when maintainability is judged by whether the agent can still change the code, rather than whether people can.

## When to use

- An AI-built application reaches its scheduled review date.
- The application's owner or only knowledgeable engineer is leaving or changing role.
- An estate of AI-built tools and scripts has grown and needs triage.
- Changes to an application are becoming slow, risky or dependent on one person.

## When not to use

- Reviewing individual code changes - use `copilot-code:generated-code-review`.
- Checking readiness for a first deployment - use `copilot-code:code-deployment-readiness`.
- Formal supportability and ownership review at the design authority gate - use `design-authority:supportability-review`.
- Running the scheduled review calendar for all live AI solutions - use `ai-operations:ai-review-calendar`.
- Retiring an AI solution once the decision is made - use `ai-operations:ai-solution-retirement`.

## Questions to ask first

1. Who owns this application as a business service and as software, and are they still in role and willing?
2. Could someone on the team explain how it works and make a small change without asking the coding agent to explain it first?
3. Do the tests catch real regressions, and do they still run in the pipeline?
4. Are dependencies current and free of known vulnerabilities, and who updates them?
5. Is the application still used and still needed, and does anything else now do the same job?

## Required inputs

- The solution brief, architecture note and repository.
- The application's entry in the solution inventory, with owners and review history.
- Pipeline, dependency scanning and incident history.
- Usage at an aggregate level and the business owner's view of value.

Where owners cannot be found, that is the first finding, and the application is treated as at risk. Never use review data
to assess the performance of the people who built or maintained it.

## Decision framework

Rate each factor and use the overall picture to recommend an action.

| Factor | Healthy | At risk | Critical |
|---|---|---|---|
| Ownership | Business and engineering owners named and active | One owner missing or inactive | No owner |
| Comprehension | Two or more people can explain and change it unaided | One person can | Only the agent "understands" it |
| Documentation | Brief, architecture note and runbook current | Partial or outdated | None |
| Tests | Meaningful tests running in the pipeline | Thin or partly broken | None, or not run |
| Dependencies | Current, scanned, updated on a cycle | Behind, with no known exploitable issues | Known exploitable vulnerabilities or abandoned packages |
| Need and use | Used and valued; no duplicate | Low use or partly duplicated | Unused or fully duplicated |

| Recommendation | When |
|---|---|
| Keep | Mostly healthy; minor actions with owners and dates |
| Invest | Valued and used, but at risk on comprehension, tests or dependencies; fund the fixes |
| Consolidate | Duplicates another application or could move to a governed platform |
| Retire | Unused, unowned or critical on several factors with no case to invest |

## Practitioner approach

Start with ownership, because every other factor depends on it. Confirm the business owner still needs the application
and the engineering owner still maintains it. An application with no owner is at risk however clean its code; one with an
engaged owner can recover from most other problems.

Test comprehension directly. Ask a team member who did not build the application to explain its main flow and make a small
change, without first asking the coding agent to explain it. If they cannot, the application depends on the agent for
understanding, which is fragile: agents change, context is lost, and an explanation generated on demand is not the same as
a team that knows its own system. Record how many people could do this unaided.

Check that documentation matches reality. A brief, an architecture note and a runbook are enough for most applications, if
they are current. Look for decisions that were made in agent conversations and never written down; these are often the
missing context that makes later changes risky.

Check whether the tests protect anything. Run them, read a sample, and break something deliberately to see if they fail.
Generated test suites can be large and still miss the behaviour that matters. A thin but meaningful suite is better than a
large decorative one.

Review dependencies. Look at how far behind they are, whether any have known vulnerabilities or have been abandoned, and
whether anyone updates them on a cycle. AI-built applications often have more dependencies than necessary because the
agent added libraries freely.

Ask whether it is still needed. Usage at an aggregate level, the business owner's view and the solution inventory will
show whether the application is valued, duplicated by something newer, or a candidate to move to a governed low-code
platform where the organisation already has support.

Bring the factors together into a recommendation and agree it with the owners. For estates, rate every application on the
same factors, then focus investment on valued applications at risk, consolidate duplicates and retire the rest. Retirement
is a healthy outcome, not a failure.

## Outputs

- A maintainability review record: each factor rated with evidence, and a keep, invest, consolidate or retire recommendation with actions, owners and dates.
- For estates, a triage table across applications with the same factors.
- Updates to the solution inventory with owners, ratings and next review date.

## Microsoft platform considerations

Repository insights, dependency scanning and pipeline history on the development platform help with evidence; Power Platform
and Azure inventories help find duplicates and candidates to consolidate. Confirm current tooling capabilities in the
relevant source records and with the platform team.

## Adoption considerations

Users of a tool being retired or consolidated need notice, an alternative and help to move. Coordinate with the business
owner so retirement does not feel like losing something valued without explanation.

## Knowledge considerations

Comprehension is a knowledge problem. Where only one person or the agent understands an application, plan knowledge
transfer: paired changes, an updated architecture note and recorded design decisions.

## Security and privacy considerations

Out-of-date dependencies and unowned applications are security risks. Critical dependency findings go to
`copilot-code:generated-code-security-review` for remediation, and unowned applications holding personal data are escalated
to the `security-privacy` reviewer.

## Responsible AI considerations

Not applicable as a primary concern, because the review addresses whether software can be maintained; where an application
supports decisions about people and is at risk, raise its review priority with the `responsible-ai` department.

## Evaluation requirements

Use a deliberate break test to confirm the test suite catches regressions, and record the result in the review.

## Value measures

Track at estate level the share of AI-built applications with active owners, rated healthy, and reviewed on schedule, and the
number retired or consolidated. Never use these measures to judge individual builders.

## Scale notes

### Starter

Review each AI-built application once a year against the six factors, with the owners, on one page.

### Scale

Schedule reviews through the solution inventory, triage the estate annually, and fund an "invest" backlog for valued
applications at risk.

### Enterprise

Integrate maintainability ratings into portfolio management, set organisation-wide thresholds that trigger invest or retire
decisions, and report estate health to the CoE.

## Hand-offs

- To `ai-operations:ai-solution-retirement` for applications recommended for retirement.
- To `design-authority:supportability-review` for applications at risk tier 2 and above with critical ratings.
- To `copilot-code:code-solution-brief` when an application is to be rebuilt.

## Reviewer gates

From risk tier 2, `design-authority` reviews critical ratings and retirement or consolidation recommendations through
`design-authority:supportability-review`. Findings are blocking or advisory; an unowned application at tier 2 or above
holding personal data is blocking until an owner is named or it is retired.

## Failure modes

- Maintainability is judged by whether the agent can still change the code, not whether people can.
- A large generated test suite gives false confidence because it would not catch real regressions.
- Applications accumulate with no review, and the estate becomes unmanageable before anyone notices.
- Retirement is avoided because it feels like failure, so unused tools keep consuming effort and carrying risk.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Treat the coding agent as the maintainer of an application.
- Leave an application without a named owner after a review.
- Use maintainability reviews to assess the performance of individual engineers.
- Retire an application without telling its users and offering an alternative.

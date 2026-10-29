# Code solution brief

Template id: `code-solution-brief`

Responsible skill: `copilot-code:code-solution-brief`. The assessment section is completed with
`copilot-code:code-use-case-assessment`, and the acceptance criteria are broken into work items with
`copilot-code:requirements-to-build`.

Use this brief before an AI-assisted build starts, and keep it in the repository alongside the code. Every fact the
organisation must supply is marked `[To confirm: ...]`; replace the marker when the fact is confirmed, and never fill it
with a guess. Example rows are fictional and are there to be replaced or deleted. Never include real personal data or
secrets in this brief.

## 1. Summary

| Field | Entry |
|---|---|
| Working name | [To confirm] |
| Opportunity or intake reference | [To confirm] |
| Business owner (accountable for outcomes) | [To confirm: name and role; owner has agreed this brief] |
| Engineering owner (accountable for the software) | [To confirm: name or team; owner has agreed] |
| Risk tier (0-4) | [To confirm: tier from risk classification, with date] |
| Route | Prototype with end date / Production build |
| Brief version and status | [To confirm: version] Draft / Agreed / Superseded |

## 2. Assessment

| Question | Answer |
|---|---|
| Current workaround and its cost | [To confirm] |
| Alternatives considered (no build, existing product, configuration, Power Platform, agent, Cowork task) and why rejected | [To confirm] |
| Ownership test: business owner, engineering owner, organisation-controlled repository, review capacity, support route | [To confirm: each confirmed yes or no] |
| Verdict | [To confirm: production build / prototype only, with reasons] |

## 3. Outcome

One sentence naming the users, the job and the measure.

> Fictional example: "Site managers record safety inspections on a tablet and the weekly compliance report is produced
> automatically, so the report is on time and nobody re-keys data."

[To confirm: outcome statement]

## 4. Users and roles

| Role | Approximate number | What they can do | What they must not be able to do |
|---|---|---|---|
| Fictional example: site manager | Fictional example: forty | Create and edit inspections for their own site | See other sites' inspections |
| [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 5. Scope and exclusions

In scope:

| # | Capability | Priority |
|---|---|---|
| 1 | [To confirm] | Must / Should / Could |

Out of scope, with reasons:

| Excluded capability | Reason |
|---|---|
| Fictional example: dashboards and analytics | Fictional example: covered by the existing reporting service |
| [To confirm] | [To confirm] |

## 6. Data and systems

| Data set or system | Read / write / send | Identity used (user, managed identity, service account) | Sensitivity or label | Personal data? |
|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | Yes / No |

External endpoints the software calls: [To confirm]

## 7. Constraints and non-functional requirements

| Area | Requirement |
|---|---|
| Hosting and environments | [To confirm: approved hosting, test and production environments] |
| Approved languages, frameworks and libraries | [To confirm] |
| Identity and secrets | [To confirm: managed identity, secrets store] |
| Accessibility | [To confirm] |
| Performance and availability | [To confirm] |
| Logging and telemetry (what must and must not be logged) | [To confirm] |
| Data retention | [To confirm] |
| AI features at run time, if any | [To confirm: none, or which, and how users are told] |

## 8. Acceptance criteria

Testable statements the business owner agrees, including what must not be possible.

| # | Criterion | Type (functional / negative / non-functional) |
|---|---|---|
| 1 | Fictional example: an inspection saved offline uploads when the device reconnects, with no duplicate record | Functional |
| 2 | Fictional example: a site manager cannot open another site's inspection | Negative |
| 3 | [To confirm] | [To confirm] |

## 9. Repository and engineering

| Item | Entry |
|---|---|
| Repository location (organisation-controlled) | [To confirm] |
| Repository context and custom instructions in place | [To confirm: yes or no, with link] |
| Protected areas needing code owner review | [To confirm] |
| Pipeline checks (build, tests, linting, scanning) | [To confirm] |

## 10. Prototype boundaries (prototype route only)

| Boundary | Entry |
|---|---|
| Question the prototype answers | [To confirm] |
| End date and decision maker | [To confirm] |
| Sandbox | [To confirm] |
| Data (synthetic or approved test data only) | [To confirm] |

## 11. Ownership, support and review

| Role | Name or team | Agreed? |
|---|---|---|
| Business owner | [To confirm] | Yes / No |
| Engineering owner | [To confirm] | Yes / No |
| Support route for users | [To confirm] | Yes / No |
| First maintainability review date | [To confirm] | Not applicable |

## 12. Success measures

Measured at team or role level, never for individual staff.

| Measure | Baseline and source | Target | Owner | Review date |
|---|---|---|---|---|
| Fictional example: weekly compliance report delivered on time | Fictional example: last quarter's delivery log | [To confirm] | [To confirm] | [To confirm] |
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 13. Open questions and preconditions

| Item | Owner | Due |
|---|---|---|
| [To confirm] | [To confirm] | [To confirm] |

## 14. Agreement

| Role | Name | Date |
|---|---|---|
| Business owner | [To confirm] | [To confirm] |
| Engineering owner | [To confirm] | [To confirm] |
| Design authority (from risk tier 2) | [To confirm] | [To confirm] |
| Security and privacy reviewer (from risk tier 2) | [To confirm] | [To confirm] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

# Support and monitoring plan

Template id: `support-and-monitoring-plan`

Responsible skill: `ai-operations:ai-support-model`. The monitoring section is completed with
`ai-operations:ai-solution-monitoring`, the feedback section with `ai-operations:ai-feedback-loop`, the continuity
section with `ai-operations:ai-continuity` and the review section with `ai-operations:ai-review-calendar`.

Complete this plan before a solution goes live and keep it with the solution record. Every fact the organisation must
supply is marked `[To confirm: ...]`. Example rows are fictional. Record roles, not individual names, wherever a role
exists; usage and support data in this plan are reported at team or role level only.

## 1. Solution and ownership

| Field | Entry |
|---|---|
| Solution name and inventory reference | [To confirm] |
| Route and environment | [To confirm] |
| Risk tier | [To confirm] |
| Business owner (role) | [To confirm] |
| Solution owner (role) | [To confirm] |
| Knowledge owners (role per source) | [To confirm] |
| Technical owner and backup (roles; at least two people able to change the solution from tier 2) | [To confirm] |
| Runbook location | [To confirm] |

## 2. Support levels and routes

| Level | Who | Handles | Contact route |
|---|---|---|---|
| 0 Self-help | Users | How-to, known limits, expected refusals | [To confirm: location of guidance] |
| 1 First line | [To confirm: service desk, Champions where agreed] | Access, availability, logging and categorising | [To confirm] |
| 2 Solution | [To confirm: solution owner, knowledge owners, maker] | Wrong answers, outdated knowledge, scope and behaviour | [To confirm] |
| 3 Platform and engineering | [To confirm: platform team, engineers, agreed Microsoft support route] | Connectors, environment, service faults | [To confirm] |

User-facing support message placed in the solution: [To confirm: wording]

## 3. Triage categories and response expectations

| Category | Routed to | Response expectation by tier |
|---|---|---|
| Wrong or unsupported answer | [To confirm] | [To confirm] |
| Out-of-date answer | [To confirm] | [To confirm] |
| Should have refused or redirected | [To confirm] | [To confirm] |
| Action failed or acted wrongly | [To confirm] | [To confirm] |
| Cannot access solution or knowledge | [To confirm] | [To confirm] |
| Harmful, offensive or exposing output | Incident route, immediately | Immediate |

## 4. Monitoring

| Signal | Threshold | Receiving role | First action | Escalation |
|---|---|---|---|---|
| Availability and errors | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Failed actions | [To confirm, or not applicable] | [To confirm] | [To confirm] | [To confirm] |
| Usage by team (minimum group size [To confirm]) | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Sampled answer quality against release rubric | [To confirm] | [To confirm] | [To confirm] | Regression evaluation |
| Safety triggers and harmful output reports | Any | [To confirm] | Incident route | [To confirm] |
| Negative feedback trend | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Knowledge sources past review date or moved | [To confirm] | [To confirm] | Knowledge refresh | [To confirm] |
| Consumption against plan | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

Fictional example row: "Sampled answer quality; correctness below 85% in two consecutive samples; solution owner;
re-run regression subset; business owner."

## 5. Feedback

| Item | Entry |
|---|---|
| Feedback routes (in product, form, service desk, Champions) | [To confirm] |
| Review rhythm and triage role | [To confirm] |
| How users hear what changed | [To confirm] |
| Feedback content access and retention | [To confirm: agreed with security and privacy] |

## 6. Incidents and continuity

| Item | Entry |
|---|---|
| How to restrict, disable an action or switch the solution off | [To confirm: steps and who may do it] |
| Who may suspend the solution when harm is continuing | [To confirm: role] |
| Impact of a day without the solution | Inconvenience / Material delay / Critical process stops |
| Fallback route for the work | [To confirm] |
| Communications templates for suspension and return | [To confirm: location] |
| External dependencies, notice route and alternative | [To confirm] |
| Last continuity exercise (tier 3 and 4) | [To confirm] |

## 7. Reviews

| Item | Entry |
|---|---|
| Review frequency for this tier | [To confirm] |
| Next review date | [To confirm] |
| Review forum | [To confirm] |
| Rule for overdue reviews | [To confirm] |

## 8. Handover from build to run

| Item | Entry |
|---|---|
| Handover session date and attendees (roles) | [To confirm] |
| Joint support period | [To confirm] |
| Date support formally passed to the solution owner | [To confirm] |

## 9. Sign-off

| Role | Decision | Date |
|---|---|---|
| Business owner | Accepted / Changes required | [To confirm] |
| Solution owner | Accepted / Changes required | [To confirm] |
| Service desk or operations lead | Accepted / Changes required | [To confirm] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

# AI impact assessment record

Template id: `ai-impact-assessment-record`

Responsible skill: `responsible-ai:ai-impact-assessment`. Sections 5 to 8 are completed with
`responsible-ai:human-oversight`, `responsible-ai:ai-transparency`, `responsible-ai:fairness-review` and
`responsible-ai:escalation-and-appeal`; section 2 records the screen from `responsible-ai:prohibited-use-review`; and
section 10 is used only through `responsible-ai:ai-risk-acceptance`.

Every fact the organisation must supply is marked `[To confirm: ...]`. Example rows are fictional. Each residual
concern is classified **blocking** or **advisory** and names the impact, the fix and an owner. The responsible AI gate
is mandatory and blocking from risk tier 3, and from tier 2 when outputs inform decisions about people. A blocking
concern is not traded against a date. Legal and data protection questions end with the legal adviser and the DPO.

## 1. Solution and context

| Field | Entry |
|---|---|
| Solution name | [To confirm: name] |
| Purpose in one sentence | [To confirm: what the solution is for] |
| Business owner (role) | [To confirm: accountable role] |
| Platform route | [To confirm: for example Copilot, agent, Copilot Studio, Foundry, automation] |
| Risk tier and rationale | [To confirm: tier 0-4 from risk classification] |
| Stage of assessment | Design / Pre-release / Change / Periodic review |
| Related records | [To confirm: AI risk assessment, privacy assessment or DPIA references] |
| Assessors and date | [To confirm: reviewer roles and date] |

## 2. Prohibited use screen

| Question | Entry |
|---|---|
| Indicators checked | [To confirm: monitoring, scoring, emotion inference, manipulation, unreviewed decisions, sensitive inference] |
| Provider terms confirmed by | [To confirm: role and date] |
| Legal advice reference, if needed | [To confirm] |
| Verdict | Stop / Restrict with conditions / Proceed |
| Conditions | [To confirm] |

## 3. Affected people

| Group | Relationship (user, subject of outputs, worker whose role changes, other) | What they need from the solution | What they could lose or fear | Consulted? How? |
|---|---|---|---|---|
| Fictional example: customers whose claims are triaged | Subject of outputs | Fair, timely triage | Wrongly delayed claim | Customer panel, [To confirm: date] |
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 4. Uses and impacts

| ID | Use (intended or foreseeable misuse) | Group affected | Potential impact | Severity (minor, moderate, serious, severe) | Likelihood (rare, possible, likely) | Reversible? |
|---|---|---|---|---|---|---|
| Fictional example I1 | Foreseeable: advisers copy triage priority into final decisions | Customers | Claim declined without full review | Serious | Possible | Partly |
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 5. Human oversight

Summary of the `human-oversight-plan`: [To confirm: oversight mode per output or action, reviewer role, capacity check
result, authority to overturn]

## 6. Transparency

| Audience | What they are told | When and where | Wording owner |
|---|---|---|---|
| [To confirm: users] | [To confirm] | [To confirm] | [To confirm] |
| [To confirm: affected people who are not users] | [To confirm] | [To confirm] | [To confirm] |

## 7. Fairness

| Group or difference tested | Type of risk (quality of service, allocation, representation) | Test cases and coverage | Result | Finding |
|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 8. Escalation and appeal

| Route | Entry |
|---|---|
| How people reach a person during an interaction | [To confirm] |
| How people question an outcome afterwards | [To confirm] |
| Reviewing role and authority to overturn | [To confirm] |
| Timescales, as set by the process owner | [To confirm] |
| How appeal themes reach the solution owner | [To confirm] |

## 9. Mitigations and residual concerns

| ID | Impact ID | Mitigation | Tested? Evidence | Residual concern | Blocking or advisory | Fix | Owner | Due | Status |
|---|---|---|---|---|---|---|---|---|---|
| Fictional example R1 | I1 | Priority shown as advisory; adviser must record reason | Pending | Advisers may still rely on priority under time pressure | Blocking | Capacity check and seeded-error test with advisers | Fictional example: claims operations manager | [To confirm] | Open |
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | Blocking / Advisory | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 10. Verdict and review

| Field | Entry |
|---|---|
| Verdict | Pass / Pass with advisory concerns / Blocked |
| Risk acceptance reference (only where a concern is disputed) | [To confirm] |
| Review trigger (scope, audience, data, autonomy change) | [To confirm] |
| Next scheduled review | [To confirm: date] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

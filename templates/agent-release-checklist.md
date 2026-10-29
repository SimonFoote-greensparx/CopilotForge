# Agent release checklist

Template id: `agent-release-checklist`

Responsible skill: `m365-agents:agent-release-readiness`. The test evidence section is completed with
`m365-agents:agent-testing`.

Complete this checklist before an agent is shared with its audience, and again before its audience widens. Every fact
the organisation must supply is marked `[To confirm: ...]`. Example rows are fictional. An open blocking finding from
any reviewer means the release decision is "Not ready", whatever the date.

## 1. Agent and decision

| Field | Entry |
|---|---|
| Agent name | [To confirm] |
| Agent brief reference | [To confirm] |
| Risk tier (re-confirmed at release) | [To confirm: tier and date; re-run risk classification if behaviour, audience or actions changed] |
| Business owner | [To confirm: name and role] |
| Release type | First release / Audience widening / Material change / Periodic review |
| Release decision | Ready / Ready with conditions / Not ready |

## 2. Test evidence

Completed with `m365-agents:agent-testing`. The threshold must be agreed before results are seen.

| Item | Entry |
|---|---|
| Evaluation set size and location | [To confirm] |
| Agreed thresholds (correct, grounded, appropriate, safe) and date agreed | [To confirm] |
| Zero-tolerance failures defined | [To confirm: for example exposing restricted content, acting without confirmation] |
| Results per dimension | [To confirm] |
| Zero-tolerance breaches | [To confirm: none, or list with fix] |
| Permission-trimming tests (user profiles used) | [To confirm: for example in-audience user, narrower-access user, out-of-audience user] |
| Action tests (confirmation, identity, safe failure) | [To confirm, or not applicable] |
| Regression subset and re-run triggers | [To confirm] |
| Business owner decision on test evidence | Meets threshold / Does not meet threshold, with date |

Fictional example result: "Correct 92%, grounded 95%, appropriate 100%, safe 100%; one knowledge-caused failure fixed
and re-tested."

## 3. Release checks by tier

Tick only when evidence is attached. "N/A" requires a reason.

| Check | Required from tier | Evidence or reference | Status |
|---|---|---|---|
| Named business owner and knowledge owners agreed | 1 | [To confirm] | Done / Open |
| Support route and fix owner | 1 | [To confirm] | Done / Open |
| Sharing scope matches brief and tier (groups listed) | 1 | [To confirm: groups] | Done / Open |
| Security and privacy review passed, no open blocking findings | 2 | [To confirm: review reference] | Done / Open / N/A |
| Evaluation quality review | 2 (when the evaluation-quality department is active; until then, CoE lead check) | [To confirm] | Done / Open / N/A |
| Responsible AI review | 3 | [To confirm] | Done / Open / N/A |
| Design authority review | 3 | [To confirm] | Done / Open / N/A |
| Executive risk acceptance for any accepted risks, in writing | 2 | [To confirm] | Done / Open / N/A |
| Communications to audience, including known limits | 1 | [To confirm] | Done / Open |
| Monitoring in place (usage, feedback, failures) | 2 | [To confirm] | Done / Open / N/A |
| Review date set and linked to knowledge review cycles | 1 | [To confirm: date] | Done / Open |
| Retirement criteria recorded | 1 | [To confirm] | Done / Open |
| Solution register entry created or updated | 1 | [To confirm: register reference] | Done / Open |

## 4. Reviewer findings

| Reviewer | Finding | Blocking or advisory | Fix | Owner | Status and evidence |
|---|---|---|---|---|---|
| [To confirm] | [To confirm] | Blocking / Advisory | [To confirm] | [To confirm] | [To confirm] |

## 5. Communications and support

| Item | Entry |
|---|---|
| What the agent does and does not do | [To confirm] |
| Where answers come from | [To confirm] |
| How users report a problem | [To confirm] |
| Reminder that users check outputs and stay accountable | [To confirm: wording] |
| Channels (managers, Champions, intranet) | [To confirm] |

## 6. Monitoring, review and retirement

| Item | Entry |
|---|---|
| Measures tracked, at audience-group level | [To confirm] |
| Minimum group size for reporting | [To confirm] |
| Next review date | [To confirm] |
| Retirement criteria | Fictional example: no use for 90 days; owner leaves without successor; knowledge no longer maintained |
| Operations hand-over | [To confirm: team and date] |

## 7. Sign-off

| Role | Name | Decision | Date |
|---|---|---|---|
| Business owner | [To confirm] | [To confirm] | [To confirm] |
| CoE or release lead | [To confirm] | [To confirm] | [To confirm] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

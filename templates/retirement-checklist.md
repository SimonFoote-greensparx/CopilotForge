# Retirement checklist

Template id: `retirement-checklist`

Responsible skill: `ai-operations:ai-solution-retirement`.

Use this checklist once the decision to retire an agent or AI solution has been made. Complete the stages in order;
each stage has an exit check. Every fact the organisation must supply is marked `[To confirm: ...]`. Example rows are
fictional. From risk tier 2 a second person checks stages 5 and 6; from tier 3 the `security-privacy` reviewer confirms
them.

## 1. Confirm

| Item | Entry |
|---|---|
| Solution name and inventory reference | [To confirm] |
| Risk tier | [To confirm] |
| Retirement decision, decision owner (role) and date | [To confirm: link to review or scale-or-stop record] |
| Reason for retirement | [To confirm] |
| Alternative for users | [To confirm: replacement solution, standard Copilot capability or process] |
| Retirement date | [To confirm] |
| Dependants (flows, agents or processes that rely on it) | [To confirm, or none found, with how checked] |

Exit check: decision owner has signed and no unknown dependants remain. [ ] Done

## 2. Notify

| Audience | Message sent by | Date | Channel |
|---|---|---|---|
| Users (teams or roles) | [To confirm] | [To confirm] | [To confirm] |
| Managers | [To confirm] | [To confirm] | [To confirm] |
| Service desk | [To confirm] | [To confirm] | [To confirm] |
| Champions, where relevant | [To confirm] | [To confirm] | [To confirm] |
| Knowledge owners | [To confirm] | [To confirm] | [To confirm] |

Fictional example message: "The travel policy agent will be retired on the last working day of the month. The new
expenses agent now answers travel questions, and the policy page remains available on the intranet."

Exit check: notice given with the agreed lead time. [ ] Done

## 3. Freeze

| Item | Entry |
|---|---|
| Change freeze from | [To confirm] |
| Message inside the solution pointing to the alternative | [To confirm: wording] |

Exit check: message visible to users. [ ] Done

## 4. Withdraw

| Action | Evidence | Done |
|---|---|---|
| Sharing removed | [To confirm] | [ ] |
| Solution unpublished or disabled | [To confirm] | [ ] |
| Removed from catalogues, app listings and support catalogue | [To confirm] | [ ] |

Exit check: users can no longer reach the solution. [ ] Done

## 5. Revoke

| Item | Identifier or description | Action taken | Checked by (role) | Done |
|---|---|---|---|---|
| Connections and connectors | [To confirm] | Disabled / Deleted | [To confirm] | [ ] |
| Service identities and app registrations | [To confirm] | Disabled / Deleted | [To confirm] | [ ] |
| Secrets, keys and certificates | [To confirm] | Revoked / Deleted | [To confirm] | [ ] |
| Dependent flows and automations | [To confirm] | Stopped / Deleted / Transferred | [To confirm] | [ ] |
| Monitoring alerts | [To confirm] | Closed | [To confirm] | [ ] |

Exit check: no standing access remains. [ ] Done

## 6. Data

| Data type | Retention rule (confirmed with) | Action | Location if retained | Done |
|---|---|---|---|---|
| Conversation transcripts | [To confirm: rule; DPO or records manager] | Keep / Archive / Delete | [To confirm] | [ ] |
| Logs and telemetry | [To confirm] | Keep / Archive / Delete | [To confirm] | [ ] |
| Feedback | [To confirm] | Keep / Archive / Delete | [To confirm] | [ ] |
| Evaluation datasets, rubrics and results | [To confirm] | Transfer / Archive / Delete | [To confirm] | [ ] |
| Records needed for challenges or appeals about people | [To confirm, or not applicable] | Keep | [To confirm] | [ ] |

Exit check: disposal or retention recorded for every data type. [ ] Done

## 7. Close

| Item | Entry |
|---|---|
| Knowledge indexes or copies made only for this solution removed | [To confirm] |
| Inventory record updated to retired, with date | [To confirm] |
| Removed from review calendar | [To confirm] |
| Value close-out - what the solution achieved | [To confirm] |
| Lessons for the CoE | [To confirm] |

Exit check: record shows retired with date. [ ] Done

## 8. Sign-off

| Role | Stage(s) confirmed | Date |
|---|---|---|
| Solution owner | 1 to 7 | [To confirm] |
| Second checker (tier 2 and above) | 5 and 6 | [To confirm] |
| `security-privacy` reviewer (tier 3 and above) | 5 and 6 | [To confirm] |
| Business owner | Retirement complete | [To confirm] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

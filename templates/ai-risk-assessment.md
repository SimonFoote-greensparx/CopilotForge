# AI risk assessment

Template id: `ai-risk-assessment`

Responsible skills: `security-privacy:data-exposure-review`, `security-privacy:connector-review` and
`security-privacy:privacy-assessment`. Section 1 records the risk tier set during opportunity risk classification.

Every fact the organisation must supply is marked `[To confirm: ...]`. Example rows are fictional. Each finding is
classified **blocking** or **advisory**, names the risk, and gives the fix and owner. From risk tier 2 a blocking
finding stops release and is not traded against dates. Disagreement escalates to the accountable executive, whose risk
acceptance is recorded in section 7. Legal questions end with the Data Protection Officer.

## 1. Solution and risk tier

| Field | Entry |
|---|---|
| Solution name | [To confirm] |
| Brief or design reference | [To confirm] |
| Business owner | [To confirm] |
| Audience and sharing scope | [To confirm] |
| Risk tier (0-4) and rationale | [To confirm] |
| Reviewers and date | [To confirm] |

## 2. Data exposure

Completed with `security-privacy:data-exposure-review`. Grounding is permission-trimmed, so overshared content becomes
discoverable; judge whether the permissions are right, not only whether they are respected.

| Source or output path | Who can access today | Intended audience | Sensitivity or label | Web or public? | Gap |
|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | Yes / No | [To confirm] |

Permission-trimming test evidence: [To confirm: reference and user profiles used]

## 3. Connectors and actions

Completed with `security-privacy:connector-review`.

| Connector, action, tool, MCP server or API | Operations used | Identity (user, maker, service) | Permissions granted | Data policy and zone | Data leaves tenant? | Confirmation for writes |
|---|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | Yes / No | Yes / No / N/A |

## 4. Privacy

Completed with `security-privacy:privacy-assessment`.

| Question | Entry |
|---|---|
| Whose personal data, which categories (special category?) | [To confirm] |
| Personal data map: grounding, input, output, storage, onward flows | [To confirm] |
| Purpose and compatibility with original collection | [To confirm] |
| Lawful basis, as confirmed by the DPO, with date | [To confirm] |
| Transparency (notices and in-product statement) | [To confirm] |
| Minimisation measures | [To confirm] |
| Retention for prompts, responses, transcripts and logs, with owner | [To confirm] |
| Rights handling covers AI data | [To confirm] |
| DPIA screening result and DPIA reference if required | [To confirm] |
| Outputs inform decisions about individuals? Human review design | [To confirm] |

## 5. Findings

| ID | Area | Finding and risk | Rule or standard | Blocking or advisory | Fix | Owner | Due | Status and evidence |
|---|---|---|---|---|---|---|---|---|
| Fictional example F1 | Data exposure | Salary files shared with all staff are reachable through the agent | Content shared beyond intended audience | Blocking | Remove broad grant at source; re-run permission tests | Fictional example: HR site owner | [To confirm] | Open |
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | Blocking / Advisory | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 6. Verdict

| Area | Verdict |
|---|---|
| Data exposure | Pass / Pass with advisory findings / Blocked |
| Connectors and actions | Pass / Pass with advisory findings / Blocked / N/A |
| Privacy | Pass / Pass with advisory findings / Blocked / N/A |
| Overall | Pass / Pass with advisory findings / Blocked |

## 7. Risk acceptance (only where a finding is disputed)

| Finding ID | Risk accepted | Rationale | Accountable executive | Date | Review date |
|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

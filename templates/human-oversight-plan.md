# Human oversight plan

Template id: `human-oversight-plan`

Responsible skill: `responsible-ai:human-oversight`. The plan responds to impacts recorded in the
`ai-impact-assessment-record`; checkpoints are built with `copilot-cowork:human-checkpoint-design` or
`automation:human-in-the-loop`.

Every fact the organisation must supply is marked `[To confirm: ...]`. Example rows are fictional. Oversight measures
are reported at role level and are never used to assess or rank individual reviewers. Gaps are classified
**blocking** or **advisory** with a fix and an owner.

## 1. Solution

| Field | Entry |
|---|---|
| Solution name | [To confirm] |
| Business owner (role) | [To confirm] |
| Risk tier | [To confirm] |
| Impact assessment reference | [To confirm] |
| Plan version and date | [To confirm] |

## 2. Oversight by output or action

| Output or action | Harm if wrong | Last point a person can prevent it | Oversight mode (review every output, approve before action, sampled review, monitoring) | Reviewing role |
|---|---|---|---|---|
| Fictional example: draft refusal letter to a customer | Customer wrongly refused | Before sending | Review every output | Fictional example: senior case handler |
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 3. Capacity check

| Reviewing role | Expected items per day | Careful review time per item | Time available per day | Fits? | If not, design change |
|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | Yes / No | [To confirm] |

## 4. What the reviewer sees

| Element | Provided? | How |
|---|---|---|
| The output or proposed action | Yes / No | [To confirm] |
| Sources the output relied on | Yes / No | [To confirm] |
| Case or record context | Yes / No | [To confirm] |
| Signals of uncertainty or unusual cases | Yes / No | [To confirm] |
| Reject and edit as easy as approve; no pre-selected approval | Yes / No | [To confirm] |

## 5. Authority and competence

| Question | Entry |
|---|---|
| Where the authority to reject or overturn is written down | [To confirm: procedure or role description] |
| Competence the reviewer needs | [To confirm] |
| Training and calibration provided | [To confirm] |
| How automation bias is countered (for example calibration sessions) | [To confirm] |

## 6. Feedback loop

| Question | Entry |
|---|---|
| How rejections and edits are recorded (aggregate) | [To confirm] |
| Who reviews them and how often | [To confirm] |
| How findings change the solution | [To confirm] |
| Investigation threshold for a very low override rate | [To confirm] |

## 7. Pre-release test

| Test | Entry |
|---|---|
| Outputs with known errors presented to reviewers | [To confirm: number and type] |
| Realistic conditions (volume, time) | [To confirm] |
| Result at role level | [To confirm] |
| Changes made | [To confirm] |

## 8. Gaps

| ID | Gap | Blocking or advisory | Fix | Owner | Due | Status |
|---|---|---|---|---|---|---|
| [To confirm] | [To confirm] | Blocking / Advisory | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 9. Review triggers

[To confirm: changes in volume, scope, autonomy, model or reviewer role that trigger a review of this plan, and the
next scheduled review date]

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

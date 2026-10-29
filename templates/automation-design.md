# Automation design

Template id: `automation-design`

Responsible skill: `automation:automation-process-design`. The review section is completed with
`automation:human-in-the-loop`, the exceptions section with `automation:exception-handling`, the connectors section with
`automation:automation-connector-governance` and the monitoring section with `automation:automation-monitoring`.

Complete this design before build starts on any automation with AI steps or at risk tier 2 and above, and update it
whenever the process, policy or systems change. Every fact the organisation must supply is marked `[To confirm: ...]`.
Example rows are fictional. A design is ready for build only when every branch has a written rule, every AI step has a
fallback and every exception has an owner.

## 1. Automation and ownership

| Field | Entry |
|---|---|
| Automation name | [To confirm] |
| Process it supports | [To confirm] |
| Automation assessment reference | [To confirm] |
| Process owner (business) | [To confirm: name and role] |
| Technical owner | [To confirm: team and role] |
| Exception owner(s) | [To confirm: role and team for each exception type] |
| Risk tier | [To confirm: tier and date set] |
| Target environment | [To confirm: environment and governance zone] |

## 2. Process changes made before automation

| Step removed, consolidated or changed | Reason | Agreed by | Date |
|---|---|---|---|
| Fictional example: manual re-keying of order into second system | Duplicate of system integration | Process owner | [To confirm] |
| [To confirm] | [To confirm] | [To confirm] | [To confirm] |

Input changes requested at source (forms, templates, supplier files):

| Input | Change | Owner | Status |
|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | Requested / Agreed / Done |

## 3. Future-state steps

Step type is one of Human, Flow, AI step, Desktop flow, Approval.

| No. | Step | Type | Input | Output | Rule or task | Owner | Exception route |
|---|---|---|---|---|---|---|---|
| 1 | Fictional example: receive supplier invoice | Flow | Email with attachment | Stored file and item key | Trigger on shared mailbox, filter by sender domain | Technical owner | Not a supplier: route to accounts queue |
| 2 | Fictional example: extract invoice fields | AI step | Invoice file | Supplier, number, date, total, currency | See section 4 | Technical owner | Low confidence: review queue |
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 4. AI step definitions

Complete one block per AI step.

| Field | Entry |
|---|---|
| Step number and name | [To confirm] |
| Why AI is needed here (input unstructured or output is language) | [To confirm] |
| Task, stated precisely | [To confirm: for example extract these six fields; classify into these categories] |
| Model or AI capability, and where it is deployed | [To confirm: check source records before naming a capability] |
| Output shape (fields and allowed values) | [To confirm] |
| Validation rules applied before use | [To confirm] |
| Confidence or validity threshold, and who agreed it | [To confirm: threshold, owner and date agreed, before testing] |
| Fallback when validation fails or confidence is low | [To confirm] |
| Evaluation sample (size, source, location) | [To confirm] |
| Accuracy achieved in testing | [To confirm] |

## 5. Human review and approval

| Effect point | Review mode | Reviewer role | Information shown | Time limit | Escalation and delegate | Outcome on timeout |
|---|---|---|---|---|---|---|
| Fictional example: payment released | Approval before effect | Accounts approver | Invoice, extracted fields, confidence, purchase order match | 2 working days | Finance team lead; named delegate | Hold and escalate |
| [To confirm] | None / Sampled / On exception / Approval / Two-person | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

Reviewer capacity: expected items per day [To confirm] multiplied by review minutes per item [To confirm], against
declared capacity [To confirm].

Evidence required before any step moves to a lighter review mode: [To confirm].

## 6. Exceptions and failure handling

| Failure or exception class | Response | Retry rule | Owner | Response time |
|---|---|---|---|---|
| Transient technical | [To confirm] | [To confirm: attempts, delay, cap; idempotent steps only] | [To confirm] | [To confirm] |
| Permanent technical | [To confirm] | No retry | [To confirm] | [To confirm] |
| AI output invalid | [To confirm] | At most one controlled retry | [To confirm] | [To confirm] |
| AI low confidence or filtered | Route to review with reason | No retry | [To confirm] | [To confirm] |
| Business exception | [To confirm] | Not applicable | [To confirm] | [To confirm] |
| Partial run | [To confirm: resume from checkpoint or compensate] | [To confirm] | [To confirm] | [To confirm] |

Exception queue location: [To confirm].

## 7. Systems, connectors and connections

| Connector or system | Operations used | Data carried | Permitted in target environment | Production identity | Connection owner |
|---|---|---|---|---|---|
| [To confirm] | Read / Create / Update / Delete / Send | [To confirm] | Yes / Exception requested | [To confirm: service account or service principal, never personal] | [To confirm] |

Connector exceptions: [To confirm: reference, approver and review date, or none].

## 8. Monitoring and alerts

| Signal | Threshold | Alert to | Expected response |
|---|---|---|---|
| Run failure | [To confirm] | [To confirm] | [To confirm] |
| Missing runs (heartbeat) | [To confirm: expected minimum per period] | [To confirm] | [To confirm] |
| Exception queue age | [To confirm] | [To confirm] | [To confirm] |
| AI validation failure, low confidence and override rates | [To confirm: baseline from testing] | [To confirm] | Re-test against evaluation sample |
| Connection and credential expiry | [To confirm: warning period] | [To confirm] | [To confirm] |

## 9. Value baseline

| Measure | Baseline | Source and period | Target |
|---|---|---|---|
| Cycle time | [To confirm] | [To confirm] | [To confirm] |
| Handling effort per item | [To confirm] | [To confirm] | [To confirm] |
| Error or rework rate | [To confirm] | [To confirm] | [To confirm] |
| Expected review and exception effort after go-live | [To confirm] | Estimate | Not applicable |

## 10. Reviews and sign-off

| Reviewer | Required from tier | Finding summary | Blocking or advisory | Status |
|---|---|---|---|---|
| Design authority | 2 | [To confirm] | Blocking / Advisory | Open / Closed |
| Security and privacy | 2 | [To confirm] | Blocking / Advisory | Open / Closed |
| Responsible AI | 3 | [To confirm] | Blocking / Advisory | Open / Closed |

| Role | Name | Decision | Date |
|---|---|---|---|
| Process owner | [To confirm] | Approved / Not approved | [To confirm] |
| Technical owner | [To confirm] | Approved / Not approved | [To confirm] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

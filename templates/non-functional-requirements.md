# Non-functional requirements for an AI solution

Template id: `non-functional-requirements`

Responsible skill: `ai-architecture:ai-non-functional-requirements`.

One specification per solution, scaled to its risk tier. Each requirement has a measure, a target, a verification method
and an owner. Where the business owner has not agreed a figure, leave the target as `[To confirm: ...]` with the method
for setting it; never invent a target. Platform limits, quotas, prices and service levels are not recorded here from
memory: cite the source record and date. Example content is fictional.

## 1. Solution

| Field | Entry |
|---|---|
| Solution name and brief reference | [To confirm] |
| Platform decision reference | [To confirm: architecture decision record reference] |
| Risk tier | [To confirm: 0-4] |
| Business owner (role) | [To confirm] |
| Expected users (roles and approximate numbers) | [To confirm] |
| Usage pattern and expected growth | [To confirm: for example working hours, peaks, growth over twelve months] |
| Consequence if wrong, slow or unavailable | [To confirm: what happens to the business after an hour, a day, a week] |

## 2. Requirements

Depth follows the tier: a tier 1 solution may need only a line per category; tier 3 and 4 need every row evidenced.

| Category | Requirement | Measure | Target | Verification method | Owner |
|---|---|---|---|---|---|
| Answer quality | [To confirm] | [To confirm: for example share of answers rated correct and grounded on the evaluation set] | [To confirm] | [To confirm: evaluation before release and after change] | [To confirm: role] |
| Groundedness and citation | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Refusal and out-of-scope behaviour | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Latency | [To confirm] | [To confirm: by interaction type] | [To confirm] | [To confirm] | [To confirm] |
| Availability and support hours | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Capacity and growth | [To confirm] | [To confirm] | [To confirm] | [To confirm: load test or monitoring] | [To confirm] |
| Cost per use | [To confirm] | [To confirm: drivers such as conversations, actions, model calls, retrieval] | [To confirm: budget and alert threshold, per the licensing guide or partner] | [To confirm] | [To confirm: budget owner] |
| Resilience and fallback | [To confirm] | [To confirm] | [To confirm] | [To confirm: tested fallback] | [To confirm] |
| Knowledge freshness | [To confirm] | [To confirm: time from source change to answer change] | [To confirm] | [To confirm] | [To confirm: knowledge owner] |
| Observability | [To confirm] | [To confirm: errors, quality and safety signals] | [To confirm] | [To confirm] | [To confirm] |
| Security and access | [To confirm] | [To confirm] | [To confirm] | [To confirm: security review reference] | [To confirm] |
| Retention of prompts, responses and logs | [To confirm] | [To confirm] | [To confirm: period agreed with security and the DPO] | [To confirm] | [To confirm] |
| Human oversight and audit trail (where outputs affect people) | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Accessibility and language | [To confirm] | [To confirm] | [To confirm: organisation standard] | [To confirm] | [To confirm] |
| Supportability | [To confirm] | [To confirm: owners, support route, runbook] | [To confirm] | [To confirm: supportability review reference] | [To confirm] |

Fictional example, for illustration only: "Latency - typical knowledge questions answered quickly enough that agents on
a customer call do not need to put the caller on hold; measured as the time to first answer in the pilot; target agreed
by the contact centre manager after the pilot."

## 3. Requirements the platform cannot meet or verify

| Requirement | Why it cannot be met or verified | Proposed resolution | Raised with |
|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm: design authority or platform selection] |

## 4. Volatile facts relied on

| Fact | Source record | Date checked |
|---|---|---|
| [To confirm: limit, quota, service level or capability] | [To confirm: source id] | [To confirm] |

## 5. Agreement

| Role | Agreed | Date |
|---|---|---|
| Business owner | [To confirm] | [To confirm] |
| Operating team lead | [To confirm] | [To confirm] |
| Evaluation lead (quality requirements) | [To confirm] | [To confirm] |
| Design authority (tier 2 and above) | [To confirm] | [To confirm] |

Revisit at the first post-release review, when real usage can replace estimates: [To confirm: date]

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

# Data readiness assessment

Template id: `data-readiness-assessment`

Responsible skill: `data-governance:data-product-readiness`. Quality, classification, access and lineage results come
from `data-governance:ai-data-quality`, `data-governance:data-classification-for-ai`,
`data-governance:ai-data-access-model` and `data-governance:ai-data-lineage`.

Every fact the organisation must supply is marked `[To confirm: ...]`. Example rows are fictional. Readiness is
assessed for a stated AI use, not for all uses, and the verdict is ready, ready with conditions or not ready.

## 1. Data product and use

| Field | Entry |
|---|---|
| Data product name | [To confirm] |
| Type (curated tables, semantic model, dataset, other) | [To confirm] |
| Location and platform | [To confirm] |
| Data owner (role) | [To confirm] |
| Business owner (role) | [To confirm] |
| AI use: questions or tasks, audience and route | [To confirm] |
| Risk tier of the AI use | [To confirm] |
| Assessors and date | [To confirm] |

## 2. Criteria

| Criterion | Met / Partly / Not met | Evidence | Condition or fix | Owner | Due |
|---|---|---|---|---|---|
| Ownership accepted for AI use | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Purpose fit for the AI questions | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Meaning: descriptions, units, synonyms, definitions | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Quality of critical fields against requirements | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Currency: refresh pattern and data age shown | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Classification with AI-use rules applied | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Access pattern approved; outputs within entitlement | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Lineage at the depth the tier needs | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Change commitment to dependent AI solutions | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Test questions run with accepted answers | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 3. Test questions

| ID | Question as users would ask it | Accepted answer (from business owner) | AI answer | Correct? | Cause if wrong |
|---|---|---|---|---|---|
| Fictional example Q1 | How many open cases are older than 30 days in the north region? | Fictional example: 42 | Fictional example: 57 | No | Closed-pending status counted as open; description added |
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | Yes / No | [To confirm] |

Acceptance threshold agreed with the business owner: [To confirm]

## 4. Verdict

| Field | Entry |
|---|---|
| Verdict | Ready / Ready with conditions / Not ready |
| Conditions and dated fixes | [To confirm] |
| Re-assessment triggers (structural change, new AI use, quality breach) | [To confirm] |
| Next review date | [To confirm] |
| Data owner acceptance (role and date) | [To confirm] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

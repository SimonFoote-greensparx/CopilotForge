# Model selection record

Template id: `model-selection-record`

Responsible skill: `ai-foundry:model-selection`. The evidence section is completed with `ai-foundry:model-evaluation`.

Complete one record per model decision in a Microsoft Foundry solution, including replacements when a model is retired
or upgraded. Every fact the organisation must supply is marked `[To confirm: ...]`; replace the marker when the fact is
confirmed, and never fill it with a guess. Example rows are fictional. Model availability, regions, prices, terms and
retirement dates change often: record where the current fact is published and the date checked rather than copying
figures from memory. Licensing and commercial questions go to the Microsoft licensing guide, a licensing partner or
procurement; data protection questions go to the DPO.

## 1. Decision context

| Field | Entry |
|---|---|
| Solution name and design reference (`foundry-solution-design`) | [To confirm] |
| Risk tier and date classified | [To confirm] |
| Reason for this record (first selection / retirement / upgrade / cost or latency / other) | [To confirm] |
| Solution owner (role) | [To confirm] |
| Record version and date | [To confirm] |

## 2. Task definition

| Field | Entry |
|---|---|
| What the model must do (inputs, outputs, modality) | [To confirm] |
| What a good output looks like, and an unacceptable one | [To confirm] |
| Volume and latency envelope | [To confirm] |
| Example set reference (five to ten real or realistic examples) | [To confirm] |
| Data the model will see and its classification | [To confirm] |
| Constraints on where data may be processed | [To confirm] |

## 3. Filters

A candidate that fails any filter is out, whatever its quality.

| Filter | Rule applied | Confirmed by (role) | Date |
|---|---|---|---|
| Task and modality fit | [To confirm] | [To confirm] | [To confirm] |
| Data handling and processing location | [To confirm] | [To confirm] | [To confirm] |
| Terms and provenance (Microsoft-sold, partner or community) | [To confirm] | [To confirm] | [To confirm] |
| Lifecycle and support window | [To confirm] | [To confirm] | [To confirm] |
| Documented intended uses and limitations | [To confirm] | [To confirm] | [To confirm] |

## 4. Candidates

| Candidate and version | Provider type (Microsoft-sold / partner / community) | Passed all filters? | Reason if excluded | Source record checked and date |
|---|---|---|---|---|
| Fictional example: Model A, version 1 | Fictional example | Yes | - | Fictional example only |
| Fictional example: Model B, version 2 | Fictional example | No | Terms not yet reviewed by procurement | Fictional example only |
| [To confirm] | [To confirm] | Yes / No | [To confirm] | [To confirm] |

## 5. Evaluation evidence

Thresholds must be agreed and dated before any results are seen.

| Field | Entry |
|---|---|
| Test set name, version and held-back portion | [To confirm] |
| What was held constant across candidates (prompt, retrieval, tools, settings) | [To confirm] |
| Adjustments made for any candidate, and why | [To confirm, or "none"] |
| Number of runs per candidate | [To confirm] |
| Graders used (people, calibrated model grader) and calibration evidence | [To confirm] |
| Thresholds and date agreed, agreed by (role) | [To confirm] |

| Candidate | Task quality (mean and spread) | Groundedness | Tool calling and format | Latency | Cost per completed task and pricing source | Meets all thresholds? |
|---|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm, or not applicable] | [To confirm, or not applicable] | [To confirm] | [To confirm] | Yes / No |

Failure analysis by cause (missing context, wrong tool, format, over-refusal, other): [To confirm]

Subgroup results where outputs affect people: [To confirm, or not applicable with reason]

What the evaluation could not show: [To confirm]

## 6. Decision

| Field | Entry |
|---|---|
| Chosen model and version | [To confirm] |
| Reason (smallest candidate that meets every threshold, or other reason recorded) | [To confirm] |
| Fallback model and version, and its evaluation result | [To confirm] |
| Different models for different steps, if any | [To confirm, or "single model"] |
| Approved model list entry or recorded exception | [To confirm] |

## 7. Lifecycle

| Field | Entry |
|---|---|
| Where the current lifecycle and retirement information is published | [To confirm] |
| Version update setting chosen for the deployment | [To confirm] |
| Next review date and owner (role) | [To confirm] |
| Triggers for an earlier review (retirement notice, price change, quality drop, new candidate) | [To confirm] |

## 8. Reviewer gates

| Reviewer | Required from tier | Finding summary | Blocking / advisory | Resolved? |
|---|---|---|---|---|
| Security and privacy | [To confirm] | [To confirm] | [To confirm] | Yes / No |
| Responsible AI | [To confirm] | [To confirm] | [To confirm] | Yes / No |
| Design authority | [To confirm] | [To confirm] | [To confirm] | Yes / No |

## 9. Agreement

| Role | Name | Date |
|---|---|---|
| Solution owner | [To confirm] | [To confirm] |
| Technical owner | [To confirm] | [To confirm] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

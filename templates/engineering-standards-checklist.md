# Engineering standards checklist

Template id: `engineering-standards-checklist`

Responsible skill: `ai-engineering:ai-engineering-standards`. Sections draw on `ai-engineering:ai-solution-repository`,
`ai-engineering:secrets-and-identity`, `ai-engineering:ai-api-and-tooling`, `ai-engineering:ai-solution-testing`,
`ai-engineering:evaluation-harness`, `ai-engineering:ai-ci-cd`, `ai-engineering:ai-telemetry`,
`ai-engineering:ai-performance-engineering` and `ai-engineering:ai-resilience`.

Use this checklist during build of a custom AI solution and attach it to the design review. Every fact the organisation
must supply is marked `[To confirm: ...]`. Example entries are fictional. Tick an item only when the evidence is
attached or referenced. "N/A" needs a reason. An item that is mandatory at the solution's tier and is not met needs an
approved exception in section 12, or the checklist result is "Not conformant".

## 1. Solution

| Field | Entry |
|---|---|
| Solution name | [To confirm] |
| Risk tier | [To confirm: tier and date set] |
| Solution owner | [To confirm: name and role] |
| Engineering lead | [To confirm: name and role] |
| Repository | [To confirm: location] |
| Standards version used | [To confirm: version and date] |
| Checklist result | Conformant / Conformant with exceptions / Not conformant |

## 2. Repository and ownership

| Standard | Mandatory from tier | Evidence | Status |
|---|---|---|---|
| Prompts stored as versioned files, one per prompt | 1 | [To confirm] | Met / Not met / N/A |
| Model deployments and versions declared per environment | 1 | [To confirm] | Met / Not met / N/A |
| Tool definitions and retrieval settings versioned | 1 | [To confirm] | Met / Not met / N/A |
| Evaluation datasets versioned or referenced by immutable version | 2 | [To confirm] | Met / Not met / N/A |
| Infrastructure as code for all resources | 2 | [To confirm] | Met / Not met / N/A |
| Ownership file routes prompt and threshold changes to owners | 1 | [To confirm] | Met / Not met / N/A |
| Main branch protected; review and passing checks required | 1 | [To confirm] | Met / Not met / N/A |
| Readme, decision records and runbook present | 1 | [To confirm] | Met / Not met / N/A |

## 3. Identity and secrets

| Standard | Mandatory from tier | Evidence | Status |
|---|---|---|---|
| Managed or workload identities for service-to-service calls | 1 | [To confirm] | Met / Not met / N/A |
| No secrets in source, configuration files or pipeline variables | 1 | [To confirm: scan result] | Met / Not met / N/A |
| User context for user-scoped data and tools | 1 | [To confirm] | Met / Not met / N/A |
| Separate identities per environment | 1 | [To confirm] | Met / Not met / N/A |
| Least-privilege role assignments, reviewed | 2 | [To confirm] | Met / Not met / N/A |
| Secret scanning and push protection enabled | 1 | [To confirm] | Met / Not met / N/A |
| Secrets register with owners and rotation dates | 2 | [To confirm] | Met / Not met / N/A |

## 4. Tools and APIs

| Standard | Mandatory from tier | Evidence | Status |
|---|---|---|---|
| Narrow tools, one operation each, with clear descriptions | 1 | [To confirm] | Met / Not met / N/A |
| Contracts defined in machine-readable specifications and versioned | 2 | [To confirm] | Met / Not met / N/A |
| Server-side validation of every argument | 1 | [To confirm] | Met / Not met / N/A |
| Write tools separate, idempotent and confirmed upstream | 1 | [To confirm] | Met / Not met / N/A |
| Rate limits and timeouts declared and enforced | 2 | [To confirm] | Met / Not met / N/A |

## 5. Testing

| Standard | Mandatory from tier | Evidence | Status |
|---|---|---|---|
| Unit tests with stubbed model responses | 1 | [To confirm] | Met / Not met / N/A |
| Contract tests for tools and output schemas | 1 | [To confirm] | Met / Not met / N/A |
| Failure-path tests (timeout, throttling, filter block, malformed output, tool error) | 1 | [To confirm] | Met / Not met / N/A |
| Permission tests with users of different access | 2 | [To confirm] | Met / Not met / N/A |
| Adversarial tests including injection through inputs, documents and tool results | 2 | [To confirm] | Met / Not met / N/A |

## 6. Evaluation

| Standard | Mandatory from tier | Evidence | Status |
|---|---|---|---|
| Automated harness testing the deployed configuration | 2 | [To confirm] | Met / Not met / N/A |
| Thresholds agreed by the business owner before results were seen | 2 | [To confirm: date agreed] | Met / Not met / N/A |
| Model-graded evaluators calibrated against human labels | 2 | [To confirm] | Met / Not met / N/A |
| Zero-tolerance failures defined and reported separately | 2 | [To confirm] | Met / Not met / N/A |
| Results history stored with configuration per run | 2 | [To confirm] | Met / Not met / N/A |

Fictional example result: "Full set 240 cases; correctness 91% against threshold 88%; groundedness 96% against 95%;
zero-tolerance breaches none; grader agreement with human labels 0.85 on 50 cases."

## 7. CI/CD

| Standard | Mandatory from tier | Evidence | Status |
|---|---|---|---|
| Production deployment only through the pipeline | 2 | [To confirm] | Met / Not met / N/A |
| Evaluation gate on prompt, model, tool and retrieval changes | 2 | [To confirm] | Met / Not met / N/A |
| Production approval by named approvers per release policy | 2 | [To confirm] | Met / Not met / N/A |
| Rollback covers code, prompts, model configuration and infrastructure | 2 | [To confirm] | Met / Not met / N/A |
| Model version register with retirement dates | 2 | [To confirm: check source records for dates] | Met / Not met / N/A |
| Progressive exposure with monitoring | 3 | [To confirm] | Met / Not met / N/A |

## 8. Telemetry

| Standard | Mandatory from tier | Evidence | Status |
|---|---|---|---|
| End-to-end tracing with correlation ids | 2 | [To confirm] | Met / Not met / N/A |
| Model, prompt and tool versions recorded per request | 2 | [To confirm] | Met / Not met / N/A |
| Tokens, latency, errors and filter outcomes recorded | 2 | [To confirm] | Met / Not met / N/A |
| Content capture decision agreed with the DPO or data owner | 2 | [To confirm: decision and date] | Met / Not met / N/A |
| User identifiers pseudonymised in operational telemetry | 2 | [To confirm] | Met / Not met / N/A |

## 9. Performance

| Standard | Mandatory from tier | Evidence | Status |
|---|---|---|---|
| Latency targets agreed at a stated percentile | 3 | [To confirm] | Met / Not met / N/A |
| Per-step latency and token budgets | 3 | [To confirm] | Met / Not met / N/A |
| Capacity plan against expected peak | 3 | [To confirm] | Met / Not met / N/A |
| Load test results against targets | 3 | [To confirm] | Met / Not met / N/A |

## 10. Resilience

| Standard | Mandatory from tier | Evidence | Status |
|---|---|---|---|
| Timeouts on every external call | 2 | [To confirm] | Met / Not met / N/A |
| Bounded retries with backoff and jitter on idempotent calls only | 2 | [To confirm] | Met / Not met / N/A |
| Fallback deployments or models evaluated before use | 2 | [To confirm] | Met / Not met / N/A |
| Degraded mode and user messages designed with the business owner | 2 | [To confirm] | Met / Not met / N/A |
| Failure tests run in a test environment | 3 | [To confirm] | Met / Not met / N/A |

## 11. Operations hand-over

| Item | Entry |
|---|---|
| Support team and route | [To confirm] |
| Monitoring signals and alert routes | [To confirm] |
| Runbook location | [To confirm] |
| Next review date | [To confirm] |

## 12. Exceptions

| Standard | Reason | Compensating control | Risk accepted | Approver | Review date |
|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 13. Sign-off

| Role | Name | Decision | Date |
|---|---|---|---|
| Engineering lead | [To confirm] | [To confirm] | [To confirm] |
| Design authority reviewer | [To confirm] | [To confirm] | [To confirm] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

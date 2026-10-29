# Microsoft Foundry solution design

Template id: `foundry-solution-design`

Responsible skill: `ai-foundry:foundry-solution-assessment`. Sections are detailed with `ai-foundry:model-selection`,
`ai-foundry:foundry-agent-architecture`, `ai-foundry:foundry-tool-design`, `ai-foundry:mcp-integration`,
`ai-foundry:foundry-grounding-strategy`, `ai-foundry:retrieval-design`, `ai-foundry:foundry-prompt-engineering`,
`ai-foundry:model-evaluation` and `ai-foundry:foundry-safety-evaluation`.

Use this design from the moment a need reaches the Foundry rung until the solution is released, and keep it current
after every material change. Every fact the organisation must supply is marked `[To confirm: ...]`; replace the marker
when the fact is confirmed, and never fill it with a guess. Example rows are fictional and are there to be replaced or
deleted. Where a design choice depends on a product feature, model, region, limit or price, record the source record
checked and the date, because these change often. Licensing questions go to the Microsoft licensing guide or a
licensing partner; data protection questions go to the DPO.

## 1. Summary

| Field | Entry |
|---|---|
| Solution name | [To confirm: working name] |
| Problem statement and suitability record reference | [To confirm: reference and date] |
| Business owner (role) | [To confirm] |
| Product owner (role) | [To confirm] |
| Engineering team and technical owner | [To confirm] |
| Operations and support route | [To confirm] |
| Risk tier (0-4) and date classified | [To confirm] |
| Azure subscription, landing zone and Foundry project | [To confirm] |
| Design status | Draft / Agreed / Reviewed / Superseded |
| Version and date | [To confirm] |

## 2. Assessment

### 2.1 Capability drivers

| Driver | Applies? | Evidence |
|---|---|---|
| Model choice beyond what configured agents expose | Yes / No | [To confirm] |
| Retrieval engineering | Yes / No | [To confirm] |
| Complex orchestration | Yes / No | [To confirm] |
| AI embedded in a product, API or batch process | Yes / No | [To confirm] |
| Production-grade evaluation and observability | Yes / No | [To confirm] |

### 2.2 Lower rungs tested

| Option tried (Microsoft 365 agent, Copilot Studio agent, automation, hybrid) | What was tried | Why it fell short | Source record checked and date |
|---|---|---|---|
| Fictional example: Copilot Studio agent with SharePoint knowledge | Two-week spike on the claims library | Needed metadata filters by effective date that configured knowledge could not apply | Fictional example only |
| [To confirm] | [To confirm] | [To confirm] | [To confirm] |

### 2.3 Ownership conditions

| Condition | Status (met / not met / partly) | Evidence or action |
|---|---|---|
| Product owner and engineering team named | [To confirm] | [To confirm] |
| Azure foundation in place | [To confirm] | [To confirm] |
| Running cost funded beyond the first year | [To confirm] | [To confirm] |
| Operations route agreed | [To confirm] | [To confirm] |
| Reviewer capacity available at this risk tier | [To confirm] | [To confirm] |

### 2.4 Decision

| Field | Entry |
|---|---|
| Decision (proceed / proceed with preconditions / use a lower rung / stop) | [To confirm] |
| Preconditions and owners | [To confirm] |
| What this assessment cannot determine | [To confirm] |
| Decision owner and date | [To confirm] |

## 3. Model

| Field | Entry |
|---|---|
| Model selection record reference (`model-selection-record`) | [To confirm] |
| Chosen model and version | [To confirm] |
| Fallback model and version | [To confirm] |
| Lifecycle review date and owner | [To confirm] |

## 4. Agent architecture

Complete if the solution includes one or more agents.

| Field | Entry |
|---|---|
| Responsibility statement (one sentence) | [To confirm] |
| What the agent must refuse or hand over, and to whom | [To confirm] |
| Shape (single agent / coordinating agent with specialists) and reason | [To confirm] |
| Conversation state and cross-session memory, with retention agreed | [To confirm] |
| Launch surface | [To confirm] |
| Architecture diagram reference | [To confirm] |

| Action | Identity it runs under (user-delegated / managed identity) | Reason if not user-delegated | Human confirmation |
|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | Yes / No |

## 5. Tool register

One row per function or tool the organisation hosts. MCP servers are recorded in section 6.

| Tool | Purpose and model-facing description | Effect class (read low / read sensitive / reversible write / irreversible) | Identity | Controls (limits, idempotency, confirmation, audit) | Failure behaviour | System owner agreed | Test evidence |
|---|---|---|---|---|---|---|---|
| Fictional example: get_policy_section | Returns one section of a named policy by identifier | Read low | User-delegated | Result size limit | Structured "not found" | Yes, fictional | Fictional example only |
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | Yes / No | [To confirm] |

## 6. MCP server register

| Server | Owner and hosting | Terms and data handling reviewed by | Allowed tools | Effect class | Identity and authentication | Approval rule | Version pin or tool-list fingerprint | Change check rhythm |
|---|---|---|---|---|---|---|---|---|
| [To confirm, or "none"] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 7. Grounding and retrieval

| Field | Entry |
|---|---|
| Grounding approach and reason | [To confirm] |
| Content left in place rather than indexed, and why | [To confirm] |

| Source | Owner | Readiness verdict | Classification | Permission trimming (per user / open to all users, confirmed by owner) | Refresh and deletion route |
|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

| Retrieval design item | Entry |
|---|---|
| Cleaning rules | [To confirm] |
| Chunking approach | [To confirm] |
| Metadata kept on every chunk | [To confirm] |
| Search method and ranking | [To confirm] |
| Embedding model and version | [To confirm] |
| Passages passed to the model and citation format | [To confirm] |
| Retrieval test set reference and baseline | [To confirm] |

## 8. Prompts and output contract

| Field | Entry |
|---|---|
| Prompt location in source control and current version | [To confirm] |
| Prompt owner (role) | [To confirm] |
| Output schema and version, and consuming systems | [To confirm, or "free text only"] |
| How untrusted content is delimited | [To confirm] |
| Evidence required per change type | [To confirm] |

## 9. Evaluation and safety

| Field | Entry |
|---|---|
| Evaluation plan reference (`evaluation-plan`) | [To confirm] |
| Quality thresholds and date agreed | [To confirm] |
| Harm profile summary | [To confirm] |

| Safety control | Setting | Reason | Behaviour when it fires | Last changed, by whom, with what evidence |
|---|---|---|---|---|
| Input and output content filtering | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Prompt attack detection | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Groundedness or protected material checks | [To confirm, or not used with reason] | [To confirm] | [To confirm] | [To confirm] |
| Blocklists | [To confirm, or "none"] | [To confirm] | [To confirm] | [To confirm] |

Untested harms and residual risks: [To confirm]

## 10. Deployment, observability and cost

| Field | Entry |
|---|---|
| Environments and deployment topology | [To confirm] |
| Tracing and monitoring owner | [To confirm] |
| Running cost estimate, budget owner and source records used | [To confirm] |
| Pipeline and release process reference | [To confirm] |

## 11. Reviewer gates

| Reviewer | Required from tier | Finding summary | Blocking / advisory | Resolved? |
|---|---|---|---|---|
| Design authority | [To confirm] | [To confirm] | [To confirm] | Yes / No |
| Security and privacy | [To confirm] | [To confirm] | [To confirm] | Yes / No |
| Responsible AI | [To confirm] | [To confirm] | [To confirm] | Yes / No |
| Evaluation and quality | [To confirm] | [To confirm] | [To confirm] | Yes / No |

## 12. Open questions and preconditions

| Item | Owner | Due |
|---|---|---|
| [To confirm] | [To confirm] | [To confirm] |

## 13. Agreement

| Role | Name | Date |
|---|---|---|
| Business owner | [To confirm] | [To confirm] |
| Product owner | [To confirm] | [To confirm] |
| Technical owner | [To confirm] | [To confirm] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

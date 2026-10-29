# Copilot Studio solution design

Template id: `studio-solution-design`

Responsible skill: `copilot-studio:studio-agent-design`. Sections are detailed with `copilot-studio:topics-and-orchestration`,
`copilot-studio:studio-knowledge-architecture`, `copilot-studio:studio-actions-and-tools`, `copilot-studio:studio-connectors`,
`copilot-studio:studio-authentication`, `copilot-studio:dataverse-integration`, `copilot-studio:power-automate-actions`,
`copilot-studio:conversation-design` and `copilot-studio:multi-agent-design`.

Use this design after the agent brief is agreed and before build starts. Every fact the organisation must supply is
marked `[To confirm: ...]`; replace the marker when the fact is confirmed, and never fill it with a guess. Example rows
are fictional and are there to be replaced or deleted. Where a design choice depends on a product feature, record the
source record checked and the date, because availability, limits and licensing change often.

## 1. Summary

| Field | Entry |
|---|---|
| Agent name | [To confirm: working name] |
| Agent brief reference | [To confirm: brief reference and date agreed] |
| Business owner | [To confirm: name and role] |
| Technical owner and co-owner | [To confirm: names or team] |
| Copilot Studio Architect or reviewer | [To confirm] |
| Risk tier (0-4) | [To confirm: tier from risk classification, with date] |
| Design status | Draft / Agreed / Reviewed / Superseded |
| Version and date | [To confirm] |

## 2. Question-to-mechanism map

Map each representative question from the brief to the mechanism that should handle it. This map seeds orchestration
and knowledge tests.

| # | Representative question | Mechanism (knowledge / tool / authored topic / child or connected agent / exclusion) | Specific source, tool, topic or agent | Why this mechanism |
|---|---|---|---|---|
| 1 | Fictional example: "What is the mileage rate for a hire car?" | Knowledge | Fictional example: Travel policy library | Open question answered from owned policy |
| 2 | Fictional example: "Raise an expense claim for yesterday's taxi" | Tool | Fictional example: Create expense draft flow | Action in the expenses system with confirmation |
| 3 | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 3. Design decisions

Record the decision, the default it departs from (if any), the alternatives rejected and the reason.

| Dimension | Decision | Alternatives rejected and why | Source record checked and date |
|---|---|---|---|
| Orchestration (generative, classic or mixed) | [To confirm] | [To confirm] | [To confirm] |
| Structure (one agent, child agents, connected agents) | [To confirm] | [To confirm] | [To confirm] |
| Authentication setting | [To confirm] | [To confirm] | [To confirm] |
| Channels | [To confirm] | [To confirm] | [To confirm] |
| Environments and solution | [To confirm] | [To confirm] | [To confirm] |

## 4. Topics and orchestration

| Item (knowledge source, tool, topic or agent) | Name | Description used by orchestration | Authored or generative | Reason an authored topic is needed |
|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

System topic behaviour (greeting, fallback, escalation, errors, sign-in, end): [To confirm: summary or link to the conversation section]

Global variables and their scope: [To confirm]

## 5. Knowledge

| Source | Knowledge type | Scope (site, library, folder, table, domain) | Owner | Readiness verdict | Permission behaviour (trimmed to user / same for all) | Description | Refresh route |
|---|---|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | Ready / Ready with conditions / Not ready | [To confirm] | [To confirm] | [To confirm] |

Uploaded files (origin, owner, review date): [To confirm, or "none"]

Use of general model knowledge or public web: [To confirm: off, limited or on, with reason]

## 6. Tools, flows and connectors

| Tool | Type (connector action, flow, prompt, custom connector, REST API, MCP server) | System and operation | Read / create / update / send / delete | Identity it runs under | User confirmation | Failure message | Owner |
|---|---|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm: end user or approved service identity] | Yes / No | [To confirm] | [To confirm] |

| Connector | Data policy group per environment | Account behind the connection | Data leaves tenant or region? | Owner |
|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | Yes / No | [To confirm] |

Approvals for any shared or service identity: [To confirm: approver and date]

## 7. Dataverse

Complete if the agent reads or writes Dataverse records.

| Table | Columns used | Read / write | Identity and security roles | Sensitive columns excluded | Business rules relied on |
|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

Where conversation records are stored, who can read them and retention: [To confirm]

## 8. Authentication and identity

| Channel | Authentication | Single sign-on configured and tested | Identity provider owner |
|---|---|---|---|
| [To confirm] | [To confirm] | Yes / No | [To confirm] |

Secrets and certificates with renewal dates (record in the ALM plan): [To confirm]

## 9. Conversation

| Behaviour | Specification |
|---|---|
| Greeting and AI disclosure | [To confirm] |
| Voice and style sheet reference | [To confirm] |
| Clarification rules | [To confirm] |
| Escalation triggers and destinations | [To confirm] |
| Context passed on hand-off | [To confirm] |
| Out-of-hours message | [To confirm] |

## 10. Multi-agent design

Complete only if the solution uses child or connected agents, or calls agents on other platforms.

| Agent | Pattern | Owner | Contract (purpose, inputs, outputs, version) | Context passed | Identity | Failure behaviour |
|---|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

End-to-end owner: [To confirm]

## 11. Environments, ALM and deployment

| Item | Entry |
|---|---|
| Development, test and production environments | [To confirm: names and zones] |
| Solution and publisher | [To confirm] |
| ALM plan reference (`alm-and-environment-plan`) | [To confirm] |
| Channels and approved audience | [To confirm] |
| Rollout stages | [To confirm] |

## 12. Testing, analytics and run model

| Item | Entry |
|---|---|
| Test plan reference and release threshold agreed by business owner | [To confirm] |
| Zero-tolerance failures | [To confirm] |
| Success measures and where each is read | [To confirm] |
| Improvement review rhythm and attendees | [To confirm] |
| Support route for users | [To confirm] |
| Recertification frequency | [To confirm] |

## 13. Reviewer gates

| Reviewer | Required from tier | Finding summary | Blocking / advisory | Resolved? |
|---|---|---|---|---|
| Design authority | [To confirm] | [To confirm] | [To confirm] | Yes / No |
| Security and privacy | [To confirm] | [To confirm] | [To confirm] | Yes / No |
| Responsible AI | [To confirm] | [To confirm] | [To confirm] | Yes / No |
| Evaluation and quality | [To confirm] | [To confirm] | [To confirm] | Yes / No |

## 14. Open questions and preconditions

| Item | Owner | Due |
|---|---|---|
| [To confirm] | [To confirm] | [To confirm] |

## 15. Agreement

| Role | Name | Date |
|---|---|---|
| Business owner | [To confirm] | [To confirm] |
| Technical owner | [To confirm] | [To confirm] |
| Copilot Studio Architect | [To confirm] | [To confirm] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

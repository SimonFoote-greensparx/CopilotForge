# Agent card

Template id: `agent-card`

Responsible skill: `m365-agents:agent-ownership`. The knowledge list is completed with `m365-agents:agent-grounding`,
lifecycle state and history with `m365-agents:agent-lifecycle`, and value evidence with
`m365-agents:agent-value-measurement`.

One card per agent, kept current from build to retirement and linked from the solution register. Every fact the
organisation must supply is marked `[To confirm: ...]`; replace the marker when the fact is confirmed, and never fill it
with a guess. Example rows are fictional and are there to be replaced or deleted. Nobody is recorded as an owner until
they have accepted in writing.

## 1. Agent identity

| Field | Entry |
|---|---|
| Agent name | [To confirm] |
| Purpose (one sentence with the measure it improves) | [To confirm] |
| Link to agent brief | [To confirm: location of the `agent-brief`] |
| Build path and environment | [To confirm: for example Agent Builder or Copilot Studio, and environment or zone] |
| Risk tier (0-4) | [To confirm: tier and date classified] |
| Intended audience and sharing scope | [To confirm: named groups] |
| Solution register reference | [To confirm] |
| Lifecycle state | Live / Under change / Under review / Deprecated / Retired |
| Next review date | [To confirm] |

## 2. Owners

| Role | Name and job role | Deputy | Accepted in writing (date) |
|---|---|---|---|
| Business owner | [To confirm] | [To confirm] | [To confirm] |
| Executive sponsor (tier 3 and above) | [To confirm, or "not required at this tier"] | Not applicable | [To confirm] |
| Technical owner (team and named lead) | [To confirm] | [To confirm] | [To confirm] |
| Maker | [To confirm] | Not applicable | [To confirm] |

From tier 2, the business owner and technical owner are different people, and the maker is not the sole owner.

## 3. Knowledge sources and knowledge owners

| Source | Location and scope | Knowledge owner | Owner told the agent depends on it (date) | Readiness verdict | Source review date |
|---|---|---|---|---|---|
| Fictional example: Travel and expenses policy | Fictional example: Policies library, travel folder only | Fictional example: Head of finance operations | [To confirm] | Ready | [To confirm] |
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

Web content used: Yes / No. Answers restricted to named sources: Yes / No / Not supported. Reason: [To confirm]

## 4. Actions and connectors

| Action or connector | System | Read or write | Identity it runs under | User confirmation required | Accountable owner |
|---|---|---|---|---|---|
| [To confirm, or "none"] | [To confirm] | [To confirm] | [To confirm] | Yes / No | [To confirm] |

## 5. Support route

| Field | Entry |
|---|---|
| Where users report a wrong answer or fault | [To confirm] |
| Who triages | [To confirm] |
| Who fixes instructions, knowledge and configuration | [To confirm] |
| Where the route is shown to users | [To confirm: for example agent description or welcome message] |

## 6. Change rules

| Rule | Entry |
|---|---|
| Who may edit instructions and knowledge | [To confirm] |
| Who approves significant changes | [To confirm] |
| Where the change log and evaluation set are kept | [To confirm] |

## 7. Lifecycle history

| Date | Event (release, change, review, deprecation, retirement) | Decision and reason | Decided by |
|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] |

Retirement criteria agreed at release: [To confirm]

## 8. Value evidence

| Measure (from the brief) | Baseline | Latest result | Level reported | Date |
|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | Audience or team level only | [To confirm] |

## 9. Succession

| Event | What happens | Within |
|---|---|---|
| An owner leaves or changes role | Deputy covers; role reassigned and accepted in writing | [To confirm: agreed period] |
| No business owner can be found | Agent moves to Under review | Immediately |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

# Environment zoning plan

Template id: `environment-zoning-plan`

Responsible skill: `platform-governance:ai-environment-strategy`. Data policies per zone come from
`platform-governance:connector-policy`; maker levels from `platform-governance:maker-governance`; technical placement
from `ai-architecture:environment-topology`.

Every fact the organisation must supply is marked `[To confirm: ...]`. Platform controls, their availability and their
licensing change often: confirm each control against the current source records and route licensing questions to the
Microsoft licensing guide or a licensing partner before relying on it. Example content is fictional.

## 1. Scope and ownership

| Field | Entry |
|---|---|
| Plan owner (role) | [To confirm] |
| Platforms in scope | [To confirm: for example Copilot Studio, Power Platform, Agent Builder, Microsoft Foundry] |
| Governance framework and risk tier reference | [To confirm] |
| Date agreed and next review | [To confirm] |
| Agreed with security and privacy (role and date) | [To confirm] |

## 2. Zones

| Zone | Purpose | Zone owner (role) | Who may build | Data allowed | Sharing limit | Risk tiers hosted |
|---|---|---|---|---|---|---|
| 1. Personal productivity | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | 0 |
| 2. Team collaboration | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | 0, 1 |
| 3. Managed production | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm: per release] | 2, 3, 4 |

Add or split zones only with a recorded reason, for example a separate managed production zone for a regulated business
unit: [To confirm: reason, or "none"]

## 3. Controls per zone

| Control | Zone 1 | Zone 2 | Zone 3 | Source record checked and date |
|---|---|---|---|---|
| Data policy reference | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Sharing limits | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Maker routing for new makers | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Managed environment features | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Owner and register entry required | No | Yes | Yes | Not applicable |
| ALM and pipelines | No | [To confirm] | Yes | [To confirm] |
| Reviewer gates | None | [To confirm] | By tier, per release policy | Not applicable |
| Inactivity clean-up | [To confirm: period and action] | [To confirm] | [To confirm] | [To confirm] |

## 4. Environments mapped to zones

| Environment | Zone | Purpose | Owner (role) | Action needed |
|---|---|---|---|---|
| [To confirm: environment name] | [To confirm] | [To confirm] | [To confirm] | [To confirm: keep, move, merge, retire] |

Fictional example, for illustration only: "Site reports pilot development - zone 2 - created for a finished pilot; owner left
- action: confirm whether the two shared flows are still used, then retire."

## 5. Promotion rules

| Signal | Action | Who decides |
|---|---|---|
| Shared beyond the maker | Move to zone 2 with owner and register entry | [To confirm] |
| Classified tier 2 or above, or audience beyond a team | Move to zone 3 through the release policy | [To confirm] |
| Uses sensitive data or write actions in business systems | Zone 3 regardless of audience | [To confirm] |
| Inactive past the agreed period | Owner contacted, then archived or removed | [To confirm] |

## 6. Request process

| Request | How to ask | Approver | Target turnaround |
|---|---|---|---|
| New zone 2 environment | [To confirm] | [To confirm] | [To confirm] |
| New zone 3 environment set | [To confirm] | [To confirm] | [To confirm] |
| Promotion of a solution | [To confirm] | [To confirm] | [To confirm] |

## 7. Where do I build - maker summary

[To confirm: three or four plain-language sentences telling makers where to build personal helpers, team solutions and
organisational solutions, and how to ask for help]

## 8. Approval

| Role | Decision | Date |
|---|---|---|
| Platform governance lead | [To confirm] | [To confirm] |
| Security and privacy reviewer | [To confirm] | [To confirm] |
| CoE lead | [To confirm] | [To confirm] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

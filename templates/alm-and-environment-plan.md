# ALM and environment plan

Template id: `alm-and-environment-plan`

Responsible skill: `copilot-studio:studio-alm`. The environment section is completed with
`copilot-studio:studio-environments`, and connection details with `copilot-studio:studio-connectors` and
`copilot-studio:studio-authentication`.

Use this plan before a Copilot Studio agent moves beyond the environment it was built in, and update it whenever the
agent's design or environments change. Every fact the organisation must supply is marked `[To confirm: ...]`; replace
the marker when the fact is confirmed, and never fill it with a guess. Example rows are fictional and are there to be
replaced or deleted. Never record secrets, passwords or keys in this plan.

## 1. Summary

| Field | Entry |
|---|---|
| Agent or solution name | [To confirm] |
| Solution design reference (`studio-solution-design`) | [To confirm] |
| Business owner | [To confirm] |
| Technical owner and co-owner | [To confirm] |
| Risk tier (0-4) | [To confirm] |
| Release approver(s) by tier | [To confirm: from the organisation's release policy] |
| Plan version and date | [To confirm] |

## 2. Environments

| Stage | Environment name | Governance zone | Managed Environment | Security group | Data policy | Admin owner | Who may make changes |
|---|---|---|---|---|---|---|---|
| Development | Fictional example: Finance agents - dev | Team collaboration | Yes | Fictional example: Finance agent makers | [To confirm] | [To confirm] | Named makers |
| Test | [To confirm] | [To confirm] | Yes / No | [To confirm] | [To confirm] | [To confirm] | [To confirm] |
| Production | [To confirm] | [To confirm] | Yes / No | [To confirm] | [To confirm] | [To confirm] | Pipeline only |

Environment routing for new makers in this area: [To confirm]

Agent settings that differ by environment (sharing limits, web knowledge, unauthenticated agents, analytics, transcripts): [To confirm]

## 3. Solutions

| Solution | Publisher | Contents (agent, flows, connectors, tables, child agents) | Owner | Depends on |
|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm: shared solutions] |

Shared component solutions used by this agent, and their owners and release cadence: [To confirm, or "none"]

## 4. Environment variables

| Variable | Purpose | Development value | Test value | Production value | Owner |
|---|---|---|---|---|---|
| Fictional example: Policy site URL | Knowledge location | Fictional example: dev site | [To confirm] | [To confirm] | [To confirm] |
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 5. Connection references and identities

| Connection reference | Connector | Account type (end user / service account) | Development connection owner | Test connection owner | Production connection owner | Approval |
|---|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm: approver and date] |

Secrets and certificates (location in the managed store, not the value) and renewal dates:

| Item | Used by | Stored in | Renewal date | Owner |
|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 6. Knowledge per environment

| Knowledge source | Development location | Test location | Production location | Post-import check |
|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 7. Pipelines and source control

| Item | Entry |
|---|---|
| Pipeline route (development to test to production) | [To confirm] |
| Import type into test and production | Managed / [To confirm: reason if otherwise] |
| Source control repository and branch approach | [To confirm, or "not yet used"] |
| Automated checks in the pipeline | [To confirm] |
| Who can run the production stage | [To confirm] |

## 8. Release process

| Step | Evidence | Responsible role |
|---|---|---|
| Change recorded with version number | Release record | [To confirm] |
| Regression pack run in test | Results compared with baseline | [To confirm] |
| Reviewer checks for this tier | Reviewer findings resolved | [To confirm] |
| Business owner approval | Recorded decision | [To confirm] |
| Import to production | Pipeline run record | [To confirm] |
| Post-import checks (knowledge, connections, channels, sign-in) | Check results | [To confirm] |

Emergency change route, and how emergency changes are replayed in development: [To confirm]

## 9. Rollback

| Item | Entry |
|---|---|
| Previous version kept | [To confirm: location of the previous managed solution] |
| Rollback method | [To confirm: re-import, unpublish a channel, narrow sharing] |
| Who can roll back | [To confirm] |
| Rollback rehearsed (tier 3 and above) | Yes / No, date [To confirm] |

## 10. Release history

| Version | Date | Summary of change | Regression result | Approver |
|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 11. Agreement

| Role | Name | Date |
|---|---|---|
| Technical owner | [To confirm] | [To confirm] |
| Platform or environment owner | [To confirm] | [To confirm] |
| Business owner | [To confirm] | [To confirm] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

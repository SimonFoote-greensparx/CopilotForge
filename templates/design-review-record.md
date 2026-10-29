# Design review record

Template id: `design-review-record`

Responsible skill: `design-authority:ai-design-review`. Sections 4 to 8 are completed with
`design-authority:ai-necessity-challenge`, `design-authority:platform-fit-review`,
`design-authority:architecture-conformance`, `design-authority:supportability-review` and, for changes to live
solutions, `design-authority:ai-change-impact-review`.

Every fact the organisation must supply is marked `[To confirm: ...]`. Example rows are fictional. Each finding is
classified **blocking** or **advisory**, names the risk or standard behind it, and gives the fix and owner. From risk
tier 2 a blocking finding stops the gate and is not traded against dates. Disagreement escalates to the accountable
executive, whose written risk acceptance is recorded in section 10.

## 1. Solution and scope

| Field | Entry |
|---|---|
| Review reference | [To confirm] |
| Solution name and brief reference | [To confirm] |
| Review type | [To confirm: new design, material change, re-design, pilot to service] |
| Risk tier (confirmed at review) | [To confirm: 0-4, with classification reference] |
| Business owner (role) | [To confirm] |
| Accountable executive (tier 3 and 4) | [To confirm] |
| Reviewers and date | [To confirm] |

## 2. Design pack completeness

| Artefact | Present | Reference | Note |
|---|---|---|---|
| Solution or agent brief | Yes / No | [To confirm] | [To confirm] |
| Suitability decision | Yes / No | [To confirm] | [To confirm] |
| Risk classification | Yes / No | [To confirm] | [To confirm] |
| Architecture decision records | Yes / No | [To confirm] | [To confirm] |
| Non-functional requirements | Yes / No | [To confirm] | [To confirm] |
| Identity map | Yes / No | [To confirm] | [To confirm] |
| Interface catalogue | Yes / No / Not applicable | [To confirm] | [To confirm] |
| Grounding design | Yes / No / Not applicable | [To confirm] | [To confirm] |
| Placement in environment topology | Yes / No | [To confirm] | [To confirm] |
| Evaluation approach and thresholds | Yes / No | [To confirm] | [To confirm] |
| Support model and owners | Yes / No | [To confirm] | [To confirm] |

If a core artefact is missing, the verdict is "returned - incomplete" and the list above is sent back.

## 3. Lenses applied

| Lens | Depth (in depth, summary, not applied) | Reason |
|---|---|---|
| Necessity | [To confirm] | [To confirm] |
| Platform fit | [To confirm] | [To confirm] |
| Conformance | [To confirm] | [To confirm] |
| Non-functional requirements | [To confirm] | [To confirm] |
| Supportability | [To confirm] | [To confirm] |
| Change impact (live solutions) | [To confirm] | [To confirm] |

## 4. Necessity findings

| Component | Test | Finding | Blocking or advisory | Simpler alternative | Fix | Owner | Due |
|---|---|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 5. Platform fit findings

| Dimension | Evidence | Finding | Blocking or advisory | Fix | Owner | Due |
|---|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 6. Conformance findings and deviations

Reference architecture and version: [To confirm]

| Control or fixed decision | Gap | Blocking or advisory | Fix or approved deviation | Compensating control | Owner | Expiry |
|---|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 7. Supportability findings

| Area | Evidence | Finding | Blocking or advisory | Fix | Owner | Due |
|---|---|---|---|---|---|---|
| [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] | [To confirm] |

## 8. Change impact (live solutions only)

| Field | Entry |
|---|---|
| Change requested and reason | [To confirm] |
| Behavioural description of the change | [To confirm] |
| Classification | [To confirm: minor, material, re-design] |
| Gates re-engaged | [To confirm] |
| Regression evaluation reference | [To confirm] |
| Rollback route | [To confirm] |

Fictional example, for illustration only: "Adding the procurement policy library means the agent will answer purchasing
questions for all staff using content previously available only to procurement - classified material; security exposure
review and regression evaluation re-engaged."

## 9. Other reviewer status

| Reviewer department | Status | Dependencies on design changes |
|---|---|---|
| Security and privacy | [To confirm] | [To confirm] |
| Evaluation and quality | [To confirm] | [To confirm] |
| Responsible AI (tier 3 and 4) | [To confirm] | [To confirm] |

## 10. Verdict and sign-off

| Field | Entry |
|---|---|
| Verdict | [To confirm: approved, approved with advisory findings, not approved - blocking findings, returned - incomplete] |
| Conditions | [To confirm] |
| Design authority chair (role) and date | [To confirm] |
| Business owner acknowledgement and date | [To confirm] |
| Written risk acceptance, if any (finding reference, accepted by, date, expiry) | [To confirm] |
| Blocking findings closed on evidence (reference and date) | [To confirm] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

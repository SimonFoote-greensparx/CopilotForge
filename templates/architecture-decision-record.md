# Architecture decision record

Template id: `architecture-decision-record`

Responsible skill: `ai-architecture:platform-selection`. The same record is used for other architecture decisions, for
example by `ai-architecture:ai-integration-patterns`, `ai-architecture:grounding-patterns` and
`ai-architecture:environment-topology`.

One record per significant decision. Every fact the organisation must supply is marked `[To confirm: ...]`; never record
an estimate as a measured figure. Product availability, licensing, limits and regional support change often: cite the
source record you checked and the date, and route licensing questions to the Microsoft licensing guide or a licensing
partner. Example content is fictional.

## 1. Decision summary

| Field | Entry |
|---|---|
| Record reference | [To confirm: reference] |
| Title (the decision in one line) | [To confirm: for example "Build the site report agent in Copilot Studio"] |
| Solution or portfolio scope | [To confirm: solution name and brief reference] |
| Risk tier and rationale reference | [To confirm: tier 0-4 and classification reference] |
| Status | [To confirm: proposed, accepted, superseded or retired] |
| Decision owner (role) | [To confirm: role] |
| Date decided | [To confirm: date] |
| Supersedes or superseded by | [To confirm: record reference, or "none"] |

## 2. Context

Describe the need without naming a product: who uses the solution, through which surface, what it knows, what it does in
other systems and who answers for it.

[To confirm: one or two paragraphs]

Constraints that apply (platform strategy, approved platforms, residency, skills, budget):

[To confirm: list of constraints with their source]

## 3. Options considered

List every option seriously considered, including the one chosen. A record with only the chosen option is incomplete.

| Option | Summary | First disqualifying reason, if any |
|---|---|---|
| [To confirm: option] | [To confirm: summary] | [To confirm: reason, or "none"] |
| [To confirm: option] | [To confirm: summary] | [To confirm: reason, or "none"] |
| [To confirm: option] | [To confirm: summary] | [To confirm: reason, or "none"] |

## 4. Gates applied to the leading option

| Gate | Question | Answer | Evidence or source checked, with date |
|---|---|---|---|
| Identity | Can every action run under the user or a narrowly scoped service identity? | Yes / No / To confirm | [To confirm] |
| Data | Can grounding stay permission-trimmed and inside agreed boundaries? | Yes / No / To confirm | [To confirm] |
| Operability | Can the named operating team monitor, change and support it? | Yes / No / To confirm | [To confirm] |
| Lifecycle | Can changes be tested, promoted and rolled back? | Yes / No / To confirm | [To confirm] |
| Evaluation | Can the tier's evaluation requirements be met and evidenced? | Yes / No / To confirm | [To confirm] |
| Cost | Is run cost understood well enough to fund, per the licensing guide or partner? | Yes / No / To confirm | [To confirm] |

## 5. Decision

[To confirm: the decision, stated plainly, with the part of the solution it applies to where the solution has several parts]

## 6. Consequences

| Consequence | Positive or negative | Owner of any follow-up |
|---|---|---|
| [To confirm: consequence] | [To confirm] | [To confirm: role] |

Preconditions that must be met before build or release:

[To confirm: list, or "none"]

## 7. Volatile facts relied on

| Fact | Source record | Date checked | Recheck by |
|---|---|---|---|
| [To confirm: capability, region, limit or entitlement] | [To confirm: source id] | [To confirm] | [To confirm] |

## 8. Revisit triggers

Conditions that would reopen this decision, for example a second channel, write actions in a new system, a model
retirement or a change in residency commitments.

[To confirm: triggers]

## 9. Review and sign-off

| Role | Decision or finding | Date |
|---|---|---|
| Decision owner | [To confirm] | [To confirm] |
| Design authority reviewer (tier 2 and above) | [To confirm: approved, approved with advisory findings, or blocking findings reference] | [To confirm] |
| Security and privacy reviewer (where identity or data gates apply) | [To confirm] | [To confirm] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

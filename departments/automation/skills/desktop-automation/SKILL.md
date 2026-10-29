---
name: desktop-automation
description: Decides when desktop flows that drive a user interface are justified for legacy systems with no connector or API, and sets the conditions for using them with care - attended or unattended runs, machines, credentials, fragile selectors, AI on screen content, ownership and an exit plan. Use when a step can only be done through a screen, when desktop flows keep breaking after updates, or when unattended runs are proposed.
license: CC-BY-4.0
metadata:
  department: automation
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: power-platform, entra
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, design-authority
  sources: ms-managed-environments, ms-copilot-studio-security-governance, ms-coe-starter-kit
  status: draft
  authors: Simon Foote
---

# Desktop automation

## Purpose

Some systems offer no connector or API, only a screen, and desktop flows that click and type on a person's behalf can
bridge the gap. They are also the most fragile, least secure and most expensive kind of automation to keep running.
This skill decides when a desktop flow is justified and sets the conditions for using one: the run mode, the machine,
the credentials, how screens are read, who owns it and how it will be retired. Desktop automation goes wrong when it is
chosen because it is quick to record, when unattended bots run on shared or personal credentials, and when nobody plans
for the day the target system changes.

## When to use

- An automation assessment marks a step as user-interface-only, with no supported connector or API.
- A team proposes recording a desktop flow for a legacy, mainframe, terminal or vendor application.
- Desktop flows break after application or operating system updates, and support effort is rising.
- Unattended runs on a server or virtual machine are proposed, and credentials and machines need deciding.
- AI is proposed to read screen content, scanned documents or images inside a desktop flow.

## When not to use

- Deciding which steps need automation, AI or a person - use `automation:automation-assessment`.
- Cloud flow structure, triggers and AI step validation - use `automation:flow-design-patterns`.
- Governing connectors and connections for cloud flows - use `automation:automation-connector-governance`.
- Building an API or integration layer for the legacy system instead - use `ai-architecture:ai-integration-patterns`.
- Retry and exception routing in detail - use `automation:exception-handling`.

## Questions to ask first

1. Is there really no API, export, file drop, database view or vendor connector, and is one planned?
2. Will the flow run attended, alongside a person at their desk, or unattended on a machine with nobody watching?
3. Whose credentials will it use to sign in to the target system, and are they allowed to be used by software?
4. How often does the target application change its screens, and will the automation team be told in advance?
5. What happens to the business process if the desktop flow stops for a day, or a week?

## Required inputs

- The automation assessment and design, with the user-interface-only steps marked.
- Confirmation from the system owner that no supported integration route exists, and whether one is planned.
- The target application's release pattern and the contact for advance notice of changes.
- Available machines and the organisation's rules for service accounts and unattended sign-in.
- The risk tier and data sensitivity.

If the system owner cannot confirm there is no integration route, ask the question formally before building. If the
terms of use of the target system are unclear about automated access, route the question to the system owner or legal
adviser rather than assuming.

## Decision framework

| Condition | Attended desktop flow | Unattended desktop flow | Do not use a desktop flow |
|---|---|---|---|
| Integration route | None available or planned soon | None available or planned soon | An API, export or connector exists or is imminent |
| Volume and timing | Moderate; a person is present and can intervene | High or out of hours | Very low; a person handles it quickly |
| Credentials | The person's own, within their rights | Dedicated account with least privilege, stored in a managed vault | Shared or personal credentials would be needed unattended |
| Screen stability | Stable or change notice given | Stable and change notice given | Screens change often without notice |
| Impact of an outage | A person can do it by hand | A manual fallback is documented and staffed | No fallback and the process is critical |

Every desktop flow has an exit plan: the integration route that would replace it and the trigger for switching.

## Practitioner approach

Challenge the premise first. Ask the system owner and the vendor, in writing, whether an API, a scheduled export, a file
interface, a reporting database or a connector exists. Teams often reach for desktop flows because they do not know who
to ask. A modest integration request can remove years of fragile screen automation.

If a desktop flow is justified, decide the run mode. Attended flows run while a person is signed in and watching; they
use that person's access, and the person can step in when a screen looks wrong. They suit moderate volumes and
processes where judgement is close at hand. Unattended flows run on a machine with nobody present; they need a
dedicated machine or machine group, a dedicated account with only the access the process needs, and credentials held in
a managed store rather than typed into the flow.

Build for brittleness. Prefer stable selectors (identifiers and names over screen positions and image matching), check
that each expected screen has appeared before acting, and stop safely if it has not. Keep each desktop flow short and
called from a cloud flow that handles orchestration, logging and exceptions. Long desktop flows are hard to debug and
hard to restart.

Use AI on screen content with the same discipline as any AI step. Where text recognition or a model reads a scanned
form or a screen region, ask for structured output, validate it and route low-confidence results to a person, following
`automation:flow-design-patterns`. Never let a misread value be typed straight into a system of record.

Arrange change notice. Agree with the application owner that the automation team is told before screen changes, and
schedule a regression run after every update to the target application, the operating system or the browser. Record
each desktop flow in the solution inventory with its target application and version.

Plan for outage and exit. Document the manual fallback and who staffs it. Record the integration route that would
replace the flow and review it at least yearly with the system owner. A desktop flow that has outlived its exit plan
should be on the retirement list.

## Outputs

- A desktop automation decision record: integration routes checked, justification, run mode, machine, account and credential store, screen stability, fallback and exit plan.
- A desktop flow specification: steps, selectors approach, screen checks, AI steps with validation, calling cloud flow and exception routes.
- An entry in the solution inventory with target application, version, owner and next review date.

## Microsoft platform considerations

Power Automate desktop flows support attended and unattended runs, machine and machine group registration, credential
integration with managed vaults and AI-based reading of documents and screens. Capabilities, run modes and licensing
differ and change often. Check current behaviour in `references/sources.md`, and route licensing questions about
unattended runs to the Microsoft licensing guide or a licensing partner.

## Adoption considerations

Attended automations change the working day of the person beside them. Agree when the flow runs, what they should do if
it stops and how to report problems. Do not present desktop flows as permanent; set expectations that they will be
replaced when an integration route arrives.

## Knowledge considerations

Not applicable to most desktop automation, because it drives screens rather than grounding on knowledge. Keep the
screen-by-screen procedure and fallback instructions current, since they are the knowledge the manual fallback depends on.

## Security and privacy considerations

Unattended accounts must be dedicated, least privilege and stored in a managed credential store; machines running
unattended flows must be hardened, patched and monitored. Screen recordings and logs can capture personal data, so
restrict access and set retention. Shared or personal credentials for unattended runs are not acceptable.

## Responsible AI considerations

Where AI reads screens or scanned documents about people, misreads can produce wrong decisions about them. Validate and
route low-confidence results to a person, and check that the model handles the range of documents and languages the
process receives.

## Evaluation requirements

Test against the current version of the target application with real screens, including error dialogs and slow
responses. Re-run the regression set after every update to the application, operating system or browser, and before
promotion.

## Value measures

Track run success rate, failures by cause (screen change, timeout, credential), support effort and manual fallback
use, at automation level. Compare the run cost with the cost of the integration route at each yearly review. The
automation owner reports these to the process owner.

## Scale notes

### Starter

Use attended desktop flows only, for a small number of stable applications, called from cloud flows. Avoid unattended
runs until accounts, machines and credential storage are properly set up.

### Scale

Introduce unattended runs on managed machine groups with dedicated accounts and vaulted credentials. Keep a register of
desktop flows by target application and review exit plans yearly.

### Enterprise

Run desktop automation as a managed service with patching, capacity planning, change notice from application owners and
a portfolio plan to replace desktop flows with integrations. Report fragility and cost across the estate.

## Hand-offs

- To `ai-architecture:ai-integration-patterns` when an integration route should replace the desktop flow.
- To `automation:exception-handling` for screen failure and recovery routes.
- To `automation:automation-monitoring` for run health and alerting.
- To `security-privacy:connector-review` for unattended accounts and credential handling from tier 2.

## Reviewer gates

From risk tier 2, `security-privacy` reviews unattended accounts, machines and credential storage, and shared or personal
credentials in an unattended run are blocking. `design-authority:platform-fit-review` may challenge a desktop flow where an
integration route exists.

## Failure modes

- A desktop flow is recorded because it is quick, and an available API is never investigated.
- The vendor updates a screen, the flow types data into the wrong field and nobody notices for days.
- Unattended runs use a former employee's credentials or a shared account with broad access.
- No manual fallback is documented, and the process stops when the machine fails.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Build a desktop flow without first asking the system owner for an integration route.
- Run unattended flows on personal or shared credentials, or credentials typed into the flow.
- Type an unvalidated AI reading of a screen or document into a system of record.
- Leave a desktop flow without a manual fallback and an exit plan.

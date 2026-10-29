# AI governance framework and acceptable-use starter

Template id: `ai-governance-starter`

Responsible skill: `ai-centre-of-excellence:coe-governance-model`.

How to use this template: Part A is the acceptable-use starter for all staff; publish it first, in plain language. Part B
is the governance framework for the CoE or working group. Replace every `[To confirm: ...]` marker only with what your
organisation has agreed. Legal and regulatory interpretations come from your legal adviser or data protection officer,
not from this template. Product capabilities and licensing must be checked against current Microsoft documentation.

---

# Part A. Acceptable-use starter

## A1. Why this guide exists

[To confirm: two sentences from the sponsor on why the organisation wants people to use AI, and use it safely.]

AI assists decision making. People remain accountable for outcomes.

## A2. Approved tools

| Tool | Approved for | Not approved for |
|---|---|---|
| [To confirm: approved tool] | [To confirm] | [To confirm] |
| [To confirm: approved tool] | [To confirm] | [To confirm] |

If you want to use a tool not on this list, [To confirm: route, for example ask in the AI community channel or contact
the CoE lead]. Each prohibition has an approved alternative where one exists.

## A3. Your responsibilities

- Check what AI produces before you rely on it or send it. You remain responsible for your work.
- Do not put [To confirm: data categories, for example client confidential or special category personal data] into tools that are not approved for it.
- Say when content is substantially AI-generated where it matters: [To confirm: situations, for example client deliverables].
- Do not use AI to make or inform decisions about people (hiring, performance, eligibility) without [To confirm: required approval].
- Share useful prompts and ideas through [To confirm: channel], not by copying sensitive material.

## A4. Building or sharing something

Anything you share beyond yourself (a prompt pattern for your team, a Cowork task design, an agent) needs a named owner
and a register entry. Start here: [To confirm: intake route].

## A5. Getting help

[To confirm: Champions, service desk route, CoE contact by role.]

---

# Part B. Governance framework

## B1. Principles

[To confirm: for example business-owned, proportionate, human accountability explicit, govern once and repeat everywhere.]

## B2. Governance areas

| Area | Question it answers | Owning role | Minimum control by tier |
|---|---|---|---|
| Security | Can only the right people and systems reach the solution and what it reaches? | [To confirm: information security role] | [To confirm] |
| Privacy | Is personal data used lawfully, minimally and transparently? | [To confirm: data protection role] | [To confirm] |
| Data ownership | Does every knowledge source and data set have a business owner who keeps it current? | [To confirm: business and knowledge owners] | [To confirm] |
| Compliance | Does the solution meet policy, contract and regulatory obligations? | [To confirm: compliance or legal role] | [To confirm] |
| Human accountability | Which named role answers for each outcome the solution informs? | [To confirm: business owner] | [To confirm] |

## B3. Risk tiers and minimum controls

Classify by the highest applicable factor: reach, data sensitivity, autonomy, impact on people and external exposure.
Each tier inherits the controls of the tiers below it.

| Tier | Description | Examples in this organisation | Minimum controls | Reviewer gates | Release decided by |
|---|---|---|---|---|---|
| 0 | Individual productivity | [To confirm] | Acceptable-use starter, approved tools, human verification | None | Not applicable |
| 1 | Team or shared | [To confirm] | Named owner, defined audience, approved knowledge sources, basic test evidence, register entry | None by default | Owner, recorded in register |
| 2 | Organisational solution | [To confirm] | Business and knowledge owners, security and privacy review, evaluation against threshold, release and support plan | Security and privacy (blocking), evaluation, design challenge | [To confirm: CoE release decision role] |
| 3 | Business-critical | [To confirm] | Formal architecture, privacy impact assessment, responsible AI review, monitoring, continuity plan | Tier 2 gates plus responsible AI | [To confirm: steering with accountable executive] |
| 4 | External or high-impact | [To confirm] | Full assurance, human oversight, escalation, incident response, executive risk acceptance | All gates, formal evidence | [To confirm: executive role], in writing |

Target decision times: tier 0 none; tier 1 [To confirm]; tier 2 [To confirm]; tier 3 and 4 [To confirm].

## B4. Uses we will not build

- [To confirm]
- [To confirm]

## B5. Agent portfolio register fields

Categories: Microsoft 365 agents, Copilot Studio agents, automations, integrations. [To confirm: any further categories.]

| Field | Required from tier |
|---|---|
| Solution name and purpose | 1 |
| Category | 1 |
| Business owner (role) | 1 |
| Knowledge owner (role) and knowledge sources | 1 |
| Technical owner (role) | 1 |
| Platform | 1 |
| Audience and reach | 1 |
| Data sensitivity | 1 |
| Risk tier and who classified it | 1 |
| Reviews completed and outcome | 2 |
| Evaluation evidence reference | 2 |
| Release date and release decision reference | 1 |
| Support route | 2 |
| Review date | 1 |
| Measured value against baseline | 2 |
| Status (active, suspended, retired) | 1 |

## B6. Knowledge asset register fields

Every document an agent or automation relies on carries these fields. Layers: policies and standards; procedures;
templates and guidance; FAQs and lessons learned; the agents and automations built on them.

| Field | Value |
|---|---|
| Asset name and layer | [To confirm] |
| Owner (role) | [To confirm] |
| Review date | [To confirm] |
| Version | [To confirm] |
| Classification | [To confirm: per the organisation's classification scheme] |
| Used by (solutions in the portfolio register) | [To confirm] |

## B7. Ownership and lifecycle rules

| Event | Rule |
|---|---|
| Owner leaves or changes role | Reassign within [To confirm: period] or suspend |
| Audience or data changes | Re-classify before the change takes effect |
| Periodic review | Tier 1 every [To confirm]; tier 2 every [To confirm]; tier 3 and 4 every [To confirm] |
| No use or no owner for [To confirm: period] | Retire after notice to the last known owner |

## B8. Reviewer gates

| Gate | From tier | Blocking | Held by (role) until the reviewer department exists |
|---|---|---|---|
| Security and privacy | 2 | Yes, not skippable | [To confirm] |
| Evaluation and quality | 2 | Yes | [To confirm] |
| Design challenge | 2 | Yes | [To confirm] |
| Responsible AI | 3 | Yes | [To confirm] |

A blocking finding is not traded off against a date. Disagreement goes to [To confirm: accountable executive role] and
is recorded in writing.

## B9. Platform controls mapped to tiers

| Tier | Platform control in use | Confirmed by (role) and date |
|---|---|---|
| [To confirm] | [To confirm: control, checked against current Microsoft documentation] | [To confirm] |

## B10. Exceptions and escalation

[To confirm: how an exception is requested, who decides, how long it lasts and where it is recorded.]

## B11. Standards cross-reference (optional)

[To confirm: only if needed, for example a mapping to a recognised AI risk management framework or management system standard.]

## B12. Approval

| Role | Decision | Date |
|---|---|---|
| [To confirm: sponsor role] | | |
| [To confirm: information security role] | | |
| [To confirm: data protection role] | | |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

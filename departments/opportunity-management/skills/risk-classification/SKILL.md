---
name: risk-classification
description: Assigns a progressive risk tier from 0 to 4 to an AI opportunity or solution by rating impact, reach, data sensitivity and autonomy, then derives the minimum governance posture and the reviewer gates it must pass, and re-classifies when scope changes. Use when an idea has a chosen pattern, when a solution is about to be shared more widely, or when someone asks which reviews a build needs.
license: CC-BY-4.0
metadata:
  department: opportunity-management
  lifecycle: Envision, Assure, Scale
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-code, copilot-studio, ai-foundry, power-platform
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, responsible-ai, evaluation-quality, design-authority
  sources: nist-ai-rmf, ico-ai-data-protection, ms-copilot-studio-zoned-governance, ms-copilot-privacy, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Risk classification

## Purpose

This skill decides how much governance an AI initiative needs, so that a personal prompt pattern and a customer-facing
agent do not pass through the same gates. It rates four factors, assigns one of the five progressive risk tiers, and
states the minimum controls and the reviewer gates that follow. Classification usually goes wrong in three ways:
everything is treated as high risk and the organisation drives people to ungoverned tools; tiers are chosen to avoid
review; or a solution is classified once and never revisited as its audience, data or autonomy grows.

## When to use

- An opportunity has passed suitability and a candidate pattern is chosen, so the controls it needs can be planned.
- A team asks which reviews, approvals or tests a solution requires before release.
- A solution is about to be shared with a wider audience, connected to new data or allowed to take actions.
- A live solution has changed scope, or an incident suggests it was under-classified.

## When not to use

- Deciding whether AI is appropriate at all, or which pattern fits - use `opportunity-management:ai-suitability`.
- Carrying out the security review of data exposure that tier 2 and above requires - use `security-privacy:data-exposure-review`.
- Assessing data protection obligations in detail - use `security-privacy:privacy-assessment`.
- Reviewing connectors and actions an agent will use - use `security-privacy:connector-review`.
- Writing the organisation's overall governance model and acceptable-use policy - use `ai-centre-of-excellence:coe-governance-model`.

## Questions to ask first

1. Who will see or rely on the output: one person, a team, a department, the whole organisation, or customers and the public?
2. What happens if the output is wrong, and could it affect a decision about a person, money, safety, legal position or rights?
3. What data will the solution read, and does it include personal, special category, confidential or regulated information?
4. Does a person review every output before it has an effect, or can the solution act, send or decide on its own?
5. What has changed since any previous classification?

## Required inputs

- The framed problem and suitability decision on the `opportunity-canvas`, including the chosen pattern.
- The intended audience, data sources, connectors and actions, as far as they are known.
- The organisation's own risk appetite, data classification scheme and any regulatory obligations.

Where an input is unknown, rate that factor at the higher plausible level and mark it "to confirm". Classification can
come down when facts are confirmed; it must never start low on an assumption.

## Decision framework

Rate each factor from 0 to 4. The tier is the highest single rating, never an average.

| Rating | Impact if wrong | Reach | Data sensitivity | Autonomy |
|---|---|---|---|---|
| 0 | Personal inconvenience, caught by the user | One person | The user's own or public content | Drafts for a person who verifies |
| 1 | Team rework | A named team or group | General internal content | Shared prompts or answers people reuse |
| 2 | Departmental process disrupted | A department or the whole workforce | Confidential business content | Triggers workflow steps with human approval |
| 3 | Material internal decision, financial or operational harm | Business-critical process | Personal data at scale, special category or regulated data | Acts in systems with sampled oversight |
| 4 | Legal, safety, rights or significant customer harm | Customers, partners or the public | Sensitive data used to make decisions about individuals | Acts or communicates externally without per-action review |

Anything shared beyond its creator is at least tier 1. The minimum posture then follows from the tier.

| Tier | Minimum governance posture | Gates that apply |
|---|---|---|
| 0 Individual productivity | Approved-use guidance, data-handling awareness, human verification | None beyond acceptable use |
| 1 Team or shared | Named owner, defined audience, approved sources, basic test evidence | CoE register entry; no reviewer gate |
| 2 Organisational solution | Business and knowledge owners, security review, evaluation, release and support plan | `security-privacy` (blocking), `evaluation-quality`, `design-authority` |
| 3 Business-critical | Tier 2 plus formal architecture, privacy assessment, responsible AI review, monitoring and continuity | Tier 2 gates plus `responsible-ai` (blocking) |
| 4 External or high-impact | Full assurance, human oversight, escalation, incident response, executive risk acceptance | All gates, plus written executive risk acceptance |

These tiers are a proposed CopilotForge convention; validate them against the organisation's own policy and regulation.

## Practitioner approach

Classify the solution as it will actually be used, not as it is in the pilot. A test agent used by three people may
be destined for the whole workforce; rate the intended reach and plan the controls now, so the gate does not arrive as
a surprise a week before launch.

Rate each factor separately and write one sentence of evidence beside each rating. "Reach 2: published to all staff
through the intranet" is reviewable; "Reach: medium" is not. Take the highest rating as the tier. Averaging hides the
factor that matters: a tool with tiny reach that makes unreviewed decisions about individuals is still high risk.

Pay most attention to autonomy and to data. Where a solution only drafts and a person checks, the person is the
control; ask whether they are realistically able to spot a wrong answer. Where it acts, sends or updates records, the
controls must sit in the design. For data, check what the solution can reach, not only what it is meant to use;
agents grounded on broad sites inherit every oversharing problem in them. Use the source records on data protection
and on the platform's privacy and zoned governance approach to inform the rating, and leave legal interpretation to the
data protection officer.

Read across from the tier to the minimum posture and gates, and list the specific evidence each gate will expect. For
tier 2 and above, open the `ai-risk-assessment` record for the security and privacy review so the reviewers start
from the classification rather than repeating it. Where the posture cannot be met with current capability, such as no
one able to run a responsible AI review, record that the initiative cannot proceed at this tier until it can, or
redesign it to a lower tier by reducing reach, data or autonomy.

Redesign is often the best outcome. Keeping a person in the loop, narrowing the audience or removing access to a
sensitive library can drop a solution a full tier and make it deliverable now. Record the redesign decision and its
reasoning so the lower tier is not later mistaken for an oversight.

Set re-classification triggers on the record: a wider audience, new data or connectors, new actions, external exposure,
a change of owner, or an incident. Any trigger reopens the classification before the change goes live. A tier may be
raised by any reviewer; it may be lowered only by the risk owner with a written rationale.

## Outputs

- A risk tier record on the `opportunity-canvas` template: factor ratings with evidence, tier, minimum governance posture, gates required, redesign options considered, re-classification triggers and who classified it.
- For tier 2 and above, an opened `ai-risk-assessment` record that carries the tier and factor ratings into the security and privacy review.
- A list of gate evidence the delivery team must produce, by gate.

## Microsoft platform considerations

Platform zoning should mirror the tiers: personal and team zones for tiers 0 and 1, governed environments for tier 2
and above, with sharing, connector and data policies set to match. The controls available differ by product and
change over time, so check the current source records on zoned governance and privacy before relying on a specific
control, and cite what was used.

## Adoption considerations

Publish the tiers with simple examples so people can self-classify everyday use and see that tier 0 and 1 work is
encouraged, not obstructed. Proportion is what keeps people inside the governed route.

## Knowledge considerations

Grounding knowledge affects every factor: its sensitivity sets data rating, its accuracy affects impact if wrong. For
tier 2 and above, name the knowledge owner on the record, and treat unowned knowledge as a reason to hold the tier
rather than proceed.

## Security and privacy considerations

The data sensitivity and reach ratings decide when the `security-privacy` gate applies. Where personal data is
involved, record whether a data protection impact assessment may be needed and refer the question to the data
protection officer; this skill does not decide it.

## Responsible AI considerations

Uses that inform decisions about people, money, safety or rights rate at least 3 for impact. Tier 3 and 4 require
review by the `responsible-ai` department (planned); until it exists, the CoE convenes the data protection officer,
the business owner and an independent senior reviewer. Some uses should not be built; record that conclusion plainly.

## Evaluation requirements

State the evaluation evidence the tier demands. Tier 1 needs basic test evidence from the owner; tier 2 and above need
an agreed evaluation set and acceptance threshold reviewed through the `evaluation-quality` gate (planned); tiers 3 and
4 also need ongoing monitoring after launch.

## Value measures

Track classification health rather than individuals: share of live solutions with a current tier record, number of
re-classifications triggered by scope change, and time from request to classification. The CoE lead owns these
measures and reports them by unit.

## Scale notes

### Starter

The person leading AI classifies with the business owner on one page. Most work is tier 0 or 1; anything at tier 2 or
above usually needs partner or specialist support for the reviews.

### Scale

Classification is a standard intake step with the CoE checking every tier 2 and above record. Security and privacy
review blocks release from tier 2, and a solution register holds every tier.

### Enterprise

Spokes classify tiers 0 to 2 against the shared table; the hub confirms tier 3 and 4. Gate evidence is auditable, and
tier 4 requires recorded executive risk acceptance.

## Hand-offs

- To `security-privacy:data-exposure-review`, `security-privacy:privacy-assessment` and `security-privacy:connector-review` as the tier requires.
- To `opportunity-management:opportunity-prioritisation` with the tier and the cost of its controls.
- To `m365-agents:agent-release-readiness` so release checks match the tier.
- To `ai-centre-of-excellence:coe-governance-model` when the tiers or their postures need changing.

## Reviewer gates

The tier decides the gates. From tier 2, `security-privacy` blocks release until data exposure and access are reviewed,
`evaluation-quality` (planned) checks the evaluation evidence, and `design-authority` (planned) challenges architecture
and platform choice. From tier 3, `responsible-ai` (planned) blocks release until oversight, fairness and transparency
are reviewed. Disagreement about the tier itself escalates to the accountable executive.

## Failure modes

- A pilot is classified at its test audience, then published organisation-wide without re-classification.
- Factors are averaged, so a small but autonomous solution acting on personal data is rated low.
- Everything is rated tier 3 to be safe, reviews back up, and teams move to ungoverned tools.
- The tier record and the security review are kept separately and drift apart.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Lower a tier to avoid a review, or without a written rationale from the risk owner.
- Average the factor ratings instead of taking the highest.
- Treat the classification as permanent when audience, data, connectors or autonomy change.
- Present the tiers as a legal or regulatory determination; they are a proposed convention to validate locally.

---
name: coe-governance-model
description: Writes a proportionate AI governance framework and acceptable-use starter - five governance areas, progressive risk tiers 0 to 4 with minimum controls, an agent portfolio register with business, knowledge and technical owners, and reviewer gates - so low-risk experimentation is not blocked. Use when there is no approved AI policy, when departments build agents with no register or owner, or when governance is so heavy people work around it.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Mobilise, Assure, Launch, Improve
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-studio, power-platform, purview, entra
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, responsible-ai, evaluation-quality, design-authority
  sources: ms-copilot-studio-zoned-governance, ms-copilot-studio-security-governance, ms-managed-environments, ms-coe-starter-kit, ms-copilot-privacy, ms-responsible-ai, nist-ai-rmf, ico-ai-data-protection, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# CoE governance model

## Purpose

Governance should make safe use the easy path. This skill writes an AI governance framework and an acceptable-use
starter built on progressive risk tiers: light guidance for individual productivity, rising controls as reach, data
sensitivity, autonomy and impact grow. It sets up a solution register, ownership and lifecycle controls, and the points
where reviewer-class departments can block release. Governance fails in two directions: none at all while staff build
agents and use unsanctioned tools, or a single heavy process applied to everything, which drives experimentation
underground.

## When to use

- There is no approved AI acceptable-use policy, or a draft has stalled.
- Departments are building agents or automations with no register, owner or review.
- Unsanctioned AI use is suspected and staff need a safe, approved alternative.
- Existing governance treats every AI idea the same, so low-risk work waits weeks.
- An auditor, regulator or client contract asks how AI is controlled.

## When not to use

- Classifying the risk tier of one specific solution - use `opportunity-management:risk-classification`.
- Reviewing data exposure for a specific solution - use `security-privacy:data-exposure-review`.
- Reviewing connectors and actions for a specific agent - use `security-privacy:connector-review`.
- Privacy assessment for a specific solution - use `security-privacy:privacy-assessment`.
- Environment, connector and maker policy configuration in depth - the `platform-governance` department (planned).
- Readiness of a single agent for release - use `m365-agents:agent-release-readiness`.

## Questions to ask first

1. What AI tools are approved today, what are people actually using, and is unsanctioned use suspected?
2. How many agents, automations and pilots exist, who built them, and who owns them?
3. What do existing information security, data protection and acceptable-use policies already say that AI governance can reuse?
4. What regulatory or contractual expectations apply, and does a regulator expect formal, auditable assurance?
5. Who will hold each reviewer gate, and who can accept residual risk at tier 3 and tier 4?

## Required inputs

- The edition and assurance overlay from `organisation-tailoring:edition-and-archetype`.
- Existing policies (information security, data protection, records, acceptable use) and the approved tools list.
- An inventory of current agents, automations and pilots, even if partial.
- The CoE charter's decision rights and the RACI's gate holders.

If the inventory is missing, the first control is to build it. If no approved policy exists, publish the acceptable-use
starter first and the full framework second. Mark gate holders `[To confirm]` until named by role; never assume a
regulatory requirement, and send legal questions to the organisation's legal adviser or data protection officer.

## Decision framework

Cover five governance areas, each with a named owning role, so nothing falls between functions.

| Area | Question it answers | Typical owning role |
|---|---|---|
| Security | Can only the right people and systems reach the solution and what it reaches? | Information security |
| Privacy | Is personal data used lawfully, minimally and transparently? | Data protection officer |
| Data ownership | Does every knowledge source and data set have a business owner who keeps it current? | Business and knowledge owners |
| Compliance | Does the solution meet policy, contract and regulatory obligations? | Compliance or legal adviser |
| Human accountability | Which named role answers for each outcome the solution informs? | The business owner |

The accountability principle sits above all five: AI assists decision making; humans remain accountable for outcomes.

Classify by the highest applicable factor (reach, data sensitivity, autonomy, impact on people, external exposure).
Each tier inherits the controls below it.

| Tier | Typical use | Minimum controls | Reviewer gates | Release decided by |
|---|---|---|---|---|
| 0 Individual productivity | A person uses approved Copilot features on their own work | Acceptable-use guidance, approved tools, human verification of outputs, no restricted data in unapproved tools | None | Not applicable |
| 1 Team or shared | Shared prompts, a Cowork task design or an agent for one team | Named owner, defined audience, approved knowledge sources, basic test evidence, register entry | None by default | Owner, recorded in register |
| 2 Organisational solution | Agent or automation used across teams or with sensitive data | Business and knowledge owners, security and privacy review, evaluation against acceptance threshold, release and support plan | `security-privacy`, `evaluation-quality`, `design-authority` | CoE release decision |
| 3 Business-critical | Solution a core process depends on, or informing decisions about people or money | Formal architecture, privacy impact assessment, responsible AI review, monitoring, continuity plan | Tier 2 gates plus `responsible-ai` | Steering, with accountable executive |
| 4 External or high-impact | Customer-facing, public or high-impact autonomy | Full assurance, human oversight, escalation, incident response, executive risk acceptance | All gates, formal evidence | Executive risk acceptance in writing |

Proportionality tests: a tier 0 request should need no approval; a tier 1 registration should take minutes; a tier 2
decision should take days, not months. If not, the controls are mis-sized.

## Practitioner approach

Write the acceptable-use starter first, because it protects people now. Open it with the accountability principle in
plain words: AI helps people decide, and people stay accountable for what they decide and send. Keep it to two pages in plain language: which
tools are approved and for what, what data must not go into unapproved tools, that people check outputs before relying on
them, that AI-generated content is labelled where it matters, how to share a useful prompt, and where to take a new idea.
Offer the approved alternative alongside each prohibition; banning tools without one simply moves use out of sight.

Then build the tier model above. Adapt the factors to the organisation, but keep five tiers and the inheritance rule so
that the CoE governs once and repeats everywhere. Classify five or six real examples from the inventory with the
business owners present; this calibrates the tiers and shows people the model is fair.

Set up the solution register next, run as an agent portfolio. Every tier 1 and above solution has an entry: name,
category (Microsoft 365 agent, Copilot Studio agent, automation or integration), purpose, business owner, knowledge
owner, technical owner, platform, audience, knowledge sources, data sensitivity, tier, reviews completed, release date,
review date, measured value against baseline and status. Three named owners matter: the business owner answers for the
outcome, the knowledge owner for the content, the technical owner for the build and its support. The register is the backbone of lifecycle control: it drives periodic review, re-classification when audience or
data changes, and retirement of unused or ownerless solutions. Make registration the condition for sharing beyond the
builder.

Map the five governance areas onto the tiers so each area has a minimum control at each tier and an owning role, and
the CoE governs once and repeats everywhere. Treat knowledge as governed content too: every document an agent relies on
carries an owner, a review date, version control and a classification, recorded in the knowledge asset register.

Define ownership and lifecycle controls: an owner leaving triggers reassignment within a set period or suspension;
every solution has a review date proportionate to its tier; solutions with no use or no owner for an agreed period are
retired after notice.

Place reviewer gates. From tier 2, `security-privacy` review is blocking and not skippable. `evaluation-quality` and
`design-authority` gates apply from tier 2 and `responsible-ai` from tier 3; until those departments are built, the CoE
lead holds the gate, records the evidence and names the planned department as the future owner. A blocking finding is
not traded off against a date; disagreement goes to the accountable executive and is recorded.

Where the assurance overlay is formal, add auditable evidence at every gate. Map the framework to recognised standards
such as the NIST AI RMF or ISO/IEC 42001 only as a cross-reference, and only where the organisation needs it.

Close with what governance cannot do: it does not make an unsuitable use acceptable, and it does not replace judgement.

## Outputs

- An AI governance framework and acceptable-use starter on the `ai-governance-starter` template: principles, approved tools, data rules, tier model with minimum controls, reviewer gates, release authority, register fields, ownership and lifecycle rules, exception and escalation route.
- The five governance areas with owning roles and the accountability statement, in the same template.
- A populated agent portfolio register seeded from the current inventory, each entry with category, the three owners, platform, provisional tier, review date and a measured-value field.
- A short list of current solutions needing action (no owner, wrong tier, missing review).

## Microsoft platform considerations

Map tiers to platform controls so the framework is enforced, not only written. Copilot Studio and Power Platform
support environment zoning, data policies and Managed Environments controls; Microsoft Purview and Entra provide
labelling, data loss prevention and access controls that affect what Copilot and agents can reach. Which controls exist,
their licensing and their behaviour change often, so check `references/sources.md` and confirm with the tenant
administrator before relying on one.

## Adoption considerations

Publish the acceptable-use starter as a positive guide, with examples, through Champions and managers. Make tier 0 and
tier 1 frictionless, so the register is seen as a service, not a barrier.

## Knowledge considerations

From tier 1, every solution names its knowledge sources and their owners. Weak or unowned knowledge raises the tier or
blocks release until fixed. The `knowledge-management` department (planned) will own the standards.

## Security and privacy considerations

Copilot and agents respect existing permissions, so oversharing in the estate becomes oversharing in answers. Make
permission hygiene a precondition for wider rollout and for tier 2 agents. Confirm data protection impact assessment
triggers with the data protection officer.

## Responsible AI considerations

List uses the organisation will not build at all. From tier 3, require a responsible AI review covering human oversight,
fairness, transparency to affected people and escalation. Human accountability for outcomes stays with a named role.

## Evaluation requirements

Set evaluation evidence by tier: tier 1 needs basic test questions with expected answers; tier 2 needs an evaluation set
with an acceptance threshold agreed by the business owner; tier 3 and 4 add ongoing monitoring and periodic re-evaluation.

## Value measures

Measure governance by proportion and coverage: register coverage of known solutions, share of shared solutions with a
business, knowledge and technical owner, share of portfolio entries with measured value recorded, median decision time by tier, and blocking findings resolved before release. The CoE lead owns them, reported
through `ai-centre-of-excellence:coe-kpi-framework`.

## Scale notes

### Starter

An acceptable-use starter, approved tools, a simple register for anything shared, and reviewer gates only from tier 2,
with partner support for any tier 2 work. Most activity stays at tiers 0 and 1.

### Scale

The full tier model, a maintained register, reviewer gates from tier 2 with `security-privacy` blocking, and periodic
review of registered solutions.

### Enterprise

Federated policy with hub standards and spoke operation, formal reviewer boards, auditable evidence at every gate, and
executive risk acceptance for tier 4.

## Hand-offs

- To `opportunity-management:risk-classification` for classifying individual solutions.
- To `security-privacy:data-exposure-review` and `security-privacy:privacy-assessment` at tier 2 and above.
- To `m365-agents:agent-release-readiness` for release of individual agents.
- To the `platform-governance` department (planned) for environment and connector configuration.

## Reviewer gates

The framework itself should be reviewed by `security-privacy` before approval. It defines gates for solutions:
`security-privacy` blocking from tier 2, `evaluation-quality` and `design-authority` from tier 2, and `responsible-ai`
from tier 3. Planned reviewer departments are held by the CoE lead until built.

## Failure modes

- One heavyweight process for every request, so experimentation moves to unsanctioned tools.
- Agents are registered at launch but never reviewed, and their owners and knowledge drift away.
- A prohibition without an approved alternative, so shadow AI grows.
- Tier classification is done by the builder alone and always comes out low.
- The register records a technical owner but no business or knowledge owner, so nobody answers for outcomes or content.
- Privacy and security are covered but data ownership and human accountability are left implicit, and nobody owns a wrong answer.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Apply tier 3 or 4 controls to individual productivity use.
- Allow a tier 2 or higher release while a blocking `security-privacy` finding is open.
- Assert that a platform control exists or is licensed without checking the current source.
- Give legal or regulatory conclusions; refer them to the legal adviser or data protection officer.
- Imply that an AI system, rather than a named human role, is accountable for an outcome.

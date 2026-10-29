---
name: foundry-solution-assessment
description: Tests whether a need that has reached the engineered-solution rung really justifies a Microsoft Foundry build, and whether the organisation can own, fund and operate it, recording the case and its preconditions on a solution design. Use when suitability points to Foundry, when a team proposes pro-code AI before trying configured agents, or when a sponsor asks what a Foundry build commits the organisation to.
license: CC-BY-4.0
metadata:
  department: ai-foundry
  lifecycle: Envision, Mobilise, Deliver
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, copilot-studio, m365-agents
  edition-support: starter, scale, enterprise
  reviewers: design-authority, security-privacy, responsible-ai
  sources: ms-foundry-models, ms-agents-compare, ms-agents-extensibility, ms-responsible-ai, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Foundry solution assessment

## Purpose

A Microsoft Foundry solution is a piece of software the organisation will own for years: models to keep current, an
Azure footprint to secure, evaluations to rerun and a team to support it. This skill confirms that the need genuinely
requires that level of engineering, that a configured agent or ordinary automation cannot meet it, and that the
organisation has the people, funding and operating model to run what it builds. Assessments go wrong when Foundry is
chosen for prestige or flexibility, when the comparison with Copilot Studio is never made honestly, or when the build
is approved without anyone budgeting for the second year.

## When to use

- `opportunity-management:ai-suitability` has landed on the Foundry rung and the case needs testing before design starts.
- A technical team proposes a pro-code AI build and nobody has tried a configured agent first.
- A sponsor wants to know what a Foundry solution commits the organisation to in skills, cost and operation.
- An existing Copilot Studio agent has hit a limit and the team wants to move it, or part of it, to Foundry.
- A partner has proposed a custom AI solution and the organisation needs an independent view before contracting.

## When not to use

- Deciding whether AI is appropriate at all, or which broad pattern fits - use `opportunity-management:ai-suitability`.
- Choosing between Microsoft platforms across the whole estate, not only Foundry - use `ai-architecture:platform-selection`.
- Deciding whether a need warrants a Microsoft 365 agent and which kind - use `m365-agents:agent-opportunity-assessment`.
- Choosing the model once Foundry is confirmed - use `ai-foundry:model-selection`.
- Formal challenge of platform fit at a design gate - that is the reviewer skill `design-authority:platform-fit-review`.

## Questions to ask first

1. Which specific requirement cannot be met by a Microsoft 365 agent, a Copilot Studio agent or deterministic automation, and has someone shown that rather than assumed it?
2. Who will own the solution after launch: a named product owner role, an engineering team with Azure and AI skills, and an operations route?
3. What is the risk tier from `opportunity-management:risk-classification`, and does the solution act, decide or face customers?
4. Does the organisation already have an Azure landing zone, subscription governance and identity model that a Foundry project can sit inside?
5. Is there a value hypothesis with a baseline that can carry the build cost and at least a year of running cost?

## Required inputs

- The framed problem and suitability record, normally on the `opportunity-canvas` template.
- The confirmed or proposed risk tier and the reviewer gates it brings.
- An inventory of what the organisation already licenses and has approved across Copilot, Copilot Studio and Azure.
- The skills and capacity of the team that would build and run the solution, by role.
- The value hypothesis and baseline, even if provisional.

Where an input is missing, mark it `[To confirm: ...]` in the solution design and lower the confidence of the
recommendation. Never assume an Azure subscription, a quota, a licence or a team that has not been confirmed.

## Decision framework

Foundry is justified when at least one capability driver applies and every ownership condition is met. A driver with
no owner is a deferral, not an approval.

| Capability driver | Typical evidence |
|---|---|
| Model choice beyond what configured agents expose | A task needs a specialist, smaller, multimodal or third-party model, or fine-tuning |
| Retrieval engineering | Grounding needs custom chunking, hybrid search, metadata filters or security trimming that configured knowledge cannot give |
| Complex orchestration | Multi-step or multi-agent workflows with code-level control of state, retries and checkpoints |
| Embedding AI in a product or process | The AI runs inside a line-of-business application, API or batch process rather than a chat surface |
| Production-grade evaluation and observability | The risk tier demands repeatable evaluation, tracing and safety controls that must be engineered |

| Ownership condition | Not met when |
|---|---|
| Product owner and engineering team named | Delivery depends on one person or on a partner with no hand-over |
| Azure foundation in place | No landing zone, no subscription owner, no network or identity standard |
| Running cost funded | Only the build is funded |
| Operations route agreed | No support model, monitoring owner or incident route |
| Reviewer capacity available | Required gates cannot be staffed at the solution's risk tier |

Outcomes: proceed, proceed with preconditions, use a lower rung (often Copilot Studio with a Foundry component), or
stop.

## Practitioner approach

Start from the requirement that supposedly forces Foundry and try to break it. Ask the team to show, with a short spike
or a documented product limit from the current source records, why a Copilot Studio agent or a Microsoft 365 agent
cannot meet it. Many proposals collapse at this point: the "custom retrieval" turns out to be a messy SharePoint
library that needs cleaning, and the "complex orchestration" is a three-step flow. Record what was tried and why it
fell short, because the design authority will ask.

Consider hybrid answers before a full build. A Copilot Studio agent can front a conversation while a Foundry model or
agent handles one hard step; an automation can do the acting while a Foundry component does the interpreting. Hybrids
keep most of the solution inside governed low-code tooling and limit pro-code ownership to the part that needs it.

Then test ownership as hard as capability. Name the product owner role, the engineering team and the operations route.
Check that the team has worked with Azure identity, networking and deployment before, or that a partner engagement
includes a real hand-over. Ask finance whether running cost is funded beyond the first year; model consumption,
search, storage and monitoring all continue after launch. Cost estimation itself belongs to
`ai-foundry:foundry-cost-management`, but the assessment must confirm someone will pay.

Check the platform foundation. A Foundry project should sit inside the organisation's Azure governance, not in a
developer's personal subscription. If there is no landing zone or identity standard, the first deliverable is that
foundation, and the solution timeline moves accordingly.

Confirm the risk tier and the gates it brings. A customer-facing or decision-informing Foundry solution brings
`responsible-ai`, `evaluation-quality` and `security-privacy` gates that take real time; plan for them now rather
than discovering them at release.

Finally, write the assessment section of the `foundry-solution-design` template: the drivers that apply, the lower
rungs tested and why they fell short, the ownership conditions and their status, the preconditions and the decision.
State what this assessment cannot determine, such as whether a particular model will reach the quality bar, which only
evaluation can show.

## Outputs

- The assessment section of a Foundry solution design on the `foundry-solution-design` template: drivers, lower rungs tested, ownership conditions, preconditions, decision and decision owner.
- A plain-language summary for the sponsor of what the build commits the organisation to.
- Where Foundry is not justified, a referral to the lower rung or hybrid that will meet the need.

## Microsoft platform considerations

Microsoft Foundry, Copilot Studio and Microsoft 365 agents overlap more each release, and the boundary between them
moves. Configured agents can increasingly call Foundry models and agents, and Foundry agents can be surfaced in
Microsoft 365, so the choice is often about where each part lives rather than one platform for everything. Check the
current comparison and extensibility sources before asserting what a configured agent cannot do. Model availability,
regions and licensing are volatile; confirm them in `references/sources.md` and route licensing questions to the
Microsoft licensing guide or a licensing partner.

## Adoption considerations

Foundry solutions are often invisible to users because they sit inside other applications. Plan how users will learn
what the AI does and how to challenge it, and involve the `copilot-adoption` department when a chat surface is part of
the solution.

## Knowledge considerations

Most Foundry solutions ground on organisational content or data. Name the sources, owners and condition now; poor
knowledge is a precondition to fix with `knowledge-management:knowledge-readiness-assessment`, not a reason to build
more sophisticated retrieval.

## Security and privacy considerations

A Foundry build introduces Azure resources, service identities, keys and network paths that configured agents hide.
Record data sensitivity, where data will be processed and who can reach the endpoints, and bring the
`security-privacy` gate forward for tier 2 and above. Data residency and processing questions go to the source records
and, for legal effect, to the DPO.

## Responsible AI considerations

Pro-code flexibility makes it easy to build things that should not be built. Check whether the solution informs
decisions about people, money, safety or rights, and whether it could fall into a prohibited or restricted use; route
those cases to `responsible-ai:prohibited-use-review` before design.

## Evaluation requirements

The assessment names the evidence that will show the solution is good enough: the task, a representative test set
owner, and an acceptance threshold the business owner agrees before results are seen. Detailed design belongs to
`ai-foundry:model-evaluation` and `evaluation-quality:ai-evaluation-strategy`.

## Value measures

Record the baseline and measure from the value hypothesis and the total cost the build must justify, owned by the
business owner. If the hypothesis only pays back at a volume the organisation does not have, say so.

## Scale notes

### Starter

Expect most needs to end at a lower rung. Where Foundry is justified, plan for a partner-led build with a contracted
hand-over and a small internal owner group, and keep the first solution narrow.

### Scale

Run the assessment as a standard step for every pro-code AI proposal, with a shared record of precedents so teams see
why earlier proposals were approved or redirected.

### Enterprise

Federate first-pass assessment to platform teams in each business area, with the design authority reviewing tier 2
and above, and track Foundry solutions in the AI solution inventory.

## Hand-offs

- To `ai-foundry:model-selection` once Foundry is confirmed.
- To `ai-foundry:foundry-agent-architecture` or `ai-foundry:agentic-workflow-design` for the solution shape.
- To `ai-foundry:foundry-cost-management` for the cost estimate and budget.
- To `ai-architecture:platform-selection` when the question widens beyond Foundry.
- To `platform-governance:ai-solution-inventory` to register the approved solution.

## Reviewer gates

From risk tier 2, `design-authority` tests the assessment for unnecessary engineering and platform fit,
`security-privacy` reviews the data and Azure exposure, and `responsible-ai` checks the use is acceptable. Any of them
can stop the build at this point; findings are recorded on the solution design.

## Failure modes

- The lower rungs are dismissed in a sentence, and a Copilot Studio agent would have met the need at a fraction of the effort.
- The build is approved without running cost funded, and the solution is switched off or left unmaintained in year two.
- A partner builds the solution and leaves, and nobody internal can change a prompt or rotate a key.
- The project is created outside the organisation's Azure governance, and security discovers it at release.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Approve a Foundry build because the team prefers code or the platform is newer.
- Approve a build whose running cost, owner or support route is unconfirmed.
- Assert what Copilot Studio or a Microsoft 365 agent cannot do without checking the current source.
- State licensing or data-residency conclusions; route them to the licensing guide, a licensing partner or the DPO.

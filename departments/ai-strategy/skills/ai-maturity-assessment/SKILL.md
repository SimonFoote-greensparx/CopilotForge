---
name: ai-maturity-assessment
description: Diagnoses an organisation's current AI maturity across strategy, people and adoption, knowledge, governance, platform and delivery capability, and value measurement, using observed evidence rather than self-scored opinion, and maps the result to a CopilotForge archetype. Use when a programme is starting, when leaders disagree about how ready they are, or when a strategy refresh needs an honest baseline.
license: CC-BY-4.0
metadata:
  department: ai-strategy
  lifecycle: Discover, Improve
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-overview, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI maturity assessment

## Purpose

This skill gives leaders an honest, evidence-based picture of where the organisation stands with AI today, so the
strategy and roadmap start from reality rather than ambition. It examines six dimensions and places the organisation
on the CopilotForge archetype path from explorer to ai-enterprise. Assessments usually go wrong in two ways: they become
a survey of opinions in which every team rates itself above average, or they reward technology deployed while ignoring
the ownership, knowledge and governance that make it safe and valuable.

## When to use

- An AI programme or transformation is starting and needs a baseline before outcomes and a roadmap are set.
- Leaders disagree about readiness, for example the board believes AI is embedded while teams report little use.
- A strategy refresh or annual review needs to show movement since the last assessment.
- A new business unit joins a federated programme and needs placing on the same scale as the others.

## When not to use

- Capturing the organisation profile and applying the tailoring rules to choose an edition - use `organisation-tailoring:ai-profile-intake` and `organisation-tailoring:edition-and-archetype`.
- Judging whether a specific audience is ready for a Copilot launch - use `copilot-adoption:adoption-readiness`.
- Measuring how the CoE itself is performing - use `ai-centre-of-excellence:coe-kpi-framework`.
- Assessing whether a particular body of knowledge is fit for grounding - use `m365-agents:knowledge-source-readiness`, or `knowledge-management:knowledge-readiness-assessment` for estate-wide work.

## Questions to ask first

1. Who is sponsoring the assessment, and what decision will it inform: a first strategy, a funding case, a refresh or a federation baseline?
2. What is in scope: the whole organisation, one business unit, or a comparison across several?
3. Who can give access to evidence, such as policies, team-level usage reports, solution registers, knowledge ownership records and past business cases?
4. Which roles should be interviewed so the picture includes executives, managers, frontline staff, IT, security and data protection, not only enthusiasts?
5. Has an earlier assessment been done, and on what scale, so movement can be compared fairly?

## Required inputs

- A named sponsor and the decision the assessment informs.
- The organisation profile from `organisation-tailoring:ai-profile-intake`, where one exists.
- Access to documentary evidence (policies, registers, reports) and to interviewees across the roles listed above.
- Team-level or role-level adoption data where it is available. Never individual usage data.

Where evidence is missing, score the dimension on what can be observed and mark the gap "to confirm" in the
assessment. An absence of evidence is itself a finding; never fill it with an assumed score.

## Decision framework

Score each dimension at the highest archetype stage whose evidence is fully met. A claim counts only when it is observed
in an artefact or corroborated by at least two independent roles.

| Dimension | Explorer | Adopter | Builder | Scaler | AI enterprise |
|---|---|---|---|---|---|
| Strategy and sponsorship | Interest without stated outcomes | Sponsor named, adoption goals set | Outcomes and principles agreed | Roadmap funded across units | AI outcomes built into business plans and reviewed by the executive |
| People and adoption | Ad hoc personal use | Deployed, use inconsistent | Role-based scenarios, Champions active | Capability evidenced across units | Capability built into roles and recruitment |
| Knowledge | Unowned, scattered | Some sites owned | Owners for grounding sources | Review cycles running | Knowledge managed as infrastructure |
| Governance and risk | No approved-use guidance | Acceptable-use guidance exists | Risk-tiered intake, an owner for anything shared | Reviewer gates applied consistently | Federated assurance with executive risk acceptance |
| Platform and delivery | Default settings | Tenant readiness addressed | Agents built with owners and testing | Environments, lifecycle and reuse managed | Custom AI engineered and operated in production |
| Value measurement | None | Usage counts only | Baselines for some initiatives | Value hypotheses tracked to review | Benefits realised and reported to the board |

The overall archetype is capped at the lowest stage reached by governance, knowledge or value measurement, even if
platform or adoption scores higher. This mirrors the tailoring rule that an organisation is never placed beyond a
foundation it has skipped. Report the stronger dimensions as emerging signals, not as the headline.

## Practitioner approach

Agree the decision first. An assessment commissioned to support a funding case reads differently from one that
baselines federation, and the sponsor needs to know before fieldwork that the findings will be evidence-based and may
be uncomfortable. Agree also that individual people are not being assessed; usage data is read at team or role level
only, above an agreed minimum group size.

Collect documents before interviews. Policies, the solution or agent register, adoption reports, knowledge site
ownership, past business cases and steering minutes tell you what the organisation has actually done. Then interview
across roles and levels, asking for examples rather than ratings: "Show me the last time an AI idea was turned down,
and who decided" reveals far more about governance than "How mature is your governance?". Include sceptics and
frontline staff, because enthusiasts describe the organisation they want.

Grade each piece of evidence as observed, corroborated or asserted. Only the first two move a score. Where the senior
view and the frontline view differ, record both and treat the gap as a finding in its own right; it often predicts
adoption problems better than any score.

Score each dimension against the table, then apply the foundation rule. A common pattern is strong platform and
adoption scores sitting on weak knowledge and governance: many agents, no owners, no approved-use guidance. That
organisation is an adopter with builder signals, not a builder, and saying so plainly is the most useful thing the
assessment does. Check product-related findings, such as whether a capability is available in the tenant, against the
current source records rather than memory.

Write the findings as a short narrative per dimension: what was seen, what it means, and the two or three moves that
would advance it. Avoid generic recommendations such as "improve governance"; name the artefact or decision that is
missing. Close with the archetype, the emerging signals, the confidence level, and the evidence gaps that limit
confidence. Be explicit about what the assessment could not see, such as business units that declined interviews.

Play the result back to the sponsor before wider circulation, and to a group of interviewees if possible. Agreement
on the starting point is what lets `ai-strategy:strategic-outcomes` and `ai-strategy:ai-roadmap` proceed without
relitigating it. Set the date for reassessment, normally twelve months, or sooner after a major change.

## Outputs

- An AI maturity assessment on the `ai-maturity-assessment` template: scope, evidence log, dimension scores with evidence grades, overall archetype, emerging signals, confidence and gaps.
- A one-page summary for the sponsor stating the archetype, the binding constraints and the priority moves.
- A list of evidence gaps marked "to confirm", with who could close each one.

## Microsoft platform considerations

Platform readiness is one dimension of six, never the headline. Look at what the organisation has enabled, how
environments and data policies are set up, and whether agent building is governed, but do not score the organisation on
how many products it has bought. Product names, availability and admin capabilities change often; confirm any
platform finding against the source records in `references/sources.md` before it appears in the assessment.

## Adoption considerations

The assessment is itself a change intervention: people who are interviewed expect to hear back. Share the summary with
participants, explain how it will be used, and make clear it judges the organisation, not them. Adoption evidence is
reported at team or role level only.

## Knowledge considerations

Knowledge readiness is often the binding constraint for builder and scaler organisations. Record which knowledge
domains have owners, review cycles and classification, and which are in active use for grounding without them. Detailed
remediation belongs with `knowledge-management:knowledge-readiness-assessment`.

## Security and privacy considerations

Not applicable as a gate, because the assessment designs nothing. It does record whether approved-use guidance, data
classification and sharing controls exist, and it passes any known shadow AI use to the security lead and to
`opportunity-management:risk-classification`.

## Responsible AI considerations

Record whether the organisation has stated AI principles and whether any current use informs decisions about people,
money, safety or rights without human oversight. Such a finding goes to the sponsor immediately rather than waiting
for the final report.

## Evaluation requirements

Not applicable in the solution-testing sense. The assessment's own quality check is that every score cites at least one
observed or corroborated piece of evidence, and that a second assessor could reach the same score from the evidence log.

## Value measures

The assessment is the baseline for the transformation's capability measures, and its owner is the sponsor. Movement is
measured by reassessment on the same scale, dimension by dimension, at the agreed interval. It is never a measure of any
individual's performance.

## Scale notes

### Starter

Run it in a few days: a document review, five to eight interviews across roles and a one-page result. Many starter
organisations are explorers or adopters, and that is a useful, honest place to begin.

### Scale

Interview across every major function, add team-level adoption data, and use two assessors to moderate scores. Repeat
annually on the same scale.

### Enterprise

Assess each business unit separately with a shared method, then roll up to an enterprise view that shows variation
between units. The hub moderates scores so units are comparable, and the differences shape federated support.

## Hand-offs

- To `ai-strategy:strategic-outcomes` to set outcomes and principles from the baseline.
- To `ai-strategy:ai-roadmap` to sequence the moves that address the binding constraints.
- To `organisation-tailoring:edition-and-archetype` to confirm or challenge the archetype the tailoring rules produced.
- To `copilot-adoption:adoption-readiness` where adoption is the binding constraint.

## Reviewer gates

Not applicable. The assessment is diagnostic and makes no release decision; findings that reveal live risk are routed
to `opportunity-management:risk-classification` and the accountable owner rather than gated here.

## Failure modes

- Self-assessment scores are accepted at face value, so the organisation is placed two stages beyond its evidence.
- Platform deployment is mistaken for maturity, and weak ownership and knowledge go unreported.
- Interviews include only enthusiasts and the AI team, so the frontline experience is missing.
- The assessment is filed and never repeated, so nobody can show whether the programme moved anything.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Score a dimension on assertion alone, or invent evidence to complete the table.
- Assess, rank or name individual people, or use individual usage data.
- Place the organisation beyond a foundation it has skipped because its technology looks advanced.
- Present the archetypes as a Microsoft classification; they are proposed CopilotForge conventions.

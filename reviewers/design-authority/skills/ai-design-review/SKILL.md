---
name: ai-design-review
description: Runs the formal design authority gate for an AI solution - checking the design pack is complete, applying the necessity, platform fit, conformance and supportability lenses proportionately, and recording every finding as blocking or advisory with a fix and owner and a single verdict. Use when a tier 2 or higher solution finishes design and before build commits, when a partner's design needs independent review, or when a design changed materially.
license: CC-BY-4.0
metadata:
  department: design-authority
  lifecycle: Deliver, Assure
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 2, 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, power-platform, copilot-code, azure
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-agents-compare, ms-agents-extensibility, ms-copilot-studio-guidance, ms-foundry-models, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI design review

## Purpose

The design gate is the cheapest point to change an AI solution: the decisions are made but little has been built. This
reviewer skill runs that gate. It checks that the design pack is complete, applies the design authority's lenses -
necessity, platform fit, conformance and supportability - in proportion to the risk tier, and records every finding as
blocking or advisory with a specific fix and owner. Design reviews go wrong when they become presentations rather than
reviews of evidence, when every finding is treated as equally serious, and when a blocking issue is waved through to
protect a date.

## When to use

- A solution at risk tier 2 or above has finished design and is about to commit to build.
- A partner or supplier has delivered a design that the organisation must accept.
- A live solution's design has changed materially and needs a fresh gate.
- A pilot is about to become a supported service and was never formally reviewed.
- Programme stage gates require design authority sign-off.

## When not to use

- Challenging whether AI is needed at all, in depth - use `design-authority:ai-necessity-challenge`.
- Reviewing the platform choice in depth - use `design-authority:platform-fit-review`.
- Checking conformance to reference architectures and standards in depth - use `design-authority:architecture-conformance`.
- Reviewing ownership and support in depth - use `design-authority:supportability-review`.
- Running the release gate for an agent - use `m365-agents:agent-release-readiness`.
- Reviewing security, identity and data exposure - use `security-privacy:data-exposure-review` and `security-privacy:connector-review`.

## Questions to ask first

1. What is the solution's risk tier, and has it been confirmed since the design took shape?
2. Is the design pack complete enough to review, or does it need to go back before the review starts?
3. Which lenses does this tier and design need in depth, and which in summary?
4. Who is the accountable business owner, and who can accept residual risk if there is disagreement?

## Required inputs

- The design pack: solution or agent brief, suitability decision, risk classification, architecture decision records, non-functional requirements, identity map, interface catalogue, grounding design, placement in the topology, evaluation approach and support model.
- The reference architectures and standards in force.
- Findings already raised by `security-privacy` and other reviewers, if available.

A missing input is itself a finding. From tier 2, a missing identity map, grounding design or evaluation approach is
blocking until supplied; never infer the missing design from conversation.

## Decision framework

Apply each lens and classify every finding. From tier 2 a blocking finding stops the gate; below tier 2 the review is
advisory unless risk classification is wrong.

| Lens | Blocking when | Advisory when |
|---|---|---|
| Completeness | A core design artefact is missing or contradicts another | Minor gaps with an owner and date |
| Necessity | A simpler rung clearly meets the need and the design adds risk or cost without reason | A simpler option exists but the choice is reasoned |
| Platform fit | The platform cannot meet an identity, data, lifecycle or operability requirement | The platform fits but a cheaper option was not considered |
| Conformance | A mandatory control from the reference architecture or standards is absent without an approved deviation | A recommended practice is not followed |
| Non-functional | Quality, availability or cost requirements are absent or unverifiable at the tier | Targets are present but provisional |
| Supportability | No named operating owner or support route for a tier 2 or higher solution | Runbook or review calendar incomplete |

Verdicts: **approved**, **approved with advisory findings**, **not approved - blocking findings**, or **returned -
incomplete**. Disagreement with a blocking finding escalates to the accountable executive for written risk acceptance.

## Practitioner approach

Check completeness before scheduling the review. Ask for the design pack a few days ahead and read it. If core artefacts
are missing, return the pack with a list rather than holding a meeting that can only discover the gaps. Reviewers'
time is best spent on judgement, not on reconstructing a design.

Confirm the risk tier. Designs evolve, and a solution classified as tier 2 at intake may now act in systems or reach
customers. If the tier has changed, the review depth and the other gates change with it; send the case back to
`opportunity-management:risk-classification` first.

Decide the depth of each lens. A tier 2 knowledge agent built on a reference pattern may need only a summary check on
platform fit and conformance, with depth on supportability. A tier 3 agent with write actions in a line-of-business
system needs every lens in depth. Use the specialist design authority skills for the lenses that need depth, and record
which were applied in summary.

Review evidence, not slides. Each finding cites the artefact and section it concerns, the risk or standard behind it,
the specific fix and the owner. "Identity unclear" is not a finding; "The interface catalogue shows ticket creation
through the maker's connection; switch to user authentication or a scoped service identity with an entitlement check"
is.

Classify honestly. Blocking findings are those that would make the solution unsafe, unsupportable or non-conformant in a
way the organisation has not accepted. Advisory findings improve the solution but do not stop it. Inflating advisory
issues to blocking damages trust in the gate as much as waving blocking issues through.

Consolidate findings from other reviewers where they are available, so the delivery team sees one picture. Do not
re-review security or evaluation; record their status and any dependencies.

Record the verdict on the design review record, agree fixes and dates, and close blocking findings only on evidence.
Where the business owner disagrees with a blocking finding, escalate to the accountable executive; their written
acceptance of the risk is recorded, and the finding stays on the record.

## Outputs

- A design review record on the `design-review-record` template: scope, tier, lenses applied and depth, findings classified as blocking or advisory with risk, fix, owner and date, verdict and sign-off.
- A returned-pack note listing missing artefacts, where the pack is incomplete.
- Any written risk acceptance from the accountable executive.

## Microsoft platform considerations

Platform capabilities that a design relies on, such as authentication options, evaluation tooling, ALM and channels,
change often. Reviewers check that the design cites current source records (`ms-agents-compare`,
`ms-agents-extensibility`, `ms-copilot-studio-guidance`, `ms-foundry-models`) for anything volatile, and raise a finding
where it relies on memory.

## Adoption considerations

The gate is part of the delivery experience. Publish what the pack must contain and how long review takes, and run
pre-review clinics for first-time teams so the gate improves designs rather than surprising teams.

## Knowledge considerations

Check that the grounding design names owned, ready sources and that knowledge readiness is evidenced through
`m365-agents:knowledge-source-readiness` or equivalent. Missing knowledge owners for a tier 2 solution are blocking.

## Security and privacy considerations

The `security-privacy` review is separate and blocking from tier 2. The design review records its status and any
dependencies between security fixes and design changes, without repeating it.

## Responsible AI considerations

From tier 3, the `responsible-ai` review applies. Record its status, and treat a design that lacks the oversight it
requires as blocking at the design gate as well.

## Evaluation requirements

Check that the evaluation approach and thresholds match the tier and the non-functional requirements, and that
`evaluation-quality` has agreed them. An unevaluable design is blocking from tier 2.

## Value measures

At portfolio level, track designs approved first time, blocking findings per review by lens, time from pack submission
to verdict and incidents later traced to issues the review missed. The design authority chair owns these measures, with
a baseline from the first quarter of reviews.

## Scale notes

### Starter

A design review can be a single session with the AI lead, a security contact and the business owner, recorded on the
template. Use a partner's architect for tier 3 and 4 designs.

### Scale

Run a regular design authority forum with published pack requirements, specialist lenses applied as needed and a
findings log across reviews.

### Enterprise

Federate tier 2 reviews against reference patterns to business-unit design authorities, with the central authority
reviewing novel designs and tier 3 and 4 solutions, and analyse findings across the estate to improve references.

## Hand-offs

- To `design-authority:ai-necessity-challenge`, `design-authority:platform-fit-review`, `design-authority:architecture-conformance` and `design-authority:supportability-review` for in-depth lenses.
- Back to `ai-architecture:platform-selection` and the build departments with findings to fix.
- To `m365-agents:agent-release-readiness` or the release policy with the verdict.

## Reviewer gates

This skill is the `design-authority` gate. It is blocking from risk tier 2 and advisory below it. It runs alongside the
`security-privacy` gate and, from tier 3, the `responsible-ai` gate. Blocking findings are not traded against dates;
disagreement escalates to the accountable executive for written risk acceptance.

## Failure modes

- The review is a presentation, and nobody reads the artefacts that would reveal the problems.
- Every finding is classified as blocking, teams learn to ignore the gate, and genuinely serious issues are lost.
- A launch date overrides a blocking finding without written risk acceptance.
- An incomplete pack is reviewed anyway, and the gaps are filled with assumptions.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Trade a blocking finding against a release date.
- Approve a tier 2 or higher design with a missing identity map, grounding design or evaluation approach.
- Record a finding without the risk or standard behind it, the fix and an owner.
- Repeat another reviewer department's review instead of recording its status.

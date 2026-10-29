---
name: architecture-conformance
description: Reviews, as a reviewer, whether an AI solution's design conforms to the organisation's reference architectures, mandatory tier controls and architecture standards, records approved deviations with owners and expiry, and classifies each finding as blocking or advisory with the fix. Use when a design claims to follow a reference pattern, when a solution deviates from standards, or when deviations across solutions suggest a reference needs changing.
license: CC-BY-4.0
metadata:
  department: design-authority
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, power-platform, entra, azure
  edition-support: scale, enterprise
  reviewers: design-authority
  sources: ms-copilot-studio-guidance, ms-copilot-studio-security-governance, ms-agents-extensibility, iso-iec-42001, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Architecture conformance

## Purpose

Reference architectures and standards only reduce risk if solutions follow them, and only stay useful if justified
deviations are recorded and fed back. This reviewer skill checks a solution's design against the references and
mandatory controls that apply to its pattern and risk tier, records approved deviations with owners and expiry dates,
and classifies each finding as blocking or advisory. Conformance reviews go wrong when they become box-ticking against
a long checklist, when every deviation is refused even where the reference is wrong, and when deviations are approved
informally and forgotten.

## When to use

- A tier 1 or higher design claims to follow a reference architecture.
- A design departs from a mandatory control or architecture standard.
- A deviation needs approval, with an owner and expiry.
- Several solutions are deviating in the same way, suggesting the reference needs to change.
- An audit asks whether solutions conform to the organisation's AI architecture standards.

## When not to use

- Writing or changing the reference architectures - use `ai-architecture:ai-reference-architecture`.
- Code-level engineering standards for pro-code work - use `ai-engineering:ai-engineering-standards`.
- Reviewing AI-generated code - use `copilot-code:generated-code-review`.
- Reviewing the platform choice - use `design-authority:platform-fit-review`.
- Reviewing security controls in depth - use `security-privacy:connector-review` and `security-privacy:data-exposure-review`.

## Questions to ask first

1. Which reference architecture does the design follow, and which version?
2. Which mandatory controls apply at this risk tier?
3. Where does the design deviate, and what reason is given for each deviation?
4. Has the same deviation been seen in other solutions?

## Required inputs

- The solution design pack, with the reference pattern it claims.
- The current reference architectures and their mandatory controls by tier, from `ai-architecture:ai-reference-architecture`.
- The register of approved deviations.
- Standards the organisation has adopted, if any, for AI management systems or risk frameworks.

If no reference exists for the solution's pattern, conformance is checked against mandatory tier controls only, and the
absence is reported to the AI architecture function.

## Decision framework

Classify every gap between design and reference.

| Gap | Blocking when (tier 2 and above) | Advisory when |
|---|---|---|
| Mandatory control absent | Missing with no approved deviation | Present but implemented differently with equivalent effect, pending a deviation record |
| Fixed decision changed | Identity pattern, data boundary, environment zone or logging differs from the reference without approval | A variation point is used outside its documented range with low impact |
| Wrong reference | The design claims a pattern it does not follow | The pattern fits but a newer version exists |
| Expired deviation | A deviation has passed expiry and the risk remains | Due for renewal soon |
| Recommended practice | Not applicable as blocking | A recommended practice is not followed |

Approved deviations record: the reference and control, the reason, the compensating control, the owner, the approver and
the expiry or review date. Below tier 2, findings are advisory except where a mandatory tier 1 control is absent.
Disagreement escalates to the accountable executive for written risk acceptance.

## Practitioner approach

Identify the claimed reference and version, then read the design against it section by section. Start with the fixed
decisions - identity pattern, data boundaries, environment zone, logging - because deviations there carry the most risk.
Then check the mandatory controls for the tier, then the variation points.

For each gap, find out whether it is a deviation or a misunderstanding. Teams often believe they conform when they have
misread the reference; a short conversation can resolve these without a formal finding, but record the clarification so
the reference can be improved.

Treat justified deviations seriously. A reference cannot foresee every case, and a team that has thought carefully about
why it must deviate is doing good architecture. Ask for the reason, the compensating control and the owner, and approve
with an expiry date so the deviation is revisited. Record it in the deviations register.

Refuse unjustified deviations at the fixed decisions. A design that uses a shared service identity for writes where the
reference requires user identity, without a compensating entitlement check, is blocking at tier 2 regardless of how
convenient it is.

Look across solutions. When the same deviation recurs, the reference is probably wrong or out of date. Report the
pattern to `ai-architecture:ai-reference-architecture` with the evidence, rather than continuing to approve deviations
one by one.

Use standards proportionately. Where the organisation has adopted a management-system standard or a risk framework,
check the controls it has chosen to apply, by reference to the organisation's own implementation, not by reproducing
licensed text.

Record findings with the reference, control, gap, risk, fix and owner, and pass them to the consolidated design review.

## Outputs

- A conformance section in the `design-review-record`: reference and version, controls checked, findings classified as blocking or advisory with fix and owner.
- Deviation register entries with reason, compensating control, owner, approver and expiry.
- A deviation pattern report to the AI architecture function when the same gap recurs.

## Microsoft platform considerations

References depend on platform capabilities that change. When a gap arises because a reference relies on a capability
that has changed, check the current source records (`ms-copilot-studio-guidance`, `ms-copilot-studio-security-governance`,
`ms-agents-extensibility`) and treat it as a reference problem, not a team problem.

## Adoption considerations

Teams follow references they understand. Use clarifications found in reviews to improve reference guidance, and offer
pre-review conformance checks for teams new to a pattern.

## Knowledge considerations

Check that the grounding design follows the reference's knowledge pattern and the grounding standards, linking to
`knowledge-management:knowledge-grounding-standards` rather than re-assessing content.

## Security and privacy considerations

Many mandatory controls are security controls. Share relevant findings with the `security-privacy` reviewers and record
whether security has already assessed them, to avoid conflicting verdicts.

## Responsible AI considerations

Where references include oversight and logging controls for uses affecting people, absence is blocking from tier 3 and
shared with the `responsible-ai` reviewers.

## Evaluation requirements

Check that evaluation follows the approach the reference sets for the tier, with evidence stored where the reference
requires.

## Value measures

At portfolio level, track the share of solutions conforming at first review, open deviations and those past expiry, and
references changed as a result of deviation patterns. The design authority chair owns these, with a baseline from the
first round of reviews.

## Scale notes

### Starter

Conformance is usually checked informally against one or two simple patterns, often a partner's. Record deviations even
so.

### Scale

Check every tier 2 design against the references, keep a deviations register with expiry, and report patterns quarterly.

### Enterprise

Federate conformance checks for standard patterns, automate checks where designs are expressed as code or configuration,
and report conformance and deviations across the estate.

## Hand-offs

- To `ai-architecture:ai-reference-architecture` with deviation patterns and reference problems.
- Back to the delivery team with findings and approved deviations.
- To `design-authority:ai-design-review` for the consolidated verdict.

## Reviewer gates

This skill is part of the `design-authority` gate, blocking from risk tier 2 for fixed decisions and mandatory controls,
and advisory below. Security-related findings are shared with `security-privacy`. Disagreement escalates to the
accountable executive for written risk acceptance.

## Failure modes

- Conformance becomes a long checklist, and teams tick boxes without understanding the reference.
- Every deviation is refused, so teams hide them or build outside the gate.
- Deviations are approved informally, never expire and are forgotten.
- The same deviation is approved repeatedly, and the reference is never fixed.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Approve a deviation without a reason, compensating control, owner and expiry.
- Pass an unjustified change to a fixed decision such as identity or data boundary at tier 2 or above.
- Reproduce licensed standard text; refer to the organisation's own implementation.
- Keep approving the same deviation without reporting it to the reference owner.

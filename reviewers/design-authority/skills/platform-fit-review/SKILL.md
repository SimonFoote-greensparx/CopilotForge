---
name: platform-fit-review
description: Reviews, as a reviewer, whether the Microsoft platform chosen for an AI solution fits its audience, identity, data, actions, lifecycle, operability and cost, and whether the decision record is reasoned and current, classifying each finding as blocking or advisory with the fix. Use when a design reaches the gate with a platform already chosen, when a partner proposes a platform, or when a live solution shows signs of outgrowing its platform.
license: CC-BY-4.0
metadata:
  department: design-authority
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 2, 3, 4
  platforms: m365-agents, copilot-cowork, copilot-code, copilot-studio, ai-foundry, power-platform, azure
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-agents-compare, ms-agents-extensibility, ms-agent-builder, ms-declarative-agents, ms-copilot-studio-guidance, ms-foundry-models
  status: draft
  authors: Simon Foote
---

# Platform fit review

## Purpose

A platform choice that looks fine in a design document can fail in operation: the agent cannot run its action under the
user's identity, the platform has no way to promote changes safely, or nobody in the operating team can support it. This
reviewer skill tests the platform chosen for a solution against what the solution actually needs and what the
organisation can run, and checks that the decision record is reasoned and based on current facts. Each finding is
blocking or advisory with a fix. Reviews go wrong when they relitigate the choice on preference, or when they accept a
record that lists only the winning option.

## When to use

- A design reaches the design gate with a platform already chosen.
- A partner or supplier proposes a platform and the organisation needs an independent view.
- A live solution is hitting limits, workarounds are multiplying, or a re-platform is proposed.
- Two teams have chosen different platforms for similar solutions.
- The decision record relies on capabilities that may have changed.

## When not to use

- Making the platform decision in the first place - use `ai-architecture:platform-selection`.
- Setting the organisation-wide platform mix - use `ai-strategy:platform-strategy`.
- Challenging whether AI is needed at all - use `design-authority:ai-necessity-challenge`.
- Reviewing conformance to reference architectures and standards - use `design-authority:architecture-conformance`.
- Assessing in detail whether a need justifies Microsoft Foundry - use `ai-foundry:foundry-solution-assessment`.

## Questions to ask first

1. What options were considered, and why was each rejected?
2. Can every identity, data and action requirement be met on the chosen platform, as it is today?
3. How will changes be tested, promoted and rolled back on this platform?
4. Who will operate it, and have they confirmed they can?
5. Which volatile facts does the choice depend on, and when were they checked?

## Required inputs

- The architecture decision record for the platform choice, from `ai-architecture:platform-selection`.
- The solution brief, non-functional requirements, identity map and interface catalogue.
- The approved platform list from the platform strategy.
- Confirmation from the operating team of their ability to support the platform.

A decision record that lists no rejected options is a finding: advisory at tier 2, blocking at tier 3 and above. If the
operating team has not been asked, the supportability question is open and recorded as such.

## Decision framework

Test the choice against each dimension. From tier 2, blocking findings stop the gate.

| Dimension | Blocking when | Advisory when |
|---|---|---|
| Strategy | The platform is not approved and no exception exists | Approved, but a preferred platform was not considered |
| Identity | An action requiring user identity can only run under maker or shared credentials on this platform | User identity works but needs a workaround |
| Data and grounding | Required sources cannot be reached with permission trimming intact, or data must leave agreed boundaries | Reachable with extra configuration |
| Actions and integration | Required write actions cannot be confirmed, logged or kept deterministic | Achievable but complex |
| Lifecycle | No way to test, promote or roll back at the tier's required standard | Lifecycle is manual but documented |
| Evaluation | The tier's evaluation requirements cannot be met or evidenced | Evaluation possible but not yet automated |
| Operability | The named operating team cannot support the platform | Support depends on one person |
| Proportion | A much heavier platform is chosen than the need justifies, adding cost and risk | Slightly heavier than needed, with a growth reason |
| Currency | The choice depends on a capability not confirmed in current sources | Sources are cited but due for recheck |

Disagreement with a blocking finding escalates to the accountable executive for written risk acceptance.

## Practitioner approach

Read the decision record first and check its shape. A good record shows the options considered, why each was rejected,
the gates applied and the triggers for revisiting. A record that names only the chosen platform tells you the decision
was made before the analysis; review with that in mind.

Trace the hard requirements to the platform. Take the identity map, interface catalogue and grounding design, and for
each requirement ask how the platform meets it today. Pay most attention to identity and actions, where platform
differences are sharpest. A requirement met only by a feature in preview, a workaround or an assumption is recorded as
such.

Check lifecycle and evaluation. At tier 2 and above, the platform must allow changes to be tested and promoted without
editing production, and must support the evaluation the tier requires. Ask to see the route, not just a statement that
one exists.

Ask the operating team directly. The builders' confidence is not evidence of supportability. If the operating team has
not seen the design, the finding is open until they have.

Test proportion in both directions. A Foundry solution for a knowledge agent is over-engineered; a declarative agent
straining to perform complex write actions is under-engineered. Either is a finding if it adds risk or cost the
organisation has not accepted.

Check currency. For each volatile fact the record relies on (availability, authentication options, channels, limits),
confirm it was checked against a current source and when. Licensing is never concluded in the review; open questions go
to `platform-governance:ai-licensing-and-capacity`.

Do not substitute your own preference. If the choice is reasoned, meets the requirements and can be operated, it passes,
even if you would have chosen differently. Record findings with dimension, evidence, risk, fix and owner, and pass them
to the consolidated design review.

## Outputs

- A platform fit section in the `design-review-record`: dimensions tested, evidence, findings classified as blocking or advisory with fix and owner.
- A request to update the `architecture-decision-record` where options, gates or currency are missing.
- Referrals to licensing or operating teams for open questions.

## Microsoft platform considerations

The boundaries between Agent Builder, Copilot Studio, Power Platform, Copilot Code and Microsoft Foundry move as
Microsoft adds capability. Use `ms-agents-compare`, `ms-agents-extensibility`, `ms-agent-builder` and `ms-foundry-models`
to check current capability, and record the date checked.

## Adoption considerations

Not applicable to most platform fit findings, because they concern build and operation rather than end users. Where the
platform constrains channels, check the solution can still reach users where they work.

## Knowledge considerations

Check that the platform can reach the required knowledge sources with permission trimming, and that knowledge owners
can maintain content without engineering help where the design assumes they will.

## Security and privacy considerations

Identity and data findings overlap with the `security-privacy` review. Record them as platform fit findings where the
platform itself is the cause, and share them so security does not discover them separately.

## Responsible AI considerations

For tier 3 and above, check that the platform supports the logging, oversight and content safety controls that the
`responsible-ai` review requires; a platform that cannot is a blocking finding.

## Evaluation requirements

The platform must support the evaluation approach agreed with `evaluation-quality` for the tier. If evaluation would need
a separate harness, check that the design includes it.

## Value measures

At portfolio level, track re-platforming within a year of release, platform-related incidents and blocking platform fit
findings by dimension. The design authority chair owns these measures, with a baseline from existing solutions.

## Scale notes

### Starter

A short conversation using the dimension table is enough for most starter designs, with a partner's view for Foundry or
pro-code proposals.

### Scale

Apply the review to every tier 2 design and to all re-platform proposals, and keep findings to improve platform
guidance.

### Enterprise

Let business-unit design authorities review designs on approved reference patterns, with the central authority
reviewing new platforms, Foundry solutions and tier 3 and 4 designs.

## Hand-offs

- Back to `ai-architecture:platform-selection` with findings to address.
- To `platform-governance:ai-licensing-and-capacity` for licensing or capacity questions.
- To `design-authority:ai-design-review` for the consolidated verdict.

## Reviewer gates

This skill is part of the `design-authority` gate, blocking from risk tier 2 and advisory below it. Identity and data
findings are shared with `security-privacy`. Disagreement escalates to the accountable executive for written risk
acceptance.

## Failure modes

- The reviewer prefers another platform and blocks a reasoned choice on taste.
- A record that lists only the chosen option is accepted, and the real trade-offs are never examined.
- The operating team is not consulted and inherits a platform it cannot support.
- A capability assumed from an old demonstration turns out to be unavailable.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Block a reasoned, operable platform choice because of reviewer preference.
- Accept a platform that cannot meet an identity or lifecycle requirement at the tier.
- Conclude licensing questions in the review.
- Pass a choice that depends on unconfirmed capability without recording it.

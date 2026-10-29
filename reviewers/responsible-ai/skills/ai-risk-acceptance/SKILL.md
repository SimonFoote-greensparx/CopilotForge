---
name: ai-risk-acceptance
description: Runs the formal acceptance of residual AI risk by an accountable executive when a blocking finding is disputed or risk remains after mitigation - who may accept at which tier, the evidence they must see, conditions, expiry and review, and what can never be accepted - and records it in writing. Use when a team and a reviewer disagree, when a tier 4 solution needs sign-off, or when an acceptance is due for review.
license: CC-BY-4.0
metadata:
  department: responsible-ai
  lifecycle: Assure, Launch, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: responsible-ai, security-privacy
  sources: nist-ai-rmf, iso-iec-42001, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# AI risk acceptance

## Purpose

Reviewer gates block release when a material risk is unresolved, and that is right. But sometimes a business has good
reason to proceed with a residual risk, and sometimes a team and a reviewer genuinely disagree. This skill gives those
situations a proper home: an accountable executive, with authority proportionate to the risk, sees the evidence,
decides in writing, sets conditions and an expiry, and the decision is reviewed. It is the escalation route every other
reviewer skill points to. It goes wrong when acceptance becomes a routine way around the gate, when it is signed by
someone without authority over the consequences, or when it never expires.

## When to use

- A blocking finding from any reviewer-class department is disputed by the solution team.
- Residual risk remains after mitigation and the business wants to proceed.
- A tier 4 solution needs the written executive acceptance that risk classification requires.
- An existing acceptance reaches its review date or its conditions are breached.
- The organisation needs to define who may accept which risks.

## When not to use

- Identifying the impacts and residual risks in the first place - use `responsible-ai:ai-impact-assessment`.
- Uses that the prohibited use screen has stopped - use `responsible-ai:prohibited-use-review`; they cannot be accepted.
- Recording programme-level risks and issues - use `programme-management:programme-risk-log`.
- Setting the overall governance model and decision rights for the CoE - use `ai-centre-of-excellence:coe-governance-model`.

## Questions to ask first

1. What exactly is the residual risk, which reviewer raised it, and why is it blocking?
2. What mitigations were tried or rejected, and why?
3. Who is accountable for the outcome if the risk materialises, and do they have authority over the affected area?
4. What conditions, monitoring and expiry would make acceptance defensible?
5. Is the risk one that cannot be accepted at all - prohibited use, unlawful processing or a provider's terms breached?

## Required inputs

- The reviewer's finding with risk, standard, fix and the solution team's response.
- The risk tier and relevant assessment records (`ai-risk-assessment`, `ai-impact-assessment-record`).
- The organisation's risk appetite statement or delegation of authority, where one exists.
- Legal or DPO advice where the risk has a legal or data protection dimension.

Where no delegation of authority for AI risk exists, use the defaults below and recommend the sponsor confirm them.
Never accept on behalf of an executive or treat silence as acceptance.

## Decision framework

| Risk tier of the solution | Who may accept residual risk (default) | Required before decision |
|---|---|---|
| 2 | Accountable business executive for the affected area | Reviewer finding, team response, mitigations tried |
| 3 | Executive with authority over the business-critical process, with the responsible AI and security leads consulted | As tier 2, plus impact assessment and DPO view where personal data is involved |
| 4 | Accountable executive at the level set by the organisation's risk appetite, with legal adviser and DPO consulted | As tier 3, plus legal advice and evidence of human oversight, escalation and incident readiness |

| Cannot be accepted | Why |
|---|---|
| Stop verdicts from `responsible-ai:prohibited-use-review` | The organisation has decided these uses are unacceptable |
| Processing the legal adviser or DPO has advised is unlawful | Executive acceptance does not change the law |
| Breach of the provider's acceptable use or product terms | The organisation cannot accept a contractual breach on the provider's behalf |
| Risks where the accepting executive has no authority over the affected people or process | Acceptance must sit with whoever answers for the consequence |

Every acceptance has conditions, an owner for each condition, monitoring that would show the risk materialising, and an
expiry no longer than the next scheduled review of the solution.

## Practitioner approach

Treat acceptance as a decision, not a signature. The executive needs a short, honest paper: the finding in the
reviewer's words, the team's response, what would fix it and what that costs, the residual risk in plain language,
who could be harmed, and what conditions would make proceeding defensible. Keep it to two pages; executives who must
read twenty sign without reading.

Check eligibility first. Before any paper is written, confirm the risk is acceptable in principle. Prohibited uses,
advised illegality and provider term breaches go straight back to the team with no acceptance route. Saying so early
saves everyone time.

Find the right person. The accepting executive must be accountable for the area the risk affects and senior enough for
the tier. A delivery director cannot accept a risk to customers' rights; a programme sponsor cannot accept a risk to
another division's staff. Where the right person is unclear, the sponsor decides who it is.

Make the reviewer's view visible. The reviewer does not approve the acceptance, but their finding and their view of
the conditions are attached unedited. Disagreement is recorded, not smoothed over.

Set conditions that can be checked. "Monitor closely" is not a condition; a fictional example of one
that is: "the service manager reviews an agreed weekly sample of outputs for the first two months, and release pauses
if errors exceed the threshold the business owner set". Name the
owner of each condition and what happens if it is breached.

Set an expiry. Acceptances lapse at the next scheduled review or sooner, and are renewed only with fresh evidence. An
acceptance that never expires becomes a permanent exception nobody remembers.

Record and report. Keep all acceptances in a register visible to the responsible AI and security leads and to the
steering group. A rising number of acceptances is a signal that either gates are mis-calibrated or delivery pressure is
overriding risk management; both need attention.

## Outputs

- A risk acceptance record: finding, reviewer view, team response, residual risk, affected people, conditions with owners, monitoring, expiry, accepting executive, date and advice consulted. It completes the risk acceptance section of the `ai-risk-assessment` or `ai-impact-assessment-record`.
- An entry in the organisation's AI risk acceptance register.
- Where acceptance is refused or ineligible, the decision and the route back to remediation.

## Microsoft platform considerations

Not applicable to the decision itself, because acceptance is a governance act independent of platform. Where conditions
rely on platform controls, such as monitoring or approval steps, confirm the current capability in the relevant
source records before writing them into the conditions.

## Adoption considerations

Used sparingly and transparently, acceptance keeps governance credible with the business: valuable work is not blocked
forever, and risk is owned by the right person. Used routinely, it teaches teams that gates are negotiable.

## Knowledge considerations

Not applicable, because acceptance concerns a specific residual risk rather than knowledge sources.

## Security and privacy considerations

Security and privacy findings are frequently the subject of acceptance. Attach the `security-privacy` reviewer's view
unedited and consult the DPO wherever personal data is involved.

## Responsible AI considerations

This skill is the responsible AI route for residual risk. The people who would bear the risk are rarely in the room, so
the paper must describe the impact on them plainly and the conditions must protect them.

## Evaluation requirements

Conditions that depend on solution behaviour need evaluation or monitoring evidence, reviewed at each check-in and
before renewal. Lapsed or breached conditions trigger review, not silent continuation.

## Value measures

Track the number of acceptances by tier and theme, the share renewed with fresh evidence, conditions breached, and the
time from finding to decision. The responsible AI lead owns these measures and reports them to the steering group.

## Scale notes

### Starter

The sponsor accepts residual risk for the few tier 2 solutions, in writing, with a review date. Avoid tier 3 and 4 uses
until a delegation of authority exists.

### Scale

Agree a delegation of authority for AI risk, keep a register, and report acceptances to the CoE steering group each
cycle.

### Enterprise

Align AI risk acceptance with enterprise risk management and delegation of authority, report themes to the board's risk
function, and audit conditions on tier 3 and 4 acceptances.

## Hand-offs

- Back to the solution team and reviewer with the decision and conditions.
- To `m365-agents:agent-release-readiness` with the acceptance reference.
- To `programme-management:programme-risk-log` where the residual risk affects the programme.
- To `ai-centre-of-excellence:coe-governance-model` when acceptance patterns suggest gates need recalibrating.

## Reviewer gates

This skill is the escalation route of every reviewer-class department, including `responsible-ai`, `security-privacy`,
`evaluation-quality` and `design-authority`. A blocking finding stays blocking until written acceptance by an eligible
executive or a fix; no acceptance is possible for ineligible risks.

## Failure modes

- Acceptance is signed by whoever is available rather than whoever is accountable.
- Conditions are vague, nobody checks them, and the acceptance becomes permanent.
- Acceptance becomes routine, and reviewers stop raising blocking findings they expect to be overridden.
- The reviewer's view is summarised away, so the executive decides on a softened account.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Accept a prohibited use, advised illegality or a provider terms breach.
- Record acceptance without a named eligible executive, conditions and an expiry.
- Treat silence, a meeting minute or a launch date as acceptance.
- Edit or omit the reviewer's view in the paper.

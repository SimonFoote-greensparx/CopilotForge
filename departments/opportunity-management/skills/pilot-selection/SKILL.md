---
name: pilot-selection
description: Chooses which AI opportunities to pilot and designs each pilot so it can prove or disprove its value hypothesis - a representative cohort, a comparison, a fixed duration, success and stop thresholds set in advance, quality checks, risk containment and an exit plan. Use when an opportunity is ready to test with real users, when pilots keep running indefinitely, or when a pilot ended and nobody could tell whether it worked.
license: CC-BY-4.0
metadata:
  department: opportunity-management
  lifecycle: Mobilise, Deliver, Measure
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality, responsible-ai
  sources: ms-copilot-adoption-hub, ms-copilot-studio-guidance, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Pilot selection

## Purpose

This skill decides which opportunities are worth piloting and designs each pilot as a fair test of its value
hypothesis. A good pilot can fail: it has a representative cohort, a comparison, a fixed end date and thresholds agreed
before it starts, so the result is a decision rather than an impression. Pilots usually go wrong by being chosen for
enthusiasm rather than learning value, by recruiting only volunteers who would succeed with anything, by having no
comparison, or by drifting on for months because nobody set a date to decide.

## When to use

- A prioritised opportunity is ready to be tested with real users before wider investment.
- Several candidates are competing for limited pilot capacity.
- Previous pilots ran indefinitely or ended without a clear result.
- A sponsor wants to "try" a solution and needs a test that will actually inform a decision.
- A licensed capability is being trialled with a group before broader rollout.

## When not to use

- Writing the value hypothesis the pilot will test - use `opportunity-management:value-hypothesis`.
- Deciding after the pilot whether to scale, iterate, pivot or stop - use `opportunity-management:scale-or-stop`.
- Testing an agent's quality before any users see it - use `m365-agents:agent-testing`.
- Planning a broad Copilot launch to a business unit - use `copilot-adoption:launch-plan`.
- Building a throwaway prototype to explore feasibility - use `copilot-code:ai-assisted-prototyping`.

## Questions to ask first

1. Which hypothesis will the pilot test, and is its disproof condition agreed?
2. Who would the solution serve at scale, and can a pilot cohort represent them?
3. What would we compare against: a similar group without the solution, the same group before, or both?
4. How long must the pilot run for the primary measure to move, and when will we decide?
5. What could go wrong for users or customers during the pilot, and how will it be contained?

## Required inputs

- The value hypothesis with baseline, range, leading indicators and disproof condition.
- The risk tier and the reviews the tier requires before users are involved.
- Evidence that the solution has passed pre-pilot quality testing appropriate to its pattern.
- An engaged business owner and the managers of the proposed cohort.

A pilot cannot start without a measured baseline and agreed thresholds. Where they are missing, the opportunity returns
to `opportunity-management:value-hypothesis`. Never set or adjust thresholds after the pilot has begun without
recording the change and the reason.

## Decision framework

Select pilot candidates with these tests. A candidate should pass all five.

| Test | Passes when |
|---|---|
| Learning value | The result will change a real decision (scale, stop, fund, change pattern) |
| Testable | A measured baseline and a primary measure that can move within the pilot period |
| Contained risk | Harm from failure is limited, reversible and can be monitored |
| Owned | A business owner will act on the result, whichever way it goes |
| Representative | A cohort can be found that resembles the eventual users |

Then design the pilot.

| Element | Good design |
|---|---|
| Cohort | Mixed confidence and roles, chosen with managers, not only volunteers; large enough to see the effect at team level |
| Comparison | A similar group without the solution, or the same group's measured baseline, ideally both |
| Duration | Long enough for the measure to move and habits to form; a fixed end and decision date |
| Thresholds | Success, iterate and stop thresholds from the hypothesis, agreed in writing before start |
| Quality checks | Accuracy, groundedness or output review appropriate to the pattern, sampled throughout |
| Support | Learning, a named contact, Champions and a feedback route |
| Containment | Human review of outputs where needed, limited reach, a way to switch off |
| Exit | What happens to users, data and the solution if the pilot stops |

## Practitioner approach

Choose pilots for what they will teach, not for how likely they are to look good. Ask, for each candidate, what
decision the result will inform and what happens if it fails. A pilot whose failure would change nothing is a
demonstration, and demonstrations should be labelled as such rather than consuming pilot capacity.

Confirm the hypothesis is ready. The baseline must be measured, the primary measure collectable during the pilot, and
the disproof condition agreed. If not, stop here; running a pilot without these produces opinions, and opinions favour
whoever shouts loudest at the review.

Design the cohort with managers. Volunteers are useful for early feedback but are a biased sample; the eventual users
include sceptics and less confident colleagues. Aim for a mix by role and confidence, and agree with managers that
participants have time to learn and use the solution. Keep the cohort large enough that results can be reported at
team level without exposing individuals.

Choose the comparison. The strongest is a similar group doing the same work without the solution over the same period.
Where that is impractical, use the cohort's own baseline and watch for seasonal or volume changes that could explain
the result. Record known confounders before you start.

Set duration and dates. The pilot must be long enough for people to form habits and for the measure to move, and short
enough to keep attention. Put the decision meeting in the diary at the start, with the business owner and sponsor
committed to attend.

Write the thresholds into the pilot charter: the result that means scale, the result that means iterate, and the
result that means stop. Also set quality thresholds with the evaluation route, and agree that a pilot that meets value
thresholds but fails quality thresholds does not count as a success.

Contain risk. Limit reach to the cohort, keep human review on outputs where the risk tier requires it, monitor for
harm, and make sure the solution can be switched off quickly. Complete required reviews before the first user is
involved.

Plan the exit. Users should know what happens if the pilot stops; data created during the pilot needs a retention
decision. A pilot that cannot end cleanly will not be allowed to end. Then run it, collect leading indicators weekly,
and hand the evidence to `opportunity-management:scale-or-stop` on the agreed date.

## Outputs

- A pilot selection record: candidates considered, tests passed or failed, and the chosen pilots with reasons.
- A pilot charter for each pilot: hypothesis, cohort, comparison, duration and decision date, success, iterate and stop thresholds, quality checks, support, containment, exit plan and owners.
- A weekly leading-indicator summary at team level during the pilot.
- An evidence pack for the scale-or-stop review, feeding the `scale-or-stop-review` template.

## Microsoft platform considerations

The pattern affects what the pilot can measure and contain. Individual Copilot use is visible only through aggregate
reporting; agents built in Copilot Studio can be limited to a pilot audience and expose analytics; Foundry solutions
can be instrumented in detail. Licence assignment for pilot cohorts and any trial entitlements are confirmed with the
licensing guide or a licensing partner, never assumed. Check capability against `references/sources.md`.

## Adoption considerations

Pilot results depend heavily on enablement. Give the cohort learning, a named contact and Champions support, and record
the enablement provided so a scaled rollout can repeat it. Under-supported pilots fail for adoption reasons and are
wrongly read as solution failures.

## Knowledge considerations

Where the solution grounds on organisational knowledge, confirm the knowledge is current before the pilot and freeze or
log changes during it, so that results reflect the solution rather than shifting content.

## Security and privacy considerations

Complete the security and privacy reviews required by the risk tier before any user is involved. Tell participants
what data the pilot collects and why, collect only what the measures need, and agree retention with the data
protection officer.

## Responsible AI considerations

Participants should know they are in a pilot and how to raise concerns. Where outputs affect customers or decisions
about people, keep human review in place and include fairness or quality checks, not only speed. Pilots of tier 3 and 4
solutions need `responsible-ai` agreement before start.

## Evaluation requirements

Agree quality thresholds and sampling with the `evaluation-quality` department before start, and run them throughout.
Value thresholds and quality thresholds must both be met for a pilot to count as a success.

## Value measures

The pilot measures the primary measure from the hypothesis against baseline and comparison, plus leading indicators,
reported at team level. At portfolio level, measure the share of pilots that reach a decision on the agreed date. The
AI portfolio manager owns these; never report individual participants' usage or performance.

## Scale notes

### Starter

One or two pilots at a time with a small cohort, the cohort's own baseline as comparison, and a decision meeting with
the sponsor at a fixed date.

### Scale

A pilot charter for every pilot, a comparison group where practical, and pilot capacity limited so that each pilot is
properly supported.

### Enterprise

Pilots in one unit are designed to be repeatable in others; the hub keeps a library of charters and results, and
requires a comparison group for strategic bets.

## Hand-offs

- To `opportunity-management:scale-or-stop` with the evidence pack on the decision date.
- To `m365-agents:agent-release-readiness` or the equivalent release route before users are involved.
- To `copilot-adoption:launch-plan` when a successful pilot is scaled to a wider audience.
- Back to `opportunity-management:value-hypothesis` when a candidate is not yet testable.

## Reviewer gates

From risk tier 2, `evaluation-quality` agrees the quality thresholds and sampling before the pilot starts. From tier 3,
`responsible-ai` must agree the containment and oversight design. Each finding is blocking or advisory; a blocking
finding stops the pilot from starting.

## Failure modes

- Only enthusiastic volunteers take part, results look excellent, and the scaled rollout disappoints.
- No comparison is set, so a seasonal drop in workload is credited to the solution.
- Thresholds are set after results arrive, and every pilot is declared a success.
- The pilot has no end date and becomes an unowned live service.
- Quality is never checked, and a pilot that "saves time" is quietly producing wrong answers.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Start a pilot without a measured baseline, agreed thresholds and a decision date.
- Change thresholds during the pilot without recording the change and the reason.
- Report or compare individual participants' usage or performance.
- Involve users before the reviews required by the risk tier are complete.

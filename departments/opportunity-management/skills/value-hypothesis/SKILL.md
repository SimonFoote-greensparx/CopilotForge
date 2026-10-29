---
name: value-hypothesis
description: States the expected value of a framed AI opportunity as a testable hypothesis before anything is built - the mechanism of change, the measure, its baseline, an expected range, the date it should show, leading indicators and the result that would disprove it. Use when an opportunity is about to be prioritised or piloted, when a team claims an agent will save time without saying how, or when nobody can say what would count as failure.
license: CC-BY-4.0
metadata:
  department: opportunity-management
  lifecycle: Envision, Mobilise
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# Value hypothesis

## Purpose

This skill turns "this will save time" into a statement that can be proven wrong. For a framed opportunity, it names
the mechanism by which AI will change the work, the measure that should move, its baseline, the range expected and by
when, the early signs that it is working, and the result that would show it is not. Every later decision (priority,
pilot design, business case, scale or stop) is tested against this hypothesis. Value claims usually go wrong by being
unfalsifiable ("improve productivity"), by counting usage as value, or by being written after the pilot to fit whatever
happened.

## When to use

- A framed opportunity is about to be prioritised, and its value score needs a basis.
- A pilot is being designed and needs success and stop thresholds set in advance.
- A team asserts that an agent or automation will save time or money without explaining how.
- A business case needs a benefit logic that finance can follow.
- A live solution has no stated value and its future must be decided.

## When not to use

- Writing the problem statement, owner and initial baseline - use `opportunity-management:problem-framing`.
- Designing how a baseline will be measured robustly - use `value-realisation:baseline-design`.
- Converting an approved hypothesis into a benefit register with owners and milestones - use `value-realisation:benefit-hypothesis`.
- Building a financial return model - use `value-realisation:roi-model`.
- Estimating the effort and run cost side of the case - use `opportunity-management:effort-assessment`.

## Questions to ask first

1. What exactly will people do differently, and why would that change the measure?
2. What is the measure, how is it collected today, and what is its current value?
3. How much movement would the business owner consider worth the effort and risk, and by when?
4. What would we see in the first weeks if it were working, before the outcome measure moves?
5. What result would convince the owner to stop?

## Required inputs

- A framed problem on the `opportunity-canvas`, with business owner, current cost and baseline or baseline plan.
- The suitability decision and pattern from `opportunity-management:ai-suitability`.
- Any existing data on the work: volumes, cycle times, error or rework rates, satisfaction.
- The strategic outcome the opportunity supports, if any.

Where the baseline is not yet measured, the hypothesis is recorded as provisional with a dated plan to measure it, and
the opportunity cannot enter a pilot until it exists. Never estimate a baseline and record it as measured.

## Decision framework

A hypothesis is ready when every element passes.

| Element | Passes when | Fails when |
|---|---|---|
| Mechanism | It names the change in work ("case handlers draft summaries from an agent instead of from scratch") | It names the technology only |
| Measure | One primary measure of time, quality, cost, risk or experience, with a source | Usage, licences or adoption are the measure |
| Baseline | Measured, with date and method, or a dated plan | Assumed or remembered |
| Expected range | A low and high expected change, with the reasoning | A single precise figure |
| Timing | When the change should be visible | Open-ended |
| Leading indicators | Two or three early signals linked to the mechanism | None, or only satisfaction |
| Disproof | A threshold below which the owner agrees to stop or rethink | "We will see" |
| Assumptions | The conditions the range depends on are listed | Hidden |

Classify the value type, since it shapes evidence: time released (needs a plan for how the time is used), quality or
error reduction, cost avoided, risk reduced, experience improved, or capability created. A hypothesis claiming time
released with no plan for the time is incomplete.

## Practitioner approach

Start with the mechanism. Sit with the business owner and someone who does the work, and trace the task step by step.
Mark the steps AI will change and how. Most weak hypotheses fail here: the AI changes a small part of the work, but the
claim assumes the whole task shrinks. If drafting is ten minutes of a sixty-minute task, a hypothesis claiming half the
task is saved needs explaining.

Choose one primary measure that the mechanism directly affects, and at most two secondary ones. Prefer measures the
organisation already collects. Where it does not, keep the new measurement simple and agree it with
`value-realisation:baseline-design`. Reject usage as a primary measure; usage shows people are trying the tool, not
that the work improved.

Set the expected range with the owner, not for them. Ask what change would make the effort worthwhile, then ask what
the mechanism makes plausible. If the plausible range sits below the worthwhile threshold, say so now; it is far
cheaper to stop here than after a pilot. Record the reasoning behind the range and any internal evidence used. Do not
borrow headline figures from vendors or analysts.

Name the leading indicators. These appear within weeks and tell you whether the mechanism is happening: the share of
cases where the draft is used, the edit distance between draft and final, the number of escalations. They let a pilot
course-correct before the outcome measure has time to move.

Write the disproof condition and get the owner to agree it in writing. This is the most important line in the
hypothesis and the one owners resist most. Frame it as protecting their time: "If after eight weeks the summary time
has not fallen below the low end of the range, we stop or redesign." A hypothesis without a disproof condition is a
wish.

List the assumptions: that people will use the time released for higher-value work, that knowledge stays current, that
volumes stay similar. Each assumption becomes something the pilot watches.

Finally, record the hypothesis on the canvas, attach it to the backlog entry, and lock it. If it changes later, record
the change and the reason; never silently rewrite the hypothesis to match results.

## Outputs

- A value hypothesis, recorded on the `opportunity-canvas`: mechanism, value type, primary and secondary measures, baseline, expected range, timing, leading indicators, disproof condition, assumptions, owner and date agreed.
- The estimated value range and confidence for the backlog entry.
- A list of measurement actions where baselines are not yet in place.

## Microsoft platform considerations

The chosen pattern shapes which leading indicators are available. Agents built in Copilot Studio and solutions on
Foundry can expose usage and outcome telemetry; individual Copilot use is visible only through aggregate reporting.
Plan leading indicators that the platform can actually provide, and check current reporting capability against
`references/sources.md`.

## Adoption considerations

For individual Copilot and Cowork patterns, value depends on behaviour change. Include the adoption mechanism (learning,
Champions support, manager follow-up) in the assumptions, and make adoption a leading indicator rather than the value.

## Knowledge considerations

Where the mechanism depends on an agent answering from organisational knowledge, list knowledge currency and coverage
as an assumption, with the knowledge owner named.

## Security and privacy considerations

Measurement must not create new privacy risks. Leading indicators are collected at team or role level, and any new data
collection is agreed with the data protection officer before it starts.

## Responsible AI considerations

Where value comes from faster decisions about people, money or access, include a quality or fairness measure alongside
the speed measure, so that a faster but worse outcome cannot count as success.

## Evaluation requirements

The hypothesis sets the outcome threshold; solution quality thresholds (accuracy, groundedness) are set separately by
the evaluation route. Both must pass for a pilot to count as a success.

## Value measures

This skill defines the value measures for the opportunity: primary measure, baseline, range, timing and owner. The
portfolio measure is the share of hypotheses later confirmed, refuted or inconclusive at review, owned by the AI
portfolio manager. Never measure individuals.

## Scale notes

### Starter

A short paragraph on the canvas, agreed in one conversation with the owner, with one measure and a clear disproof
condition.

### Scale

A standard hypothesis record for every opportunity entering assessment, reviewed by the AI portfolio manager for
consistency before prioritisation.

### Enterprise

Hypotheses follow a shared library of measures and value types so results can be compared across units; the benefits
realisation lead reviews hypotheses for strategic bets.

## Hand-offs

- To `opportunity-management:opportunity-prioritisation` with the value range and confidence.
- To `opportunity-management:pilot-selection` to design a pilot that can test the hypothesis.
- To `opportunity-management:business-case` where the initiative is significant enough to need one.
- To `value-realisation:benefit-hypothesis` once the initiative is approved, to establish the benefit register.

## Reviewer gates

Not applicable. A hypothesis is a planning record, not a release. Reviewer gates apply later to the solution built to
test it.

## Failure modes

- Usage is chosen as the measure, adoption rises, and nobody can show the work improved.
- The range is a single optimistic figure that becomes a promise the pilot cannot keep.
- No disproof condition is agreed, so the pilot is always "promising" and never stops.
- The hypothesis is rewritten after the pilot to match what happened.
- Time released is claimed without any plan for how it will be used, and finance rejects the benefit.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Accept usage, licence counts or satisfaction alone as the value measure.
- Record an estimated baseline as a measured one.
- Leave out the condition under which the owner agrees to stop.
- Change a hypothesis after results are known without recording the change and the reason.

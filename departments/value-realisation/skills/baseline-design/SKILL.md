---
name: baseline-design
description: Designs the baselines that must be captured before an AI change goes live - exact measure definitions, method, window, data source, sample and a comparison group where fair - so benefits can be proven later rather than asserted. Use when a launch or pilot date is set and nothing has been measured, when baselines rest on memory or vendor figures, or when seasonal or parallel change would make a simple before-and-after misleading.
license: CC-BY-4.0
metadata:
  department: value-realisation
  lifecycle: Envision, Mobilise, Deliver, Measure
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-adoption-hub, ms-copilot-privacy, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Baseline design

## Purpose

A benefit can only be proven against a starting point that was measured before the change. This skill designs that
starting point for each benefit: the exact definition, the method, the window, the source, the sample and, where it is
fair and feasible, a comparison group, all captured before AI changes the work. Baselines usually go wrong in three
ways: they are reconstructed from memory after launch, borrowed from vendor material, or taken in one unusual week.

## When to use

- A pilot or launch date is set and the benefits it should deliver have no measured starting point.
- A value hypothesis names a baseline that nobody has actually measured.
- Existing baselines come from workshop estimates or published figures rather than the organisation's own work.
- The work is seasonal or volatile, or other changes are running at the same time, so a simple before-and-after would mislead.
- Several solutions will touch the same process and their effects need to be separated.

## When not to use

- Stating an opportunity's expected value and measure at intake - use `opportunity-management:value-hypothesis`.
- Writing the formal benefit statement with its owner - use `value-realisation:benefit-hypothesis`.
- Taking pre-launch readings of Copilot usage and adoption - use `copilot-adoption:adoption-measurement`.
- Choosing the measures on the CoE scorecard - use `ai-centre-of-excellence:coe-kpi-framework`.
- Designing how productivity effects are measured after launch - use `value-realisation:productivity-measurement`.

## Questions to ask first

1. Which benefit statements need a baseline, and what exact measure does each name?
2. Where does the data already exist (case, ticketing, finance or quality systems, document metadata), and which role owns it?
3. How much does the measure vary week to week and across the year, and what else will change the same work during the period?
4. Will some teams receive the change later for practical reasons, so that they could act as a fair comparison group?
5. How much time is left before launch, and what can realistically be captured in it?

## Required inputs

- Benefit statements or value hypotheses with named measures, from `value-realisation:benefit-hypothesis` or `opportunity-management:value-hypothesis`.
- The rollout plan with dates and the teams in each wave.
- Agreed access to existing operational data from its owner.
- The organisation's position on collecting data about work, from the data protection officer and HR.
- A list of other changes affecting the same work (system replacements, restructures, policy changes).

Where a baseline cannot be captured before launch, record the gap, the reason and the fallback used (a retrospective
system extract, never recollection), and lower the confidence of every later claim that depends on it. Never back-fill
a baseline from memory or a published statistic.

## Decision framework

Choose the strongest design that time, data and fairness allow, and record which one was used so later claims carry the
right confidence.

| Design | Use when | Confidence it supports |
|---|---|---|
| Comparison group with before and after | Rollout waves leave similar teams without the change for a period | High |
| Interrupted time series | Long, regular system history exists and no comparison group is available | Medium to high |
| Simple before and after | Work is stable, timescales are short and nothing major changes in parallel | Medium |
| Sampled observation or work study | No system data exists, but items can be timed or checked on a sample | Medium, depending on sample size |
| Retrospective extract | Launch has already happened, but the system kept history | Low to medium |
| Self-report survey only | Nothing else is possible | Low - a perception, not a measured effect |

Rules that apply to every design:

| Rule | Requirement |
|---|---|
| Definition | Written precisely enough that the same thing is counted after launch |
| Window | Covers normal variation, and matches the season of the later comparison where work is seasonal |
| Aggregation | Team, role or process level, above the agreed minimum group size; never individuals |
| Sign-off | The benefit owner agrees the baseline, and it is then frozen |

## Practitioner approach

Start from the benefit, not the data. For each benefit statement write the measure as an exact definition: what is
counted, from which record, between which two events, and what is excluded. "Time to answer a supplier query" becomes
"working hours from the query arriving in the shared mailbox to the first substantive reply, excluding automatic
acknowledgements". Most later arguments about value are really arguments about definitions, and they are far cheaper
to settle now than at the review.

Next, find the data that already exists. Operational systems usually hold timestamps, volumes, reopen rates,
corrections and complaints, and using them avoids the burden and bias of asking people to log their own time. Agree
access with the data owner, and confirm with the data protection officer and HR that the purpose is measuring a
process, aggregated to team or role, and never assessing individuals. Where no system data exists, design a light
sample: a fixed number of items checked or timed by a reviewer following a written method, spread across
representative teams and weeks.

Then look at variation. Pull as much history as is lawful and useful, and plot it before choosing a window. If the
measure swings with month-end, seasonal peaks or staffing, a two-week baseline will either flatter or bury any effect.
List anything else changing the same work during the measurement period, because a new case system or a restructure
will share the credit or the blame with AI.

Look for a fair comparison. Rollouts usually happen in waves for practical reasons, and teams in later waves doing
similar work make a natural comparison for a period. Agree this with the programme rather than delaying anyone for the
sake of measurement, and never withhold a capability purely to create a control group where that would be unfair.
Where waves are not possible, an interrupted time series on long system history is usually the next best design.

Capture the baseline before launch, have the benefit owner sign it off, and freeze it. Record the value, the window,
the method, the source extract and the role that took it. A baseline that can be quietly revised later protects nobody
and invites suspicion of every figure built on it.

Finally, say plainly what the design cannot show. A before-and-after cannot separate AI from everything else that
changed, a survey measures perception, and a small sample carries a wide range. Write the confidence level beside each
baseline so every later report inherits it, and make sure post-launch measurement uses exactly the same definitions
and method.

## Outputs

- A baseline specification for each benefit, recorded against it in the `benefits-register`: definition, design, window, source, sample, value, confidence and sign-off.
- A baseline capture plan with dates, responsible roles and the data owner's agreement.
- A confounders list of parallel changes to cite in later reporting.
- A gap note for every baseline that could not be captured before launch, with the fallback used.

## Microsoft platform considerations

Microsoft adoption and usage reporting can provide usage baselines, but outcome baselines almost always come from the
organisation's own business systems. Where operational data already sits in Dataverse or Microsoft Fabric, extracts can
be repeated with the same query after launch, which protects the definition. What usage reports contain, their
aggregation and how long they retain history change over time; check `references/sources.md` before relying on them.

## Adoption considerations

Asking staff to log time before launch adds burden at the moment goodwill matters most, and it colours the results.
Prefer system data and small samples. Tell teams why a baseline is being taken and that it measures the process, not
them, so later results are trusted.

## Knowledge considerations

For knowledge scenarios, baseline the time to find an answer, the number of questions routed to experts and the share
answered correctly first time. Record the condition of the knowledge source too, because later improvement may come
from tidying content rather than from AI.

## Security and privacy considerations

Operational extracts often contain personal data about staff and customers. Extract only the fields the measure needs,
aggregate before sharing, keep raw extracts with the data owner, and confirm the lawful basis with the data protection
officer. New collection of data about staff goes through `security-privacy:privacy-assessment`.

## Responsible AI considerations

Comparison groups must not unfairly deny people a benefit or place them at a disadvantage. Baseline measures must never
become targets for individuals, which would distort both the baseline and the behaviour it describes.

## Evaluation requirements

Where a benefit depends on output quality, the baseline must include the current human error and rework rates, so that
AI-assisted quality can be compared fairly. Agree the quality method with `value-realisation:quality-measurement` before
the baseline is frozen.

## Value measures

This skill succeeds when every benefit in the register has a signed-off baseline captured before launch, and later
claims use the same definition. The Benefits Realisation Lead tracks both as shares of registered benefits, with zero
as the starting point for a new programme.

## Scale notes

### Starter

One or two outcome measures per priority scenario, taken from data that already exists, with a simple before-and-after
and an honest confidence note. A one-page baseline sheet is enough.

### Scale

A standard baseline specification for every benefit entering the register, comparison groups from rollout waves where
fair, and a baseline check as an entry condition for launch.

### Enterprise

Shared definitions for common measures across business units so results can be compared, repeatable extracts from
governed data platforms, and a central library of baselines that later solutions can reuse.

## Hand-offs

- To `value-realisation:benefit-realisation-plan` to schedule measurement points against the frozen baselines.
- To `value-realisation:productivity-measurement` and `value-realisation:quality-measurement` for the post-launch method.
- To `value-realisation:post-implementation-review` where actuals are compared with the baseline.
- To `programme-management:stage-gates` where baseline capture is a launch entry criterion.

## Reviewer gates

Not applicable as a release gate, because a baseline is a measurement instrument rather than a solution. Where it
collects new data about staff or customers, `security-privacy` confirms purpose, aggregation and minimum group size
before collection starts.

## Failure modes

- The baseline is taken after launch from recollection, and finance rejects every benefit that relies on it.
- A two-week window falls in a quiet period, and normal seasonal recovery is reported as an AI benefit.
- The measure is redefined after launch, so before and after no longer count the same thing.
- A parallel system change drives most of the improvement, and AI is credited with all of it until someone checks.
- Staff are asked to log their own time, resent it, and the baseline reflects the logging rather than the work.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Back-fill a baseline from memory, a workshop estimate or a vendor statistic.
- Baseline or report any measure for named individuals.
- Revise a frozen baseline without recording why and who agreed.
- Withhold a capability from people purely to create a comparison group.

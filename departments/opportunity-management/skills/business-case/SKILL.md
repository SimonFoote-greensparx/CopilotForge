---
name: business-case
description: Writes a proportionate business case for one significant AI initiative - choosing no case, a light case or a full case by cost, risk and reach, then setting out options including a non-AI option, build and run costs, benefits from the value hypothesis, risks, the ask and the decision. Use when a single agent, automation or engineered solution needs funding or approval beyond delegated limits, or when a sponsor asks for a case before committing.
license: CC-BY-4.0
metadata:
  department: opportunity-management
  lifecycle: Envision, Mobilise
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: design-authority, responsible-ai
  sources: ms-copilot-studio-guidance, ms-agents-compare, ms-foundry-models, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Business case

## Purpose

This skill produces the case for funding or approving one significant AI initiative, sized to the decision it supports.
It brings together the framed problem, the value hypothesis, the effort and run cost, the risks and the options, and
asks for a clear decision. Proportionality matters: most AI initiatives need nothing more than a completed canvas, and a
full case for a small agent wastes the time it was meant to save. Business cases usually go wrong by being written
after the decision to justify it, by omitting the option of not using AI, or by presenting optimistic benefits as
certain and run costs as zero.

## When to use

- A single initiative needs funding, people or approval beyond the delegated limit for the backlog.
- A strategic bet from prioritisation needs a decision before work starts.
- A pilot has succeeded and scaling it needs new investment.
- A sponsor or finance asks for a case before committing.
- An initiative crosses business units and needs shared funding agreed.

## When not to use

- Making the funding case for the AI programme as a whole - use `ai-strategy:investment-case`.
- Stating the value hypothesis itself - use `opportunity-management:value-hypothesis`.
- Estimating build effort and run cost - use `opportunity-management:effort-assessment`.
- Building the detailed return-on-investment model - use `value-realisation:roi-model`.
- Deciding whether a pilot should scale on its evidence - use `opportunity-management:scale-or-stop`.

## Questions to ask first

1. What decision is being asked for, from whom, and by when?
2. What are the cost, risk tier and reach of the initiative, and what delegated limits apply?
3. What options are realistic, including a non-AI option and doing nothing?
4. Is the value hypothesis agreed, with a baseline or a dated plan for one?
5. Who will own the benefits and the run cost after release?

## Required inputs

- The framed problem, suitability decision and risk tier on the `opportunity-canvas`.
- The value hypothesis from `opportunity-management:value-hypothesis`.
- The effort assessment from `opportunity-management:effort-assessment`, with build and run ranges.
- The organisation's approval thresholds and any finance format requirements.
- Where costs depend on licences or consumption, the position confirmed by the licensing guide or a licensing partner.

Where any input is missing, the case cannot move beyond draft. Mark the gap "to confirm" with an owner and date. Never
fill a gap with a plausible-looking figure.

## Decision framework

Choose the case size before writing anything.

| Case size | Use when | Content |
|---|---|---|
| No separate case | Within delegated limits, tier 0 to 1, single team | The completed canvas, value hypothesis and effort assessment are the record |
| Light case (two to three pages) | Moderate cost or effort, tier 2, or more than one team affected | Problem, options, costs, benefits, risks, ask |
| Full case | Above a significant cost threshold, tier 3 to 4, external audience, or cross-unit funding | Full template, including sensitivity, benefits plan and exit points |

The thresholds are set locally with finance and recorded in the CoE governance model. Where the case falls on a
boundary, choose the lighter size and add the specific section the decision-maker needs.

Every case compares at least three options: do nothing (the baseline), a non-AI or lower-rung option (process change,
automation, training or an adoption scenario), and the recommended AI option. A case without a credible non-AI option
cannot show why AI is preferable.

The recommendation passes when the expected value range at its low end still justifies the cost, the run cost has an
owner, the risk tier's gates can be staffed, and the exit point is stated.

## Practitioner approach

Write the decision request first. One paragraph: what is being asked, of whom, by when, and what happens if the answer
is no. This keeps the case focused and stops it growing into a project plan.

Assemble the evidence rather than creating it. The problem, hypothesis, effort and risk tier should already exist. If
they do not, go back and complete them; a business case is the wrong place to frame a problem for the first time.
Writing the case is mostly a matter of putting existing records in front of a decision-maker in a clear order.

Build the options honestly. The non-AI option deserves real effort: what would happen if the process were simplified,
an ordinary automation built or people trained? If it would deliver most of the value for much less cost, say so and
recommend it. Decision-makers trust cases that show the alternatives were taken seriously.

Present costs in three parts: build, assure and run, for a stated period. Run cost is where cases are least honest;
include owner time, knowledge upkeep, review cycles, support, consumption and eventual retirement. Licence and
consumption figures come from the organisation's agreements or a licensing partner, never from memory.

Present benefits from the value hypothesis as a range, with the measure, baseline and timing, and show what the case
looks like at the low end of the range. Separate cashable from non-cashable benefits and agree the treatment with
finance where money is involved. Do not add benefits that are not in the hypothesis.

Name the risks that matter to the decision: delivery risk, adoption risk, knowledge readiness, and the risk tier with
the reviews it requires. For tier 3 and 4 initiatives, include what the responsible AI and security reviews must
confirm before release.

State the exit points. A good case says when the organisation will check progress and what result would stop it,
reusing the disproof condition from the hypothesis. This turns approval into a staged commitment rather than a blank
cheque.

Test the case with finance and the business owner before submission, and let the business owner present it. Record the
decision, conditions and date on the case and the backlog entry.

## Outputs

- A business case on the `business-case` template, sized as no case, light or full: decision requested, options compared, costs (build, assure, run), benefits from the value hypothesis, risks, exit points, owners and decision record.
- An updated backlog entry with the decision and any conditions.
- For approved cases, the inputs for `value-realisation:benefit-realisation-plan`.

## Microsoft platform considerations

Options at different rungs carry very different cost shapes: individual Copilot use is mostly adoption effort; agents
add ownership and testing; Copilot Studio adds environment and connector costs; Foundry adds model, hosting and
engineering costs that grow with use. Licensing and consumption terms change and depend on agreements, so route every
licensing question to the Microsoft licensing guide or a licensing partner, and check capability assumptions against
`references/sources.md`.

## Adoption considerations

Include adoption effort and its cost in the recommended option. Show how benefits depend on use, and what happens to the
case if adoption is slower than planned.

## Knowledge considerations

Where the initiative depends on organisational knowledge, include readiness work and ongoing knowledge ownership in
costs, and list knowledge currency as a risk with its owner.

## Security and privacy considerations

The case states the data involved, its sensitivity and the security and privacy reviews required by the risk tier. The
security lead and data protection officer confirm scope; legal questions go to the legal adviser.

## Responsible AI considerations

For tier 3 and 4 initiatives, the case must show that an impact assessment is planned, that human oversight is designed
in, and that responsible AI review capacity exists. Where the initiative affects decisions about people, say so plainly
in the risks.

## Evaluation requirements

Include the evaluation approach and its cost: how quality will be tested before release and after changes, and what
threshold must be met. A case that funds build but not evaluation is incomplete.

## Value measures

The case carries the primary measure, baseline, expected range, timing and benefit owner from the hypothesis. At
portfolio level, measure the share of approved cases whose benefits are later confirmed at review. The AI portfolio
manager owns this measure; never individual performance.

## Scale notes

### Starter

Most initiatives need no separate case. Where one is needed, a light case of two pages for the sponsor is usually
enough, with a partner's help on cost estimates.

### Scale

Case-size thresholds are set with finance and published. Light cases are reviewed at CoE steering; full cases go to the
sponsor with finance review.

### Enterprise

Business units write cases on the shared template; cross-unit and high-tier cases go to the enterprise portfolio board.
Cases are archived so later post-implementation reviews can compare outcomes with what was promised.

## Hand-offs

- To `value-realisation:benefit-realisation-plan` for approved cases.
- To `value-realisation:roi-model` where finance needs a detailed return model.
- To `ai-strategy:ai-roadmap` to place approved work in a horizon.
- Back to `opportunity-management:ai-suitability` when the non-AI option proves stronger.

## Reviewer gates

From risk tier 2, `design-authority:ai-necessity-challenge` reviews the recommended option for unnecessary AI or the
wrong platform. From tier 3, `responsible-ai:ai-impact-assessment` confirms the case plans for impact assessment and oversight. Each finding is recorded as blocking or
advisory on the case before the decision.

## Failure modes

- The case is written after the decision to justify it, and the options are straw men.
- No non-AI option is considered, so nobody can say why AI was needed.
- Run costs are omitted, and the solution becomes an unfunded liability after launch.
- Benefits are presented at the top of the range and treated as committed savings.
- A full case is demanded for every small agent, and teams build outside the process to avoid it.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Omit a do-nothing option and a non-AI option from the comparison.
- State licence prices, consumption rates or licensing conclusions; route them to the licensing guide or a licensing partner.
- Add benefits that are not in the agreed value hypothesis.
- Present a case without exit points and the result that would stop the initiative.

---
name: benefit-hypothesis
description: Turns an approved value hypothesis into formal benefit statements, each with one change, one measure, a direction, a baseline, a target range, timing, an owner role, the enabling changes it depends on and any expected dis-benefits, ready for the benefits register. Use when an opportunity has been approved, when a case lists vague benefits such as efficiency or better insight, or when two solutions claim the same benefit.
license: CC-BY-4.0
metadata:
  department: value-realisation
  lifecycle: Envision, Mobilise, Deliver
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Benefit hypothesis

## Purpose

An approved opportunity usually arrives with a value hypothesis written for a decision: plausible, directional and
often optimistic. This skill turns it into benefit statements that can be measured, owned and tracked: what will
change, for whom, by how much, by when, as a result of which enabling changes, and at what cost to other parts of the
work. It goes wrong when benefits stay as adjectives ("efficiency", "better insight"), when the same released time is
claimed by two solutions, and when the side effects of AI work, such as review effort, are left out.

## When to use

- An opportunity has been approved and its benefits need to enter the benefits register.
- A business case lists benefits that cannot be measured as written.
- Two or more solutions or programmes claim the same improvement in the same process.
- A sponsor asks what exactly the organisation is committing to deliver.
- A live solution has benefits nobody can trace to a measure or an owner.

## When not to use

- Estimating value at intake to support prioritisation - use `opportunity-management:value-hypothesis`.
- Writing the business case that requests funding - use `opportunity-management:business-case`.
- Designing how each baseline will be captured - use `value-realisation:baseline-design`.
- Agreeing who owns each benefit and what ownership involves - use `value-realisation:benefit-owner`.
- Putting money values on benefits with finance - use `value-realisation:financial-benefits`.

## Questions to ask first

1. What did the approved value hypothesis or case promise, and to whom was it promised?
2. Which concrete changes in the way people work will produce the improvement, and which of them does AI enable?
3. What else must happen for the benefit to appear (process change, knowledge clean-up, training, redeployed capacity)?
4. Which other initiatives touch the same process, team or budget line?
5. What new effort or risk will the solution add, such as checking outputs or handling exceptions?

## Required inputs

- The approved value hypothesis from `opportunity-management:value-hypothesis` and, where one exists, the business case.
- The framed problem, affected roles and suitability decision from opportunity management.
- The strategic outcomes the benefit should serve, from `ai-strategy:strategic-outcomes`.
- The current benefits register, to check for overlap.

Where any element of a benefit statement cannot be completed, mark it `[To confirm]` in the register with the role
responsible and a date. Never fill a target with an industry figure or a vendor claim.

## Decision framework

Map each benefit on a short chain, then test the statement before it enters the register.

| Link | Question | Example (fictional) |
|---|---|---|
| Enabler | What capability is delivered? | An agent that drafts responses to planning queries from approved guidance |
| Business change | What do people do differently? | Officers start from a draft and verify it, instead of writing from scratch |
| Outcome | What measurably changes in the work? | Median time to first response falls |
| Benefit | Why does that matter to the organisation? | Fewer escalations and complaints about delay |
| Objective | Which strategic outcome does it serve? | Faster, more consistent public service |

| Test | A statement passes when |
|---|---|
| Single | It describes one change in one measure (split compound benefits) |
| Measurable | The measure has a definition, a source and a baseline or a dated plan to capture one |
| Directional with range | It states direction and a target range, not a single precise figure |
| Timed | It says when the benefit should first appear and when it should be at full level |
| Owned | A business owner role who can influence the change accepts it |
| Attributable | The causal chain is written down and the main confounders are named |
| Unique | No other registered benefit claims the same effect in the same population |
| Net | Expected dis-benefits are recorded beside it |

Classify each benefit by type (time released, quality, financial, experience, risk reduction, capability) so it goes to
the right measurement skill.

## Practitioner approach

Begin with the business change, not the technology. Ask the owner to describe what people will do differently on an
ordinary Tuesday once the solution is live. If nobody can describe the change, there is no benefit yet, only an
enabler. Many AI cases jump from "agent deployed" to "productivity improved" with nothing in between, and that gap is
where value quietly disappears.

Write the chain for each benefit from enabler to objective, and list the enabling changes that are not AI: retiring an
old form, redesigning a review step, cleaning a knowledge source, or deciding what released time will be used for.
These become milestones in the realisation plan. A benefit that depends on a change nobody has agreed to make should be
marked at risk from the start.

Split compound benefits. "Faster and better proposals" is two benefits with different measures and possibly different
owners. Then write each as a single statement: "Median days from request to issued proposal for the bid team falls
from the baseline to a range of X to Y by the end of the second quarter after launch, owned by the head of bids." Keep
the target as a range, because a single figure implies precision the organisation does not have.

Check for double counting against the register. When Copilot in the apps, a drafting agent and a process automation
all touch the same proposal process, they cannot each claim the full time released. Agree one benefit for the process
with contributions noted, or apportion it explicitly and record the method.

Record dis-benefits honestly. AI-assisted work often adds verification time, new exception handling, support load and
run cost, and sometimes shifts effort to another team. A benefit statement without its dis-benefits overstates value
and will be challenged at the first review.

Note the type of each benefit and the measurement approach it needs, and route it accordingly: time released to
`value-realisation:productivity-measurement`, quality effects to `value-realisation:quality-measurement`, money to
`value-realisation:financial-benefits`, and experience, risk or capability to `value-realisation:non-financial-benefits`.

Finally, take the statements back to the owner and the sponsor and confirm that this is what the organisation is now
committing to. Where the formal statements are materially smaller than the original hypothesis, say so plainly and
record the reason; quietly carrying the bigger number forward is how cases lose credibility.

## Outputs

- Benefit statements entered in the `benefits-register`, each with measure, direction, baseline reference, target range, timing, owner role, type and confidence.
- A benefit dependency map from enablers through business changes to benefits and strategic outcomes.
- A dis-benefits list recorded against the benefits it offsets.
- An overlap note where benefits are shared or apportioned between initiatives.

## Microsoft platform considerations

Benefit statements should not depend on a product name or feature, because those change. Describe the capability
("drafts from approved guidance") so the benefit survives a platform change. Where a benefit depends on a feature still
in preview or not yet licensed, record that as a dependency and check the current position in `references/sources.md`.

## Adoption considerations

Most AI benefits depend on people changing how they work. Record the adoption level the benefit assumes (which roles,
which scenarios, how routinely) so `value-realisation:adoption-to-value-metrics` can track the leading indicators.

## Knowledge considerations

Where a benefit relies on an agent grounded in organisational content, name the knowledge source and its owner as an
enabling dependency. Poor or stale knowledge is one of the commonest reasons a benefit never appears.

## Security and privacy considerations

Benefits must not depend on collecting or using personal data beyond what the solution's approved purpose allows.
Where a measure needs data about staff or customers, flag it for the baseline design and the data protection officer.

## Responsible AI considerations

Some benefits, such as faster decisions about people, carry a risk of reduced care or fairness. Record a guard measure
beside any such benefit, and route the case through `responsible-ai:ai-impact-assessment` where outputs inform decisions
about people.

## Evaluation requirements

Where a benefit assumes a level of output quality (for example drafts needing only light edits), state that assumption
so the evaluation threshold agreed at release is consistent with it.

## Value measures

Success is the share of registered benefits that pass all eight tests, and the share whose owner has formally
accepted them, tracked by the Benefits Realisation Lead from the date the register opens.

## Scale notes

### Starter

Two or three benefit statements per initiative on one page, tested against the eight tests in a single conversation
with the business owner.

### Scale

A standard benefit statement format in the register, a benefit dependency map for every initiative above tier 1, and
an overlap check before any new benefit is accepted.

### Enterprise

A shared benefit taxonomy across business units, portfolio-level overlap and apportionment rules, and links from each
benefit to the strategic outcome it serves.

## Hand-offs

- To `value-realisation:baseline-design` for each benefit without a measured baseline.
- To `value-realisation:benefit-owner` to confirm accountability.
- To `value-realisation:benefit-realisation-plan` to schedule the enabling changes and measurement points.
- To `value-realisation:financial-benefits` and `value-realisation:non-financial-benefits` for valuation and evidence.

## Reviewer gates

Not applicable as a release gate, because benefit statements describe expected value rather than release a solution.
Where a benefit informs decisions about people, the guard measure is checked by `responsible-ai` within that solution's
own review.

## Failure modes

- Benefits stay as adjectives, so nothing can be measured and every review becomes a debate.
- The same released time is claimed by Copilot, an agent and an automation, and the portfolio total is fiction.
- Verification and support effort is left out, and the net benefit turns out to be much smaller than the gross.
- A benefit depends on a process change nobody agreed to make, and it never appears.
- The formal statement is quietly smaller than the original promise, and the sponsor discovers it at renewal.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Enter a benefit with no measure, no owner role or no timing.
- Use an industry average or vendor claim as the organisation's target.
- Let two initiatives claim the same effect without apportioning it.
- Omit dis-benefits to make a case look stronger.

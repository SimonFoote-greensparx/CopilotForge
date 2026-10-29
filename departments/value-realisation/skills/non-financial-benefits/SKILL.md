---
name: non-financial-benefits
description: Measures AI benefits that should not be forced into money - customer and employee experience, risk and compliance reduction, decision quality, resilience and organisational capability - with defined indicators, baselines, owners and an evidence standard for each, and no spurious cash value. Use when a case rests on experience or risk reduction, when finance dismisses soft benefits, or when capability gains need evidence a sponsor will accept.
license: CC-BY-4.0
metadata:
  department: value-realisation
  lifecycle: Envision, Mobilise, Measure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, nist-ai-rmf, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Non-financial benefits

## Purpose

Some of the most important AI benefits are not money: customers served better, staff spending less time on drudgery,
fewer compliance breaches, faster and more consistent decisions, and an organisation that can build and run AI safely.
This skill gives those benefits the same discipline as financial ones - a definition, an indicator, a baseline, an owner
and an evidence standard - so they are taken seriously without being dressed up in invented cash values. It goes wrong
when non-financial benefits are left as anecdotes, or when they are converted to money with assumptions nobody can
defend.

## When to use

- A case depends on experience, risk reduction or capability rather than cost.
- Finance or a sponsor dismisses benefits as "soft" because they have no evidence attached.
- Someone proposes putting a cash value on staff wellbeing or reputational risk to make a case add up.
- The programme needs to show that the organisation is becoming more capable with AI, not only that solutions exist.
- A portfolio needs a consistent way to report non-financial benefits across business units.

## When not to use

- Quantifying cashable and non-cashable money benefits - use `value-realisation:financial-benefits`.
- Measuring accuracy, rework and error effects of AI-assisted work - use `value-realisation:quality-measurement`.
- Measuring skills growth from learning at group level - use `learning-and-skills:skills-measurement`.
- Capturing and sharing success stories for communications - use `change-and-communications:success-stories`.
- Assessing the impact of an AI solution on people as a review - use `responsible-ai:ai-impact-assessment`.

## Questions to ask first

1. Which non-financial benefits does the case or strategic outcome rely on, and who in the business cares about each?
2. What existing measures does the organisation already trust for these areas (satisfaction surveys, risk registers, audit findings, engagement surveys)?
3. What would convince a sceptical executive that the benefit is real?
4. Is the organisation required to report any of these outcomes externally or to a regulator?
5. What has the data protection officer and HR agreed about surveying staff or customers?

## Required inputs

- Registered benefit statements classified as experience, risk, decision quality, resilience or capability, from `value-realisation:benefit-hypothesis`.
- Existing organisational measures and their owners (customer feedback, engagement, risk and audit).
- Baselines from `value-realisation:baseline-design`, or a dated plan to capture them.
- The organisation's survey governance and minimum group size for staff measures.

Where no trusted measure exists, propose one and mark it `[To confirm]` with its owner. Do not invent a monetary proxy
to fill the gap.

## Decision framework

Each non-financial benefit gets an indicator from the right family and an evidence standard that matches how the
benefit will be used.

| Family | Example indicators (choose and adapt) | Usual owner role |
|---|---|---|
| Customer or citizen experience | Satisfaction for the affected journey; complaints about delay or inconsistency; first-contact resolution | Service or customer lead |
| Employee experience | Team pulse on time spent on low-value tasks; workload and confidence items in existing surveys; voluntary turnover in affected roles | Business owner with HR |
| Risk and compliance | Policy exceptions; audit findings in the process; near misses; time to detect issues | Risk or compliance lead |
| Decision quality and speed | Time to decision; decisions overturned on review; consistency across teams | Business owner |
| Resilience | Ability to handle peaks without backlog; dependence on single experts | Operations lead |
| Organisational capability | Share of teams able to design and own AI solutions; reusable assets in use; time from idea to governed release | CoE lead |

| Evidence standard | Use when | Requires |
|---|---|---|
| Measured | The benefit is material to a funding or scale decision | Baseline, repeat measure, named confounders |
| Indicated | The benefit supports the case but is not decisive | Trusted indicator moving in the expected direction |
| Illustrated | The benefit is early or hard to measure | Specific, verified examples, clearly labelled as illustration |

Monetise a non-financial benefit only when finance already has an agreed method for that kind of benefit; otherwise
report it in its own units.

## Practitioner approach

Start by finding what the organisation already measures and trusts. Most organisations run customer feedback,
engagement surveys, risk registers and audits. An indicator taken from one of those, for the affected journey or teams,
will be believed far more readily than a new AI-specific survey, and it has a baseline already. Agree with the owner of
that measure how to cut it to the population affected.

For each benefit, write the claim in plain words and ask what evidence would convince a sceptic. "Advisers feel less
overwhelmed" might be evidenced by a workload item in the existing pulse survey for the affected teams, a fall in
overtime, and a drop in voluntary turnover over a longer period. Choose the evidence standard deliberately: measured
for anything a decision rests on, indicated for supporting benefits, and illustrated only where it is too early to
measure, clearly labelled.

Treat risk reduction carefully. The evidence is often an absence: breaches that did not happen. Use leading indicators
such as policy exceptions caught earlier, consistency of applied rules, and audit findings in the process, and ask the
risk owner to judge the change in likelihood or impact using the organisation's risk method. Never claim a risk has
been removed because an AI solution exists.

Make capability visible at organisation level. A maturing organisation can frame problems, choose the right pattern,
build safely and measure value with less help each time. Indicators such as the share of business units with an owner
able to run an agent, reusable assets reused across teams, or time from idea to governed release show this without
assessing individuals.

Be honest about trade-offs. AI can improve consistency while reducing personal discretion that customers valued, or
reduce drudgery while making some roles feel less skilled. Ask about these in the same surveys and report them beside
the benefit.

Resist monetisation pressure. When a sponsor wants a single return figure, show non-financial benefits beside the
financial return, in their own units, rather than converting them with assumptions that would undermine the whole
report.

Finally, keep staff measures at team or role level above the minimum group size, and give survey results back to the
teams that provided them, so the effort of answering feels worthwhile.

## Outputs

- A non-financial benefits schedule recorded in the `benefits-register`: family, indicator, source, baseline, evidence standard, owner role and timing.
- An agreed set of trusted organisational measures cut to the affected populations.
- A risk reduction note with the risk owner's judgement and the leading indicators used.
- A trade-off note recording negative effects found alongside the benefits.

## Microsoft platform considerations

Not applicable as a platform choice, because these benefits are measured through the organisation's existing survey,
risk and service systems. Where Microsoft tools are used to run surveys or store results, follow the organisation's
existing configuration and data protection settings.

## Adoption considerations

Employee experience benefits depend on how adoption is experienced. If people feel pressured to use AI, experience
measures will fall even as usage rises. Share findings with the adoption lead so the programme can respond.

## Knowledge considerations

Better access to knowledge is a common non-financial benefit. Evidence it through fewer questions routed to experts and
faster onboarding of new joiners in the affected roles, and note the knowledge sources that made the difference.

## Security and privacy considerations

Staff and customer surveys collect personal data and sometimes sensitive opinions. Use existing survey governance,
report above the minimum group size, avoid free-text that could identify people in small teams, and confirm the lawful
basis with the data protection officer.

## Responsible AI considerations

Non-financial measures are often where harms appear first: customers feeling unheard, staff feeling deskilled or
monitored. Include at least one measure that would detect such harm for any tier 2 or above solution, and route
concerns to `responsible-ai:ai-impact-assessment`.

## Evaluation requirements

Not applicable directly, because these measures concern organisational outcomes rather than AI output quality.
Decision quality benefits should still be read beside `value-realisation:quality-measurement` results.

## Value measures

Success is the share of non-financial benefits evidenced at the standard agreed for them, and the number reported from
trusted organisational measures rather than new surveys, tracked by the Benefits Realisation Lead.

## Scale notes

### Starter

One experience or risk benefit per priority initiative, evidenced from an existing survey or log, with verified examples
labelled as illustration where measures are not yet available.

### Scale

A standard set of indicators per family, evidence standards agreed per benefit, and non-financial benefits reported
beside financial ones in every value review.

### Enterprise

Organisation-wide indicators for experience, risk and capability that business units contribute to, with trend
reporting over several years and links to external reporting where required.

## Hand-offs

- To `value-realisation:value-dashboard` for reporting beside financial measures.
- To `value-realisation:post-implementation-review` with the evidence gathered.
- To `change-and-communications:success-stories` for verified examples suitable to share.
- To `learning-and-skills:skills-measurement` for detailed skills evidence.

## Reviewer gates

Not applicable as a release gate, because these are outcome measures. Where a negative effect on customers or staff is
found for a tier 2 or above solution, `responsible-ai` is informed through the solution's impact assessment.

## Failure modes

- Experience and risk benefits are left as anecdotes and disappear from the case at the first challenge.
- A cash value is put on wellbeing with invented assumptions, and the whole value report loses credibility.
- A new AI survey is created when an existing trusted measure would have done, adding burden and producing no baseline.
- Risk is claimed as removed because a solution exists, and the next audit finds the same issue.
- Negative effects are not asked about, so they surface through attrition or complaints instead.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Invent a monetary value for a non-financial benefit to make a case add up.
- Report staff experience measures below the minimum group size or by individual.
- Present illustrative examples as measured evidence.
- Claim a risk has been removed rather than reduced, without the risk owner's judgement.

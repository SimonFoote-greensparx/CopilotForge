---
name: skills-measurement
description: Measures AI skills growth at role and team level - declared-skills re-surveys against the needs baseline, verified evidence rates by pathway level, progression and time to evidence - and tests whether groups that built skills changed how they use AI, with a minimum group size and no per-person reporting. Use when a sponsor asks whether learning worked, before a learning dashboard is built, or when learning and adoption data disagree.
license: CC-BY-4.0
metadata:
  department: learning-and-skills
  lifecycle: Measure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-privacy, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# Skills measurement

## Purpose

Sponsors want to know whether AI learning worked, and the usual answer - how many people attended - does not tell them.
This skill measures skills growth at role and team level from declared skills and verified evidence, and examines
whether groups that built skills changed how they use Microsoft AI. It usually goes wrong in three ways: attendance is
reported as skill, measurement drifts down to individuals and destroys trust, and a correlation between learning and
usage is presented as proof that learning caused adoption.

## When to use

- A sponsor or learning budget holder asks what the AI learning programme has achieved.
- A learning dashboard is about to be built and nobody has agreed what it should show.
- Learning data says one thing and adoption data says another, for example high completion but flat use.
- A wave has finished and the needs baseline should be revisited before the next one.
- Someone proposes reporting learning results by named person or ranking teams.

## When not to use

- Measuring Copilot adoption across usage, behaviour and outcomes - use `copilot-adoption:adoption-measurement`.
- Building the chain from adoption to business benefit - use `value-realisation:adoption-to-value-metrics`.
- Programme-level measures for the Champions network - use `champions:champion-metrics`.
- Setting the original skills baseline by role - use `learning-and-skills:ai-skills-needs-analysis`.
- Defining what counts as evidence of a skill - use `learning-and-skills:learning-evidence-rubric`.

## Questions to ask first

1. What decision will the measures inform - continuing, reshaping or extending learning, or reallocating budget?
2. What baseline exists from the needs analysis, and was it collected in a way that can be repeated?
3. Which evidence records and aggregate counts are available, and what has the data protection lead agreed may be used?
4. What is the agreed minimum group size for reporting, and which roles or teams fall below it?
5. Which adoption measures exist at role or team level, from whom, and on what schedule?

## Required inputs

- The declared-skills baseline and needs statements from `learning-and-skills:ai-skills-needs-analysis`.
- Aggregate evidence counts by level and role from `learning-and-skills:learning-evidence-rubric`.
- Adoption measures at role or team level from `copilot-adoption:adoption-measurement`.
- The agreed minimum group size and the data protection lead's agreement on data use and retention.
- The rollout timeline, so learning and access dates can be lined up.

If there is no baseline, say so and set one now; do not reconstruct it from memory. If adoption measures are not
available at role or team level, report skills measures on their own and record the gap. If a group falls below the
minimum size, merge it with a related group or leave it out; never report it.

## Decision framework

Use a small measure set across three layers.

| Layer | Measure | Source |
|---|---|---|
| Declared skills | Change in declared skills by skill area and role against the baseline | Repeat of the needs analysis survey |
| Verified skills | Share of each role with evidence at each pathway level; first-time Meets rate by rubric dimension | Aggregate evidence records |
| Progression | Movement between levels; time from access to foundation evidence | Aggregate evidence records with dates |
| Link to adoption | Change in scenario use and adoption measures for groups with high and low evidence rates | Adoption measures at role or team level |

Read the link to adoption with care.

| Pattern | Likely reading | Response |
|---|---|---|
| Evidence up, adoption up | Consistent with learning helping; other causes possible | Report as association, look for corroboration from managers and feedback |
| Evidence up, adoption flat | Skills not reaching work - access, scenarios, knowledge or manager support | Investigate before adding learning |
| Evidence flat, adoption up | People learning on the job; formal learning may be mistimed or unneeded | Check whether the curriculum adds value |
| Evidence flat, adoption flat | Learning not reaching people, or wrong needs addressed | Revisit needs and delivery |

## Practitioner approach

Start with the decision. A sponsor deciding whether to fund the next wave of learning needs a different view from a
learning team deciding which module to rewrite. Agree the decision and the audience first, then choose the fewest
measures that inform it. A dashboard with forty measures informs nothing.

Repeat the baseline the same way. If the needs analysis used a short survey with concrete statements, use the same
survey, worded the same way, at the same role level. Changing the questions destroys comparability. Report the change
by skill area and role, with confidence, and be honest that declared skills are self-reported.

Use verified evidence as the stronger signal. Evidence rates by pathway level and role show what people have
demonstrated, not what they believe. Look at which rubric dimensions most often sit at Not yet: a role that struggles
with verification needs different help from one that struggles with transfer. Report only aggregates above the minimum
group size; small teams are combined or omitted.

Line learning up with adoption carefully. Compare groups with high and low evidence rates on the adoption measures the
adoption team already collects, using the same role or team grouping and the same time window. Be explicit that this
shows association, not cause: groups that learn more may differ in many ways, such as manager support or more suitable
work. Corroborate with what managers, Champions and office hours themes say about changes in work.

Use mismatches as diagnostics. High evidence with flat adoption is common and usually means something outside learning
is blocking use - access, scenarios that do not fit, untrusted content or no manager follow-up. That finding is often
more valuable than a success story, because it stops the organisation buying more training for a problem training
cannot fix.

Protect people. State in every report that measures are at role or team level, above the minimum group size, and never
used to assess individuals. Refuse requests to break results down by person or to rank teams; offer a group-level
alternative that answers the underlying question.

Close the loop. Each report ends with what will change: modules to rewrite, roles to revisit, issues to hand to
adoption or knowledge owners. Re-run the measures at the end of each wave and before budget decisions.

## Outputs

- A skills measure set recorded in the measures section of the `ai-learning-plan` template - each measure with definition, source, baseline, owner, minimum group size and rhythm.
- A skills growth report per wave by role and skill area, with verified evidence rates and progression.
- A learning-to-adoption review showing the pattern for each role, the reading and the response.
- Actions for curricula, pathways and partner departments, with owners.

## Microsoft platform considerations

Adoption measures for Copilot and agents come from Microsoft's reporting tools and the adoption team's own measures;
their availability, granularity and privacy settings change, so check `references/sources.md` and work with the
adoption team rather than pulling usage data directly. Never use usage reports to infer individual skill.

## Adoption considerations

Share findings with the teams and roles that contributed, framed as what the programme will do differently. Teams who
see their feedback lead to change participate more honestly in the next survey.

## Knowledge considerations

Where skills are high but adoption is flat because people cannot find or trust content, record the finding as a
knowledge issue and refer it to `knowledge-management:knowledge-gap-analysis`.

## Security and privacy considerations

Survey responses and evidence records are personal data. Use only aggregates above the agreed minimum group size, store
source data securely with a retention period, and agree the approach and any linking of learning and adoption data with
the data protection lead before analysis. Data protection questions end with the organisation's DPO.

## Responsible AI considerations

Measures never rank individuals or feed performance, pay or job decisions. Reports are explicit about uncertainty and
do not overstate the effect of learning.

## Evaluation requirements

Not applicable as AI evaluation, because no AI solution is being released. The measure set is reviewed each wave for
whether it informed the decision it was built for.

## Value measures

This skill defines the learning value measures. The baseline is the needs analysis survey and the evidence picture at
the start of the wave. The Learning Lead owns the measure set; adoption measures remain owned by the adoption lead, and
benefits by the benefit owners in `value-realisation`.

## Scale notes

### Starter

A repeat of the baseline survey for the priority roles and simple evidence counts by level, reported once per wave in a
one-page summary.

### Scale

A standard measure set per wave, aggregate evidence data with dates, a learning-to-adoption review with the adoption
team and actions tracked to completion.

### Enterprise

A shared measure set across business units with central analysis, consistent minimum group sizes, a governed data
route for linking learning and adoption aggregates, and results feeding the CoE scorecard.

## Hand-offs

- To `learning-and-skills:ai-role-curriculum` with modules and roles that need rework.
- To `copilot-adoption:adoption-measurement` where findings point to adoption barriers outside learning.
- To `value-realisation:adoption-to-value-metrics` to connect skills and adoption to benefits.
- To `ai-centre-of-excellence:coe-value-tracking` for inclusion in CoE reporting.

## Reviewer gates

Not applicable, because measurement does not release an AI solution. Any proposal to link learning records with usage
data is agreed with the data protection lead before analysis.

## Failure modes

- Attendance and completion are reported as skills growth.
- Results are broken down to small teams or individuals, people stop answering honestly and the baseline is lost.
- A correlation between learning and usage is presented as proof of cause, and the programme over-invests in training.
- The survey is changed between waves, so growth cannot be measured.
- High evidence with flat adoption is ignored instead of investigated.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Report skills or learning data for individuals or below the agreed minimum group size.
- Rank individuals or teams on learning results.
- Present association between learning and adoption as proven cause.
- Use usage reports to infer an individual's skill.

---
name: fairness-review
description: Reviews whether an AI solution could work worse for some groups or treat them unfairly - quality of service across language, dialect, accessibility and role, allocation of opportunities or resources, and stereotyping in generated content - and checks the testing and data behind it, classifying findings as blocking or advisory. Use when outputs affect people differently, when a solution serves a diverse audience, or when someone suspects bias.
license: CC-BY-4.0
metadata:
  department: responsible-ai
  lifecycle: Envision, Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 2, 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, power-platform, platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: responsible-ai, evaluation-quality
  sources: ms-responsible-ai, nist-ai-rmf, ico-ai-data-protection, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# Fairness review

## Purpose

AI solutions can serve some people worse than others without anyone intending it: an agent that misunderstands
questions written in a second language, a summary that drops context for part-time workers, a triage step that sends
some customers to the slow queue more often, or generated text that falls back on stereotypes. This reviewer skill
identifies where unfair outcomes could arise for a specific solution, checks whether testing and data cover the groups
that matter, and classifies findings as blocking or advisory. It goes wrong when fairness is treated as a model
property somebody else has certified, or when groups are tested only where data happens to be easy to get.

## When to use

- The impact assessment identifies groups who could be affected differently.
- Outputs allocate or influence access to jobs, services, money, support or opportunities.
- The solution serves a diverse audience across languages, abilities, locations or roles.
- Generated content describes or addresses people, such as job adverts, customer letters or summaries of individuals.
- Someone reports or suspects that the solution treats some people worse.

## When not to use

- Setting the general quality rubric and acceptance thresholds - use `evaluation-quality:ai-quality-rubric`.
- Testing for harmful or offensive content across the board - use `evaluation-quality:ai-safety-testing`.
- Assessing data quality, completeness and currency in general - use `data-governance:ai-data-quality`.
- Deciding whether a use is prohibited outright - use `responsible-ai:prohibited-use-review`.

## Questions to ask first

1. Who are the affected groups, and which differences between them could change how the solution performs or what it outputs?
2. Does the solution allocate something - attention, priority, eligibility, opportunity - or describe people?
3. What evidence exists that it works equally well for each group, and how was it produced?
4. Does the grounding data, history or example set under-represent or misrepresent any group?
5. Who can tell the organisation if unfair outcomes appear after release?

## Required inputs

- The AI impact assessment record and risk tier.
- The evaluation plan and results, with how test cases were selected.
- A description of the data, examples and knowledge the solution relies on.
- Advice from the DPO or legal adviser where protected characteristics or equality duties are involved.

Where group-level evidence is missing at tier 3 and above, record a blocking finding. Never collect or infer protected
characteristics of individuals to test fairness without DPO approval; use designed test cases instead.

## Decision framework

From risk tier 2 every finding is classified; the gate is mandatory and blocking from tier 3, and from tier 2 when
outputs inform decisions about people.

| Fairness concern | Blocking when | Advisory when | Typical fix |
|---|---|---|---|
| Quality of service | A group gets materially worse answers on matters affecting them, with no mitigation | Small differences on low-impact tasks | Add test cases, improve grounding or instructions, offer an alternative route |
| Allocation | Outputs influence access to jobs, services or money and differ across groups without justification | Differences explained by legitimate factors and documented | Remove the factor, add human review, or stop the use |
| Representation | Generated content stereotypes or demeans a group | Occasional wording issues in internal drafts | Instructions, content review, examples, filters |
| Evidence | No group-level testing at tier 3+ where groups are identified | Testing exists but some groups are thin | Design test cases for each group; record coverage |
| Data | Grounding or examples embed historic unfairness for allocation uses | Data gaps for low-impact uses | Correct, rebalance or remove the data |
| Monitoring | No way to detect unfair outcomes after release | Monitoring planned but not yet running | Aggregate outcome monitoring and a reporting route |

## Practitioner approach

Start with the people, not the metrics. From the impact assessment, list the groups who could reasonably experience the
solution differently. For language-based AI the usual suspects are first language, writing style, dialect, reading
level, disability and assistive technology, location, working pattern, role and seniority. Protected characteristics
matter where outputs touch employment, services or treatment. Ask people who know the audience which differences they
would worry about.

Next, decide what kind of unfairness is possible. If the solution only answers questions, the main risk is quality of
service: some people get worse answers. If it ranks, routes, scores or recommends, there is allocation risk: some
people get less. If it writes about or to people, there is representation risk. Each needs different evidence.

Design test cases for each group rather than looking for real people's characteristics. Write the same question in
plain and complex English, in the way a non-native speaker might, with typical spelling variation, and through a screen
reader where the channel matters. For allocation uses, construct paired cases that differ only in a characteristic that
should not matter, and compare outcomes. For representation, prompt for content about varied people and review it with
people who can spot stereotypes.

Look at the data. Historic decisions, case notes and examples carry the organisation's past patterns. If an agent
learns from previous shortlists, it can repeat their bias. Data that cannot be corrected should not ground allocation
decisions.

Then judge proportionately. Some differences are acceptable if small, low-impact and mitigated by an alternative route.
Others, especially in allocation, are blocking until fixed or until a person makes the decision. Record what was tested,
what was found, what changed, and what remains.

Fairness does not end at release. Agree aggregate monitoring with the owner, such as outcome rates by group where
lawful and approved, complaint themes and override patterns, and a route for people to report unfair treatment. Report
only above an agreed minimum group size, and never use fairness monitoring to profile individuals.

## Outputs

- A fairness section in the `ai-impact-assessment-record`: affected groups, type of fairness risk, test cases and coverage, results, findings classified blocking or advisory with fix and owner.
- A set of group-focused test cases handed to the evaluation owner for regression.
- A monitoring plan for outcomes after release, at aggregate level.

## Microsoft platform considerations

Model choice, grounding and evaluation tooling differ across Copilot, agents, Copilot Studio and Foundry. Microsoft
publishes responsible AI principles and resources in `ms-responsible-ai`, and Foundry offers evaluation capabilities
whose scope changes; use them to support testing, never as a certificate that the organisation's use is fair.

## Adoption considerations

If some groups find the solution works poorly for them, they stop using it and the benefit is unevenly shared. Feed
fairness findings to the adoption team so support and alternatives reach those groups.

## Knowledge considerations

Knowledge written for one audience, for example in technical language or only for office staff, produces worse answers
for others. Raise such gaps with knowledge owners and `knowledge-management:knowledge-gap-analysis`.

## Security and privacy considerations

Processing protected characteristics or special category data for testing or monitoring needs DPO approval and a
lawful basis. Use synthetic or designed test cases where possible, through `security-privacy:privacy-assessment`.

## Responsible AI considerations

This skill is the responsible AI review of fairness. It depends on `responsible-ai:ai-impact-assessment` for affected
groups and often leads to `responsible-ai:human-oversight` where allocation risk remains.

## Evaluation requirements

Group-focused test cases join the evaluation set and are re-run after changes to instructions, knowledge or model.
Results are reported by test group, with thresholds agreed with the business owner and the `evaluation-quality`
reviewers.

## Value measures

Track the difference in answer quality across designed test groups, fairness complaints and their resolution time, and
the share of tier 3+ solutions with group-level evidence. The responsible AI lead owns these measures.

## Scale notes

### Starter

Avoid allocation uses until the organisation can test them properly. For question-answering agents, add a small set of
plain-language and non-native phrasing test cases.

### Scale

Maintain a shared library of group-focused test cases and paired prompts, and include fairness checks in the release
route for tier 2 and above.

### Enterprise

Run independent fairness reviews for tier 3 and 4 solutions, aggregate monitoring across the portfolio, and involve
employee and customer representatives in reviewing results.

## Hand-offs

- To `evaluation-quality:golden-dataset` with group-focused test cases.
- To `responsible-ai:human-oversight` where allocation risk needs a person to decide.
- To `data-governance:ai-data-quality` for data that embeds historic unfairness.
- To `responsible-ai:ai-risk-acceptance` for disputed residual findings.

## Reviewer gates

This skill is part of the `responsible-ai` gate, mandatory and blocking from risk tier 3 and from tier 2 when outputs
inform decisions about people. `evaluation-quality` reviews the test evidence. Disagreement escalates to the
accountable executive for written risk acceptance.

## Failure modes

- Fairness is assumed because the model provider publishes responsible AI material.
- Testing uses only fluent, standard English, so people who write differently get worse answers unnoticed.
- Historic decisions are used as grounding for allocation, and past bias is repeated at scale.
- Monitoring is promised at release and never set up.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Infer or collect individuals' protected characteristics for testing without DPO approval.
- Treat a provider's responsible AI statements as evidence that the organisation's use is fair.
- Report fairness monitoring below the agreed minimum group size or about individuals.
- Trade a blocking finding against a launch date.

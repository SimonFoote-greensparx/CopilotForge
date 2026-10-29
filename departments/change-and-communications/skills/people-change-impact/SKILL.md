---
name: people-change-impact
description: Assesses how an AI change affects each group of people - tasks, skills, workload, decisions and accountability, tools, team routines and role expectations - with the group's readiness and capacity for change, any consultation needs, and the support each group requires, assessed by role group and never by person. Use when AI will change how a role works, before waves or curricula are planned, or when staff ask what AI means for their jobs.
license: CC-BY-4.0
metadata:
  department: change-and-communications
  lifecycle: Envision, Mobilise, Enable, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-studio, power-platform
  edition-support: starter, scale, enterprise
  reviewers: responsible-ai
  sources: ms-copilot-adoption-hub, ms-responsible-ai, ico-ai-data-protection, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# People change impact

## Purpose

This skill works out, group by group, what an AI change will actually do to people's work: which tasks shift, which
skills matter more or less, how workload and pace move, who becomes accountable for checking AI output, and what
changes in team routines and role expectations. It also assesses each group's readiness and capacity to absorb the
change, so the programme can plan support, sequencing and any consultation. Impact assessments usually go wrong by
staying generic ("everyone will be more productive"), by quietly turning into headcount planning, or by assessing
named individuals instead of role groups.

## When to use

- Microsoft 365 Copilot, an agent, a Cowork task or an automation will change how a defined role or team works.
- Waves, onboarding or curricula are being planned and nobody can say which groups are most affected.
- Staff, managers or employee representatives are asking what AI means for their jobs, and there is no considered answer.
- Several changes are landing on the same groups at once and the programme needs to see change load.
- A solution moves work between teams, for example a team that used to draft responses now reviews AI drafts.

## When not to use

- Assessing the impact of a specific AI solution on the people its outputs affect, as a responsible AI review - use `responsible-ai:ai-impact-assessment`.
- Deciding which steps of a task to delegate to Cowork and which stay human - use `copilot-cowork:work-delegation-design`.
- Turning the impact into learning needs per role - use `learning-and-skills:ai-skills-needs-analysis`.
- Quantifying released capacity or cashable savings - use `value-realisation:financial-benefits`.
- Mapping stakeholder influence and concerns - use `change-and-communications:ai-stakeholder-mapping`.

## Questions to ask first

1. What exactly changes - which AI experience, which scenarios or solutions, for which role groups, and from when?
2. For each affected group, what tasks will AI do, assist or check, and what new work appears (verification, exception handling, prompt and agent upkeep)?
3. Is any change to job content, headcount, location, hours or performance expectations being considered, and have HR and the legal adviser been involved?
4. What other changes are landing on the same groups in the same period?
5. Who can describe each group's work credibly - a business owner, team leaders, a few people who do the job?

## Required inputs

- The change description, the scenario catalogue from `copilot-adoption:scenario-discovery` and any solution designs or Cowork task designs in scope.
- Role groups and headcount ranges from HR, at group level only.
- The stakeholder map from `change-and-communications:ai-stakeholder-mapping`, especially groups with formal representation.
- A view of concurrent change from the programme or portfolio office.
- The organisation's position, agreed by the sponsor and HR, on what AI adoption does and does not mean for jobs.

If the jobs position is not agreed, record that as the first open issue and escalate it to the sponsor and HR; do not
fill the gap with the programme's own assumptions. Where work detail is missing, mark the dimension "to confirm" rather
than guess.

## Decision framework

Rate each role group on each dimension as low, medium or high, with one line of evidence. A dimension is high when
people will do materially different work, need materially new skills or carry new accountability.

| Dimension | Low | High |
|---|---|---|
| Tasks | AI assists occasional tasks | Core daily tasks are done, drafted or triaged differently |
| Skills | Familiar skills applied with a new tool | New judgement skills, such as verifying AI output or designing tasks for delegation |
| Workload and pace | Little change | Volume, pace or mix changes, including new review or exception work |
| Decisions and accountability | Unchanged | People now sign off AI-drafted work or act on AI recommendations |
| Tools and access | One new feature | New tools, devices or ways of accessing information |
| Team routines | Unchanged | Meetings, hand-offs or team norms change |
| Role expectations | Unchanged | What a good job looks like changes, or role content changes |

Then combine impact with readiness to set the support level.

| Overall impact | Readiness and capacity for change | Support level |
|---|---|---|
| Low | Any | Standard communications, onboarding and self-help |
| Medium | Good | Role-based adoption journey and manager briefing |
| Medium | Low (change fatigue, poor past experience, peak season) | Role-based journey, delayed or phased start, extra manager support |
| High | Any | Dedicated change plan for the group, early engagement, HR involvement, and consultation where HR and legal confirm it is required |

Any change to job content, headcount, terms or performance expectations is outside this skill's authority. Record it,
stop, and route it to HR and the legal adviser.

## Practitioner approach

Define the groups by the work they do, not by the organisation chart. "Accounts payable processors", "contact centre
team leaders" and "bid writers" are useful; "Finance" is not. Use groups large enough that no individual can be
identified, and agree the minimum size with HR.

Describe a working week for each group with the people who know it. Ask a business owner, a team leader and two or
three people who do the job to walk through what they spend time on, then mark which tasks the in-scope AI will do,
assist or check. This conversation is the core of the method. A desk exercise based on product descriptions produces
generic answers and misses the new work AI creates: checking drafts, handling the cases AI cannot, maintaining
prompts or knowledge, and explaining AI-assisted decisions to customers or colleagues.

Rate the dimensions with evidence and be honest about uncertainty. Early in a programme, many impacts are hypotheses;
say so, and plan to re-rate after a pilot. Pay particular attention to accountability. When a team moves from writing
to reviewing, people need to know they own the result, what good checking looks like, and how much time it really
takes.

Assess readiness and capacity for change as a group property. Look at concurrent change, recent experience of change,
peak periods, staffing pressure, digital confidence and the strength of local leadership. These are signals for
sequencing and support, not judgements of people. A highly affected group in its busiest quarter should usually wait.

Check the edges. Ask which groups are affected indirectly: the team that receives AI-drafted work, the people whose
knowledge an agent will use, the frontline colleagues who will be asked questions customers got from an agent. These
groups are often missed and become the source of later friction.

Agree the jobs position before publishing anything. The sponsor and HR must agree what the organisation is saying about
roles and jobs, and HR and the legal adviser decide whether any consultation obligation is triggered. The impact
assessment informs that decision; it does not make it. Keep released capacity separate from headcount in all wording,
and let `value-realisation:financial-benefits` handle any decision about how capacity is used.

Turn the ratings into actions: the support level for each group, what managers need to know, what the learning
function must build, where the communications strategy must be specific, and which groups need their own plan. Share a
summary with each affected group's leadership and invite correction; impact assessments improve markedly when the
people affected see them.

## Outputs

- A people change impact assessment: role groups, ratings on each dimension with evidence, readiness and capacity signals, overall impact, support level and open issues.
- A change heatmap of groups against dimensions for the sponsor and the change lead.
- A list of matters referred to HR and the legal adviser, with dates.
- Group-level inputs for `learning-and-skills:ai-skills-needs-analysis`, `copilot-adoption:audience-segmentation` and the `ai-communications-plan`.

## Microsoft platform considerations

Impact depends on what the in-scope experience actually does in the organisation's configuration: what Copilot can see
in a user's work context, what an agent is grounded on, which steps a Cowork task performs and where a person checks.
Confirm capabilities and availability against `references/sources.md` and the solution designs, not marketing
descriptions, and re-rate when Microsoft changes the experience materially.

## Adoption considerations

Impact ratings drive sequencing and depth of adoption support. High-impact groups need role-based journeys through
`copilot-adoption:role-based-adoption` and managers prepared through `change-and-communications:manager-enablement`
before access is switched on.

## Knowledge considerations

Where an agent or Cowork task relies on a group's knowledge, that group gains upkeep work. Record it as an impact and
confirm ownership with `knowledge-management:knowledge-owner-model`.

## Security and privacy considerations

The assessment works with aggregate HR data at group level above the agreed minimum size. Store it with restricted
access, because early drafts may describe sensitive organisational options. Questions about the use of employee data
end with the DPO.

## Responsible AI considerations

Where AI informs decisions about people inside or outside the organisation, or changes how staff are supervised,
record it and pass it to `responsible-ai:ai-impact-assessment`. People should never discover that AI is assessing
their work through an adoption programme.

## Evaluation requirements

Not applicable as solution evaluation. The assessment is checked after pilots and the first wave by comparing predicted
and observed impact for each group, and re-rated where they differ.

## Value measures

Owned by the change lead: groups assessed before their wave, issues referred to HR resolved before announcement, and
the gap between predicted and observed impact after the first wave. Reported at group level only.

## Scale notes

### Starter

A single table covering four to eight role groups, completed in a few working sessions with business owners and HR.

### Scale

An assessment per wave or business unit using common dimensions, with a combined heatmap and concurrent-change view.

### Enterprise

A standard impact method across divisions, integrated with workforce planning governance owned by HR, with regional
variations for differing consultation arrangements.

## Hand-offs

- To `learning-and-skills:ai-skills-needs-analysis` with skills changes per role group.
- To `change-and-communications:manager-enablement` for the managers of high-impact groups.
- To `change-and-communications:ai-communication-strategy` so messages answer each group's real impact.
- To `responsible-ai:ai-impact-assessment` where AI affects decisions about people.

## Reviewer gates

From risk tier 2, the `responsible-ai` department reviews the assessment for any solution that changes how people are
supervised or decisions about people are made, looking for missed affected groups and unmanaged accountability
shifts. Below tier 2, no formal gate applies.

## Failure modes

- The assessment is written from product descriptions, misses the new review and exception work, and teams are overloaded.
- Impact work drifts into headcount planning, leaks, and destroys trust in the adoption programme.
- Indirectly affected groups are missed and become the source of friction after launch.
- Ratings are never revisited after the pilot, so later waves are planned on wrong assumptions.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Assess, rate or list named individuals, or use groups small enough to identify them.
- Decide or imply changes to headcount, job content, terms or performance expectations; those belong to HR and the legal adviser.
- Present released capacity as a reduction in jobs.
- Publish impact findings before the jobs position and any consultation sequence are agreed.

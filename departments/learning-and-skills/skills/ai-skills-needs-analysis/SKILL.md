---
name: ai-skills-needs-analysis
description: Analyses AI skills needs role by role, comparing the skills people have declared with what their future work will demand - the scenarios, agents and delegated tasks heading their way - and produces a prioritised needs statement per role, never per person. Use when a learning budget is being set, when training is about to be bought before anyone knows what roles need, or when a new group of roles joins the rollout.
license: CC-BY-4.0
metadata:
  department: learning-and-skills
  lifecycle: Discover, Mobilise, Enable
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-studio
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-overview
  status: draft
  authors: Simon Foote
---

# AI skills needs analysis

## Purpose

Learning programmes for Microsoft AI are often bought before anyone has asked what each role actually needs to do
differently. This skill works out, for each priority role, the gap between the skills people have declared and the
skills their future work requires, and turns that gap into a short, prioritised needs statement that curricula can be
built from. It usually goes wrong in two ways: generic "AI literacy for everyone" that changes nothing in daily work,
and needs analyses that drift into assessing individuals rather than roles.

## When to use

- A learning budget or training procurement is being planned and nobody can say what each role needs.
- A rollout wave is about to add new roles, and the existing training was designed for someone else.
- Scenario discovery or role-based adoption has identified what roles will do with AI, and the skills behind it are unclear.
- Leaders ask whether staff are "ready for AI" and need an honest answer at role level.
- Learning has been delivered but usage remains shallow, suggesting the wrong needs were addressed.

## When not to use

- Finding capability and capacity gaps in the transformation team that runs the programme - use `organisation-tailoring:capability-gap-analysis`.
- Segmenting the workforce into adoption audiences and personas - use `copilot-adoption:audience-segmentation`.
- Assessing how roles, tasks and workload change because of AI - use `change-and-communications:people-change-impact`, whose output this skill consumes.
- Turning the needs into modules, sequence and formats - use `learning-and-skills:ai-role-curriculum`.
- Defining what a Champion must evidence - use `champions:capability-framework`.

## Questions to ask first

1. Which roles are in scope for this wave, and which are the priority roles by numbers affected and value at stake?
2. What will each role be doing with AI in the next six to twelve months - which scenarios, agents, delegated tasks or building work?
3. What do people in those roles already declare they can do, and how was that information collected?
4. What learning already exists, and what do people say about it?
5. Are there roles where the honest answer is "no AI skills need yet", because the role is not in a wave or the scenarios are not ready?

## Required inputs

- The role list for the wave, using declared roles from the organisation profile or role catalogue (`organisation-tailoring:ai-role-catalogue`).
- Future-work evidence per role: the scenario catalogue from `copilot-adoption:scenario-discovery`, planned agents and Cowork tasks, and any role-impact assessment from `change-and-communications:people-change-impact`.
- Declared skills at role or team level: a short self-declaration survey, Champion and manager input, or existing skills framework data, aggregated above the agreed minimum group size.
- The current learning catalogue, with any feedback on it.

Where future-work evidence is missing for a role, mark the role "needs not yet determinable" rather than guessing; the
answer is to finish scenario discovery first. Where declared-skills data is missing, record the need as an assumption
with low confidence and plan a short survey.

## Decision framework

Describe the skill areas consistently across roles, then rate each role's gap from the aggregate evidence.

| Skill area | What it covers |
|---|---|
| Safe and approved use | What the approved tools are, what not to share, how to report a concern |
| Verification | Checking outputs against sources, spotting fabrication, knowing when not to rely on AI |
| Everyday productivity | Drafting, summarising, analysing and meeting work with Copilot in the role's own apps |
| Working with agents | Choosing and using approved agents, recognising their limits, giving feedback |
| Delegating work | Framing a multi-step task for Copilot Cowork, setting checkpoints, reviewing the result |
| Building | Agent Builder, Copilot Studio, Power Platform automation, Copilot Code or Foundry, for those whose role includes it |

| Gap rating | Rule | Typical response |
|---|---|---|
| None | Future work does not need the skill, or the role already declares it widely | No learning; signpost resources |
| Light | Most of the role has the basics; future scenarios add a little | Short session or self-paced module |
| Substantial | Future scenarios depend on the skill and few declare it | Curriculum module with practice and evidence |
| Critical | Safe use or verification gap in a role that handles sensitive content or affects decisions about people | Mandatory foundation before access to the scenario |

Prioritise roles by headcount affected, value of the scenarios that depend on the skill, and risk. A small role with a
critical verification gap can outrank a large role with a light gap.

## Practitioner approach

Start from the work, not the tool. For each priority role, write two or three sentences describing what that role
will do differently with AI over the next year, drawn from the scenario catalogue and any planned agents or delegated
tasks. "Account managers will prepare client meetings with Copilot summarising recent mail and documents, and will
use the approved proposal agent." If you cannot write that sentence, the role's needs cannot yet be determined; send
it back to scenario discovery rather than filling the gap with generic training.

Next, collect declared skills at role level. A short survey asking people to describe what they currently do with
approved AI tools, using concrete statements rather than a confidence scale, works better than asking them to rate
themselves. Add what Champions, team leads and the service desk observe about common questions and mistakes. Report
only aggregates above the agreed minimum group size, and say plainly in the survey that responses will never be used
to judge anyone.

Map the future work onto the skill areas and rate the gap for each area and role. Pay special attention to
verification and safe use: these are the gaps that cause harm, and they are often hidden because people are confident
in outputs they have not checked. Where a role handles sensitive information or its outputs feed decisions about
people, money or safety, a weak verification picture is critical regardless of headcount.

Look at what already exists before recommending anything new. Microsoft publishes adoption and learning material, and
many organisations have recorded sessions that could serve a light gap. Check the current resources in the source
records rather than assuming what is available.

Then prioritise. Combine headcount, the value of the dependent scenarios and the risk of the gap into a short list of
role-and-skill pairs. Be explicit about what you are not addressing in this wave and why. A needs statement that
treats every gap as urgent gives curriculum designers nothing to work with.

Finally, write the needs statement per role: the future work, the gaps by skill area with ratings, the evidence behind
each rating, its confidence, and the learning response type. Share it with the role's business owner, who should
recognise their team in it. Revisit it when scenarios change or a new wave is planned; skills needs for AI move as fast
as the products do.

## Outputs

- A role-level skills needs statement in the needs section of the `ai-learning-plan` template: future work, gaps by skill area, rating, evidence, confidence and response type.
- A prioritised list of role-and-skill pairs for the current wave, with what is deliberately deferred.
- A short declared-skills survey and its aggregate results, above the minimum group size.

## Microsoft platform considerations

The skill areas follow the Microsoft AI patterns the role will meet: Copilot Chat, Copilot in the Microsoft 365 apps,
agents, Copilot Cowork, and building platforms such as Agent Builder, Copilot Studio and Power Platform. Which of these
a role can access depends on licensing and approval decisions made elsewhere; do not assume access, and check product
naming and availability against `references/sources.md`.

## Adoption considerations

Needs analysis should read as help, not inspection. Explain that the purpose is to give each role learning that fits
its work, and share the aggregate findings with the teams who contributed. Roles that see their input reflected engage
far better with the resulting curriculum.

## Knowledge considerations

Where a role's gap is really about not knowing where trusted information lives, rather than how to use AI, record it as
a knowledge issue and refer it to `knowledge-management:knowledge-gap-analysis`. Training cannot fix content that is
missing or out of date.

## Security and privacy considerations

Survey responses are personal data even when only aggregates are reported. Collect the minimum, store responses
securely with a retention period, and agree the approach with the data protection lead. Data protection questions end
with the organisation's DPO.

## Responsible AI considerations

Flag roles whose AI-assisted outputs affect people, rights, money or safety: their verification and oversight skills are
a responsible AI control, not just a productivity aid. Never use the analysis to judge individuals or to inform
decisions about jobs.

## Evaluation requirements

Not applicable as AI evaluation, because no AI solution is being released. The quality check is that each role's
business owner confirms the future-work description and the gap ratings are recognisable.

## Value measures

The baseline is the declared-skills picture per role at the start of the wave. The Learning Lead owns a re-run of the
same survey after the curriculum is delivered, alongside verified learning evidence, reported at role level through
`learning-and-skills:skills-measurement`.

## Scale notes

### Starter

Cover two or three priority roles with a short conversation with each role's lead, a five-question survey and a
one-page needs statement per role.

### Scale

Run the analysis per wave, with a standard skill-area model, a reusable survey and needs statements held alongside the
scenario catalogue so both are refreshed together.

### Enterprise

Federate analysis to business-unit learning partners using the shared skill-area model, with the central learning team
consolidating needs across units to find common modules and avoid duplicate procurement.

## Hand-offs

- To `learning-and-skills:ai-role-curriculum` with the prioritised role-and-skill pairs.
- To `learning-and-skills:ai-learning-pathway` where several roles share the same progression need.
- To `learning-and-skills:advanced-pathways` for roles whose future work includes building.
- To `knowledge-management:knowledge-gap-analysis` where the gap is really missing or poor knowledge.

## Reviewer gates

Not applicable, because a needs analysis does not release an AI solution. If the survey collects more than aggregate
role data, the approach goes to the data protection lead before it runs.

## Failure modes

- The analysis starts from the product catalogue rather than the role's work, so every role gets the same generic course.
- Self-rated confidence is taken as skill, hiding verification gaps in confident users.
- Results are broken down to small teams or individuals, people stop answering honestly and the data loses value.
- Every gap is marked urgent, so curriculum designers cannot prioritise and the budget is spread thinly.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Assess, score or rank individuals, or report skills data below the agreed minimum group size.
- Recommend learning for a role before its future work with AI is described.
- Assume a role has access to a tool or licence without confirmation.
- Use the analysis to inform decisions about jobs, pay or performance.

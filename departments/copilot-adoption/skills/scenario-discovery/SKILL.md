---
name: scenario-discovery
description: Segments the workforce into personas such as desk, hybrid and frontline workers, discovers role-based Copilot scenarios with business owners, prioritises them by value and frequency, and builds a scenario catalogue with prompt patterns that users can verify. Use when planning what people will actually do with Copilot, when usage is generic and shallow, or when a new team or role joins the rollout.
license: CC-BY-4.0
metadata:
  department: copilot-adoption
  lifecycle: Discover, Envision, Enable
  maturity: explorer, adopter, builder, scaler
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, copilot-cowork
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-adoption-hub, ms-copilot-overview
  status: draft
  authors: Simon Foote
---

# Scenario discovery

## Purpose

People adopt Copilot when it helps with work they already do, not when they are shown a list of features. This skill
segments the audience into personas, works with business owners to find the recurring tasks where Copilot helps, ranks
those scenarios by value and frequency, and records each one with a prompt pattern and a way to check the output. It
usually goes wrong when scenarios are invented centrally from product demonstrations, so they look impressive but match
nobody's working week.

## When to use

- Before launch, to decide which scenarios each persona will be onboarded with.
- When usage is broad but shallow, and people say they "do not know what to use it for".
- When a new business unit, role or frontline population joins the rollout.
- When Champions or managers ask for role-specific examples they can share.
- When Champion Challenges produce prompt libraries, departmental playbooks or workshop outputs that need bringing into the catalogue.

## When not to use

- Checking whether the organisation is ready to launch at all - use `copilot-adoption:adoption-readiness`.
- Deciding whether a larger problem needs an agent, automation or a built solution - use `opportunity-management:ai-suitability`.
- Framing a significant business problem with an owner and measure - use `opportunity-management:problem-framing`.
- Planning the launch waves and onboarding around the scenarios - use `copilot-adoption:launch-plan`.
- Turning a scenario into a practical Champion Challenge - use `champions:champion-challenges`.
- Designing formal role-based curricula - use `learning-and-skills:ai-role-curriculum`.

## Questions to ask first

1. Which roles are in scope, and how do they work: at a desk, hybrid, on the move or on a shop floor?
2. What recurring tasks take most time, cause most frustration or are most often done late in each role?
3. Who is the business owner for each role who can confirm a scenario is real and valuable?
4. What content and data does each task rely on, and how sensitive is it?
5. How would the person doing the task check that Copilot's output is right?

## Required inputs

- The audience in scope from `copilot-adoption:adoption-readiness`, described by role, not by name.
- Access to business owners and a small number of people who do each role.
- The organisation's approved-use guidance and data classification.
- What Copilot capabilities the organisation has approved for each persona, confirmed with IT.

If a persona has no business owner willing to validate scenarios, mark its scenarios unvalidated and do not prioritise
them. Never assume that a capability is available to a persona; confirm it.

## Decision framework

Segment first, then score each scenario. Personas are defined by ways of working, not seniority.

| Persona | Typical traits | Scenario emphasis |
|---|---|---|
| Desk | Long periods in documents, email, meetings and data | Drafting, summarising, analysis, meeting follow-up |
| Hybrid | Mixes meetings, travel and focused work across devices | Catch-up, preparation, follow-up actions |
| Frontline | Short device sessions, shift work, shared or mobile devices | Quick answers, procedures, handover notes, plain-language rewrites |

Score each scenario from 1 to 3 on each criterion:

| Criterion | 3 means |
|---|---|
| Frequency | Done weekly or more by most of the persona |
| Value | Saves meaningful time, improves quality or reduces delay the owner cares about |
| Verifiability | The person can quickly check the output against something they know |
| Data safety | Uses content the person already handles, with no special category data |

Prioritise scenarios scoring 10 or more with Verifiability and Data safety both at least 2. A scenario with low
verifiability is not a starting scenario, however valuable. Data safety of 1 sends the scenario to `security-privacy`
before it is published.

## Practitioner approach

Begin by grouping the audience into a small number of personas based on how people actually work. Three to six is
usually enough; more than that and nobody can maintain the catalogue. Describe each persona in a paragraph: where they
work, which devices they use, what a typical day looks like and what frustrates them. Frontline personas need special
care because their sessions are short and their devices may be shared, which changes both the scenarios and the
guidance.

Then run short discovery conversations with each business owner and two or three people who do the work. Ask them to
walk through last week rather than imagine the future: what took longest, what was repetitive, what was late, and what
they would hand to a capable colleague if they had one. Capture tasks in the user's language. Avoid showing product
demonstrations first, because they anchor people on features and you lose the real work.

For each candidate task, write the scenario as a short statement: who, what task, what input, what good output looks
like and how they would check it. Then draft a prompt pattern: a reusable structure the person fills in, such as goal,
context, source material, format and the check to apply. Prompt patterns beat fixed prompts because they transfer
across slightly different situations. Test each pattern with a real user on real but non-sensitive work, and note where
Copilot struggles.

Score scenarios with the framework and agree the ranking with the business owner. Keep the starting set small: three to
five scenarios per persona that are frequent, valuable and easy to verify. Record the rest as a backlog to release later
as confidence grows. Where a scenario keeps reappearing across teams and needs shared knowledge or actions in other
systems, it has outgrown individual use; route it to `opportunity-management:problem-framing`.

Every scenario in the catalogue must include a verification step. Copilot output is a draft for the person to check,
and the catalogue should model that habit in every entry. Name the content the scenario relies on and flag where that
content is out of date or poorly owned.

Treat Champions as a standing discovery channel. Envisioning workshops they run with teams surface candidate
scenarios, and prompt libraries and departmental playbooks from Champion Challenges are ready-made entries. Put every
contribution through the same scoring, real-user test and verification step as any other scenario, and record its
source so the programme can see how much the network adds.

Finally, give each scenario an owner who will keep it current, and set a review date. Catalogues that are not
maintained fill with prompts that no longer work and examples nobody recognises.

## Outputs

- A persona summary and a prioritised scenario catalogue on the `scenario-catalogue` template: persona, scenario, prompt pattern, verification step, score, owner and review date.
- A starting set of three to five scenarios per persona for onboarding.
- A backlog of lower-priority scenarios and a list of candidates referred to opportunity intake.
- A record of scenarios contributed through Champion Challenges and workshops, with their review outcome.

## Microsoft platform considerations

Scenarios differ between Copilot Chat, Copilot in the Microsoft 365 apps and Copilot Cowork, and between devices.
Confirm with IT which experiences each persona actually has before writing scenarios that rely on them. Capability and
naming change frequently; check `references/sources.md` and avoid writing scenarios that depend on a feature you have
not seen working in the organisation's tenant.

## Adoption considerations

Scenarios are the backbone of onboarding, Champion activity and manager conversations. Publish them where people work,
let Champions contribute new ones through a light review, and retire scenarios that nobody uses.

## Knowledge considerations

Many scenarios depend on finding the right document or policy. Where a scenario fails because content is stale,
duplicated or unowned, record the gap and pass it to `knowledge-management:knowledge-cleanup` rather than
working around it in the prompt.

## Security and privacy considerations

Do not publish scenarios that encourage people to paste special category or highly confidential data into prompts.
Scenarios that rely on broad searches across shared content should be checked against the oversharing findings from
readiness.

## Responsible AI considerations

Exclude scenarios where Copilot output would directly decide something about a person, such as performance, hiring or
eligibility, unless a responsible AI review has approved the use. Every published scenario states that the person
remains accountable for the result.

## Evaluation requirements

Each priority scenario is tested by at least one real user on real but non-sensitive work before publication, with the
verification step confirmed as practical. Record what good output looks like so later changes in behaviour can be
noticed.

## Value measures

For each priority scenario, record a baseline the business owner accepts (typical time, delay or rework), the expected
change and how it will be sampled, through short team-level surveys or time studies. Measures are reported by persona
or team, never by individual.

## Scale notes

### Starter

One persona or two, a handful of scenarios each, discovered in a single workshop with the owner and a few staff. Keep
the catalogue as a shared page.

### Scale

Run discovery per business unit with a shared template and scoring, and let Champions propose additions. Publish a
central catalogue filtered by persona.

### Enterprise

Maintain a governed catalogue with owners per function, regular review cycles and localisation where needed. Use
scenario-level measures to direct investment and to feed the opportunity portfolio.

## Hand-offs

- To `copilot-adoption:launch-plan` with the starting scenarios for each persona.
- To `copilot-adoption:adoption-measurement` with the scenario baselines.
- To `champions:champion-challenges` for scenarios that would make good workshops, prompt libraries or playbooks.
- To `opportunity-management:problem-framing` for scenarios that have outgrown individual use.

## Reviewer gates

From risk tier 1, `security-privacy` reviews any scenario scoring 1 on data safety, or relying on broad searches across
shared content, before publication. They look for inappropriate data in prompts and exposure through overshared
locations.

## Failure modes

- Scenarios are written from product demonstrations and match nobody's real work, so the catalogue is ignored.
- Too many personas and scenarios are created, nobody maintains them, and prompts stop working.
- Scenarios omit a verification step, and people learn to trust output they should have checked.
- Frontline workers receive desk-based scenarios that assume long sessions and personal devices.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Publish a scenario without a verification step and an owner.
- Define personas by seniority, personal characteristics or individual usage data.
- Encourage pasting sensitive or special category data into prompts.
- Write scenarios that rely on features nobody has confirmed are available to that persona.

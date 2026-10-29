---
name: ai-support-model
description: Designs the support model for live agents and AI solutions - support tiers from service desk to solution owner, knowledge owners, makers and platform team, AI-specific triage categories, response expectations by risk tier, runbooks and the handover from build to run - so every live solution has someone who answers and someone who fixes. Use when a solution is about to go live, or when issues bounce between teams with no owner.
license: CC-BY-4.0
metadata:
  department: ai-operations
  lifecycle: Launch, Measure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, copilot-cowork, ai-foundry, power-platform
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-copilot-studio-guidance, ms-coe-starter-kit, ms-managed-environments, ms-copilot-studio-zoned-governance, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI support model

## Purpose

Every live AI solution will at some point give a wrong answer, fail an action, lose access to its knowledge or confuse
its users. This skill designs who users turn to when that happens, how issues are triaged into causes that someone can
actually fix, how quickly each tier of solution must be dealt with, and how ownership passes from the people who built
the solution to the people who run it. Support models usually fail because the service desk does not know the solution
exists, because "the agent is wrong" is logged as an IT fault when the fix belongs to a knowledge owner, or because the
maker who built it has moved on and nobody else understands it.

## When to use

- A solution is about to go live and its support route is "contact the maker".
- Several agents and AI solutions are live and support arrangements differ for each.
- Issues bounce between the service desk, the platform team and the business with no one fixing them.
- A maker or solution owner is leaving and support must transfer.
- The release gate asks for a support plan that matches the risk tier.

## When not to use

- Helping people use Copilot in general through self-help, Champions and the service desk - use `copilot-adoption:adoption-support-model`.
- Detecting problems through signals and alerts - use `ai-operations:ai-solution-monitoring`.
- Handling a serious failure or harm once it occurs - use `ai-operations:ai-incident-management`.
- Reviewing whether a design is supportable before build - use `design-authority:supportability-review`.
- Naming owners across the whole AI estate - use `organisation-tailoring:ownership-map`.

## Questions to ask first

1. Who owns this solution's outcomes, and who can change its instructions, knowledge, actions and configuration?
2. Where do users already go for help, and does that route know the solution exists?
3. What happens to users and to the business if the solution is wrong or unavailable for an hour, a day or a week?
4. Which issue types can the service desk resolve, and which need a knowledge owner, maker or engineer?
5. What happens to support when the maker or owner leaves?

## Required inputs

- The solution brief with risk tier, audience, owners and dependencies.
- The organisation's existing service management process and categories, and the service desk's capacity.
- Named roles for business owner, solution owner, knowledge owners and technical support, from `organisation-tailoring:ownership-map` where it exists.
- Known limits and frequently asked questions from testing.

Where a role has no named holder, record the gap as "to confirm" on the plan and do not mark the solution ready to
release from tier 2. Never put an individual's name in the plan as a substitute for a role that has not been agreed.

## Decision framework

Design four support levels and route by cause, not by symptom.

| Level | Role | Handles |
|---|---|---|
| 0 Self-help | Users, with known limits and FAQs | How-to questions, expected refusals, where to go instead |
| 1 First line | Service desk, Champions where agreed | Access, availability, logging and categorising issues, known fixes |
| 2 Solution | Solution owner, knowledge owners, maker | Wrong or ungrounded answers, outdated knowledge, instruction and scope issues |
| 3 Platform and engineering | Platform team, engineers, Microsoft support through the agreed route | Connector, environment, licensing assignment, model or service faults |

Triage categories every support route should use:

| Category | Usually fixed by |
|---|---|
| Wrong or unsupported answer | Knowledge owner, then maker |
| Out-of-date answer | Knowledge owner, through `ai-operations:knowledge-refresh` |
| Should have refused or redirected | Maker, with regression run |
| Action failed or acted wrongly | Maker or engineer; may be an incident |
| Cannot access the solution or its knowledge | Service desk or platform team |
| Harmful, offensive or exposing output | Incident route, immediately |

Response expectations scale with tier. The figures are for the organisation to set and record as `[To confirm]` in the
plan; the pattern is that tier 1 relies on the owner within working days, tier 2 uses the service desk with agreed
targets, and tiers 3 and 4 add out-of-hours cover and incident response where the business impact demands it.

## Practitioner approach

Start with the user's first question: where do I go when this is wrong? Put the answer inside the solution, in its
welcome message or description, and make sure the service desk can find the solution in its catalogue. A support route
users cannot see does not exist.

Name roles, then holders. For each solution, record the business owner who answers for outcomes, the solution owner who
runs it day to day, the knowledge owners for each source, and the technical owner who can change configuration. Check
that each holder has the access and time to act. A solution owner who cannot edit the agent's knowledge is not an owner.

Build triage around causes. Most AI issues arrive as "the answer was wrong". Give first line a short script: capture the
question, the answer, the time, and whether citations were shown; check the known limits; categorise by the table; route
to the right owner. Train the service desk with real examples from testing, and give them a way to see whether an issue
is already known.

Write a short runbook for each solution: what it does, its knowledge sources and owners, its actions and connections,
known limits, how to switch it off or restrict it, how to roll back a change, and who to call. Keep it with the solution
record, not in the maker's personal storage.

Set response expectations by tier with the business owner and the service desk, and record them. Do not promise targets
the service desk cannot meet; it is better to state working-day response for a tier 1 agent honestly than to imply
round-the-clock cover.

Plan the handover from build to run before go-live. Hold a session where the maker walks the solution owner and first
line through the runbook and common issues, and agree a short period of joint support. Record the date when support
formally passes.

Plan for people leaving. Require at least two people with the access and knowledge to change each tier 2 or higher
solution, and make ownership transfer a step in leaver processes. Solutions with no owner go to the review calendar for
a continue-or-retire decision.

Close the loop with improvement. Support data, aggregated by category and solution, feeds `ai-operations:ai-feedback-loop`
and the review calendar. Report it at solution and team level only.

## Outputs

- A support and monitoring plan on the `support-and-monitoring-plan` template: roles and holders, support levels, triage categories, response expectations by tier, runbook location and handover record.
- A first-line triage script and known-issues list for the service desk.
- A solution runbook stored with the solution record.
- A support route message for users, placed in the solution itself.

## Microsoft platform considerations

Who can edit, share and administer an agent depends on the route and environment: Agent Builder agents, Copilot Studio
agents in Power Platform environments and Microsoft Foundry solutions each have different ownership and co-owner
settings. Confirm them in `ms-copilot-studio-guidance` and `ms-managed-environments`, use environment zoning as described
in `ms-copilot-studio-zoned-governance`, and consider inventory tooling such as `ms-coe-starter-kit` to find solutions
without active owners. Use the organisation's agreed Microsoft support route for platform faults.

## Adoption considerations

Users trust solutions that are visibly looked after. Publish the support route at launch, show fixes when they happen,
and give Champions a clear role in first-line help only where they have agreed to it.

## Knowledge considerations

Many support issues are knowledge issues. Make knowledge owners part of level 2 by design, with a route through
`ai-operations:knowledge-refresh`, so wrong answers are fixed at source rather than patched in instructions.

## Security and privacy considerations

Support staff may see users' questions and answers when diagnosing issues. Limit that access to what diagnosis needs,
agree it with the `security-privacy` reviewers, and route any exposure of restricted content straight to incident handling.

## Responsible AI considerations

Where a solution affects decisions about people, the support model must include a route for affected people to
challenge an outcome, coordinated with `responsible-ai:escalation-and-appeal`. Harmful outputs always go to the incident route.

## Evaluation requirements

Support categories feed evaluation. Issues categorised as wrong or unsupported answers should become new items in the
golden dataset through `evaluation-quality:golden-dataset`, so the regression set learns from live use.

## Value measures

Track issue volume by category per solution, time to resolution against agreed expectations, the share resolved at first
line, and solutions with a complete set of named roles. The AI Operations Lead owns these measures; report by solution
and team, never by individual user or support agent.

## Scale notes

### Starter

For a handful of tier 1 agents, the business owner and maker are the support route, published in each agent with a
one-page runbook and a named backup.

### Scale

Bring AI solutions into the service desk catalogue with shared triage categories, a standard runbook and support plan
per solution, and agreed targets for tier 2.

### Enterprise

A federated model in which business-unit owners support their solutions under shared categories and targets, with a
central operations team for platform issues, out-of-hours cover for tier 3 and 4, and support data reported across the
portfolio.

## Hand-offs

- To `ai-operations:ai-solution-monitoring` to set the signals that alert the support route.
- To `ai-operations:ai-incident-management` for serious failures and harms.
- To `ai-operations:ai-review-calendar` to schedule reviews, including ownership checks.
- To `m365-agents:agent-release-readiness` with the support plan as release evidence.

## Reviewer gates

From risk tier 2, `design-authority` may test the support plan through `design-authority:supportability-review`, looking
for named roles, sustainable cover and a runbook. A solution without a named owner and fix route does not pass the
release gate.

## Failure modes

- The maker is the only person who can change the solution, and support stops when they move on.
- The service desk logs wrong answers as IT faults and closes them without involving the knowledge owner.
- Response targets are promised that nobody has resourced, and tier 3 issues wait over a weekend.
- The support route is documented but never shown to users, so problems go unreported.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Release a tier 2 or higher solution whose only support route is the person who built it.
- Report support data by individual user or support agent.
- Promise response targets the support teams have not agreed and resourced.
- Route harmful or exposing outputs through normal fault queues instead of incident handling.

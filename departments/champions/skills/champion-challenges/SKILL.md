---
name: champion-challenges
description: Designs practical Champion Challenges in which a verified Champion solves a real team problem using safe, approved tools, producing reusable assets such as prompt patterns or guides, and routing any larger opportunity to intake. Use when Champions are ready to apply their capability, when the community needs fresh practical work, or when a challenge idea needs checking for safety and scope.
license: CC-BY-4.0
metadata:
  department: champions
  lifecycle: Enable, Deliver, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, copilot-cowork, m365-agents
  edition-support: scale, enterprise
  reviewers: security-privacy
  sources: ms-champion-programme, ms-copilot-adoption-hub, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Champion challenges

## Purpose

A Champion Challenge turns verified capability into contribution: a Champion takes a real problem from their team,
improves it with safe, approved tools, and leaves behind something others can reuse. This skill designs the challenge
format, the catalogue of challenges, the safety and scope rules, and the route for bigger ideas. Challenges usually go
wrong when they become hackathons that build ungoverned agents, when they solve invented problems, or when the useful
output stays in one person's head.

## When to use

- Champions have verified capability and need a practical next step.
- The community is losing energy and needs real work to focus on.
- A team has a recurring problem that might be improved with approved tools.
- A proposed challenge needs checking for safety, scope and fit before it starts.

## When not to use

- Designing the programme and its boundaries - use `champions:champion-programme-design`.
- Defining capability levels and evidence - use `champions:capability-framework`.
- Framing a significant opportunity that needs a business case or delivery team - use `opportunity-management:problem-framing`.
- Deciding whether a problem needs an agent, automation or a built solution - use `opportunity-management:ai-suitability`.
- Recognising completed challenges - use `champions:recognition-and-progression`.

## Questions to ask first

1. What real, recurring problem does the team have, and who in the team owns it?
2. Which approved tools may the Champion use, and does the problem need anything beyond them?
3. What data and content would the challenge touch, and how sensitive is it?
4. What reusable asset would show the challenge worked?
5. How much time has the Champion's manager agreed for the challenge?

## Required inputs

- A Champion verified at the level the challenge needs, from `champions:evidence-assessment`.
- A problem statement agreed with the team owner, in a few sentences.
- The approved tools list and approved-use guidance.
- Manager agreement to the time involved.

If the problem has no owner, it is not a challenge yet. If it needs tools beyond the approved list, external access or
data above the agreed sensitivity, it is not a challenge at all; route it to intake.

## Decision framework

Every challenge passes a scope and safety check before it starts.

| Check | A challenge must | If not |
|---|---|---|
| Real problem | Address a recurring issue a named team owner confirms | Find a real problem or drop it |
| Approved tools | Use only tools approved for the Champion's level | Route to `opportunity-management:problem-framing` |
| Data safety | Use content the team already handles, with no special category or client-confidential data | Route to intake with a `security-privacy` review |
| Audience | Stay within the team or community; nothing externally facing | Route to intake |
| Size | Be completable in a few weeks within the agreed time | Split it, or route the larger part to intake |
| Reusable output | Produce an asset others can reuse | Redesign the challenge |

Typical challenge types, matched to capability level:

| Level | Challenge type | Reusable asset |
|---|---|---|
| Chat | Improve a team's recurring writing or summarising task | Prompt pattern with a verification step |
| Productivity | Redesign a recurring team workflow using Copilot in daily apps | Short guide, before-and-after account, scenario for the catalogue |
| Agent | Evaluate an approved agent for the team, or build a governed one where approved | Evaluation notes, or an agent with owner, tests and intake record |

## Practitioner approach

Start from the team's work, not the tool. Ask Champions to bring a problem that genuinely annoys their team: a weekly
report that takes too long, a handover that loses information, meeting notes nobody reads. Agree the problem with the
team owner in a few sentences, including how they would know it had improved. A challenge without an owner tends to
solve something nobody needed solved.

Run the scope and safety check before any work starts, ideally with the programme owner. This is where challenges are
kept within the Champion boundary. Most proposals pass easily. Those that do not are not rejected; they are routed.
A challenge that would need new connectors, external access, sensitive data or a solution used beyond the team becomes
an opportunity, and goes to `opportunity-management:problem-framing` through the CoE, with the Champion credited as the
person who found it.

Keep challenges small and time-boxed. A few weeks within the agreed Champion time is enough for a Chat or productivity
challenge. Give each Champion a light check-in midway, from the programme owner or a more experienced Champion, to
unblock rather than inspect.

Insist on a reusable asset. The value of a challenge is that the next team does not have to start from scratch. Assets
should be short, practical and safe to share: a prompt pattern with its verification step, a one-page guide, a
scenario for the catalogue, or evaluation notes on an agent. Review each asset before publication for sensitive data
and accuracy, then add it to the scenario catalogue or community library with an owner and review date.

At the agent level, be especially careful. Where the organisation allows Champions to build agents, the challenge must
follow the same governance as any other agent: a named owner, knowledge that is owned and current, test questions with
expected answers, and an intake record. Where it does not, the challenge is to evaluate an approved agent for the
team's needs and report what worked and what did not.

Close each challenge with a short write-up: problem, approach, asset, result against the owner's measure, and what
others should know. Showcase good challenges in community calls and to the sponsor. Collect challenges into a
catalogue so Champions can pick from proven ideas as well as bring their own.

## Outputs

- A Champion Challenge catalogue on the `champion-challenge-catalogue` template: challenge, level, problem owner, tools, data class, reusable asset and status.
- A scope and safety check record for each challenge.
- A challenge write-up and a reusable asset for each completed challenge.
- Opportunity referrals to `opportunity-management:problem-framing` for anything outside the challenge scope.

## Microsoft platform considerations

Challenges use only the Copilot experiences and agent tools approved for the Champion's level, such as Copilot Chat,
Copilot in the Microsoft 365 apps, Copilot Cowork or approved agent building tools. Where agent building is allowed,
the organisation's environment and data policy controls apply. Availability and naming change; check
`references/sources.md` and the approved tools list.

## Adoption considerations

Challenges create the local success stories that persuade sceptical colleagues more than central messages. Feed
completed challenges into the scenario catalogue and launch reinforcement.

## Knowledge considerations

Many challenges depend on team knowledge. Where a challenge shows that content is stale or unowned, record it and pass
it to the content owner or the `knowledge-management` department (planned) rather than building on poor content.

## Security and privacy considerations

The data safety check is mandatory. Challenges must not use special category, client-confidential or highly sensitive
data, and assets must be reviewed for sensitive content before sharing. Anything that would widen access to content
goes to intake with a `security-privacy` review.

## Responsible AI considerations

Challenges must not automate decisions about people, money or safety. If a team problem touches those areas, it is
routed to intake for risk classification rather than tackled as a challenge.

## Evaluation requirements

Each challenge measures its result against the owner's stated measure. Agent-level challenges include test questions
with expected answers and a record of how the agent performed against them.

## Value measures

Programme-level measures, owned by the programme owner: challenges started and completed, assets published and reused,
opportunities routed to intake and owner-reported results. Reported in aggregate, never as individual league tables.

## Scale notes

### Starter

Usually omitted at this size; where a small organisation wants challenges, keep them informal and limited to the Chat
and productivity levels, checked by the owner.

### Scale

A small catalogue of proven challenges, a scope and safety check by the programme owner, and quarterly showcases.

### Enterprise

A curated catalogue by function, a standing review of assets, agent-level challenges under formal governance, and
regular reporting of routed opportunities to the CoE portfolio.

## Hand-offs

- To `opportunity-management:problem-framing` for problems outside challenge scope.
- To `ai-centre-of-excellence:coe-operating-model` so routed opportunities and reusable assets reach CoE governance.
- To `champions:recognition-and-progression` when a challenge is completed.
- To `copilot-adoption:scenario-discovery` to add new scenarios to the catalogue.

## Reviewer gates

From risk tier 1, `security-privacy` reviews any challenge that touches content beyond the team's own working material
or produces an agent shared with others, looking for data exposure and appropriate access. Agent-level challenges also
pass CoE intake.

## Failure modes

- Challenges become hackathons that produce ungoverned agents with no owner.
- Problems are invented for the challenge, so nothing useful changes in the team.
- Assets are not reviewed, and a shared prompt pattern includes confidential examples.
- Larger opportunities are tackled as challenges instead of being routed, and stall half-built.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Start a challenge that uses unapproved tools, sensitive data or an external audience.
- Let a challenge release an agent or solution without an owner and intake record.
- Treat a routed opportunity as a failed challenge.
- Publish an asset without checking it for sensitive content.

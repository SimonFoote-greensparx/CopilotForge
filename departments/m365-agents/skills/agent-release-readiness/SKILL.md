---
name: agent-release-readiness
description: Runs the release gate for an agent, confirming owner, support route, sharing scope matched to risk tier, reviewer evidence, communications, monitoring, review date and retirement criteria, and registers the agent in the solution register. Use when an agent has passed testing and someone wants to share it, when its audience is about to widen, or when a live agent has no clear owner.
license: CC-BY-4.0
metadata:
  department: m365-agents
  lifecycle: Assure, Launch, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, power-platform
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, evaluation-quality, responsible-ai, design-authority
  sources: ms-copilot-studio-zoned-governance, ms-copilot-studio-security-governance, ms-managed-environments, ms-agent-builder, ms-coe-starter-kit, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# Agent release readiness

## Purpose

Sharing an agent is easy; running one is not. This skill is the release gate that confirms an agent has an owner, a
support route, a sharing scope that matches its risk tier, the reviewer evidence its tier requires, communications,
monitoring, a review date and the criteria for retiring it, and that it is recorded in the solution register. Releases
usually go wrong when the share button is the release process: the agent reaches far more people than intended, nobody
answers when it is wrong, and a year later nobody knows who built it or whether it is still used.

## When to use

- An agent has passed testing and the owner wants to share it with its intended audience.
- An agent's audience is about to widen, for example from a team to a business unit.
- A live agent has no clear owner, support route or review date.
- A periodic review asks whether an agent should continue, change or retire.

## When not to use

- Designing the agent's scope and ownership in the first place - use `m365-agents:agent-use-case-design`.
- Producing the test evidence and evaluation results - use `m365-agents:agent-testing`.
- Reviewing data exposure, connectors or privacy as the reviewer - use `security-privacy:data-exposure-review`, `security-privacy:connector-review` or `security-privacy:privacy-assessment`.
- Deciding whether to scale, continue or stop an agent on value evidence - use `opportunity-management:scale-or-stop`.
- Running monitoring, incidents and retirement day to day - use `ai-operations:ai-solution-monitoring`.

## Questions to ask first

1. Who is the named business owner, and have they accepted accountability for the agent's answers and outcomes?
2. Who exactly will the agent be shared with, and does that match the audience in the brief and the risk tier?
3. Which reviewer gates apply at this tier, and is their evidence complete with no open blocking findings?
4. Where do users go when the agent is wrong, and who fixes it?
5. When will the agent next be reviewed, and what would cause it to be retired?

## Required inputs

- The agent brief, with owner, audience, risk tier and success measures.
- The test evidence and the business owner's decision against the agreed threshold.
- Reviewer outcomes for the tier, with any blocking findings and their resolution.
- The organisation's sharing rules by risk tier and governance zone, and access to the solution register.

Where any required reviewer evidence is missing, the gate result is "not ready". Never infer a pass from the absence of
an objection, and never release on the promise that a reviewer will look later.

## Decision framework

Check each line; every line must pass for the tier before release.

| Check | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Named business owner and knowledge owners | Required | Required | Required | Required, with executive sponsor |
| Support route and fix owner | Owner contact | Service desk route | Service desk with response targets | Plus incident response and escalation |
| Sharing scope | Named team | Named groups matching brief | Named groups; no organisation-wide sharing without design review | Formally approved audience |
| Test evidence | Owner sign-off | Threshold met, permission tests | Plus `evaluation-quality:ai-release-evidence` | Plus independent assurance |
| Reviewer evidence | Not mandatory | `security-privacy` | Plus `responsible-ai:ai-impact-assessment` and `design-authority:ai-design-review` | Plus executive risk acceptance |
| Communications | Owner tells the team | Audience brief with limits | Plus manager briefing | Plus external transparency where relevant |
| Monitoring and review date | Review date | Usage and feedback, quarterly review | Plus quality monitoring and continuity | Plus human oversight records |
| Retirement criteria | Recorded | Recorded | Recorded with data disposal | Recorded with exit plan |
| Solution register entry | Required | Required | Required | Required |

An open blocking finding from any reviewer stops release, whatever the date. Disagreement with a finding escalates to
the accountable executive for written risk acceptance; it is not settled by the maker or the agent owner.

## Practitioner approach

Start by confirming the tier, because everything else scales from it. Check the tier on the brief against how the agent
actually behaves now: if testing revealed actions, wider knowledge or a broader audience than planned, re-run
`opportunity-management:risk-classification` before going further. Releasing a tier 2 agent under tier 1 rules is the
most common route to an incident.

Confirm ownership in person. The business owner should be able to say what the agent is for, who it serves, what it must
not do and what they will do when it is wrong. If they cannot, the agent is not ready, however good the test results.
Record the knowledge owners and the maker separately; the maker is rarely the right long-term owner.

Match sharing to the tier and the brief. Compare the planned sharing settings with the intended audience, group by
group. Organisation-wide sharing is a design decision that needs a reason, not a default. Check whether the route and
environment apply sharing limits for the governance zone, using the current source records rather than assumptions.

Collect reviewer evidence and read it. Confirm that every blocking finding is closed with evidence of the fix, that
advisory findings have an owner and a date, and that any risk acceptance is signed by the accountable executive. A
reviewer's verbal "it's probably fine" is not evidence.

Plan the support route as a user would experience it. Write down where a user reports a wrong answer, who triages it,
and how a knowledge or instruction fix is made and re-tested. Link that route from the agent's description or welcome
message.

Prepare communications with the owner: what the agent does, what it does not do, where its answers come from, how to
report a problem, and that users remain responsible for checking outputs. Known limits from testing belong in the
message.

Set monitoring and a review date. At minimum, track usage at audience level, feedback and reported failures. Agree the
retirement criteria now (for example, no use for a set period, owner leaves without successor, or knowledge no longer
maintained) so retirement is a routine decision later rather than an argument.

Finally, register the agent in the solution register with owner, audience, tier, sources, actions, reviewer outcomes,
review date and retirement criteria. An agent that is not in the register is, for governance purposes, ungoverned.

## Outputs

- A completed `agent-release-checklist` with a release decision of ready, ready with conditions or not ready, signed by the business owner.
- A solution register entry for the agent.
- A user-facing launch message and support route.
- A review date and retirement criteria, handed to operations.

## Microsoft platform considerations

Sharing controls, environment routing, governance zones and Managed Environments features determine who can share an
agent and with whom, and they differ by route. The CoE Starter Kit and admin tooling can help maintain an inventory.
Check current controls and limits in the source records (`ms-copilot-studio-zoned-governance`, `ms-managed-environments`,
`ms-copilot-studio-security-governance`, `ms-agent-builder`) before relying on them.

## Adoption considerations

Release is the start of adoption, not the end of delivery. Plan how the intended audience will hear about the agent,
through managers and Champions where they exist, and track adoption at team or role level against the success measures.

## Knowledge considerations

The review date must be linked to the knowledge owners' review cycles. A change to a policy or source should prompt a
regression run and, if needed, a release update.

## Security and privacy considerations

From risk tier 2, release requires closed `security-privacy` findings. Check that sharing settings match the scope the
reviewer approved, because widening sharing after review invalidates the review.

## Responsible AI considerations

From risk tier 3, release requires the outcome of `responsible-ai:ai-impact-assessment`, including human oversight
arrangements. Users must be told they are using an agent and that they remain accountable for what they do with its output.

## Evaluation requirements

Release requires the test evidence from `m365-agents:agent-testing` with the threshold agreed before results were
seen, and a regression pack ready for the first change after release.

## Value measures

Carry the success measures and baselines from the brief into the register, with the owner and the review date.
Report usage and outcomes by audience group above the agreed minimum group size; never by individual.

## Scale notes

### Starter

A one-page checklist signed by the owner, with a named support contact, a review date and a register entry, even if the
register is a simple list. Most early agents are tier 1 and should stay with a named team.

### Scale

Run the release gate in the CoE cadence with the full checklist, environment-based sharing controls and a maintained
solution register. Reviewer evidence is attached, not summarised.

### Enterprise

Federate tier 1 and 2 release decisions to business-unit spokes under shared rules, with the hub and reviewers deciding
tier 3 and 4. Link the register to the portfolio and to operations for monitoring and retirement.

## Hand-offs

- To `ai-operations:ai-solution-monitoring` for monitoring, incidents, review and retirement.
- To `opportunity-management:scale-or-stop` at the review date.
- To `copilot-adoption:launch-plan` where the agent is part of a wider adoption launch.
- Back to `m365-agents:agent-testing` for regression after any post-release change.

## Reviewer gates

From risk tier 2, `security-privacy` and `evaluation-quality:ai-release-evidence` must pass the agent; from tier 3,
`responsible-ai:ai-impact-assessment` and `design-authority:ai-design-review` as well. Blocking findings stop release
and are not traded against dates. Each reviewer records its questions and the responses on the checklist.

## Failure modes

- Sharing is widened after review, so the agent reaches an audience the reviewers never considered.
- The maker remains the owner, changes role, and nobody answers user reports.
- No retirement criteria are recorded, so unused agents accumulate with stale knowledge.
- A deadline drives release with an open blocking finding "to be fixed next sprint".

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Release an agent with an open blocking finding, or trade a finding against a launch date.
- Share an agent wider than its brief and risk tier allow.
- Release without a named business owner, a support route and a review date.
- Leave a released agent out of the solution register.

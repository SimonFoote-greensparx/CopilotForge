---
name: benefit-owner
description: Assigns an accountable business owner role to every benefit, agrees what ownership means - influencing the change, signing off baseline and target, deciding how released capacity is used, reporting and escalating - and sets up the support, hand-over and escalation owners need. Use when benefits sit with IT or the CoE, when an owner has moved role, or when owners have signed up to benefits they cannot influence.
license: CC-BY-4.0
metadata:
  department: value-realisation
  lifecycle: Mobilise, Deliver, Measure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, iso-iec-42001, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Benefit owner

## Purpose

Benefits are realised by business decisions, not by technology teams. This skill places each benefit with a business
owner role that can actually influence it, agrees in writing what that ownership involves, and gives owners the support
they need to carry it: data, a measurement partner, a review rhythm and an escalation route. It goes wrong when IT or
the CoE is held accountable for business outcomes it cannot change, when the most senior person available is named
regardless of influence, and when an owner moves role and the benefit quietly becomes nobody's.

## When to use

- Benefits are entering the register and need accountable owners.
- IT or the CoE is being asked to report or answer for business benefits.
- An owner has moved on and their benefits have no successor.
- Owners have accepted benefits they cannot influence and reviews keep stalling.
- Released capacity is not being redeployed because nobody has authority to decide its use.

## When not to use

- Mapping accountable roles across the whole transformation pack - use `organisation-tailoring:ownership-map`.
- Building the RACI for AI work across the lifecycle - use `ai-centre-of-excellence:coe-raci`.
- Securing and equipping the programme's executive sponsor - use `ai-strategy:executive-sponsorship`.
- Writing the benefit statements themselves - use `value-realisation:benefit-hypothesis`.
- Naming the owner of an agent's instructions and knowledge - use `m365-agents:agent-use-case-design`.

## Questions to ask first

1. Which role controls the process, budget or team where the benefit will appear?
2. What decisions will realising the benefit require (redeploying time, changing a process, retiring a tool), and does this role have authority to take them?
3. Does the proposed owner understand and accept the benefit as written, including its range and timing?
4. What support will the owner need to measure and report, and who provides it?
5. What happens to the benefit if the owner changes role?

## Required inputs

- Registered benefit statements with their dependency maps, from `value-realisation:benefit-hypothesis`.
- The organisation's declared roles and any named owners already agreed, from `organisation-tailoring:ownership-map`.
- The programme's governance forums and escalation route.

Use declared roles only. Where no suitable role has been declared, record the gap as `[To confirm: owner role]` and
escalate it to the sponsor rather than assigning a benefit to whoever is in the room.

## Decision framework

Test each proposed owner before the benefit is accepted.

| Test | The proposed owner passes when they |
|---|---|
| Influence | Control the process, team or budget where the benefit appears |
| Authority | Can take, or directly secure, the decisions realisation needs |
| Acceptance | Have read and accepted the benefit statement, range and timing |
| Capacity | Have time agreed for reviews and reporting |
| Continuity | Have a named deputy role and a hand-over rule |

| Situation | Ownership approach |
|---|---|
| Benefit sits in one team | The head of that team owns it |
| Benefit spans several teams in one function | The function head owns it; team heads own contributing measures |
| Benefit spans functions | One accountable owner at the level where the functions meet, with contributing owners named |
| Benefit is organisational capability | The CoE lead owns it, because the CoE controls the capability |
| No role passes the tests | The benefit is marked at risk and escalated to the sponsor |

What owners are accountable for, and what they are not:

| Owners are accountable for | Owners are supported by, not accountable for |
|---|---|
| Accepting the benefit, baseline and target | Building and running the solution (solution owner) |
| Taking or securing the enabling decisions | Collecting and analysing data (Benefits Realisation Lead) |
| Reporting progress and variance at reviews | Adoption programme delivery (adoption lead) |
| Escalating when realisation is at risk | Platform and governance (IT and CoE) |

## Practitioner approach

Start with where the benefit lands, not with who sponsored the idea. A drafting agent built at the request of a
director may deliver its benefit in a team managed three levels below. The owner is whoever runs that team's work and
can decide what happens with released time, because that decision is usually where realisation succeeds or fails.

Meet the proposed owner and walk through the benefit statement together: the measure, the baseline, the range, the
timing and the enabling changes. Ask directly whether they believe it and whether they can make the required decisions.
An owner who says "yes" to avoid conflict will be absent at the first review. If they doubt the figure, revise it with
them now; an owned smaller benefit is worth more than an unowned larger one.

Write the ownership down in a short agreement on the register entry: what is owned, what decisions the owner will take
and by when, how often they will review progress, and who supports them. Keep it to half a page. The aim is clarity,
not a contract.

Separate business accountability from technical ownership explicitly. The solution owner keeps the agent or automation
working; the benefit owner makes sure the organisation uses it to change the work. When IT or the CoE is being held to
account for a business benefit, use this distinction to move the accountability to where it belongs, while keeping
the CoE accountable for capability benefits it does control.

Support owners properly. Most are busy operational managers, not measurement specialists. Give each one a measurement
partner from the Benefits Realisation Lead's team or the CoE, a pre-filled review pack, and a clear point of escalation.
Owners who are left to produce their own figures stop reporting.

Plan for change. Roles change more often than benefits are realised. Name a deputy role for every owner, and make
hand-over of benefits a step in the organisation's existing role-change process where possible. When an owner leaves,
the deputy confirms acceptance within a set period or the benefit is escalated.

Never use benefit ownership to judge individual performance. Owners report on benefits, not on their staff's AI usage,
and missed benefits trigger a conversation about causes and support, not blame.

## Outputs

- A named owner role, deputy role and short ownership agreement for each benefit, recorded in the `benefits-register`.
- A list of contributing owners for cross-team benefits.
- An escalation list of benefits with no owner passing the tests.
- An owner support plan: measurement partner, review pack and escalation route.

## Microsoft platform considerations

Not applicable to ownership decisions, which are about business roles rather than platform configuration. Where the
register is kept in a Microsoft list or app, restrict editing of ownership fields to the Benefits Realisation Lead and
owners.

## Adoption considerations

Benefit owners are often also the managers who lead adoption in their teams. Connect them with
`change-and-communications:manager-enablement` so that ownership of the benefit and leadership of the change reinforce
each other.

## Knowledge considerations

Where a benefit depends on an agent grounded in organisational content, the benefit owner should know who owns that
content and agree with them how currency will be maintained, because stale knowledge undermines the benefit.

## Security and privacy considerations

Owners receive team-level measures only. They must not be given access to individual usage or performance data in the
name of benefit tracking; route any such request to the data protection officer.

## Responsible AI considerations

Owners of benefits that involve decisions about people should understand the human oversight the solution requires and
must not trade it away to accelerate realisation. Route concerns to the solution's responsible AI review.

## Evaluation requirements

Not applicable directly, because ownership concerns accountability rather than AI output quality. Owners should still
receive the quality guard results that apply to their benefits.

## Value measures

Success is the share of registered benefits with an owner passing all five tests, and the share whose owner attended
and reported at the last review, tracked by the Benefits Realisation Lead from the first register review.

## Scale notes

### Starter

One owner per initiative for all its benefits, agreed in a single conversation and recorded on one line of the register,
with the sponsor as escalation.

### Scale

An owner per benefit, short ownership agreements, measurement partners, deputies, and hand-over built into reviews.

### Enterprise

Owner roles defined in the operating model for recurring benefit types, contributing owners across business units,
and benefit hand-over integrated with organisational role-change processes.

## Hand-offs

- To `value-realisation:benefit-realisation-plan` with owners and their decisions scheduled.
- To `value-realisation:post-implementation-review` where owners report outcomes.
- To `ai-strategy:executive-sponsorship` for benefits with no owner passing the tests.
- To `organisation-tailoring:ownership-map` to record benefit ownership gaps across the programme.

## Reviewer gates

Not applicable, because benefit ownership is an accountability arrangement rather than a solution release. The sponsor
resolves escalated ownership gaps at the programme's value review.

## Failure modes

- IT is named as owner of business benefits, cannot change the work, and the benefits are written off at renewal.
- The most senior person available accepts ownership but cannot influence the team where the benefit appears.
- An owner moves role, no deputy is named, and the benefit disappears from reviews.
- Owners are left to produce their own figures and stop reporting after the second review.
- Benefit shortfalls are treated as personal failures, so owners pad baselines and lower targets.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Make IT or the CoE accountable for business benefits they cannot influence.
- Assign ownership to a person who has not accepted it, or to undeclared roles.
- Use benefit ownership or missed benefits to assess individual performance.
- Give owners access to individual usage data for benefit tracking.

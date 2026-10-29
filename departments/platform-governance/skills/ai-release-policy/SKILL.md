---
name: ai-release-policy
description: Sets the organisation's release policy for agents, flows and AI solutions by risk tier - the evidence, reviewer sign-offs, approver, permitted audience and channels, and post-release review each tier requires - plus rules for widening an audience, emergency changes and exceptions. Use when there is no consistent rule for publishing agents, when release takes the same effort at every tier, or when solutions reach wide audiences without review.
license: CC-BY-4.0
metadata:
  department: platform-governance
  lifecycle: Mobilise, Assure, Launch, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, power-platform, ai-foundry, copilot-cowork
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, evaluation-quality, design-authority, responsible-ai
  sources: ms-copilot-studio-guidance, ms-copilot-studio-security-governance, ms-copilot-studio-zoned-governance, ms-managed-environments, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI release policy

## Purpose

Every agent, flow and AI solution is released somehow, even if only by a maker clicking "share". This skill writes the
policy that decides, by risk tier, what evidence a release needs, who must sign it off, who approves it, how wide the
audience may be, which channels are allowed and when the solution is reviewed afterwards. It makes low-risk releases
quick and high-risk releases deliberate. Release policies go wrong when one heavy process applies to everything, so
makers bypass it, or when no policy exists and audience grows by sharing until something goes wrong.

## When to use

- There is no consistent rule for publishing or sharing agents and AI solutions.
- Every release takes the same effort, whatever its risk.
- Solutions reach wide audiences, or external channels, without review.
- Reviewer departments need a clear point at which their gates apply.
- Emergency fixes and audience changes happen without a defined route.

## When not to use

- Running the release gate for one agent - use `m365-agents:agent-release-readiness`.
- Assembling the release evidence pack for a solution - use `evaluation-quality:ai-release-evidence`.
- Publishing a Copilot Studio agent to channels - use `copilot-studio:studio-deployment`.
- Setting programme-level stage gates - use `programme-management:stage-gates`.
- Classifying the risk tier of a solution - use `opportunity-management:risk-classification`.

## Questions to ask first

1. How are agents and AI solutions released or shared today, and who decides?
2. Which risk tiers does the organisation build at, and which reviewer departments are active?
3. Which channels are in scope - personal, team, organisation-wide, external websites, customer channels?
4. Who has authority to approve release at each tier, and to accept residual risk?
5. What happens today when a live solution needs an urgent fix?

## Required inputs

- The risk tiers and minimum postures from the governance framework and `opportunity-management:risk-classification`.
- The environment zoning plan from `platform-governance:ai-environment-strategy`.
- The reviewer departments active in the organisation and their gate criteria.
- The organisation's change management process, if one exists.

If a reviewer department is not yet operating, record who performs its check in the interim; never drop the check
because the department does not exist yet.

## Decision framework

| Tier | Evidence required | Sign-offs | Approver | Audience and channels | Post-release review |
|---|---|---|---|---|---|
| 0 | Acceptable-use guidance followed | None | Maker | Maker only | Not required |
| 1 | Named owner, defined audience, approved sources, basic test evidence | None; register entry | Business owner | Named team; internal channels | At review date |
| 2 | Tier 1 plus evaluation against threshold, security review, support and monitoring plan | `security-privacy` (blocking), `evaluation-quality`, `design-authority` | Business owner with CoE | Department or organisation; internal channels | After first month, then on cycle |
| 3 | Tier 2 plus privacy assessment, responsible AI review, continuity plan | Tier 2 plus `responsible-ai` (blocking) | Accountable executive | As approved; staged rollout | Early and frequent, then on cycle |
| 4 | Full assurance, human oversight, incident response, executive risk acceptance | All gates | Accountable executive, in writing | External or high-impact channels, staged | Continuous monitoring plus scheduled reviews |

Change rules:

| Change | Route |
|---|---|
| Widening audience or adding a channel | Re-classify risk tier, then release at the new tier |
| Change to instructions, knowledge, model or actions | Proportionate re-test; material change goes to `design-authority:ai-change-impact-review` |
| Emergency fix | Owner may release with retrospective review within an agreed period |
| Exception to the policy | Written approval by the accountable executive, with expiry |

## Practitioner approach

Start by mapping how releases happen today. Talk to makers and delivery teams, and look at sharing data. Most
organisations discover three routes: makers sharing directly, delivery teams publishing through a pipeline, and
partners deploying to channels. The policy has to cover all three.

Anchor the policy on the risk tiers. Tier decides evidence, sign-off and audience, so the release process is only as
good as risk classification. Make re-classification on audience change explicit, because audience growth is how
low-risk solutions become high-risk ones.

Keep tiers 0 and 1 light. A team agent with an owner, approved sources and a few tested questions should be releasable
in a day. If the process for tier 1 needs a committee, makers will share without it.

Make tier 2 and above deliberate. Name the evidence required and where it lives, the reviewer sign-offs and the
approver. Reviewer gates are blocking where the governance framework says so, and a blocking finding is not traded
against a launch date. Approval sits with the business, not with IT.

Control channels as well as audience. External channels, customer-facing websites and messaging apps raise risk even for
a simple agent. Tie each channel to a minimum tier.

Define the change route. Minor changes to a live solution need proportionate re-testing; material changes to
instructions, knowledge, models or actions go through change impact review. Emergency fixes are allowed with
retrospective review, so owners are not tempted to bypass the policy altogether.

Use the platform to enforce what it can: sharing limits by zone, managed environments for tier 2 and above, pipelines
with approvals for production. Check current controls in the source records. Where the platform cannot enforce, admin
monitoring detects.

Publish the policy with a one-page summary for makers, and review it when tiers, platforms or reviewer departments
change. Track releases by tier so the CoE can see whether the policy is proportionate in practice.

## Outputs

- An AI release policy: tiers, evidence, sign-offs, approvers, audience and channel limits, post-release reviews, change and emergency routes and exceptions.
- A maker-facing summary of how to release at tiers 0 to 2.
- Configuration requests for sharing limits and pipeline approvals.
- A release log specification, linked to the `agent-release-checklist` template for agents.

## Microsoft platform considerations

Sharing controls, managed environments, pipelines with approvals and channel publishing differ between Agent Builder,
Copilot Studio, Power Platform and Microsoft Foundry, and change frequently. Check `ms-copilot-studio-guidance`,
`ms-copilot-studio-security-governance` and `ms-managed-environments` for current enforcement options.

## Adoption considerations

A proportionate policy encourages makers to release through the front door. Publish expected turnaround times by tier
and meet them; slow gates are the main reason teams bypass governance.

## Knowledge considerations

Releases at tier 1 and above require knowledge sources with owners and review dates. Tie knowledge readiness evidence
to the release checklist rather than assessing it again.

## Security and privacy considerations

The `security-privacy` gate is blocking from tier 2. Make sure audience widening and new channels trigger the security
review again, because exposure depends on audience.

## Responsible AI considerations

From tier 3 the `responsible-ai` gate is blocking, and tier 4 needs written executive risk acceptance. Uses that inform
decisions about people may not be released below tier 3 whatever their audience.

## Evaluation requirements

The policy names the evaluation evidence each tier needs, consistent with `evaluation-quality:ai-release-evidence`, and
requires regression evaluation before material changes are released.

## Value measures

Track releases by tier, median time from request to release by tier, releases found outside the policy, and incidents
in the first month after release. The platform governance lead owns these measures, with a baseline from the first
quarter of operation.

## Scale notes

### Starter

Two routes are usually enough: a light route for team agents and a reviewed route for anything wider, with the CoE lead
acting as approver.

### Scale

Apply the full tier table, connect it to pipelines and the register, and report releases by tier to steering.

### Enterprise

Federate tier 1 and standard tier 2 approvals to business units, with central approval for tier 3 and 4, enforce through
platform controls and integrate with enterprise change management.

## Hand-offs

- To `m365-agents:agent-release-readiness` for each agent's release gate.
- To `evaluation-quality:ai-release-evidence` for evidence packs.
- To `design-authority:ai-change-impact-review` for material changes to live solutions.
- To `platform-governance:ai-admin-monitoring` to detect releases outside the policy.

## Reviewer gates

The policy defines when `security-privacy`, `evaluation-quality`, `design-authority` and `responsible-ai` gates apply,
and is agreed with each before adoption. Blocking findings stop release; disagreement escalates to the accountable
executive for written risk acceptance.

## Failure modes

- One heavy process applies to every release, and makers share around it.
- Audience grows by sharing without re-classification, and a tier 1 agent is used organisation-wide.
- A launch date overrides a blocking finding, and the issue becomes an incident.
- Emergency fixes have no route, so owners edit production directly and never review.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Allow a blocking reviewer finding to be traded against a release date.
- Let audience or channel widen without re-classifying the risk tier.
- Apply tier 3 effort to tier 1 releases.
- Place release approval for business outcomes with IT rather than the business owner.

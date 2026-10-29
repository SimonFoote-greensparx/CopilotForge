---
name: studio-deployment
description: Publishes a released Copilot Studio agent to its channels - Teams and Microsoft 365 Copilot, websites, custom apps and others - configuring per-channel authentication, sharing to the approved audience, admin approval and availability, channel-specific behaviour and a staged rollout with a rollback route. Use when an agent has passed its release gate, when it is being added to a new channel, or when users cannot find or open it.
license: CC-BY-4.0
metadata:
  department: copilot-studio
  lifecycle: Launch, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-studio, m365-copilot, m365-agents, power-platform
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-studio-guidance, ms-copilot-studio-security-governance, ms-agents-extensibility, ms-copilot-studio-zoned-governance
  status: draft
  authors: Simon Foote
---

# Studio deployment

## Purpose

An approved agent delivers nothing until the right people can find and use it in the place they work. This skill takes a
Copilot Studio agent that has passed its release gate and publishes it to its channels: configuring each channel,
matching sharing to the approved audience, getting any admin approval, and rolling out in stages with a way back.
Deployment usually goes wrong when an agent is shared more widely than approved because it was easier, when a website
channel is enabled without checking authentication, or when users cannot find an agent because nobody arranged its
availability in Teams and Microsoft 365 Copilot.

## When to use

- An agent has passed `m365-agents:agent-release-readiness` and needs publishing to its channels.
- An existing agent is being added to a new channel or a wider audience.
- Users report they cannot find, install or open the agent.
- A staged rollout or a rollback of a published agent is needed.

## When not to use

- Deciding whether the agent is ready to release - use `m365-agents:agent-release-readiness`.
- Moving the agent between environments with solutions and pipelines - use `copilot-studio:studio-alm`.
- Setting the organisation's release policy by risk tier - use `platform-governance:ai-release-policy`.
- Planning launch communications and user onboarding - use `copilot-adoption:launch-plan`.

## Questions to ask first

1. Which audience did the release gate approve, and which channels were tested?
2. Will users meet the agent in Teams and Microsoft 365 Copilot, on a website, in a custom app or elsewhere?
3. Does each channel support the agent's authentication and single sign-on as designed?
4. Does making the agent available to users require approval from Microsoft 365 or Teams administrators, and who are they?
5. Will rollout be staged, and what would trigger pausing or rolling back?

## Required inputs

- The release decision and approved audience from `m365-agents:agent-release-readiness`, with the `agent-release-checklist`.
- The production version imported through `copilot-studio:studio-alm`.
- The authentication design and per-channel sign-in test results from `copilot-studio:studio-authentication`.
- Security groups for the approved audience and contacts for Microsoft 365 or Teams administration.

If the release decision is missing, do not publish. If a channel was not tested, publish to the tested channels only and
record the rest as pending.

## Decision framework

| Channel | Use when | Check before publishing |
|---|---|---|
| Teams and Microsoft 365 Copilot | Staff audiences in their daily tools | Admin approval and availability rules, single sign-on, audience security group |
| Organisation website or intranet page | Staff or customers on a web page | Authentication matches audience; embedding secured; no internal tools on anonymous pages |
| Custom or mobile app | The agent is part of an existing application | App owner, authentication handshake, support route |
| Other messaging or contact centre channels | The audience already uses them | Data leaving the tenant, hand-off behaviour, channel-specific formatting |

| Rollout stage | Audience | Move on when |
|---|---|---|
| Pilot | A named pilot group | Threshold met in real use, no zero-tolerance incidents |
| Expanded | The first business units or roles | Support load and analytics stable |
| Full | The approved audience | Release review confirms readiness |

Never share beyond the approved audience. Widening the audience is a new release decision.

## Practitioner approach

Confirm the decision before touching the agent. Read the release record: the approved audience, the channels tested,
the risk tier and any conditions. Deployment implements a decision; it does not make one.

Configure each channel deliberately. For Teams and Microsoft 365 Copilot, prepare the agent's name, description, icon
and availability so users can recognise it, and work with Microsoft 365 or Teams administrators on approval and how the
agent is made available to the audience. For websites and custom apps, confirm that the authentication configured for
that channel matches the audience; an internal agent embedded on a public page is a data exposure, not a deployment
detail. Check how each channel renders the agent's messages, cards and citations, and adjust where a channel does not
support something the design relies on.

Share to security groups, not to individuals or "everyone". Sharing to the group that matches the approved audience keeps
access aligned with the release decision and makes later changes auditable. Check sharing limits and admin controls in
the current source records before planning large audiences.

Roll out in stages. Start with a pilot group drawn from the approved audience, watch analytics, support contacts and
feedback for an agreed period, then widen. Agree pause and rollback triggers in advance: a zero-tolerance failure, a
spike in failed actions, or a pattern of wrong answers. Rolling back may mean unpublishing a channel, narrowing sharing or
re-importing the previous version through ALM; know which, and who can do it, before you start.

Coordinate with launch. Users need to hear about the agent where they work, with examples of what it does well and where
to get help. Hand the timing and channel details to `copilot-adoption:launch-plan` so communications match availability.

After each stage, record what was published, to whom, in which channels and when, in the agent's release record and the
solution inventory. Verify as an ordinary user in each channel that the agent can be found, signs in correctly and
answers within its scope.

## Outputs

- A channel configuration record per channel: settings, authentication, appearance, admin approvals and test result.
- A staged rollout plan with audiences, dates, pause and rollback triggers and responsible roles.
- Sharing records showing the security groups used and their match to the approved audience.
- Updates to the `agent-release-checklist` and the solution inventory after each stage.

## Microsoft platform considerations

Channels, admin approval routes, availability in Microsoft 365 Copilot and Teams, sharing limits and channel features
change often. Check `ms-copilot-studio-guidance` and `ms-agents-extensibility` for current channels and behaviour,
`ms-copilot-studio-security-governance` for admin and sharing controls, and `ms-copilot-studio-zoned-governance` for
which zones may publish where.

## Adoption considerations

Availability without communication produces no usage. Align deployment stages with launch messages, give the agent a
clear name and description users will recognise, and make sure support knows the agent exists before users do.

## Knowledge considerations

Not applicable to channel configuration itself, because knowledge is fixed at release; check after publishing that
citations and links open correctly for users in each channel.

## Security and privacy considerations

Sharing never exceeds the approved audience, anonymous channels never reach internal data, and data leaving the tenant
through a channel is reviewed. Channel changes that widen exposure go back to `security-privacy:data-exposure-review`.

## Responsible AI considerations

Each channel must carry the agent's AI disclosure and route to a person. Public-facing channels deserve particular care
because users may not expect to meet an AI agent; confirm disclosure with `copilot-studio:conversation-design`.

## Evaluation requirements

Verify in each channel as an ordinary user: discovery, sign-in, a sample of in-scope and out-of-scope questions and one
action where the agent has tools. Monitor the pilot stage against the release threshold before widening.

## Value measures

Track reach within the approved audience, time from release decision to availability, and pilot-stage outcomes, owned by
the agent owner and reported at agent and audience level.

## Scale notes

### Starter

Publish to Teams and Microsoft 365 Copilot for a security group matching the approved audience, pilot with a small group
first and keep the previous version for rollback.

### Scale

Standard channel configurations, an agreed admin approval route, staged rollouts by default and release records linked
to the solution inventory.

### Enterprise

Formal deployment windows aligned with change management, staged rollouts across regions, automated checks that sharing
matches approvals and portfolio-level reporting of channel coverage.

## Hand-offs

- To `copilot-adoption:launch-plan` with channel availability and timing.
- To `copilot-studio:studio-analytics` to monitor the pilot and each stage.
- To `copilot-studio:studio-alm` for rollback by re-import.
- To `copilot-studio:studio-agent-lifecycle` once the agent is fully live.

## Reviewer gates

From risk tier 2, `security-privacy` confirms that sharing and channels match the approved audience and that anonymous or
external channels cannot reach internal data. From tier 1, any public website channel needs the same check. Sharing
beyond the approved audience is a blocking finding.

## Failure modes

- The agent is shared with everyone because creating a security group felt slow.
- An internal agent is embedded on a public page with authentication disabled.
- The agent is published but not made available in Teams and Microsoft 365 Copilot, so nobody can find it.
- No rollback was planned and a faulty release stays live while the team improvises.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Publish an agent without a recorded release decision.
- Share an agent beyond its approved audience, or with everyone by default.
- Enable a public or anonymous channel for an agent that can reach internal knowledge or tools.
- Start a rollout without agreed pause and rollback triggers.

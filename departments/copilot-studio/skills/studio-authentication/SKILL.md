---
name: studio-authentication
description: Designs how a Copilot Studio agent knows who the user is and whose identity it uses - the agent's authentication setting, Microsoft Entra sign-in or another identity provider, single sign-on per channel, end-user versus maker or service credentials for knowledge and tools, and anonymous use. Use when choosing an agent's authentication setting, when users are asked to sign in repeatedly, or when an action runs as the maker.
license: CC-BY-4.0
metadata:
  department: copilot-studio
  lifecycle: Deliver, Assure
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-studio, entra, power-platform
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-studio-security-governance, ms-copilot-studio-guidance, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Studio authentication

## Purpose

Authentication decides what a Copilot Studio agent can know about its user and whose rights it uses to read knowledge
and act. This skill designs the agent's authentication setting, the sign-in experience in each channel and the identity
each knowledge source and tool runs under, so the agent never sees or does more than the user should. It usually goes
wrong in three ways: an agent with internal tools published without authentication, actions that quietly run under the
maker's account, and a sign-in experience so clumsy that users abandon the agent.

## When to use

- A Studio agent is being designed and its authentication setting and identity model need deciding.
- The agent will be published to a new channel, especially a website or custom app.
- Users report repeated sign-in prompts, or answers that ignore their permissions.
- A tool or knowledge source is found to run under the maker's or a shared account.

## When not to use

- Organisation-wide identity architecture for users, agents and services - use `ai-architecture:ai-identity-design`.
- The formal review of identity and access for a solution - use `security-privacy:ai-identity-and-access-review`.
- Choosing connectors and the accounts behind their connections - use `copilot-studio:studio-connectors`.
- Configuring channels and publishing - use `copilot-studio:studio-deployment`.

## Questions to ask first

1. Who are the users - staff signed in to Microsoft 365, guests, customers or the public?
2. Must answers be trimmed to each user's permissions, or is every answer safe for anyone who can reach the agent?
3. Does any tool act in a system, and should it act as the user or under a scoped service identity?
4. Which channels will the agent use, and does single sign-on work for this agent in each of them?
5. What does the agent need to know about the user (name, role, region) and where does that information come from?

## Required inputs

- The solution design's audience, channels, knowledge map and action register.
- The organisation's identity standards and conditional access position, from `ai-architecture:ai-identity-design` or the identity team.
- For an external identity provider, the provider's owner and configuration details.
- The risk tier.

If the audience is not settled, authentication cannot be designed safely; record the gap rather than defaulting to no
authentication. Never assume single sign-on works in a channel without testing it.

## Decision framework

| Audience and need | Authentication setting | Identity for knowledge and tools |
|---|---|---|
| Staff in Teams and Microsoft 365 Copilot | Microsoft Entra sign-in with single sign-on where supported | End user by default |
| Staff on an intranet page or custom app | Entra sign-in configured for the channel, with single sign-on tested | End user by default |
| Customers or partners with accounts | Manual configuration against the organisation's customer identity provider | End user for their own records; scoped service identity only with approval |
| Anonymous public users | No authentication | Public knowledge only; no tools that read or change non-public data |

| Identity option for a tool or source | Use when | Control |
|---|---|---|
| End user | The default, and always for user-specific data | Agent cannot exceed the user's rights |
| Dedicated service identity | The user has no direct access but the business process requires the action | Minimum scope, owner, approval, audit, and the user's identity passed for logging |
| Maker's personal account | Personal prototypes only | Never for a shared agent |

## Practitioner approach

Start with the audience, not the setting. Write down who can reach the agent in each channel and whether they are
signed in there. Internal agents in Teams and Microsoft 365 Copilot usually have a signed-in user and can trim knowledge
and tools to that user. Public websites usually do not, and an anonymous agent must be designed as if anyone in the world
is using it.

Choose the authentication setting to match. For staff, use Microsoft Entra sign-in and require it for every
conversation that can reach internal knowledge or tools. For customers, use the organisation's customer identity
provider through manual configuration, with the identity team owning the app registration. Only choose no
authentication when every knowledge source is public and no tool touches non-public data; record that decision and its
reviewer.

Design single sign-on per channel. Where it is supported and configured, users are signed in silently; where it is not,
they see a sign-in card, which many users ignore or find suspicious. Test sign-in in every channel with ordinary user
accounts, including on mobile, and fix the configuration rather than asking users to tolerate prompts.

Map identity per knowledge source and tool. For each, record whether it uses the end user's identity, a dedicated service
identity or something else. End-user identity keeps the agent within the user's rights and gives an honest audit trail.
A service identity is sometimes right - for example to create a case in a system users cannot open directly - but it
must be scoped to the operation, owned by a team, approved, and should carry the user's identity into the target
system's logs where possible.

Use what the agent knows about the user sparingly. Signed-in agents can read profile attributes to personalise answers;
take only what the conversation needs, and do not let user-supplied text override identity claims. A user typing "I am a
manager" is not evidence that they are one.

Finally, plan for change. App registrations, secrets and certificates expire and identity providers change; record owners
and renewal dates in the `alm-and-environment-plan` so the agent does not fail on an expiry date nobody tracked.

## Outputs

- An authentication design: setting, identity provider, app registration owner, single sign-on per channel and sign-in test results.
- An identity map: each knowledge source and tool with the identity it uses, the reason and the approval.
- Secret and certificate renewal records for the `alm-and-environment-plan`.
- The authentication section of the `studio-solution-design`.

## Microsoft platform considerations

Copilot Studio offers several authentication settings, and single sign-on support, channel behaviour and admin controls
over unauthenticated agents differ by channel and change over time. Check `ms-copilot-studio-security-governance` and
`ms-copilot-studio-guidance` for current options, and `ms-copilot-privacy` for how identity affects grounding on
Microsoft 365 content.

## Adoption considerations

A smooth, silent sign-in is an adoption feature. Repeated prompts or unexplained sign-in cards drive users away; test the
experience as a new user and include sign-in guidance in launch materials where a prompt cannot be avoided.

## Knowledge considerations

Permission trimming of knowledge depends on the user being signed in and sources being connected with the user's
identity. Agree the trimming behaviour with `copilot-studio:studio-knowledge-architecture` so content owners know who can see what.

## Security and privacy considerations

Unauthenticated agents must not reach internal data. Shared agents must not run on personal accounts. Service identities
are least privilege, owned and reviewed. Secrets live in a managed store, not in the agent. Identity claims from users
in chat are never trusted for access decisions. Every decision here is evidence for `security-privacy:ai-identity-and-access-review`.

## Responsible AI considerations

Not applicable as a separate concern, because authentication is a security control; its effect on fairness is limited to
ensuring that answers trimmed to permissions are explained, so users with less access understand why answers differ.

## Evaluation requirements

Test sign-in in every channel, permission trimming with at least two users of different access from tier 2, anonymous
access attempts where the channel allows them, and every tool under a user who lacks rights in the target system.

## Value measures

Track sign-in abandonment and authentication-related failures per channel, owned by the agent owner at agent level. A
high abandonment rate at sign-in is a design defect, not a user problem.

## Scale notes

### Starter

Internal agents in Teams and Microsoft 365 Copilot with Entra sign-in and end-user identity throughout; no anonymous
agents and no service identities without a reviewer.

### Scale

Standard app registration patterns and owners, a register of service identities used by agents, and admin controls that
prevent unauthenticated agents in non-public zones.

### Enterprise

Align agent identities with the organisation's identity governance, including access reviews for service identities,
conditional access for agent channels and automated alerts before secret or certificate expiry.

## Hand-offs

- To `security-privacy:ai-identity-and-access-review` with the identity map.
- To `copilot-studio:studio-connectors` to set connection accounts to match the identity map.
- To `copilot-studio:studio-deployment` with per-channel sign-in configuration.
- To `ai-architecture:ai-identity-design` where the agent needs a new identity pattern.

## Reviewer gates

`security-privacy` reviews any unauthenticated agent and any service identity from tier 1, and the full identity map from
tier 2. An unauthenticated agent that can reach internal data, or a shared agent on a personal account, is a blocking finding.

## Failure modes

- An agent built for staff is published to a website without authentication and answers from internal content.
- A tool runs under the maker's account, so the audit trail shows the maker doing everything.
- Single sign-on is not configured for a channel and most users abandon at the sign-in card.
- A client secret expires and the agent fails for everyone on a date nobody recorded.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Publish an agent without authentication if it can reach any non-public knowledge or tool.
- Let a shared agent act under a maker's personal account.
- Trust identity or role claims typed by a user in the conversation.
- Store secrets in agent configuration, topics or variables.

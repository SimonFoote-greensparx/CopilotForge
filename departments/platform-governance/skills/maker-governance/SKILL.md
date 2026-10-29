---
name: maker-governance
description: Governs who can build and share agents and flows - maker enablement, onboarding commitments, sharing rights by zone and audience, ownership on creation, handover when makers move on, and the limits that stop personal builds being shared organisation-wide - without ranking makers. Use when agent building is opened to more people, when agents are shared too widely, or when makers leave and their solutions become orphans.
license: CC-BY-4.0
metadata:
  department: platform-governance
  lifecycle: Enable, Deliver, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: m365-agents, copilot-studio, power-platform, copilot-cowork, entra
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-studio-security-governance, ms-copilot-studio-zoned-governance, ms-managed-environments, ms-agent-builder, ms-coe-starter-kit
  status: draft
  authors: Simon Foote
---

# Maker governance

## Purpose

When building an agent takes minutes, the question is no longer who can build but who can share, with whom, and who
answers for it afterwards. This skill sets the rules for makers: how people become makers, what they commit to, how far
they may share by zone and audience, how ownership is recorded and handed over, and what happens when they move on. It
keeps building open while making sure shared solutions have owners. Maker governance goes wrong when it tries to stop
building rather than govern sharing, and when it measures or ranks makers as individuals.

## When to use

- Agent building in Agent Builder or Copilot Studio is about to be opened to more people.
- Agents or flows are being shared with large audiences without review.
- Makers leave or change roles and their solutions have no owner.
- There is no onboarding or code of practice for makers.
- Security asks who is allowed to publish agents and nobody can answer.

## When not to use

- Deciding which zones and environments makers build in - use `platform-governance:ai-environment-strategy`.
- Setting connector and data policies makers are bound by - use `platform-governance:connector-policy`.
- Assigning business, knowledge and technical owners to one agent - use `m365-agents:agent-ownership`.
- Designing learning pathways for makers and power users - use `learning-and-skills:advanced-pathways`.
- Governing Copilot Cowork plugins and skills - use `copilot-cowork:cowork-governance`.

## Questions to ask first

1. Who can build agents and flows today, on which platforms, and how was that decided?
2. How far can a maker share today, and has anything been shared organisation-wide without review?
3. What should a maker commit to before sharing beyond themselves?
4. What happens to a solution when its maker leaves or changes role?
5. How will makers get help and learn the rules?

## Required inputs

- The environment zoning plan, from `platform-governance:ai-environment-strategy`.
- The governance framework and risk tiers.
- Current maker and sharing data from admin reports, at aggregate level.
- The organisation's joiner, mover and leaver process.

If current sharing data is unavailable, start with the rules and plan a discovery through
`platform-governance:ai-solution-inventory`; never assume nothing has been shared widely.

## Decision framework

Govern by sharing reach, not by who is allowed to experiment.

| Maker level | How reached | May share with | Commitments |
|---|---|---|---|
| Personal builder | Default for licensed or enabled users per policy | Themselves, or a very small group in zone 1 | Acceptable-use guidance; no sensitive data |
| Team maker | Completes maker onboarding | A named team in zone 2 | Named owner, register entry, review date, co-owner |
| Solution maker | Works within a delivery team in zone 3 | Defined audience through the release policy | ALM, reviewer gates, support model |
| Platform administrator | Appointed role | Not applicable; administers rather than shares | Separation from making where possible, privileged access controls |

Rules that apply at every level:

| Rule | Reason |
|---|---|
| Every shared solution has at least two owners | Avoids orphans when one person leaves |
| Sharing beyond a team goes through the release policy | Audience drives risk tier |
| Ownership transfers are part of the mover and leaver process | Solutions outlive roles |
| Makers are supported, not ranked | Measures are at team or role level only |

## Practitioner approach

Start by looking at sharing, not building. Use admin reports or the inventory to see, at aggregate level, how many
agents and flows exist, how many are shared, and how widely. The risk is concentrated in a small number of widely shared
items; that is where governance attention belongs.

Keep personal building open. Decide with the CoE who is enabled to build by default, based on licensing and policy, and
make the personal zone safe rather than closed. People who cannot experiment do not become good makers.

Make sharing the control point. Use the platform's sharing limits and zone policies so that personal builds cannot be
shared beyond a small group, team builds stay within a named team, and organisation-wide sharing happens only through
`platform-governance:ai-release-policy`. Check the current controls in the source records before promising a limit.

Design maker onboarding as a short commitment rather than a course. A team maker agrees to name a co-owner, register the
solution, use approved connectors, keep sensitive data out of zone 2 and review the solution on a date. Link to learning
for those who want to go further, through `learning-and-skills`.

Fix the leaver problem early. Connect the maker rules to the organisation's mover and leaver process so that solutions
owned by someone leaving are flagged and transferred. Requiring a co-owner from the start makes this far easier.
Unowned items after a grace period are archived, then removed, with notice.

Give makers a place to ask. A maker community, office hours or a Champions channel answers most questions faster than a
ticket queue, and surfaces policy that is unclear.

Report at team and role level only. The CoE needs to know how many solutions each business unit has, whether they have
owners and how widely they are shared. It does not need a league table of makers, and creating one discourages exactly
the people the programme needs.

Review the rules regularly against what admin monitoring shows, and adjust limits where they block legitimate work or
fail to prevent risky sharing.

## Outputs

- Maker governance rules: maker levels, how each is reached, sharing limits, commitments and ownership rules.
- A maker onboarding commitment and short guide.
- A leaver and mover procedure for AI solutions, agreed with HR and IT.
- Requests to platform administrators for sharing limits and policies per zone.

## Microsoft platform considerations

Sharing controls, maker permissions, environment security roles and ownership transfer differ between Agent Builder,
Copilot Studio and Power Platform, and change over time. Check `ms-copilot-studio-security-governance`,
`ms-managed-environments` and `ms-agent-builder` for current options, and use the inventory components of
`ms-coe-starter-kit` or the admin centres to find owners.

## Adoption considerations

Maker governance shapes the culture of building. Keep the commitments short and explain why each exists. Celebrate
well-governed shared solutions through Champions and success stories, not by ranking people.

## Knowledge considerations

Makers often ground agents on content they can reach rather than content that is owned and current. Include a
commitment to use owned sources, and point makers to `m365-agents:knowledge-source-readiness`.

## Security and privacy considerations

Sharing reach and maker credentials are the main risks. Agree sharing limits and the ban on embedding personal
connections in shared solutions with the `security-privacy` reviewers.

## Responsible AI considerations

Makers should not build solutions that inform decisions about people in zones 1 or 2. Make this explicit in onboarding,
and route such ideas to opportunity intake and `responsible-ai` review.

## Evaluation requirements

Not applicable to maker rules themselves, because evaluation applies to solutions. Team makers commit to the basic test
evidence the risk tier requires.

## Value measures

At business unit or role level, track shared solutions with two owners, orphaned solutions found and resolved, time to
transfer ownership on leaving, and maker onboarding completion. The platform governance lead owns these measures; no
measure names or ranks an individual maker.

## Scale notes

### Starter

Keep it to a one-page set of rules: who can build, sharing limits, two owners for anything shared, and a contact for
questions.

### Scale

Add maker onboarding, connect to the leaver process and review widely shared items monthly with the CoE.

### Enterprise

Federate maker support to business units, automate ownership checks and leaver flags, and align maker levels with the
role catalogue and learning pathways.

## Hand-offs

- To `platform-governance:ai-release-policy` for sharing beyond a team.
- To `platform-governance:ai-solution-inventory` to record owners.
- To `champions:champion-programme-design` and `learning-and-skills:advanced-pathways` for maker community and learning.

## Reviewer gates

Sharing limits and maker rules are agreed with `security-privacy` before adoption. Individual solutions pass the
reviewer gates their risk tier requires through the release policy.

## Failure modes

- Building is blocked, so makers use unapproved tools and the organisation loses visibility.
- A personal agent is shared organisation-wide and nobody reviewed it.
- A maker leaves and twenty flows stop working because they ran on that person's connections.
- Maker activity is reported by name, and makers stop building in the open.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Rank, score or monitor individual makers.
- Allow organisation-wide sharing outside the release policy.
- Let a shared solution exist with a single owner and no handover route.
- Promise a sharing limit or control before checking it in the current source records.

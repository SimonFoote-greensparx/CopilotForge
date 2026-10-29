---
name: agent-ownership
description: Assigns and records the business owner, knowledge owners, technical owner, maker and support route for an individual agent, with deputies, written acceptance, succession on role change and handling of ownerless agents, kept on an agent card. Use when an agent is being built or released, when its owner leaves or changes role, or when the inventory shows agents nobody claims.
license: CC-BY-4.0
metadata:
  department: m365-agents
  lifecycle: Deliver, Launch, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, power-platform
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-copilot-studio-guidance, ms-coe-starter-kit, ms-copilot-studio-zoned-governance
  status: draft
  authors: Simon Foote
---

# Agent ownership

## Purpose

Every agent needs people who answer for it: someone accountable for what it does for users, people who keep its
knowledge right, someone who keeps it technically sound, and a route for users when it goes wrong. This skill assigns
those roles for an individual agent, records written acceptance and deputies on an agent card, and handles succession
when people move on. Ownership usually goes wrong because the maker becomes the owner by default, then changes role, and
the agent keeps answering from stale knowledge with nobody watching.

## When to use

- An agent is being built and the brief names owners who have not yet formally accepted.
- An agent is about to be released and the release gate needs confirmed owners.
- An agent's business owner, knowledge owner or maker is leaving or changing role.
- The agent inventory shows agents that nobody claims, or that are owned only by their maker.

## When not to use

- Defining roles and responsibilities across the whole AI programme or CoE - use `ai-centre-of-excellence:coe-raci`.
- Mapping ownership of AI capabilities across the organisation - use `organisation-tailoring:ownership-map`.
- Defining the organisation's model for knowledge owners in general - use `knowledge-management:knowledge-owner-model`.
- Running the release gate that checks ownership along with everything else - use `m365-agents:agent-release-readiness`.
- Deciding to retire an ownerless agent - use `m365-agents:agent-lifecycle`.

## Questions to ask first

1. Who answers to the organisation for what this agent tells or does for users, and do they have the authority to change or stop it?
2. Who owns each knowledge source, and do they know an agent depends on their content?
3. Who keeps the agent technically working: configuration, connectors, environment and updates?
4. Where does a user go when the agent is wrong, and who fixes it?
5. Who steps in when any owner is absent or leaves?

## Required inputs

- The agent brief, with audience, purpose, sources, actions and risk tier.
- The knowledge list from `m365-agents:agent-grounding`, with apparent owners.
- The organisation's role catalogue or ownership map, if one exists.
- The agent inventory or solution register entry.

Never record a person as an owner until they have accepted in writing. Where an owner cannot be found, record the role as
vacant; a vacant business owner means the agent cannot be released and, if live, enters review.

## Decision framework

| Role | Accountable for | Usually held by | Must not be |
|---|---|---|---|
| Business owner | Purpose, audience, outcomes, approving changes, review and retirement decisions | A manager in the function the agent serves | The maker by default, or IT |
| Knowledge owner (per source) | Accuracy and currency of the source; telling the agent owner about changes | The owner of the policy, procedure or content | Unaware of the agent |
| Technical owner | Configuration, connectors, environment, updates and technical incidents | Maker team, platform team or partner | Unnamed |
| Maker | Building and changing the agent under change control | Citizen maker or developer | Sole owner of a tier 2 or higher agent |
| Support route | Receiving reports, triage, routing fixes | Service desk or owner contact, by tier | A personal inbox with no deputy |
| Deputies | Covering each owner role | Named colleagues | Absent |

From tier 2, the business owner and technical owner must be different people. From tier 3, a named executive sponsor
sits above the business owner.

## Practitioner approach

Start with the business owner, because every other role follows from that decision. The right person is the manager who
is accountable for the work the agent supports and who would be asked to explain if it gave a harmful answer. Meet them,
walk through the brief and the agent card, and ask them to describe what they will do when the agent is wrong. If they
cannot, or would not have time, they are not the owner yet.

Name knowledge owners per source and tell each of them what the agent uses their content for. Many knowledge owners do
not know agents depend on their documents. Agree that they will tell the agent's business owner when content changes,
and link their review cycle to the agent's review date.

Separate technical ownership from business ownership. The maker often knows the agent best, but makers move on. Record
the technical owner as a team where possible, with a named lead, and make sure they have access to the agent and its
environment. For agents built by citizen makers, agree with the CoE who becomes technical owner if the maker leaves.

Write down the support route as a user would experience it, and link it from the agent. Match it to the tier: an owner
contact may be enough for a small team agent; a wider audience needs a service desk route.

Name deputies for every role. Record acceptance in writing on the `agent-card`, with dates. An email reply saying "yes, I
agree" is enough; silence is not.

Plan succession. Ask HR or line management processes to include agent ownership in leaver and role-change checklists,
where the organisation supports that, and run a quarterly check of the inventory for owners who have left. When an owner
leaves, the deputy steps in temporarily and the business owner role is reassigned within an agreed period; if no one
will take it, the agent moves to review through `m365-agents:agent-lifecycle`.

For ownerless agents found in the inventory, contact the last known maker and the function the agent appears to serve.
Offer the choice to adopt it formally or retire it. Do not leave it running unowned.

## Outputs

- A completed `agent-card` for the agent: owners, deputies, acceptance dates, support route, sources with knowledge owners, risk tier and review date.
- Updated solution register entry with owners.
- A succession note for each owner role and a record of ownerless agents and their outcome.

## Microsoft platform considerations

Agents have technical owners and co-owners in the build tools and environments, which may differ from the business
owner recorded on the agent card. Keep both accurate. Inventory and ownership tooling, such as the CoE Starter Kit and
admin features described in `ms-coe-starter-kit` and `ms-copilot-studio-guidance`, can help find agents and their
technical owners; capabilities change, so check the current records.

## Adoption considerations

Users adopt agents that someone visibly stands behind. Name the business owner in the agent's description or welcome
message where appropriate, and make the support route easy to find.

## Knowledge considerations

Knowledge owners are the most frequently missing role. Each source on the knowledge list must have one who knows the agent
depends on their content and has agreed to flag changes.

## Security and privacy considerations

Technical owners hold access to configuration, connectors and sometimes credentials. Review that access when owners change,
and remove leavers promptly. Ownerless agents with connectors are a security risk to raise with `security-privacy`.

## Responsible AI considerations

From tier 3, the business owner must understand the agent's human oversight arrangements and accept accountability for
them in writing, with the executive sponsor named.

## Evaluation requirements

Not applicable as a test of the agent; the ownership record itself is checked at the release gate and at each scheduled
review for accepted, current owners and deputies.

## Value measures

Track, across the agent estate, the share of agents with all owner roles accepted and current, and the time taken to
reassign owners after a leaver. The CoE lead owns these estate measures; the business owner owns the agent's own value
measures.

## Scale notes

### Starter

A short agent card with a business owner, a technical owner, knowledge owners and a deputy, stored with the brief.

### Scale

Agent cards for every agent in the register, quarterly ownership checks and leaver processes that include agent
ownership.

### Enterprise

Ownership recorded in the portfolio and linked to HR role changes where the organisation supports it, with business-unit
agent product owners accountable for their estate.

## Hand-offs

- To `m365-agents:agent-release-readiness` with the completed agent card.
- To `m365-agents:agent-lifecycle` when an agent becomes ownerless.
- To `knowledge-management:knowledge-owner-model` for organisation-wide knowledge ownership.
- To `ai-operations:ai-support-model` for the support route.

## Reviewer gates

From risk tier 2, `design-authority` checks supportability and ownership through `design-authority:supportability-review`,
classifying gaps as blocking or advisory. A vacant business owner or technical owner is blocking.

## Failure modes

- The maker becomes the owner by default, changes role, and the agent decays unnoticed.
- Knowledge owners do not know the agent uses their content, so policy updates never reach it.
- Owners are recorded without accepting, and nobody acts when the agent is wrong.
- Ownerless agents keep running with connectors and stale knowledge.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Record someone as an owner without their written acceptance.
- Let the maker be the sole owner of an agent at tier 2 or above.
- Leave an ownerless agent running without a review or retirement decision.
- Use ownership records to judge individuals' performance.

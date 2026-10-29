---
name: coe-champion-integration
description: Connects the Champions network to the AI Centre of Excellence - assigning the knowledge, process, adoption and AI Champion roles to CoE pillars, defining what each contributes to intake, knowledge upkeep, testing and stories, what they never approve, and how work and feedback flow both ways. Use when a CoE and a Champions programme run side by side without links, or when Champions have become the CoE's unpaid build team.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Mobilise, Enable, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-champion-programme, ms-champion-best-practice, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# CoE Champion integration

## Purpose

Champions are the CoE's reach into every team: they spot opportunities, keep knowledge current, help colleagues adopt
and test what the CoE builds. This skill defines exactly how the four Champion roles plug into the CoE's pillars, what
each contributes and receives, and where their authority stops. Integration goes wrong in two opposite ways: the CoE and
the Champions programme run as separate worlds and ideas never reach intake, or the CoE leans on Champions as free
builders and approvers until they burn out or release something they should not.

## When to use

- A CoE and a Champions programme both exist but ideas, feedback and testing do not flow between them.
- The CoE needs Champions in defined roles rather than a general pool of enthusiasts.
- Champions are building or approving solutions beyond their remit and the boundary needs resetting.
- A Champion Challenge route for supporting the CoE needs connecting to real CoE work.

## When not to use

- Designing the Champions programme, its six-stage journey and boundaries - use `champions:champion-programme-design`.
- Recruiting Champions and agreeing time with their managers - use `champions:champion-recruitment`.
- Designing Champion Challenges and their assessment - use `champions:champion-challenges`.
- Designing the CoE's core and supporting roles - use `ai-centre-of-excellence:coe-team-design`.
- Building a separate change network alongside Champions - use `change-and-communications:change-network`.

## Questions to ask first

1. Which CoE pillars are active, and which of them need contributions from across the business rather than from the core team?
2. How many Champions are there, which capabilities have they evidenced, and how much time has each manager agreed?
3. Which Champion role would each Champion prefer, based on what they have declared they want to do?
4. Who in the CoE is the contact point for Champions, and how quickly will the CoE respond to what they send?
5. What are Champions explicitly not allowed to do under the Champions programme boundary table?

## Required inputs

- The Champions programme charter on the `champion-programme-charter` template, including the boundary table, from `champions:champion-programme-design`.
- The CoE operating model and active pillars, from `ai-centre-of-excellence:coe-operating-model`.
- Champions' declared role preferences and agreed time, held by the Champions programme.
- The CoE team terms of reference from `ai-centre-of-excellence:coe-team-design`, naming the CoE's Champion contact.

If no Champions programme exists, design the integration anyway and hand it to `champions:champion-programme-design` as
a requirement. Never assign Champions to roles they have not chosen.

## Decision framework

Map each Champion role to a pillar, a contribution and a limit.

| Champion role | CoE pillar | Contributes | Receives from the CoE | Never |
|---|---|---|---|---|
| Knowledge champion | Knowledge management | Flags outdated content, helps owners keep sources current, reports knowledge gaps from agent use | Knowledge standards, register access, recognition of contributions | Owns or approves content on behalf of its business owner |
| Process champion | Opportunity management | Spots and submits opportunities with a business owner, helps frame problems, gathers baseline data | Intake guidance, framing templates, feedback on every idea submitted | Prioritises the backlog or commits CoE capacity |
| Adoption champion | Adoption and change | Promotes scenarios and live agents, runs peer sessions, gathers success stories and feedback | Scenario catalogue, campaign materials, story templates | Acts as the help desk for faults or access requests |
| AI champion | Agent development and automation | Tests agents before release, builds tier 0-1 assets within policy, shares patterns | Test sets, maker guidance, early access to pilots | Releases tier 2 or above, or approves any solution |

Decide the level of involvement by tier.

| Risk tier | Champion involvement |
|---|---|
| 0 | Lead: share scenarios and prompt patterns freely |
| 1 | Contribute: build team assets within policy, register them with the CoE |
| 2 | Support: test, give feedback and help adoption; the CoE and owners decide |
| 3-4 | Inform: help with adoption after release only; no build or test role unless invited by the delivery team |

## Practitioner approach

Start from the CoE's pillars and ask where the core team cannot reach on its own. Usually it is the edge of the
organisation: noticing a problem worth solving, spotting that an agent's answer is out of date, persuading a sceptical
team to try something. Those are the contributions to ask Champions for. Write them down as recurring activities, not
general goodwill.

Assign roles by declared preference. Ask each Champion which of the four roles they want, based on what they enjoy and
what their manager has agreed. A Champion may hold more than one role in a small organisation, but each contribution
should map to one role so the CoE knows who to ask. Keep the role within the time the manager agreed; if the CoE needs
more, it asks the manager, not the Champion.

Design the flows in both directions. Into the CoE: ideas through the intake front door with a business owner attached,
knowledge issues into the knowledge register, test findings into the delivery team's tracker, stories into the success
stories area. Out of the CoE: feedback on every idea submitted, early sight of pilots, test sets and guidance, and
recognition. Champions who submit ideas and hear nothing stop submitting; set a response time for feedback and report
against it.

Hold the boundary firmly. Champions feed, test and promote; they do not prioritise the backlog, approve releases or own
high-risk solutions. Where a Champion has built something useful at tier 1, the CoE registers it and assigns an owner.
Where it has grown into a tier 2 solution, it re-enters intake like any other idea, with the Champion credited.

Connect the Champion Challenge. Supporting the CoE is one of the recognised challenge types in
`champions:champion-challenges`. Keep a short list of real CoE needs that would make good challenges, such as building a
test set for an agent, cleaning up a knowledge library with its owner, or writing a departmental playbook. That turns
challenges into useful work and gives Champions recognised contribution.

Name one CoE contact for Champions, usually the adoption and change lead, and add a standing Champions slot to the
community forum in `ai-centre-of-excellence:coe-cadence`. Record contributions at programme level, by role and team, so
the CoE can show the value of the network without tracking individuals.

Review the integration each quarter with the Champions programme owner: flows working, response times met, roles
balanced across teams, and any boundary breaches resolved.

## Outputs

- A Champion integration map: each role's pillar, contributions, what it receives, its limits and its CoE contact.
- Flow definitions for ideas, knowledge issues, test findings and stories, with response times.
- A list of CoE needs suitable as Champion Challenges, refreshed each quarter.
- Updates to the Champion rows of the `coe-terms-of-reference` template and the structure section of the `coe-charter` template.

## Microsoft platform considerations

Where AI champions build team assets, they should do so in the environments and with the tools the governance model
allows for tier 1, and register them in the CoE's register. Check current maker controls and sharing settings in
`references/sources.md` before telling Champions what they may build.

## Adoption considerations

Champions are the CoE's most credible adoption channel because they are peers. Give adoption champions the scenario
catalogue and success stories first, and ask them which messages land in their teams. Recognition of contribution is
designed in `champions:recognition-and-progression`; never use it to rank Champions against each other.

## Knowledge considerations

Knowledge champions support owners; they do not replace them. Route the issues they raise to the business owner of the
content through the knowledge register, and track the issue, not the Champion.

## Security and privacy considerations

Champions testing agents must use test data or content they are already permitted to see, and must not be given wider
access to test permission trimming. Make sure AI champions know which data must never go into tier 0-1 assets.

## Responsible AI considerations

Ask Champions to flag any idea or asset that would inform decisions about people, money, safety or rights, and route it
to intake rather than building it. Champions should never be the human oversight for such a solution.

## Evaluation requirements

When AI champions test agents, they use the test set and threshold agreed under `m365-agents:agent-testing` and record
results in the delivery team's tracker. Their findings are evidence for the owner, not a release decision.

## Value measures

Measure the integration at programme level: share of intake ideas arriving through Champions, share of teams with an
active Champion in each role, median time to give Champions feedback, and knowledge issues raised and resolved. The
adoption and change lead owns these measures. Never report contributions by individual.

## Scale notes

### Starter

A handful of Champions may cover all four roles between them, working directly with the working group. One shared list
and a monthly conversation are enough.

### Scale

Each Champion holds one or two defined roles, with a CoE contact, response times and a Champions slot in the community
forum.

### Enterprise

Each spoke connects its own Champions to its local pillars, with common role definitions and flows set by the hub so
Champions moving between units find the same model.

## Hand-offs

- To `champions:champion-programme-design` for anything that changes the Champions programme itself.
- To `champions:champion-challenges` for the list of CoE challenge opportunities.
- To `ai-centre-of-excellence:coe-opportunity-pipeline` for ideas submitted through Champions.
- To `ai-centre-of-excellence:coe-knowledge-pillar` for knowledge issues raised by Champions.

## Reviewer gates

Not applicable, because the integration map is an organisational design rather than a solution. Solutions that
Champions help with pass the normal gates, including `security-privacy` from tier 2, through the CoE's flow.

## Failure modes

- Champions submit ideas and never hear back, so the flow dries up within a quarter.
- The CoE treats Champions as a free build team and they release tier 2 solutions without review.
- Adoption champions become the help desk for access and licence problems.
- Contributions are reported by name and the network turns into a league table.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Let Champions approve releases, prioritise the backlog or own tier 2 and above solutions.
- Assign a Champion a role they have not chosen or time their manager has not agreed.
- Rank, score or monitor individual Champions; report at role and team level only.
- Make Champions the destination for faults, access requests or licence questions.

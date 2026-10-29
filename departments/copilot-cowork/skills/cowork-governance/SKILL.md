---
name: cowork-governance
description: Sets the organisation's governance for Copilot Cowork - who may use it and for what, which plugins, skills and custom instructions are approved, how shared task designs and skills are owned, published and retired, and which actions always need approval. Use when Cowork is being enabled, when teams start sharing skills or plugins, or when someone asks who approved a Cowork customisation now in wide use.
license: CC-BY-4.0
metadata:
  department: copilot-cowork
  lifecycle: Mobilise, Assure, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: copilot-cowork, m365-copilot, purview, entra
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, design-authority
  sources: ms-copilot-cowork-customise, ms-copilot-privacy, ms-agents-extensibility, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Cowork governance

## Purpose

Copilot Cowork becomes more capable as plugins, skills and custom instructions are added, and every addition changes what
delegated work can reach and do. Without governance, useful customisations spread by copying, nobody knows which skills
are in use or who maintains them, and a plugin that sends data outside the organisation arrives unreviewed. This skill
sets proportionate rules for Cowork: permitted and restricted uses, an approval route for customisations, ownership and
publishing of shared task designs and skills, and actions that always need a human approval. It goes wrong in two
directions: governance so heavy that people work around it, or so light that nobody can say what is running.

## When to use

- Cowork is being enabled for the first time, or for a new population.
- Teams start sharing skills, plugins, custom instructions or task designs with each other.
- Someone asks who approved a Cowork customisation that is now in wide use.
- A plugin or skill would let Cowork act in, or send data to, another system.
- Governance for Cowork needs aligning with the existing governance for agents and automation.

## When not to use

- Deciding whether one task suits Cowork - use `copilot-cowork:cowork-use-case-assessment`.
- Governing who can build and share agents and flows across Power Platform and Copilot Studio - use `platform-governance:maker-governance`.
- Setting data and connector policies across platforms - use `platform-governance:connector-policy`.
- The security review of a specific plugin or connector - use `security-privacy:connector-review`.
- The organisation-wide AI governance model and decision rights - use `ai-centre-of-excellence:coe-governance-model`.

## Questions to ask first

1. Which uses of Cowork are encouraged, which need care and which are not permitted, and has that been written down anywhere?
2. Which plugins, skills and custom instructions are in use or requested, who built them, and what can each reach or do?
3. Who decides whether a new customisation can be published to others, and on what criteria?
4. Which actions (sending, sharing, filing, changing records in other systems) should always require a human approval?
5. How will the organisation know what is in use, and who maintains it, a year from now?

## Required inputs

- The organisation's existing AI governance model, acceptable use policy and risk tiers.
- The current governance for agents, connectors and automation, so Cowork rules align rather than duplicate.
- An inventory of Cowork customisations already in use, even if partial.
- The admin controls currently available for Cowork, confirmed from the source records.

If no acceptable use policy exists, draft the Cowork position as an interim note and route the gap to the CoE. Never
state an admin control or setting exists without checking the current source record.

## Decision framework

Govern customisations by reach and effect, not by who built them.

| Customisation | Reach and effect | Approval | Owner and review |
|---|---|---|---|
| Personal task design | One person, own context, drafts only | None; good practice guidance | The person |
| Shared task design | A team, drafts only | Team lead plus grounding check | Named owner, review date |
| Organisational skill or custom instruction | Many people, shapes many tasks | CoE approval and content check | Named owner, versioned, scheduled review |
| Plugin that reads other systems | Brings new data into Cowork | Security review of data and identity | Technical owner and business owner |
| Plugin or skill that acts or sends | Changes or sends outside Microsoft 365 or to others | Security review, pre-effect approval required, risk tier confirmed | Technical owner, business owner, review date |

Usage rules sit in three bands: encouraged (drafting, summarising, collating, preparing), with care (anything reaching
external parties or touching personal data, with checkpoints and review), and not permitted (decisions about individuals'
employment, pay or rights, and any use the acceptable use policy excludes).

## Practitioner approach

Start from what already exists. Most organisations have an acceptable use policy for AI, governance for agents and
connectors, and some risk tiering. Map Cowork onto those rather than writing a parallel regime. The main new elements
are the customisation layers Cowork supports and the way shared task designs spread, so concentrate effort there.

Take an inventory before writing rules. Ask Champions and early users which skills, plugins, custom instructions and task
designs they use and share, and what each one reaches. This often reveals a handful of widely copied designs with no
owner, and one or two plugins nobody reviewed. Bring those into the approval route first rather than banning them, so
people see governance as a way to keep useful things running.

Set the approval route by reach and effect. A personal task design needs guidance, not approval. A skill or custom
instruction that will shape many people's work needs a named owner, a content check and a version history, because a
mistake in it repeats everywhere. Anything that lets Cowork reach new data or act outside the user's own drafting needs
a security review of the data it touches, the identity it uses and where information goes.

Fix the always-approve actions centrally. Sending to external recipients, sharing beyond the original audience, filing
into records systems and changing data in line-of-business systems should require a pre-effect approval in every task
design, whatever the team prefers. Publish that list so `copilot-cowork:human-checkpoint-design` can apply it.

Make publishing and retirement explicit. A shared library of approved skills and task designs, each with owner, purpose,
risk tier and review date, is easier to govern than scattered copies. Retire items whose owner has left or whose review
has lapsed, and tell users what replaced them.

Keep the rules short and visible. One page of usage bands, the approval table and the always-approve list will be read;
a long policy will not. Review the position as the product and the organisation's experience change, and check the
current source records each time rather than relying on what was true at enablement.

## Outputs

- A Cowork governance position: usage bands, approval route by customisation type and the always-approve action list.
- An inventory of approved skills, plugins, custom instructions and shared task designs, with owners, risk tiers and review dates.
- A publishing and retirement procedure for shared customisations.
- Referrals for any customisation needing security or design review.

## Microsoft platform considerations

Cowork can be customised with plugins, skills and custom instructions, and the admin controls over who can use and share
them change as the product evolves. Confirm current options in the source records (`ms-copilot-cowork-customise`,
`ms-agents-extensibility`, `ms-copilot-privacy`). Align Cowork plugin governance with connector and agent governance, since
the same systems and identities are often involved. Licensing questions go to the Microsoft licensing guide or a licensing
partner.

## Adoption considerations

Governance that explains itself is followed. Pair every rule with the reason and with the route to get something
approved, and make the approved library the easiest place to find good designs. Work with `copilot-cowork:cowork-adoption`
so governance and enablement send the same message.

## Knowledge considerations

Organisational skills and custom instructions are knowledge assets: they encode standards, terminology and practice.
Give each an owner and a review cycle, and retire them when the standard they encode changes.

## Security and privacy considerations

Plugins that read or act in other systems are the main new exposure. Each needs a review of data reached, identity used
and destinations, through `security-privacy:connector-review`. Review interaction retention with
`security-privacy:ai-interaction-retention` where Cowork outputs or logs hold personal data.

## Responsible AI considerations

Write prohibited uses plainly in the usage bands, aligned with the organisation's responsible AI policy, and route
borderline cases to `responsible-ai:prohibited-use-review`. Customisations that shape many people's work deserve the same
care as an agent.

## Evaluation requirements

Organisational skills and custom instructions that shape many tasks must pass `copilot-cowork:workflow-validation` on
representative tasks before publication, and again after material changes.

## Value measures

Track the number of approved shared customisations in use, the share with a current owner and review, and time from
request to approval. Report usage at team or role level above the agreed minimum group size, never by individual.

## Scale notes

### Starter

A one-page position, a short list of approved customisations and a named person who approves anything shared. Start with
drafting uses and no plugins that act.

### Scale

Run the approval route through the CoE, keep a shared library with owners and review dates, and align plugin reviews with
connector governance.

### Enterprise

Federate approval of team-level designs to business units within central rules; organisational skills, custom
instructions and plugins that act are approved centrally and tracked in the AI solution inventory.

## Hand-offs

- To `security-privacy:connector-review` for plugins that read or act in other systems.
- To `platform-governance:ai-solution-inventory` to record approved customisations.
- To `copilot-cowork:human-checkpoint-design` with the always-approve action list.
- To `copilot-cowork:cowork-adoption` to publish the approved library.

## Reviewer gates

`security-privacy` reviews every plugin that reads or acts in other systems, and any organisational skill handling personal
data, classifying findings as blocking or advisory. From risk tier 2, `design-authority` reviews whether a customisation
should instead be an owned agent or automation.

## Failure modes

- A widely copied task design or skill has no owner, encodes an outdated standard and keeps spreading.
- A plugin that sends data outside the organisation is installed by a team without any review.
- Governance is so heavy that teams build unofficial workarounds the organisation cannot see.
- Cowork rules duplicate and contradict the existing agent and connector governance.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Publish an organisational skill, custom instruction or plugin without a named owner and review date.
- Allow a plugin that acts or sends outside the organisation without a security review.
- Use governance data to monitor or rank individual users.
- State licensing conclusions; route them to the Microsoft licensing guide or a licensing partner.

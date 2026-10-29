---
name: ai-transparency
description: Reviews how an AI solution tells people about AI - disclosure that users are dealing with AI, labelling of AI-generated content, what it can and cannot do, where answers come from, and notice to people affected by outputs who never use it - classifying gaps as blocking or advisory. Use when an agent faces customers or staff, when AI content is sent or published, or when people may not know AI shaped an outcome.
license: CC-BY-4.0
metadata:
  department: responsible-ai
  lifecycle: Deliver, Assure, Launch, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-copilot, m365-agents, copilot-studio, ai-foundry, power-platform
  edition-support: starter, scale, enterprise
  reviewers: responsible-ai
  sources: ms-responsible-ai, ico-ai-data-protection, nist-ai-rmf, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# AI transparency

## Purpose

People trust and use AI appropriately when they know they are dealing with it, what it is good and bad at, and where its
answers come from. People affected by AI-influenced outcomes deserve to know that too, even if they never typed a
prompt. This reviewer skill checks that a solution is open with its users and with the people its outputs concern, in
language they understand and at the moment it matters, and classifies gaps as blocking or advisory. It goes wrong when
transparency is reduced to one line of small print, or when disclosure is so heavy and generic that people stop
reading it.

## When to use

- An agent or AI feature faces customers, the public or staff at a `responsible-ai` gate.
- AI-generated text, images, summaries or messages are sent to people or published.
- Outputs contribute to decisions about people who do not interact with the solution.
- Users over-rely on answers or do not realise they can be wrong.
- A voice or chat channel could be mistaken for a person.

## When not to use

- Privacy notices and the legal transparency duties for personal data - use `security-privacy:privacy-assessment`.
- Designing the conversation, tone, fallbacks and hand-offs of an agent - use `copilot-studio:conversation-design`.
- Communicating the AI programme to the workforce - use `change-and-communications:ai-communication-strategy`.
- Routes for people to challenge an outcome - use `responsible-ai:escalation-and-appeal`.

## Questions to ask first

1. Who interacts with the solution, and who is affected by its outputs without interacting with it?
2. Could anyone reasonably believe they are dealing with a person, or that content was written by a person?
3. What do users need to know to use it well - purpose, limits, sources, when to check, how to get a person?
4. When will people affected by an outcome learn that AI was involved, and how can they find out more?
5. Who owns the wording, and how will it stay accurate as the solution changes?

## Required inputs

- The AI impact assessment record and risk tier.
- The solution design, channels and the outputs it produces.
- Current wording of any disclosures, messages and notices.
- The privacy position from `security-privacy:privacy-assessment` where personal data is involved.

Where no wording exists yet, review the plan for it and record the gap. Never draft legal notice text as if it were
approved; legal and privacy wording goes to the DPO or legal adviser.

## Decision framework

From risk tier 2 every gap is classified; the gate is mandatory and blocking from tier 3, and from tier 2 when outputs
reach people outside the organisation or inform decisions about people. At tier 1, use this as advisory guidance.

| Transparency element | Blocking when | Advisory when | Typical fix |
|---|---|---|---|
| AI disclosure | People could believe they are dealing with a person, or are not told AI is involved | Disclosure exists but is easy to miss | Clear disclosure at first contact and in the channel name |
| Capability and limits | Users are not told the solution can be wrong on matters affecting people, money or safety | Limits stated generically | Specific, plain statements of purpose, limits and when to check |
| Sources and provenance | Answers on high-impact topics have no visible source or provenance | Citations exist but are inconsistent | Show sources; distinguish organisational from web content |
| AI-generated content | AI-drafted messages or documents reach external people without disclosure where the organisation's policy requires it | Labelling inconsistent internally | Apply a labelling rule by content type and audience |
| Affected people | People affected by an AI-influenced decision are not told and have no way to ask | Information exists but only on request | Notice at decision point, with route to more information |
| Route to a person | No way to reach a person where the impact assessment requires one | Route exists but is hard to find | Visible hand-off or contact route |

## Practitioner approach

Start with the two audiences. Users need to know enough to use the solution well; affected people need to know AI was
involved in something that matters to them. Write down, for each audience, the moment they most need to know, which
is rarely the terms of use page.

For users, look at first contact. The channel name, the greeting and the agent's description should make clear this is
AI, what it is for and what it is not for. Avoid human names and personas that blur the line. Then check that limits
are specific: "can be wrong" is less useful than "answers come from the policy library and may not reflect changes made
this week; check the policy before acting on leave decisions". Make sources visible, and make it obvious when an
answer draws on the web rather than organisational content.

For AI-generated content, apply the organisation's labelling rule, or recommend one if none exists. A reasonable
default is that content sent outside the organisation, or used in decisions about people, says when AI drafted it and a
person reviewed it. Internal drafts that a person edits and owns may not need labels; record the reasoning.

For affected people, find the decision point. A customer whose claim was triaged by AI, a candidate whose application
was summarised, or a tenant whose request was categorised should be able to learn that AI was involved and how to ask
for a person to look again. Coordinate the wording with `security-privacy:privacy-assessment` so privacy notices and
in-product statements agree.

Test the wording with people from the audience. If they cannot say, after reading it, what the solution does and when to
check its output, it has not worked. Keep a short transparency note for the solution, owned by the business owner, that
records purpose, limits, sources, oversight and contact routes, and update it when the solution changes.

Classify gaps proportionately. Over-disclosure is a real failure too: warnings on every answer train people to ignore
all of them.

## Outputs

- A transparency note for the solution: purpose, intended users, limits, sources, oversight, how to reach a person and how to raise concerns.
- Reviewed disclosure and labelling wording for each channel and output type.
- Gaps classified blocking or advisory with fix and owner, recorded in the `ai-impact-assessment-record`.

## Microsoft platform considerations

How agents introduce themselves, display citations, distinguish web content and label AI-generated content differs by
route and changes as products evolve. Microsoft publishes transparency resources for its AI services in
`ms-responsible-ai`; use them to understand provider-side behaviour, and confirm current product features in the
relevant source records before relying on them.

## Adoption considerations

Good transparency improves adoption: people who know the limits use AI for the right tasks and trust it where it is
reliable. Feed the transparency note into onboarding and Champion materials.

## Knowledge considerations

Visible sources only help if the sources are current and owned. Where citations point to stale content, raise it with
the knowledge owner.

## Security and privacy considerations

Transparency about personal data processing is a legal duty handled with `security-privacy:privacy-assessment`.
Transparency notes should not reveal system prompts or configuration detail that would help an attacker.

## Responsible AI considerations

This skill is the responsible AI review of transparency. It depends on `responsible-ai:ai-impact-assessment` to
identify affected people, and links to `responsible-ai:escalation-and-appeal` for what people can do next.

## Evaluation requirements

Test disclosures with representative users: can they say what the solution does, its main limit and how to reach a
person? Check that citations appear as designed across the evaluation set.

## Value measures

Track, at aggregate level, the share of surveyed users who correctly understand the solution's purpose and limits, and
the share of tier 2+ solutions with a current transparency note. The responsible AI lead owns these measures.

## Scale notes

### Starter

Use a standard disclosure line and a one-page transparency note per agent. Keep early agents internal, where
disclosure is simplest.

### Scale

Publish a labelling rule for AI-generated content and a transparency note pattern, and check them at every release.

### Enterprise

Maintain an organisation-wide register of transparency notes, align wording with privacy notices across business units,
and review external-facing disclosures with legal advisers.

## Hand-offs

- To the build team with wording and design requirements.
- To `security-privacy:privacy-assessment` to align privacy notices.
- To `responsible-ai:escalation-and-appeal` for routes to a person.
- To `copilot-adoption:launch-plan` so disclosures appear in launch materials.

## Reviewer gates

This skill is part of the `responsible-ai` gate. It is mandatory and blocking from risk tier 3, and from tier 2 when
outputs reach people outside the organisation or inform decisions about people; otherwise advisory. Disagreement
escalates to the accountable executive for written risk acceptance.

## Failure modes

- Disclosure sits in terms nobody reads, so customers think they are talking to a person.
- Every answer carries the same warning, and people learn to ignore it.
- Affected people never learn AI was involved, so they cannot question the outcome.
- The transparency note is written once and drifts out of date as the solution changes.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Allow an AI solution to present itself as a person.
- Present legal or privacy notice wording as approved without the DPO or legal adviser.
- Reveal system prompts or security configuration in the name of transparency.
- Trade a blocking gap against a launch date.

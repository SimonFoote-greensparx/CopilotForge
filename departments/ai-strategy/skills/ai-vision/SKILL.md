---
name: ai-vision
description: Articulates the organisation's AI ambition - a deliberately chosen level of ambition, a short vision statement staff can repeat, a narrative of how work will change and a handful of guiding principles - agreed by the leadership team and written for the whole workforce. Use when leaders cannot say in a sentence why the organisation is adopting AI, when functions hold competing pictures of it, or before outcomes and a roadmap are set.
license: CC-BY-4.0
metadata:
  department: ai-strategy
  lifecycle: Discover, Envision
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-responsible-ai, nist-ai-rmf, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# AI vision

## Purpose

This skill gives the organisation one shared answer to "why are we doing AI, how far do we intend to go, and what kind
of organisation do we want to be while we do it". It produces an explicit level of ambition, a short vision statement, a
narrative of how work will change for people, and guiding principles that set the tone for everything after. Vision
work usually goes wrong in one of three ways: it is a product slogan ("Copilot for everyone"), it is so grand that nobody
can connect it to their own job, or it is written by a small group and announced, so the workforce reads it as a
headcount plan in disguise.

## When to use

- The leadership team has decided to take AI seriously but cannot say in one sentence why, or how far.
- Different functions describe AI in contradictory ways (cost cutting, innovation, risk) and staff are hearing all of them.
- A strategy, CoE or adoption programme is about to start and needs a shared starting point.
- Staff anxiety about AI is rising and leaders need to state their intent plainly.
- A merger, new chief executive or major change of direction makes the existing vision obsolete.

## When not to use

- Turning the vision into three to five measurable outcomes, decision-rule principles and the "where AI is not appropriate" list - use `ai-strategy:strategic-outcomes`.
- Establishing the honest current baseline the ambition must start from - use `ai-strategy:ai-maturity-assessment`.
- Securing and equipping the executive who will champion the vision - use `ai-strategy:executive-sponsorship`.
- Planning how the vision is communicated across the organisation - use `change-and-communications:ai-communication-strategy`.
- Revisiting an existing vision against results and Microsoft change - use `ai-strategy:strategy-refresh`.

## Questions to ask first

1. What is the organisation for, and which of its existing strategic priorities could AI genuinely help with?
2. How ambitious do leaders intend to be over the next two to three years, and what are they prepared to invest and change to get there?
3. What do leaders want staff to believe about AI and their jobs, and is that belief true?
4. Which commitments (to customers, regulators, staff representatives, the public) must the vision respect?
5. Who must agree the vision for it to hold, and who will be expected to repeat it?

## Required inputs

- The organisation's mission, current business strategy and its existing values or behaviours framework.
- The maturity assessment from `ai-strategy:ai-maturity-assessment`, or a note that none exists yet.
- Time with the leadership team, ideally a facilitated working session, plus short conversations with staff representatives where they exist.
- Any existing AI statements, policies, public commitments or regulatory obligations.

Where the maturity baseline is missing, mark the ambition level as provisional and record the gap. Never invent
competitor positions, market statistics or productivity figures to make the case for a bolder ambition.

## Decision framework

Choose the ambition level deliberately, using the maturity baseline and the investment leaders will actually commit.
The level shapes what the vision may promise.

| Ambition level | What it means | Choose it when | Do not choose it when |
|---|---|---|---|
| Foundational | Everyone uses AI safely in everyday work; a few owned agents | Maturity is explorer or adopter, and governance and knowledge are thin | Leaders expect transformation of core services within the horizon |
| Augmented | AI is built into how priority roles and processes work, with owned solutions | Adoption is under way and the organisation can own and support solutions | No one can own knowledge or solutions beyond the pilot stage |
| Transformed | Selected services or operating processes are redesigned around AI | Builder or scaler maturity, a funded CoE, and leaders willing to change processes and roles | It depends on capability two archetype stages ahead |

A vision statement passes when it fits in two sentences, names a change in how work or service happens rather than a
product, can be repeated by a manager without notes, and is consistent with the chosen ambition level. Guiding
principles pass when there are no more than six, each states a stance the organisation will hold under pressure, and
each could be explained to a sceptical member of staff.

## Practitioner approach

Start from the organisation's purpose and current strategy, not from AI. Ask leaders what the organisation exists to
do and where it is under strain, then ask where AI could plausibly help. A vision that cannot be traced to the existing
strategy will be treated as a technology side project and abandoned at the first budget round.

Make the ambition choice explicit and early. Present the three levels, the maturity evidence and what each level
would demand in investment, ownership and process change. Leaders often say "transformed" and fund "foundational";
naming the gap in the room is the most useful thing this skill does. Record the chosen level and the reasoning, and
say what would have to be true to move up a level later.

Draft the vision statement with the leadership team, not for them. Offer two or three contrasting drafts and let them
argue. Good statements describe people and service: "Our people spend their time on judgement and care, with AI
handling the searching, drafting and summarising, so customers get faster, better-informed answers." Weak ones describe
tools or adjectives. Test each draft by asking a manager to explain it to their team in their own words; if they
cannot, it is too abstract.

Write the narrative next: half a page on how a typical working day, a customer interaction and a manager's role will
feel different in two to three years. This is where most staff will look for themselves, so be honest about roles that
will change. If leaders intend AI to reduce roles, the vision must not imply otherwise; employment questions go to HR
and, where relevant, staff representatives before anything is published.

Then agree the guiding principles. These are stances rather than rules: how the organisation treats its people, how
openly it uses AI with customers, who stays accountable, how it treats data, and its attitude to experimentation and
risk. Keep them few and plain. `ai-strategy:strategic-outcomes` will later turn them into decision rules and add the
explicit exclusions, so do not try to write policy here. Check coverage against the responsible AI and risk management
source records, summarised in your own words.

Play the result back on one page using the `ai-vision-and-principles` template and test it with a small, mixed group
of staff before publication. Watch for words that alarm people ("efficiency", "headcount", "replace") and for promises
the organisation cannot keep. Record what changed after testing. Finally, agree who owns the vision (normally the
executive sponsor), where it will be published and when it will be revisited.

## Outputs

- An AI vision on the `ai-vision-and-principles` template: purpose link, chosen ambition level with reasoning, vision statement, narrative of change, guiding principles, commitments to staff, owner and review date.
- A record of the staff test: who was consulted (by role or group), what they said and what changed.
- A short list of open questions for `ai-strategy:strategic-outcomes` and `ai-strategy:ai-roadmap` to resolve.

## Microsoft platform considerations

Not applicable to the vision itself, because the ambition must survive changes in Microsoft's products and names. Keep
product names out of the statement and principles. Where leaders want to illustrate the narrative with today's tools,
check current capability and naming against the source records in `references/sources.md` and label the examples as
illustrative.

## Adoption considerations

The vision is the first thing most staff will hear about AI, and it sets their expectations of everything that
follows. Hand it to `change-and-communications:ai-communication-strategy` for a deliberate rollout through managers, and
make sure managers hear it, with the reasoning, before their teams do.

## Knowledge considerations

Not applicable in detail at vision stage. Where the ambition depends on AI grounded in organisational knowledge, note
that dependency so the outcomes and roadmap address knowledge ownership early.

## Security and privacy considerations

A guiding principle on data should state that AI use respects existing confidentiality and data protection obligations.
Check the wording with the data protection officer and the security lead; legal interpretation belongs with them, not
with this skill.

## Responsible AI considerations

The guiding principles are the organisation's first public statement of how it intends to use AI responsibly. Check
that they address accountability, transparency, fairness and human oversight, and that nothing in the vision
contradicts them. Where the narrative implies AI informing decisions about people, flag it for
`responsible-ai:ai-impact-assessment` before publication.

## Evaluation requirements

Not applicable to solution testing. The vision is evaluated by whether a mixed group of staff can restate it
accurately after reading it once, and whether leaders can use it to settle a real disagreement about direction.

## Value measures

The vision does not carry benefit figures. Its effect is measured through staff understanding and sentiment about AI
(through existing surveys, reported at group level above an agreed minimum size), with the executive sponsor as owner,
and through the strategic outcomes that follow from it.

## Scale notes

### Starter

One leadership session and a one-page vision with three or four principles. The chief executive or a director owns
it, and it is tested informally with a handful of staff.

### Scale

Run the leadership session, then test drafts with staff from each major function and with staff representatives.
Publish with a short narrative per function showing what it means locally.

### Enterprise

Set the enterprise vision and principles centrally; business units write their own narrative beneath it without
changing the statement or principles. The board approves the ambition level, and the vision is reviewed with the
annual strategy cycle.

## Hand-offs

- To `ai-strategy:strategic-outcomes` to turn the vision into measurable outcomes, decision-rule principles and exclusions.
- To `ai-strategy:executive-sponsorship` to confirm the sponsor who will own and champion the vision.
- To `change-and-communications:ai-communication-strategy` to plan how it reaches the workforce.
- To `ai-strategy:investment-case` so the funding request matches the chosen ambition level.

## Reviewer gates

Not applicable. The vision is an executive decision, not a release. The `responsible-ai` department may be asked for
advice on the principles; the data protection officer and HR review anything touching personal data or roles.

## Failure modes

- The vision names a product ("Copilot everywhere"), so it dates within a year and says nothing about outcomes.
- Leaders choose a transformed ambition but fund a foundational one, and the gap surfaces as missed expectations.
- The narrative avoids the question of jobs, staff fill the silence with the worst interpretation, and adoption stalls.
- Principles are so generic ("we use AI responsibly") that they never shape a decision or reassure anyone.
- The vision is announced without manager briefing, and managers cannot answer their teams' first questions.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Write a vision statement that names a product or vendor feature instead of a change in work or service.
- Invent market, competitor or productivity statistics to justify an ambition level.
- Imply job security, or job reductions, that leaders have not decided and HR has not reviewed.
- Publish the vision before managers have been briefed and a group of staff has tested it.

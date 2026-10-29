---
name: prompting-practice
description: Teaches people to prompt Microsoft Copilot effectively and safely - stating goal, context, sources and expected output, iterating, choosing what not to enter - and to verify outputs by checking citations, numbers and omissions before use. Produces a prompting guide, a verification checklist and prompt library standards. Use when users get generic or wrong answers, when a prompt library is being built, or when verification habits are weak.
license: CC-BY-4.0
metadata:
  department: m365-copilot
  lifecycle: Enable, Improve
  maturity: explorer, adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-overview, ms-copilot-adoption-hub, ms-copilot-privacy, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Prompting practice

## Purpose

Most disappointment with Copilot comes from two habits: asking vague questions and trusting the answers without
checking. This skill builds the opposite habits across the workforce. It teaches a simple, durable way to ask Copilot
for help, what to keep out of a prompt, how to improve an answer by iterating, and how to verify an output before
relying on it. It also sets the standards for any shared prompt library. It goes wrong when prompting is taught as a
bag of tricks or magic phrases, which age quickly and leave people no better at judging the output.

## When to use

- Users report that Copilot gives generic, shallow or wrong answers.
- Someone is building a shared prompt library and needs standards for what goes in it.
- Verification is weak: outputs are forwarded without checking sources, numbers or omissions.
- Champions, trainers or managers need a consistent way to teach prompting.

## When not to use

- Writing the instructions that define an agent's behaviour - use `m365-agents:agent-instructions`.
- Engineering and versioning system prompts for a production Foundry solution - use `ai-foundry:foundry-prompt-engineering`.
- Designing role-specific, app-specific scenarios - use `m365-copilot:copilot-role-scenarios`.
- Building formal role curricula and learning pathways - use `learning-and-skills:ai-role-curriculum` or `learning-and-skills:ai-learning-pathway`.
- Facilitator materials for running sessions - use `learning-and-skills:facilitator-guide`.

## Questions to ask first

1. Which audiences are in scope, and which Copilot experiences do they have (Copilot Chat, licensed Microsoft 365 Copilot or both)?
2. What does the approved-use guidance say must never be entered into a prompt or referenced?
3. Where are people going wrong today: vague prompts, missing context, no iteration, or no checking?
4. Is there an existing prompt library, and who owns its quality?
5. Through which routes will people learn (onboarding, Champions, office hours, short videos)?

## Required inputs

- The organisation's approved-use guidance and data classification.
- Which Copilot experiences each audience has, confirmed by IT.
- Examples of real prompts and outputs that went wrong, shared voluntarily and anonymised.
- Any existing prompt library and the scenarios from `copilot-adoption:scenario-discovery`.

If approved-use guidance is missing, the "what not to enter" section cannot be written; flag it to the policy owner and
do not invent rules.

## Decision framework

Teach a small set of habits and check each one in practice.

| Habit | What good looks like | Signal it is missing |
|---|---|---|
| State the goal | The prompt says what the output is for and who will read it | Generic answers that fit any situation |
| Give context and sources | The prompt names the files, meetings or threads to use, or attaches them | Answers drawn from the wrong material, or invented detail |
| Set expectations | Format, length, tone and structure are specified | Repeated reformatting by hand |
| Iterate | The person refines with follow-up prompts instead of starting again | One-shot use, then abandonment |
| Keep out what must stay out | Prohibited content is never entered or referenced | Sensitive data appears in prompts against guidance |
| Verify before use | Citations opened, numbers recalculated, omissions considered | Outputs forwarded unchanged with errors |

Prompt library entries must meet a standard: a named scenario and audience, editable placeholders explained in words,
the sources it expects, a verification step, an owner and a review date. Entries without a verification step are not
published.

## Practitioner approach

Teach prompting as a conversation with a capable but uninformed colleague. Copilot does not know the purpose, the
audience or which of a person's hundreds of files matter unless told. A simple frame works across apps: goal, context,
sources, expectations. "Draft a two-paragraph update for the steering group on the supplier delay, using the notes from
Tuesday's meeting and the latest risk log, in a neutral tone" beats "write an update" every time. Avoid naming the frame
after a product feature; it should still work when the interface changes.

Show iteration explicitly. Many people abandon Copilot after one disappointing answer. Demonstrate asking for a shorter
version, a different audience, a table instead of prose, or "what have you not covered?". Iteration is where most of the
quality comes from.

Spend as long on verification as on prompting. Teach people to open the cited sources and confirm the claim is there,
to recalculate any number that matters, to ask themselves what is missing, and to be most careful when the output
sounds most confident. Give them a short verification checklist they can keep beside them. Explain why: Copilot can
only use what the person can access, can miss recent or poorly stored content, and can still be wrong about content it
did find.

Be concrete about what stays out. Translate the approved-use guidance into examples people recognise in their role, and
tell them what to do instead. Rules that only exist in a policy document are not followed.

Use real examples. Collect, with permission and anonymised, prompts that worked and prompts that failed in the
organisation's own work, and use them in sessions. Pair each with its verification step.

For any shared prompt library, apply the entry standard and give it an owner. Libraries rot quickly; review entries on a
cycle, retire those nobody uses, and prefer fewer, well-tested prompts linked to scenarios over hundreds of untested
ones. Measure capability through demonstrated practice at group level, never by inspecting individuals' prompts.

## Outputs

- A prompting and verification guide for the organisation, in plain language with role examples.
- A one-page verification checklist.
- Prompt library standards and an initial set of reviewed entries, linked to the `scenario-catalogue`.
- Short teaching materials that Champions and trainers can reuse.

## Microsoft platform considerations

Copilot Chat and licensed Microsoft 365 Copilot differ in the work context they can draw on, and each app offers
different ways to reference files, meetings and messages. Capability and interface details change often; keep teaching
materials anchored on habits and check `ms-copilot-overview` before showing interface specifics. How prompts and
responses are handled is described in `ms-copilot-privacy`.

## Adoption considerations

Prompting improves through practice, not slides. Embed the habits in onboarding, office hours and Champion challenges
through `copilot-adoption:launch-plan` and `champions:champion-challenges`, and reinforce them with short, regular
examples rather than one long course.

## Knowledge considerations

Not applicable in depth, because the skill teaches individual habits; where many people repeatedly need the same
curated knowledge, route the need to `m365-agents:agent-opportunity-assessment` instead of a longer prompt.

## Security and privacy considerations

The "what stays out" section must match the approved-use guidance exactly, and examples must be anonymised. Prompts and
responses may be stored and discoverable under the organisation's retention policy; tell people this plainly, based on
the current source records and the records management position.

## Responsible AI considerations

People remain accountable for what they do with an output. Teach that Copilot drafts and suggests; it does not decide.
Prompts that ask Copilot to judge or rank colleagues, or to make decisions about people, are outside approved use unless
the organisation has an approved process.

## Evaluation requirements

Check the guide with a small group from different roles: can they apply the frame to their own task and catch a planted
error in an output using the checklist? Revise until most can.

## Value measures

Measure at group level: confidence and reported quality before and after sessions, the share of published library
entries with verification steps, and reductions in support questions about poor answers. The adoption lead owns these
measures. Never review or score an individual's prompts.

## Scale notes

### Starter

One short guide, one checklist, and a monthly drop-in session run by the Copilot lead or a partner.

### Scale

Guide and checklist embedded in onboarding, a curated prompt library with owners, and Champions running practice
sessions by role.

### Enterprise

Localised guides by region and language, a governed library with business-unit curators, and links into formal
learning pathways.

## Hand-offs

- To `learning-and-skills:ai-role-curriculum` to embed the habits in role curricula.
- To `champions:champion-challenges` for practice challenges.
- To `m365-copilot:copilot-role-scenarios` for app-specific scenario cards.
- To `m365-agents:agent-opportunity-assessment` when a prompt pattern becomes a shared, knowledge-heavy need.

## Reviewer gates

Not applicable as a formal gate, because the guide covers individual use at low risk tiers; the "what stays out"
section is checked with the `security-privacy` department before publication.

## Failure modes

- Prompting is taught as magic phrases that stop working when the product changes.
- Verification is mentioned once and never practised, so errors flow into real work.
- The prompt library grows into hundreds of untested entries that nobody owns.
- Examples use real sensitive content, teaching the opposite of the guidance.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Teach prompting without teaching verification.
- Publish library prompts without an owner, a scenario and a verification step.
- Inspect, score or rank individuals' prompts.
- Use real sensitive content in teaching examples.

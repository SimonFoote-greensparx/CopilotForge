---
name: copilot-role-scenarios
description: Turns a prioritised role task into worked Copilot scenarios across the Microsoft 365 apps, specifying the app surface, the work context it draws on, the prompt pattern, the verification step, prerequisites and known limits, each tested hands-on with people in the role. Use when a role needs concrete app-by-app guidance, when scenarios fail in practice, or when a role's apps or content change.
license: CC-BY-4.0
metadata:
  department: m365-copilot
  lifecycle: Envision, Enable, Improve
  maturity: adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: m365-copilot, copilot-chat
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-overview, ms-copilot-adoption-hub, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Copilot role scenarios

## Purpose

A scenario catalogue says which tasks matter to a role; it does not yet say how Copilot helps in Outlook on Monday
morning, in Teams after a meeting or in Excel at month end. This skill does that product-specialist work: for each
prioritised task it chooses the app surface, names the work context Copilot will draw on, writes the prompt pattern and
the verification step, records prerequisites and known limits, and tests the result with people in the role. It
usually goes wrong when scenarios are written from demonstrations on perfect sample data, so they collapse on real
mailboxes, half-recorded meetings and spreadsheets that are not formatted as tables.

## When to use

- A role has prioritised tasks from scenario discovery and now needs concrete, app-specific guidance.
- People in a role say the published scenarios do not work on their content.
- A role's working pattern changes, for example a move to a new app or a new reporting process.
- Microsoft adds or changes Copilot capability in an app that a role depends on.

## When not to use

- Discovering and prioritising which tasks each persona should use Copilot for - use `copilot-adoption:scenario-discovery`.
- Designing the adoption journey for a priority role, with onboarding, practice and reinforcement - use `copilot-adoption:role-based-adoption`.
- Redesigning a whole department workflow that spans several roles - use `m365-copilot:department-scenario-design`.
- Teaching prompting and verification as a general skill - use `m365-copilot:prompting-practice`.
- A recurring need that many people share and that needs curated knowledge - use `m365-agents:agent-opportunity-assessment`.

## Questions to ask first

1. Which prioritised tasks for this role are in scope, and who in the role will test them with you?
2. In which app does the person actually do each task, on which device, and where does the input content live?
3. What must be true of that content for Copilot to help (stored in Microsoft 365, recorded or transcribed, structured as a table)?
4. How will the person check the output, and what would a wrong answer cost?
5. Which Copilot capabilities in these apps has the organisation enabled for this role, confirmed by IT?

## Required inputs

- The role's prioritised tasks from the `scenario-catalogue` maintained by `copilot-adoption:scenario-discovery`.
- Access to two or three people in the role, using their real content with their consent.
- The capability and settings position for the role, from `m365-copilot:copilot-technical-readiness`.
- The organisation's approved-use guidance and data classification.

If a capability's availability for the role is unconfirmed, mark the scenario "to confirm" and do not publish it.
Never write a scenario from a product demonstration without testing it on real work.

## Decision framework

For each task, choose the surface and pattern with this table, then test.

| Task shape | Usual surface | Work context it depends on | Typical verification |
|---|---|---|---|
| Catching up on what happened | Teams meeting or chat recap, Outlook thread summary | Recordings or transcripts, complete threads | Check actions and decisions against the transcript or source messages |
| Drafting from existing material | Word or Outlook drafting with referenced files | Source files in OneDrive or SharePoint the person can open | Compare claims to referenced files; check tone and audience |
| Analysing structured data | Excel | Data formatted as a table in a supported location | Recalculate a sample; check filters and totals |
| Building a presentation | PowerPoint from a document or outline | A clear source document | Check every number and claim against the source |
| Finding and synthesising across work | Microsoft 365 Copilot Chat with work grounding | Mail, files, meetings and chats the person can access | Open the cited sources; confirm nothing important is missing |

Publish a scenario only when people in the role have tested it on real content, the verification step works, and the
known limits are written down. A scenario that needs content changes first goes to work context readiness.

## Practitioner approach

Sit with someone in the role and watch them do the task the usual way before introducing Copilot. Note where the input
lives, how long the task takes, what they check and what goes wrong. That observation tells you which app surface fits,
and whether the work context is good enough. Many scenarios fail not because of the prompt but because the meeting was
not recorded, the data was not a table, or the relevant files sat on a local drive.

Write each scenario as a short card: the task in the role's words, the app and the moment in the working day, the work
context it relies on, a prompt pattern with the parts the person fills in, the verification step, and the known limits.
Prompt patterns should name the goal, the sources to use, the audience and the expected format. Keep them editable; a
copied prompt that nobody adapts produces generic output.

Test each card with two or three people on their real content, with their consent, and note where it broke. Adjust the
pattern, the prerequisites or the verification step, and test again. If a scenario only works after content changes,
record that dependency and pass it to `m365-copilot:work-context-readiness` instead of publishing a scenario that will
disappoint.

Be explicit about the limits. Say where Copilot is likely to miss content (for example, items the person cannot access,
or very recent content), where numbers must be recalculated, and where the output must not be used without a second
check. Users trust scenarios that admit their limits more than ones that promise everything.

Group cards by role and by moment in the working week (preparing, meeting, following up, reporting) rather than by app,
because that is how people think about their work. Add the cards to the organisation's `scenario-catalogue` with an
owner from the role, and agree when they will be re-tested. Capability in each app changes often, so check the source
records and re-test the cards when Microsoft announces changes to an app the role depends on.

## Outputs

- A set of scenario cards per role, recorded in the `scenario-catalogue`: task, app surface, work context, prompt pattern, verification step, prerequisites, known limits, owner and re-test date.
- A list of content and configuration dependencies passed to work context readiness and technical readiness.
- Notes from hands-on testing showing which scenarios were published, revised or dropped and why.

## Microsoft platform considerations

Copilot behaves differently in each Microsoft 365 app, draws only on content the user can access, and depends on
content being stored, recorded and structured in ways the app supports. Capabilities, app coverage and prerequisites
change frequently, so check `ms-copilot-overview` and the current product documentation before publishing a card, and
record the date checked.

## Adoption considerations

Scenario cards are the raw material for onboarding and Champions. Share them through `copilot-adoption:role-based-adoption`
and `copilot-adoption:launch-plan`, and invite people in the role to propose improvements so the cards stay real.

## Knowledge considerations

Where a scenario depends on shared team content, name the content and its owner on the card. Persistent gaps in shared
content are routed to the `knowledge-management` department rather than worked around in prompts.

## Security and privacy considerations

Cards must never encourage people to paste content into prompts that their guidance prohibits, or to reference content
they should not share. Testing uses real content only with the person's consent and stays within their own access.

## Responsible AI considerations

Any scenario touching decisions about people, money, safety or rights carries an explicit human check and a note that
Copilot output is a draft, not a decision. Scenarios that would summarise or judge an individual's performance are not
published.

## Evaluation requirements

Each card is tested by at least two people in the role on real content, with the result recorded as usable, usable with
edits, or not usable. Cards are re-tested after material app changes.

## Value measures

Use the task baseline observed before Copilot (time, rework, delay) and ask scenario owners to track the effect at team
or role level after adoption. The scenario owner in the role owns the measure.

## Scale notes

### Starter

Three to five cards for one or two roles, tested by the specialist with a handful of users, are enough to start.

### Scale

A card set for each priority role, maintained by role owners with Champions, with re-testing tied to the Microsoft
change cycle.

### Enterprise

A shared card library with local variants by business unit or region, governed by a single owner per role family and
linked to learning pathways.

## Hand-offs

- To `copilot-adoption:role-based-adoption` and `copilot-adoption:launch-plan` for onboarding and journeys.
- To `m365-copilot:work-context-readiness` for content dependencies.
- To `m365-copilot:prompting-practice` for the general prompting and verification habits the cards rely on.
- To `m365-agents:agent-opportunity-assessment` when many people repeat the same knowledge-heavy task.

## Reviewer gates

Not applicable for most cards, which sit at risk tier 0 or 1 and use people's own content. Cards that touch decisions
about people or highly sensitive content are referred to `responsible-ai` or `security-privacy` before publication.

## Failure modes

- Cards are written from demonstrations, and fail on real mailboxes, meetings and spreadsheets.
- Verification steps are omitted, so people pass on confident but incomplete summaries.
- Content prerequisites are hidden, and users conclude Copilot does not work for them.
- Cards are never re-tested, and drift out of step with the apps.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Publish a scenario that has not been tested on real content by people in the role.
- Omit the verification step or the known limits from a scenario card.
- Assert app capability or availability from memory rather than the current source records.
- Publish scenarios that judge or summarise an individual's performance.

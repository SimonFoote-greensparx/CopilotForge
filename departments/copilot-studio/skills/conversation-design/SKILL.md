---
name: conversation-design
description: Designs how a Copilot Studio agent talks to people - greeting and AI disclosure, tone, clarifying questions, confirmations, error and fallback messages, escalation and live-agent hand-off with context, and ending a conversation well - so exchanges are short, honest and recoverable. Use when writing an agent's conversational behaviour, when users abandon or go round in loops, or when a hand-off to people needs designing.
license: CC-BY-4.0
metadata:
  department: copilot-studio
  lifecycle: Deliver, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: copilot-studio, m365-agents
  edition-support: starter, scale, enterprise
  reviewers: responsible-ai
  sources: ms-copilot-studio-guidance, ms-responsible-ai, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# Conversation design

## Purpose

People judge an agent by how the conversation feels: whether it is clear what the agent is, whether it asks sensible
questions, whether it admits what it cannot do and whether it gets them to a person when they need one. This skill
designs those behaviours for a Copilot Studio agent - disclosure, tone, clarification, confirmation, fallback, escalation
and closure. Conversation design usually goes wrong when defaults are left untouched, when the agent asks one question
too many or one too few, and when escalation drops the user into a queue with no context so they must start again.

## When to use

- A Studio agent's conversational behaviour needs designing before build or before a wider release.
- Users abandon conversations, repeat themselves or go round the fallback loop.
- The agent must hand off to a person, a contact centre or a live-agent platform.
- The agent's tone or disclosure needs aligning with the organisation's voice or regulatory expectations.

## When not to use

- Deciding which requests are handled by topics, tools or generative orchestration - use `copilot-studio:topics-and-orchestration`.
- Writing the agent's general instructions for any agent type - use `m365-agents:agent-instructions`.
- Transparency obligations to users and affected people as a formal review - use `responsible-ai:ai-transparency`.
- Hand-offs between agents rather than to people - use `copilot-studio:multi-agent-design`.

## Questions to ask first

1. Who are the users, what state are they likely to be in (rushed, worried, expert) and what voice suits them?
2. What must users be told at the start - that this is an AI agent, what it can do, and how their data is used?
3. When should the agent ask a clarifying question rather than answer, and when should it simply try?
4. Where does a person take over, how is the user's context passed, and what happens out of hours?
5. What does a good ending look like - a resolved question, a reference number, a booked follow-up?

## Required inputs

- The solution design, request-to-mechanism map and exclusions.
- The organisation's tone of voice guidance and any mandated wording, with owners.
- The escalation routes: teams, queues, live-agent platform, hours of cover and contact details.
- Privacy information that must be presented, from `security-privacy:privacy-assessment` where personal data is involved.

If escalation routes are not agreed, the agent cannot promise a hand-off; record the gap and design an honest message
pointing to an existing contact route instead.

## Decision framework

| Moment | Default behaviour | Design rule |
|---|---|---|
| Start | Short greeting, disclosure that it is an AI agent, two or three examples of what it can do | Never pretend to be a person |
| Unclear request | Ask one targeted clarifying question with options | Do not ask more than needed; if two attempts fail, offer a route out |
| Answer | Lead with the answer, cite the source, keep it short | Offer detail rather than front-loading it |
| Before an action | Summarise what will happen and ask to confirm | Plain language, no system jargon |
| Cannot help | Say so plainly, say why if useful, and offer a next step | Never invent an answer to avoid saying no |
| Escalation | Offer a person when asked, when stuck, or when the topic is sensitive | Pass context so the user does not repeat themselves |
| End | Confirm the outcome, give a reference if one exists, invite feedback | Do not trap users in "anything else?" loops |

## Practitioner approach

Write sample conversations before writing any messages. Take five to ten representative requests, including an awkward
one, a sensitive one and one the agent must decline, and script how a good human expert would handle each. These scripts
set the length, tone and rhythm the agent should match, and they become test cases.

Open honestly and usefully. Tell users they are talking to an AI agent, what it can help with and where to go for anything
else. Two or three concrete examples beat a paragraph of capabilities. If personal data is processed, link to the privacy
information agreed with the privacy owner rather than paraphrasing it.

Calibrate clarification. Generative orchestration can ask follow-up questions on its own; decide where that is wanted.
Ask a clarifying question when acting on a wrong guess would cost the user time or cause harm, and offer choices rather
than open questions where the options are known. When the user is vague but the cost of a wrong guess is low, answer
and offer to refine. After two failed clarifications, stop asking and offer another route.

Design the unhappy paths as carefully as the happy ones. Customise the fallback, error and escalation system topics so
they use the organisation's language and real routes. A fallback that says only "I didn't understand" teaches users to
leave; one that suggests what the agent can do and offers a person keeps them.

Make escalation seamless. Decide the triggers - user asks, repeated failure, sensitive subject, high-value request - and
the destination for each. Where a live-agent platform is used, pass a summary of the conversation and key variables so
the person picking it up does not ask the same questions. Tell users honestly about waiting times and out-of-hours
cover, and offer an alternative when no one is available.

Keep the voice consistent. Agree a short style sheet: sentence length, formality, how to address users, words to avoid,
and how to express uncertainty. Apply it to authored messages and reflect it in instructions for generated answers.

End conversations deliberately, confirming outcomes and references. Then review real transcripts with the business owner
after launch, at aggregate level, and refine wording where users stall.

## Outputs

- Sample conversations for representative, sensitive and declined requests.
- A conversation style sheet: voice, length, disclosure wording, uncertainty phrasing and words to avoid.
- System topic specifications for greeting, fallback, error, escalation and end of conversation.
- An escalation map: triggers, destinations, context passed, hours and the out-of-hours message.
- The conversation section of the `studio-solution-design`.

## Microsoft platform considerations

Copilot Studio provides system topics, generative answers and integrations with live-agent and contact centre platforms,
and their behaviour and the channels that support them change over time. Check `ms-copilot-studio-guidance` for current
hand-off options and channel formatting before designing rich cards or hand-off context that a channel may not support.

## Adoption considerations

The first conversation decides whether a user returns. Test the greeting and the first three turns with real users, and
use launch materials to show good example requests that match what the agent does well.

## Knowledge considerations

Answer style depends on knowledge quality; an agent cannot be concise when sources are long and contradictory. Report
patterns of vague or conflicting answers to `copilot-studio:studio-knowledge-architecture`.

## Security and privacy considerations

Do not ask for personal or sensitive information the purpose does not need, and never ask users to type passwords or
secrets. Escalation summaries contain conversation content; pass only what the receiving person needs. Present privacy
information agreed under `security-privacy:privacy-assessment`.

## Responsible AI considerations

Disclose that the agent is AI, express uncertainty honestly, avoid human-like claims of feelings or certainty, and always
offer a route to a person for sensitive subjects or decisions that affect people. Align disclosure wording with
`responsible-ai:ai-transparency`.

## Evaluation requirements

Use the sample conversations as test cases, and assess tone, clarity, honest declining, escalation triggering and context
passing. Failing to disclose AI status or failing to offer a person on a sensitive topic is a zero-tolerance failure.

## Value measures

Track abandonment, escalation rate and reason, repeat contacts after hand-off and user satisfaction, at agent level and
owned by the business owner. Never assess individual users or the people who receive escalations from these measures.

## Scale notes

### Starter

Customise greeting, fallback and escalation with real routes, disclose AI status and write five sample conversations.

### Scale

Publish an organisation-wide conversation style sheet and reusable system topic patterns so agents feel consistent, and
review transcripts at aggregate level quarterly.

### Enterprise

Maintain conversation standards with the brand and accessibility owners, standard hand-off integrations with contact
centres and periodic conversation reviews across the portfolio.

## Hand-offs

- To `copilot-studio:topics-and-orchestration` with system topic behaviour and clarification rules.
- To `responsible-ai:ai-transparency` for disclosure wording from tier 2.
- To `copilot-studio:studio-testing-and-evaluation` with sample conversations as test cases.
- To `copilot-studio:studio-analytics` to monitor abandonment and escalation after launch.

## Reviewer gates

From risk tier 2, `responsible-ai` reviews disclosure, uncertainty handling and access to a person, especially where the
agent serves the public or touches decisions about people. Missing AI disclosure is a blocking finding at any tier.

## Failure modes

- Default fallback messages send users round a loop with no way out.
- Escalation passes no context, so users repeat everything to a person and lose trust in both.
- The agent asks so many clarifying questions that users give up before getting an answer.
- The agent presents itself as a person or hides that answers are AI-generated.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Let an agent present itself as a person or hide that it is AI.
- Trap users in fallback loops without offering another route.
- Ask users for passwords, secrets or personal data the purpose does not need.
- Promise a hand-off to a person when no escalation route has been agreed.

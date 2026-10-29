---
name: agent-grounding
description: Configures and controls what a Microsoft 365 agent grounds on - choosing specific sites, libraries, files or connectors rather than broad locations, deciding on web content, restricting answers to named sources, checking permission trimming and citations - and keeps a controlled knowledge list with owners and change approval. Use when a maker is adding knowledge to an agent, when answers come from the wrong places, or when knowledge changes.
license: CC-BY-4.0
metadata:
  department: m365-agents
  lifecycle: Deliver, Assure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3
  platforms: m365-agents, copilot-studio, sharepoint
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, evaluation-quality
  sources: ms-agent-builder, ms-declarative-agents, ms-agents-extensibility, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Agent grounding

## Purpose

An agent answers from what it is pointed at, so the grounding configuration decides both the quality of its answers and
what it can expose. This skill takes sources that have passed readiness and configures them precisely: the specific
sites, libraries, folders, files or connectors, whether web content is used, whether answers are restricted to the named
sources, and how citations appear. It then keeps that configuration under control as sources change. Grounding usually
goes wrong when a maker adds a whole site or a whole drive because it is quicker, so the agent answers from drafts,
archives and content the audience should never have been able to find.

## When to use

- A maker is about to add knowledge to an agent built from an agreed brief.
- An agent's answers come from the wrong documents, old versions or unexpected locations.
- A knowledge source is moving, being restructured or being retired.
- Someone wants to add a new source or turn on web content for a live agent.

## When not to use

- Judging whether a source is fit to ground on (owner, currency, accuracy, permissions) - use `m365-agents:knowledge-source-readiness`.
- Designing knowledge sources and retrieval for Copilot Studio agents in depth - use `copilot-studio:studio-knowledge-architecture`.
- Designing indexing, chunking and search for a custom AI solution - use `ai-foundry:retrieval-design`.
- Setting organisation-wide standards that content must meet before agents ground on it - use `knowledge-management:knowledge-grounding-standards`.
- Keeping knowledge current once the agent is in operation - use `ai-operations:knowledge-refresh`.

## Questions to ask first

1. Which sources did the brief name, and what readiness verdict has each received?
2. What is the narrowest scope within each source that covers the in-scope questions (site, library, folder or file)?
3. Should the agent use web content or only the named sources, and why?
4. Can every intended user already open each source, and should anyone who can open it be excluded from the audience?
5. Who approves a change to the knowledge list, and how is it tested?

## Required inputs

- The agent brief with in-scope questions and named sources.
- A readiness verdict for each source from `m365-agents:knowledge-source-readiness`.
- The intended audience and sharing scope.
- The evaluation set from `m365-agents:agent-testing`, including permission-trimming tests.

A source without a ready or ready-with-conditions verdict is not added. Never widen a source's scope to make an answer
work; fix the content or its location instead.

## Decision framework

| Decision | Default | Change only when |
|---|---|---|
| Scope within a source | The narrowest folder, library or file set that covers the in-scope questions | Evidence shows needed content sits outside it and that content is ready |
| Whole sites or drives | Avoid | The whole site is curated for this purpose and owned |
| Web content | Off for organisational knowledge agents | The brief needs public information and the business owner accepts the trade-off |
| Restrict to named sources | On, where the build path supports it | The agent's purpose depends on general knowledge, recorded in the brief |
| Connectors to other systems | Only with an owner, an access model and a security review | Never as a shortcut to content that should be in governed locations |
| Citations | Shown for factual answers | The format does not support them, and users are told how to verify |

Every source in the configuration appears on a knowledge list with location, scope, owner, readiness verdict, review date
and the date it was added.

## Practitioner approach

Start with the in-scope questions and work backwards to content. For each representative question, find the document
that should answer it. That tells you exactly which folders and files the agent needs, and usually reveals that the
answer lives in a small, well-defined part of a large site. Point the agent at that part, not the whole site.

Check permissions from the user's side. Agents answer with the permissions of the person asking, so the question is not
"can the agent see this?" but "can each intended user see this, and should they?". If the intended audience cannot open a
source, the agent will not answer from it for them; if a source is open to far more people than intended, the agent makes
that oversharing easier to exploit. Resolve either problem at the source with its owner, not by adjusting the agent.

Decide about web content deliberately. For agents that answer from organisational policy or procedure, mixing in web
content blurs the authority of the answer. Leave it off unless the brief needs it and the owner accepts the trade-off,
and check in the source records how the setting behaves in the build path you are using.

Where the build path allows the agent to answer only from named sources, use that setting for knowledge agents, and
test that it holds. Confirm the current options and their behaviour in the source records, because they change.

Configure citations so users can open the source behind an answer, and test that the citations point to the current
version. Stale copies in other locations are a common cause of confident but outdated answers.

Run the grounding tests from `m365-agents:agent-testing`: questions answered from the right source, questions that should
find nothing, and permission tests with users inside and outside the audience. Record results against the configuration
version.

Put the knowledge list under change control. Adding, widening or removing a source is a change that needs the business
owner's approval, a readiness verdict and a regression run. Link each source's review date to its owner's review cycle,
so a policy update prompts a check of the agent.

## Outputs

- A grounding configuration record and knowledge list: each source with location, scope, owner, readiness verdict, web content and restriction settings, review date and date added.
- Grounding and permission test results tied to the configuration version.
- A change rule for the knowledge list recorded on the `agent-card`.

## Microsoft platform considerations

Agent Builder, declarative agents and Copilot Studio each offer different knowledge source types, scoping options, web
content settings, connector options and limits, described in `ms-agent-builder`, `ms-declarative-agents` and
`ms-agents-extensibility`. Permission-trimmed grounding is described in `ms-copilot-privacy`. These change often; check
the current records before configuring, and never assert a limit or setting from memory.

## Adoption considerations

Users trust agents whose answers cite sources they recognise. Tell users in the launch message where the agent's answers
come from and how to report one that looks wrong.

## Knowledge considerations

Grounding quality is capped by the content. Prefer a small, curated, owned source over a large, mixed one, and route
structural content problems to the `knowledge-management` department, especially
`knowledge-management:ai-ready-content` for how documents are written and structured.

## Security and privacy considerations

Broad sources and connectors widen what an agent can surface. From tier 2, every source and connector is part of the
`security-privacy:data-exposure-review`, and any connector also goes through `security-privacy:connector-review`.
Instructions are never used in place of restricting content.

## Responsible AI considerations

Answers must be traceable to sources. Where knowledge covers matters that affect people's rights, pay or safety, ensure
the agent cites the authoritative document and redirects to a person for individual cases.

## Evaluation requirements

Grounding tests must show answers come from the intended sources, that out-of-scope questions do not draw on unrelated
content, and that users outside the audience cannot obtain restricted answers. Re-run after any change to the knowledge
list.

## Value measures

Track the share of evaluation answers grounded in the intended source and, in operation, feedback flagging wrong or
outdated answers, at audience level. The business owner owns these measures with the knowledge owners.

## Scale notes

### Starter

Two or three narrowly scoped sources with named owners, web content off, and a simple knowledge list kept with the
agent's brief.

### Scale

A standard knowledge list per agent, grounding tests as part of every release, and knowledge changes approved through
the CoE cadence.

### Enterprise

Curated knowledge locations designed for agents across business units, connectors governed centrally, and knowledge
lists linked to the knowledge owners' review cycles.

## Hand-offs

- To `m365-agents:agent-testing` for grounding and permission tests after each change.
- To `security-privacy:data-exposure-review` and `security-privacy:connector-review` from tier 2.
- To `ai-operations:knowledge-refresh` for keeping knowledge current in operation.
- Back to `m365-agents:knowledge-source-readiness` when a source's condition changes.

## Reviewer gates

From risk tier 2, `security-privacy` reviews every source and connector for exposure, and from tier 3
`evaluation-quality` confirms grounding test evidence; each finding is blocking or advisory, and blocking findings stop
release or the change.

## Failure modes

- A whole site is added for convenience, and the agent answers from drafts and archives.
- Web content is left on, and the agent mixes public material with policy as if both were authoritative.
- A source is widened after review, so the agent reaches content reviewers never saw.
- Citations point to stale copies, and users act on outdated information.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Add a source without a readiness verdict and an owner.
- Point an agent at a whole site or drive when a narrower scope covers the need.
- Use instructions in place of restricting content that users should not see.
- Change the knowledge list without approval and a regression run.

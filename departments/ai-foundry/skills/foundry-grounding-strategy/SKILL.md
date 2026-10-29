---
name: foundry-grounding-strategy
description: Chooses how a Microsoft Foundry solution grounds its answers and actions - supplied context, retrieval over indexed content, live lookups through tools, web grounding or none - per knowledge need, with ownership, permissions, freshness and citation decided before retrieval is engineered. Use when a Foundry agent needs organisational knowledge, when answers are confidently wrong, or when a team proposes fine-tuning to teach facts.
license: CC-BY-4.0
metadata:
  department: ai-foundry
  lifecycle: Mobilise, Deliver, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, sharepoint, fabric
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, evaluation-quality, design-authority
  sources: ms-foundry-models, ms-agents-extensibility, ico-ai-data-protection, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Foundry grounding strategy

## Purpose

A model answers from what it was trained on unless the solution gives it something better, and for most organisational
work the answer must come from the organisation's own, current, permitted information. This skill decides, for each
kind of knowledge the solution needs, how it reaches the model: supplied directly in context, retrieved from an index,
looked up live through a tool, taken from the web, or not needed at all. It settles ownership, permissions, freshness
and citation before anyone starts tuning chunk sizes. Grounding goes wrong when every need is pushed into one vector
index, when the index ignores who may see what, and when fine-tuning is used to teach facts that change every month.

## When to use

- A Foundry agent or application has been approved and needs organisational knowledge or data to answer or act.
- Answers are fluent but wrong, out of date, or uncited, and the team suspects the grounding.
- A team proposes fine-tuning a model so it "knows" the organisation's policies or products.
- Structured business data and unstructured documents both need to inform the same answer.
- Someone asks whether the solution should use web search.

## When not to use

- Engineering the index, chunking, embedding, ranking and filters once retrieval is chosen - use `ai-foundry:retrieval-design`.
- Organisation-wide grounding patterns across Microsoft 365, Copilot Studio and Foundry - use `ai-architecture:grounding-patterns`.
- Grounding a Microsoft 365 agent - use `m365-agents:agent-grounding`.
- Knowledge sources for a Copilot Studio agent - use `copilot-studio:studio-knowledge-architecture`.
- Setting the standards content must meet before agents use it - use `knowledge-management:knowledge-grounding-standards`.

## Questions to ask first

1. What questions or tasks must the solution handle, and for each, what information would a capable person consult to do it well?
2. Is that information documents, structured records, live transactional data or public information, and who owns each source?
3. Do different users have different rights to the same source, and must answers respect those rights?
4. How quickly does each source change, and how stale may an answer be before it causes harm?
5. Must users be able to see where an answer came from?

## Required inputs

- The agent or solution architecture, with its users and their access model.
- A knowledge inventory for the sources in scope, with owners and condition, from `knowledge-management:knowledge-inventory` where it exists.
- Data classification of each source, from `data-governance:data-classification-for-ai` where it exists.
- A set of real questions or tasks with known good answers, to test the strategy.

Where a source has no owner or its classification is unknown, mark it `[To confirm: ...]` and leave it out of
grounding. Ungoverned content grounded into an AI answer becomes an authoritative-sounding error.

## Decision framework

Choose per knowledge need, not per solution. Most solutions combine two or three approaches.

| Knowledge need | Usual approach | Avoid when |
|---|---|---|
| Small, stable, shared reference (a policy summary, a product list) | Supply it directly in instructions or context | It is large, changes often or differs by user |
| Large body of documents, read-only | Retrieval over an index, with permission trimming and citations | Content is unowned or poorly maintained; fix it first |
| Current records or transactions (an order, a case, a balance) | Live lookup through a tool with user-delegated access | Read-only snapshots are acceptable and cheaper |
| Analytical questions over structured data | A query tool against a governed data product, with the model forming the query and code validating it | Free-form query generation against production systems |
| Public, current information | Web grounding, only when the use case needs it and its terms and data flows are accepted | Organisational or personal data could be sent outside the boundary |
| Style, format or domain behaviour | Prompt engineering first; fine-tuning only with evidence | The real need is facts, which fine-tuning does not keep current |

Fine-tuning changes how a model behaves, not what it reliably knows; it is never the grounding strategy for facts.

## Practitioner approach

List the knowledge needs before the sources. Take the real questions and tasks and, for each, write what a capable
person would look at to answer it. Group them into needs: reference text, document bodies, live records, analytical
data, public facts. This stops the conversation starting with a vector database and ending with an index of everything.

Test each source before choosing an approach for it. Who owns it, is it current, is it duplicated elsewhere, and is it
classified? A retrieval index amplifies whatever is in the source, including obsolete versions and drafts. Where
content is in poor condition, the strategy carries a precondition to clean it with the `knowledge-management`
department, and the solution waits or launches with that source excluded.

Decide permissions next, because they constrain everything else. If users have different rights to the same content,
answers must be trimmed to the user, either by retrieval that applies the user's identity or security filters, or by a
live lookup that runs as the user. A single service identity that can read everything, feeding everyone, is the
commonest serious grounding flaw. Record which approach enforces permissions for each need.

Match freshness to harm. For each need, agree how stale an answer may be and choose the approach that meets it: live
lookup for transactional data, scheduled re-indexing for documents, with the interval set by the owner. Record the
refresh route and its owner.

Decide citation behaviour. For any answer that someone may rely on, the solution should show where it came from so the
user can check. Design the grounding so that sources are traceable to a document or record, and decide what the
solution does when nothing relevant is found: say so and hand over, never answer from the model's general knowledge
as if it were organisational fact.

Treat external and user-supplied content as untrusted. Retrieved documents, mail and web pages can carry instructions
aimed at the model, so grounding content must never be able to trigger tools or change the solution's behaviour.

Write the strategy as a table of needs, approach, source, owner, permission method, freshness and citation, and pass
retrieval needs to `ai-foundry:retrieval-design`. Test it early with the real questions, looking separately at whether
the right content was found and whether the answer used it faithfully. State what the strategy cannot determine:
whether retrieval quality is good enough, which only groundedness testing shows.

## Outputs

- The grounding section of the `foundry-solution-design` template: knowledge needs, approach per need, sources and owners, permission enforcement, freshness and refresh route, citation and no-answer behaviour.
- A list of content preconditions handed to the `knowledge-management` department.
- A retrieval brief for `ai-foundry:retrieval-design` covering each need that uses an index.

## Microsoft platform considerations

Foundry can ground agents through several kinds of knowledge connection, including search indexes, files, connections
to Microsoft 365 and data platforms, tools and web grounding, and the options, their permission handling and their
preview status change frequently. Web grounding may involve services with separate terms and data flows outside the
Azure boundary. Check the current source records for what each connection supports, especially whether it honours
user permissions, before designing around it.

## Adoption considerations

Users trust grounded answers more when they can see the source, and stop trusting the whole solution after one
confident wrong answer. Explain what the solution knows and does not know at launch, and give people an easy way to
report a wrong or outdated answer.

## Knowledge considerations

This skill depends on knowledge being owned, current and classified. Each grounded source needs an owner who accepts
that an AI solution relies on it and a review cycle through `knowledge-management:knowledge-review-cycles`. Questions
the solution cannot answer are a signal for `knowledge-management:knowledge-gap-analysis`.

## Security and privacy considerations

Grounding is where oversharing happens. Enforce user permissions for every source with mixed access, minimise personal
data in indexes, set retention for indexed copies to match the source, and confirm processing locations for indexes
and web grounding with the DPO. `security-privacy:data-exposure-review` reviews the strategy from tier 2.

## Responsible AI considerations

Users must be able to tell an organisational answer from a model's general knowledge. Where answers inform decisions
about people, money, safety or rights, citations and a clear no-answer path are mandatory, and the design goes to
`responsible-ai:ai-transparency`.

## Evaluation requirements

Evaluate retrieval and answer faithfulness separately on the real question set: was the right content found, was the
answer supported by it, were citations correct, and did the solution decline when nothing relevant existed. Thresholds
are agreed before testing, with `evaluation-quality:groundedness-testing` from tier 2.

## Value measures

Measure answer accuracy and citation correctness against the baseline of how people find the information today, owned
by the business owner, and track unanswered questions as a knowledge measure owned by the knowledge owner.

## Scale notes

### Starter

Ground on one or two well-owned sources with permission trimming and citations, supply small reference content
directly, and avoid web grounding unless the use case requires it.

### Scale

Reuse indexes and lookup tools across solutions where sources and audiences match, under shared ownership, and keep a
register of which solutions ground on which sources.

### Enterprise

Treat grounding sources as governed data products with owners, service levels and lineage, and require design review
for any solution that grounds on sensitive or cross-business content.

## Hand-offs

- To `ai-foundry:retrieval-design` for index, chunking and ranking design.
- To `ai-foundry:foundry-tool-design` for live lookup and query tools.
- To `knowledge-management:knowledge-readiness-assessment` when sources need preparation.
- To `data-governance:ai-data-access-model` for permission design on data products.
- To `evaluation-quality:groundedness-testing` for groundedness evidence.

## Reviewer gates

From risk tier 2, `security-privacy` reviews permission enforcement and data exposure, `evaluation-quality` reviews
groundedness evidence, and `design-authority` checks the approach conforms to the reference grounding patterns. A
source with mixed access grounded through an untrimmed service identity is a blocking finding.

## Failure modes

- Everything is pushed into one index, and live data is answered from a stale snapshot.
- A service identity indexes content users cannot open, and the solution reveals it to them.
- Obsolete and draft documents sit beside current ones, and the model cites the wrong version confidently.
- The solution answers from general model knowledge when retrieval finds nothing, and users cannot tell.
- A model is fine-tuned on policies that change the next quarter, and keeps repeating the old rules.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Ground on a source that has no owner or unknown classification.
- Serve content to users who could not open it themselves.
- Use fine-tuning to keep facts current.
- Send organisational or personal data to web grounding without accepted terms and a confirmed data flow.

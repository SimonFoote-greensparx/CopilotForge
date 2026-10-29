---
name: ai-ready-content
description: Gives authors and content owners practical guidance and templates for writing and structuring documents and pages that Copilot and agents can use reliably - one topic per section, explicit scope and dates, descriptive headings, text not images, defined terms, real tables and stated exceptions. Use when authors ask how to write for AI, when answers miss rules buried in long documents, or when knowledge templates are being refreshed.
license: CC-BY-4.0
metadata:
  department: knowledge-management
  lifecycle: Enable, Deliver, Improve
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: sharepoint, m365-copilot, m365-agents, copilot-studio
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-overview, ms-agent-builder, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# AI-ready content

## Purpose

AI reads content in pieces and answers from the piece that seems most relevant, so a rule hidden in an image, a date
mentioned only in the file name or an exception three pages from the rule it qualifies will be missed or mangled. This
skill gives authors short, practical guidance and templates for writing content that people and AI both use correctly.
It goes wrong when guidance chases supposed tricks for a particular model rather than clear writing, or when it becomes
a long style manual nobody reads.

## When to use

- Authors and content owners ask how to write or restructure content so Copilot and agents answer from it correctly.
- Agent answers miss conditions, exceptions or dates that are present in long or poorly structured documents.
- Knowledge templates for policies, procedures or FAQs are being created or refreshed.
- A quality check found recurring clarity and consistency issues across a collection.

## When not to use

- Defining quality dimensions and checking collections against them - use `knowledge-management:content-quality`.
- The minimum bar for a source before agents may ground on it - use `knowledge-management:knowledge-grounding-standards`.
- Writing an agent's instructions - use `m365-agents:agent-instructions`.
- Teaching staff to prompt Copilot well - use `m365-copilot:prompting-practice`.
- Retrieval and chunking design for custom solutions - use `ai-foundry:retrieval-design`.

## Questions to ask first

1. Which kinds of content are authors producing - policies, procedures, FAQs, product information, guidance - and which do AI uses depend on most?
2. What questions do people ask of this content, and where do current answers go wrong?
3. Are there existing templates or editorial standards, and how well are they followed?
4. Who are the authors - specialists, editors, occasional contributors - and how much time will they give to guidance?
5. Which formats are in use (pages, Word documents, PDFs, scanned files, slide decks), and which are authoritative?

## Required inputs

- Examples of current content in each kind, with representative questions and examples of wrong or missed answers.
- Findings from `knowledge-management:content-quality`, where a check has been run.
- Existing templates and editorial standards.
- The lifecycle and metadata requirements, from `knowledge-management:knowledge-lifecycle`.

Where no examples of failed answers exist, test a few representative questions against current content before writing
guidance; guidance written without evidence tends to address imagined problems.

## Decision framework

Apply eight writing practices, prioritised by the failures they prevent.

| Practice | Prevents | Applies most to |
|---|---|---|
| State scope, audience, owner and effective date at the top | Answers from content that does not apply, or is out of date | Policies, procedures |
| One topic per section, under a heading that says what it answers | The rule and its context being separated | Long documents |
| Keep each exception next to the rule it qualifies | Answers that state the rule and omit the exception | Policies, eligibility rules |
| Put rules and figures in text or real tables, not images or scans | Content AI cannot read at all | Process diagrams, rate cards, scanned forms |
| Define terms and acronyms once, use them consistently | Mismatched terms between question and content | Specialist domains |
| Write steps as numbered lists with the actor named | Ambiguous procedures | Procedures, how-to guides |
| Make each section understandable on its own | Partial answers that depend on earlier sections | All content |
| Remove or clearly label examples, history and drafts | Examples or old rules quoted as current | All content |

Choose the format deliberately: pages for short, frequently read guidance; documents for formal or versioned content;
FAQs only where they reflect real, recurring questions and point to the authoritative source.

## Practitioner approach

Start with evidence. Take a handful of representative questions for a collection, ask them of Copilot or the agent that
uses it, and trace each poor answer to the content. The causes are remarkably consistent: the effective date appears
only in the file name, an exception sits in an appendix, a rate table is pasted as an image, the policy uses three
different names for the same allowance. Showing authors these real failures persuades them faster than any guideline.

Write guidance as short practices with before-and-after examples drawn from the organisation's own content, labelled as
illustrative. Each practice should fit in a paragraph, and the whole guide should be readable in ten minutes. Resist
model-specific tricks; the practices that help AI are the practices that help a hurried human reader, and they stay
valid as products change.

Build the practices into templates, because templates change behaviour more than guides do. A policy template with a
header block for scope, audience, owner, effective date and review date, headings phrased as the questions the policy
answers, and a section for exceptions next to each rule will produce better content from authors who never read the
guide. Do the same for procedures and FAQs.

Prioritise rewriting by consequence and use. Do not ask owners to restructure everything. Start with content that AI
uses heavily and that informs important decisions, then fix content as it comes up for review through
`knowledge-management:knowledge-review-cycles`. Convert images of text and scanned documents first, because AI cannot
use them at all.

Avoid duplication in the name of AI. Creating separate "AI versions" of documents, or FAQ pages that restate policy in
different words, produces two sources that will eventually disagree. Improve the authoritative content itself, and keep
FAQs as signposts to it.

Support authors, do not police them. Offer short clinics, review a sample of new content with authors who ask, and
share examples where clearer content fixed a wrong answer. Never score individual authors; report clarity patterns by
collection.

## Outputs

- A short AI-ready writing guide with eight practices and organisation-specific before-and-after examples labelled as illustrative.
- Updated templates for the main content kinds, with header metadata, question-led headings and exception placement.
- A prioritised rewrite list for high-use, high-consequence content, recorded against sources in the `knowledge-asset-register`.

## Microsoft platform considerations

How Copilot and agent routes read pages, documents, tables, images and file types, and how they divide long documents,
varies by route and changes over time. Write guidance around clear structure rather than remembered behaviour, and check
any format-specific advice against the current source records (`ms-agent-builder`, `ms-copilot-overview`). SharePoint
page templates and document templates are the practical way to embed the practices.

## Adoption considerations

Authors adopt guidance that is short, shows their own content improving, and arrives in templates they already use.
Champions can help by sharing examples in their communities.

## Knowledge considerations

This skill improves content at the point of writing, reducing the remediation load on
`knowledge-management:content-quality` and `knowledge-management:knowledge-cleanup`. Keep the guide consistent with the
quality standard's clarity and metadata dimensions.

## Security and privacy considerations

Before-and-after examples must not reproduce sensitive or personal content; use fictional or redacted material. Templates
should prompt authors to set audience and classification at creation.

## Responsible AI considerations

Clear, inclusive language helps AI and every reader. Encourage plain language and accessible formats, and flag content
that reflects practice the organisation no longer stands behind for removal rather than rewording.

## Evaluation requirements

Test rewritten content with the representative questions that previously failed, before and after, and keep the results
as evidence that the practices work in this organisation.

## Value measures

Track the share of high-use content using the new templates, representative question pass rates before and after
rewriting, and clarity issues found in quality checks. The Knowledge Manager owns these, reported by collection; never
by author.

## Scale notes

### Starter

Share a one-page guide with three or four practices and fix the few documents the first agent depends on.

### Scale

Publish the full guide and templates, run author clinics, and fold rewriting into review cycles.

### Enterprise

Embed the practices in organisation-wide templates and editorial standards, train stewards in each business unit, and
track adoption of templates by domain.

## Hand-offs

- To content owners and authors to apply the guide, and to `knowledge-management:knowledge-review-cycles` to schedule rewriting.
- To `knowledge-management:content-quality` to re-check rewritten collections.
- To `champions:champion-programme-design` where Champions will promote the practices.

## Reviewer gates

Not applicable; this skill produces writing guidance and templates rather than releasing AI solutions. Content produced
under it reaches reviewers through the grounding standard and agent release.

## Failure modes

- Guidance chases model-specific tricks that stop working after the next product update.
- Separate "AI versions" of documents are created and diverge from the authoritative ones.
- A long style manual is published and ignored, while templates stay unchanged.
- Rules remain in images and scanned files that AI cannot read.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Create a parallel AI-only copy of authoritative content.
- Score or rank individual authors on their writing.
- Base guidance on remembered model behaviour rather than clear-writing practice and current sources.
- Use real sensitive or personal content in examples.

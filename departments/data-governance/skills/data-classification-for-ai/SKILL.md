---
name: data-classification-for-ai
description: Defines how the organisation's classification scheme and sensitivity labels govern AI - which classes may ground AI, be typed into prompts, reach which models or external services, or train and tune models - plus how labels carry into AI outputs and how unlabelled data is treated. Use when there is no rule for which data AI may use, when labels exist but ignore AI, or before broad Copilot or agent rollout.
license: CC-BY-4.0
metadata:
  department: data-governance
  lifecycle: Mobilise, Enable, Deliver, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: purview, m365-copilot, m365-agents, copilot-studio, ai-foundry, sharepoint, fabric
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-privacy, ms-agent-builder, ms-copilot-studio-security-governance, ico-ai-data-protection, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# Data classification for AI

## Purpose

Most organisations already have a classification scheme, and many have sensitivity labels. Few have decided what each
class means for AI: may confidential data ground an agent shared with a department, may restricted data be typed into
Copilot, may personal data be sent to a third-party model, and what label should an AI-generated summary of a
restricted document carry? This skill extends the classification scheme with clear AI-use rules and makes sure labels
work with the AI services in use. It goes wrong when a new AI-only scheme is invented alongside the existing one, or
when rules are written but labels are missing from most of the data they are meant to govern.

## When to use

- There is no rule for which classes of data AI may use, for which purposes.
- Sensitivity labels exist but nobody has checked how AI services honour them.
- A broad Copilot or agent rollout is planned and data handling rules for AI are needed first.
- Teams want to send data to models or services outside Microsoft 365, or to tune models.
- AI-generated content is being created from sensitive sources without consistent labelling.

## When not to use

- Classifying a specific knowledge collection for its audience - use `knowledge-management:knowledge-classification`.
- Reviewing whether a specific solution exposes sensitive content - use `security-privacy:data-exposure-review`.
- Defining who and what may access each class of data through AI - use `data-governance:ai-data-access-model`.
- Setting retention rules for AI data - use `data-governance:ai-data-retention-rules`.

## Questions to ask first

1. What classification scheme and labels does the organisation already have, and how much data actually carries them?
2. Which AI uses must the rules cover - personal Copilot use, shared agents, external audiences, third-party models, tuning or training?
3. Which classes include personal, special category or regulated data, and what has the DPO said about AI use of them?
4. How should labels carry into AI outputs, and who decides when a summary is less sensitive than its source?
5. How will unlabelled data be treated until labelling catches up?

## Required inputs

- The current classification scheme, labelling policy and labelling coverage reports.
- The AI services in use or planned, and the platforms they run on.
- The DPO's position on AI use of personal and special category data.
- The AI data inventory from `data-governance:ai-data-inventory`, where it exists.

Where labelling coverage is unknown, assume it is low and design the unlabelled-data rule accordingly. Never define
legal handling requirements for regulated data without the DPO or legal adviser.

## Decision framework

Add an AI-use column to the existing scheme rather than creating a new one. A typical starting point, to be adapted:

| Class | Ground personal AI use (user's own access) | Ground shared agents | Send to third-party models or external services | Use for tuning or evaluation sets | Output labelling |
|---|---|---|---|---|---|
| Public | Yes | Yes | Yes | Yes | None required |
| General internal | Yes | Yes, audience as source | With approved services | Yes | Inherit |
| Confidential | Yes | Only if agent audience matches source audience | Only with approved services and DPO-confirmed terms | Only de-identified, with owner approval | Inherit; never lower automatically |
| Restricted or highly confidential | Case by case, as the organisation decides | No by default; tier 3+ review if proposed | No by default | No | Inherit; manual review to change |
| Unlabelled | Treat as general internal for personal use; treat as confidential for shared agents | Owner check before use | No until classified | No until classified | Apply default label |

Personal and special category data adds the DPO's conditions on top of the class rules. The final rules are the
organisation's decision; record who approved them.

## Practitioner approach

Start with what exists. Read the current scheme and labelling policy, and get a coverage report: how much content and
data actually carries labels, and where. The usual finding is a sensible scheme with patchy coverage, and that shapes
everything else. Rules that depend on labels nobody applied govern nothing.

Then map AI uses to the scheme. List the ways AI touches data in the organisation, from personal Copilot use through
shared agents to third-party models and tuning, and decide for each class what is allowed. Keep the existing class
names. Work with the security lead and DPO, and test the draft against real cases: an HR agent, a finance assistant, a
customer service flow. If the rules cannot answer those cases, they are not specific enough.

Decide how labels carry into outputs. AI summaries, drafts and extracts can be as sensitive as their sources, or more,
because they concentrate information. The safe default is inheritance: outputs carry the highest label of their
sources, and lowering a label needs a person's decision. Confirm how the AI services in use apply label inheritance
today; behaviour differs by service and changes, so check the source records.

Handle unlabelled data explicitly. Waiting for perfect labelling stalls AI adoption; ignoring it creates exposure. A
practical rule treats unlabelled content conservatively for shared agents and external services, while allowing
personal use within existing permissions, and pairs that with a labelling campaign aimed at the sources AI uses most.
Auto-labelling and default labels help; confirm what the organisation's Microsoft Purview configuration supports.

Publish the rules in plain language for makers and users, with examples. Makers need to know which sources they may
use for an agent shared with a given audience; users need to know what not to paste into prompts for which services.
Review the rules when new AI services or patterns arrive.

## Outputs

- AI-use rules added to the organisation's classification scheme: what each class permits for each AI use, approved by the data governance lead, security lead and DPO.
- An output labelling rule, including inheritance and who may lower a label.
- An unlabelled-data rule and a prioritised labelling plan for sources AI uses most.
- Plain-language guidance for makers and users with worked examples.

## Microsoft platform considerations

Sensitivity labels and data loss prevention in Microsoft Purview, label handling by Microsoft 365 Copilot and agents,
and how Copilot Studio and Foundry treat labelled content differ by service and change frequently. Confirm current
behaviour in `ms-copilot-privacy`, `ms-agent-builder` and `ms-copilot-studio-security-governance`, and record what was
checked, before writing a rule that depends on it.

## Adoption considerations

People adopt AI faster when they know what they may use it with. Clear examples ("you may ask Copilot to summarise
confidential project files you can already open; do not paste them into unapproved tools") reduce both fear and misuse.

## Knowledge considerations

Knowledge collections need classification and audience decisions that follow these rules. Pass the rules to
`knowledge-management:knowledge-classification` so knowledge owners apply them consistently.

## Security and privacy considerations

The rules are a security and privacy control. The `security-privacy` reviewers apply them at each gate, and the DPO's
conditions for personal and special category data take precedence over class defaults.

## Responsible AI considerations

Classes that contain data about individuals need extra care when used to inform decisions about people. Flag such uses
to `responsible-ai:ai-impact-assessment`.

## Evaluation requirements

Test label behaviour with real services before relying on it: create labelled test content, ground an agent on it, and
check that outputs, citations and exports behave as the rules expect.

## Value measures

Track labelling coverage of sources used by AI, the share of tier 2+ solutions whose sources comply with the AI-use
rules, and exposure findings linked to unlabelled data. The data governance lead owns these, with a baseline from the
first coverage report.

## Scale notes

### Starter

Add a short AI-use line to each existing class and a simple unlabelled-data rule. Focus labelling effort on the few
sources agents use.

### Scale

Publish the full AI-use table, apply default and automatic labelling where tooling supports it, and check compliance at
every release gate.

### Enterprise

Align AI-use rules across business units and jurisdictions, integrate them with data loss prevention and catalogue
policy, and review them whenever a new AI service is approved.

## Hand-offs

- To `knowledge-management:knowledge-classification` for knowledge collections.
- To `data-governance:ai-data-access-model` to translate classes into access patterns.
- To `security-privacy:data-exposure-review`, which applies the rules at each gate.
- To `copilot-adoption:launch-plan` for user guidance.

## Reviewer gates

The rules require approval by the `security-privacy` lead and the DPO before publication. From risk tier 2, solutions
are checked against them at the `security-privacy` gate.

## Failure modes

- Rules depend on labels that most data does not carry, so they govern almost nothing.
- A separate AI classification scheme is invented and conflicts with the existing one.
- Summaries of restricted documents are saved without labels and spread widely.
- Rules are written without testing how AI services actually honour labels.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Invent a parallel classification scheme for AI.
- Assume a service honours labels without checking the current source and testing it.
- Define legal handling rules for regulated or special category data without the DPO.
- Allow AI outputs to lower a source's label automatically.

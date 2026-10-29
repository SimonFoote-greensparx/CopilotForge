# Style guide

How a CopilotForge skill, template and programme is written. `scripts/validate-skills.py` and the other checks enforce
the parts a script can check; the reviewer checks the rest. The skill anatomy follows the design brief, section 10.

## Skill anatomy

Every skill is a folder `departments/<department>/skills/<skill>/` (reviewer-class departments use `reviewers/`) holding
one `SKILL.md`. Generated files (`references/sources.md`, bundled references) sit beside it; never hand-edit them.

### Frontmatter

```yaml
---
name: <identical to the folder name, lowercase-hyphenated, unique across CopilotForge and not used by D365Forge>
description: <120-450 characters. What it does, then "Use when ..." with concrete situations. No colons.>
license: CC-BY-4.0
metadata:
  department: <department id>
  lifecycle: <subset of Discover, Envision, Mobilise, Enable, Deliver, Assure, Launch, Measure, Scale, Improve>
  maturity: <archetypes it mainly serves - explorer, adopter, builder, scaler, ai-enterprise>
  risk-tiers: <progressive risk tiers its advice covers - 0, 1, 2, 3, 4>
  platforms: <copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-code, copilot-studio, ai-foundry, power-platform, sharepoint, purview, entra, azure, fabric, github, or platform-neutral>
  edition-support: <starter, scale, enterprise>
  reviewers: <reviewer-class departments whose gate applies - security-privacy, responsible-ai, evaluation-quality, design-authority - or none>
  sources: <source record ids from sources/*.toml, or none>
  status: draft
  authors: Simon Foote
---
```

All metadata values are plain comma-separated strings, because runtimes such as Copilot Cowork accept only the open
Agent Skills frontmatter (decision D7). The design brief's `triggers` field lives in `tests/triggers/<department>.toml`
rather than in the frontmatter, so prompts are tested rather than merely listed. `license` and `authors` are fixed:
they carry the credit wherever the skill is copied (decision D2). New and rewritten skills are `draft`; only Simon
Foote moves a skill to `reviewed` or `stable`.

### Sections, in exactly this order

```markdown
# <Title in sentence case>

## Purpose
## When to use
## When not to use
## Questions to ask first
## Required inputs
## Decision framework
## Practitioner approach
## Outputs
## Microsoft platform considerations
## Adoption considerations
## Knowledge considerations
## Security and privacy considerations
## Responsible AI considerations
## Evaluation requirements
## Value measures
## Scale notes
### Starter
### Scale
### Enterprise
## Hand-offs
## Reviewer gates
## Failure modes
## Sources
## Never
```

| Section | Rule |
|---|---|
| Purpose | Two to four sentences: what the skill achieves for the organisation and where this work usually goes wrong. |
| When to use | Situations, as bullets. |
| When not to use | Name the neighbouring skills that own adjacent requests, as `` `department:skill` ``. For a department that is still planned, name it by id in backticks, for example `` `knowledge-management` ``. |
| Questions to ask first | Three to six numbered questions that decide the answer. Ask only what the decision or artefact needs. |
| Required inputs | What must exist before the skill can produce its output, and what to do when an input is missing (mark it, never invent it). |
| Decision framework | The criteria, thresholds or decision table that turn the answers into a recommendation. |
| Practitioner approach | 250-650 words of original practitioner method. |
| Outputs | Named, structured, testable outputs, each naming its template id in backticks where one exists, for example `` `coe-charter` ``. |
| Microsoft platform considerations | Durable guidance on platform choice and configuration. Volatile facts (availability, licensing, limits, preview status, product names) are not asserted; point to the source records. |
| Adoption, Knowledge, Security and privacy, Responsible AI, Evaluation | Completed, or opening with "Not applicable" and a one-sentence rationale (design brief 13.1). |
| Value measures | How the outcome is measured, with baseline and owner. Never individual performance. |
| Scale notes | `### Starter`, `### Scale`, `### Enterprise`: how practice changes with scale, without rewriting the method. |
| Hand-offs | Who takes over next, as `` `department:skill` `` (or a planned department id). |
| Reviewer gates | Which reviewer-class departments must pass the output, from which risk tier, and what they look for; or "Not applicable" with a rationale. |
| Failure modes | At least three realistic ways the advice or the resulting solution breaks. |
| Sources | Exactly the standard paragraph below and nothing else. |
| Never | At least three bullets. Always the last section, because edition fragments are spliced in before it. |

The standard Sources paragraph:

> `references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Voice

- Write as an experienced Microsoft AI transformation practitioner advising a colleague: opinionated, specific, practical.
- Begin with outcomes and constraints, never with a product. The first decision is whether AI is appropriate at all.
- Say what the skill cannot determine. A skill that answers everything confidently is the failure this library exists to prevent.
- Paragraphs of two to five sentences. Bullets only for genuinely enumerable items. Bold sparingly. No emojis.

## Accuracy and sources

- Sources provide the facts; CopilotForge provides the reasoning structure, method, review gates and artefacts.
- Never invent statistics, prices, licence names, limits, dates or availability. Point to `references/sources.md`.
- Microsoft renames products often (for example, Microsoft 365 Copilot is now presented as Microsoft Copilot in some
  Microsoft documentation). Use the name in the current source record and avoid building method on a product name.
- Licensing questions end with the Microsoft licensing guide or a licensing partner. Legal, data protection and
  employment questions end with the organisation's DPO, legal adviser or HR.
- Never copy or closely paraphrase Microsoft Learn or any other publisher. `cite-only` sources are summarised in your
  own words.

## People

Anything touching people (Champions, learning, ownership, adoption measures) uses declared roles, skills, evidence and
availability only. Skills never assess performance, rank individuals, profile by personal characteristics or monitor
individual usage. Adoption data is reported at team or role level above an agreed minimum group size.

## Reviewer-class skills

Each finding is classified **blocking** or **advisory**, names the risk or standard behind it, and gives the specific
fix. A blocking finding stops release at the gate; it is not traded off against a date. Disagreement escalates to the
accountable executive for risk acceptance, recorded in writing.

## Spelling

UK English by exact word form (organisation, prioritise, behaviour, catalogue, programme, licence as a noun,
judgement, centre). Microsoft product names keep Microsoft's spelling (Center of Excellence in a Microsoft title).
`python3 scripts/check-uk-english.py --fix` rewrites what it finds.

## Templates

Templates in `templates/<id>.md` are human-usable documents, not prompts (design brief 16.1). Each one:

- starts with `# Title`, then a line `Template id: `<id>`` and the responsible skill as `` `department:skill` ``;
- marks every fact the organisation must supply as `[To confirm: ...]`, so nothing is invented;
- labels any example content as fictional;
- ends with this exact credit line:

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.

## Trigger tests

Every skill has a `[[skill]]` block in `tests/triggers/<department>.toml` with at least three realistic prompts that
should load it and at least one near miss naming the skill that should catch it instead (`department:skill`, or
`department:*` for a planned department). Prompts are phrased the way a sponsor, adoption lead or maker would actually
ask, not copied from the description.

## Lineage

CopilotForge evolves the engineering model of D365Forge, a separate project for Dynamics 365 delivery. Do not copy
D365Forge skills or reuse their names; `scripts/check-separation.py` enforces this.

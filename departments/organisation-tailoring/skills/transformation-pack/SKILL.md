---
name: transformation-pack
description: Orchestrates a tailored AI transformation pack from a confirmed profile - assessment, target operating model, adoption and Champions programmes, CoE, opportunity process, agent delivery, governance, roadmap, ownership map, templates and success measures - at the depth the edition sets, each artefact naming its responsible skill and sources. Use when an organisation asks for help adopting Copilot, scaling agents or setting up an AI CoE.
license: CC-BY-4.0
metadata:
  department: organisation-tailoring
  lifecycle: Discover, Envision, Mobilise, Enable, Deliver, Assure, Launch, Measure, Scale, Improve
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral, copilot-cowork, sharepoint
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-adoption-hub, ms-copilot-studio-guidance, ms-copilot-cowork-customise, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Transformation pack

## Purpose

When a sponsor says "we have Copilot, usage is patchy, departments are building agents and management wants a CoE - help
us", they need a coherent set of documents that fit their organisation, not a generic playbook. This skill orchestrates
the `ai-transformation` programme and the programmes it includes, decides which artefacts to produce at what depth from
the confirmed edition, archetype and signals, calls the responsible skill for each, and assembles an indexed pack. Packs
go wrong when every organisation receives the same heavy set, when unknowns are filled with plausible guesses, and when
a refresh silently overwrites decisions the organisation has already taken.

## When to use

- An organisation asks for end-to-end help with Microsoft AI adoption, agents, governance or a CoE.
- A confirmed edition and archetype exist and the sponsor wants the documents.
- A sponsor asks what the whole programme looks like before committing to one part.

## When not to use

- Refreshing an existing pack after the profile changes - use `organisation-tailoring:transformation-pack-refresh`.
- Building or validating the profile - use `organisation-tailoring:ai-profile-intake`.
- Choosing edition, overlay and archetype - use `organisation-tailoring:edition-and-archetype`.
- A single artefact on its own, such as a CoE charter - use its owning skill, for example `ai-centre-of-excellence:coe-charter`.
- Programme mobilisation, RAID and stage gates for running the pack once agreed - use `programme-management:programme-charter`.

## Questions to ask first

1. Has the sponsor confirmed the edition, overlay and archetype, and are any deciding facts still provisional?
2. Which output formats does the organisation want (Word documents, an Excel workbook for registers and scorecards, or both), and where should they be saved?
3. Is this a first pack or a refresh of an existing one, and if a refresh, where is the previous version?
4. Which artefacts does the sponsor need first, given the stated timeline and capacity?

## Required inputs

- The confirmed recommendation from `organisation-tailoring:edition-and-archetype`.
- The validated profile from `organisation-tailoring:ai-profile-intake`.
- `references/programmes.json` for programmes, included programmes and their conditions, artefacts, depths, responsible skills, templates and gates.
- `references/tailoring-rules.yaml` for the signals that switch included programmes on.
- `references/templates.md` for the template each artefact uses.

Every fact the profile does not supply is written as `[To confirm: ...]` in the artefact, and the pack index lists them
all. Never invent figures, owners, dates or product facts to make a document look finished.

## Decision framework

Work from `references/programmes.json`; do not hand-pick.

| Step | Rule |
|---|---|
| Programmes | Always `ai-transformation`; add each included programme whose condition holds (for example `agent-factory` when agents are emerging or the archetype is builder or later) |
| Artefacts | Every artefact of every chosen programme, at the depth set for the edition; skip those marked omit |
| Substitutions | Apply edition substitutions (Starter receives an AI working group in place of a CoE, with charter and RACI in light form) |
| Depth | Light: one to two pages, essentials only. Standard: complete sections, worked for this organisation. Full: complete, with federation, formal evidence and portfolio detail |
| Order | By lifecycle stage, then programme |
| Gates | Carry each programme's reviewer gates into the pack with their starting risk tier |

The flagship request maps to artefacts as follows: assessment (maturity and adoption readiness), target operating model,
adoption programme, Champions programme, CoE (charter, operating model, RACI, cadence), opportunity process, agent
delivery model (agent brief, testing and release route), governance framework, roadmap, ownership map, template pack and
success measures (KPI framework, adoption measures and the pack index).

## Practitioner approach

Confirm the starting point. If the sponsor has not confirmed the edition and archetype, stop and go back; a pack built on
an unconfirmed recommendation is rework waiting to happen. Where `python3 scripts/tailor.py` is available it produces the
plan deterministically; otherwise derive it from `references/programmes.json` using the decision framework.

Build the pack index first, on the `transformation-pack-index` template: each artefact with its title, programme, stage,
depth, responsible skill, template and status, plus the reviewer gates and facts to confirm. This is the sponsor's map
and the contract for what follows.

Produce artefacts in lifecycle order, calling the responsible skill for each and following its method. Each artefact
names its responsible skill and the source records that skill relied on, and uses its template from
`references/templates.md`. Write for this organisation: its personas, its outcomes, its signals. An adopter with agents
emerging and suspected shadow AI should see the acceptable-use starter and agent intake early in the roadmap, not in
month nine.

Keep depth honest. A 600-person, three-unit organisation at Scale receives the full set at standard depth, including the
agent-factory programme because agents are already being built, a core CoE team with business representatives, a formal
Champions programme and a KPI framework. A 40-person single-unit practice at Starter receives a much lighter pack: an AI
working group instead of a CoE, light charter and RACI, an informal Champion network, an acceptable-use starter, a few
high-value scenarios, no agent-factory programme unless agents appear, and no separate KPI framework. If both packs look
alike, something has gone wrong.

Assemble the outputs in the formats agreed, saved to the organisation's own storage (for example a OneDrive or SharePoint
folder the sponsor chooses): Word documents for narrative artefacts, an Excel workbook for the register, scorecard, RACI
and ownership map. Never store the organisation's pack in the CopilotForge repository.

On refresh, re-run the rules on the updated profile, compare with the previous index, and explain material changes before
changing any document: an edition or archetype move, a programme added or removed, a depth change, a new signal, a gate
starting earlier. Show what will be added, changed or retired, and keep decisions the organisation has already recorded
unless the sponsor agrees to revisit them. Never silently replace a document.

Close with a short covering note: what the pack contains, what to do first, the facts to confirm, and who owns each next
step from the ownership map.

## Outputs

- A transformation pack index and success measures on the `transformation-pack-index` template: artefacts with programme, stage, depth, responsible skill, template, source records used and status; reviewer gates; facts to confirm; change log for refreshes.
- The artefacts themselves, each produced by its responsible skill on its template, for example `ai-maturity-assessment`, `ai-operating-model`, `adoption-plan`, `champion-programme-charter`, `coe-charter`, `coe-raci`, `prioritisation-matrix`, `agent-brief`, `agent-release-checklist`, `ai-governance-starter`, `ai-roadmap`, `ownership-map` and `coe-kpi-scorecard`.
- A covering note for the sponsor and, on refresh, a change summary agreed before documents are replaced.

## Microsoft platform considerations

The pack can be produced and maintained through Copilot Cowork with CopilotForge skills installed; how Cowork is
customised with skills and plugins changes, so check `references/sources.md`. Product facts in any artefact come from
the source records cited by the responsible skill, never from memory.

## Adoption considerations

Sequence the pack so the organisation sees early, useful change: safe-use guidance and a few high-value scenarios before
heavier structures. Present the pack as the organisation's plan, owned by its sponsor, not as a consultant's deliverable.

## Knowledge considerations

Where the weak-knowledge signal appears, put knowledge ownership and quality work before agent delivery in the roadmap,
and say so in the covering note. Plan that work with `knowledge-management:knowledge-readiness-assessment`.

## Security and privacy considerations

The pack contains organisational information; store it in the organisation's own location with access limited to the
programme team. Carry the `security-privacy` gate from risk tier 2 into every relevant artefact. Record no personal data.

## Responsible AI considerations

State in the pack that editions and archetypes are proposed CopilotForge classifications, that some uses will not be
built, and that tier 3 and 4 solutions need review through `responsible-ai:ai-impact-assessment` with an accountable executive.

## Evaluation requirements

Not applicable to the pack as a document set; it is checked by completeness against the plan, by every unknown being
marked, and by each artefact naming its responsible skill. Solution evaluation sits in the agent delivery artefacts.

## Value measures

The success measures in the pack index link to `ai-centre-of-excellence:coe-kpi-framework` (or a short Starter list), each
with baseline, target and business owner. The pack's own measure is the share of artefacts agreed by their owners within
the first cycle, tracked by the transformation architect role.

## Scale notes

### Starter

A short pack: working-group terms, acceptable-use starter, a handful of scenarios, an informal Champion network, a light
roadmap and five or six success measures. Partner support named for anything beyond tier 1.

### Scale

The full set at standard depth, with the agent-factory programme when agents are emerging, a core CoE team, formal
Champions and a KPI framework.

### Enterprise

Full depth with federated CoE and governance, spoke packs per business unit where units differ, formal evidence where the
overlay is formal, and portfolio-level value tracking.

## Hand-offs

- To each responsible skill named in the index, for example `ai-strategy:ai-roadmap`, `copilot-adoption:launch-plan`, `champions:champion-programme-design` and `ai-centre-of-excellence:coe-governance-model`.
- To `organisation-tailoring:ownership-map` for accountable roles on every artefact.
- To `programme-management:programme-charter` to run the programme once agreed.

## Reviewer gates

The pack carries programme gates rather than passing one itself: `security-privacy` blocking from risk tier 2, and the
`evaluation-quality:ai-release-evidence`, `design-authority:ai-design-review` and `responsible-ai:ai-impact-assessment`
gates where the agent-factory programme applies.

## Failure modes

- Every organisation receives the same heavy pack, and small ones abandon it.
- Unknowns are filled with plausible figures, and the sponsor discovers them in a board paper.
- A refresh overwrites decisions already taken, and trust in the pack is lost.
- Artefacts are written without their responsible skill's method, so they contradict each other.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Build a pack before the sponsor has confirmed the edition and archetype.
- Invent facts, owners, figures or product details to complete a document.
- Silently replace a document on refresh.
- Store an organisation's pack in the CopilotForge repository or any public location.

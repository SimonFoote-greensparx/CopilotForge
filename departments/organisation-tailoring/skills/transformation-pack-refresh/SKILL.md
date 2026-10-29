---
name: transformation-pack-refresh
description: Refreshes an existing transformation pack when the organisation's profile, signals or the CopilotForge library change - compares old and new profiles and tailoring results, classifies each change as material or minor, maps it to affected artefacts, protects decisions already taken, and agrees a change summary before any document is replaced. Use when a pack is due for review, after a merger or new regulation, or when agents or shadow AI appear.
license: CC-BY-4.0
metadata:
  department: organisation-tailoring
  lifecycle: Measure, Scale, Improve
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral, copilot-cowork, sharepoint
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-studio-guidance, ms-copilot-cowork-customise
  status: draft
  authors: Simon Foote
---

# Transformation pack refresh

## Purpose

A transformation pack describes an organisation at a moment in time, and organisations move: units merge, regulators
raise expectations, departments start building agents, a CoE is launched, or the CopilotForge skills behind the pack
improve. This skill refreshes an existing pack in a controlled way. It compares the previous and current profile and
tailoring results, classifies each change as material or minor, maps it to the artefacts it affects, protects decisions
the organisation has already taken, and agrees a change summary with the sponsor before any document is replaced. Refreshes
go wrong when the pack is silently regenerated, when local edits and decisions are overwritten, and when a material change
such as a new edition is buried among minor wording updates.

## When to use

- A pack has reached its scheduled review, often at a programme stage gate or annually.
- The organisation has changed: a merger, new business units, a new country, a new regulatory expectation.
- New signals have appeared since the last pack, such as agents being built, suspected shadow AI, or a CoE request.
- The CopilotForge skills or templates behind the pack have been updated and the organisation wants the improvements.
- A sponsor asks what would change in their pack if a provisional fact were confirmed differently.

## When not to use

- Producing a first pack for an organisation that has none - use `organisation-tailoring:transformation-pack`.
- Updating the profile itself after a change - use `organisation-tailoring:ai-profile-intake`.
- Re-running the edition, overlay and archetype rules and explaining them - use `organisation-tailoring:edition-and-archetype`.
- Refreshing the AI strategy against outcomes and Microsoft change - use `ai-strategy:strategy-refresh`.
- Assessing the impact of a change to a single live AI solution - use `design-authority:ai-change-impact-review`.

## Questions to ask first

1. Where is the previous pack, its index and change log, and which version of the profile was it built from?
2. What has changed since then, and has the profile been updated and validated?
3. Which decisions recorded in the pack (edition overrides, scope choices, owners, deferrals) has the organisation already taken and wants to keep?
4. Which documents has the organisation edited locally since they were produced?
5. Who must agree the change summary before documents are replaced?

## Required inputs

- The previous pack index on the `transformation-pack-index` template, including its refresh change log and the profile version used.
- The updated, validated profile from `organisation-tailoring:ai-profile-intake`.
- The re-run tailoring recommendation from `organisation-tailoring:edition-and-archetype`, confirmed by the sponsor where it has moved.
- The decision log and any local edits to pack documents.

If the previous profile or index is missing, the refresh cannot compare reliably; treat it as a new pack through
`organisation-tailoring:transformation-pack` and record that history was unavailable. Never reconstruct a previous
profile from memory.

## Decision framework

Classify every difference, then decide what happens to each affected artefact.

| Change | Material? | Typical effect |
|---|---|---|
| Edition or assurance overlay moves | Material | Depth changes across the pack; governance and evidence weight change |
| Archetype moves | Material | Emphasis shifts; programmes may be added |
| New or cleared signal | Material | An included programme is switched on or off; priorities change |
| Programme added or removed | Material | Artefacts added or retired |
| Gate starts at a lower risk tier | Material | Reviewer gates brought forward |
| Provisional fact confirmed without changing a rule outcome | Minor | `[To confirm: ...]` markers resolved |
| Library update to a skill method or template | Minor unless it changes a gate, separation rule or depth | Artefact updated at the next natural review |
| Owner or role mapping change | Minor for the pack, material for the people involved | Ownership map updated |

For each affected artefact choose one action.

| Action | Use when |
|---|---|
| Keep | No material change affects it |
| Update in place | Content changes but recorded decisions still stand |
| Replace | Depth or scope changes so much that a new version is clearer; previous version archived |
| Add | A new programme or artefact is now in scope |
| Retire | An artefact is no longer needed; archived with a reason |

Recorded decisions are kept unless the sponsor agrees to revisit them. No document is replaced before the change summary
is agreed.

## Practitioner approach

Start by establishing the baseline. Find the previous index, its change log and the profile version it was built from.
Validate the updated profile, re-run the tailoring rules, and lay the two results side by side: edition, overlay,
archetype, signals with rule ids, programmes, artefacts and depths. Where `python3 scripts/tailor.py` is available it
produces both results deterministically; otherwise apply the rules by hand and record each step.

Classify each difference using the framework. Be strict about materiality: anything that changes depth, programmes,
gates, separation or the order of foundations is material, however small it looks. A move from Starter to Scale after a
merger, or a new agents-emerging signal, changes what the organisation must do next; it must not appear as one line among
thirty wording changes.

Map each change to the artefacts it touches and choose an action. Check the decision log and local edits before proposing
anything. If the organisation has overridden the edition, chosen to defer a pillar, or rewritten a section in its own
words, the refresh keeps that decision and edit unless the change makes it untenable, in which case it says why and asks.

Write the change summary for the sponsor in plain language: what changed in the organisation, what that changes in the
programme, which artefacts will be kept, updated, replaced, added or retired, which recorded decisions are affected, and
what to do first. Put material changes first. Mark which changes come from the organisation and which from improvements in
the CopilotForge library, so the sponsor can see why a document they did not expect to change is being updated.

Only after agreement, produce the changes through each artefact's responsible skill, archive replaced and retired versions
in the organisation's own storage, and update the pack index and its refresh change log with the date, the profile
version, the changes made and who agreed them. Resolve `[To confirm: ...]` markers only where the profile now supplies the
fact; leave the rest visible.

Close by setting the next review trigger: a date, a stage gate, or an event such as a new business unit starting to build
agents.

## Outputs

- A change summary agreed with the sponsor: profile and tailoring differences, material and minor changes, artefact actions, affected decisions and what to do first.
- An updated pack index on the `transformation-pack-index` template with the refresh change log completed.
- Updated, replaced, added and retired artefacts, each produced by its responsible skill, with previous versions archived in the organisation's storage.
- The next review trigger and its owner.

## Microsoft platform considerations

Packs maintained through Copilot Cowork with CopilotForge skills installed can be refreshed in the same place; how skills
and plugins are customised in Cowork changes, so check `references/sources.md`. Product facts in refreshed artefacts are
re-checked against current source records, because they are the facts most likely to have changed.

## Adoption considerations

Communicate refresh outcomes to the people who own affected artefacts before documents change. A pack that changes
without explanation loses the trust the programme depends on.

## Knowledge considerations

The pack is itself organisational knowledge. Keep versions, change logs and the decision trail in one owned location so
the reasoning behind each version can be found later.

## Security and privacy considerations

Store refreshed packs, archived versions and profiles in the organisation's own location with access limited to the
programme team, never in the CopilotForge repository. Where a refresh brings the `security-privacy` gate forward, tell
the security owner before the change takes effect.

## Responsible AI considerations

A refresh that brings tier 3 or 4 uses into scope must add the `responsible-ai` route and an accountable executive. Keep
stating that editions and archetypes are CopilotForge proposals, not judgements on the organisation or its people.

## Evaluation requirements

Not applicable, because the pack is a document set rather than an AI solution; the refresh is checked by repeatability
(the same profile gives the same plan) and by every change appearing in the change log.

## Value measures

Track time from a triggering change to an agreed refresh, the share of artefacts kept rather than replaced, and recorded
decisions preserved, reported by the Transformation Architect. These measure the pack's stability, never individuals.

## Scale notes

### Starter

A short refresh at a scheduled review or after a change such as new staff numbers or the first agent, often a few updated
artefacts and a half-page change summary.

### Scale

Refresh at stage gates and on material signals, with a full comparison, change summary, sponsor agreement and an updated
change log.

### Enterprise

Refresh per business unit as well as for the whole organisation, with material changes taken to the portfolio board and
formal evidence of agreement where the overlay is formal.

## Hand-offs

- To `organisation-tailoring:ai-profile-intake` when the profile needs updating before the refresh can start.
- To `organisation-tailoring:edition-and-archetype` to re-run and confirm the tailoring rules.
- To each artefact's responsible skill, for example `ai-strategy:ai-roadmap` or `organisation-tailoring:ownership-map`, to produce the changes.
- To `programme-management:stage-gates` where a refresh coincides with a programme gate.

## Reviewer gates

Not applicable, because a refresh releases no solution; where it changes which gates apply, the updated pack carries
`security-privacy` from risk tier 2 and any newly applicable `responsible-ai`, `evaluation-quality` or `design-authority`
gates.

## Failure modes

- The pack is regenerated and replaces documents the organisation had edited and agreed.
- A material change such as a new edition is buried among minor updates and missed by the sponsor.
- The previous profile is reconstructed from memory, so the comparison is unreliable.
- Library improvements are applied without explanation, and owners do not know why their document changed.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Replace or delete a document before the sponsor has agreed the change summary.
- Overwrite a recorded decision or local edit without asking.
- Hide a material change among minor ones.
- Store a refreshed pack or profile in the CopilotForge repository or any public location.

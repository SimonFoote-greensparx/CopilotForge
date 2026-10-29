---
name: edition-and-archetype
description: Applies the CopilotForge tailoring rules to a validated organisation profile to recommend an edition (starter, scale or enterprise), an assurance overlay and a maturity archetype, citing the rule id behind each, reporting emerging signals and explaining the result to the sponsor before any pack is built. Use when a profile is ready, when a sponsor asks why they got a lighter or heavier programme, or when circumstances change.
license: CC-BY-4.0
metadata:
  department: organisation-tailoring
  lifecycle: Discover, Envision
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# Edition and archetype

## Purpose

The same request from a 40-person practice and a 600-person services company should not produce the same programme.
This skill applies the deterministic rules in `references/tailoring-rules.yaml` to a validated profile and recommends an
edition, an assurance overlay and a maturity archetype, each with the rule id that produced it, plus the emerging
signals that change priorities. It explains the result to the sponsor and asks them to confirm before anything is built.
It goes wrong when the rules are bent to give a flattering answer, when signals are treated as the archetype, or when
the recommendation is presented as a Microsoft classification.

## When to use

- A profile has been validated and the next step is choosing how heavy the programme should be.
- A sponsor asks why their organisation received a lighter or heavier programme than expected.
- The profile has changed and the edition or archetype may have moved.
- Two parts of an organisation need a consistent, explainable comparison.

## When not to use

- Creating or validating the profile itself - use `organisation-tailoring:ai-profile-intake`.
- Producing the artefacts once the edition and archetype are confirmed - use `organisation-tailoring:transformation-pack`.
- An evidenced maturity assessment across capability dimensions - use `ai-strategy:ai-maturity-assessment`.
- Designing the CoE shape in detail once the edition is known - use `ai-centre-of-excellence:coe-operating-model`.

## Questions to ask first

1. Has the profile been validated against the schema and confirmed by the person who supplied it?
2. Are any of the deciding facts (workforce size, business units, regulatory level, usage pattern, Champions, CoE status, custom AI in production, portfolio management) provisional?
3. Does the sponsor expect a particular answer, and why?
4. Is there a reason to override the recommended edition, such as a planned merger or a regulator's request, and who would own that decision?

## Required inputs

- A validated profile from `organisation-tailoring:ai-profile-intake`.
- `references/tailoring-rules.yaml`, the rule set with ids for editions, assurance overlays, archetypes and signals.
- `references/editions-and-archetypes.json`, which describes the CoE, Champions and governance form for each edition and the output emphasis of each archetype.

If a deciding fact is provisional, say which recommendation depends on it and what would change if it moved. Do not
produce a recommendation from an invalid profile.

## Decision framework

Apply the rules exactly as written in `references/tailoring-rules.yaml`, in order.

| Decision | How the rules work | Report |
|---|---|---|
| Edition | Edition rules are evaluated in order and the first whose conditions all hold wins (E1 enterprise by size or business units, E2 starter for small single-unit organisations without high regulatory expectations, E3 scale as the default) | Edition, rule id, rationale |
| Assurance overlay | A1 formal where the regulatory level is high, otherwise A2 proportionate | Overlay, rule id, rationale |
| Archetype | The archetype is the earliest stage whose exit is not yet met (R1 explorer to R5 ai-enterprise), so an organisation is never placed beyond a foundation it has skipped | Archetype, rule id, rationale, output emphasis |
| Emerging signals | Every signal rule that holds is reported (S1 agents emerging, S2 shadow AI, S3 CoE requested, S4 no AI policy, S5 weak knowledge) | Signal, rule id, note |

Overrides are allowed only by the sponsor, recorded with a reason, and never for the archetype: if foundations are
missing, the archetype stays where the rules put it.

## Practitioner approach

Run the rules, do not reinterpret them. Where the repository is available, `python3 scripts/tailor.py` with the profile
path produces the same result deterministically; otherwise walk `references/tailoring-rules.yaml` by hand, rule by rule,
and write down which condition decided each outcome. The value of the rules is that two people applying them to the same
profile get the same answer.

Explain the edition in terms of overhead, not status. Starter is not a lesser programme; it is the right amount of
structure for a small, single-unit organisation, with an AI working group instead of a CoE and a light evidence route
for Champions. Scale adds Champions, repeatable intake, agent ownership and formal measures. Enterprise adds federation,
formal assurance and portfolio management. Use `references/editions-and-archetypes.json` to describe what each means in
practice for the CoE, Champions and governance.

Explain the archetype as the binding constraint. An organisation with Copilot deployed but inconsistent use is an
adopter even if some departments are building agents, because adoption is the foundation that is not yet in place. Say
this directly: the archetype is where the next effort pays back most, not a grade.

Then report the emerging signals separately. Signals are later-stage facts showing up early, and they change priorities
without changing the archetype. Agents emerging means an intake and lifecycle route is needed now; shadow AI means an
approved-use starter and safe alternatives come first; a requested CoE means the CoE programme is in scope; no AI policy
and weak knowledge are preconditions to fix. An adopter with agents emerging gets the agent-factory programme as well as
adoption, which is exactly the point of reporting signals.

Write a one-page summary for the sponsor: edition with rule id, overlay with rule id, archetype with rule id, signals with
rule ids, and what each means for the programme. State that editions and archetypes are proposed CopilotForge
classifications, not Microsoft's. List the provisional facts and what would change if they moved.

Ask the sponsor to confirm before continuing. If they disagree with the edition, record their decision and reason; if
they disagree with the archetype, explain which foundation is missing and offer to revisit when it is in place. Only
then hand to `organisation-tailoring:transformation-pack`.

## Outputs

- A tailoring recommendation: edition, assurance overlay, archetype and emerging signals, each with its rule id and rationale from `references/tailoring-rules.yaml`.
- A one-page sponsor explanation of what the recommendation means for the CoE, Champions, governance and programmes.
- A record of the sponsor's confirmation, or of any edition override with its reason.

## Microsoft platform considerations

Not applicable in depth, because the rules are platform-neutral and depend on organisational facts. Do not cite Microsoft
maturity models as the source of the archetypes; where Microsoft adoption or agent maturity guidance is useful for
context, check `references/sources.md`.

## Adoption considerations

The archetype tells the sponsor where adoption effort should go. For explorers and adopters, adoption and Champions are
the main programme; for builders, agent lifecycle and governance join them.

## Knowledge considerations

Report weak knowledge as a signal even when it does not change the archetype, because it governs whether agent work can
succeed. Name it as a precondition in the sponsor summary.

## Security and privacy considerations

The formal assurance overlay changes evidence requirements at every gate; make sure the sponsor understands this before
confirming. Keep the profile and recommendation in the organisation's own storage.

## Responsible AI considerations

Explain that the classifications are proposals with stated rules, not judgements about the organisation's people. Never
use the archetype to rank departments or individuals.

## Evaluation requirements

Not applicable to an AI solution; the recommendation is tested by repeatability: the same profile must give the same
result, which the golden tests behind the rules check.

## Value measures

Not a value-bearing artefact itself; the sponsor's confirmed outcomes flow to `ai-centre-of-excellence:coe-kpi-framework`,
where baselines and owners are set.

## Scale notes

### Starter

A five-minute explanation: working group, light artefacts, the two or three signals that matter. Confirm in the same
conversation.

### Scale

A one-page summary taken to the sponsor, with signals mapped to programmes and provisional facts named.

### Enterprise

Run the rules for the whole organisation and, where units differ materially, for each business unit. Record overrides
formally where the assurance overlay is formal.

## Hand-offs

- To `organisation-tailoring:transformation-pack` once the sponsor confirms.
- Back to `organisation-tailoring:ai-profile-intake` if a deciding fact is wrong or provisional.

## Reviewer gates

Not applicable, because the recommendation releases no solution; the sponsor's confirmation is the gate before the pack
is built, and gates for later solutions, such as `security-privacy` from tier 2, are carried into the pack.

## Failure modes

- The archetype is bumped up to flatter the sponsor, and the pack skips foundations.
- Signals are treated as the archetype, so an adopter receives a scaler programme.
- Rules are applied loosely, and two runs on the same profile give different answers.
- The recommendation is presented as a Microsoft classification.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Change the rules or their order to reach a preferred answer.
- Place an organisation beyond a foundation it has skipped.
- Present editions or archetypes as Microsoft classifications.
- Continue to the pack without the sponsor's confirmation.

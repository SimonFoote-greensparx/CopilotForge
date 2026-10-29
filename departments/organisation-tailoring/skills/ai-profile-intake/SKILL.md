---
name: ai-profile-intake
description: Creates or validates an organisation profile - size, business units, regulatory context, Microsoft estate, current AI use, knowledge, governance, adoption and delivery capability - by short interview or from a file, capturing only what tailoring needs and marking unknowns. Use when someone asks for help with an AI programme and no profile exists, when a profile file is supplied, or when circumstances have changed since the last pack.
license: CC-BY-4.0
metadata:
  department: organisation-tailoring
  lifecycle: Discover
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-overview, ms-copilot-privacy, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# AI profile intake

## Purpose

Every tailored recommendation in CopilotForge starts from an organisation profile: a short, structured statement of the
facts that change the advice. This skill builds that profile through a focused interview, or validates one the
organisation already has, against `references/profile-schema.json`. It captures only what tailoring needs, records
roles and aliases rather than names, and marks every unknown so nothing downstream is invented. Intake goes wrong when it
becomes a long questionnaire nobody finishes, when guesses are recorded as facts, or when the profile ends up somewhere
it should not be stored.

## When to use

- Someone asks for help with Copilot, agents, a CoE or an AI programme and no profile exists yet.
- An organisation supplies a profile file that needs validating before a pack is produced.
- Circumstances have changed (a merger, new business units, agents appearing, a new policy) and the profile is stale.
- A pack is being refreshed and the profile must be confirmed first.

## When not to use

- Turning a valid profile into an edition, assurance overlay and archetype - use `organisation-tailoring:edition-and-archetype`.
- Producing the transformation pack from a confirmed profile - use `organisation-tailoring:transformation-pack`.
- A full AI maturity assessment with evidence and scoring - use `ai-strategy:ai-maturity-assessment`.
- Assessing readiness of a specific audience for Copilot adoption - use `copilot-adoption:adoption-readiness`.

## Questions to ask first

1. How many people work in the organisation, in how many business units that set their own priorities, and in which countries?
2. Does a regulator expect formal, auditable assurance of how you use AI, or is the regulatory context low or medium?
3. Which Microsoft AI tools are in use today, how consistently, and are staff already building agents or using unapproved tools?
4. Is there an approved AI acceptable-use policy, a CoE or working group, and any Champions?
5. What internal delivery capability exists (makers, developers, partners), and what is the main constraint (budget, capacity, timeline)?
6. Which role sponsors this work, and what outcomes do they want in the next year?

## Required inputs

- The person's answers, or an existing profile file in YAML.
- `references/profile-schema.json`, which defines the fields, allowed values and required sections.
- `references/sample-profile.yaml`, a fictional complete example to show the expected shape.

Required fields are listed in the schema. Where an optional fact is unknown, omit it so the tailoring plan lists it
under facts to confirm; where a required fact is unknown, record the most cautious honest value only with the person's
agreement and note it as provisional. Never guess a workforce size, a licence count or a policy status.

## Decision framework

| Situation | Action |
|---|---|
| A profile file is supplied | Validate against `references/profile-schema.json`; report each error in plain language; ask only for what is missing or invalid |
| No profile, short time available | Ask the six questions above, fill required fields, leave optional ones blank |
| No profile, a working session available | Add personas, knowledge, data sensitivity, portfolio and constraints |
| Answer is uncertain | Record the cautious value as provisional, or leave optional fields out; never round up maturity |
| Answer includes a personal name or personal data | Replace with a role or alias before recording |
| Answer contradicts another (for example "no agents" but "makers building agents") | Ask once to resolve; if unresolved, record both in a note and flag it |

The profile is ready when it validates against the schema, every required field has a confirmed or provisional value,
and the person agrees it is a fair description.

## Practitioner approach

Explain the purpose in one sentence before asking anything: "I need a few facts about your organisation so the advice
fits its size, risk and starting point." Then ask the questions above in conversation, not as a form. Most people can
answer them in ten minutes, and that is enough for a first tailoring plan.

Listen for the facts the rules depend on. Workforce size, number of business units and regulatory level decide the
edition. How consistently Copilot is used, whether Champions exist, whether a CoE is established, how many business
units run their own solutions and whether custom AI is in production decide the archetype. Agents already built,
suspected unsanctioned use, a requested CoE, the absence of a policy and weak knowledge ownership are signals that
change priorities. Probe these gently: "When you say departments are starting to build agents, roughly how many exist
today?" is better than "Do you have agents?".

Translate answers into the schema's values and read them back. "Usage is patchy, some teams use it daily and others not
at all" becomes a usage pattern of inconsistent; say so and check. Where the person is unsure, record the cautious value
as provisional, or leave the optional field out so it appears under facts to confirm. Do not round an organisation up;
an optimistic profile produces advice that skips foundations.

Use roles and aliases throughout. The sponsor is "Chief Operating Officer", not a name. The organisation may be an alias
if the person prefers. Do not record personal data, client names or commercially sensitive details the tailoring does
not need.

If a file is supplied, validate it and report problems in plain language: "business units must be a whole number" rather
than a schema error. Ask only about what is missing or invalid.

Agree where the profile will live before saving it. A real profile is the organisation's information and belongs in its
own storage, such as the person's OneDrive, a private project location or the git-ignored input folder of a local clone,
never in a public repository or a shared sample folder. Show the final YAML, confirm it is a fair description, and hand
it to `organisation-tailoring:edition-and-archetype`.

## Outputs

- A valid organisation profile in YAML, conforming to `references/profile-schema.json`, saved in the organisation's own storage.
- A short list of provisional values and facts to confirm, with who can confirm each.
- A plain-language read-back the person has agreed.

## Microsoft platform considerations

The profile records which Microsoft tools are in use, but not product facts. Do not infer licensing, availability or
feature access from the profile. Microsoft product names are changing, so record what the organisation calls a tool and
map it to the schema; the source records in `references/sources.md` describe current naming.

## Adoption considerations

The usage pattern and Champions fields shape the adoption advice. Ask about frontline and desk-based roles separately,
because inconsistent use often means one group is well served and another is not.

## Knowledge considerations

Ask who owns the main knowledge repositories and how current they are. Weak ownership or quality is one of the most
consequential signals, because it governs whether agents can be trusted.

## Security and privacy considerations

The profile is organisational information. Keep it in the organisation's own storage with access limited to the people
preparing the pack. Record no personal data; if an answer includes a name, replace it with a role. The organisation's
data protection officer decides how long the profile is kept.

## Responsible AI considerations

Not applicable in depth at intake, which records context rather than assessing a use; capture the regulatory notes and
any known high-impact uses so later skills can route them to `responsible-ai:ai-impact-assessment`.

## Evaluation requirements

Not applicable, because the profile is an input rather than an AI solution; its quality test is that it validates
against the schema and the person agrees it is accurate.

## Value measures

Not a value-bearing artefact itself. Record the sponsor's target outcomes so `ai-centre-of-excellence:coe-kpi-framework`
can set baselines later; the sponsor role owns them.

## Scale notes

### Starter

Six questions, required fields only, ten minutes. Leave optional sections out and let the plan list them as facts to
confirm.

### Scale

Add personas with headcount, knowledge ownership, data sensitivity, portfolio counts and constraints in a working session
with the sponsor's delegate.

### Enterprise

Capture per business unit where units differ materially, and confirm regulatory context with risk and compliance roles.
Expect the profile to be refreshed at each major phase.

## Hand-offs

- To `organisation-tailoring:edition-and-archetype` with the validated profile.
- To `ai-strategy:ai-maturity-assessment` when a deeper, evidenced assessment is needed.

## Reviewer gates

Not applicable, because intake records context and releases nothing; the profile's storage location should follow the
organisation's information security policy, and `security-privacy` may be consulted on it.

## Failure modes

- Intake becomes a forty-question survey and the profile is never finished.
- Optimistic answers are recorded as facts, and the pack skips foundations the organisation does not have.
- Personal names or client details are recorded and then copied into every artefact.
- The profile is saved into a shared or public location.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Record personal names or personal data in a profile; use roles and aliases.
- Invent a fact the person did not give, or round maturity up.
- Save a real profile into a public repository or the samples folder.
- Infer licensing or product availability from the profile.

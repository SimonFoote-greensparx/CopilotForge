---
name: practice-labs
description: Designs safe hands-on practice for AI learning - realistic fictional scenario packs, practice spaces matched to what is being learnt from a learner's own approved tools to isolated maker and specialist sandboxes, rules on what may enter them, reset and clean-up, and lab exercises with expected results and a check step. Use when training is all demonstration, when people practise on live customer data, or when makers need somewhere safe to build.
license: CC-BY-4.0
metadata:
  department: learning-and-skills
  lifecycle: Enable, Deliver, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-studio, power-platform, copilot-code, ai-foundry, sharepoint
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-privacy, ms-managed-environments, ms-copilot-studio-zoned-governance, ms-agent-builder, ms-foundry-models, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# Practice labs

## Purpose

People learn to use Microsoft AI by using it, checking what comes back and trying again, and that needs somewhere safe
to do it. This skill designs practice labs - the scenario packs, practice spaces, data rules, exercises and clean-up -
so learners can practise realistically without exposing real data or creating ungoverned solutions. It usually goes
wrong when practice is replaced by demonstration, when "realistic" material turns out to be copied real data, when
fictional content placed in the live tenant is surfaced to people who never joined the training, or when maker
sandboxes become shadow production.

## When to use

- Training is mostly demonstration and learners leave without having tried anything themselves.
- Learners are practising on real customer, employee or confidential data because nothing else is available.
- A role curriculum or advanced track needs exercises with known good answers.
- Makers or specialists need a place to build agents, flows or code while learning, away from production.
- Old practice spaces are full of abandoned agents, flows and test content nobody owns.

## When not to use

- Setting the governance zones and environment strategy for all AI building - use `platform-governance:ai-environment-strategy`.
- Configuring the concrete Copilot Studio environments makers use for real work - use `copilot-studio:studio-environments`.
- Designing prompting guidance and verification checklists - use `m365-copilot:prompting-practice`.
- Writing the session plan in which a lab is used - use `learning-and-skills:facilitator-guide`.
- Deciding what evidence a lab exercise must produce - use `learning-and-skills:learning-evidence-rubric`.

## Questions to ask first

1. What will learners practise - everyday Copilot use, agents, delegated Cowork tasks, building, code or Foundry work - and at which pathway level?
2. Can learners practise on their own non-sensitive work with their own approved tools, or do they need shared fictional material?
3. Where does the organisation's environment strategy allow learning and building to happen, and with what controls?
4. Who owns each practice space, and who will reset it and clean it up?
5. What must never enter a lab - which data classes, connectors, secrets and external sharing?

## Required inputs

- The curricula or advanced tracks that need practice, with their exercises and evidence, from `learning-and-skills:ai-role-curriculum` or `learning-and-skills:advanced-pathways`.
- The environment strategy and zones from `platform-governance:ai-environment-strategy`, and data classification rules from `data-governance:data-classification-for-ai`.
- The approved-use guidance and approved tools for each learner group.
- A named owner for each practice space with time to maintain it.

If no environment strategy exists, do not create maker sandboxes; limit labs to own-work practice and read-only
fictional scenario packs, and record the gap. If no owner can be named for a practice space, do not create it.

## Decision framework

Choose the lightest lab that lets learners practise what the level requires.

| Lab type | Suits | Where it lives | Data allowed |
|---|---|---|---|
| Own-work practice | Foundation and Applied learning on Copilot Chat and the Microsoft 365 apps | The learner's own approved tools | The learner's own non-sensitive work they already have access to |
| Shared scenario pack | Group sessions, verification exercises, agent use | A restricted training site or team limited to learners and labelled as fictional | Fictional documents, mail and data only |
| Maker sandbox | Agent Builder, Copilot Studio, Power Platform automation | A dedicated learning environment in the personal or team zone, as the environment strategy allows | Fictional data; no connectors to production systems |
| Specialist lab | Copilot Code, Microsoft Foundry, evaluation practice | An isolated project, repository or subscription set by the environment strategy | Synthetic data; no production secrets or keys |

Apply these rules to every lab:

| Rule | Why |
|---|---|
| Fictional content is labelled fictional in its title and body | Grounded answers must never present it as real |
| Shared packs sit where only learners can reach them | Copilot can surface any content a user has access to |
| Every lab has an owner, a reset routine and an expiry | Labs left running become ungoverned |
| Anything worth keeping moves out through the normal intake and release route | Lab builds are never promoted directly |

## Practitioner approach

Start with own-work practice wherever you can. For foundation and applied learning, the best lab is the learner's own
approved Copilot on their own non-sensitive work: a real document to summarise, a real meeting to recap, a real draft to
improve. It needs no build, it is immediately relevant, and it produces evidence of real practice. Give clear guidance
on what to choose and what to avoid, such as anything about named colleagues, health or customer details.

Use shared scenario packs where own work will not do: group sessions where everyone needs the same material,
verification exercises where you need a known right answer, or roles whose real work is too sensitive. Write a small,
coherent fictional world - a fictional organisation, its projects, mail threads, a policy with a deliberate exception
and a spreadsheet with an error in it - so that exercises can test whether learners catch omissions and mistakes. Never
build "fictional" material by lightly editing real records.

Think carefully about where shared packs live. Microsoft 365 Copilot answers from content a user can access, so a
fictional pack placed in a broadly shared site can turn up in real work for people who never joined the training.
Keep packs in a restricted site or team for learners, label every item as fictional, and remove access when the cohort
finishes. If practice reveals that learners can reach real content they should not, stop and report it through the
security route rather than continuing the exercise.

For makers, the sandbox follows the environment strategy, not the learning team's convenience. Agree with the platform
owner which zone hosts learning builds, the data policies that apply, and that no production connectors or real data
are used. Set an expiry for learning builds and a monthly clean-up, and tell makers at the start that nothing built in
the sandbox is shared beyond the cohort or promoted directly. A build worth keeping goes through intake and release
like any other solution.

Specialist labs for Copilot Code and Microsoft Foundry need isolation, synthetic data, cost limits agreed with the
platform owner and no real secrets. Treat model or deployment choices in a lab as practice, not precedent.

Write every exercise with an expected result and a check step: what a good output contains, the error that should be
caught, and what the learner records as evidence. Test each exercise against the current product before every cohort,
because Copilot's answers vary and features change.

Finally, give each lab an owner, a reset routine, an expiry and a short record of what it contains and who can reach it.

## Outputs

- A lab catalogue in the practice environment section of the `ai-learning-plan` template - lab type, purpose, location, access, data allowed, owner, reset routine and expiry.
- Fictional scenario packs with a content list, labelling and the deliberate errors and exceptions they contain.
- Lab exercises with instructions, expected results, the check step and the evidence they produce.
- Lab rules for learners covering what may and may not enter, sharing limits and how to report a problem.
- Where maker or specialist labs are needed, a request recorded against the `environment-zoning-plan` template.

## Microsoft platform considerations

Own-work practice uses whichever Copilot experiences the learner is approved for. Shared packs usually sit in a
restricted SharePoint site or team. Maker sandboxes for Agent Builder, Copilot Studio and Power Platform follow the
organisation's environment zones and Managed Environments settings; specialist labs follow the Foundry and code
repository arrangements set by the environment strategy. Environment features, limits and costs change, so check
`references/sources.md` and the platform owner before designing a lab, and route licensing or capacity questions to
`platform-governance:ai-licensing-and-capacity`.

## Adoption considerations

Practice is where confidence comes from. Labs should feel low-stakes: learners are told mistakes are expected, nothing
in the lab is assessed as performance, and the point is to see where AI helps and where it gets things wrong.

## Knowledge considerations

Scenario packs are curated knowledge assets with an owner, version and review date. Keep a content list so exercises
can be updated when the pack changes, and retire packs that no longer match current scenarios.

## Security and privacy considerations

Labs never contain real personal, customer or confidential data, production connectors or live secrets. Shared packs
are restricted to learners and removed after use. If practice exposes oversharing of real content, it is reported to
the security route and referred to `security-privacy:data-exposure-review`. Maker and specialist labs are agreed with
the platform owner and reviewed by the security function before first use.

## Responsible AI considerations

Exercises deliberately include errors, omissions and ambiguous cases so learners practise verification and judgement,
not only speed. Fictional scenarios avoid stereotypes and do not use real people's names.

## Evaluation requirements

Not applicable as AI evaluation, because labs do not release an AI solution. Each exercise is checked against the
current product before a cohort, so its expected result still holds.

## Value measures

Baseline: the share of sessions in each curriculum that include hands-on practice today. Measures: share of modules with
a tested lab exercise, lab-based evidence meeting the rubric at role level, and the number of expired lab artefacts
cleaned up on schedule. Owned by the Learning Lead with the platform owner for sandboxes.

## Scale notes

### Starter

Own-work practice guidance and one shared fictional scenario pack in a restricted site, owned by the adoption or
learning lead.

### Scale

A small catalogue of scenario packs by role family, a maker sandbox in the agreed zone with expiry and clean-up, and
exercises tested before each cohort.

### Enterprise

A managed lab service with packs localised by region, maker and specialist labs per business unit under the central
environment strategy, automated reset and an inventory of lab artefacts.

## Hand-offs

- To `platform-governance:ai-environment-strategy` where no zone exists for learning builds.
- To `learning-and-skills:facilitator-guide` to embed lab exercises in sessions.
- To `learning-and-skills:learning-evidence-rubric` to align exercise outputs with evidence.
- To `security-privacy:data-exposure-review` if practice reveals learners can reach content they should not.

## Reviewer gates

`security-privacy` reviews maker sandboxes, specialist labs and any shared scenario pack placed in the live tenant
before first use, from risk tier 1, checking data rules, access restriction, connectors and clean-up. Own-work practice
on approved tools needs no separate gate.

## Failure modes

- Fictional packs are placed in a widely shared site and surface in real Copilot answers for people outside the training.
- "Fictional" material is real data with names changed, and still identifies people or customers.
- Maker sandboxes have no expiry, and learning builds are quietly used for real work.
- Exercises have no expected result, so learners cannot tell whether they verified anything.
- Exercises are not retested and fail live because the product has changed.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Put real personal, customer or confidential data into a lab or scenario pack.
- Connect a learning sandbox to production systems or use live secrets in it.
- Promote a lab build to shared or production use without going through intake and release.
- Leave a practice space without an owner, a reset routine and an expiry.

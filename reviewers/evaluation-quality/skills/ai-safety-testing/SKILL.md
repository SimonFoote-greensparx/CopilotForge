---
name: ai-safety-testing
description: Tests and reviews whether an AI solution avoids harmful outputs for its audience - hateful, violent, sexual or self-harm content, dangerous or regulated advice, demeaning statements about people, and poor handling of users in distress - checking platform content controls as configured, classing findings blocking or advisory. Use when a solution reaches the public or a broad workforce, or after harmful output is reported.
license: CC-BY-4.0
metadata:
  department: evaluation-quality
  lifecycle: Deliver, Assure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 2, 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, copilot-cowork
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality, responsible-ai
  sources: ms-responsible-ai, ms-foundry-models, ms-copilot-studio-guidance, ms-copilot-studio-security-governance, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI safety testing

## Purpose

An AI solution can be correct and grounded most of the time and still cause harm on the occasions it produces offensive,
dangerous or demeaning content, or responds badly to someone in distress. Platform content controls reduce that risk;
they do not remove it, and their configuration and the solution's own instructions change what gets through. This
reviewer skill designs and reviews scripted safety tests for the harms that matter to a solution's audience and
domain, checks content controls as actually configured, and classifies each finding as blocking or advisory. Safety
testing goes wrong when teams assume platform filters cover everything, or test generic harms while missing the
domain-specific ones such as unsafe workplace advice.

## When to use

- A solution at tier 2 or above will be used by a broad workforce, customers or the public.
- A solution operates in a domain where advice can cause harm, such as health, safety, finance, legal or employment matters.
- Content control settings, the model or the solution's instructions have changed.
- A user has reported an offensive, unsafe or distressing output.
- Safety evidence is submitted to the `evaluation-quality` gate.

## When not to use

- Prompt injection, data exfiltration and attacks on tools or connectors - use `security-privacy:ai-security-testing`.
- Planning an open-ended adversarial exercise with a dedicated team - use `evaluation-quality:red-team-plan`.
- Configuring content safety controls in Microsoft Foundry - use `ai-foundry:foundry-safety-evaluation`.
- Deciding whether a use should be built at all - use `responsible-ai:prohibited-use-review`.
- Bias and unequal treatment across groups of people - use `responsible-ai:fairness-review`.

## Questions to ask first

1. Who will use the solution, including vulnerable users, customers or the public, and in what state might they arrive?
2. Which domain harms apply - unsafe instructions, medical, legal or financial advice, statements about named people?
3. Which content controls apply on the chosen route, at what settings, and who changed them from the defaults?
4. What should the solution do when a user discloses distress, risk of harm or a safeguarding concern?
5. Who will run tests that involve distressing content, and how will they be supported?

## Required inputs

- The solution brief with audience, domain, scope and behaviour rules, and the risk tier.
- The content control configuration for the route, confirmed by the builder.
- The organisation's escalation routes for distress and safeguarding, confirmed with HR or the relevant owner.
- A harm catalogue for the domain, built with subject experts.

Where escalation routes for distress are not defined, the solution cannot be tested against them; record that as
blocking from tier 2 for any solution reachable by a broad workforce or the public.

## Decision framework

Build tests in four categories and scale depth by tier.

| Category | Examples of what to test | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| General harmful content | Hateful, violent, sexual or self-harm content, requested directly and indirectly | Core set | Core set with paraphrases | Plus independent testers |
| Domain harm | Unsafe instructions, regulated advice without caveats, made-up procedures in safety-critical work | Domain set from experts | Expanded with variants | Plus scenario walk-throughs |
| Harm to people | Demeaning or speculative statements about named individuals or groups | Core set | Expanded | Plus review with `responsible-ai` |
| Distress handling | Disclosures of distress, risk or safeguarding concern | Required if broad audience | Required | Required with oversight evidence |

Classify findings.

| Finding | Blocking from tier 2 when | Advisory when |
|---|---|---|
| Harmful content produced | Any occurrence in general or harm-to-people categories | Not applicable; any harmful output is blocking |
| Domain advice | Unsafe or uncaveated advice on safety, health, legal or financial topics | Caveats present but weakly worded |
| Distress handling | No safe response or no route to help | Route given but tone needs work |
| Over-refusal | Not blocking unless it prevents a safety-critical use | Legitimate questions refused, harming usefulness |
| Controls | Content controls lowered from defaults without a recorded decision | Settings documented but rationale thin |

## Practitioner approach

Start with a harm catalogue specific to the solution. Sit with a subject expert and the business owner and list what a
harmful answer would look like for this audience: a maintenance agent describing a shortcut that bypasses a safety
lock, an HR agent giving definitive legal advice on dismissal, a customer agent repeating a slur from a complaint it
summarised. Generic harm lists miss these, and they are usually the ones that matter most.

Write test items for each catalogue entry, directly and indirectly. Direct requests test whether the solution refuses;
indirect ones test whether harmful content slips out while answering something reasonable, such as summarising a
document that contains offensive language. Add role-play and hypothetical framings, which often get past instructions
that only cover direct requests. Keep items in a restricted dataset; they are harmful by design.

Confirm the content controls as configured, not as assumed. Ask the builder to show the current settings for the route
and any changes from defaults, and record who approved each change and why. Then test the solution with those
settings. Where controls were loosened for a legitimate reason, test the categories they affect more deeply.

Test distress handling with care. Agree the expected behaviour with HR or the safeguarding owner: acknowledge, avoid
giving advice beyond the solution's role, and point to the organisation's support routes. Write a small number of
realistic disclosures and check the response every time; this category does not tolerate variation.

Run each item more than once, because outputs vary. Score with the safety dimension from
`evaluation-quality:ai-quality-rubric`: pass or fail, with no partial credit. Record the actual output for every failure.

Look for over-refusal too. A solution that refuses ordinary questions about, say, medication storage in a care setting
is safe and useless. Note over-refusals as advisory unless they block a safety-critical use, and route them to the
builder.

Protect the testers. Safety testing exposes people to distressing material. Use volunteers who have been briefed, rotate
the work, and offer the organisation's support services. Never assign this testing to someone without their agreement.

Report failures with causes - instructions, knowledge content, configuration or model behaviour - and re-test after each
fix. Harmful output in the general or harm-to-people categories is never traded against other dimensions.

## Outputs

- A safety test set by category, held in a restricted location, linked from the `evaluation-plan`.
- A record of content control settings as tested, with approvals for any change from defaults.
- A safety results record with failures, causes, fixes and re-test outcomes, classified blocking or advisory.
- Agreed expected behaviour for distress disclosures, with the owner who confirmed it.

## Microsoft platform considerations

Microsoft provides content safety controls across Copilot Studio and Microsoft Foundry, and Microsoft's responsible AI
resources describe its approach. Which controls exist, their defaults and how they are configured differ by route and
change over time; confirm them in `ms-copilot-studio-guidance`, `ms-copilot-studio-security-governance`,
`ms-foundry-models` and `ms-responsible-ai`. Detailed Foundry configuration belongs with `ai-foundry:foundry-safety-evaluation`.

## Adoption considerations

Tell users what the solution will not help with and where to go instead. A clear refusal with a useful redirect keeps
trust; an unexplained refusal drives people to unapproved tools.

## Knowledge considerations

Harmful content can enter through grounding, for example quoted complaints or historical documents. Where tests show
this, work with the knowledge owner to remove or restrict the content rather than relying on filters alone.

## Security and privacy considerations

Safety and security tests overlap at jailbreak attempts. Share jailbreak findings with `security-privacy:ai-security-testing`
so they are tested as attacks too. Restrict access to safety datasets and recorded outputs.

## Responsible AI considerations

Safety testing provides evidence to the `responsible-ai` reviewers, especially `responsible-ai:human-oversight` for
distress handling and `responsible-ai:ai-impact-assessment` for domain harms. A pattern of harmful outputs may mean the
use should not proceed, which is their decision.

## Evaluation requirements

This skill supplies the safe dimension of evaluation. Minimum from tier 2: a domain harm catalogue, test items in every
applicable category run more than once, content controls recorded as tested, and zero harmful outputs in the general and
harm-to-people categories.

## Value measures

Track safety failures found before release versus reported after, time to fix and re-test, and over-refusal reports.
The AI Evaluation Lead reports by solution; never by tester, maker or user.

## Scale notes

### Starter

A short domain harm catalogue built with one expert, a core set of harmful and distress items run three times each,
and the content settings recorded.

### Scale

Shared safety test sets by domain, reused across solutions, with solution-specific additions and a briefed pool of
volunteer testers who rotate.

### Enterprise

Central safety standards and datasets owned by `evaluation-quality`, independent testers for tier 4, red-team findings
feeding the sets, and portfolio-level tracking of safety incidents and near misses.

## Hand-offs

- To `evaluation-quality:red-team-plan` from tier 3 for open-ended adversarial testing.
- To `security-privacy:ai-security-testing` with jailbreak findings.
- To `responsible-ai:human-oversight` and `responsible-ai:ai-impact-assessment` with distress and domain harm evidence.
- To `evaluation-quality:ai-release-evidence` with results.

## Reviewer gates

This skill operates within the `evaluation-quality` gate from risk tier 2, with `responsible-ai` reviewing distress and
harm-to-people evidence from tier 3. Blocking findings stop release and are not traded against dates; disagreement
escalates to the accountable executive for written risk acceptance.

## Failure modes

- Platform filters are assumed to cover every harm, so domain-specific dangerous advice is never tested.
- Content controls were loosened during build to fix over-refusal and nobody re-tested.
- Distress disclosures produce a generic reply with no route to help.
- Testers are exposed to harmful material without agreement or support.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Pass a solution that produced harmful content in the general or harm-to-people categories.
- Assume platform content controls are configured as the defaults without checking.
- Assign safety testing involving distressing content to anyone without their agreement and support.
- Store harmful test items where an agent or a general audience could reach them.

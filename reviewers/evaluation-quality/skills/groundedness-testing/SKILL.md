---
name: groundedness-testing
description: Tests and reviews whether an AI solution's answers are supported by the permitted sources it cites - claim-level support, citation accuracy, behaviour when knowledge is silent, stale or contradictory, and blending with model or web knowledge - classing findings blocking or advisory. Use when a knowledge-grounded agent or retrieval solution approaches release, after knowledge changes, or when users report invented or wrongly cited answers.
license: CC-BY-4.0
metadata:
  department: evaluation-quality
  lifecycle: Deliver, Assure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-copilot, m365-agents, copilot-cowork, copilot-studio, ai-foundry, sharepoint
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality
  sources: ms-copilot-privacy, ms-declarative-agents, ms-agent-builder, ms-copilot-studio-guidance, ms-foundry-models, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Groundedness testing

## Purpose

A grounded answer is one whose claims are supported by the sources the solution is permitted to use, with citations
that lead a user to the supporting passage. Fluent, confident answers that are not supported are the failure users find
hardest to detect and most damaging to trust. This reviewer skill tests groundedness at the level of individual claims
and citations, probes what the solution does when its knowledge is silent, stale or contradictory, and reviews
groundedness evidence submitted by teams, classifying each finding as blocking or advisory. Testing usually goes wrong
when a citation's presence is taken as proof of support, or when nobody checks what happens when the answer is not in
the knowledge at all.

## When to use

- A knowledge-grounded agent, Cowork workflow or retrieval solution at tier 2 or above approaches release.
- Knowledge sources have been added, restructured or substantially updated.
- Users report answers that sound right but cannot be found in the cited documents.
- The solution can draw on web content or general model knowledge as well as internal sources.
- Groundedness evidence is submitted to the `evaluation-quality` gate.

## When not to use

- Deciding whether knowledge sources are owned, current and fit to ground on before build - use `m365-agents:knowledge-source-readiness`.
- Designing how grounding or retrieval works in the first place - use `m365-agents:agent-grounding` or `ai-foundry:retrieval-design`.
- Scoring overall correctness, tone and scope with a rubric - use `evaluation-quality:ai-quality-rubric`.
- Checking whether grounding exposes content to the wrong people - use `security-privacy:data-exposure-review`.

## Questions to ask first

1. Which sources is the solution permitted to answer from, and which is authoritative when they disagree?
2. Should the solution ever answer from general model knowledge or the web, and if so how should users be able to tell?
3. What should the solution say when the knowledge does not contain an answer?
4. Which topics carry the highest consequence if an answer is invented, such as policy, legal, safety or financial matters?
5. How will testers verify claims - who can open the sources and has time to read them?

## Required inputs

- The golden dataset with expected sources, including knowledge-silent and contradiction items, from `evaluation-quality:golden-dataset`.
- The list of permitted knowledge sources, their owners and versions at the time of testing.
- The solution's behaviour rules for silence, uncertainty and web or model knowledge.
- Testers entitled to open every permitted source.

Where testers cannot open the sources, claims cannot be verified and groundedness is untested; record that as blocking
from tier 2 rather than accepting the citation list as evidence.

## Decision framework

Test four things, each with its own pass criterion.

| Test | What is checked | Pass when |
|---|---|---|
| Claim support | Each factual claim in a sample of answers is traced to a passage in a permitted source | Every material claim is supported; minor connective phrasing excepted |
| Citation accuracy | Each citation leads to a passage that supports the claim it is attached to | Citations point to the supporting passage, not merely a related document |
| Silence handling | Knowledge-silent items | The solution says it cannot answer from its sources and redirects as specified, without inventing |
| Conflict and currency | Contradiction items and items whose source recently changed | The solution uses the authoritative or current version, or surfaces the conflict |

Where web or general model knowledge is permitted, add a provenance test: users can tell which parts of an answer came
from outside the organisation's sources.

Classify findings.

| Finding | Blocking from tier 2 when | Advisory when |
|---|---|---|
| Unsupported claims | Any on a high-consequence topic, or a rate above the agreed threshold elsewhere | Isolated, low-consequence, with a clear cause and fix |
| Wrong citations | Citations routinely point to documents that do not support the claim | Citation precise to document but not section |
| Silence handling | The solution invents answers when knowledge is silent | Redirect wording unclear but no invention |
| Conflicts | Superseded content used on policy, legal, safety or financial topics | Minor inconsistency on low-consequence topics |
| Provenance | Web or model content presented as internal guidance | Provenance shown but easy to miss |

## Practitioner approach

Sample, then go claim by claim. From the latest evaluation run, take a sample of answers across categories, weighted
towards high-consequence topics. Break each answer into its factual claims - a figure, a rule, a date, an eligibility
condition, a step - and for each claim find the passage that supports it in a permitted source. Record supported,
partly supported or unsupported. This is slower than checking whether an answer "looks right", and it is the only way to
find fluent inventions.

Check every citation against the claim it sits beside. A citation to the right policy that does not contain the stated
rule is a failure, because users who check it will find nothing and stop trusting the solution. Note whether citations
are precise enough for a user to find the passage quickly.

Run the knowledge-silent items several times. Solutions that refuse correctly once may invent on a second attempt or a
paraphrase. The pass condition is consistent: the solution says it cannot answer from its sources and points somewhere
useful.

Probe currency and conflict deliberately. Use the contradictions recorded during knowledge readiness, and add items
about content that changed recently, to see whether the solution prefers the current version. Where the old version is
still reachable, the fix is almost always to retire or restrict it at source, not to instruct the solution to prefer
newer files.

If web or general model knowledge is enabled, ask questions that the internal sources answer differently from public
information and check which answer appears and how it is labelled.

Trace each failure to a cause before recommending a fix: missing or poor knowledge, retrieval not finding the right
passage, instructions encouraging the model to fill gaps, or configuration such as web grounding left on. Route
knowledge causes to the knowledge owner, retrieval causes to the builders and configuration causes to the maker, and
re-test the affected items after each fix.

AI-assisted groundedness scoring can scale this work, but treat it as a filter until it has been compared with human
claim checks on a sample. Report results as rates per test, with high-consequence failures listed individually.

## Outputs

- A groundedness test record: sample, claims checked, support rate, citation accuracy, silence and conflict results, provenance findings and causes.
- Findings classified blocking or advisory with the risk, fix and owner, attached to the `evaluation-plan` results.
- A list of knowledge defects passed to knowledge owners, with re-test items.

## Microsoft platform considerations

Microsoft 365 Copilot, agents built in Agent Builder or Copilot Studio, and Microsoft Foundry solutions ground and cite
in different ways, and controls for web grounding and knowledge scope differ by route and change over time. Confirm
current behaviour in `ms-copilot-privacy`, `ms-declarative-agents`, `ms-agent-builder`, `ms-copilot-studio-guidance`
and `ms-foundry-models`, and record the configuration under which tests ran.

## Adoption considerations

Teach users to check citations on important answers, and make it easy to report an answer that the citation does not
support. Users who see invented answers corrected quickly keep using the solution.

## Knowledge considerations

Most groundedness failures are knowledge failures: duplicates, superseded versions, gaps and contradictions. Pass them
to `knowledge-management:content-quality` and the knowledge owner, and treat repeated failures as a sign the source
needs restructuring for grounding.

## Security and privacy considerations

Testers must be entitled to open every source they verify against. If a citation reveals a document the tester should
not see, stop and raise it with `security-privacy:data-exposure-review`.

## Responsible AI considerations

Invented answers about people, eligibility or entitlements cause real harm. Treat unsupported claims on those topics as
high consequence and involve `responsible-ai:ai-transparency` on how uncertainty is shown to users.

## Evaluation requirements

This skill supplies the grounded dimension of evaluation. Minimum from tier 2: claim-level checks on a sample weighted
to high-consequence topics, citation accuracy recorded, knowledge-silent items run repeatedly, and conflict items tested.

## Value measures

Track support rate and citation accuracy per release, the number of knowledge defects found and fixed, and user reports
of unsupported answers after launch. The AI Evaluation Lead reports by solution, never by maker or tester.

## Scale notes

### Starter

Check every claim in a dozen answers on the topics that matter most, run the knowledge-silent questions three times
each, and fix contradictions at source.

### Scale

A standard groundedness record across solutions, sampling weighted by consequence, and calibrated AI-assisted support
scoring to extend coverage.

### Enterprise

Groundedness testing built into regression runs for every grounded solution, with trends tracked across the portfolio
and recurring knowledge defects fed into estate-wide content programmes.

## Hand-offs

- To the knowledge owner and `knowledge-management:content-quality` for knowledge-caused failures.
- To `m365-agents:agent-grounding` or `ai-foundry:retrieval-design` for retrieval and configuration fixes.
- To `evaluation-quality:regression-evaluation` with the items to re-run after fixes.
- To `evaluation-quality:ai-release-evidence` with results and findings.

## Reviewer gates

This skill operates within the `evaluation-quality` gate and is blocking from risk tier 2 and advisory below it.
Blocking findings stop release and are not traded against dates; disagreement escalates to the accountable executive
for written risk acceptance.

## Failure modes

- A citation's presence is accepted as proof that the claim is supported.
- Knowledge-silent questions are run once, pass, and the solution invents on the next attempt.
- Instructions telling the solution to prefer recent files are used in place of retiring superseded content.
- Web grounding is left on and public information is presented as internal policy.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Accept citations as evidence of support without checking the cited passage.
- Pass a tier 2 or higher solution that invents answers when its knowledge is silent.
- Fix superseded-content failures with instructions instead of at the source.
- Verify claims against sources the tester is not entitled to open.

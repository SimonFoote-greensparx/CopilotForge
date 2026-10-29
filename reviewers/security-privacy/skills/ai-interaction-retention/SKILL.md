---
name: ai-interaction-retention
description: Reviews how a specific AI solution stores prompts, responses, transcripts, traces, agent memory and generated files - where each lands, who can read it, which retention and deletion controls apply, and whether audit, eDiscovery and legal hold reach it - classifying each finding as blocking or advisory. Use when a solution reaches its security gate, when transcripts or tracing are switched on, or when nobody can say where conversations are kept.
license: CC-BY-4.0
metadata:
  department: security-privacy
  lifecycle: Assure, Launch, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-copilot, m365-agents, copilot-studio, ai-foundry, power-platform, purview, azure
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-privacy, ms-copilot-studio-security-governance, ms-foundry-models, ico-ai-data-protection, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# AI interaction retention

## Purpose

Every AI interaction leaves records: the prompt, the response, a transcript, perhaps a trace with retrieved passages, a
summary written to a system, a file the agent created, or a memory it keeps for next time. Those records often hold
more sensitive content than the sources they came from, because people type into AI what they would never write in a
document. This reviewer skill checks, for one solution, where each kind of interaction record lands, who can read it,
how long it lives and whether the organisation's retention, audit and legal hold controls reach it, and classifies each
finding as blocking or advisory. Reviews go wrong when the platform's default storage is assumed to satisfy the
organisation's rules, or when a second copy in a log or analytics store is forgotten entirely.

## When to use

- An AI solution at risk tier 2 or above reaches its `security-privacy` gate.
- Conversation transcripts, tracing, logging or analytics are about to be switched on or extended.
- An agent writes summaries, notes or files into business systems, or keeps memory between conversations.
- Legal, records or audit colleagues ask whether AI interactions are covered by holds and searches.
- Nobody can say where a solution's conversations are stored or who can read them.

## When not to use

- Setting the organisation's retention rules and periods for AI data - use `data-governance:ai-data-retention-rules`.
- Judging whether retaining personal data is lawful and proportionate, and DPIA screening - use `security-privacy:privacy-assessment`.
- Designing telemetry and logging for a pro-code solution - use `ai-engineering:ai-telemetry`.
- Reviewing who can reach grounding content through the solution - use `security-privacy:data-exposure-review`.

## Questions to ask first

1. What interaction records does this solution create - prompts, responses, transcripts, traces, analytics, memory, generated files, records in other systems?
2. Where does each one land, under which service, region and tenant boundary?
3. Who can read each store - users, makers, administrators, support, analysts, a supplier?
4. Which retention period and deletion control applies to each store, and who confirmed it matches the organisation's rules?
5. Can audit, eDiscovery and legal hold reach each store when the organisation needs them to?

## Required inputs

- The solution design, risk tier, channels and any logging, tracing or analytics configuration.
- The organisation's retention rules for AI data, from `data-governance:ai-data-retention-rules`, or its general records schedule.
- The privacy position from `security-privacy:privacy-assessment` where personal data is involved.
- Access lists for each store holding interaction records.

Where the organisation has no retention rule for AI interactions, record a blocking finding from tier 2 and route it to
`data-governance:ai-data-retention-rules` and the DPO. Never set a retention period on the organisation's behalf.

## Decision framework

Classify every finding. From risk tier 2 a blocking finding stops release and is not traded against dates; below tier 2
the review is advisory, but a finding that would be blocking means the tier needs re-checking.

| Area | Blocking when | Advisory when | Typical fix |
|---|---|---|---|
| Record map | Interaction stores are unknown or incomplete | All stores known but undocumented in the design | Complete the record map from configuration, not memory |
| Access to records | Makers, analysts or suppliers can read full transcripts containing confidential or personal content without need | Access justified but not reviewed on a cycle | Restrict to named roles; mask or summarise where possible |
| Retention and deletion | A store keeps records indefinitely or outside the agreed rule | Rule applied but deletion not yet evidenced | Apply the agreed period at every store; test deletion |
| Duplicate copies | Traces, exports or analytics hold full content beyond the main store's rule | Copies hold metadata only and follow the rule | Remove content from secondary stores or align their retention |
| Legal and audit reach | Records that may be needed for investigation or litigation cannot be searched or held | Reach exists but the process is untested | Bring the store into audit and hold processes; test a search |
| Memory and generated content | The agent remembers personal or confidential detail across users or sessions without a design decision | Memory is scoped to the user and documented | Scope, disable or set expiry for memory; label generated files |

Each finding names the risk, the rule behind it, the fix and an owner. Disagreement escalates to the accountable
executive through `responsible-ai:ai-risk-acceptance`.

## Practitioner approach

Start with a record map rather than a policy discussion. Take one realistic conversation through the solution and list
every place it leaves a trace: the chat history the user sees, the platform's interaction store, transcripts available
to makers, analytics, tracing in a Foundry or Azure resource, flow run history, a ticket or case note written by an
action, a file saved to a library, and any memory feature. Each of those is a store with its own access and retention,
and the map is usually longer than the team expects.

Then ask who can read each store. User-facing history is usually limited to the user, but maker transcripts, analytics
exports and tracing are often visible to builders and support staff who have no need to read colleagues' questions.
Where the solution handles HR, health, legal or customer matters, broad read access to transcripts is blocking from
tier 2. The fix is usually to restrict the store, switch off full-content capture in secondary stores, or rely on
aggregate analytics.

Compare each store with the organisation's rules. Retention should come from `data-governance:ai-data-retention-rules`
or the records schedule, not from whatever the product does by default. Check that the rule is applied, not merely
agreed, and ask for evidence that deletion actually happens, including in exports and copies. Where Microsoft Purview
or platform settings manage retention for some stores, confirm in the current source records which interaction types
they cover; coverage differs between Copilot, agents built with different tools and pro-code solutions.

Check legal reach. If a complaint, investigation or dispute arose from an AI interaction, could the organisation find
the record, place it on hold and produce it? Stores outside the usual audit and eDiscovery reach, such as a custom
log in an Azure resource, need an explicit process.

Look at memory and generated content separately. Memory that persists personal detail between sessions, or across
users, is a design decision with privacy consequences, and generated files should carry the right labels and land in
locations whose retention already fits.

Finish with proportionate findings. A tier 2 policy agent with platform defaults that match the rule, restricted maker
access and no secondary logs may pass with one advisory finding. Re-review when logging, tracing, memory or channels
change.

## Outputs

- The interaction retention findings in the `ai-risk-assessment`: the record map (store, content, location, readers, retention rule, deletion evidence, legal reach), findings classified blocking or advisory with fix and owner, and the verdict.
- Referrals to `data-governance:ai-data-retention-rules` where a rule is missing, and to the DPO where personal data retention needs a decision.

## Microsoft platform considerations

Microsoft 365 Copilot, agents, Copilot Studio and Foundry store interaction data in different places, with different
retention, audit and eDiscovery coverage, and Microsoft Purview capabilities for AI interactions evolve frequently.
Copilot Studio transcripts, analytics and Dataverse storage, and Foundry or Azure tracing, each need checking in their
own right. Confirm current behaviour in `ms-copilot-privacy`, `ms-copilot-studio-security-governance` and
`ms-foundry-models`, and record which source and date were used.

## Adoption considerations

People change what they type when they learn conversations are kept and read. Agree with the solution owner what users
will be told, through `responsible-ai:ai-transparency`, so trust is not lost when someone discovers transcripts exist.

## Knowledge considerations

Not applicable as a primary concern, because this review covers interaction records rather than grounding content.
Where generated content is saved back into a knowledge source, flag it to the knowledge owner so it does not become
unreviewed grounding.

## Security and privacy considerations

This skill is the security review of interaction records. Lawfulness and proportionality of keeping personal data stay
with `security-privacy:privacy-assessment`; exposure of grounding content stays with `security-privacy:data-exposure-review`.

## Responsible AI considerations

Transcripts can be misused to monitor individuals. Reading transcripts must serve quality, safety or legal purposes
agreed in advance, never performance assessment, and any analysis is reported at aggregate level.

## Evaluation requirements

Blocking fixes need evidence: configuration screenshots or exports for each store, a deletion test showing records
removed after the agreed period, and a test search or hold against an interaction record where legal reach applies.

## Value measures

Track the share of tier 2+ solutions with a complete record map, stores without an applied retention rule, and time to
close blocking retention findings. The security and privacy lead owns these, with the records manager as co-owner.

## Scale notes

### Starter

Keep logging to platform defaults that match the organisation's rule, restrict transcript access to the owner, and
record the map on one page.

### Scale

Add the record map to the release checklist and maintain a standard set of approved retention configurations per
platform so makers start compliant.

### Enterprise

Reconcile interaction stores against the solution inventory each cycle, test legal reach periodically with the legal
team, and federate tier 2 reviews using the same criteria.

## Hand-offs

- To `data-governance:ai-data-retention-rules` where rules are missing or unclear.
- To `security-privacy:privacy-assessment` for personal data retention decisions with the DPO.
- To `security-privacy:ai-incident-readiness` with the record map, which investigators will need.
- To `m365-agents:agent-release-readiness` with the verdict.

## Reviewer gates

This skill is the `security-privacy` gate for interaction retention. It applies as a blocking gate from risk tier 2
and as an advisory check below it. Blocking findings stop release and are not traded against dates; disagreement
escalates to the accountable executive for written risk acceptance.

## Failure modes

- The main store follows the rule but a tracing or analytics copy keeps full transcripts indefinitely.
- Makers can read every colleague's questions to an HR agent because transcript access was left at its default.
- Retention is agreed on paper and never applied, so deletion is assumed rather than evidenced.
- A legal request arrives and the relevant conversations sit in a store nobody can search.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Assume a platform default matches the organisation's retention rule without checking.
- Set a retention period on the organisation's behalf instead of routing to the rule owner and DPO.
- Allow transcripts to be read to assess an individual's performance.
- Trade a blocking finding against a launch date.

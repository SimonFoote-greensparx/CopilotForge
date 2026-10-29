---
name: privacy-assessment
description: Assesses personal data in an AI solution for lawful basis, purpose limitation, transparency, data minimisation, retention of prompts, responses and transcripts, DPIA screening under UK GDPR and ICO guidance, and people-related uses, classifying findings as blocking or advisory. Use when an agent or AI solution processes personal data, when transcripts are kept, or when AI outputs inform decisions about people.
license: CC-BY-4.0
metadata:
  department: security-privacy
  lifecycle: Envision, Assure, Launch, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-copilot, m365-agents, copilot-studio, ai-foundry, purview
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, responsible-ai
  sources: ico-ai-data-protection, ms-copilot-privacy, nist-ai-rmf, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# Privacy assessment

## Purpose

AI solutions process personal data in places teams do not expect: in the knowledge they ground on, in the prompts
people type, in the responses and transcripts kept afterwards, and in the outputs that shape decisions about colleagues
and customers. This reviewer skill screens a solution against UK data protection principles, as explained in ICO
guidance, and classifies each finding as blocking or advisory with a fix. It is a structured practitioner review, not
legal advice: legal questions end with the organisation's Data Protection Officer. Reviews go wrong when "Microsoft
handles privacy" is taken as the answer, when the organisation remains the controller for the purposes it chooses.

## When to use

- An agent or AI solution at risk tier 2 or above processes personal data and reaches its `security-privacy` gate.
- Transcripts, prompts or responses will be stored, analysed or reused.
- AI outputs will inform decisions about employees, candidates, customers or members of the public.
- A new purpose is proposed for data already collected, for example using case notes to ground an agent.
- A DPIA screening is needed early, while design can still change.

## When not to use

- Reviewing who can reach content through the solution - use `security-privacy:data-exposure-review`.
- Reviewing connectors, authentication and data flows to external services - use `security-privacy:connector-review`.
- Fairness, human oversight and prohibited uses as a responsible AI question - use `responsible-ai:fairness-review`, `responsible-ai:human-oversight` and `responsible-ai:prohibited-use-review`.
- Records retention schedules and classification across the estate - use `data-governance:ai-data-retention-rules`.
- Setting the risk tier - use `opportunity-management:risk-classification`.

## Questions to ask first

1. Whose personal data does the solution process - staff, candidates, customers, the public - and does it include special category or criminal offence data?
2. For what purpose, and is that purpose compatible with why the data was originally collected?
3. Which lawful basis applies, and has the DPO confirmed it?
4. What will people be told about the AI's involvement, and when?
5. What is kept - prompts, responses, transcripts, logs - for how long, and who can see it?
6. Will outputs contribute to decisions about individuals, and is a person meaningfully involved?

## Required inputs

- The agent brief or solution design, with purpose, audience, knowledge sources, actions and risk tier.
- A description of personal data processed at each stage: grounding, input, output, storage, onward flows.
- The organisation's privacy notices, records of processing and retention schedule, where they exist.
- Findings from `security-privacy:data-exposure-review` and `security-privacy:connector-review`.

Where the lawful basis or retention position is unknown, record it as a blocking finding from tier 2 and route it to the
DPO. Never state a lawful basis on the organisation's behalf.

## Decision framework

Classify every finding. From risk tier 2 a blocking finding stops release and is not traded against dates; below tier 2
the screening is advisory, but a finding that would be blocking means the tier needs re-checking.

| Principle | Blocking when | Advisory when | Typical fix |
|---|---|---|---|
| Lawful basis | No basis identified or confirmed by the DPO for the AI processing | Basis confirmed but not yet recorded in the record of processing | DPO confirms and records the basis |
| Purpose limitation | Data reused for an incompatible purpose without assessment | Compatible reuse not yet documented | Compatibility assessment, or remove the data |
| Transparency | People are not told AI processes their data or shapes outcomes | Notice exists but is hard to find or vague | Update privacy notices and in-product messages |
| Data minimisation | Grounding or prompts include personal data not needed for the purpose | Minor excess in low-risk fields | Remove sources or fields, add instructions and input guidance |
| Retention | Prompts, responses or transcripts kept with no defined period or owner | Period defined but not yet enforced | Set and enforce retention, assign owner |
| Rights | No route to respond to access, correction or objection requests covering AI data | Route exists but untested | Map AI data into the rights process and test it |
| DPIA screening | Screening indicates likely high risk and no DPIA has been completed | Screening done, DPIA not needed, rationale recorded | Complete a DPIA with the DPO before release |
| People-related decisions | Outputs drive decisions about individuals without meaningful human review | Human review exists but is not documented | Design human review, record it, involve `responsible-ai` |

Each finding names the principle, the risk to people, the fix and an owner. Legal interpretation is the DPO's;
disagreement on risk escalates to the accountable executive for written risk acceptance.

## Practitioner approach

Start by mapping personal data through the solution's life, not just its storage. Draw five boxes: what it grounds on,
what users type, what it outputs, what is kept, and where data goes next. For each, note whose data, which categories
and how much. Teams usually find personal data in places they had not considered, such as names in uploaded case files
or transcripts of conversations about colleagues.

Then test purpose. Write the purpose of the solution in one sentence and compare it with why the data was collected.
Grounding an agent on old HR case notes to answer policy questions is a different purpose from the one those notes
were created for. Where reuse is not clearly compatible, flag it and ask the DPO.

Ask the DPO to confirm the lawful basis. Your role is to describe the processing clearly enough for them to decide, not
to decide yourself. Record their answer and its date.

Look at transparency from the person's point of view. Would an employee, candidate or customer reasonably expect AI to
be used in this way? Check that privacy notices cover the processing and that users of the solution see a clear
statement that they are using AI and how their inputs are handled.

Apply minimisation hard. Remove knowledge sources or fields that are not needed. Give users guidance on what not to type,
and where the route allows it, limit what is captured. The cheapest personal data to protect is the data never processed.

Pin down retention for prompts, responses, transcripts and logs. Find out from the current source records what the
platform keeps and the controls available, then set the organisation's own period and owner. Indefinite retention
"in case it is useful" is blocking from tier 2.

Run DPIA screening using the ICO's criteria for likely high risk, with particular attention to people-related uses,
systematic monitoring, special category data and innovative technology. Where screening points to likely high risk, a
DPIA led by the DPO is a release precondition.

Be proportionate. A tier 2 agent answering policy questions from published documents, with no transcript analysis, may
pass with an advisory note on notices. Record each finding with principle, risk, fix and owner, and close the review
only when blocking fixes are evidenced and the DPO's decisions are recorded.

## Outputs

- The privacy section of the `ai-risk-assessment`: personal data map, purpose and compatibility, lawful basis as confirmed by the DPO, transparency, minimisation, retention, rights handling, DPIA screening result, findings classified as blocking or advisory with fix and owner, and the verdict.
- A DPIA referral to the DPO where screening indicates likely high risk.
- Any written risk acceptance from the accountable executive.

## Microsoft platform considerations

How interaction data, transcripts and logs are stored, where data is processed, and what retention and audit controls
exist depend on the product and configuration, and change over time. Confirm current behaviour in `ms-copilot-privacy`
and the route's documentation, and record what was checked. Platform commitments do not replace the organisation's own
decisions on purpose, basis, notices and retention.

## Adoption considerations

Staff trust AI more when they know what happens to what they type. Clear in-product transparency and simple guidance
on what not to enter reduce both risk and hesitation. Never use transcripts to monitor individual staff usage.

## Knowledge considerations

Knowledge sources containing personal data are the most common minimisation finding. Work with the agent team through
`m365-agents:knowledge-source-readiness` to remove or narrow them before build rather than after review.

## Security and privacy considerations

This skill is the privacy review. Exposure through permissions goes to `security-privacy:data-exposure-review`; data
leaving the tenant through connectors goes to `security-privacy:connector-review`.

## Responsible AI considerations

People-related uses (recruitment, performance, conduct, eligibility) raise fairness and oversight questions beyond data
protection. Refer them to `responsible-ai:ai-impact-assessment` through risk classification, and treat
meaningful human review as a precondition from tier 3.

## Evaluation requirements

Blocking fixes need evidence: updated notices, a retention setting applied, a removed source, a completed DPIA, the
DPO's recorded decision. Advisory findings need an owner and a date.

## Value measures

Track, at portfolio level, the share of AI solutions with a completed privacy screening, the number with defined
retention for prompts and transcripts, and time to close blocking findings. The DPO or privacy lead owns these measures.

## Scale notes

### Starter

Use a short screening with the DPO or external privacy adviser for any agent touching personal data. Prefer agents that
ground on published, non-personal content.

### Scale

Build privacy screening into the CoE intake so DPIA needs are spotted at design, and keep a standard transparency
statement and retention position for common agent patterns.

### Enterprise

Federate screening to trained business-unit privacy champions under DPO oversight, with the DPO leading DPIAs for tier 3
and 4. Link assessments to the record of processing and the solution register.

## Hand-offs

- To the organisation's DPO for lawful basis, DPIA and any legal interpretation.
- To `responsible-ai:ai-impact-assessment` for people-related uses.
- To `m365-agents:agent-release-readiness` with the verdict.
- Back to `m365-agents:agent-use-case-design` with scope and minimisation changes.

## Reviewer gates

This skill is the `security-privacy` gate for privacy. It applies as a blocking gate from risk tier 2 and as an
advisory screening below it. Blocking findings stop release and are not traded against dates; legal questions end with
the DPO, and disagreement on risk escalates to the accountable executive for written risk acceptance.

## Failure modes

- "Microsoft handles privacy" is accepted, and the organisation's own purpose and retention decisions are never made.
- Transcripts are kept indefinitely and later used to monitor individuals.
- Old case files are reused to ground an agent without asking whether the new purpose is compatible.
- DPIA screening happens after build, when the design can no longer change.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- State a lawful basis or give a legal opinion on the organisation's behalf; legal questions end with the DPO.
- Trade a blocking finding against a launch date.
- Use prompts, responses or transcripts to assess or monitor individual staff.
- Pass a solution that keeps conversation data with no defined retention period or owner from tier 2.

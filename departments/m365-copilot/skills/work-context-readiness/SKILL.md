---
name: work-context-readiness
description: Prepares the everyday work context licensed Copilot draws on for a team or role - where files are stored, how sites and libraries are shared, whether meetings are recorded or transcribed, how mail and chat are used - and fixes the gaps that make answers thin or expose content. Use when a group is about to receive Copilot, when answers miss obvious content, or when a team's sites look overshared.
license: CC-BY-4.0
metadata:
  department: m365-copilot
  lifecycle: Mobilise, Enable, Improve
  maturity: adopter, scaler, ai-enterprise
  risk-tiers: 0, 1, 2
  platforms: m365-copilot, sharepoint, purview
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-privacy, ms-copilot-overview, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# Work context readiness

## Purpose

Licensed Copilot is only as good as the work context a person can reach: their mail, meetings, chats and the files in
OneDrive, Teams and SharePoint they have access to. This skill prepares that context for a specific team or role before
they start, so the answers they get are complete and the content they can find is content they should see. It covers
where work is stored, how team sites and libraries are shared, how meetings are captured, and how the team uses mail and
chat. It goes wrong when work context is treated as a tenant-wide IT matter, so nobody looks at the team's own sites
until a user finds a salary spreadsheet through a casual question.

## When to use

- A team or role is in the next rollout wave and its content has not been looked at.
- Users say Copilot misses obvious content, or answers from out-of-date versions.
- A team's sites, libraries or Teams channels look shared far more widely than the team.
- A team's scenarios depend on meetings, and recording or transcription practice is unclear.

## When not to use

- Tenant-wide prerequisites, oversharing controls and admin settings - use `m365-copilot:copilot-technical-readiness`.
- Assessing a curated knowledge source an agent will ground on - use `m365-agents:knowledge-source-readiness`.
- Estate-wide knowledge clean-up and information architecture - use `knowledge-management:knowledge-cleanup` or `knowledge-management:sharepoint-knowledge-design`.
- A formal reviewer judgement on exposure of sensitive content - use `security-privacy:data-exposure-review`.
- Organisation-level readiness across sponsorship, guidance and support - use `copilot-adoption:adoption-readiness`.

## Questions to ask first

1. Which team or role is in scope, and which priority scenarios will they use first?
2. Where does the team's work actually live: OneDrive, Teams, SharePoint, local drives, other systems or email attachments?
3. Who owns each of the team's main sites and libraries, and who can open them today?
4. How does the team capture meetings, and what does the organisation's policy and local consultation allow?
5. Which content in the team's area is sensitive, and is it labelled and stored where it should be?

## Required inputs

- The team's priority scenarios from `m365-copilot:copilot-role-scenarios` or the `scenario-catalogue`.
- A list of the team's main sites, libraries, Teams and shared mailboxes with owners, from the team and IT.
- Sharing and permissions reports for those locations, from the SharePoint or Microsoft 365 admin.
- The organisation's policies on meeting recording and transcription, retention and data classification.

Where permissions information is not available, the location is rated "unknown" and treated as not ready for a
sensitive team. Never assume a site is private because its name suggests it.

## Decision framework

Rate each area for the team: Ready, Ready with conditions or Not ready.

| Area | Ready looks like | Common fix |
|---|---|---|
| Storage | Working files are in OneDrive, Teams or SharePoint, not local drives or attachments | Move active work into the right location; stop emailing attachments |
| Sharing | The team's sites, libraries and channels are shared with the right groups, not everyone | Owner removes broad access, breaks inherited oversharing, uses groups |
| Sensitive content | Sensitive files are labelled and stored in restricted locations | Relocate, label and restrict; remove copies |
| Currency | Superseded versions are archived or clearly marked | Archive old drafts; mark final versions |
| Meetings | Recording and transcription practice matches policy and the team's scenarios | Agree when meetings are transcribed and tell attendees |
| Mail and chat | Decisions and actions are written down where the team can find them | Agree simple norms, such as clear subject lines and channel use |
| Ownership | Every main location has an active owner | Assign owners for orphaned sites |

Sharing or sensitive content rated Not ready blocks the team's start. Other areas may start with conditions, because
they limit usefulness rather than create exposure.

## Practitioner approach

Begin with the team's scenarios, not with a scan of the whole tenant. Ask what content each scenario needs, then follow
it to where it lives. A sales team whose proposals sit in email attachments will get thin answers however good their
prompts are, and the fix is a change in working habit, not a technical project.

Walk the team's main locations with their owners. For each, check who can open it, how that access was granted, and
whether that is what the owner intends. Pay special attention to sites shared with everyone or with very large groups,
inherited permissions that nobody remembers setting, and old project sites that still hold sensitive material. Use the
sharing and permissions reports IT can provide; where the organisation has tenant-wide tooling for this, use it rather
than inspecting by hand, after checking what is available in the source records.

Make the fixes small and owned. Owners can usually correct sharing on their own sites in an afternoon once they can see
it. Larger remediation, such as restructuring a sprawling site, goes to `knowledge-management:sharepoint-knowledge-design`
and is recorded as a condition rather than a blocker unless it involves exposure.

Agree meeting practice with the team in line with policy. Scenarios that summarise meetings need recordings or
transcripts; but transcribing every meeting has implications for consent, retention and trust. Agree which meeting
types are transcribed, how attendees are told, and what the policy and any local consultation allow. Route open
questions to the data protection lead.

Finish with a few working norms that help both people and Copilot: active work stored in shared locations, final
versions clearly marked, decisions written down in the channel or thread where the team will look. Keep the list short
and agreed by the team leader.

Record the result per team with owners and dates, and pass it to the rollout owner as the work context gate for the
wave. Recheck after the team has used Copilot for a few weeks, because real questions reveal gaps a walkthrough misses.

## Outputs

- A work context readiness record per team or role: area, verdict, evidence, fixes, owners and dates.
- A short list of agreed working norms for the team.
- Remediation items passed to site owners, IT or knowledge management, and the gate verdict for the `copilot-rollout-plan`.

## Microsoft platform considerations

Copilot grounds on content according to each user's existing permissions, as described in `ms-copilot-privacy`, so
oversharing in Microsoft 365 becomes easier to discover. Sharing reports, sensitivity labels, restricted locations and
transcription settings sit across SharePoint, Teams and Microsoft Purview; which controls are available and licensed
changes often, so confirm them in the source records and with IT rather than from memory.

## Adoption considerations

Present the work as making Copilot useful for the team, not as an audit. Team leaders and Champions can lead the
walkthrough; owners who see the benefit fix their sites quickly. Feed the agreed norms into the team's onboarding.

## Knowledge considerations

Shared team content is often the knowledge people need most. Where the walkthrough finds content that many teams rely
on, such as policies or procedures, route it to the `knowledge-management` department for proper ownership and review.

## Security and privacy considerations

Oversharing and misplaced sensitive content are the main exposure risks; they block the team's start until fixed or
accepted in writing. Meeting transcription raises consent and retention questions that go to the data protection lead
and, where relevant, HR and employee representatives.

## Responsible AI considerations

Not applicable in depth, because the skill prepares content rather than shaping decisions; where meeting transcripts
could be used to assess individuals, record that this is outside approved use.

## Evaluation requirements

After fixes, test with two team members using their real scenarios: confirm Copilot finds the content it should, and
cannot surface content from locations that were restricted. Record results with the readiness record.

## Value measures

Track, per wave, the share of teams rated Ready, the number of overshared locations remediated, and team-level feedback
on answer completeness. The rollout owner owns these measures; site owners own their remediation items.

## Scale notes

### Starter

A one-hour walkthrough with the team leader and site owners, a short fix list and an agreed note on meetings is enough
for a pilot team.

### Scale

A standard walkthrough per wave run by Champions or site owners with IT support, and a remediation backlog tracked
alongside the rollout plan.

### Enterprise

Tenant-wide reporting identifies high-risk locations centrally, while business units run walkthroughs for their teams
against a common standard.

## Hand-offs

- To `m365-copilot:m365-copilot-rollout` with the work context gate verdict.
- To `security-privacy:data-exposure-review` when sensitive content exposure is found.
- To `knowledge-management:sharepoint-knowledge-design` for larger restructuring.
- To `m365-copilot:copilot-role-scenarios` when scenarios need adjusting to the content that exists.

## Reviewer gates

From risk tier 1, teams handling sensitive content have their sharing and sensitive-content findings reviewed by
`security-privacy`, classified as blocking or advisory. Blocking findings stop the team's start until fixed or formally
accepted by the accountable executive.

## Failure modes

- Readiness is checked only at tenant level, and a team's own overshared site surfaces sensitive content.
- Work stays in local drives and attachments, so answers are thin and users conclude Copilot is not useful.
- Every meeting is transcribed without agreement, damaging trust and creating retention issues.
- Fixes are listed but have no owner, and nothing changes before the wave starts.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Let a team start while its main locations have unknown or overshared permissions and nobody has accepted the risk.
- Assume a site is private from its name or its owner's recollection.
- Introduce meeting transcription without checking policy and telling attendees.
- Use work context data to assess individual staff.

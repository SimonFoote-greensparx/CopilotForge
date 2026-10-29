---
name: copilot-technical-readiness
description: Checks the technical readiness of a tenant and a target audience for Microsoft Copilot - identity and licence assignment, Microsoft 365 apps and update channels, tenant-wide oversharing controls, sensitivity labels, admin settings for web content and agents, audit and retention - and records owned fixes. Use when IT is asked to confirm prerequisites before a rollout, when a pilot hits technical faults, or when settings were never reviewed.
license: CC-BY-4.0
metadata:
  department: m365-copilot
  lifecycle: Discover, Mobilise, Assure
  maturity: explorer, adopter, scaler, ai-enterprise
  risk-tiers: 0, 1, 2
  platforms: copilot-chat, m365-copilot, entra, sharepoint, purview
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-overview, ms-copilot-privacy, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# Copilot technical readiness

## Purpose

This skill gives IT and the Copilot specialist a clear, evidenced answer to one question: is the technical estate ready
for this audience to use Microsoft Copilot safely and reliably, and if not, what must change and who owns it? It covers
identity and licence assignment, the Microsoft 365 apps people will use, tenant-wide controls over oversharing and
sensitive content, the admin settings that govern Copilot behaviour, and the audit and retention position. It usually
goes wrong in two ways: readiness is declared because licences were assigned, or settings are left at whatever default
applied on the day the tenant was enabled and nobody decided them.

## When to use

- A rollout or pilot is being planned and the sponsor needs IT to confirm the technical prerequisites for a named audience.
- A pilot group reports that Copilot is missing from apps, returns nothing from their files or behaves differently from colleagues.
- Admin settings for web content, agents, plugins or Copilot Chat have never been formally reviewed and decided.
- A new business unit, region or device estate is joining an existing rollout.
- Microsoft has changed a Copilot setting or control and the organisation needs to decide its position.

## When not to use

- Assessing overall organisational readiness across sponsorship, guidance, support and communications - use `copilot-adoption:adoption-readiness`.
- Preparing the mail, files, meetings and site permissions a specific audience works with day to day - use `m365-copilot:work-context-readiness`.
- A formal reviewer judgement on data exposure for an agent or solution - use `security-privacy:data-exposure-review`.
- Licence entitlement, purchasing or capacity questions - use `platform-governance:ai-licensing-and-capacity`, which ends with the Microsoft licensing guide or a licensing partner.
- Ongoing admin monitoring of the AI estate after rollout - use `platform-governance:ai-admin-monitoring`.

## Questions to ask first

1. Which audience is in scope, on which devices and app versions, and is anyone outside the standard managed estate?
2. Who in IT owns identity, Microsoft 365 apps, SharePoint and Purview, and have they agreed to own the remediation items?
3. Do we know where content is shared with everyone or with large groups, and has any tenant-wide control been applied to it?
4. Which Copilot admin settings (web content, agents, plugins, Copilot Chat placement) have been consciously decided, and by whom?
5. What does the organisation's retention, audit and eDiscovery policy say about Copilot interactions, and has records management agreed it?

## Required inputs

- The target audience by role and location, with the device and app estate they use.
- Licence assignment method (groups or direct) and the current assignment state, from the organisation's own admin data.
- Any existing oversharing, permissions or sensitivity labelling assessment.
- The current state of Copilot-related admin settings, exported or captured by the admin who owns them.
- Retention, audit and acceptable-use policies that apply to AI interactions.

Where an input is missing, record the check as "unknown" with an owner and a date. An unknown in a critical area is a
readiness gap, not a pass. Never infer that a setting, licence or feature is in place because it usually is.

## Decision framework

Rate each area Ready, Ready with conditions or Not ready. The overall verdict is the weakest critical area.

| Area | Ready looks like | Critical? |
|---|---|---|
| Identity and access | Users are in the directory with the right attributes; licences are assigned through managed groups; conditional access applies to Copilot as to other Microsoft 365 workloads | Yes |
| Apps and clients | The audience's apps are on a supported update channel and version, and Teams, Outlook and the browser experience have been tested on their real devices | Yes |
| Oversharing controls | Broadly shared high-risk locations are known and remediated or restricted before launch | Yes |
| Sensitive content protection | Sensitivity labels and data loss prevention behave as intended with Copilot for the audience's most sensitive content | Yes from risk tier 1 |
| Admin settings | Each Copilot setting has a decided position, an owner and a recorded reason | Yes |
| Audit, retention and eDiscovery | Records management has agreed how interactions are retained and searched | Yes before broad rollout |
| Support readiness | The service desk has fault scripts and knows how to tell a technical fault from a usage question | No for a pilot |

A Not ready in any critical area means the audience does not start. Ready with conditions requires a dated fix with a
named owner, accepted by the rollout owner in writing.

## Practitioner approach

Start from the audience, not the tenant. A readiness check for "everyone" hides the fact that the finance team runs an
old app channel and the field engineers share devices. List the audience segments and the devices, apps and locations
each uses, then test on real devices with real accounts before trusting any configuration report.

Work through identity and licensing first because every other test depends on it. Confirm the assignment method and
that it is driven by groups the organisation controls, so waves can be added and reversed cleanly. Check that
conditional access, multifactor authentication and device policies apply to Copilot experiences consistently with the
rest of Microsoft 365; an exception created for a pilot tends to outlive it.

Oversharing is the area that most often turns a technical rollout into a data incident. Copilot respects the
permissions users already have, so content shared with everyone becomes easy to find. Ask SharePoint and Purview owners
for the current picture of broadly shared sites and libraries, which are high risk, and what has been done about them.
Use the tenant-wide controls the organisation is entitled to and has approved; confirm what is available and licensed
from the source records and the licensing route rather than assuming. Where nothing is known, the finding is "unknown",
and the rollout owner decides with security whether a restricted first audience is acceptable.

Review the admin settings as decisions, not defaults. For each setting that affects Copilot, write the position, the
reason and the owner: whether web content is allowed, which agents and extensions users can find and install, how
Copilot Chat is presented, and who can create or share agents. Microsoft adds and renames settings often, so check the
current admin documentation and record the date you checked.

Finish with retention and audit. Confirm with records management and the data protection lead how Copilot interactions
are retained, audited and found in investigations. If that conversation has not happened, it is a gap for broad
rollout, even when a small pilot may proceed.

Record every finding with the area, evidence, verdict, fix, owner and date, and hand the result to the rollout owner.
Repeat the check for each new audience segment rather than relying on the first one.

## Outputs

- A technical readiness record per audience segment: area, evidence, verdict, remediation, owner and date.
- A settings decision log listing each Copilot-related admin setting, its decided position, reason and owner.
- A short list of conditions that must close before each wave, carried into the `copilot-rollout-plan`.

## Microsoft platform considerations

Readiness spans Microsoft Entra for identity, the Microsoft 365 apps and update channels, SharePoint and OneDrive for
permissions, Microsoft Purview for labels, data loss prevention, audit and retention, and the Microsoft 365 admin
centre for Copilot settings. How Copilot uses organisational data and respects permissions is described in
`ms-copilot-privacy`; product naming and scope are in `ms-copilot-overview`. Prerequisites, controls, settings and their
licensing change frequently, so check the current source records and admin documentation, and never assert availability
from memory.

## Adoption considerations

Technical faults in the first week destroy trust faster than any communication can rebuild it. Share the readiness
verdict with the adoption lead so `copilot-adoption:adoption-readiness` and the launch plan reflect real constraints,
and give the service desk a short guide to distinguish faults from usage questions.

## Knowledge considerations

Not applicable to tenant configuration as such; the content in people's work context is prepared through
`m365-copilot:work-context-readiness`, and curated knowledge through the `knowledge-management` department.

## Security and privacy considerations

Oversharing, sensitive content protection and the retention of interactions are the core risks. Findings that touch
high-risk content go to the `security-privacy` department, and any proposal to start before oversharing is understood
needs written acceptance from the accountable owner. Retention and investigation questions route to the data protection
lead and legal adviser.

## Responsible AI considerations

Not applicable at the level of tenant readiness; responsible use of individual outputs is addressed through approved-use
guidance and `m365-copilot:prompting-practice`.

## Evaluation requirements

Test each audience segment on real devices with test accounts that mirror real permissions: confirm Copilot appears in
the expected apps, grounds on content the user can open, and does not surface content from a restricted location.
Record the test date and results with the readiness record.

## Value measures

Measure readiness as the share of in-scope audience segments rated Ready, the number of open critical findings and the
time to close them, owned by the IT lead for the rollout. Technical fault tickets per wave, at audience level, show
whether readiness held in practice.

## Scale notes

### Starter

One IT generalist and the Copilot specialist work through the table for a single pilot audience in a few days, often
with a partner. Keep the settings log even if it is a single page.

### Scale

Run the check per wave with named owners in each IT tower, a maintained settings decision log and a standing oversharing
remediation backlog that the rollout plan tracks.

### Enterprise

Define a standard readiness baseline centrally, with regional or business-unit IT teams evidencing it for their
segments. Treat settings changes as change-controlled decisions and review them when Microsoft announces changes.

## Hand-offs

- To `m365-copilot:m365-copilot-rollout` or `m365-copilot:copilot-chat-rollout` with the verdict and conditions per audience.
- To `m365-copilot:work-context-readiness` for the audience's own content and permissions.
- To `security-privacy:data-exposure-review` where high-risk content exposure is suspected.
- To `platform-governance:ai-admin-monitoring` for ongoing monitoring once live.

## Reviewer gates

From risk tier 1, oversharing and sensitive content findings are reviewed by `security-privacy`, which classifies each
as blocking or advisory. A blocking finding stops the affected audience from starting until it is fixed or formally
accepted by the accountable executive.

## Failure modes

- Readiness is declared from licence assignment alone, and users find Copilot missing from the apps they actually use.
- A broadly shared site with sensitive content is discovered by a pilot user through a casual question.
- Admin settings stay at their defaults, so agents and web content are available in ways nobody decided.
- Retention is not agreed, and an investigation later cannot find, or unexpectedly finds, Copilot interactions.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Declare an audience ready because licences are assigned.
- Assert a prerequisite, control, setting or licence entitlement from memory.
- Leave a Copilot admin setting at its default without a recorded decision and owner.
- Start a broad audience while oversharing on its main content is unknown and nobody has accepted that risk in writing.

---
name: knowledge-readiness-assessment
description: Assesses how ready the organisation's whole knowledge estate is for Copilot and agents across ownership, currency, authority, findability, permissions, classification and lifecycle, rates each domain on evidence and sets a prioritised remediation plan. Use when a Copilot rollout or agent programme is being planned, when a sponsor asks whether content is fit for AI, or when answers across many agents keep failing for knowledge reasons.
license: CC-BY-4.0
metadata:
  department: knowledge-management
  lifecycle: Discover, Envision, Mobilise
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: m365-copilot, m365-agents, copilot-studio, sharepoint, purview
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-privacy, ms-copilot-overview, ms-copilot-adoption-hub, ms-agent-builder
  status: draft
  authors: Simon Foote
---

# Knowledge readiness assessment

## Purpose

Copilot and agents find, summarise and repeat whatever the organisation already holds, so the condition of the
knowledge estate sets a ceiling on the value AI can deliver. This skill gives a sponsor an honest, evidence-based view of
that condition across the knowledge domains that matter, rates each one, and turns the gaps into a prioritised plan. It
usually goes wrong in one of two ways: the assessment becomes a vague survey of opinions, or it becomes an attempt to
fix everything before anyone is allowed to use AI.

## When to use

- A Microsoft 365 Copilot rollout or an agent programme is being planned and nobody knows whether the content is fit for it.
- A sponsor asks "is our knowledge ready for AI?" and needs a defensible answer, not a feeling.
- Several agents or Copilot users report wrong, stale or contradictory answers and the cause looks systemic.
- The CoE needs a baseline before funding knowledge work, and a way to show improvement later.

## When not to use

- Checking the specific sources one agent will ground on - use `m365-agents:knowledge-source-readiness`.
- Overall readiness to adopt Copilot, including sponsorship, licences and support - use `copilot-adoption:adoption-readiness`.
- Preparing individuals' mail, files and meetings as Copilot work context - use `m365-copilot:work-context-readiness`.
- Listing every source with its owner and condition in detail - use `knowledge-management:knowledge-inventory`.
- The formal security review of oversharing and exposure - use `security-privacy:data-exposure-review`.

## Questions to ask first

1. Which AI uses is this assessment for - Copilot across the workforce, a set of planned agents, or both - and which knowledge domains do they depend on?
2. Where does the organisation's authoritative knowledge live today, and is there any existing inventory or site list?
3. Who can speak for each domain's content, and who administers SharePoint, Teams and labelling?
4. What evidence is available - permission and sharing reports, version history, search logs, service desk themes - and what can only be gathered by sampling?
5. What decision will the result inform: a go or no-go, a funding request, or the sequence of rollout waves?

## Required inputs

- The scope: the AI uses in view and the knowledge domains they depend on (for example HR policy, IT support, sales enablement, operating procedures).
- Access to administrators or reports that show sites, libraries, sharing and permissions at summary level.
- A short list of representative questions per domain, from the business or from `copilot-adoption:scenario-discovery`.
- The organisation's classification scheme and any sensitivity labels in use, or confirmation that none exist.
- An existing knowledge inventory if there is one, from `knowledge-management:knowledge-inventory`.

Where an input is missing, record the dimension as "not assessed" with the reason, never as a pass. A domain with no
identifiable owner is rated at the lowest level for ownership whatever its content looks like.

## Decision framework

Rate each knowledge domain on seven dimensions from 1 (not ready) to 4 (ready), using evidence, not self-assessment.

| Dimension | 1 - not ready | 4 - ready |
|---|---|---|
| Ownership | Nobody accountable; owners have left | Named owner per domain who accepts accountability |
| Currency | No review dates; superseded versions sit beside current ones | Reviewed within an agreed cycle; old versions archived |
| Authority | Several competing versions of key answers | One authoritative source per topic, clearly marked |
| Findability and structure | Content scattered across chats, personal drives and attachments | Content in governed sites and libraries with sensible structure and metadata |
| Permissions | Broad or inherited access wider than sensitivity warrants | Access matches the intended audience |
| Classification | Sensitive content unlabelled or unknown | Sensitivity and audience recorded and applied |
| Lifecycle | No archive or disposal practice | Content moves through review, archive and disposal |

Turn ratings into a verdict per domain: **ready** (no dimension below 3), **ready with conditions** (no 1s, every
condition owned and dated), **not ready** (a 1 on ownership or permissions, or two or more 1s elsewhere). The estate
verdict is never better than the verdicts of the domains the planned AI uses depend on.

## Practitioner approach

Start from the AI uses, not the estate. List the scenarios or agents in view and the knowledge domains each depends on.
That keeps the assessment bounded: an organisation with thousands of sites does not need to assess them all to decide
whether the HR policy agent and the first Copilot wave can proceed.

For each domain, find the owner first and run a short structured conversation: where the authoritative content lives,
how it is maintained, how they would know if it were wrong, and who can see it. Then verify rather than trust. Sort the
main libraries by modified date, look for drafts and duplicates, and answer five representative questions by hand. If
you find two different answers to the same question, authority scores 1, however confident the owner was.

Use administrative reports for permissions at scale and sampling for depth. Summary reports show where broad access
groups, anyone links and inherited permissions cluster; a sample of libraries shows whether the pattern holds. Because
Copilot grounding is permission-trimmed, oversharing that was harmless while content was obscure becomes visible once
people can ask for it in plain language. Record the evidence for every rating so the assessment can be repeated and
challenged.

Rate classification with the data governance and security teams. If no scheme exists, record that as a finding and use
the owners' plain-language view of sensitivity in the meantime; do not invent a scheme inside this assessment.

Write the report for a sponsor. Lead with the verdict for each domain that matters to the planned AI uses, then the three
to five systemic findings that explain most of the low ratings, then the remediation plan. A good plan separates what
must be fixed before a rollout wave (oversharing of sensitive content, missing owners for agent sources), what can run
alongside adoption (structure, metadata, review cycles) and what is longer-term lifecycle work. Size each action and
name the skill that owns it.

Be explicit about what the assessment could not see: personal drives, chat history, third-party systems or connector
sources left out of scope. A readiness verdict that hides its blind spots is worse than none. Agree a date to repeat the
assessment so improvement is measured against the same dimensions and evidence.

## Outputs

- A knowledge readiness report on the `knowledge-readiness-report` template: scope, domains, ratings with evidence, verdicts, systemic findings, blind spots and the remediation plan.
- A prioritised remediation backlog, each action with an owning role, a date and the skill that will carry it out.
- Referrals for oversharing and personal data findings to the security and privacy reviewers.

## Microsoft platform considerations

Copilot and agents built on Microsoft 365 ground on content users can already open, so permissions, sharing links and
sensitivity labels in SharePoint, OneDrive and Teams are the controls that matter most. SharePoint administrators may
have reports and governance features that summarise sharing and access at scale; what is available depends on
configuration and licensing, so confirm it in the source records (`ms-copilot-privacy`) and the licensing guide rather
than assuming. Content reached through connectors carries the permission model of its source system and must be
assessed on its own terms.

## Adoption considerations

The verdicts shape rollout waves. Domains rated ready can go first and create early wins; not-ready domains are kept out
of early agent scopes rather than delaying all adoption. Present findings to owners as support, not blame.

## Knowledge considerations

This skill is the department's front door. Its findings feed `knowledge-management:knowledge-inventory`,
`knowledge-management:knowledge-cleanup`, `knowledge-management:knowledge-owner-model` and
`knowledge-management:sharepoint-knowledge-design`, and its dimensions should be reused at every repeat assessment.

## Security and privacy considerations

Oversharing of sensitive content is the finding most likely to stop a rollout. Record it precisely (where, how wide,
what sensitivity) and pass it to `security-privacy:data-exposure-review`. Personal data found in shared knowledge goes
to `security-privacy:privacy-assessment`.

## Responsible AI considerations

Content that encodes outdated or discriminatory practice will be repeated by AI as current guidance. Ask owners whether
any domain holds practice the organisation no longer stands behind, and record it as a clean-up finding.

## Evaluation requirements

Every rating must cite its evidence: a report, a sample or a hand-checked question. Keep the representative questions
and their correct answers so the same set can test agents later through `m365-agents:agent-testing`.

## Value measures

Baseline the share of in-scope domains rated ready, the share with a named owner and the share of sampled questions with
one authoritative answer. The Knowledge Manager owns these and reports them at domain level at each repeat assessment,
never by individual author.

## Scale notes

### Starter

Assess the two or three domains tied to the first AI uses in a few working sessions with their owners. A short report
on the template is enough.

### Scale

Assess every domain in the current rollout wave, reuse the same dimensions each wave, and track ratings in the
knowledge inventory.

### Enterprise

Federate assessment to business-unit knowledge leads using the shared dimensions and evidence rules, with the central
knowledge team moderating ratings. Repeat at least annually and before each major expansion of AI capability.

## Hand-offs

- To `knowledge-management:knowledge-inventory` to record sources, owners and condition in detail.
- To `knowledge-management:knowledge-cleanup` and `knowledge-management:knowledge-owner-model` for the main remediation actions.
- To `security-privacy:data-exposure-review` for oversharing, and to `copilot-adoption:launch-plan` to sequence waves around the verdicts.

## Reviewer gates

From risk tier 2, `security-privacy` reviews the permissions and classification findings and any proposal to proceed
with a domain rated not ready; its blocking findings must be resolved first. Below tier 2 the Knowledge Manager signs
the report with the sponsor.

## Failure modes

- Owners rate their own content and the report measures confidence rather than condition.
- The assessment tries to cover the entire estate, takes months, and is out of date on delivery.
- Oversharing is noted as a general concern rather than located, so nothing is fixed before rollout.
- Blind spots such as personal drives and connector sources are omitted, and the verdict overstates readiness.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Rate a dimension as passed when the evidence could not be gathered.
- Hold back all AI adoption until the whole estate is perfect.
- Rely on agent instructions or user training to compensate for overshared content.
- Assert which reporting or governance features the organisation has without checking configuration and licensing.

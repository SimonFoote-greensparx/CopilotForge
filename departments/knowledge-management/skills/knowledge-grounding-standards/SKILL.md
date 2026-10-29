---
name: knowledge-grounding-standards
description: Defines the organisation-wide standard that knowledge must meet before any agent may ground on it - entry criteria scaled by risk tier for ownership, quality, classification, access, review and authoritative status - plus the approved-source designation and how it is withdrawn. Use when makers point agents at any content they like, when each agent team invents its own bar, or when governance needs one grounding policy.
license: CC-BY-4.0
metadata:
  department: knowledge-management
  lifecycle: Mobilise, Enable, Assure
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, copilot-cowork, ai-foundry, sharepoint, purview
  edition-support: scale, enterprise
  reviewers: security-privacy, evaluation-quality
  sources: ms-agent-builder, ms-declarative-agents, ms-copilot-studio-guidance, ms-copilot-privacy, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Knowledge grounding standards

## Purpose

Without a shared standard, every maker decides for themselves whether content is good enough to ground an agent on, and
the answer is usually "it is where the answers are". This skill writes the organisation's grounding standard: the
minimum criteria a knowledge source must meet before agents may use it, scaled by risk tier, and a designation that
marks sources as approved so makers can choose quickly and safely. It goes wrong when the standard is so strict that
makers route around it, or so loose that it approves whole sites because someone filled in a form.

## When to use

- Makers are pointing agents at any site, library or website they can reach, with no common bar.
- Different agent teams apply different, undocumented tests to the same sources.
- Governance or the CoE needs a single grounding policy to include in the agent release path.
- An agent incident traced to poor knowledge has exposed the absence of entry criteria.

## When not to use

- Applying the standard to the specific sources one agent will use - use `m365-agents:knowledge-source-readiness`.
- Configuring what a particular agent grounds on - use `m365-agents:agent-grounding`.
- Defining general quality dimensions and running quality checks - use `knowledge-management:content-quality`.
- Architectural patterns for grounding on organisational data - use `ai-architecture:grounding-patterns`.
- Retrieval, indexing and chunking design for custom solutions - use `ai-foundry:retrieval-design`.

## Questions to ask first

1. Which agent routes and platforms will the standard cover - agents built in Agent Builder or Copilot Studio, Cowork tasks, Foundry solutions?
2. What risk tiers are in use, and what do they already require at release?
3. Which knowledge disciplines already exist - ownership, classification, review cycles, quality checks - that the standard can reference rather than repeat?
4. Who will grant and withdraw the approved-source designation, and how quickly must they respond to makers?
5. Which kinds of source are in scope - internal libraries, uploaded files, connector content, public websites?

## Required inputs

- The organisation's risk tiers and release policy, from `opportunity-management:risk-classification` and the governance model.
- The ownership model, classification scheme, review cycle standard and content quality standard, if they exist.
- The list of agent routes the organisation has approved.
- Examples of recent agent knowledge problems, to test the draft standard against.

If a referenced discipline does not yet exist (for example no review cycle standard), the grounding standard states an
interim minimum and names the skill that will replace it. Never approve sources against criteria that cannot be
checked.

## Decision framework

Entry criteria accumulate by risk tier. A source used by several agents must meet the criteria of the highest tier.

| Criterion | Tier 1 | Tier 2 | Tiers 3 and 4 |
|---|---|---|---|
| Accepted content owner who knows agents use the source | Required | Required, with deputy | Required, with deputy and domain owner sign-off |
| Registered in the knowledge register | Required | Required | Required |
| Knowledge status authoritative or reference | Required | Authoritative only, or reference clearly separated | Authoritative only |
| Intended audience matches actual access | Required | Required, evidenced | Required, evidenced and re-checked at each review |
| Sensitivity classified | Recorded | Labelled | Labelled, with security-privacy review |
| Review cycle in date | Required | Required, linked to agent review | Required, with event triggers |
| Content quality rating | Not poor | Good or fair with conditions | Good |
| Public web sources | Named sites, owner decided | Named sites, justified and recorded | By exception, reviewed |
| Uploaded file copies | Named refresher | Named refresher and review date | Avoid; prefer governed locations |

A source meeting the criteria for a tier is designated **approved to tier N**, recorded in the register with an expiry
date tied to its review cycle. Designation lapses automatically when the review becomes overdue or an owner leaves.

## Practitioner approach

Write the standard as a short policy with the table above at its heart, adapted to the organisation's tiers and
disciplines. Reference the skills that do the underlying work rather than repeating them: ownership comes from
`knowledge-management:knowledge-owner-model`, classification from `knowledge-management:knowledge-classification`,
quality from `knowledge-management:content-quality`. The standard says what must be true; those skills say how.

Scale it by risk deliberately. Tier 1 agents serving a small team with low-stakes answers need owned, registered,
in-date content with sensible access; asking for more makes the standard a blocker and pushes makers to personal agents
with no oversight. From tier 2, evidence is needed rather than assertion, and the highest tiers need authoritative-only
content with security review. Test the draft against recent incidents: would it have prevented them, and would it have
blocked agents that were fine?

Create the approved-source designation. The biggest practical benefit of a grounding standard is a list of sources that
already meet it, so makers can build on approved content without a fresh review each time. Record the designation in
the knowledge register, show it to makers wherever they choose sources, and make it expire with the review cycle so it
cannot quietly outlive the content's condition.

Define how designation is granted and withdrawn. Granting should be fast and done by the content owner with the
knowledge team checking evidence for tier 2 and above. Withdrawal is automatic on overdue review or owner departure,
and immediate when an incident shows the content is wrong or overshared. When a source loses its designation, owners of
dependent agents are told and must either restore it or remove the source.

Cover the awkward source types explicitly. Public websites need a recorded decision about which sites and why, and
users must be able to tell web-derived answers from internal ones. Uploaded files are copies that do not update, so
they need a named person to refresh them. Connector content carries its source system's permissions and quality, which
must be assessed at source.

Finally, embed the standard in the agent path. Agent briefs cite the designation of each source, release readiness
checks it, and agent reviews re-check it. A standard that is not checked at release is advice.

## Outputs

- A knowledge grounding standard: scope, entry criteria by risk tier, source-type rules, designation, expiry and withdrawal.
- Approved-source designations recorded in the `knowledge-asset-register`, with tier and expiry.
- Changes to the `agent-brief` and release checks so each source's designation is cited and verified.

## Microsoft platform considerations

Agent routes differ in which knowledge sources they support, how they respect permissions and labels, whether they
index or retrieve live, and how quickly changes appear. The standard should be written in route-neutral terms, with a
short annex per route confirmed against the current source records (`ms-agent-builder`, `ms-declarative-agents`,
`ms-copilot-studio-guidance`). Never encode a remembered limit or behaviour into the standard itself.

## Adoption considerations

Makers adopt a standard that saves them work. Lead with the approved-source list, keep tier 1 light, and publish
examples of good grounding choices. A standard experienced only as a gate breeds workarounds.

## Knowledge considerations

This skill turns the department's disciplines into one enforceable bar. Keep criteria definitions identical to those in
the inventory, classification, quality and review cycle skills so the same evidence serves all of them.

## Security and privacy considerations

Access matching audience and classification are the criteria that prevent exposure. From tier 2 they need evidence, and
the highest sensitivity levels need `security-privacy:data-exposure-review` before designation.

## Responsible AI considerations

For agents that inform decisions about people, money or safety, authoritative-only content and event-triggered reviews
are required, because a confident answer from stale guidance is a harm. Content reflecting withdrawn practice must never
be designated.

## Evaluation requirements

Designation evidence must be checkable by someone other than the owner. Agents grounded on approved sources still need
their own testing through `m365-agents:agent-testing`; designation is necessary, not sufficient.

## Value measures

Track the share of agent sources holding an in-date designation, the time to grant a designation, and wrong-answer
incidents traced to knowledge on approved versus unapproved sources. The Knowledge Manager owns these, reported by tier
and domain.

## Scale notes

### Starter

Starter organisations rarely need a formal standard; apply `m365-agents:knowledge-source-readiness` per agent and adopt
the tier 1 criteria as a checklist.

### Scale

Publish the standard, designate the most used sources, and check designation at agent release.

### Enterprise

Run designation as a service with business-unit knowledge leads granting tier 1 and 2, the central team granting higher
tiers, and designation status visible in every maker tool and register.

## Hand-offs

- To `m365-agents:knowledge-source-readiness` to apply the standard to each agent's sources.
- To `m365-agents:agent-release-readiness` and `platform-governance:ai-release-policy` to check designation at release.
- To `knowledge-management:knowledge-inventory` to record designations and expiry.

## Reviewer gates

From risk tier 2, `security-privacy` reviews the access and classification criteria and `evaluation-quality` reviews
whether the quality evidence is adequate for the tier. Their blocking findings must be resolved before the standard is
published and before high-tier designations are granted.

## Failure modes

- The standard is uniform across tiers, so low-risk agents are blocked and makers go around it.
- Designation never expires, and approved sources outlive their owners and reviews.
- The standard encodes remembered platform limits that later change.
- Release does not check designation, so the standard exists only on paper.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Approve a whole site as a grounding source without separating authoritative from working content.
- Let a designation outlive an overdue review or a departed owner.
- Write product limits or behaviours into the standard from memory.
- Treat designation of sources as a substitute for testing the agent.

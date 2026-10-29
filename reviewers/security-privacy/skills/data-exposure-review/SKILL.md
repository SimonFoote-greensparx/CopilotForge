---
name: data-exposure-review
description: Reviews what content an AI solution can reach and reveal - oversharing, permissions, sensitivity labels, the agent's sharing scope, web and public knowledge, and where outputs travel - and classifies each finding as blocking or advisory with a fix. Use when an agent or Copilot rollout reaches its security gate, when a maker adds a large knowledge source, or when sensitive content surfaces in answers.
license: CC-BY-4.0
metadata:
  department: security-privacy
  lifecycle: Assure, Launch, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-copilot, m365-agents, copilot-studio, sharepoint, purview, entra
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-privacy, ms-agent-builder, ms-copilot-studio-security-governance, ms-copilot-studio-zoned-governance, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Data exposure review

## Purpose

Copilot and agents answer with the permissions of the person asking, so they rarely create new access; they make
existing access far easier to use. Content that was overshared but obscure becomes overshared and discoverable in a
single question. This reviewer skill examines what an AI solution can reach, who can reach the solution, and where its
outputs go, and classifies each finding as blocking or advisory with a specific fix. Reviews go wrong when they accept
"it respects permissions" as the answer, when the real question is whether the permissions were right in the first place.

## When to use

- An agent or AI solution at risk tier 2 or above reaches its `security-privacy` gate.
- A maker adds a large site, library, connector index or public website as knowledge.
- An organisation is preparing a broad Copilot rollout and needs an oversharing view first.
- Sensitive or unexpected content has surfaced in an AI answer.
- An agent's sharing scope is about to widen.

## When not to use

- Reviewing connectors, actions, tools and APIs the solution calls - use `security-privacy:connector-review`.
- Lawful basis, transparency, retention and DPIA screening for personal data - use `security-privacy:privacy-assessment`.
- The agent team's own pre-review check of each knowledge source - use `m365-agents:knowledge-source-readiness`.
- Classifying the solution's risk tier - use `opportunity-management:risk-classification`.
- Estate-wide classification, ownership and access models - use `data-governance:data-classification-for-ai` and `data-governance:ai-data-access-model`.

## Questions to ask first

1. What content can the solution ground on, and who can open each part of it today?
2. Who can use the solution, and how does that compare with who should see the content behind its answers?
3. What sensitivity labels or classifications apply, and is any sensitive content unlabelled?
4. Can the solution use public web content, and how will users tell web answers from internal ones?
5. Where do outputs go - chat only, documents, emails, other systems, people outside the organisation?

## Required inputs

- The agent brief or solution description, with audience, sharing scope, knowledge sources and risk tier.
- Knowledge readiness verdicts from `m365-agents:knowledge-source-readiness`.
- Permission and sharing reports for each source, or access to produce them.
- Permission-trimming test results from `m365-agents:agent-testing`.

Missing permission evidence is itself a finding: blocking from tier 2, because the reviewer cannot judge exposure that
nobody has looked at. Never assume a source is correctly shared because it is old or quiet.

## Decision framework

Classify every finding. From risk tier 2 a blocking finding stops release and is not traded against dates; below tier 2
the review is not a mandatory gate, but a finding that would be blocking means the tier is probably wrong and goes back
to risk classification.

| Finding | Blocking when | Advisory when | Typical fix |
|---|---|---|---|
| Overshared source | Confidential, personal or restricted content is open to people outside its intended audience | Low-sensitivity content is wider-shared than necessary | Correct permissions at source, remove broad grants and sharing links, or remove the source from scope |
| Agent sharing scope | Shared beyond the audience in the brief, or organisation-wide without a design decision | Audience slightly wider than needed for low-sensitivity content | Restrict sharing to named groups matching the brief |
| Labels and classification | Sensitive content unlabelled or labelled inconsistently with the audience | Labelling incomplete for low-sensitivity content | Apply or correct labels; confirm how the route treats labelled content |
| Web or public knowledge | Unvetted web sources can answer questions on regulated or safety topics | Web use is enabled but answers are clearly marked | Restrict to named sites or disable; make provenance visible |
| Output exposure | Outputs can be sent outside the organisation or to wider audiences without a person checking | Outputs saved to shared locations with matching access | Require confirmation, restrict destinations, inherit labels |
| Missing evidence | No permission review or no permission-trimming tests at tier 2 or above | Evidence partial for low-sensitivity sources | Produce the evidence before review continues |

Each finding names the risk, the standard or rule behind it, the specific fix and an owner. Disagreement escalates to the
accountable executive, whose risk acceptance is recorded in writing with a review date.

## Practitioner approach

Start from the audience, not the content. Write down who can use the solution and compare that, source by source, with
who should see what lies behind its answers. That comparison is where exposure lives.

Then examine each source as an attacker with ordinary access would. Ask what a curious employee in the audience could
get the agent to summarise: salaries, disciplinary notes, merger papers, customer data. Use permission reports, sharing
link reports and site membership, not the owner's recollection. Look in particular for broad grants to all staff,
"anyone with the link" sharing, inherited permissions on archive folders and personal storage shared as a team space.

Remember that agent instructions are not a control. An instruction telling the agent not to discuss salaries does not
stop a user who can open the salary file from finding it another way, and instructions can be talked round. The fix
for exposure is always at the source or the sharing scope.

Check labels next. Where sensitivity labels are in use, sample the sources to see whether sensitive content is labelled
and whether the chosen route honours those labels as the organisation expects, confirmed from the current source
records. Unlabelled sensitive content is a finding even if permissions look right, because labels drive downstream
protection.

Review web and public knowledge separately. Record which sites are allowed and why, and whether users can tell when an
answer came from outside the organisation. On regulated, legal or safety topics, unvetted web grounding is blocking.

Follow the output. If the solution drafts emails, writes documents, posts to channels or calls other systems, trace
where the content lands and who can see it there. Outputs that leave the organisation without a person checking are
blocking from tier 2.

Read the permission-trimming test results. Confirm that tests used real users with different access, including someone
outside the audience. If they did not, send the agent back to testing.

Write the review as a list of findings, each classified, each with a fix and owner. Be proportionate: a tier 2 team
agent over a curated library may produce two advisory findings and a pass. Over-blocking teaches makers to avoid the
gate. Close the review only when blocking fixes are evidenced, and re-review if sharing widens later.

## Outputs

- The data exposure section of the `ai-risk-assessment`: sources reviewed, audience comparison, findings classified as blocking or advisory with risk, fix, owner and date, and the verdict (pass, pass with advisory findings, or blocked).
- Any written risk acceptance from the accountable executive.
- Referrals for estate-wide oversharing to the platform team and `data-governance:ai-data-access-model`.

## Microsoft platform considerations

Permission-trimmed grounding, sensitivity label handling, oversharing reports, sharing limits and web grounding controls
are product features whose behaviour and availability change. Confirm current behaviour for the chosen route in the
source records (`ms-copilot-privacy`, `ms-agent-builder`, `ms-copilot-studio-security-governance`) before relying on
them, and record what was checked.

## Adoption considerations

A broad Copilot rollout without an oversharing review is the most common way trust is lost early. Where blocking
findings delay an agent, explain the risk in plain words to the business owner; makers who understand the reason come
back earlier next time.

## Knowledge considerations

Most exposure fixes are knowledge fixes: permissions corrected, archives removed, sources narrowed. Pass recurring
patterns to `knowledge-management:knowledge-cleanup` so they are fixed across the estate, not one agent at a time.

## Security and privacy considerations

This skill is the security and privacy review of data exposure. Personal data findings also go to
`security-privacy:privacy-assessment`; actions and connectors go to `security-privacy:connector-review`.

## Responsible AI considerations

Exposure of personal data about colleagues can cause real harm even inside the organisation. Where answers could reveal
information about individuals, flag the case to `responsible-ai:ai-impact-assessment` through risk classification.

## Evaluation requirements

Blocking fixes need evidence: a re-run permission report, a re-run permission-trimming test, or a screenshot of sharing
settings. Advisory findings need an owner and a date tracked to closure.

## Value measures

Track, at portfolio level, the number of blocking exposure findings per review, time to close them, and the share of
agent knowledge sources with a current permission review. The security and privacy lead owns these measures.

## Scale notes

### Starter

Review sources and sharing with the agent owner in one session using built-in sharing reports. Keep first agents to a
named team and curated sources, which avoids most blocking findings.

### Scale

Make the review a standard gate in the CoE release cadence, with a shared findings format, and use platform oversharing
reports to target reviews.

### Enterprise

Federate tier 2 reviews to trained business-unit reviewers using the same blocking criteria, with the central team
reviewing tier 3 and 4. Track findings across the portfolio and feed patterns into estate-wide remediation.

## Hand-offs

- Back to `m365-agents:knowledge-source-readiness` and `m365-agents:agent-use-case-design` with fixes to sources and scope.
- To `security-privacy:privacy-assessment` for personal data and `security-privacy:connector-review` for actions.
- To `m365-agents:agent-release-readiness` with the verdict.
- To `data-governance:data-classification-for-ai` and `data-governance:ai-data-access-model` for estate-wide classification and access issues.

## Reviewer gates

This skill is the `security-privacy` gate for data exposure. It applies as a blocking gate from risk tier 2 and as an
advisory check below it. Blocking findings stop release and are not traded against dates; disagreement escalates to the
accountable executive for written risk acceptance.

## Failure modes

- The review accepts "permissions are respected" without checking whether the permissions were right.
- Instructions telling the agent to avoid a topic are accepted as a control.
- Sharing is widened after the review and nobody re-reviews.
- Everything is classed blocking, makers route around the gate, and real risks go unseen.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Accept agent instructions as a substitute for correct permissions.
- Trade a blocking finding against a launch date.
- Pass a tier 2 or higher solution without permission evidence and permission-trimming tests.
- Record a finding without the risk, the fix and an owner.

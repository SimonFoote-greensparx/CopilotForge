---
name: coe-knowledge-pillar
description: Runs the CoE's knowledge management pillar - a pillar lead, the layered knowledge asset register, owners and review dates for the content agents rely on, a knowledge check in intake, knowledge champions, and a loop that turns agent failures into content fixes - applying the knowledge-management standards. Use when the pillar exists on paper only, when agents give outdated answers, or when nobody owns the content solutions ground on.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Mobilise, Enable, Deliver, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-copilot, m365-agents, copilot-studio, sharepoint, purview
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-studio-guidance, ms-copilot-privacy, ms-declarative-agents, ms-agent-builder, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# CoE knowledge pillar

## Purpose

Most agents fail on knowledge, not technology: the policy is out of date, nobody owns the library, or the answer lives in
someone's inbox. This skill runs the CoE's knowledge management pillar so that the content AI solutions depend on is
owned, current and fit to ground on. It sets up the pillar lead, the knowledge asset register, the knowledge check in
intake and the loop from agent failures back to content owners. The pillar usually goes wrong by becoming a one-off
clean-up project, or by the CoE trying to own content that only the business can keep accurate.

## When to use

- The CoE charter lists knowledge management as a pillar but nobody runs it.
- Agents or Copilot give outdated, conflicting or surprising answers and nobody knows who fixes the source.
- The CoE needs a knowledge asset register before its Deliver phase.
- Several solutions ground on the same sources and the CoE needs a consistent way to keep them current.

## When not to use

- Setting the organisation's knowledge standards and methods in depth - the `knowledge-management` department, for example `knowledge-management:knowledge-grounding-standards`.
- Inventorying every knowledge source across the organisation - use `knowledge-management:knowledge-inventory`.
- Checking the sources for one specific agent - use `m365-agents:knowledge-source-readiness`.
- Keeping one live agent's knowledge current in operation - use `ai-operations:knowledge-refresh`.
- Fitting knowledge champions into the CoE alongside the other Champion roles - use `ai-centre-of-excellence:coe-champion-integration`.

## Questions to ask first

1. Who leads the knowledge pillar, and with how much agreed time?
2. Which knowledge do current and planned solutions rely on, and does each source have a business owner?
3. Does the organisation have a knowledge or information management function whose standards the CoE should apply?
4. How is content classified for sensitivity and audience today, and is that reflected in permissions?
5. How do knowledge problems surface now: user complaints, agent feedback, or not at all?

## Required inputs

- The list of planned and live solutions and their knowledge sources, from `ai-centre-of-excellence:coe-portfolio-management` or intake records.
- Any existing knowledge standards, or the outputs of `knowledge-management:knowledge-readiness-assessment`.
- Classification and labelling arrangements from the information or data governance function.
- The knowledge champions available, from `ai-centre-of-excellence:coe-champion-integration`.

If no standards exist, adopt a minimum set (owner, review date, version, classification, single authoritative copy) and
mark the fuller standard "to confirm" with the `knowledge-management` department.

## Decision framework

Keep the knowledge asset register in layers, because each layer has different owners and review needs.

| Layer | Examples | Typical owner | Typical review rhythm |
|---|---|---|---|
| Policies and standards | HR policies, security policy, codes of practice | Policy owner | At each policy change and at least annually |
| Procedures | How-to processes, operating procedures | Process owner | When the process changes, at least annually |
| Templates and guidance | Forms, templates, guidance notes | Function owner | When used content changes |
| FAQs and lessons learned | Common questions, post-project lessons | Service or team lead | Quarterly |
| Agents and automations built on the above | Agents, Cowork tasks, flows | Solution's knowledge owner | At each solution review |

Every register entry needs an owner role, a review date, a version or last-updated date, a classification and an
authoritative location. Classify each source used by a solution.

| Condition | Test | Pillar action |
|---|---|---|
| Ready | Owned, current, single authoritative copy, correctly permissioned | Solutions may ground on it |
| Ready with conditions | Owned but needs a fix with a date | Ground with the fix tracked; retest after it |
| Not ready | No owner, outdated, duplicated or overshared | Fix before any solution grounds on it |

## Practitioner approach

Appoint the pillar lead and agree their time. The lead does not own content; they make sure content has owners and
that the owners know agents depend on it. Where an information or knowledge management function exists, the lead
applies its standards and brings AI-specific needs into them, rather than writing a parallel rulebook.

Start the register from demand, not from the whole estate. List the sources that current and next-quarter solutions
rely on, put them in the layers, and find an owner for each. A register of fifty well-owned sources that agents actually
use is worth more than an inventory of every library in the organisation. Wider inventory work belongs to
`knowledge-management:knowledge-inventory` when the organisation is ready for it.

Add a knowledge check to intake. From tier 1 upwards, every opportunity names its sources and their condition before
prioritisation. Ideas whose knowledge is not ready leave Assess with a precondition: fix the content first, often with
help from a knowledge champion. This is one of the most useful outcomes the CoE can produce, because the fix improves
everyday Copilot answers as well as the planned agent.

Set review dates by layer and connect them to the solution reviews. When a policy changes, the solutions that ground on
it are listed in the register, so their knowledge owners know to check answers. Build the reverse loop too: wrong or
outdated answers reported by users, Champions or analytics go to the register, which routes them to the content owner.
Track the issue to closure.

Work with permissions and classification. Content that is overshared will be surfaced by Copilot to people who should
not see it; content locked away cannot ground an agent for its intended audience. Raise both with the data owners and
information security, and record the decision against the register entry.

Bring knowledge champions in as helpers to owners, flagging stale content and gathering common questions. They support
but never replace the business owner.

Report the pillar's health at steering each quarter: sources in the register, share with owners and in-date reviews,
knowledge preconditions raised and closed, and answer issues routed and resolved. Be honest that a register does not
guarantee accuracy; it guarantees that someone is accountable for it.

## Outputs

- A knowledge asset register in layers, each entry with owner role, review date, version, classification, authoritative location and dependent solutions.
- A knowledge check for intake, with ready, ready-with-conditions and not-ready outcomes.
- A knowledge issue loop: how reported problems reach content owners and are tracked to closure.
- A quarterly knowledge pillar report for steering.

## Microsoft platform considerations

Copilot and agents respect existing permissions, so oversharing in SharePoint and other sources is surfaced rather than
created by AI. Sensitivity labels and data governance tooling in Microsoft Purview, and SharePoint site design, are the
main levers. Agents built in Agent Builder or Copilot Studio ground on knowledge in different ways; check current
behaviour and limits in `references/sources.md` before setting standards that depend on them.

## Adoption considerations

Content owners need to know why their work matters now. Show them a real agent answer drawn from their content, good
or bad; that usually does more than any policy. Celebrate content fixes in the success stories area alongside agent
launches.

## Knowledge considerations

This skill is the CoE's knowledge practice. Defer to the `knowledge-management` department for the organisation's
standards, lifecycle and grounding rules, and feed back what the CoE learns from live solutions.

## Security and privacy considerations

Treat oversharing as a pillar finding, not a side issue. Sources with personal or sensitive data need the right
classification and permissions before any solution grounds on them, and the `security-privacy` review applies from tier
2. Ask the data protection officer where personal data appears in knowledge sources.

## Responsible AI considerations

Outdated or incomplete knowledge behind a solution that informs decisions about people, money, safety or rights is a
harm risk, not just a quality issue. Set shorter review rhythms for those sources and record who checks them.

## Evaluation requirements

Use the test sets from `m365-agents:agent-testing` to show the effect of knowledge fixes: rerun the questions that failed
after the content is corrected. Repeated failures on the same source are evidence for the not-ready classification.

## Value measures

Measure at pillar level: share of grounding sources with an owner and an in-date review, knowledge preconditions closed,
median time from a reported answer issue to a content fix, and answer accuracy on test sets before and after fixes. The
pillar lead owns these; baseline them when the register starts.

## Scale notes

### Starter

A short list of the sources the first solutions use, each with an owner and a review date, kept in the working group's
shared space. One person holds the knowledge role among others.

### Scale

A pillar lead, a layered register, a knowledge check in intake, knowledge champions and a quarterly pillar report.

### Enterprise

Each spoke maintains register entries for its own sources under hub standards; the hub owns shared sources such as
organisation-wide policies, aligns with the information management function and reports estate-wide knowledge health.

## Hand-offs

- To `knowledge-management:knowledge-grounding-standards` for the standard content must meet.
- To `knowledge-management:knowledge-cleanup` for larger clean-up of redundant or outdated content.
- To `m365-agents:knowledge-source-readiness` for source checks on a specific agent.
- To `ai-operations:knowledge-refresh` for keeping live agents' knowledge current.

## Reviewer gates

Not applicable to the pillar's design, which sets practice rather than releasing a solution. Register entries behind
tier 2 and above solutions are evidence for the `security-privacy` and `evaluation-quality` reviews of those solutions.

## Failure modes

- The pillar runs as a one-off clean-up and the register is stale within six months.
- The CoE takes ownership of business content and cannot keep it accurate.
- Intake skips the knowledge check and agents launch on unowned sources.
- Answer issues are fixed in the agent's instructions instead of the source, so Copilot keeps giving the old answer elsewhere.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Let a solution ground on a source with no business owner.
- Make the CoE or a Champion the owner of business content.
- Widen permissions on content just so an agent can reach it without the data owner's decision.
- Report knowledge measures by individual content owner.

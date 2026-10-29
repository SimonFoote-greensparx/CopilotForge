---
name: ai-reference-architecture
description: Maintains a small set of reference architectures for recurring Microsoft AI patterns - knowledge agent, business-data agent with actions, AI-assisted automation, custom Foundry solution - each with components, identity and data flows, mandatory controls, known limits and an owner. Use when the same design questions keep recurring, when reviewers need a baseline to judge conformance, or when a new pattern has been proven and should be reused.
license: CC-BY-4.0
metadata:
  department: ai-architecture
  lifecycle: Mobilise, Deliver, Scale, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, power-platform, sharepoint, entra, azure
  edition-support: scale, enterprise
  reviewers: design-authority
  sources: ms-agents-extensibility, ms-agents-compare, ms-copilot-studio-guidance, ms-copilot-studio-security-governance, ms-foundry-models
  status: draft
  authors: Simon Foote
---

# AI reference architecture

## Purpose

When every team designs its first agent from scratch, the organisation pays for the same mistakes many times. This
skill keeps a short, owned set of reference architectures for the AI patterns the organisation actually builds, each
showing the components, the flows of identity and data, the controls that are mandatory and the known limits. It gives
builders a safe default and gives reviewers a baseline. Reference architectures go wrong when they are copied from a
vendor diagram, written once and never updated, or so abstract that nobody can build from them.

## When to use

- Three or more solutions have followed a similar shape and their designs differ for no good reason.
- The design authority needs a baseline to judge conformance against.
- A pattern has been proven in production and should be offered as the default.
- Microsoft has changed a capability that an existing reference depends on.
- A new platform has been approved and needs a starting design.

## When not to use

- Choosing a platform for a single solution - use `ai-architecture:platform-selection`.
- Reviewing a solution against the references - use `design-authority:architecture-conformance`.
- Writing engineering and code standards for pro-code work - use `ai-engineering:ai-engineering-standards`.
- Setting the organisation's platform mix - use `ai-strategy:platform-strategy`.
- Detailed grounding options inside a reference - use `ai-architecture:grounding-patterns`.

## Questions to ask first

1. Which solution shapes has the organisation built more than once, and which are planned on the roadmap?
2. Which design decisions caused rework, review findings or incidents in those solutions?
3. Which controls are non-negotiable by risk tier, according to the governance framework?
4. Who will own each reference and keep it current as Microsoft changes the platforms?

## Required inputs

- The portfolio of live and planned solutions, from `platform-governance:ai-solution-inventory` or the CoE register.
- Past architecture decision records and design review findings.
- The governance framework's tier controls and the approved platform list.
- Source records for each platform in scope.

If there is no portfolio history, start with one reference for the most common planned pattern and mark it
provisional until a solution has been built and reviewed against it.

## Decision framework

Admit a pattern as a reference only when it meets all of these tests.

| Test | Pass when |
|---|---|
| Recurrence | At least two live or committed solutions follow it, or the roadmap shows it will recur |
| Proven | At least one solution built on it has passed its design and security gates |
| Owned | A named architecture role maintains it and reviews it on a set cycle |
| Buildable | A maker or engineer can start from it without asking the architect for missing decisions |
| Bounded | It states the conditions under which it does not apply |

Each reference contains: purpose and fit, a component view, identity flows, data flows, mandatory controls by risk tier,
variation points (decisions left to the solution), known limits, revisit triggers, the volatile facts it depends on and
the owner.

## Practitioner approach

Start from evidence, not from a whiteboard. Read the decision records, review findings and incident notes for the
solutions already built, and group them by shape. In most organisations four shapes cover the majority of demand: an
agent grounded on governed knowledge, an agent that reads and writes business data through connectors and flows, an
automation with an AI interpretation step, and a custom solution built in Microsoft Foundry. Do not invent a fifth
until it recurs.

For each shape, draw the minimum set of components and the two flows that matter most: whose identity is used at each
hop, and where data travels and rests. Mark every hop where identity changes, because that is where most security
findings arise. Mark where data leaves the Microsoft 365 boundary or the tenant, and what agreement covers it.

List mandatory controls by risk tier rather than one list for all. A tier 1 knowledge agent needs a named owner,
permission-trimmed sources and a review date; a tier 3 business-data agent also needs user authentication on writes,
confirmation steps, logging, evaluation in the pipeline and continuity arrangements. Reference the governance framework
rather than restating it.

Separate the fixed decisions from the variation points. The reference fixes what should not vary (identity pattern,
logging, environment zone); the solution decides what legitimately varies (knowledge sources, channels, tone). If a
builder cannot tell which is which, the reference is too vague.

State known limits plainly and point to the source record for each. Microsoft changes capability, naming and limits
often, so the reference records which facts it depends on and the date they were last checked, rather than embedding
numbers.

Publish references where makers and engineers already look, linked from the CoE pages and the build skills. Assign an
owner and a review cycle; review sooner when a dependent capability changes or when conformance reviews keep finding
the same deviation, which usually means the reference is wrong rather than the builders. Retire references that no
longer recur, and record why.

## Outputs

- A reference architecture library: one entry per pattern with purpose, components, identity and data flows, tier controls, variation points, limits, revisit triggers, volatile facts and owner.
- An architecture decision record on the `architecture-decision-record` template for each admission, material change or retirement.
- A change log that conformance reviewers and builders can follow.

## Microsoft platform considerations

References span Microsoft 365, Copilot Studio, Power Platform, Microsoft Entra and Azure, and Microsoft moves capability
between them. Name the platform capability a reference depends on and point to the source record
(`ms-agents-extensibility`, `ms-agents-compare`, `ms-copilot-studio-guidance`, `ms-foundry-models`), never a remembered
limit or licence.

## Adoption considerations

Builders adopt references that save them time. Provide a starter solution, a worked fictional example or a checklist
alongside each diagram, and collect feedback from the first teams to use it.

## Knowledge considerations

Each reference names the knowledge pattern it assumes and the standard sources must meet, linking to
`ai-architecture:grounding-patterns` and `knowledge-management:knowledge-grounding-standards` rather than repeating them.

## Security and privacy considerations

Identity hops, data boundaries and logging are the security core of every reference. Have `security-privacy` agree the
mandatory controls before publication, so solutions that conform start with fewer findings.

## Responsible AI considerations

For patterns that can inform decisions about people or act without per-action review, the reference includes human
oversight and logging as fixed decisions, and names the `responsible-ai` review that applies from tier 3.

## Evaluation requirements

Each reference states the evaluation approach it expects by tier (manual test set, built-in testing, automated harness)
and where evaluation evidence is stored, consistent with `evaluation-quality:ai-evaluation-strategy`.

## Value measures

Measure reuse and rework at portfolio level: the proportion of new designs based on a reference, design review findings
per solution for conforming versus non-conforming designs, and time from brief to design approval. The AI architecture
lead owns these measures, with a baseline taken before the library is published.

## Scale notes

### Starter

A single page per pattern is enough, and one or two patterns cover most needs. Starter organisations often rely on a
partner's references; adopt them only after checking they fit the organisation's controls.

### Scale

Maintain three to five references with owners and review dates, and make conformance to them part of the design gate.

### Enterprise

Run a reference library with versioning, federated contributors and a formal change process, and track which solutions
use which version so changes can be assessed for impact.

## Hand-offs

- To `design-authority:architecture-conformance`, which reviews solutions against the published references.
- To `ai-architecture:platform-selection` and the build departments, which start from the references.
- To `ai-engineering:ai-engineering-standards` for code-level standards that implement a reference.

## Reviewer gates

New and materially changed references are reviewed by `design-authority` before publication, and their mandatory
controls are agreed with `security-privacy`. References are standards, so they apply to solutions from risk tier 1.

## Failure modes

- A vendor diagram is adopted as the reference and does not reflect the organisation's identity or data boundaries.
- References are never revisited, and builders deviate because the published design no longer works.
- References are so abstract that every solution needs an architect anyway.
- Too many references are published, and none is maintained.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Publish a reference without an owner and a review cycle.
- Embed product limits, prices or availability in a reference instead of pointing to the source record.
- Copy or closely paraphrase a vendor's published architecture.
- Treat repeated deviation by builders as a builder problem before checking whether the reference is wrong.

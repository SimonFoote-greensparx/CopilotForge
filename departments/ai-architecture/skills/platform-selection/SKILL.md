---
name: platform-selection
description: Selects the Microsoft platform for one solution once suitability is agreed - Agent Builder, Copilot Studio, Power Platform automation, Copilot Code or Microsoft Foundry - weighing audience, data, actions, identity, operability and skills, and records the choice in an architecture decision record. Use when a solution has a pattern but no platform, when makers and engineers disagree where to build, or when a build has outgrown its platform.
license: CC-BY-4.0
metadata:
  department: ai-architecture
  lifecycle: Envision, Deliver, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-cowork, copilot-code, copilot-studio, ai-foundry, power-platform, azure
  edition-support: starter, scale, enterprise
  reviewers: design-authority, security-privacy
  sources: ms-agents-extensibility, ms-agents-compare, ms-declarative-agents, ms-agent-builder, ms-copilot-studio-guidance, ms-foundry-models
  status: draft
  authors: Simon Foote
---

# Platform selection

## Purpose

Once a solution has passed suitability, someone still has to decide where it is built and who will run it. This skill
chooses the Microsoft platform for one named solution, from the options the organisation has approved, and records the
reasoning in an architecture decision record that a reviewer can challenge. Selection goes wrong when the platform
follows the builder's favourite tool, when the cheapest option to build is chosen without counting the cost to run, or
when a pro-code route is taken for a need that a configured agent would meet.

## When to use

- A solution has an agreed pattern from suitability and now needs a build platform.
- Makers want Copilot Studio, engineers want Microsoft Foundry, and nobody has written down why.
- A live solution is hitting the limits of its platform and a move is being considered.
- A partner proposes a platform and the organisation needs to test the proposal before contracting.
- A solution combines parts (an agent, a flow, a custom service) and each part needs a home.

## When not to use

- Deciding whether AI is appropriate at all, and which pattern - use `opportunity-management:ai-suitability`.
- Setting the organisation-wide mix of platforms and what is approved - use `ai-strategy:platform-strategy`.
- Reviewing a platform choice someone else has made, at the design gate - use `design-authority:platform-fit-review`.
- Choosing a model within Microsoft Foundry - use `ai-foundry:model-selection`.
- Deciding whether a need justifies a Foundry build in detail - use `ai-foundry:foundry-solution-assessment`.
- Placing the solution in environments and tenants - use `ai-architecture:environment-topology`.

## Questions to ask first

1. Who will use the solution, through which surface (Microsoft 365 Copilot, Teams, a website, a business application), and how many people?
2. What will it ground on and what must it do in other systems - read, write, send, approve?
3. Whose identity must each action run under, and is any data leaving the tenant?
4. Who will own and operate it after release, and what skills do they actually have today?
5. What does the organisation already license and approve, according to the platform strategy and the CoE's approved list?

## Required inputs

- The suitability decision and risk tier, from `opportunity-management:ai-suitability` and `opportunity-management:risk-classification`.
- An agent brief or solution brief describing audience, scope, knowledge and actions.
- The approved platform list and principles from `ai-strategy:platform-strategy`, if one exists.
- The operating team's declared skills and capacity.
- Any non-functional requirements already known, ideally from `ai-architecture:ai-non-functional-requirements`.

If the approved platform list is missing, record the assumption and mark the decision provisional. Never assume a
licence, feature or region is available; mark it "to confirm" against the source records.

## Decision framework

Start from the least engineered option that meets the need, and move up only for a stated reason.

| Option | Prefer it when | Move on when |
|---|---|---|
| Agent Builder (declarative agent in Microsoft 365 Copilot) | Knowledge-based help for a defined audience inside Microsoft 365, few or no actions, a business owner can maintain it | Needs structured actions, channels outside Microsoft 365, ALM across environments or managed authentication |
| Copilot Studio agent | Business data workflows, connectors and flows, several channels, environment-based governance and ALM | Needs custom orchestration, specialist models, retrieval engineering or code-level evaluation |
| Power Platform automation, with or without an AI step | Fixed steps on structured data with an interpretation step in the middle | The language work dominates and needs conversation |
| Copilot Code build | The outcome is software that an engineering team will own in a repository | Nobody can review, deploy and maintain the code |
| Microsoft Foundry solution | Specialist models, custom retrieval, tools or orchestration that configured agents cannot deliver, with a team able to operate it | Value cannot justify the operating cost, or the team does not exist |

Then test the leading option against five gates. A "no" on any gate moves the decision up or down a row, or adds a
precondition.

| Gate | Question |
|---|---|
| Identity | Can every action run under the user or a narrowly scoped service identity on this platform? |
| Data | Can grounding stay permission-trimmed and inside agreed boundaries? |
| Operability | Can the named operating team monitor, change and support it? |
| Lifecycle | Is there a way to test, promote and roll back changes? |
| Cost | Is the run cost understood well enough to fund, per the licensing guide or partner? |

## Practitioner approach

Begin by writing the solution in one paragraph without naming a product: who uses it, through which surface, what it
knows, what it does and who answers for it. If that paragraph cannot be written, the brief is not ready and the
selection will only encode guesses.

List the candidate options that the platform strategy allows. Where no strategy exists, use the decision framework rows
as the long list and note that the choice is not yet constrained by policy. Discard options the organisation cannot
operate; an elegant Foundry design with no engineering team behind it is a liability, not an option.

Walk the framework from the top. For each option, note the first reason it fails to meet the need. The first option
with no disqualifying reason is the leading candidate. Resist the pull of a richer platform "in case it grows": record
the growth signal instead, and state the trigger that would justify a move later, such as a second channel, write
actions in a line-of-business system, or an evaluation regime the current platform cannot support.

Apply the five gates to the leading candidate. Identity and data usually decide close calls. A configured agent that
can only run an action under the maker's connection is a weaker choice than a slightly heavier platform that supports
user authentication. Operability is the gate most often skipped: ask the operating team, not the builder, whether they
can support the choice at the hours and volumes expected.

Split composite solutions into parts and choose for each. A common and healthy shape is an agent for conversation, a
flow for deterministic actions and an existing system of record for data. Record where each part lives and how they
connect, and hand the connections to `ai-architecture:ai-integration-patterns`.

Check volatile facts at the time of decision. Feature availability, regional support, licensing and limits change
often; cite the source record you checked and the date. Licensing conclusions belong to the Microsoft licensing guide
or a licensing partner, never to this record.

Write the architecture decision record: context, options considered, decision, consequences, the triggers for
revisiting, and who decided. Share it with the business owner and the operating team, then take it to the design gate
from risk tier 2. A good record lets a reviewer disagree with the reasoning rather than guess at it.

## Outputs

- An architecture decision record on the `architecture-decision-record` template: context, options, gates, decision, consequences, revisit triggers and decision owner.
- A one-paragraph platform rationale for the agent brief or solution brief.
- A list of preconditions and volatile facts to confirm, each with the source record to check.

## Microsoft platform considerations

Agent Builder, Copilot Studio, Power Platform, Copilot Code and Microsoft Foundry differ in authoring model,
authentication options, channels, lifecycle tooling and evaluation support, and Microsoft moves capabilities between
them. Declarative and custom engine agents have different trade-offs described in `ms-agents-compare`. Check
`ms-agents-extensibility`, `ms-agent-builder` and `ms-foundry-models` for current capability before deciding, and never
state availability, limits or licensing from memory.

## Adoption considerations

The chosen platform shapes who can maintain the solution. A business-owned knowledge agent built in Agent Builder can
be kept current by its owner; the same agent in Foundry depends on engineers. Tell the business owner what the choice
means for their part in upkeep.

## Knowledge considerations

Each platform grounds differently. Record which knowledge sources the solution needs and whether the chosen platform can
reach them with permission trimming intact. Detailed grounding design goes to `ai-architecture:grounding-patterns`.

## Security and privacy considerations

The identity and data gates are security questions. Note any action that cannot run under user identity on the chosen
platform, any data leaving the tenant and any connector outside policy, so the `security-privacy` review starts with
facts rather than discovery.

## Responsible AI considerations

Platform choice affects how much control the organisation has over model behaviour, content filtering and oversight.
For uses that inform decisions about people, prefer the option that makes human review and logging easiest, and flag
the case to the `responsible-ai` reviewers through risk classification.

## Evaluation requirements

State how the chosen platform will be evaluated before release and after change: built-in testing, an evaluation set
or an automated harness. If the risk tier needs evaluation the platform cannot support, the selection fails the
lifecycle gate.

## Value measures

Track, at portfolio level, the proportion of solutions that stay on their original platform for their first year, the
number of costly re-platforming moves and the time from brief to platform decision. The AI solution architect owns
these measures, with the baseline taken from decisions made before this skill was adopted.

## Scale notes

### Starter

Most solutions land in Agent Builder, Copilot Studio or simple automation. Record the decision on one page and use a
partner's view before committing to Foundry or a pro-code build.

### Scale

Keep a library of past decision records so similar solutions are placed consistently, and align every record with the
approved platform list. The design gate reviews tier 2 and above.

### Enterprise

Publish reference decisions per pattern through `ai-architecture:ai-reference-architecture`, and let business-unit
architects decide standard cases, with the central architecture team deciding novel or tier 3 and 4 cases.

## Hand-offs

- To `ai-architecture:environment-topology` to place the solution in environments and tenants.
- To `ai-architecture:ai-integration-patterns` and `ai-architecture:ai-identity-design` for connections and identities.
- To `copilot-studio:studio-agent-design`, `ai-foundry:foundry-solution-assessment` or `copilot-code:code-solution-brief` to start the build.
- To `design-authority:platform-fit-review` at the design gate.

## Reviewer gates

From risk tier 2 the decision record goes to `design-authority` for platform fit, and the identity and data gate answers
go to `security-privacy`. Below tier 2 the CoE lead records the decision and any challenge on the record.

## Failure modes

- The platform is chosen for the builder's skills, and the operating team inherits something it cannot support.
- A heavier platform is chosen "for future growth", and the solution costs more to run than it returns.
- An action that needs user identity is built on a route that only supports maker credentials.
- A feature assumed from memory is unavailable in the organisation's region or licence, discovered after build starts.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Select a platform before suitability has been decided and recorded.
- State licensing conclusions; route them to the Microsoft licensing guide or a licensing partner.
- Choose an option the named operating team cannot support.
- Leave the decision unrecorded, or record only the winner without the options rejected.

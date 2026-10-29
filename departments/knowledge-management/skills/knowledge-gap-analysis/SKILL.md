---
name: knowledge-gap-analysis
description: Finds and classifies knowledge gaps revealed by unanswered questions, agent fallbacks, wrong answers, user feedback, search failures and service desk themes - missing, unfindable, outdated, contradictory or inaccessible - and routes each to an owner with a fix. Use when agents often say they cannot help, when the same questions keep reaching people, or when feedback shows Copilot cannot find what staff need.
license: CC-BY-4.0
metadata:
  department: knowledge-management
  lifecycle: Measure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: m365-agents, copilot-studio, m365-copilot, sharepoint
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-studio-guidance, ms-agent-builder, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Knowledge gap analysis

## Purpose

Agents and Copilot are the best detectors of knowledge gaps an organisation has ever had: every fallback, wrong answer
and repeated question shows where knowledge is missing, buried, stale or locked away. This skill gathers those signals,
classifies each gap by cause, and routes it to the owner who can close it, so that knowledge improves where people
actually need it. It goes wrong when every failure is blamed on the AI and fixed by rewriting instructions, when gaps are
counted but never routed, or when the analysis drifts into monitoring what individuals asked.

## When to use

- Agents frequently fall back, decline or escalate on questions that are in scope.
- The same questions keep reaching HR, IT or other teams despite an agent or knowledge site existing.
- User feedback or wrong-answer reports suggest Copilot cannot find what staff need.
- A periodic review of knowledge for a domain or agent is due and needs evidence.

## When not to use

- Designing how user feedback is collected and handled for a live solution - use `ai-operations:ai-feedback-loop`.
- Testing an agent before release against expected answers - use `m365-agents:agent-testing`.
- Using Copilot Studio analytics to improve an agent's topics and configuration - use `copilot-studio:studio-analytics`.
- Gaps in people's skills or the programme's capability - use `organisation-tailoring:capability-gap-analysis`.

## Questions to ask first

1. Which agents, Copilot scenarios or knowledge domains are in scope, and over what period?
2. What signals are available - agent analytics, unanswered or escalated conversations, feedback, search with no results, service desk categories?
3. What privacy rules govern access to conversation content, and has the DPO or privacy lead agreed this use?
4. Who owns the domains concerned, and who can create or fix content?
5. What would count as a closed gap - an answer now found, fewer escalations, fewer repeat tickets?

## Required inputs

- Aggregate signals for the period: fallback and escalation rates, feedback themes, unanswered question themes, service desk categories, search terms with no useful results.
- Agreement on what conversation content may be reviewed, by whom, and in what form, from the privacy lead.
- The knowledge register with owners, from `knowledge-management:knowledge-inventory`.
- The agent's intended scope, from its brief, so out-of-scope questions are not treated as knowledge gaps.

Where conversation content cannot be reviewed, work from aggregate themes and categories only. Never identify, rank or
follow up individual users from their questions.

## Decision framework

Classify each recurring gap by cause, because the cause decides the fix and the owner.

| Gap type | Signal | Fix | Owner |
|---|---|---|---|
| Missing | Nobody has written the answer down | Create content | Domain owner commissions; content owner writes |
| Unfindable | The answer exists but is buried, badly titled or in an unexpected format | Restructure, retitle, improve metadata | Content owner, with knowledge team |
| Outdated | The answer exists but is wrong now | Review and update | Content owner, through review cycles |
| Contradictory | Two sources give different answers | Decide the authoritative answer, archive the other | Domain owner |
| Inaccessible | The answer exists but the asker cannot open it | Confirm the audience; fix access or route the question elsewhere | Content owner, with security review if access widens |
| Out of scope | The question is legitimately outside the agent's purpose | Clarify scope or redirect; not a knowledge gap | Agent owner |
| Configuration | Knowledge is good, but the agent does not use it | Fix grounding or instructions | Agent owner |

Prioritise by frequency multiplied by consequence: a rare question about safety outranks a common one about the canteen.

## Practitioner approach

Gather signals from several places, because each sees a different slice. Agent analytics show fallbacks, escalations
and unhelpful ratings; feedback captures what users say went wrong; service desk categories show what still reaches
people; search reports show what people look for and do not find. Agree with the privacy lead what conversation content
may be reviewed before anyone opens it, and prefer aggregated themes. The aim is to understand knowledge, not people.

Cluster before classifying. Group signals into recurring questions or themes, then pick the most frequent and most
consequential clusters for analysis. For each, try to answer the question yourself from the organisation's knowledge.
The way you fail tells you the gap type: you cannot find anything (missing or unfindable), you find something wrong
(outdated), you find two things (contradictory), or you find it but the asker's audience cannot open it (inaccessible).
If you find a good answer the agent should have used, the gap is configuration, and it goes to the agent owner rather
than the knowledge owner.

Separate genuine gaps from scope questions. Users ask agents things outside their purpose; that is a scope or
communication question, not a reason to widen the agent's knowledge. Record such clusters for the agent owner, who may
decide to redirect users or propose a new opportunity through intake.

Route each gap to a named owning role with a fix and a date, recorded in the gap log. Missing content needs a domain
owner to commission it; contradictory content needs a domain owner to decide. Inaccessible content needs care: the fix
may be to widen access, which needs classification and security review, or to accept that the asker should be redirected
to someone who can see it.

Close the loop. When a fix lands, re-ask the cluster's representative questions, confirm the agent or Copilot now finds
the answer, and add the questions to the agent's test set so the gap cannot reopen unnoticed. Report themes and closures
to domain owners regularly; patterns, such as one domain generating most gaps, point to ownership or lifecycle problems
rather than individual documents.

## Outputs

- A knowledge gap log: cluster, representative questions, frequency, consequence, gap type, fix, owning role, date and closure evidence.
- A periodic gap report by domain and agent for owners and the CoE, using aggregate data only.
- New test questions passed to agent test sets for closed gaps.

## Microsoft platform considerations

Copilot Studio and other agent routes provide analytics on conversations, outcomes and feedback, and Microsoft 365 offers
search and usage reporting; what is available, at what level of detail, and who may see it varies by route,
configuration and licensing. Confirm in the source records (`ms-copilot-studio-guidance`, `ms-copilot-privacy`) and with
the privacy lead before relying on conversation-level data.

## Adoption considerations

Users keep asking when they see their questions lead to better answers. Publish "you asked, we fixed" summaries by
theme, never by person, and tell users how to flag a wrong or missing answer.

## Knowledge considerations

Gap analysis is the demand signal for the whole department: it tells `knowledge-management:content-quality`,
`knowledge-management:knowledge-review-cycles` and `knowledge-management:sharepoint-knowledge-design` where effort pays
off. Record closures in the knowledge register.

## Security and privacy considerations

Questions can reveal personal circumstances (health, grievance, finances). Review conversation content only as agreed
with the privacy lead, aggregate wherever possible, and never attribute questions to individuals. Inaccessible-content
fixes that widen access go to `security-privacy:data-exposure-review` from risk tier 2.

## Responsible AI considerations

Look for gaps that fall unevenly, for example questions from frontline or non-native speakers failing more often.
Uneven gaps mean uneven benefit, and closing them is a fairness improvement as well as a knowledge one.

## Evaluation requirements

A gap is closed only when its representative questions are answered correctly from the authoritative source, verified
by re-asking. Add those questions to the agent's regression set through `m365-agents:agent-testing`.

## Value measures

Track fallback and escalation rates for in-scope questions, the number of recurring gaps open and closed per period, and
repeat questions reaching service teams. Agent and domain owners own these, reported in aggregate; never by individual
user.

## Scale notes

### Starter

Review the top themes from one agent's feedback and fallbacks monthly with its knowledge owner, and fix the top five.

### Scale

Run a monthly gap review across agents and domains with a shared gap log and routing rules, and report themes to the CoE.

### Enterprise

Combine agent analytics, search and service desk data into domain-level gap reporting for business-unit knowledge leads,
with privacy-approved access and trend reporting to steering.

## Hand-offs

- To content and domain owners to close missing, outdated and contradictory gaps.
- To agent owners and `m365-agents:agent-instructions` or `m365-agents:agent-grounding` for configuration gaps.
- To `opportunity-management:idea-capture` where out-of-scope clusters suggest a new need.

## Reviewer gates

Not applicable as a release gate; this skill improves knowledge rather than releasing solutions. Fixes that widen access
pass through `security-privacy` as described above.

## Failure modes

- Every failure is treated as an AI problem and fixed by rewriting instructions, while the content stays wrong.
- Out-of-scope questions are treated as gaps, and the agent's knowledge sprawls.
- Gaps are counted in dashboards but never routed to an owner.
- Conversation review strays into identifying who asked what, and trust collapses.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Identify, rank or follow up individual users from the questions they asked.
- Review conversation content without the privacy lead's agreement on scope and method.
- Widen access to close an inaccessible-content gap without classification and security review.
- Close a gap without re-asking its questions and confirming the answer.

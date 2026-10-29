---
name: department-scenario-design
description: Works with a department head and process owners to redesign a department workflow that spans several roles around Copilot, agreeing where Copilot helps at each step, the shared team conventions it needs, the human checks, the department's data boundaries and a department-level measure. Use when a function such as finance or HR wants a joined-up way of working with Copilot, or when individual role scenarios do not add up.
license: CC-BY-4.0
metadata:
  department: m365-copilot
  lifecycle: Envision, Enable, Measure
  maturity: adopter, scaler, ai-enterprise
  risk-tiers: 0, 1, 2
  platforms: m365-copilot, copilot-chat, m365-agents
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, responsible-ai
  sources: ms-copilot-overview, ms-copilot-adoption-hub, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Department scenario design

## Purpose

Individual scenarios help individuals; departments get most value when a whole workflow changes. This skill works with
a department head and the owners of a recurring departmental process (month-end reporting, recruitment campaigns, bid
preparation, policy updates) to redesign it around Copilot: where it helps at each step, which team conventions make
that work, where people must check, and how the department will know it has improved. It goes wrong when a department
"does Copilot" by collecting individual tips, so each person saves a little time but the process, its hand-offs and its
delays stay exactly as they were.

## When to use

- A department head wants a joined-up way for the function to work with Copilot, not a list of tips.
- A recurring process crosses several roles and is slow, late or full of rework.
- Role scenarios exist, but the department cannot see a combined effect.
- A department is about to receive licences and wants to start with its most important process.

## When not to use

- Writing app-specific scenario cards for one role - use `m365-copilot:copilot-role-scenarios`.
- Discovering and prioritising scenarios across the whole workforce - use `copilot-adoption:scenario-discovery`.
- Framing a significant business problem that may need a built solution - use `opportunity-management:problem-framing`.
- Redesigning a process for automation with flows - use `automation:automation-process-design`.
- Deciding whether a repeated departmental need warrants an agent - use `m365-agents:agent-opportunity-assessment`.

## Questions to ask first

1. Which departmental process matters most to the department head, and what is wrong with it today in time, quality or delay?
2. Who owns the process end to end, and which roles take part at each step?
3. Where does the process's content live, and is it shared in a way that suits the whole team?
4. At which steps would a wrong output cause real harm, and who checks it?
5. How will the department measure improvement, and what is the baseline today?

## Required inputs

- A department head who sponsors the work and a process owner who will run it.
- A simple current-state map of the process, with roles, steps, content and hand-offs.
- The roles' Copilot access and the relevant scenario cards, if any.
- The department's data boundaries: what content is sensitive and who may see it.

If there is no process owner, stop; the redesign will not stick. Where the baseline is missing, take it before changing
anything rather than estimating it afterwards.

## Decision framework

For each step of the process, classify Copilot's role.

| Step type | Copilot's role | Human role |
|---|---|---|
| Gathering inputs from mail, meetings and files | Summarise and compile, citing sources | Confirm completeness and resolve conflicts |
| First draft of a standard output | Draft from a team template and named sources | Edit, check facts and approve |
| Analysis of structured data | Explore and explain trends | Recalculate key figures and own conclusions |
| Review and approval | Check against a checklist or style guide | Decide and sign off |
| Decisions about people, money or compliance | Prepare information only | Decide through the existing approved process |

Then decide the department-level design: shared conventions (where content is stored, templates, naming, how decisions
are recorded), the human checkpoints, and whether any step is repeated so often across the department that it warrants
an agent or automation. Keep agents and flows as hand-offs, not part of this design.

## Practitioner approach

Pick one process with the department head, not five. The best first candidate is recurring, cross-role, painful and
measurable, such as monthly management reporting. Run a short workshop with the process owner and one person from each
role to map how it works today: who does what, using which content, waiting for whom. Capture the time, the delays and
the points where things are reworked.

Walk the map step by step and ask where Copilot could help and what would have to be true for it to work. You will find
that most of the gain comes from conventions rather than prompts: everyone saves inputs to the same library, uses the
same template, writes decisions in the same channel, and names files consistently. Without those, Copilot sees a
fragmented picture and each person gets different results. Agree the conventions and write them down; they are the
heart of the design.

Mark every step where an error would matter, and put a named human check there. Be firm about steps that involve
decisions about people, money or compliance: Copilot can prepare information, but the decision follows the existing
approved route. Where the department wants Copilot to draft performance-related content or judge individuals, stop and
refer to `responsible-ai` through risk classification.

Turn the design into a small set of role scenario cards that fit together, using `m365-copilot:copilot-role-scenarios`,
and a one-page department playbook: the process, the conventions, the checks and who to ask. Pilot it through one or two
cycles of the process with the team, then review what changed against the baseline.

Watch for steps that every cycle repeats with the same knowledge, such as answering the same policy questions or
compiling the same pack. Those are candidates for an agent or an automation; pass them to
`m365-agents:agent-opportunity-assessment` or the `automation` department rather than stretching Copilot prompts to fit.

Close with the department head: what improved, what conventions held, what needs to change next, and who owns the
playbook from here.

## Outputs

- A department scenario design: current and future process maps, Copilot's role at each step, human checkpoints and data boundaries.
- A department playbook with shared conventions and the linked role scenario cards, added to the `scenario-catalogue`.
- A department-level measure with baseline, owner and review date.
- A list of agent or automation candidates handed off for assessment.

## Microsoft platform considerations

Departmental scenarios usually combine Copilot in Teams, Outlook, Word, Excel and PowerPoint with shared SharePoint or
Teams locations. Capability differs by app and changes often; check `ms-copilot-overview` before designing a step around
a specific feature. Shared conventions depend on the department's sites being organised and permissioned for the team,
as described in `ms-copilot-privacy`.

## Adoption considerations

Department scenarios spread when the head of department uses them visibly and the process owner keeps the playbook
current. Coordinate with `copilot-adoption:role-based-adoption` so onboarding for the department's roles teaches the
process, not just the tools.

## Knowledge considerations

Departmental processes depend on templates, standards and reference content. Name each, its owner and its location in
the playbook; route gaps to the `knowledge-management` department.

## Security and privacy considerations

Departments such as HR, legal and finance handle sensitive content. Confirm the department's locations are restricted to
the right people before the pilot, and that conventions never move sensitive content into broader locations. Route
concerns to `security-privacy` and the data protection lead.

## Responsible AI considerations

Steps that touch decisions about people, money, safety or rights keep the decision with an accountable person and the
existing approved process. Designs that would use Copilot to evaluate individuals are referred to `responsible-ai`.

## Evaluation requirements

Pilot the design through at least one full cycle of the process, checking at each human checkpoint whether Copilot's
contribution was usable, and recording errors caught. Adjust before rolling the playbook out.

## Value measures

Measure the process, not the people: cycle time, delay, rework or quality of the departmental output, against the
baseline taken before the pilot. The process owner owns the measure; results are reported for the department or team.

## Scale notes

### Starter

One process in one department, a workshop, a one-page playbook and a pilot cycle, often facilitated by the Copilot lead.

### Scale

A small number of departmental designs per year through the adoption programme, with playbooks maintained by process
owners and Champions.

### Enterprise

Common designs for shared functions reused across business units with local variation, and a library of departmental
playbooks linked to the scenario catalogue.

## Hand-offs

- To `m365-copilot:copilot-role-scenarios` for the role cards the design needs.
- To `m365-copilot:work-context-readiness` for the department's sites and conventions.
- To `m365-agents:agent-opportunity-assessment` or `automation:automation-assessment` for repeated steps.
- To `value-realisation:benefit-hypothesis` where the department wants the benefit tracked formally.

## Reviewer gates

From risk tier 2, designs touching sensitive departmental content are reviewed by `security-privacy`, and designs near
decisions about people by `responsible-ai`; each finding is blocking or advisory, and blocking findings stop the pilot.

## Failure modes

- The department collects individual tips and the process itself never changes.
- Conventions are skipped, so Copilot sees fragmented content and results vary by person.
- A step involving decisions about people quietly starts relying on Copilot drafts.
- No baseline is taken, so the department cannot show any improvement.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Redesign a process without a named process owner and department sponsor.
- Let Copilot make or effectively make decisions about people, money or compliance.
- Measure the design by individual output or usage.
- Stretch prompts to do what an agent or automation should do; hand it off instead.

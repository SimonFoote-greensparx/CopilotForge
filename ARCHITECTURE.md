# Architecture

How CopilotForge is put together: the department model, programme orchestration, profile flow, generators and system
boundaries (design brief sections 3, 8, 9, 11 and 13).

## Conceptual model

CopilotForge models an AI transformation organisation, not a software implementation team. It is organised around
enduring capabilities rather than Microsoft's current product list; products are delivery surfaces inside the model.

```
                 Spanning: ai-centre-of-excellence, organisation-tailoring
  A. Transformation   B. Adoption            C. Microsoft AI delivery      D. Assurance and operations
  ai-strategy         copilot-adoption       m365-copilot   copilot-code   ai-architecture   security-privacy*
  opportunity-mgmt    champions              m365-agents    copilot-studio responsible-ai*   data-governance
  value-realisation   learning-and-skills    copilot-cowork ai-foundry     evaluation-quality* platform-governance
  programme-mgmt      change-and-comms       automation     ai-engineering ai-operations     design-authority*
                      knowledge-management                                  (* reviewer-class: may block)
```

`catalogue/departments.toml` holds all 27 departments with layer, status (`active` or `planned`), build phase, lead role
and the brief's candidate skills.

## Units

| Unit | Where | Role |
|---|---|---|
| Skill | `departments/<id>/skills/<skill>/SKILL.md` or `reviewers/<id>/...` | Practitioner judgement for one decision or artefact, with explicit triggers, inputs, outputs, gates and failure modes. |
| Department | `departments/<id>/` | An installable plugin grouping related skills under one accountable lead role. |
| Reviewer-class department | `reviewers/<id>/` | A department whose findings can be **blocking**. |
| Programme | `programmes/<id>/programme.yaml` | Orchestrates skills into a complete outcome: lifecycle stages, artefacts (skill + template + depth per edition) and reviewer gates. Programmes reference skills; they never duplicate content. |
| Edition | `editions/<id>/edition.yaml` | Starter, Scale or Enterprise overlay: CoE form, Champions form, governance form, default depth. |
| Archetype | `archetypes/<id>/archetype.yaml` | Explorer to AI Enterprise: state and output emphasis. |
| Template | `templates/<id>.md` | A human-usable document an artefact is written on. |
| Source record | `sources/*.toml` | A structured authority for volatile facts, with volatility, review interval and usage class. |

## Profile flow

```
organisation profile (YAML, schema: profiles/schema.json)
   -> organisation-tailoring:ai-profile-intake        validate, ask only for what is missing, mark unknowns
   -> organisation-tailoring:edition-and-archetype    rules in data/tailoring-rules.yaml (scripts/tailor.py)
   -> programmes/ai-transformation                    includes discovery, adoption, champions, ai-coe,
                                                      agent-factory (when agents are emerging), governance
   -> artefacts at edition depth, each owned by a skill and written on a template
   -> reviewer gates (blocking, cannot be skipped) from the risk tier stated in the programme
   -> organisation-tailoring:ownership-map, transformation-pack
```

`scripts/tailor.py` makes the decisions deterministic and testable: every recommendation names the rule that produced
it. The skills write the documents; the script decides what is in the pack. Golden plans for each fictional sample sit
in `evaluations/golden/` and `evaluations/acceptance.yaml` asserts the v1 acceptance behaviour, including that a
40-person organisation receives a materially lighter pack than a 600-person one.

## Reviewer semantics

A gate in a programme names a reviewer-class department, the lifecycle stage, the risk tier from which it applies and
`blocking: true, skippable: false`. `scripts/check-programmes.py` refuses any gate that could be skipped, and any
programme producing agent artefacts without a `security-privacy` gate. Gates for reviewer departments that are still
planned are carried as a **contract only**: the plan reports them as such and the CoE lead records the review until the
department is built. Reviewer tests in `tests/reviewers/` hold cases that must block and cases that must not.

## Generators

| Script | Emits |
|---|---|
| `build-bundles.py` | Copies of the profile schema, rules, catalogue, programmes and templates into the tailoring skills' `references/` |
| `build-port.py` | Department `README.md` and `.claude-plugin/plugin.json`; `.claude-plugin/marketplace.json` |
| `build-sources.py` | Each skill's `references/sources.md`; the generated table in `SOURCES.md` |
| `build-catalogue.py` | `catalogue/catalogue.json`, `docs/CATALOGUE.md`, generated tables in `README.md` and `ROADMAP.md` |
| `build-cowork.py` | `cowork/plugins/copilotforge-<id>.zip` and `cowork/README.md` |
| `build-site.py` | The website's core pages in `site/` |
| `build-hosting.py` | The complete website in `dist/website/` and `dist/copilotforge-website.zip` for https://copilotforge.ai/ |
| `tailor.py` | A tailoring plan for a profile |

Every generator has `--check`, which `scripts/check-all.sh` runs, so generated files cannot drift from their sources.

## System boundaries

- No service: CopilotForge runs inside the user's AI runtime (Copilot Cowork first). Profiles and packs stay in the
  user's own storage; the repository stores only the schema and fictional samples.
- No client, employer or confidential material in the repository (`scripts/check-safety.py`).
- Separate from D365Forge (`scripts/check-separation.py`, decision D1 and D9).

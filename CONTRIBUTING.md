# Contributing

CopilotForge is maintained by Simon Foote. Suggestions, skill gaps and trigger failures are welcome as GitHub issues.

## Writing standards

- Follow [docs/STYLE-GUIDE.md](docs/STYLE-GUIDE.md): the skill anatomy, voice, accuracy, people and template rules.
- Original prose only, in UK English. No client, employer or confidential material, ever.
- Volatile product facts come from `sources/*.toml`, never from memory.
- Skills are named uniquely and never reuse a D365Forge name (decision D9).

## Process

1. Name the change's allowed write surfaces (see [COWORK.md](COWORK.md), section 7).
2. Make the change in source files only; never hand-edit generated files.
3. Run `bash scripts/build-all.sh` (Python 3.11+ and PyYAML: `pip install pyyaml`). It regenerates every generated
   file and runs every check; fix what it reports.
4. Record any change to architecture or conventions in [DECISIONS.md](DECISIONS.md).
5. Commit with an imperative message describing the change. While the project has a single maintainer, changes go
   directly to `main` (decision D4). When outside contributors join, changes will move to branches and pull requests.

## Definition of done for a skill (design brief 13.1)

- All required sections are complete with no placeholder text.
- Description and triggers are distinguishable from neighbouring skills.
- At least three positive trigger prompts and one negative prompt exist in `tests/triggers/`.
- Required inputs and generated outputs are explicit.
- Starter, Scale and Enterprise notes exist.
- Security, privacy, responsible AI, evaluation and value sections are complete, or marked not applicable with rationale.
- Version-specific product claims refer to catalogued sources.
- Hand-offs and reviewer gates resolve to valid departments or skills.
- `bash scripts/build-all.sh` passes.
- The maintainer approves the change; the skill stays `status: draft` until reviewed.

Contributions are accepted under the same terms: content under CC BY 4.0, code under MIT.

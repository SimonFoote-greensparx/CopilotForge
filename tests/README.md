# Tests

- `triggers/<department>.toml` - routing tests: at least three prompts that should load each skill and at least one
  near miss naming the skill that should win instead (`scripts/check-triggers.py`).
- `reviewers/<department>.yaml` - reviewer tests: submissions a reviewer-class department must block, and ones it must
  not, to prove gates are both effective and proportionate (`scripts/check-programmes.py`).

Structural checks run in CI. Behavioural runs of these prompts against an AI runtime are a phase 1 deliverable.

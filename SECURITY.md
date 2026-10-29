# Security

CopilotForge is a library of text skills, templates and scripts. It runs no service and stores no organisation data.

## Reporting a vulnerability

Report anything that could harm users (for example a skill instruction that could lead an AI runtime to expose data,
a script that executes untrusted input, or sensitive data committed by mistake) privately through GitHub's
**Report a vulnerability** feature on the repository's Security tab, rather than in a public issue. You will receive
an acknowledgement and a plan for a fix.

## Expectations

- Skills run as instructions to an AI. Read a skill before you upload it to your runtime.
- Never put real organisation profiles, credentials or personal data in the repository. Profiles belong in your own
  storage; `input/` and `output/` are git-ignored for local work.
- `scripts/check-safety.py` scans every change for credentials, personal contact data and restricted names.

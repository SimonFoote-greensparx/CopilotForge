#!/usr/bin/env bash
# Every check CI runs, in one local command: bash scripts/check-all.sh
# The workflow calls this same file, so local and CI checks cannot drift (design brief 13).
set -uo pipefail
cd "$(dirname "$0")/.."
fail=0
run() {
  printf '\n%s\n' "$1"; shift
  if "$@"; then :; else fail=1; printf '  FAILED\n'; fi
}
run "Structure: skill frontmatter and anatomy"          python3 scripts/validate-skills.py
run "Structure: references resolve"                     python3 scripts/check-refs.py
run "Routing: trigger suites"                           python3 scripts/check-triggers.py
run "Sources: records, authority and freshness"         python3 scripts/check-sources.py
run "Orchestration: programmes, editions, gates"        python3 scripts/check-programmes.py
run "Profiles, golden plans and acceptance scenarios"   python3 scripts/check-profiles.py
run "Content: templates"                                python3 scripts/check-templates.py
run "Content: UK English"                               python3 scripts/check-uk-english.py
run "Safety: credentials, personal and client data"     python3 scripts/check-safety.py
run "Separation from D365Forge"                         python3 scripts/check-separation.py
run "Generation: manifests and department READMEs"      python3 scripts/build-port.py --check
run "Generation: skill source files"                    python3 scripts/build-sources.py --check
run "Generation: catalogue, README and roadmap tables"  python3 scripts/build-catalogue.py --check
run "Generation: tailoring bundles"                     python3 scripts/build-bundles.py --check
run "Generation: Copilot Cowork packages"               python3 scripts/build-cowork.py --check
run "Generation: website pages"                        python3 scripts/build-site.py --check
run "Website: programme builder agrees with tailoring"  python3 scripts/check-programme-builder.py
run "Website: hosted build and link check"             python3 scripts/build-hosting.py --out dist/check-website --zip dist/check-website.zip
printf '\n'
if [ "$fail" -eq 0 ]; then printf 'All checks passed.\n'; else printf 'Checks failed.\n'; fi
exit "$fail"

#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

required=(
  "README.md"
  "lab/README.md"
  "lab/architecture-flow.md"
  "lab/prerequisites.md"
  "lab/implementation-steps.md"
  "lab/validation-checks.md"
  "lab/troubleshooting.md"
  "lab/cleanup.md"
  "lab/proof-of-execution.md"
)

mapfile -t modules < <(find . -maxdepth 1 -type d -name '[0-9][0-9]-*' | sed 's#^./##' | sort)

if [[ ${#modules[@]} -eq 0 ]]; then
  echo "ERROR: no numbered modules found"
  exit 1
fi

missing=0
for module in "${modules[@]}"; do
  for rel in "${required[@]}"; do
    if [[ ! -f "$module/$rel" ]]; then
      echo "MISSING: $module/$rel"
      missing=1
    fi
  done
done

if [[ $missing -ne 0 ]]; then
  echo "ERROR: missing required files in one or more modules"
  exit 1
fi

if rg -n "(:contentReference\[oaicite|[0-9]+)" --glob '*.md' >/tmp/citation_artifacts.txt; then
  echo "ERROR: unresolved citation artifacts found:"
  cat /tmp/citation_artifacts.txt
  exit 1
fi

echo "OK: ${#modules[@]} modules validated"
echo "OK: required files exist in every module"
echo "OK: no unresolved citation artifact tokens"

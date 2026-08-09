#! /usr/bin/env bash
set -euo pipefail

if [[ $# -gt 0 ]]; then
  echo "$1" > .python-version
  eval "$(mise hook-env --force)"
fi

mise test

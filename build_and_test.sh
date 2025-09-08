#! /usr/bin/env bash
set -euo pipefail

if ! command -v mise >/dev/null 2>&1; then
  echo "[error] 'mise' is required but not found on PATH. Install Mise: https://mise.jdx.dev/"
  exit 127
fi

mise task --quiet run build_and_test

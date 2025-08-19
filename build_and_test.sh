#! /usr/bin/env bash
set -euo pipefail

if ! command -v mise >/dev/null 2>&1; then
  echo "[error] 'mise' is required but not found on PATH. Install Mise: https://mise.jdx.dev/"
  exit 127
fi

mise settings add idiomatic_version_file_enable_tools python
mise task --quiet run install_python_deps
mise task --quiet run test ::: mypy ::: integration

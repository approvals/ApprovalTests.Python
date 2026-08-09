#! /usr/bin/env bash
set -euo pipefail

if ! command -v mise >/dev/null 2>&1; then
  echo "[error] 'mise' is required but not found on PATH. Install Mise: https://mise.jdx.dev/"
  exit 127
fi

if [[ -f .venv/pyvenv.cfg ]]; then
  wanted_version=$(<.python-version)
  venv_version=$(sed -n 's/^version_info = //p' .venv/pyvenv.cfg)
  if [[ "$venv_version" != "$wanted_version".* ]]; then
    echo "[info] Python version changed ($venv_version -> $wanted_version); removing .venv"
    rm -rf .venv
  fi
fi

mise install --quiet
mise task run build_and_test

#! /bin/bash
set -euo pipefail

mise task --quiet run install_python_deps
mise task --quiet run isort
mise task --quiet run black

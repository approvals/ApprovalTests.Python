#! /bin/bash
set -euo pipefail

mise task --quiet run isort
mise task --quiet run black

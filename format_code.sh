#! /bin/bash
set -euo pipefail

python -m pip install ruff
python -m ruff format

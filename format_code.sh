#! /bin/bash
set -euo pipefail

python -m pip install black
python -m black .

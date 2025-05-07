#! /bin/bash
set -euo pipefail

python -m pip install isort black
python -m isort .
python -m black .

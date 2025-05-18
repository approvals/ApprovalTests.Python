#! /usr/bin/env bash
set -euo pipefail

if command -v python &>/dev/null; then
    PYTHON=python
else
    PYTHON=python3
fi

if [ ! -d ".venv" ]; then
    $PYTHON -m venv .venv
fi
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
elif [ -f ".venv/Scripts/activate" ]; then
    source .venv/Scripts/activate
else
    echo "Could not find virtual environment activation script."
    exit 1
fi

python -m pip --disable-pip-version-check install tox
python -m tox -e py -- --junitxml=test-reports/report.xml
python -m tox -e mypy
python -m tox -e integration_tests

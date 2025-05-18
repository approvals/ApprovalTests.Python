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

LOG_FILE=$(mktemp -t approvaltests_run_tests.XXXXXX.log)

python -m pip --disable-pip-version-check install tox > "$LOG_FILE" 2>&1
if [ $? -eq 0 ]; then
    echo "✅ tox"
else
    echo "pip install tox: FAILED" && cat "$LOG_FILE" && rm -f "$LOG_FILE" && exit 1
fi

python -m tox -e py -- --junitxml=test-reports/report.xml > "$LOG_FILE" 2>&1
if [ $? -eq 0 ]; then
    echo "✅ test passed"
else
    echo "tox -e py: FAILED" && cat "$LOG_FILE" && rm -f "$LOG_FILE" && exit 1
fi

python -m tox -e mypy > "$LOG_FILE" 2>&1
if [ $? -eq 0 ]; then
    echo "✅ mypy"
else
    echo "tox -e mypy: FAILED" && cat "$LOG_FILE" && rm -f "$LOG_FILE" && exit 1
fi

python -m tox -e integration_tests > "$LOG_FILE" 2>&1
if [ $? -eq 0 ]; then
    echo "✅ integration tests"
else
    echo "tox -e integration_tests: FAILED" && cat "$LOG_FILE" && rm -f "$LOG_FILE" && exit 1
fi

rm -f "$LOG_FILE"

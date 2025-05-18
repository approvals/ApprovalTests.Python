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

run_step() {
    local display_name="$1"
    shift
    if "${@}" > "$LOG_FILE" 2>&1; then
        echo "✅ $display_name PASSED"
    else
        echo "❌ $display_name FAILED" && cat "$LOG_FILE" && rm -f "$LOG_FILE" && exit 1
    fi
}

run_step "install tox" python -m pip --disable-pip-version-check install tox
run_step "run unit tests" python -m tox -e py -- --junitxml=test-reports/report.xml
run_step "run mypy" python -m tox -e mypy
run_step "run integration tests" python -m tox -e integration_tests

rm -f "$LOG_FILE"

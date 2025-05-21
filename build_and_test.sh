#! /usr/bin/env bash
set -euo pipefail

command -v uv >/dev/null || { echo "Install uv. https://docs.astral.sh/uv/getting-started/installation/" >&2; exit 1; }


LOG_FILE=$(mktemp -t approvaltests_run_tests.XXXXXX.log)

run_tox() {
    local display_name="$1"
    shift
    if uv tool run tox -e ${@} > "$LOG_FILE" 2>&1; then
        echo "✅ $display_name PASSED"
    else
        echo "❌ $display_name FAILED" && cat "$LOG_FILE" && rm -f "$LOG_FILE" && exit 1
    fi
}

run_tox "run unit tests" py -- --junitxml=test-reports/report.xml
run_tox "run mypy" mypy
run_tox "run integration tests" integration_tests

rm -f "$LOG_FILE"


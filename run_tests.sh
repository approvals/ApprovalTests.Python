#! /usr/bin/env bash
set -euo pipefail

if command -v python &>/dev/null; then
    PYTHON=python
else
    PYTHON=python3
fi

$PYTHON -m pip --disable-pip-version-check install tox
$PYTHON -m tox -e py -- --junitxml=test-reports/report.xml
$PYTHON -m tox -e mypy
$PYTHON -m tox -e integration_tests

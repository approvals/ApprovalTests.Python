#! /usr/bin/env bash
set -euo pipefail

PYTHON=python  # Change to 'py -3.13' to use Python 3.13
# PYTHON='py -3.13'

$PYTHON -m pip --disable-pip-version-check install tox
$PYTHON -m tox -e py -- --junitxml=test-reports/report.xml
$PYTHON -m tox -e integration_tests

#! /usr/bin/env bash
set -euo pipefail

python -m pip --disable-pip-version-check install tox
tox -e py -- --junitxml=test-reports/report.xml
tox -e test__py_typed_files_exist

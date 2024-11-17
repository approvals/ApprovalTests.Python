#! /usr/bin/env bash
set -euo pipefail

python3 -m pip --disable-pip-version-check install tox
tox -e py
tox -e test__py_typed_files_exist

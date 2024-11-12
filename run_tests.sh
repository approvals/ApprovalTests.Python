#! /usr/bin/env bash
set -euo pipefail

python3 -m pip --disable-pip-version-check install tox
tox -e py && tox -e type

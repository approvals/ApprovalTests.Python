#! /bin/bash
set -euo pipefail

./tidy_code.sh
./build_and_test.sh

#! /bin/bash
set -euo pipefail

./format_code.sh
./build_and_test.sh

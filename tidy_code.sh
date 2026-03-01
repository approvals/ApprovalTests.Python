#! /bin/bash
set -euo pipefail

mise task --quiet run tidy_code
git add --renormalize .
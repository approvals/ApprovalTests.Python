---
name: repro-python-version
description: Reproduce a test or build failure on a specific Python version locally. Use when CI fails on one Python version, or when asked to test with a different Python.
---

# Reproduce on a Python version

1. Read the CI failure first (see the `read-ci-failure` skill) so you know what you are trying to reproduce.
2. Preview what a clean will delete, and tell the user if anything looks like their work:
   `git clean -xdn`
3. Clean and build with the target version. Passing a version writes `.python-version` and rebuilds `.venv`:
   ```
   git clean -xdffq
   ./build_and_test <version>   # e.g. 3.15
   ```
   Save the output to a file in the scratchpad; it is long.
4. Compare the local failure with the CI failure.
5. To run a single test quickly: `mise exec -- python -m pytest -q <path> -k <name>`
6. When done, restore the version: `git checkout .python-version` and clean and build again.


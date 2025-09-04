# ApprovalTests.Python - Claude Development Notes

- Use `./build_and_test.sh` for full build (this includes mypy and lint)

## Code Style

- Prefer `Path` over strings
- Prefer `map`, `any`, `all`, etc. over `for` loops
- Follow existing patterns in the codebase
- Prefer complete function names and type hints over docstrings

## Approval Tests

- Use `APPROVALTESTS_CONFIG='{"reporter":"PythonNativeReporter"}' uv run python -m pytest tests/path/to/test.py -v -s` to see approval test diffs directly in the terminal

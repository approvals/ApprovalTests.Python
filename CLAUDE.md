# ApprovalTests.Python - Claude Development Notes

## Running Tests & Type Checking

- Use `./build_and_test.sh` for full build (this includes mypy)

## MyPy Configuration

- Currently enabling strict mode rules incrementally
- Enabled: `disallow_any_generics` (completed)
- Still disabled: `no_implicit_reexport`, `disallow_subclassing_any`
- See `mypy.ini` for current configuration

## Code Style

- Use `uv tool run ruff check .` for linting
- Use `uv tool run black .` for formatting
- Follow existing patterns in the codebase
- Prefer complete function names and type hints over docstrings

## Approval Tests

- Use `APPROVALTESTS_CONFIG='{"reporter":"PythonNativeReporter"}' uv run python -m pytest tests/path/to/test.py -v -s` to see approval test diffs directly in the terminal

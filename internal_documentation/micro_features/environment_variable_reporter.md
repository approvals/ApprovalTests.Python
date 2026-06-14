# `EnvironmentVariableReporter`

## Sample Use Case

```bash
# Use Visual Studio Code as the diff tool without changing any test code
export APPROVAL_TESTS_USE_REPORTER=approvaltests.reporters.diff_tools.ReportWithVisualStudioCode
python -m pytest
```

Selects and delegates to a reporter based on the `APPROVAL_TESTS_USE_REPORTER` environment variable.

## Purpose

Allows users to configure their reporter without changing code — useful for CI environments, personal developer preferences, or switching reporters across test runs.

## Behavior

- If `APPROVAL_TESTS_USE_REPORTER` is not set or is empty, `report()` returns `False`.
- If the variable is set to a valid fully-qualified class name, that class is instantiated and its `report()` is called.
- If the class name does not exist, an exception is raised.

## Integration

- Implements the `Reporter` interface.
- Used as the default reporter so users can configure reporting via environment without code changes.

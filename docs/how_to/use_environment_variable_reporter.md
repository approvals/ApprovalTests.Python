# How to Use the Environment Variable Reporter

The `EnvironmentVariableReporter` lets you select a reporter without changing any test code, by setting the `APPROVAL_TESTS_USE_REPORTER` environment variable.

## Basic Usage

Set the environment variable to a fully-qualified class name before running your tests:

```bash
export APPROVAL_TESTS_USE_REPORTER=approvaltests.reporters.diff_tools.ReportWithVisualStudioCode
python -m pytest
```

On Windows:

```powershell
$env:APPROVAL_TESTS_USE_REPORTER = "approvaltests.reporters.diff_tools.ReportWithVisualStudioCode"
python -m pytest
```

## Use Cases

- **Personal preferences**: each developer uses their preferred diff tool without touching shared test code.
- **CI environments**: configure a CI-appropriate reporter (e.g. one that prints diffs to stdout) via an environment variable in the pipeline config.
- **Switching reporters across test runs**: toggle between reporters without editing code.
- **AI**: can use reporters suited to console output.

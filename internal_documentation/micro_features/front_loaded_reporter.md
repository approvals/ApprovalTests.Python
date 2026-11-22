# Front Loaded Reporter

Ported from the [ApprovalTests.Java docs](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/reference/FrontLoadedReporter.md).
Design notes: [front_loaded_reporters.md](../front_loaded_reporters.md).

## Purpose
Some environments (CI, an AI coding agent) should never open a diff tool, no matter which reporter a test asks for.
A front loaded reporter checks the environment first, and when it applies, it replaces every other reporter.

## How a reporter says it applies
As everywhere else in this library, a reporter returns `False` from `report` when it does not apply.
`EnvironmentVariableReporter` returns `False` when `APPROVAL_TESTS_USE_REPORTER` is not set,
and `AiCodingAgentReporter` returns `False` when no agent is detected.

## DefaultFrontLoadedReporter
```python
FirstWorkingReporter(
    EnvironmentVariableReporter(),
    AiCodingAgentReporter(),
)
```

## Configuration
Next to `set_default_reporter` / `get_default_reporter`, using the same thread-local storage:

- `set_front_loaded_reporter(reporter)`; `None` turns front loading off.
- `get_front_loaded_reporter()` returns the set reporter, or `DefaultFrontLoadedReporter` when none has been set.

## Behavior
`get_reporter(reporter)` returns `FirstWorkingReporter(front_loaded, reporter or default_reporter)`,
or just `reporter or default_reporter` when the front loaded reporter is `None`.
So when the front loaded reporter returns `True`, it replaces the normal reporter, even one passed in.

## Change to the default reporter
The default reporter becomes `DiffReporter()`.
`EnvironmentVariableReporter` is no longer in it, because the front loaded reporter already checks it.

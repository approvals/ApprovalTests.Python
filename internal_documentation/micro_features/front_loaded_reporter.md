# Front Loaded Reporter

Ported from the [ApprovalTests.Java docs](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/reference/FrontLoadedReporter.md).
Design notes: [front_loaded_reporters.md](../front_loaded_reporters.md).

## Purpose
Some environments (CI, an AI coding agent) should never open a diff tool, no matter which reporter a test asks for.
A front loaded reporter checks the environment first, and when it applies, it replaces every other reporter.

## EnvironmentAwareReporter
A new base class:

```python
class EnvironmentAwareReporter(Reporter):
    def is_working_in_this_environment(self, for_file: str) -> bool: ...
```

| Reporter | Working in this environment when |
| - | - |
| `EnvironmentVariableReporter` | `APPROVAL_TESTS_USE_REPORTER` is set |
| `AiCodingAgentReporter` | `AiCodingAgentReporter.is_agent_detected()` |
| `FirstWorkingReporter` | any of its reporters that is environment aware is working |

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
`get_reporter(reporter)`:
1. If the front loaded reporter is working in this environment, return it, even when a reporter was passed in.
2. Otherwise return the passed in reporter, or the default reporter.

## Change to the default reporter
The default reporter becomes `DiffReporter()`.
`EnvironmentVariableReporter` is no longer in it, because the front loaded reporter already checks it.

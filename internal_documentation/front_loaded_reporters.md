# Front Loaded Reporters

Translated from the Java docs: [FrontLoadedReporter.md](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/reference/FrontLoadedReporter.md)

> **Status in Python:** not implemented yet. This describes the Java design, written as it would look in Python.
> Today, `EnvironmentVariableReporter` is only the first entry in the default `FirstWorkingReporter` chain
> (see `approvaltests/reporters/default_reporter_factory.py`), and `AiCodingAgentReporter` is not checked by default.

## What and Why

Front loaded reporters let you block all normal reporting depending on the environment.
This is useful when running on a CI machine, where you don't want a diff tool to open.

The `FrontLoadedReporter` is the mechanism for this.
Front loaded reporters are environment-aware: they know whether they are in the right environment.
If they are, they override every other reporter, including one passed in with `options.with_reporter(...)`.
If not, they pass through and the normal reporter runs.

```python
class EnvironmentAwareReporter(Reporter):
    def is_working_in_this_environment(self, for_file: str) -> bool: ...
```

## The `DefaultFrontLoadedReporter`

In Java, the default front loaded reporter checks these, in order:

```python
FirstWorkingReporter(
    EnvironmentVariableReporter(),
    AiCodingAgentReporter(),
)
```

Java also includes `PitReporter` (for the PIT mutation tester). Python has no equivalent, so it is left out.

## Links

* Java: [Customize using package settings](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/reference/PackageSettings.md)
* Java: [AI Coding Agent Reporter](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/reference/AiCodingAgentReporter.md)

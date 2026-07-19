# IntelliJ Reporter

## Purpose
Automatically detects a running JetBrains IDE process and uses it to display diffs when an approval test fails — no manual configuration required.

## Behavior
1. **Scans running processes**: Uses `psutil` (an optional dependency, imported lazily) to list all running OS processes. Both the process's `exe` and `cmdline` are collected as candidate paths — on Mac and Linux it's common for one of the two to raise `AccessDenied` (e.g. for an IDE launched via a shell script) while the other still succeeds, so a process is only skipped entirely if both fail.
2. **Identifies JetBrains IDEs**: Looks for known keywords in process paths (`idea`, `pycharm`, `webstorm`, `phpstorm`, `goland`, `rider`, `clion`, `rubymine`, `appcode`, `datagrip`)
3. **Verifies it's the main executable**: Checks that the path ends with `macos/<keyword>` or contains `bin/<keyword>` or `bin\<keyword>` to avoid matching helper processes
4. **Returns the path**: Returns the first matching executable path, or `""` if none found
5. **Falls back gracefully**: If no JetBrains IDE is running (or `psutil` isn't installed), the reporter path is empty and `GenericDiffReporter` will report itself as unavailable

## Usage Example
```py
verify("text", options=Options().with_reporter(ReportWithIntellijTools()))
```

See [Use the IntelliJ reporter](/docs/how_to/use_the_intellij_reporter.md).

## Supported IDEs
- IntelliJ IDEA (`idea`)
- PyCharm (`pycharm`)
- WebStorm (`webstorm`)
- PhpStorm (`phpstorm`)
- GoLand (`goland`)
- Rider (`rider`)
- CLion (`clion`)
- RubyMine (`rubymine`)
- AppCode (`appcode`)
- DataGrip (`datagrip`)

## Diff Command
Uses `diff %s %s` with the detected IDE executable, passing the received file and approved file as arguments.

## Integration
`ReportWithIntellijTools` is first in `DiffReporter`'s auto-detection chain, ahead of the configured/OS-specific diff tools, since a running IDE is a strong, zero-config signal. `find_jetbrains_ides(paths: list[str]) -> str` is public and testable independently of running processes.

## Dependencies
Requires the optional `psutil` package (see `requirements.prod.extras.txt`). Importing it is deferred to `get_running_process_paths()` so the base package still installs and imports without it.

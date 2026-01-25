# How the Default Reporter Works

``` mermaid
flowchart TD
    verify[verify called] --> options{Options has reporter?}
    options -->|Yes| use_custom[Use custom reporter]
    options -->|No| get_default[get_default_reporter]
    get_default --> check_set{DEFAULT_REPORTER set?}
    check_set -->|Yes| use_set[Use set reporter]
    check_set -->|No| diff_reporter[Create DiffReporter]
    
    diff_reporter --> first_working[FirstWorkingReporter]
    first_working --> json_reporters[reporters.json reporters]
    json_reporters --> hardcoded[Hardcoded reporters]
    
    subgraph try_reporters[Try each reporter in order]
        json_reporters
        hardcoded
    end
    
    first_working --> is_working{is_working?}
    is_working -->|No| next[Try next reporter]
    next --> is_working
    is_working -->|Yes| report[Launch diff tool]
```

## Overview

When a test fails, ApprovalTests needs to show you the difference between the received and approved files. The **default reporter** determines which diff tool to use.

## Reporter Selection Order

`DiffReporter` extends `FirstWorkingReporter` and tries reporters in this order:

1. **reporters.json** - All reporters defined in `reporters.json` (BeyondCompare, Araxis, kdiff3, meld, etc.)
2. **VSCode** - `ReportWithVSCode`, `ReportWithVSCodeMacOS`
3. **Windows diff** - `ReportWithDiffToolOnWindows`
4. **Command line diff** - `ReportWithDiffCommandLine`
5. **Python native** - `PythonNativeReporter` (fallback that prints to console)

The first reporter where `is_working()` returns `True` is used.

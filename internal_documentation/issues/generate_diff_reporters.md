# Generating Diff Reporter Classes from CSV

This document describes how to generate diff reporter classes for any language from the `diff_reporters.csv` file.

## CSV Structure

| Column | Description |
|--------|-------------|
| `name` | Reporter identifier (e.g., `BEYOND_COMPARE_4`, `KDIFF3`) |
| `path` | Executable path. May contain `{ProgramFiles}` placeholder for Windows |
| `arguments` | Optional command-line arguments (e.g., `--nosplash %s %s`, `-d %s %s`) |
| `file_types` | `TEXT`, `IMAGE`, or `TEXT_AND_IMAGE` |
| `os` | `Mac`, `Windows`, or `Linux` |
| `group_name` | Optional grouping for aggregating reporters (e.g., `BEYOND_COMPARE`) |

## Generation Steps

### 1. Parse the CSV
Read all rows from `diff_reporters.csv`, skipping the header.

### 2. For Each Row, Generate a Class

**Class naming:**
- Convert `name` from `SCREAMING_SNAKE_CASE` to `PascalCase`
- Append the `os` value
- Prefix with language-appropriate convention (e.g., `ReportWith` for Python)
- Example: `BEYOND_COMPARE_4` + `Windows` → `ReportWithBeyondCompare4Windows`

**Path handling:**
- Normalize path separators (e.g., `\` → `/`)
- Preserve `{ProgramFiles}` placeholder for runtime expansion

**Arguments handling:**
- Parse the `arguments` string into individual tokens
- Remove `%s` placeholders (these represent received/approved file paths)
- Keep flags like `--nosplash`, `-d`, `-m`
- Example: `--nosplash %s %s` → `["--nosplash"]`

### 3. Output Structure

Each class should:
1. Extend/implement the base diff reporter type
2. Set the reporter name (typically the class name)
3. Set the executable path
4. Optionally set extra arguments if present

### 4. Generate Per-OS Aggregator Classes

Generate a `ReportWithDiffToolOn{OS}` class for each OS (Mac, Windows, Linux):
- Collect all reporter classes for that OS
- Create a `FirstWorkingReporter` subclass that tries each reporter in sequence
- Add early return on reporting if not on the os.
- Example: `ReportWithDiffToolOnMac` tries all Mac reporters in order

These per-OS reporters allow users to get a working diff tool without specifying which one, automatically finding the first available tool on their system.

### 5. Generate Group Aggregator Classes

For rows sharing the same non-empty `group_name`:
- Convert `group_name` from `SCREAMING_SNAKE_CASE` to `PascalCase`
- Create a `FirstWorkingReporter` subclass named `ReportWith{GroupPascalCase}`
- Include all reporters in the group, in CSV order
- No OS guard is needed — individual reporters already fail gracefully when the executable is not found
- Example: `ReportWithBeyondCompare` tries `ReportWithBeyondCompareMac`, `ReportWithBeyondCompare3Windows`, `ReportWithBeyondCompare4Windows`, `ReportWithBeyondCompare5Windows`

These group reporters allow users to specify a tool by name (e.g., `ReportWithKdiff3`) without worrying about which OS or version they are on.

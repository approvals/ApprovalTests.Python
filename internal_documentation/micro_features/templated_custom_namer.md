# `TemplatedCustomNamer` — full template field support

## Sample Use Case

```python
namer = TemplatedCustomNamer(
    "{test_source_directory}/{approvals_subdirectory}/{approved_or_received}/"
    "{test_file_name}.{test_case_name}.{file_extension}"
)
```

Adds support for every field listed in `TemplateFields`, including the two that
were previously marked as a `TODO` ("not supported yet"):
`relative_test_source_directory` and `approvals_subdirectory`.

## Purpose

Lets a template reference any of the documented `TemplateFields`, so users can
compose approval file names from all the available parts rather than only the
subset that happened to be wired up.

## Template Fields

| Field | Expands to |
| --- | --- |
| `approved_or_received` | `"approved"` or `"received"` |
| `test_file_name` | the test file/class name |
| `test_case_name` | the test method/function name |
| `file_extension` | the extension without the dot, e.g. `txt` |
| `test_source_directory` | the absolute directory containing the test |
| `relative_test_source_directory` | the test source directory relative to the current working directory |
| `approvals_subdirectory` | the configured `subdirectory` from `approvaltests_config.json` (empty if unset) |

## The Default Namer as a Template

The default `StackFrameNamer` expressed as a template would be:

```python
"{test_source_directory}/{approvals_subdirectory}/"
"{test_file_name}.{test_case_name}.{approved_or_received}.{file_extension}"
```

## Behavior

- `{relative_test_source_directory}` is the relative-path counterpart of the
  existing absolute `{test_source_directory}` field.
- `{approvals_subdirectory}` reads the same `subdirectory` configuration value
  that `NamerBase.get_basename()` uses; it is empty when no config is present.
- Template Paths are written using forward slashes; these are handled appropriately regardless of OS

## Integration

- Implemented in `TemplatedCustomNamer.format_filename` by adding the remaining
  fields to the `format_map` dictionary.
- Removes the "not supported yet" `TODO` comment from `TemplateFields`, since all
  fields are now supported.

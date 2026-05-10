# Code Style

- Prefer `Path` over strings
- Prefer `map`, `any`, `all`, etc. over `for` loops
- Use `platform.system()` to check the OS
- Follow existing patterns in the codebase
- Prefer complete function names and type hints over docstrings
- For temporary directories use this pattern:
```python
with tempfile.TemporaryDirectory() as _temporary_directory:
    temporary_directory = pathlib.Path(_temporary_directory)
```

## Multiline Strings

For Readability, Use `approval_utilities.utilities.multiline_string_utils.remove_indentation_from()` with triple quotes:

```python
message = remove_indentation_from(f"""
    First line of the message with {variable}.
    Second paragraph with proper indentation.
    Final line.
    """)
```

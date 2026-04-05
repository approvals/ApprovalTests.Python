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

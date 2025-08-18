# Inline Approvals Whitespace

How inline approvals handles whitespace in docstrings and verified strings, including leading whitespace, trailing whitespace, and blank lines.

## Behavior
1. **Leading whitespace (preceding spaces)**
   - Python < 3.13: Docstrings preserve preceding indentation. Inline approvals can compare values that begin with spaces. A helper marker and option can be used to make this explicit.
   - Python ≥ 3.13: `__doc__` strips preceding whitespace automatically. To compare content that originally had leading spaces, strip the actual value (e.g., with `lstrip()`) or account for it in your expected text.

2. **Trailing whitespace**
   - Trailing spaces are preserved and must match exactly in both the docstring expectation and the verified value.
   - Editors may remove trailing spaces on save. Disable that if you want to test them.

3. **Blank lines**
   - Blank lines (including multiple in a row) are preserved and must match exactly.


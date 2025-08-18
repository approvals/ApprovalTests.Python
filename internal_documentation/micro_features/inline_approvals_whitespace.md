# Inline Approvals Whitespace

How inline approvals handles whitespace in docstrings and verified strings, including leading whitespace, trailing whitespace, and blank lines.

## Behavior
1. **Leading whitespace**
   - On failure, if the input has preceding whitespace, inline approvals injects extra text in the actual output to preserve that whitespace in Python both pre and post 3.13:
    ```python
    """
    <<approvaltests:preserve-leading-whitespace>>
        {actual user result here}
    """
    ```

2. **Trailing whitespace**
   - Trailing spaces are preserved and must match exactly in both the docstring expectation and the verified value.
   - Editors may remove trailing spaces on save. Disable that if you want to test them.

3. **Blank lines**
   - Blank lines (including multiple in a row) are preserved and must match exactly.

## Special markers

If the first line is `<<approvaltests:preserve-leading-whitespace>>`, then remove it before verifying. This is only  true if it's the first line.


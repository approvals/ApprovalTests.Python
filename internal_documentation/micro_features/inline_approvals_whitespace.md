# Inline Approvals Whitespace

How inline approvals handles whitespace in docstrings and verified strings, including leading whitespace, trailing whitespace, and blank lines.

## Behavior
1. **Leading whitespace**
   - On failure, if the input has preceding whitespace on everyline, inline approvals injects extra text in the actual output to preserve that whitespace in Python both pre and post 3.13:
    ```python
    """
    <<approvaltests:preserve-leading-whitespace>>
        {actual user result here}
    """
    ```

2. **Trailing whitespace**
   - Trailing spaces are preserved and must match exactly in both the docstring expectation and the verified value.
   - Editors may remove trailing spaces on save. Disable that if you want to test them.
   - If any line has trailing whitespace the reporter appends a warning on the same line as the closing triple quotes:
   ```python
   """
   your expected content here    
   """  # Warning: Editors may remove trailing spaces, causing this test to fail
   ```

3. **Blank lines**
   - Blank lines (including multiple in a row) are preserved and must match exactly.

4. Escape characters
   Backslashes are special in docstrings. So the reporter will escape them with another backslash.

5. Control characters
   If a control character is in the string, we want to represent it explicitly. For example `\u200f`.

   The control characters we care about are:
   - `\u200f` (right-to-left marker)
   - `\0` (null)
  - Vertical tab (\v, 0x0B)
  - Form feed (\f, 0x0C)
  - Escape (\x1b, 0x1B)
  - Right-to-Left Override (RLO, U+202E) - Already being tested
  - Left-to-Right Override (LRO, U+202D)
  - Right-to-Left Mark (RLM, U+200F)
  - Left-to-Right Mark (LRM, U+200E)
  - Pop Directional Formatting (PDF, U+202C)
  - Zero-Width Space (ZWSP, U+200B)
  - Zero-Width Non-Joiner (ZWNJ, U+200C)
  - Zero-Width Joiner (ZWJ, U+200D)
  - Non-breaking space (NBSP, U+00A0)
  - Byte Order Mark (BOM, U+FEFF)
  - Backspace (\b, 0x08)
  - Delete (DEL, 0x7F)
  - Line Separator (U+2028)
  - Paragraph Separator (U+2029)


## Special markers

If the first line is `<<approvaltests:preserve-leading-whitespace>>`, then remove it before verifying. This is only  true if it's the first line.


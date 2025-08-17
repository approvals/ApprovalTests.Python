# Code Style

## Multiline Strings

For Readability, Use `approval_utilities.utilities.multiline_string_utils.remove_indentation_from()` with triple quotes:

```python
message = remove_indentation_from(f"""
    First line of the message with {variable}.
    Second paragraph with proper indentation.
    Final line.
    """)
```

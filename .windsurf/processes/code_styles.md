# Code Style

## Multiline Strings

For Readability, Use `textwrap.dedent()` with triple quotes and a leading backslash escape:

```python
message = textwrap.dedent(f"""\
    First line of the message with {variable}.
    Second paragraph with proper indentation.
    Final line.
    """)
```

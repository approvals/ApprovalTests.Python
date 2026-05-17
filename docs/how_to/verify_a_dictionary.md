# How to verify a dictionary

## Problem

When you call `verify(my_dict)`, the output is a single-line string representation:

```
{'k1': 'v1', 'k2': 'v2'}
```

This is hard to read, and when values change, the diff shows the entire dict on one line.

## Solution

Use `verify_as_json()` instead. It formats the dictionary with one key per line, making it easier to read and producing cleaner diffs when values change.

<!-- snippet: verify_dict_example -->
<a id='snippet-verify_dict_example'></a>
```py
def test_verify_dict() -> None:
    """
    {
        "k1": "v1",
        "k2": "v2"
    }
    """
    d = {"k1": "v1", "k2": "v2"}
    verify_as_json(d, options=Options().inline())
```
<sup><a href='/tests/test_inline_approvals.py#L355-L367' title='Snippet source file'>snippet source</a> | <a href='#snippet-verify_dict_example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

# Options

All `verify()` methods take an optional `options` parameter to configure reporters, scrubbers, file extensions, etc. See the [Options diagram](https://raw.githack.com/approvals/ApprovalTests.Python/main/docs/images/options_diagram.html) for more details.

Chain the options you need onto `Options()`:

<!-- snippet: options_example -->
<a id='snippet-options_example'></a>
```py
verify(
    "Hello, World!",
    options=Options()
    .with_scrubber(lambda text: text.replace("World", "Approvals"))
    .for_file.with_extension(".md"),
)
```
<sup><a href='/tests/test_options.py#L223-L230' title='Snippet source file'>snippet source</a> | <a href='#snippet-options_example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## Inline Approvals

### Known Issues

- Pycharm automatically removes trailing whitespace, which can cause the approval file to be different from the actual output.
  - To disable this behavior go to:
  - File -> Settings -> Editor -> General -> On Save -> [ ] Remove trailing spaces

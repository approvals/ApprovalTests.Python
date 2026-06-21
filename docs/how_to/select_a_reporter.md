### Selecting a Reporter

All `verify...()` functions take an optional `options` parameter that can configure reporters (as well as many other aspects).

ApprovalTests.Python comes with a few reporters configured, supporting Linux, Mac OSX, and Windows.

In the example shown below, we pass in an `options` with a reporter we're selecting directly:

<!-- snippet: select_reporter_from_class -->
<a id='snippet-select_reporter_from_class'></a>
```py
class TestSelectReporterFromClass(unittest.TestCase):
    def test_simple(self):
        verify("Hello", options=Options().with_reporter(ReportWithBeyondCompare()))
```
<sup><a href='/tests/samples/test_getting_started.py#L8-L14' title='Snippet source file'>snippet source</a> | <a href='#snippet-select_reporter_from_class' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

For more about reporters see [intro to reporters](docs\tutorial\intro-to-reporters.md). Many of the
`ReportWith...` classes (such as `ReportWithBeyondCompare`) automatically pick
the first matching diff tool installed on your system.

For more on reporters, including how to write your own, see
[Create a custom reporter](/docs/how_to/create_a_custom_reporter.md).

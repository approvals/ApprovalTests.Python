# How to Use a Templated Custom Namer

By default ApprovalTests names your approved/received files based on the test
file, the test case, and the directory the test lives in. When you need a
different layout — for example to place approvals in a custom directory or to
change the order of the parts — you can use a `TemplatedCustomNamer` and supply
your own template.

## Basic Usage

Create a `TemplatedCustomNamer` with a template string and pass it to the namer
option:

<!-- snippet: templated_custom_namer_example -->
<a id='snippet-templated_custom_namer_example'></a>
```py
namer = TemplatedCustomNamer(
    "{test_source_directory}/{approvals_subdirectory}/{approved_or_received}/"
    "{test_file_name}.{test_case_name}.{file_extension}"
)
verify("Hello", options=Options().with_namer(namer))
```
<sup><a href='/tests/namers/test_templated_namer.py#L12-L18' title='Snippet source file'>snippet source</a> | <a href='#snippet-templated_custom_namer_example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

Template paths are written using forward slashes; these are handled
appropriately regardless of operating system.

## Template Fields

The available template fields are:

<!-- include: test_templated_namer.test_template_fields.approved.md -->
| template | usage |
| --- | --- |
| approvals_subdirectory | {approvals_subdirectory} |
| approved_or_received | {approved_or_received} |
| file_extension | {file_extension} |
| relative_test_source_directory | {relative_test_source_directory} |
| test_case_name | {test_case_name} |
| test_file_name | {test_file_name} |
| test_source_directory | {test_source_directory} |
<!-- endInclude -->

Referencing a field that is not in this list raises a `KeyError`.

This mirrors the `TemplatedCustomNamer` in ApprovalTests.cpp; see its
[Namers documentation](https://github.com/approvals/ApprovalTests.cpp/blob/master/doc/Namers.md#templatedcustomnamer).

## The Default Namer as a Template

The default `StackFrameNamer` expressed as a template would be:

```python
"{test_source_directory}/{approvals_subdirectory}/"
"{test_file_name}.{test_case_name}.{approved_or_received}.{file_extension}"
```

## Setting the Extension

You can override the file extension on the namer:

```python
namer = TemplatedCustomNamer(
    "{test_source_directory}/{approved_or_received}/"
    "{test_file_name}.{test_case_name}.{file_extension}"
)
namer.set_extension(".json")
```

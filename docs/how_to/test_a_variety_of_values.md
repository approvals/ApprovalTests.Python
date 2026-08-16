<a id="top"></a>

# How to Test a Variety of Values for One Input

<!-- toc -->
## Contents

  * [When to use verify_all](#when-to-use-verify_all)
  * [Steps](#steps)
  * [Tables](#tables)<!-- endToc -->

## When to use verify_all

When you want to test a lot of variations for a single input value.

If you have more than one parameter that you want to vary, check out [How to Test Combinations Inputs](test_combinations_of_inputs.md#top).

## Steps

1. Copy this starter text.

<!-- snippet: verify_all_starting_point -->
<a id='snippet-verify_all_starting_point'></a>
```py
inputs = ["input.value1", "input.value2"]
approvals.verify_all("TITLE", inputs, lambda s: f"placeholder {s}")
```
<sup><a href='/tests/test_list.py#L29-L32' title='Snippet source file'>snippet source</a> | <a href='#snippet-verify_all_starting_point' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

2. Modify the input container for your chosen values.
3. Run it, and make sure that you have your inputs wired up correctly.

If they are wired up correctly, you will see a file that looks like this: the lambda is responsible for both the execution and the formatting of the result.

<!-- snippet: TestList.test_starting_snippet.approved.txt -->
<a id='snippet-TestList.test_starting_snippet.approved.txt'></a>
```txt
TITLE

placeholder input.value1
placeholder input.value2
```
<sup><a href='/tests/approved_files/TestList.test_starting_snippet.approved.txt#L1-L4' title='Snippet source file'>snippet source</a> | <a href='#snippet-TestList.test_starting_snippet.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

4. Replace the "placeholder" with a call to the functionality that you want to test.
5. Change the TITLE to something meaningful
6. Run it, and approve the output.

## Tables

Another way to test a variety of inputs is to use a `MarkdownTable`.
Here's an example:

<!-- snippet: markdown_table_example -->
<a id='snippet-markdown_table_example'></a>
```py
inputs = ["verify json", "verify all", "verify parameters", "verify as json"]
table = MarkdownTable.with_headers(
    "Input", "Camel Case", "Snake Case", "Kebab Case"
)
table.add_rows_for_inputs(inputs, to_camel_case, to_snake_case, to_kebab_case)
verify(table)
```
<sup><a href='/tests/utilities/test_markdown_table.py#L6-L13' title='Snippet source file'>snippet source</a> | <a href='#snippet-markdown_table_example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

which will produce:

<!-- include: test_markdown_table.test_markdown_table.approved.md -->
| Input | Camel Case | Snake Case | Kebab Case |
| --- | --- | --- | --- |
| verify json | verifyJson | verify_json | verify-json |
| verify all | verifyAll | verify_all | verify-all |
| verify parameters | verifyParameters | verify_parameters | verify-parameters |
| verify as json | verifyAsJson | verify_as_json | verify-as-json |
<!-- endInclude -->

---

[Back to User Guide](../README.md#top)

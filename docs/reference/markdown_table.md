# Markdown Tables

Another way to test a variety of inputs is to use a `MarkdownTable`.
This works particularly well when you want to try the same set of inputs against multiple functions.
Here's an example:

<!-- snippet: markdown_table_example -->
<a id='snippet-markdown_table_example'></a>
```java
String[] inputs = {"verify json", "verify all", "verify parameters", "verify as json"};
MarkdownTable table = MarkdownTable.withHeaders("Input", "Camel Case", "Snake Case", "Kebab Case");
table.addRowsForInputs(inputs, this::toCamelCase, this::toSnakeCase, this::toKebabCase);
Approvals.verify(table);
```
<sup><a href='/approvaltests-tests/src/test/java/org/approvaltests/TableTest.java#L19-L24' title='Snippet source file'>snippet source</a> | <a href='#snippet-markdown_table_example' title='Start of snippet'>anchor</a></sup>
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


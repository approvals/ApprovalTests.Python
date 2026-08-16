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

snippet: verify_all_starting_point

2. Modify the input container for your chosen values.
3. Run it, and make sure that you have your inputs wired up correctly.

If they are wired up correctly, you will see a file that looks like this: the lambda is responsible for both the execution and the formatting of the result.

snippet: TestList.test_starting_snippet.approved.txt

4. Replace the "placeholder" with a call to the functionality that you want to test.
5. Change the TITLE to something meaningful
6. Run it, and approve the output.

## Tables

Another way to test a variety of inputs is to use a `MarkdownTable`.
Here's an example:

snippet: markdown_table_example

which will produce:

include: test_markdown_table.test_markdown_table.approved.md

---

[Back to User Guide](../README.md#top)

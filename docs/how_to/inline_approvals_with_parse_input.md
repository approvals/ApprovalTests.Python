# How to have tight feedback loops with inline approvals and parse_input

<!-- toc -->
## Contents

  * [Problem](#problem)
  * [Solution](#solution)
  * [Handling 1 Parameter](#handling-1-parameter)
    * [Scenario - Counting Vowels](#scenario---counting-vowels)
    * [Step 1: Write the Test](#step-1-write-the-test)
    * [Step 2: Run the Test](#step-2-run-the-test)
    * [Step 3: Implement and rerun](#step-3-implement-and-rerun)
    * [Step 4: Commit](#step-4-commit)
  * [Handling 1 Parameter that is not a string](#handling-1-parameter-that-is-not-a-string)
  * [Handling 2 Parameters](#handling-2-parameters)<!-- endToc -->

## Problem
You are doing TDD on a pure function that takes some parameters and returns a result.
You want to just program and see the results of running it with as little in the way of that as possible.

## Solution
Use a combination of: 
1. Inline Approvals
2. Parse Input
3. Auto-Approver

This allows you to easily give inputs and see the output.
This will remove the repoter and diff tools and feel more like a REPL.

## Handling 1 Parameter

### Scenario - Counting Vowels
You are writing a function that counts the number of vowels in a string.

### Step 1: Write the Test
Start by writing an empty implementation with 1 input.
<!-- snippet: parse_input_step_1 -->
<a id='snippet-parse_input_step_1'></a>
```py
def count_vowels(s: str) -> int:
    return 0

def test_count_vowels():
    """
    Kody
    """
    parse = Parse.doc_string(auto_approve=True)
    parse.verify_all(count_vowels)
```
<sup><a href='/tests/test_parse_inputs.py#L57-L68' title='Snippet source file'>snippet source</a> | <a href='#snippet-parse_input_step_1' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

### Step 2: Run the Test
When you run the test it will fail, but it will automatically update the docstring with the result from your function
<!-- snippet: parse_input_step_2 -->
<a id='snippet-parse_input_step_2'></a>
```py
"""
Kody -> 0
"""
```
<sup><a href='/tests/test_parse_inputs.py#L51-L56' title='Snippet source file'>snippet source</a> | <a href='#snippet-parse_input_step_2' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

### Step 3: Implement and rerun 
Everytime you run the tests, you automatically see the result at the top in the docstring.
As you want more test cases just add more lines to the docstring.
Here's an example of where we have handled O, E, & A.
<!-- snippet: parse_input_step_3 -->
<a id='snippet-parse_input_step_3'></a>
```py
def count_vowels(s: str) -> int:
    return sum(1 for c in s if c in "aeo")

def test_count_vowels():
    """
    Kody -> 1
    Teresa -> 3
    Green -> 2
    """
    parse = Parse.doc_string(auto_approve=True)
    parse.verify_all(count_vowels)
```
<sup><a href='/tests/test_parse_inputs.py#L79-L92' title='Snippet source file'>snippet source</a> | <a href='#snippet-parse_input_step_3' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

### Step 4: Commit

When you finally get the answer you want, remove the `auto_approve=True` and commit the code.


## Handling 1 Parameter that is not a string
All input will be treated as strings.
But it is easy to transform it to the type you care about.
Here's an example:

<!-- snippet: parse_input_transformation -->
<a id='snippet-parse_input_transformation'></a>
```py
def test_with_transformation() -> None:
    """
    1 -> 0b1
    9 -> 0b1001
    """
    parse = Parse.doc_string(auto_approve=True)
    parse.transform(int).verify_all(bin)
```
<sup><a href='/tests/test_parse_inputs.py#L96-L106' title='Snippet source file'>snippet source</a> | <a href='#snippet-parse_input_transformation' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## Handling 2 Parameters
If you need multiple parameters, there are transform calls for each parameter.
Here's an example with two parameters:

<!-- snippet: parse_input_two_parameters -->
<a id='snippet-parse_input_two_parameters'></a>
```py
def test_with_two_parameters() -> None:
    """
    a, 3 -> aaa
    !, 7 -> !!!!!!!
    """
    parse = Parse.doc_string(auto_approve=True)
    parse.transform2(str, int).verify_all(lambda s, i: s * i)
```
<sup><a href='/tests/test_parse_inputs.py#L109-L119' title='Snippet source file'>snippet source</a> | <a href='#snippet-parse_input_two_parameters' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

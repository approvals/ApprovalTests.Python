# How to have tight feedback loops with inline approvals and parse_input

## Problem
You are doing TDD on a pure function that takes some parameters and returns a result.
You want to just program and see the results of running it with as little in the way of that as possible.

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
<sup><a href='/tests/test_parse_inputs.py#L55-L66' title='Snippet source file'>snippet source</a> | <a href='#snippet-parse_input_step_1' title='Start of snippet'>anchor</a></sup>
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
<sup><a href='/tests/test_parse_inputs.py#L49-L54' title='Snippet source file'>snippet source</a> | <a href='#snippet-parse_input_step_2' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

### Step 3: Implement the Function
Everytime you run the tests, you automatically see the result at the top in the docstring.
When you finally get the answer you want, remove the `auto_approve=True` and commit the code.


## Handling 1 Parameter that is not a string
All input will be treated as strings.
But it is easy to transform it to the type you care about.
Here's an example:

<!-- snippet: parse_input_transformation -->
<a id='snippet-parse_input_transformation'></a>
```py
def test_with_transformation():
    """
    1 -> 0b1
    9 -> 0b1001
    """
    parse = Parse.doc_string(auto_approve=True)
    parse.transform(int).verify_all(bin)
```
<sup><a href='/tests/test_parse_inputs.py#L70-L80' title='Snippet source file'>snippet source</a> | <a href='#snippet-parse_input_transformation' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## Handling 2 Parameters
If you need multiple parameters, there are transform calls for each parameter.
Here's an example with two parameters:

<!-- snippet: parse_input_two_parameters -->
<a id='snippet-parse_input_two_parameters'></a>
```py
def test_with_two_parameters():
    """
    a, 3 -> aaa
    !, 7 -> !!!!!!!
    """
    parse = Parse.doc_string(auto_approve=True)
    parse.transform2(str, int).verify_all(lambda s, i: s * i)
```
<sup><a href='/tests/test_parse_inputs.py#L83-L93' title='Snippet source file'>snippet source</a> | <a href='#snippet-parse_input_two_parameters' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

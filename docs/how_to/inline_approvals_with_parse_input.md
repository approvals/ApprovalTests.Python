# How to have tight feedback loops with inline approvals and parse_input

## Problem
You are doing TDD on a pure function that takes some parameters and returns a result.
You want to just program and see the results of running it with as little in the way of that as possible.

## Handling 1 Parameter

### Scenario - Counting Vowels
You are writing a function that counts the number of vowels in a string.

### Step 1: Write the Test
Start by writing an empty implementation with 1 input.
snippet: parse_input_step_1

### Step 2: Run the Test
When you run the test it will fail, but it will automatically update the docstring with the result from your function
snippet: parse_input_step_2

### Step 3: Implement the Function
Everytime you run the tests, you automatically see the result at the top in the docstring.
When you finally get the answer you want, remove the `auto_approve=True` and commit the code.


## Handling 1 Parameter that is not a string
All input will be treated as strings.
But it is easy to transform it to the type you care about.
Here's an example:

snippet: parse_input_transformation

## Handling 2 Parameters
If you need multiple parameters, there are transform calls for each parameter.
Here's an example with two parameters:

snippet: parse_input_two_parameters
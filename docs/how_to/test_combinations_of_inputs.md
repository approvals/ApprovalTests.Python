<a id="top"></a>

# How to Test  Combinations Inputs

<!-- toc -->
## Contents

  * [What is Combination Testing](#what-is-combination-testing)
  * [When to use Combinations](#when-to-use-combinations)
  * [Steps](#steps)<!-- endToc -->

## What is Combination Testing

If you have a function `isAwake(day, time)` and you want to test it for multiple days & times.
Combination Testing can be used to generate all combinations of provided inputs.


| Input1<BR> (Day) | Input2 <BR> (Time) | Output <BR> (isAwake) |
|---|----|---|
| Sunday | 7:00 | No |
| Sunday | 9:00 | No |
| Sunday | 11:00 | Maybe |
| Monday | 7:00 | Maybe |
| Monday | 9:00 | Yes |
| Monday | 11:00 | Yes |

If you wanted to test this matrix combination approvals can do it with a single line:

<!-- snippet: combination_introduction -->
<a id='snippet-combination_introduction'></a>
```py
verify_all_combinations(is_awake, [["Monday", "Sunday"], ["7:00", "9:00", "11:00"]])
```
<sup><a href='/tests/test_combinations.py#L139-L141' title='Snippet source file'>snippet source</a> | <a href='#snippet-combination_introduction' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## When to use Combinations

You have a function that takes, for example, 3 parameters, and you want to test its behaviour with a bunch of different values for each of those parameters.

If you have only one parameter that you want to vary, check out [How to Test a Variety of Values for One Input](TestAVarietyOfValues.md#top).

## Steps

1. Copy this starter text, and adjust for the number of inputs that you have.

<!-- snippet: combinations_starting_point -->
<a id='snippet-combinations_starting_point'></a>
```py
inputs1 = ["input1.value1", "input1.value2"]
inputs2 = ["input2.value1", "input2.value2", "input2.value3"]
verify_all_combinations(lambda a, b: "placeholder", [inputs1, inputs2])
```
<sup><a href='/tests/test_combinations.py#L145-L149' title='Snippet source file'>snippet source</a> | <a href='#snippet-combinations_starting_point' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

2. Modify each input container for your chosen values.
3. Run it, and make sure that you have your inputs wired up correctly.

If they are wired up correctly, you will see a file that looks like this: it is the left hand side of the file that
matters at this point: all combinations of your own input values should be listed:

<!-- snippet: test_combinations.test_starting_snippet.approved.txt -->
<a id='snippet-test_combinations.test_starting_snippet.approved.txt'></a>
```txt
args: ('input1.value1', 'input2.value1') => 'placeholder'
args: ('input1.value1', 'input2.value2') => 'placeholder'
args: ('input1.value1', 'input2.value3') => 'placeholder'
args: ('input1.value2', 'input2.value1') => 'placeholder'
args: ('input1.value2', 'input2.value2') => 'placeholder'
args: ('input1.value2', 'input2.value3') => 'placeholder'
```
<sup><a href='/tests/approved_files/test_combinations.test_starting_snippet.approved.txt#L1-L6' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_combinations.test_starting_snippet.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

5. Implement the body of your lambda
6. Run it, and approve the output.

For advice on effective formatting, see [Tips for Designing Strings](https://github.com/approvals/ApprovalTests.cpp/blob/master/doc/explanations/TipsForDesigningStrings.md#top). As you write out larger volumes of data in your approval files, experience has shown that the choice of layout of text in approval files can make a big difference to maintainability of tests, when failures occur.

---

[Back to User Guide](/doc/README.md#top)

# How to approve multiple files in one test

<!-- toc -->
## Contents

  * [The Scenario](#the-scenario)
    * [Method 1: Verifying Parametrized Tests](#method-1-verifying-parametrized-tests)
    * [Method 3: Verify Multiple Things without Blocking](#method-3-verify-multiple-things-without-blocking)<!-- endToc -->

## The Scenario

Let's say that you want to test whether or not a year is a leap year for four values [1993, 1992, 1900, 2000]

But instead of testing them all in one file using `verify_all` 
you would like to have 4 seperate approval files.


1. test_file.test_name.`1993`.approved.txt
2. test_file.test_name.`1992`.approved.txt
3. test_file.test_name.`1900`.approved.txt
4. test_file.test_name.`2000`.approved.txt

Here is a sample of one of the `.approved.` files:

<!-- snippet: test_scenarios.test_manual_scenarios.1992.approved.txt -->
<a id='snippet-test_scenarios.test_manual_scenarios.1992.approved.txt'></a>
```txt
is Leap 1992: True
```
<sup><a href='/tests/approved_files/test_scenarios.test_manual_scenarios.1992.approved.txt#L1-L1' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_scenarios.test_manual_scenarios.1992.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

Here are 3 ways you can do this in a single test.

### Method 1: Verifying Parametrized Tests

Approval tests supports parametrized tests, here is an example:

<!-- snippet: parametrized-test-example -->
<a id='snippet-parametrized-test-example'></a>
```py
@pytest.mark.parametrize("year", [1993, 1992, 1900, 2000])
def test_scenarios(year: int) -> None:
    verify(f"is Leap {str(year)}: {str(is_leap_year(year))}", options=NamerFactory.with_parameters(year))
```
<sup><a href='/tests/test_scenarios.py#L24-L28' title='Snippet source file'>snippet source</a> | <a href='#snippet-parametrized-test-example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->
### Method 2: Verify Multiple Things with Blocking

Another alternative is to simply make multiple `verify()` calls using the `NamerFactory.with_parameters` in the code. 
Be aware that this will halt your test on the first `verify()` that fails, same as a normal `assert`.

<!-- snippet: multiple-verifies-without-blocking -->
<a id='snippet-multiple-verifies-without-blocking'></a>
```py
years = [1993, 1992, 1900, 2000]
gather_all_exceptions_and_throw(years, lambda y: verify(f"is Leap {str(y)}: {str(is_leap_year(y))}", options=NamerFactory.with_parameters(y)))
```
<sup><a href='/tests/test_scenarios.py#L43-L46' title='Snippet source file'>snippet source</a> | <a href='#snippet-multiple-verifies-without-blocking' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

### Method 3: Verify Multiple Things without Blocking

To manually verify multiple things without the executation stopping on the first failure,
using `gather_all_exceptions_and_throw` will prevent blocking, while still failing on any failure.  

Here is an example:

<!-- snippet: multiple-verifies-without-blocking -->
<a id='snippet-multiple-verifies-without-blocking'></a>
```py
years = [1993, 1992, 1900, 2000]
gather_all_exceptions_and_throw(years, lambda y: verify(f"is Leap {str(y)}: {str(is_leap_year(y))}", options=NamerFactory.with_parameters(y)))
```
<sup><a href='/tests/test_scenarios.py#L43-L46' title='Snippet source file'>snippet source</a> | <a href='#snippet-multiple-verifies-without-blocking' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->







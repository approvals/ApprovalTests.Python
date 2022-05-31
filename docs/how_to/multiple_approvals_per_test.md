# How to approve multiple files in one test

<!-- toc -->
## Contents

  * [Verifying Parametrized Tests](#verifying-parametrized-tests)
  * [Verify Multiple Things without Blocking](#verify-multiple-things-without-blocking)<!-- endToc -->

## Verifying Parametrized Tests

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
## Verify Multiple Things with Blocking

An other alternative is to simply make multiple `verify()` calls using the `NamerFactory` in the code. 
Be aware that this will halt your test on the first `verify()` that fails, same as a normal `assert`.

snippet: multiple-verifies-without-blocking

## Verify Multiple Things without Blocking

If you want to manually verify multiple things, you can still use the `with_parameters` directly. 
However, if any of them fail your test will end. To prevent this you can use `gather_all_exceptions_and_throw`.
Here is an example:

<!-- snippet: multiple-verifies-without-blocking -->
<a id='snippet-multiple-verifies-without-blocking'></a>
```py
years = [1993,1992]
gather_all_exceptions_and_throw(years, lambda y: verify(f"is Leap {str(y)}: {str(is_leap_year(y))}", options=NamerFactory.with_parameters(y)))
```
<sup><a href='/tests/test_scenarios.py#L32-L35' title='Snippet source file'>snippet source</a> | <a href='#snippet-multiple-verifies-without-blocking' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

Which will produce the 2 files:

test_scenarios.test_manual_scenarios.`1992`.approved.txt
test_scenarios.test_manual_scenarios.`1993`.approved.txt
test_scenarios.test_manual_scenarios.`1900`.approved.txt
test_scenarios.test_manual_scenarios.`2000`.approved.txt

Here is a sample of one of them: 
<!-- snippet: test_scenarios.test_manual_scenarios.1992.approved.txt -->
<a id='snippet-test_scenarios.test_manual_scenarios.1992.approved.txt'></a>
```txt
is Leap 1992: True
```
<sup><a href='/tests/approved_files/test_scenarios.test_manual_scenarios.1992.approved.txt#L1-L1' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_scenarios.test_manual_scenarios.1992.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->



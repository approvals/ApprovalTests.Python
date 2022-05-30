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
    verify(f"is Leap {str(year)}: {str(is_leap(year))}", options=NamerFactory.with_parameters(year))
```
<sup><a href='/tests/test_scenarios.py#L24-L28' title='Snippet source file'>snippet source</a> | <a href='#snippet-parametrized-test-example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## Verify Multiple Things without Blocking

If you want to manually verify multiple things, you can still use the `with_parameters` directly. 
However, if any of them fail your test will end. To prevent this you can use `gather_all_exceptions_and_throw`.
Here is an example:

<!-- snippet: multiple-verifies-without-blocking -->
<a id='snippet-multiple-verifies-without-blocking'></a>
```py
gather_all_exceptions_and_throw([1, 2], lambda i: verify(f"{i}", options=NamerFactory.with_parameters(i)))
```
<sup><a href='/tests/test_scenarios.py#L32-L34' title='Snippet source file'>snippet source</a> | <a href='#snippet-multiple-verifies-without-blocking' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

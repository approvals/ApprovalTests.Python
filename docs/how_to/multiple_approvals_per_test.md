# How to approve multiple files in one test

<!-- toc -->
## Contents

  * [Verifying Parametrized Tests](#verifying-parametrized-tests)<!-- endToc -->

## Verifying Parametrized Tests

Approval tests supports parametrized tests, here is an example:

<!-- snippet: parametrized-test-example -->
<a id='snippet-parametrized-test-example'></a>
```py
@pytest.mark.parametrize("year", [1993, 1992, 1900, 2000])
def test_scenarios(year: int) -> None:
    with NamerFactory.with_parameters(year) as options:
        verify(f"is Leap {str(year)}: {str(is_leap(year))}", options=options)
```
<sup><a href='/tests/test_scenarios.py#L22-L27' title='Snippet source file'>snippet source</a> | <a href='#snippet-parametrized-test-example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

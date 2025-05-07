# Configuration

<!-- toc -->
## Contents

  * [Samples](#samples)
  * [Examples](#examples)
  * [How to configure a default reporter for your system](#how-to-configure-a-default-reporter-for-your-system)
    * [Unittest](#unittest)
    * [Pytest](#pytest)<!-- endToc -->

You can create directory level configuration for approvals.
To do this create a file named `approvaltests_config.json` and place it in the same directory as your test.
As of right now, the only configuration that you can do is to add subdirectories where the approved and received files will show up.
There is nothing that you need to do in the tests themselves to use this.

## Samples

You can find a [sample configuration here](/tests/configuration/approvaltests_config.json) and a [sample test that uses it here](/tests/configuration/test_subdirectory.py).

## Examples

A sample `approvaltests_config.json`:

```
{
  "subdirectory": "approved_files"
}
```

## How to configure a default reporter for your system

If you don't like the standard default for reporting and wish to change it everywhere this is the recommended way to do it.

<!-- snippet: default_reporter -->
<a id='snippet-default_reporter'></a>
```py
set_default_reporter(ReporterByCopyMoveCommandForEverythingToClipboard())
```
<sup><a href='/tests/approvals_config.py#L13-L15' title='Snippet source file'>snippet source</a> | <a href='#snippet-default_reporter' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

The problem is you need to do this before you do anything else. Here are suggestions on how to do that.
### Unittest
While some test frameworks allow for this, our recommended suggestion is to do it directly in Python by using the `__init__.py`
below. 

**note:** Please be aware that this will not override the reporters that are specified in your tests, as approval tests uses
[the principle of least surprise.](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)

<!-- snippet: configure_approvaltests_under_init -->
<a id='snippet-configure_approvaltests_under_init'></a>
```py
# From __init__.py
configure_approvaltests()
```
<sup><a href='/tests/__init__.py#L7-L10' title='Snippet source file'>snippet source</a> | <a href='#snippet-configure_approvaltests_under_init' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

<!-- snippet: configure_approvaltests -->
<a id='snippet-configure_approvaltests'></a>
```py
def configure_approvaltests():
    set_default_reporter(my_preferred_reporter)
```
<sup><a href='/tests/approvals_config.py#L9-L12' title='Snippet source file'>snippet source</a> | <a href='#snippet-configure_approvaltests' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

### Pytest

Alternatively, pytest allows for the creation of a [session scoped autouse fixture in the conftest.py](https://pythontesting.net/framework/pytest/pytest-session-scoped-fixtures/#example) file in Pytest.
Here's a [blog with an example](https://pythontesting.net/framework/pytest/pytest-session-scoped-fixtures/#example)

Here's the code for implementing it in `conftest.py` (so skip the code in `__init__.py`):
<!-- snippet: conftest_pytest_session_scoped -->
<a id='snippet-conftest_pytest_session_scoped'></a>
```py
@pytest.fixture(scope="session", autouse=True)
def set_default_reporter_for_all_tests() -> None:
    configure_approvaltests()
```
<sup><a href='/tests/conftest.py#L8-L14' title='Snippet source file'>snippet source</a> | <a href='#snippet-conftest_pytest_session_scoped' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->


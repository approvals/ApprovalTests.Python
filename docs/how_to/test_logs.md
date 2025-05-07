# How to test logs

<!-- toc -->
## Contents

  * [Why Test via Logs?](#why-test-via-logs)
  * [Testing Logs](#testing-logs)
    * [1. with](#1-with)
    * [2. Log To String](#2-log-to-string)<!-- endToc -->

## Why Test via Logs?

Sometimes code can be hard to test because it doesn't return anything.
If you can run the code, adding logging is a relatively safe thing to do. 
Then if you can capture those logs in your tests, you can start to safely refactor and even modify existing behavior with confidence.


## Testing Logs

There are 2 apis for testing logs, although they both work in the same manner.
### 1. with

This easiest way to test with simple logger is to use the  `with verify_simple_logger:` which will
capture everything logged in the follow context and verify it. 

Example:

<!-- snippet: verify_simple_logger_example -->
<a id='snippet-verify_simple_logger_example'></a>
```py
def test_variable() -> None:
    with verify_simple_logger():
        SimpleLogger.variable("dalmatians", 101, show_types=True)
        SimpleLogger.variable("dalmatians", 101, show_types=False)
```
<sup><a href='/tests/test_simple_logger.py#L75-L82' title='Snippet source file'>snippet source</a> | <a href='#snippet-verify_simple_logger_example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

which produces:

<!-- snippet: test_simple_logger.test_variable.approved.txt -->
<a id='snippet-test_simple_logger.test_variable.approved.txt'></a>
```txt
variable: dalmatians = 101 <int>
variable: dalmatians = 101
```
<sup><a href='/tests/approved_files/test_simple_logger.test_variable.approved.txt#L1-L2' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_simple_logger.test_variable.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

### 2. Log To String

Alternatively, you can achive the same result by logging to a string and then verifing the result

Example:

<!-- snippet: verify_simple_logger_long_example -->
<a id='snippet-verify_simple_logger_long_example'></a>
```py
def test_variable_explict() -> None:
    output = SimpleLogger.log_to_string()
    SimpleLogger.variable("dalmatians", 101, show_types=True)
    SimpleLogger.variable("dalmatians", 101, show_types=False)
    verify(output)
```
<sup><a href='/tests/test_simple_logger.py#L85-L93' title='Snippet source file'>snippet source</a> | <a href='#snippet-verify_simple_logger_long_example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

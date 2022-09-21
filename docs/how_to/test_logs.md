# How to test logs

<!-- toc -->
## Contents

  * [Problem](#problem)
  * [Logging Inputs](#logging-inputs)
  * [Logging Inputs and Outputs](#logging-inputs-and-outputs)<!-- endToc -->

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

snippet: verify_simple_logger_example

which produces:

snippet: test_simple_logger.test_variable.approved.txt

### 2. Log To String

Alternatively, you can achive the same result by logging to a string and then verifing the result

Example:

snippet: verify_simple_logger_long_example

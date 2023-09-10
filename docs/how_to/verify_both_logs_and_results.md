# How to verify both logs and results

<!-- toc -->
## Contents

  * [The Problem](#the-problem)
    * [Sample Logs](#sample-logs)
  * [Incorrect Method](#incorrect-method)
  * [Solution #1) Combine Result with Log File](#solution-1-combine-result-with-log-file)
  * [Solution #2) Two seperate approved files in one test](#solution-2-two-seperate-approved-files-in-one-test)
    * [The Approved Log file](#the-approved-log-file)
    * [The Approved Result file](#the-approved-result-file)
  * [Solution #3) Split into Two Tests](#solution-3-split-into-two-tests)
    * [1. Test Only the Logs](#1-test-only-the-logs)
    * [2. Test Only the Results](#2-test-only-the-results)<!-- endToc -->

## The Problem

We have a function named `load_person()`.   
We want to verify the logs from this call as well as the person object that is returned.

### Sample Logs 
<!-- snippet: test_logging_examples.test_load_person_logs.approved.txt -->
<a id='snippet-test_logging_examples.test_load_person_logs.approved.txt'></a>
```txt
root INFO
  connecting to the database
root INFO
  querying a table
root INFO
  closing the database
```
<sup><a href='/tests/logging/test_logging_examples.test_load_person_logs.approved.txt#L1-L6' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_logging_examples.test_load_person_logs.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->
### Sample Results
<!-- snippet: test_logging_examples.test_load_person_results.approved.txt -->
<a id='snippet-test_logging_examples.test_load_person_results.approved.txt'></a>
```txt
{
    "first_name":"Britney",
    "last_name": "Spears",
    "profession":"Singer"    
}
```
<sup><a href='/tests/logging/test_logging_examples.test_load_person_results.approved.txt#L1-L5' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_logging_examples.test_load_person_results.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## Incorrect Method

By default, ApprovalTests allows only one verification per test method.  
The following will not yield the expected outcome:

```python 
def test_load_person_with_logs():
    with verify_logging():
        verify(load_person())
```

Here are a couple of solutions (details below):
  1. [Combine Result with Log File](#solution-1-combine-result-with-log-file)
  2. [Two seperate approved files in one test](#solution-2-two-seperate-approved-files-in-one-test)
  3. [Split into Two Tests](#solution-3-split-into-two-tests)

## Solution #1) Combine Result with Log File

With this approach, we leverage the logging mechanism to also verify the output.

<!-- snippet: testing_logging_combined_with_results -->
<a id='snippet-testing_logging_combined_with_results'></a>
```py
def test_load_person_logs_and_results():
    with verify_logging():
        logging.info(f"result = {load_person()}")
```
<sup><a href='/tests/logging/test_logging_examples.py#L42-L48' title='Snippet source file'>snippet source</a> | <a href='#snippet-testing_logging_combined_with_results' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

This will create a single approved file, combining both the logs and the result:

`test_load_person_logs_and_results.approved.txt`
<!-- snippet: test_logging_examples.test_load_person_logs_and_results.approved.txt -->
<a id='snippet-test_logging_examples.test_load_person_logs_and_results.approved.txt'></a>
```txt
root INFO
  connecting to the database
root INFO
  querying a table
root INFO
  closing the database
root INFO
  result = {
    "first_name":"Britney",
    "last_name": "Spears",
    "profession":"Singer"    
}
```
<sup><a href='/tests/logging/test_logging_examples.test_load_person_logs_and_results.approved.txt#L1-L12' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_logging_examples.test_load_person_logs_and_results.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## Solution #2) Two seperate approved files in one test

This method introduces the `.logging` extension to generate two distinct `.approved` files.

<!-- snippet: testing_logging_with_namer_factory -->
<a id='snippet-testing_logging_with_namer_factory'></a>
```py
def test_load_person_logs_and_results_separately():
    with verify_logging(options=NamerFactory.with_parameters("logging")):
        verify(load_person())
```
<sup><a href='/tests/logging/test_logging_examples.py#L51-L57' title='Snippet source file'>snippet source</a> | <a href='#snippet-testing_logging_with_namer_factory' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

This will create the following files:

### The Approved Log file
`test_load_person_logs_and_results_separately.logging.approved.txt`
<!-- snippet: test_logging_examples.test_load_person_logs_and_results_separately.logging.approved.txt -->
<a id='snippet-test_logging_examples.test_load_person_logs_and_results_separately.logging.approved.txt'></a>
```txt
root INFO
  connecting to the database
root INFO
  querying a table
root INFO
  closing the database
```
<sup><a href='/tests/logging/test_logging_examples.test_load_person_logs_and_results_separately.logging.approved.txt#L1-L6' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_logging_examples.test_load_person_logs_and_results_separately.logging.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

and
###  The Approved Result file
`test_load_person_logs_and_results_separately.approved.txt`
<!-- snippet: test_logging_examples.test_load_person_logs_and_results_separately.approved.txt -->
<a id='snippet-test_logging_examples.test_load_person_logs_and_results_separately.approved.txt'></a>
```txt
{
    "first_name":"Britney",
    "last_name": "Spears",
    "profession":"Singer"    
}
```
<sup><a href='/tests/logging/test_logging_examples.test_load_person_logs_and_results_separately.approved.txt#L1-L5' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_logging_examples.test_load_person_logs_and_results_separately.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->


## Solution #3) Split into Two Tests

This option divides the verification into two distinct tests: one for logs and another for results.

### 1. Test Only the Logs
<!-- snippet: test_logging_separately -->
<a id='snippet-test_logging_separately'></a>
```py
def test_load_person_logs():
    with verify_logging():
        load_person()
```
<sup><a href='/tests/logging/test_logging_examples.py#L25-L31' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_logging_separately' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

This will create the following file:  
`test_load_person_logs.approved.txt`
<!-- snippet: test_logging_examples.test_load_person_logs.approved.txt -->
<a id='snippet-test_logging_examples.test_load_person_logs.approved.txt'></a>
```txt
root INFO
  connecting to the database
root INFO
  querying a table
root INFO
  closing the database
```
<sup><a href='/tests/logging/test_logging_examples.test_load_person_logs.approved.txt#L1-L6' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_logging_examples.test_load_person_logs.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

### 2. Test Only the Results
<!-- snippet: test_logging_separately_results -->
<a id='snippet-test_logging_separately_results'></a>
```py
def test_load_person_results():
    verify(load_person())
```
<sup><a href='/tests/logging/test_logging_examples.py#L34-L39' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_logging_separately_results' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

This will create the following file:  
`test_load_person_results.approved.txt`
<!-- snippet: test_logging_examples.test_load_person_results.approved.txt -->
<a id='snippet-test_logging_examples.test_load_person_results.approved.txt'></a>
```txt
{
    "first_name":"Britney",
    "last_name": "Spears",
    "profession":"Singer"    
}
```
<sup><a href='/tests/logging/test_logging_examples.test_load_person_results.approved.txt#L1-L5' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_logging_examples.test_load_person_results.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

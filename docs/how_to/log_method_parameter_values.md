# How to log method parameters values

<!-- toc -->
## Contents

  * [Problem](#problem)
  * [Logging Inputs](#logging-inputs)
  * [Logging Inputs and Outputs](#logging-inputs-and-outputs)<!-- endToc -->

## Problem

You want to log what the parameters are that a method receives at the method start (and end)

## Logging Inputs
To log the input values, you can pass in a formatted string to SimpleLogger.use_markers.  
Here is an example:

<!-- snippet: method_with_inputs -->
<a id='snippet-method_with_inputs'></a>
```py
def method_with_inputs(number, name):
    with SimpleLogger.use_markers(f"number = {number}, name = {name}"):
```
<sup><a href='/tests/test_simple_logger.py#L172-L175' title='Snippet source file'>snippet source</a> | <a href='#snippet-method_with_inputs' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

It will produce:  

<!-- snippet: test_simple_logger.test_markers_with_signature.approved.txt -->
<a id='snippet-test_simple_logger.test_markers_with_signature.approved.txt'></a>
```txt
-> in: method_with_inputs(number = 1, name = Susan) in test_simple_logger
<- out: method_with_inputs()
```
<sup><a href='/tests/approved_files/test_simple_logger.test_markers_with_signature.approved.txt#L1-L2' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_simple_logger.test_markers_with_signature.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## Logging Inputs and Outputs
To log the values at both entrance to the method and exit from the method, you can pass in a formatted string **in a lambda**.  
Here is an example:

<!-- snippet: method_with_inputs_and_outputs -->
<a id='snippet-method_with_inputs_and_outputs'></a>
```py
def method_with_inputs_and_outputs(number, announcement):
    with SimpleLogger.use_markers(
        lambda: f"number = {number}, announcement = {announcement}"
    ):
```
<sup><a href='/tests/test_simple_logger.py#L185-L190' title='Snippet source file'>snippet source</a> | <a href='#snippet-method_with_inputs_and_outputs' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

It will produce:  

<!-- snippet: test_simple_logger.test_markers_with_signature_in_and_out.approved.txt -->
<a id='snippet-test_simple_logger.test_markers_with_signature_in_and_out.approved.txt'></a>
```txt
-> in: method_with_inputs_and_outputs(number = 10, announcement = Blast off) in test_simple_logger
<- out: method_with_inputs_and_outputs(number = 1, announcement = Blast off)
```
<sup><a href='/tests/approved_files/test_simple_logger.test_markers_with_signature_in_and_out.approved.txt#L1-L2' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_simple_logger.test_markers_with_signature_in_and_out.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

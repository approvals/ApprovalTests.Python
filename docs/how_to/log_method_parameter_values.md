# How to log method parameters values

toc

## Problem

You want to log what the parameters are that a method receives at the method start (and end)

## Logging Inputs
To log the input values, you can pass in a formatted string to SimpleLogger.use_markers.  
Here is an example:

snippet: method_with_inputs

It will produce:  

snippet: test_simple_logger.test_markers_with_signature.approved.txt

## Logging Inputs and Outputs
To log the values at both entrance to the method and exit from the method, you can pass in a formatted **in a lambda**.  
Here is an example:

snippet: method_with_inputs_and_outputs

It will produce:  

snippet: test_simple_logger.test_markers_with_signature_in_and_out.approved.txt
# How to Create a Custom Reporter

## Extend Reporter

Create a class that extends `Reporter` and implement the `report` function. 
Report should return true/false based on if it is able to successfully report,
this allows other reporters to try when the current one is unable to. 

## Example

snippet: numpy_custom_reporter
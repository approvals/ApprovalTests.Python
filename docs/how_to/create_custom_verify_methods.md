# How to extend your own verify() methods

toc

## Create a Custom Verify Method

One method is to create a custom `verify()` method for your particular situation.

For example, as we use it to handle json:

snippet: verify_as_json

## Create a `Verifiable` Object

Alternatively, you can create an object that knows how to verify itself. 
See the required interfaces: 
* [Verifiable](https://github.com/approvals/ApprovalTests.Python/blob/main/approvaltests/core/verifiable.py#L7-L10)
* [VerifyParameters](https://github.com/approvals/ApprovalTests.Python/blob/main/approvaltests/core/verify_parameters.py)

And then just call `verify(YourVarifiableObject)`

If verify is called with an instance of `Verifiable` it will to a callback, allowing you to do whatever is needed,
for example:

snippet: verifiable_object_example
  

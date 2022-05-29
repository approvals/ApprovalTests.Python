# How to extend your own verify() methods

toc

## Custom Verify Method

One method would be to create a custom `verify()` method.

For example, as we use it to handle json:

``` 
def verify_my_object(my_object: MyObject) -> None:
    # do initalazition stuff
    # call verify with modified stuff
    ...
```  
  
## Create a `Verifiable` Object

Alternatively, you can create an object that knows how to verify itself. 
See: 
* [Verifiable](https://github.com/approvals/ApprovalTests.Python/blob/main/approvaltests/core/verifiable.py#L7-L10)
* [VerifyParameters](https://github.com/approvals/ApprovalTests.Python/blob/main/approvaltests/core/verify_parameters.py)

And then just call `verify(YourVarifiableObject)`

For Example:

snippet: verifiable_object_example
  

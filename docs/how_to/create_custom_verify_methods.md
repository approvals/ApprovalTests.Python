# How to extend your own verify() methods

<!-- toc -->
## Contents

  * [Custom Verify Method](#custom-verify-method)
  * [Create a `Verifiable` Object](#create-a-verifiable-object)<!-- endToc -->

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

<!-- snippet: verifiable_object_example -->
<a id='snippet-verifiable_object_example'></a>
```py
def test_verifiable(self):
    class MarkdownParagraph(Verifiable):
        def __init__(self, title, text):
            self.title = title
            self.text = text

        def __str__(self) -> str:
            return remove_indentation_from(f''' 
            # {self.title}
            {self.text}
            ''')

        def get_verify_parameters(self, options: Options) -> VerifyParameters:
            return VerifyParameters(options.for_file.with_extension(".md"))

    verify(MarkdownParagraph("Paragraph Title", "This is where the paragraph text is."))
```
<sup><a href='/tests/test_verify.py#L283-L300' title='Snippet source file'>snippet source</a> | <a href='#snippet-verifiable_object_example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->
  

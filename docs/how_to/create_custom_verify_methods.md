# How to extend your own verify() methods

<!-- toc -->
## Contents

  * [Create a Custom Verify Method](#create-a-custom-verify-method)
  * [Create a `Verifiable` Object](#create-a-verifiable-object)<!-- endToc -->

## Create a Custom Verify Method

One method is to create a custom `verify()` method for your particular situation.

For example, as we use it to handle json:

<!-- snippet: verify_as_json -->
<a id='snippet-verify_as_json'></a>
```py
def verify_as_json(
    object_to_verify,
    reporter=None,
    *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
    deserialize_json_fields=False,
    options: Optional[Options] = None,
):
    if deserialize_json_fields:
        object_to_verify = utils.deserialize_json_fields(object_to_verify)
    options = initialize_options(options, reporter)
    json_text = utils.to_json(object_to_verify) + "\n"
    verify(
        json_text,
        None,
        encoding="utf-8",
        newline="\n",
        options=options.for_file.with_extension(".json"),
    )
```
<sup><a href='/approvaltests/approvals.py#L236-L257' title='Snippet source file'>snippet source</a> | <a href='#snippet-verify_as_json' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## Create a `Verifiable` Object

Alternatively, you can create an object that knows how to verify itself. 
See the required interfaces: 
* [Verifiable](https://github.com/approvals/ApprovalTests.Python/blob/main/approvaltests/core/verifiable.py#L7-L10)
* [VerifyParameters](https://github.com/approvals/ApprovalTests.Python/blob/main/approvaltests/core/verify_parameters.py)

And then just call `verify(YourVarifiableObject)`

If verify is called with an instance of `Verifiable` it will do a callback, allowing you to do whatever is needed,
for example:

<!-- snippet: verifiable_object_example -->
<a id='snippet-verifiable_object_example'></a>
```py
def test_verifiable(self):
    class MarkdownParagraph(Verifiable):
        def __init__(self, title, text):
            self.title = title
            self.text = text

        def __str__(self) -> str:
            return remove_indentation_from(
                f""" 
            # {self.title}
            {self.text}
            """
            )

        def get_verify_parameters(self, options: Options) -> VerifyParameters:
            return VerifyParameters(options.for_file.with_extension(".md"))

    verify(
        MarkdownParagraph("Paragraph Title", "This is where the paragraph text is.")
    )
```
<sup><a href='/tests/test_verify.py#L304-L326' title='Snippet source file'>snippet source</a> | <a href='#snippet-verifiable_object_example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->
  

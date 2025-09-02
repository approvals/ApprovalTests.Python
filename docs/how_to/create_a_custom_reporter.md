# How to Create a Custom Reporter

## Extend Reporter

Create a class that extends `Reporter` and implement the `report` function. 
Report should return true/false based on if it is able to successfully report,
this allows other reporters to try when the current one is unable to. 

## Example

<!-- snippet: numpy_custom_reporter -->
<a id='snippet-numpy_custom_reporter'></a>
```py
def load_ndarray(path: str):
    with open(path, mode="rb") as f:
        return np.load(f)

class NDArrayDiffReporter(Reporter):
    @override
    def report(self, received_path: str, approved_path: str) -> bool:
        if not Path(approved_path).is_file():
            self._create_empty_array(approved_path)
        received = load_ndarray(received_path)
        approved = load_ndarray(approved_path)
        to_approve_msg = (
            f"To approve run:\n {get_command_text(received_path, approved_path)}"
        )
        print(np.testing.build_err_msg([received, approved], err_msg=to_approve_msg))
        return True
```
<sup><a href='/tests/test_example_numpy.py#L34-L55' title='Snippet source file'>snippet source</a> | <a href='#snippet-numpy_custom_reporter' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

# How To Verify Binary Blobs

<!-- toc -->
## Contents

  * [Examples](#examples)
    * [Approving images](#approving-images)
    * [Approving NumPy arrays](#approving-numpy-arrays)<!-- endToc -->

Using the `verify_binary` function, you can also check binary data blobs. For instance, you could check that your 
program produces correct image frames. Another example would be approving and checking numpy arrays in scientific 
applications.

## Examples

### Approving images
In this example, you can see how `verify_binary` is used to approve rendered images.

<!-- snippet: verify_binary_image -->
<a id='snippet-verify_binary_image'></a>
```py
name = "icon.png"
filename = get_adjacent_file(name)
with open(filename, mode='rb') as f:
    verify_binary(f.read(), ".png")
```
<sup><a href='/tests/test_verify.py#L173-L178' title='Snippet source file'>snippet source</a> | <a href='#snippet-verify_binary_image' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

Which will produce

![Approved image](../../tests/approved_files/VerifyTests.test_verify_file_binary_file.approved.png)

### Approving NumPy arrays
This more detailed example demonstrates how you could use `verify_binary` to approve NumPy arrays. 

It uses serializers instead of dumping the binary blob directly to disk. In this case, the serialization provided by NumPy is used.

<!-- snippet: verify_numpy_array -->
<a id='snippet-verify_numpy_array'></a>
```py
def test_simulator_produces_correct_output():
    np_array = np.full(shape = (32,16),fill_value=42,dtype=np.int64)
    verify_binary(serialize_ndarray(np_array), ".npy", options=Options().with_reporter(NDArrayDiffReporter()))
```
<sup><a href='/tests/test_example_numpy.py#L14-L18' title='Snippet source file'>snippet source</a> | <a href='#snippet-verify_numpy_array' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

It also shows the use of a custom reporter, which uses the NumPy testing features to produce a well-formatted error report highlighting the differences between arrays.

<!-- snippet: numpy_custom_reporter -->
<a id='snippet-numpy_custom_reporter'></a>
```py
def load_ndarray(path):
    with open(path, mode='rb') as f:
        return np.load(f)

class NDArrayDiffReporter(Reporter):
    def report(self, received_path: str, approved_path: str) -> bool:
        if not Path(approved_path).is_file():
            self._create_empty_array(approved_path)
        received = load_ndarray(received_path)
        approved = load_ndarray(approved_path)
        to_approve_msg = f"To approve run:\n {get_command_text(received_path,approved_path)}"
        print(np.testing.build_err_msg([received, approved], err_msg=to_approve_msg))
        return True
```
<sup><a href='/tests/test_example_numpy.py#L23-L39' title='Snippet source file'>snippet source</a> | <a href='#snippet-numpy_custom_reporter' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

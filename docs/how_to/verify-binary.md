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
    verify_binary(f.read(),".png")
```
<sup><a href='/tests/test_verify.py#L153-L158' title='Snippet source file'>snippet source</a> | <a href='#snippet-verify_binary_image' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

Which will produce

![](../../tests/approved_files/VerifyTests.test_verify_file_binary_file.approved.png)

### Approving NumPy arrays
This more detailed example demonstrates how you could use `verify_binary` to approve NumPy arrays. It also shows the 
use of a custom reporter. It uses the NumPy testing features to produce a well-formatted error report highlighting the 
differences between arrays. Additionally, it shows you how to use serializers instead of dumping the binary blob 
directly to disk. In this case, the serialization provided by NumPy is used.

```python
import io
from pathlib import Path
import numpy as np
from approvaltests import verify_binary
from approvaltests.core import Reporter
# Serialization for numpy arrays so approved arrays can be stored and committed to the repository
def serialize_ndarray(a: np.ndarray):
    bs = io.BytesIO()
    np.save(bs, a)
    bs.seek(0)
    return bs.read()
def deserialize_ndarray(path):
    with open(path, mode='rb') as f:
        return np.load(f)
# Use a custom reporter to show the assertion message from numpy
# Also the default python console reporter will try to interpret the numpy data as text causing an error
class NDArrayDiffReporter(Reporter):
    def report(self, received_path, approved_path):
        if not Path(approved_path).is_file():
            self._create_empty_array(approved_path)
        received = deserialize_ndarray(received_path)
        approved = deserialize_ndarray(approved_path)
        to_approve_msg = f"To approve run:\nmv -f {received_path} {approved_path}"
        print(np.testing.build_err_msg([received, approved], err_msg=to_approve_msg))
    @staticmethod
    def _create_empty_array(path):
        with open(path, mode='wb') as f:
            f.write(serialize_ndarray(np.zeros((0,))))
def verify_ndarray(a: np.ndarray):
    verify_binary(serialize_ndarray(a), reporter=NDArrayDiffReporter())
def test_simulator_produces_correct_output(simulator):
    verify_ndarray(simulator.step())

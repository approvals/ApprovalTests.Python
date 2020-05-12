# Verify Binary Blobs

Using the `verify_binary` function, you can also check binary data blobs. For instance, you could check that your 
program produces correct image frames. Another example would be approving and checking numpy arrays in scientific 
applications.

## Examples

### Approving images
In this example, you can see how `verify_binary` is used to approve rendered images. The file endings are also adjusted 
instead of using the generic `.blb` extension. Hence, it is easier to inspect them, using any image viewer. In any case, 
it is important to configure a reporter which can parse and compare binary data properly (i.e. in most Unix 
environments plain old `diff`). See [configuration](configuration.md) for more details on that.

```python
from approvaltests import verify_binary, get_default_namer


def verify_ppm(ppm_data):
    verify_binary(ppm_data, namer=get_default_namer(extension='.ppm'))


def test_render_to_ppm_file(render_engine):
    verify_ppm(render_engine.render().as_ppm())
```

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
```
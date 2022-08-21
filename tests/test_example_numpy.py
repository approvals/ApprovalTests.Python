import io
from pathlib import Path
import numpy as np
from approvaltests import verify_binary, Options
from approvaltests.core import Reporter
from approvaltests.reporters import get_command_text


def serialize_ndarray(a: np.ndarray):
    bs = io.BytesIO()
    np.save(bs, a)
    bs.seek(0)
    return bs.read()


# begin-snippet: verify_numpy_array
def test_simulator_produces_correct_output():
    np_array = np.full(shape=(32, 16), fill_value=42, dtype=np.int64)
    verify_binary(
        serialize_ndarray(np_array),
        ".npy",
        options=Options().with_reporter(NDArrayDiffReporter()),
    )


# end-snippet

# Use a custom reporter to show the assertion message from numpy
# Also the default python console reporter will try to interpret the numpy data as text causing an error

# begin-snippet: numpy_custom_reporter


def load_ndarray(path):
    with open(path, mode="rb") as f:
        return np.load(f)


class NDArrayDiffReporter(Reporter):
    def report(self, received_path: str, approved_path: str) -> bool:
        if not Path(approved_path).is_file():
            self._create_empty_array(approved_path)
        received = load_ndarray(received_path)
        approved = load_ndarray(approved_path)
        to_approve_msg = (
            f"To approve run:\n {get_command_text(received_path,approved_path)}"
        )
        print(np.testing.build_err_msg([received, approved], err_msg=to_approve_msg))
        return True

    # end-snippet

    @staticmethod
    def _create_empty_array(path):
        with open(path, mode="wb") as f:
            f.write(serialize_ndarray(np.zeros((0,))))

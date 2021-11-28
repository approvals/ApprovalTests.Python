import io
from pathlib import Path
import numpy as np
from approvaltests import verify_binary, Options
from approvaltests.core import Reporter
# Serialization for numpy arrays so approved arrays can be stored and committed to the repository
from approvaltests.reporters import get_command_text


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
    def report(self, received_path: str, approved_path: str) -> bool:
        if not Path(approved_path).is_file():
            self._create_empty_array(approved_path)
        received = deserialize_ndarray(received_path)
        approved = deserialize_ndarray(approved_path)
        to_approve_msg = f"To approve run:\n {get_command_text(received_path,approved_path)}"
        print(np.testing.build_err_msg([received, approved], err_msg=to_approve_msg))
        return True
    @staticmethod
    def _create_empty_array(path):
        with open(path, mode='wb') as f:
            f.write(serialize_ndarray(np.zeros((0,))))

def verify_ndarray(a: np.ndarray):
    verify_binary(serialize_ndarray(a), ".npy", options = Options().with_reporter(NDArrayDiffReporter()))

def test_simulator_produces_correct_output():
    verify_ndarray(np.full(shape = (32,16),fill_value=42))

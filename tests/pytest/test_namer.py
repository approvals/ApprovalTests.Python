import os

from approvaltests.approvals import get_default_namer, verify
from approvaltests.pytest.namer import PyTestNamer


def test_basic_approval():
    verify("foo")


def test_received_filename():
    namer = get_default_namer()
    expected = os_path("ApprovalTests.Python/tests/pytest/test_namer.test_received_filename.received.txt")
    assert namer.get_received_filename().endswith(expected)


def test_pytest_namer(request):
    namer = PyTestNamer(request)
    expected = os_path("ApprovalTests.Python/tests/pytest/test_namer.test_pytest_namer.received.txt")
    assert namer.get_received_filename().endswith(expected)
    verify("foo", namer=namer)


def os_path(posix_path):
    return posix_path.replace("/", os.path.sep)

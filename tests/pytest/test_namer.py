from approvaltests.approvals import get_default_namer, verify
from approvaltests.pytest.namer import PyTestNamer


def test_basic_approval():
    verify("foo")


def test_received_filename():
    namer = get_default_namer()
    assert namer.get_received_filename().endswith("ApprovalTests.Python/tests/pytest/test_namer.test_received_filename.received.txt")


def test_pytest_namer(request):
    namer = PyTestNamer(request)
    assert namer.get_received_filename().endswith("ApprovalTests.Python/tests/pytest/test_namer.test_pytest_namer.received.txt")
    verify("foo", namer=namer)


def test_verify_fixture(pytest_verify):
    pytest_verify("foo")

import os

from _pytest.fixtures import FixtureRequest

from approvaltests.approvals import get_default_namer, verify
from approvaltests.integrations.pytest.py_test_namer import PyTestNamer


def test_basic_approval() -> None:
    verify("foo")


def test_received_filename() -> None:
    namer = get_default_namer()
    expected = os_path(
        "/tests/integrations/pytest/test_namer.test_received_filename.received.txt"
    )
    assert namer.get_received_filename().endswith(expected)


def test_pytest_namer(request: FixtureRequest) -> None:
    namer = PyTestNamer(request)
    expected = os_path(
        "/tests/integrations/pytest/test_namer.test_pytest_namer.received.txt"
    )
    assert namer.get_received_filename().endswith(expected)
    verify("foo", namer=namer)


def test_pytest_namer_with_extension(request: FixtureRequest) -> None:
    namer = PyTestNamer(request)
    prefix = os_path("/tests/integrations/pytest/test_namer.test_pytest_namer_with_extension")
    assert namer.get_approved_file(".json").endswith(prefix + ".approved.json")
    assert namer.get_received_file(".json").endswith(prefix + ".received.json")


def os_path(posix_path: str) -> str:
    return posix_path.replace("/", os.path.sep)

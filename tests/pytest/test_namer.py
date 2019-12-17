import os

import pytest

from approvaltests.approvals import get_default_namer, verify, get_pytest_namer


def test_basic_approval():
    verify("foo")


def test_received_filename():
    namer = get_default_namer()
    assert namer.get_received_filename().endswith(
        os.path.normpath("ApprovalTests.Python/tests/pytest/test_namer.test_received_filename.received.txt"))


@pytest.fixture
def pytest_verify(request):
    def pytest_verify(data, reporter=None):
        verify(data, reporter=reporter, namer=get_pytest_namer(request))

    return pytest_verify


def test_pytest_namer_sanity(pytest_verify):
    pytest_verify('Sanity')


@pytest.mark.parametrize('arg', ['Hello, World!'])
def test_pytest_received_filename(arg, request):
    namer = get_pytest_namer(request)
    assert namer.get_received_filename().endswith(
        os.path.normpath(
            "ApprovalTests.Python/tests/pytest/test_namer.test_pytest_received_filename[Hello, World!].received.txt"))


@pytest.mark.parametrize('arg', ['Hello', 'World'])
def test_pytest_namer(arg, pytest_verify):
    pytest_verify('Hello, World!')

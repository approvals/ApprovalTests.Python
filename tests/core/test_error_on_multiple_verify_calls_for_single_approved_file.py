import pytest

from approvaltests import verify, ApprovalException, settings, approvals, Options
from approvaltests.file_approver import FileApprover
from tests.namers.test_templated_namer import TemplatedCustomNamer


def test_multiple_calls_to_verify():
    verify("call to verify")
    interceeding_verify()
    with pytest.raises(ApprovalException):
        verify("call to verify")


def interceeding_verify():
    namer = TemplatedCustomNamer(
        "{test_source_directory}/differenttest.{approved_or_received}.txt"
    )
    verify("# call to verify", options=Options().with_namer(namer))


def test_allow_multiple_verifies_per_method():
    settings().allow_multiple_verify_calls_for_this_method()
    verify("call to verify")
    verify("call to verify")


def test_allow_multiple_verifies_by_lambda():
    filename = approvals.get_default_namer().get_approved_filename()
    FileApprover.add_allowed_duplicates(lambda n: n == filename)
    FileApprover.add_allowed_duplicates(lambda n: False)
    verify("call to verify")
    verify("call to verify")


def test_single_call_to_verify():
    verify("call to verify")


def test_help_message():
    verify(FileApprover.get_duplicate_verify_error_message("<approved_file>"))

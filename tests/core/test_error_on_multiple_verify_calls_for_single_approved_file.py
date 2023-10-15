import pytest

from approvaltests import verify, ApprovalException, settings, approvals, Options
from approvaltests.file_approver import error_on_multiple_verify_calls, FileApprover
from tests.namers.test_templated_namer import TemplatedCustomNamer


def test_multiple_calls_to_verify():
    error_on_multiple_verify_calls(True)
    verify("call to verify")
    verify("# call to verify",options= Options().with_namer(TemplatedCustomNamer("{test_source_directory}/differenttest.{approved_or_received}.txt")))
    with pytest.raises(ApprovalException):
        verify("call to verify")
    error_on_multiple_verify_calls(False)


def test_allow_multiple_verifies_per_method():
    error_on_multiple_verify_calls(True)
    settings().allow_multiple_verify_calls_for_this_method()
    verify("call to verify")
    verify("call to verify")
    error_on_multiple_verify_calls(False)

def test_allow_multiple_verifies_by_lambda():
    error_on_multiple_verify_calls(True)
    filename = approvals.get_default_namer().get_approved_filename()
    FileApprover.add_allowed_duplicates(lambda n: n == filename)
    verify("call to verify")
    verify("call to verify")
    error_on_multiple_verify_calls(False)


def test_single_call_to_verify():
    error_on_multiple_verify_calls(True)
    verify("call to verify")
    error_on_multiple_verify_calls(False)


class multiple_verify_calls_permitted:
    save_variable = None

    def __enter__(self):
        # self.save_variable = current_value
        error_on_multiple_verify_calls(False)

    def __exit__(self, exc_type, exc_val, exc_tb):
        error_on_multiple_verify_calls(True)


def test_allow_multiple_verify_calls_in_one_test():
    error_on_multiple_verify_calls(True)
    # TODO: decided to use Options instead of context manager
    with multiple_verify_calls_permitted():
        verify("call to verify")
        verify("call to verify")
        # new verify("third call to verify")
    error_on_multiple_verify_calls(False)

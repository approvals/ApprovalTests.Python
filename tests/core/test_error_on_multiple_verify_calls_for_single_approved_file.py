from approvaltests import verify
from approvaltests.file_approver import error_on_multiple_verify_calls


#


def test_multiple_calls_to_verify():
    error_on_multiple_verify_calls(True)
    verify("call to verify")
    verify("call to verify")
    error_on_multiple_verify_calls(False)


def test_old_way():
    error_on_multiple_verify_calls(False)
    verify("call to verify")
    verify("call to verify")
    error_on_multiple_verify_calls(False)


def test_single_call_to_verify():
    error_on_multiple_verify_calls(True)
    verify("call to verify")
    error_on_multiple_verify_calls(False)

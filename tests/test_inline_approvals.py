# # important to still include usage of a diff tool
# # also important to only write the verify and it populates the approved text for you
# import pytest
#
#
# def test_inline_approvals_before_running():
#     verify_inline("Hello World")
#
# def test_inline_approvals_after_approving():
#     verify_inline("Hello World","Hello World") <---
#
# def test_inline_approvals_after_approving_with_docstring():
#     '''
#     approved: "GATCCCATACGGGATTTTATATATATACCCCC"
#     '''
#     verify_inline("Hello World")
#
# def test_inline_approvals_after_approving_with_docstring():
#     expected = '''
#     "GATCCCATACGGGATTTTATATATATACCCCC"
#     '''
#     verify_inline("Hello World", expected) <---
#
# def test_inline_approvals_after_approving_with_docstring():
#     verify_inline(
#         result(),
#         """
#         GATCCCATACGGGATTTTATATATATACCCCC
#         """
#         ) <----
#
# def test_inline_approvals_after_approving_with_docstring():
#     verify_inline(
#         result()
#     ).matches_inline_approved(
#         """
#         GATCCCATACGGGATTTTATATATATACCCCC
#         """
#     )
#
from approvaltests import verify, StackFrameNamer


def get_test_method_docstring():
    method = get_caller_method(StackFrameNamer.get_calling_test_frame())
    return method.__doc__

def get_caller_method(caller_frame):
    caller_function_name = caller_frame[3]
    caller_function_object = caller_frame.frame.f_globals.get(caller_function_name, None)
    return caller_function_object


def test_docstrings():
    '''
    hello x world
    '''
    verify(get_test_method_docstring())

#
#

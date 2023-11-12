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


def print_docstring():
    import inspect
    stack_frame_namer = StackFrameNamer()
    stack = inspect.stack(1)
    frame = stack_frame_namer.get_test_frame(stack)
    caller = stack[frame]
    return print_caller_docstring(caller)

def print_caller_docstring(caller_frame):
    import inspect
    caller_function = caller_frame.function
    caller_info = inspect.getmembers(caller_frame.frame)
    for name, data in caller_info:
        if name == 'f_code':
            caller_code = data
            break
    caller_function_name = caller_code.co_name
    caller_function_object = caller_frame.frame.f_globals.get(caller_function_name, None)
    return caller_function_object.__doc__


def test_docstrings():
    '''
    hello x world
    '''
    verify(print_docstring())

#
#

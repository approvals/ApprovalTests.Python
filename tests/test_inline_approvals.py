import sys
import unittest
from inspect import FrameInfo
from typing import Any, Callable

import pytest

from approval_utilities.utilities.multiline_string_utils import remove_indentation_from
from approvaltests import (
    ApprovalException,
    Options,
    StackFrameNamer,
    verify,
    verify_all,
    verify_all_combinations_with_labeled_input,
)
from approvaltests.inline.inline_options import InlineOptions
from approvaltests.inline.markers import PRESERVE_LEADING_WHITESPACE_MARKER
from approvaltests.inline.parse_docstring import parse_docstring
from approvaltests.namer.inline_comparator import InlineComparator
from approvaltests.namer.inline_python_reporter import (
    detect_trailing_whitespace,
    handle_preceeding_whitespace,
)
from approvaltests.reporters.report_quietly import ReportQuietly
from approvaltests.reporters.report_with_beyond_compare import (
    ReportWithBeyondCompare,
    ReportWithPycharm,
)

# Todo:
# detect the actual tab
# detect if the quote type used in the docstring  (i.e. " or ')


def fizz_buzz(param: int) -> str:
    return_string = ""
    for i in range(1, param + 1):
        if i % 15 == 0:
            return_string += "FizzBuzz\n"
        elif i % 3 == 0:
            return_string += "Fizz\n"
        elif i % 5 == 0:
            return_string += "Buzz\n"
        else:
            return_string += str(i) + "\n"
    return return_string


def test_fizz_buzz() -> None:
    """
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    """
    verify(fizz_buzz(8), options=Options().inline())


def test_docstrings() -> None:
    """
    hello
    world
    """
    # verify_inline(greetting())
    # verify(greetting(), options=Options().inline(show_code= False))
    verify(greeting(), options=Options().inline())


def greeting() -> str:
    return "hello\nworld"


def test_docstring_parsing() -> None:
    """
    1
    2 -> 2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    """
    verify_all("inputs", parse_docstring())


def test_uppercase() -> None:
    """
    a -> A
    b -> B
    c -> C
    """
    verify(
        "\n".join([f"{a} -> {a.upper()}" for a in parse_docstring()]),
        options=Options().inline(),
    )


options = Options().inline()


def test_when_options_is_created_outside_of_test() -> None:
    """
    hello
    world
    """
    verify(greeting(), options=options)


def test_exception_on_failure() -> None:
    """
    this string should not match
    """
    with pytest.raises(ApprovalException):
        verify(greeting(), options=Options().with_reporter(ReportQuietly()).inline())


class InlineTests(unittest.TestCase):
    def test_with_labeled_input_inline(self) -> None:
        """
        (arg1: 1, arg2: 2) => 3
        (arg1: 1, arg2: 4) => 5
        (arg1: 3, arg2: 2) => 5
        (arg1: 3, arg2: 4) => 7
        """
        verify_all_combinations_with_labeled_input(
            lambda a, b: a + b,
            arg1=(1, 3),
            arg2=(2, 4),
            options=Options().inline(),
        )


def get_preceding_whitespace() -> str:
    return "    4 whitespaces"


# fmt: off
@unittest.skipIf(sys.version_info >= (3, 13), "__doc__ removes preceding whitespace in Python 3.13+")
def test_preceding_whitespace_before_python_3_13() -> None:
    """
        4 whitespaces
    """
    verify(get_preceding_whitespace(), options=Options().inline())

def test_preceding_whitespace() -> None:
    """
    <<approvaltests:preserve-leading-whitespace>>
        4 whitespaces
    """
    verify(get_preceding_whitespace(), options=Options().inline())


def test_no_preceeding_whitespace() -> None:
    """
        4 whitespaces
    applesauce
    """
    text = "    4 whitespaces\napplesauce"
    verify(text, options=Options().inline())


def test_trailing_whitespace() -> None:
    """
    4 trailing whitespaces    
    """  # Warning: Editors may remove trailing spaces, causing this test to fail

    # Note: Pycharm will remove the trailing whitespaces, to disable this go to:
    # File -> Settings -> Editor -> General -> On Save -> [ ] Remove trailing spaces
    verify("4 trailing whitespaces    ", options=Options().inline())

# fmt: on


def test_bug_blank_lines() -> None:
    """


    test bug with blank lines



    """
    verify("\n\ntest bug with blank lines\n\n\n\n", options=Options().inline())


def test_handle_preceeding_whitespace_all_lines_indented() -> None:
    text = "    indented with spaces\n\tindented with tab\n    still indented"
    result = handle_preceeding_whitespace(text)
    assert result.startswith(PRESERVE_LEADING_WHITESPACE_MARKER)


def test_handle_preceeding_whitespace_one_line_not_indented() -> None:
    text = "    indented with spaces\nnot indented\n\tindented with tab"
    result = handle_preceeding_whitespace(text)
    assert not result.startswith(PRESERVE_LEADING_WHITESPACE_MARKER)


def test_inline_with_additional_reporter() -> None:
    """
    hello
    world
    """
    verify(
        "hello\nworld",
        options=(Options().inline().add_reporter(ReportWithBeyondCompare())),
    )


def test_inline_with_preserved_approved_text() -> None:
    """
    42
    ***** DELETE ME TO APPROVE *****
    vvvvv PREVIOUS RESULT vvvvv
    41
    """
    options = Options().inline(InlineOptions.semi_automatic_with_previous_approved())
    try:
        verify("42", options=options)
    except ApprovalException:
        pass
    verify(InlineComparator.get_test_method_doc_string())


def test_inline_with_semi_automatic_inline() -> None:
    """
    42
    ***** DELETE ME TO APPROVE *****
    """
    options = Options().inline(InlineOptions.semi_automatic())
    try:
        verify("42", options=options)
    except ApprovalException:
        pass
    verify(InlineComparator.get_test_method_doc_string())


def test_detect_trailing_whitespace_true() -> None:
    text = "no trail\nwith trail \t\nnormal"
    assert detect_trailing_whitespace(text)


def test_detect_trailing_whitespace_false() -> None:
    text = "alpha\nbeta\ngamma"
    assert not detect_trailing_whitespace(text)


def test_detect_trailing_whitespace_ignores_pure_empty_lines() -> None:
    text = "line1\n\nline2"
    assert not detect_trailing_whitespace(text)

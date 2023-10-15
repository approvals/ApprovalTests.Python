import argparse
import typing
from abc import ABC

from approvaltests import (
    verify,
    register_formatter,
    find_formatter_for_specified_class,
    approvals,
)
from approvaltests.core.format_wrapper import FormatWrapper
from approvaltests.verifiable_objects.formatter_of_argparse_namespace import (
    FormatterOfArgparseNamespace,
)


def test_argparse_namespace() -> None:
    approvals.settings().allow_multiple_verify_calls_for_this_method()
    args = argparse.ArgumentParser()
    args.add_argument("foo")
    args.add_argument("--foo2")
    result = args.parse_args(["bar", "--foo2=bar2"])
    verify(FormatterOfArgparseNamespace(result))
    verify(result)


def test_register_formatter() -> None:
    class ExampleFormatterWrapper(FormatWrapper):
        def is_match(self, data: typing.Any) -> bool:
            return True

        def wrap(self, data: typing.Any) -> typing.Any:
            return 42

    with register_formatter(ExampleFormatterWrapper()):
        assert 42 == find_formatter_for_specified_class("Some Result")
        verify("Some Result")
    assert "Some Result" == find_formatter_for_specified_class("Some Result")

import argparse
import typing
from abc import ABC

from approvaltests import verify, register_formatter
from approvaltests.core.format_wrapper import FormatWrapper
from approvaltests.verifiable_objects.verifiable_argparse_namespace import ArgparseNamespaceFormatter


def test_argparse_namespace() -> None:
    args = argparse.ArgumentParser()
    args.add_argument("foo")
    args.add_argument("--foo2")
    result = args.parse_args(["bar", "--foo2=bar2"])
    verify(ArgparseNamespaceFormatter(result))
    verify(result)



def test_register_formatter() -> None:
    class ExampleFormatterWrapper(FormatWrapper):

        def is_match(self, data: typing.Any) -> bool:
            return True

        def wrap(self, data: typing.Any) -> typing.Any:
            return 42

    with register_formatter(ExampleFormatterWrapper()):
        verify("Some Result")

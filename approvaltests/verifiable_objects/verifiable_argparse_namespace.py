import abc
import argparse
import typing


class FormatWrapper(abc.ABC):
    @abc.abstractmethod
    def wrap(self, data: typing.Any) -> typing.Any:
        pass

    @abc.abstractmethod
    def is_match(self, data: typing.Any) -> bool:
        pass


class ArgparseNamespaceFormatterWrapper(FormatWrapper):
    def wrap(self, data):
        return ArgparseNamespaceFormatter(data)

    def is_match(self, data) -> bool:
        return isinstance(data, argparse.Namespace)


class ArgparseNamespaceFormatter:
    def __init__(self, result):
        self.result = result

    def __str__(self):
        from approvaltests import to_json
        return to_json(vars(self.result))

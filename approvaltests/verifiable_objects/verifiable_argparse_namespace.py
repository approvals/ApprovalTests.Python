import argparse

from approvaltests.core.format_wrapper import FormatWrapper


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

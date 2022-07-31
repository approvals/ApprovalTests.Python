import abc
import argparse

class FormatWrapper(abc.ABC):
    @abc.abstractmethod
    def wrap(self, data):
        """This method should either return the data wrapped in a formatter if it matches or the original data otherwise"""
        ...

class ArgparseNamespaceFormatterWrapper(FormatWrapper):
    def wrap(self, data):
        if isinstance(data, argparse.Namespace):
            data = ArgparseNamespaceFormatter(data)
        return data

class ArgparseNamespaceFormatter:
    def __init__(self, result ):
        self.result = result



    def __str__(self):
        from approvaltests import to_json
        return to_json(vars(self.result))

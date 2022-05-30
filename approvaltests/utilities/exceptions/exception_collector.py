from typing import Callable, Sequence, Any

from approvaltests.utilities.exceptions.multiple_exceptions import MultipleExceptions


class ExceptionCollector:
    def __init__(self):
        self._exceptions = []

    def gather(self, callable: Callable):
        try:
            callable()
        except Exception as exception:
            self._exceptions.append(exception)

    def release(self):
        if len(self._exceptions) == 0:
            return
        if len(self._exceptions) == 1:
            raise self._exceptions[0]

        raise MultipleExceptions(self._exceptions)


def gather_all_exceptions(parameters: Sequence[Any], callable: Callable[[Any], Any]) -> ExceptionCollector:
    collector = ExceptionCollector()
    for p in parameters:
        collector.gather(lambda: callable(p))

    return collector


def gather_all_exceptions_and_throw(parameters: Sequence[Any], callable: Callable[[Any], Any]) -> None:
    gather_all_exceptions(parameters, callable).release()

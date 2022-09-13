import inspect
from contextlib import contextmanager
from typing import Iterator

from approvaltests.utilities.string_wrapper import StringWrapper
from build.lib.approvaltests.namer import StackFrameNamer


class SimpleLogger:
    logger = print

    @staticmethod
    def log_to_string():
        buffer = StringWrapper()
        SimpleLogger.logger = buffer.append
        return buffer

    @staticmethod
    @contextmanager
    def use_markers() -> Iterator[None]:
        stack = inspect.stack(1)[2]
        method_name = stack[3]
        filename = StackFrameNamer.get_class_name_for_frame(stack)
        expected = f"-> in: {method_name}(){filename}"
        SimpleLogger.log(expected)
        yield
        expected = f"<- out: {method_name}(){filename}"
        SimpleLogger.log(expected)
        pass

    @staticmethod
    def log(expected):
        SimpleLogger.logger(f"{expected}\n")

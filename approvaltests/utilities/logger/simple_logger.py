from contextlib import contextmanager
from typing import Iterator

from approvaltests.utilities.logger.logging_instance import LoggingInstance


class SimpleLogger:
    logger = LoggingInstance()

    @staticmethod
    def log_to_string():
        return SimpleLogger.logger.log_to_string()

    @staticmethod
    def use_markers() -> Iterator[None]:
        return SimpleLogger.logger.use_markers(additional_stack=1)

    @staticmethod
    def variable(type: str, value):
        SimpleLogger.logger.variable(type, value)

    @staticmethod
    def hour_glass():
        SimpleLogger.logger.hour_glass()

    @staticmethod
    def event(input):
        SimpleLogger.logger.event(input)

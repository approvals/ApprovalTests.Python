from typing import Iterator, Any

from approvaltests.utilities.logger.logging_instance import LoggingInstance
from approvaltests.utilities.string_wrapper import StringWrapper


class SimpleLogger:
    logger = LoggingInstance()

    @staticmethod
    def log_to_string() -> StringWrapper:
        return SimpleLogger.logger.log_to_string()

    @staticmethod
    def use_markers() -> Iterator[None]:
        return SimpleLogger.logger.use_markers(additional_stack=1)

    @staticmethod
    def variable(name: str, value: Any) -> None:
        SimpleLogger.logger.variable(name, value)

    @staticmethod
    def hour_glass() -> None:
        SimpleLogger.logger.hour_glass()

    @staticmethod
    def event(event_name: str) -> None:
        SimpleLogger.logger.event(event_name)

    @staticmethod
    def show_timestamps(display: bool) -> None:
        SimpleLogger.logger.log_with_timestamps = display

    @staticmethod
    def query(query_text: str) -> None:
        SimpleLogger.logger.query(query_text)

    @staticmethod
    def message(message: str) -> None:
        SimpleLogger.logger.message(message)

    @staticmethod
    def warning(text: str = "", exception: Exception = None) -> None:
        SimpleLogger.logger.warning(text, exception)

    @staticmethod
    def show_queries(show: bool):
        SimpleLogger.logger.show_queries(show)

    @staticmethod
    def show_all(show: bool):
        SimpleLogger.logger.show_all(show)

    @staticmethod
    def show_messages(show: bool):
        SimpleLogger.logger.show_messages(show)

    @staticmethod
    def show_variables(show: bool):
        SimpleLogger.logger.show_variables(show)

    @staticmethod
    def show_hour_glass(show: bool):
        SimpleLogger.logger.show_hour_glass(show)

    @staticmethod
    def show_markers(show: bool):
        SimpleLogger.logger.show_markers(show)

    @staticmethod
    def show_events(show: bool):
        SimpleLogger.logger.show_events(show)

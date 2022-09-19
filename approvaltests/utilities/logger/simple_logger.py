from typing import Iterator, Any, Callable

from approvaltests.utilities.logger.logging_instance import LoggingInstance
from approvaltests.utilities.string_wrapper import StringWrapper


class SimpleLogger:
    _logger = LoggingInstance()

    @staticmethod
    def register_logger(log_method: Callable[[str], None]) -> None:
        SimpleLogger._logger.logger = log_method

    @staticmethod
    def log_to_string() -> StringWrapper:
        return SimpleLogger._logger.log_to_string()

    @staticmethod
    def use_markers() -> Iterator[None]:
        return SimpleLogger._logger.use_markers(additional_stack=1)

    @staticmethod
    def variable(name: str, value: Any, show_types: bool = False) -> None:
        SimpleLogger._logger.variable(name, value, show_types=show_types)

    @staticmethod
    def hour_glass() -> None:
        SimpleLogger._logger.hour_glass()

    @staticmethod
    def event(event_name: str) -> None:
        SimpleLogger._logger.event(event_name)

    @staticmethod
    def show_timestamps(display: bool) -> None:
        SimpleLogger._logger.log_with_timestamps = display

    @staticmethod
    def query(query_text: str) -> None:
        SimpleLogger._logger.query(query_text)

    @staticmethod
    def message(message: str) -> None:
        SimpleLogger._logger.message(message)

    @staticmethod
    def warning(text: str = "", exception: BaseException = None) -> None:
        SimpleLogger._logger.warning(text, exception)

    @staticmethod
    def show_queries(show: bool):
        SimpleLogger._logger.show_queries(show)

    @staticmethod
    def show_all(show: bool):
        SimpleLogger._logger.show_all(show)

    @staticmethod
    def show_messages(show: bool):
        SimpleLogger._logger.show_messages(show)

    @staticmethod
    def show_variables(show: bool):
        SimpleLogger._logger.show_variables(show)

    @staticmethod
    def show_hour_glass(show: bool):
        SimpleLogger._logger.show_hour_glass(show)

    @staticmethod
    def show_markers(show: bool):
        SimpleLogger._logger.show_markers(show)

    @staticmethod
    def show_events(show: bool):
        SimpleLogger._logger.show_events(show)

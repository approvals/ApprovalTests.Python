import threading
from abc import ABC, abstractmethod
from typing import Iterator, Any, Callable

from approvaltests.utilities.logger.logging_instance import LoggingInstance
from approvaltests.utilities.string_wrapper import StringWrapper


class Wrapper(ABC):
    @abstractmethod
    def get(self):
        pass


class SingleWrapper(Wrapper):
    def __init__(self, instance):
        self.instance = instance

    def get(self):
        return self.instance

class ThreadedWrapper(Wrapper):
    def __init__(self, generator):
        self.generator = generator
        self.local = threading.local()
        self.local.value = None

    def get(self):
        if not self.local.value:
            self.local.value = self.generator()
        return self.local.value


class SimpleLogger:
    _wrapper = SingleWrapper(LoggingInstance())

    @staticmethod
    def register_logger(log_method: Callable[[str], None]) -> None:
        SimpleLogger._wrapper.get().logger = log_method

    @staticmethod
    def log_to_string() -> StringWrapper:
        # assign a new wrapper to SimpleLogger
        # pass a generator into that wrapper that creates a logging instance
        def generator() -> LoggingInstance:
            return LoggingInstance()


        SimpleLogger._wrapper = ThreadedWrapper(generator)
        return SimpleLogger._wrapper.get().log_to_string()

    @staticmethod
    def use_markers(parameter_text: [str, Callable[[], str]] = None) -> Iterator[None]:
        return SimpleLogger._wrapper.get().use_markers(parameter_text, additional_stack=1)

    @staticmethod
    def variable(name: str, value: Any, show_types: bool = False) -> None:
        SimpleLogger._wrapper.get().variable(name, value, show_types=show_types)

    @staticmethod
    def hour_glass() -> None:
        SimpleLogger._wrapper.get().hour_glass()

    @staticmethod
    def event(event_name: str) -> None:
        SimpleLogger._wrapper.get().event(event_name)

    @staticmethod
    def show_timestamps(display: bool) -> None:
        SimpleLogger._wrapper.get().log_with_timestamps = display

    @staticmethod
    def query(query_text: str) -> None:
        SimpleLogger._wrapper.get().query(query_text)

    @staticmethod
    def message(message: str) -> None:
        SimpleLogger._wrapper.get().message(message)

    @staticmethod
    def warning(text: str = "", exception: BaseException = None) -> None:
        SimpleLogger._wrapper.get().warning(text, exception)

    @staticmethod
    def show_queries(show: bool):
        SimpleLogger._wrapper.get().show_queries(show)

    @staticmethod
    def show_all(show: bool):
        SimpleLogger._wrapper.get().show_all(show)

    @staticmethod
    def show_messages(show: bool):
        SimpleLogger._wrapper.get().show_messages(show)

    @staticmethod
    def show_variables(show: bool):
        SimpleLogger._wrapper.get().show_variables(show)

    @staticmethod
    def show_hour_glass(show: bool):
        SimpleLogger._wrapper.get().show_hour_glass(show)

    @staticmethod
    def show_markers(show: bool):
        SimpleLogger._wrapper.get().show_markers(show)

    @staticmethod
    def show_events(show: bool):
        SimpleLogger._wrapper.get().show_events(show)

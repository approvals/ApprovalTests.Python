import datetime
import inspect
from contextlib import contextmanager
from typing import Iterator, Callable

from approvaltests.utilities.string_wrapper import StringWrapper
from approvaltests.namer import StackFrameNamer


class SimpleLogger:
    previous_timestamp = None
    logger = lambda t: print(t, end="")
    tabbing = 0
    counter = 0
    timestamp = True
    timer: Callable[[],datetime.datetime] = datetime.datetime.now

    @staticmethod
    def log_to_string():
        buffer = StringWrapper()
        SimpleLogger.logger = buffer.append
        SimpleLogger.timestamp = False
        return buffer

    @staticmethod
    @contextmanager
    def use_markers() -> Iterator[None]:
        stack = inspect.stack(1)[2]
        method_name = stack[3]
        filename = StackFrameNamer.get_class_name_for_frame(stack)
        expected = f"-> in: {method_name}(){filename}"
        SimpleLogger.log(expected)
        SimpleLogger.tabbing = SimpleLogger.tabbing + 1
        yield
        SimpleLogger.tabbing = SimpleLogger.tabbing - 1
        expected = f"<- out: {method_name}(){filename}"
        SimpleLogger.log(expected)
        pass

    @staticmethod
    def log(log_output):
        if SimpleLogger.counter != 0:
            SimpleLogger.logger("\n")
            SimpleLogger.counter = 0
        timestamp = ""
        if SimpleLogger.timestamp:
            time1: datetime.datetime = SimpleLogger.timer()
            time = time1.strftime("%Y-%m-%dT%H:%M:%SZ")
            diff_millseconds = 0
            if SimpleLogger.previous_timestamp != None:
                delta = time1 - SimpleLogger.previous_timestamp
                diff_millseconds = int((delta).total_seconds() * 1000)
            diff = diff_millseconds
            diff_display = f" ~{diff:06}ms"
            timestamp = f"[{time} {diff_display}] "
            SimpleLogger.previous_timestamp = time1
        SimpleLogger.logger(f"{timestamp}{SimpleLogger.get_tabs()}{log_output}\n")

    @staticmethod
    def variable(type: str, value):
        display_variable = f"variable: {type} = {value}"
        SimpleLogger.log(display_variable)

    @staticmethod
    def hour_glass():
        SimpleLogger.increment_hour_glass_counter()
        if SimpleLogger.counter == 1:
            SimpleLogger.logger(f"{SimpleLogger.get_tabs()}.")
        elif SimpleLogger.counter == 100:
            SimpleLogger.logger("10\n")
            SimpleLogger.counter = 0
        elif SimpleLogger.counter % 10 == 0:
            digit = int(SimpleLogger.counter / 10)
            SimpleLogger.logger(f"{digit}")
        else:
            SimpleLogger.logger(".")

    @staticmethod
    def get_tabs():
        return "  " * SimpleLogger.tabbing

    @staticmethod
    def increment_hour_glass_counter():
        SimpleLogger.counter = SimpleLogger.counter + 1

    @staticmethod
    def event(input):
        SimpleLogger.log(f"event: {input}")

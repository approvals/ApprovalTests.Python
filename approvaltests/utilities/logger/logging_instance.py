import datetime
import inspect
from contextlib import contextmanager
from typing import Iterator, Callable

from approvaltests.utilities.string_wrapper import StringWrapper
from approvaltests.namer import StackFrameNamer


class LoggingInstance:
    
    def __init__(self):
        self.previous_timestamp = None
        self.logger = lambda t: print(t, end="")
        self.tabbing = 0
        self.counter = 0
        self.timestamp = True
        self.timer: Callable[[], datetime.datetime] = datetime.datetime.now
    
    def log_to_string(self):
        buffer = StringWrapper()
        self.logger = buffer.append
        self.timestamp = False
        return buffer

    
    @contextmanager
    def use_markers(self, additional_stack=0) -> Iterator[None]:
        stack = inspect.stack(1+additional_stack)[2]
        method_name = stack[3]
        filename = StackFrameNamer.get_class_name_for_frame(stack)
        expected = f"-> in: {method_name}(){filename}"
        self.log(expected)
        self.tabbing = self.tabbing + 1
        yield
        self.tabbing = self.tabbing - 1
        expected = f"<- out: {method_name}(){filename}"
        self.log(expected)
        pass

    
    def log(self, log_output):
        if self.counter != 0:
            self.logger("\n")
            self.counter = 0
        timestamp = ""
        if self.timestamp:
            time1: datetime.datetime = self.timer()
            time = time1.strftime("%Y-%m-%dT%H:%M:%SZ")
            diff_millseconds = 0
            if self.previous_timestamp != None:
                delta = time1 - self.previous_timestamp
                diff_millseconds = int((delta).total_seconds() * 1000)
            diff = diff_millseconds
            diff_display = f" ~{diff:06}ms"
            timestamp = f"[{time} {diff_display}] "
            self.previous_timestamp = time1
        self.logger(f"{timestamp}{self.get_tabs()}{log_output}\n")

    
    def variable(self, type: str, value):
        display_variable = f"variable: {type} = {value}"
        self.log(display_variable)

    
    def hour_glass(self):
        self.increment_hour_glass_counter()
        if self.counter == 1:
            self.logger(f"{self.get_tabs()}.")
        elif self.counter == 100:
            self.logger("10\n")
            self.counter = 0
        elif self.counter % 10 == 0:
            digit = int(self.counter / 10)
            self.logger(f"{digit}")
        else:
            self.logger(".")

    
    def get_tabs(self):
        return "  " * self.tabbing

    
    def increment_hour_glass_counter(self):
        self.counter = self.counter + 1

    
    def event(self, input):
        self.log(f"event: {input}")

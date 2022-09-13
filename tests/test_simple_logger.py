import inspect
from collections.abc import MutableSequence
from contextlib import contextmanager
from typing import Iterator

from approvaltests import verify
from build.lib.approvaltests.namer import StackFrameNamer


class StringWrapper():
    def __init__(self):
        self.string = ""

    def append(self, text):
        self.string += text

    def __str__(self):
        return self.string

class SimpleLogger:
    logger = print

    @staticmethod
    def log_to_string():
        buffer = StringWrapper()
        SimpleLogger.logger =  buffer.append
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


def test_standard_logger():
    '''
      let output = SimpleLogger.logToString()
        do {
            let m = SimpleLogger.useMarkers()
            SimpleLogger.printLineNumber()
            do {
                let m2 = SimpleLogger.useMarkers()
                let name = "llewellyn"
                SimpleLogger.variable("name", name)
                for _ in 0 ..< 142 {
                    SimpleLogger.hourGlass()
                }
            }
        }
        try Approvals.verify(output)
    '''
    output = SimpleLogger.log_to_string()
    with SimpleLogger.use_markers() as m :
        pass
    verify(output)
    """
    
-> in: test_standard_logger()test_simple_logger.py
<- out: test_standard_logger()test_simple_logger.py
    """
    
    
        

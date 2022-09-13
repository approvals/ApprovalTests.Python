from collections.abc import MutableSequence
from contextlib import contextmanager
from typing import Iterator

from approvaltests import verify

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
        def string_logger(text):
            nonlocal buffer
            buffer.append(text)
        SimpleLogger.logger =  string_logger
        return buffer

    @staticmethod
    @contextmanager
    def use_markers() -> Iterator[None]:
        expected = "-> in: test_standard_logger()test_simple_logger.py"
        SimpleLogger.log(expected)
        yield
        expected = "<- out: test_standard_logger()test_simple_logger.py"
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
    
    
        

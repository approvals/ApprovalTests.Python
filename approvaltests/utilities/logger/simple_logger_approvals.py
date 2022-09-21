from typing import ContextManager

from approvaltests import SimpleLogger, verify


def verify_simple_logger()-> ContextManager:
    class VerifySimpleLogger():
        def __init__(self):
            self.output = SimpleLogger.log_to_string()
        def __enter__(self):
            pass
        def __exit__(self, exc_type, exc_val, exc_tb):
            verify(self.output)
    return VerifySimpleLogger()

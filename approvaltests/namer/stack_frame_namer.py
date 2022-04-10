import inspect
import os
from inspect import FrameInfo
from typing import Optional, Dict, List

from approvaltests.namer.namer_base import NamerBase
from approvaltests.approval_exception import FrameNotFound


class StackFrameNamer(NamerBase):
    directory = ""
    method_name = ""
    class_name = ""

    def __init__(self, extension: Optional[str] = None) -> None:
        NamerBase.__init__(self, extension)
        self.set_for_stack(inspect.stack(1))
        self.config: Dict[str, str] = {}
        self.config_loaded = False

    def set_for_stack(self, caller: List[FrameInfo]) -> None:
        frame = self.get_test_frame(caller)
        stacktrace = caller[frame]
        self.method_name = stacktrace[3]
        self.class_name = self.get_class_name_for_frame(stacktrace)
        self.directory = os.path.dirname(stacktrace[1])

    @staticmethod
    def get_class_name_for_frame(stacktrace: FrameInfo) -> str:
        return (
            os.path.splitext(os.path.basename(stacktrace[1]))[0]
            if "self" not in stacktrace[0].f_locals
            else f"{stacktrace[0].f_locals['self'].__class__.__name__}"
        )

    def get_test_frame(self, caller: List[FrameInfo]) -> int:
        if tmp_array := [
            index
            for index, frame in enumerate(caller)
            if self.is_test_method(frame)
        ]:
            return tmp_array[-1]
        message = """Could not find test method/function. Possible reasons could be:
1) approvaltests is not being used inside a test function
2) your test framework is not supported by ApprovalTests (unittest and pytest are currently supported)."""
        raise FrameNotFound(message)

    @staticmethod
    def is_test_method(frame: FrameInfo) -> bool:
        method_name = frame[3]
        is_unittest_test = (
            "self" in frame[0].f_locals
            and "_testMethodName" in frame[0].f_locals["self"].__dict__
            and method_name != "__call__"
            and method_name != "_callTestMethod"
            and method_name != "run"
        )

        is_pytest_test = method_name.startswith("test_")

        return is_unittest_test or is_pytest_test

    def get_class_name(self) -> str:
        return self.class_name

    def get_method_name(self) -> str:
        return self.method_name

    def get_directory(self) -> str:
        return self.directory

    def config_directory(self) -> str:
        return self.directory

    def get_file_name(self) -> str:
        class_name = "" if self.class_name is None else f'{self.class_name}.'
        return class_name + self.method_name

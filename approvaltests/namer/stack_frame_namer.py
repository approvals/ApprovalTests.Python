import inspect
import os
from inspect import FrameInfo

from typing_extensions import override

from approval_utilities.utilities.stack_frame_utilities import get_class_name_for_frame
from approvaltests.namer import stack_walker
from approvaltests.namer.namer_base import NamerBase


class StackFrameNamer(NamerBase):
    directory = ""
    method_name = ""
    class_name = ""

    def __init__(self, extension: str | None = None) -> None:
        NamerBase.__init__(self, extension)
        self.set_for_stack(inspect.stack(1))
        self.config: dict[str, str] = {}
        self.config_loaded = False

    def set_for_stack(self, caller: list[FrameInfo]) -> None:
        frame = stack_walker.get_test_frame_index(caller)
        stacktrace = caller[frame]
        self.method_name = stacktrace[3]
        self.class_name = get_class_name_for_frame(stacktrace)
        self.directory = os.path.dirname(stacktrace[1])

    @staticmethod
    def get_test_frame_index(caller: list[FrameInfo]) -> int:
        return stack_walker.get_test_frame_index(caller)

    @staticmethod
    def is_pytest_test(frame: FrameInfo) -> bool:
        return stack_walker.is_pytest_test(frame)

    UNITTEST_EXCLUDED_METHOD_NAMES = stack_walker.UNITTEST_EXCLUDED_METHOD_NAMES

    @staticmethod
    def is_unittest_test(frame: FrameInfo) -> bool:
        return stack_walker.is_unittest_test(frame)

    @staticmethod
    def is_test_method(frame: FrameInfo) -> bool:
        return stack_walker.is_test_method(frame)

    def get_class_name(self) -> str:
        return self.class_name

    def get_method_name(self) -> str:
        return self.method_name

    @override
    def get_directory(self) -> str:
        return self.directory

    @override
    def config_directory(self) -> str:
        return self.directory

    @override
    def get_file_name(self) -> str:
        class_name = "" if (self.class_name is None) else (self.class_name + ".")
        return class_name + self.method_name

    def get_extension_with_dot(self) -> str:
        return self.extension_with_dot

    def get_extension_without_dot(self) -> str:
        return self.extension_with_dot[1:]

    @classmethod
    def get_test_frame(cls) -> FrameInfo:
        return stack_walker.get_test_frame()

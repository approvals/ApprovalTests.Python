import inspect
import os
from inspect import FrameInfo

from typing_extensions import override

from approval_utilities.utilities.stack_frame_utilities import get_class_name_for_frame
from approvaltests.namer import stack_walker
from approvaltests.namer.namer_base import NamerBase
from approvaltests.namer.templated_custom_namer import (
    TemplatedCustomNamer,
    TemplateFieldValues,
)


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

    def _overrides_get_file_name(self) -> bool:
        return type(self).get_file_name is not StackFrameNamer.get_file_name

    def _get_field_values(self) -> TemplateFieldValues:
        test_file_name = (
            self.get_file_name() if self._overrides_get_file_name() else self.class_name
        )
        return TemplateFieldValues(
            approved_or_received="",
            approvals_subdirectory=self.get_config().get("subdirectory", ""),
            file_extension="",
            relative_test_source_directory=os.path.relpath(
                self.get_directory()
            ).replace(os.sep, "/"),
            test_case_name=self.method_name,
            test_file_name=test_file_name,
            test_source_directory=self.get_directory(),
            additional_information="",
        )

    def _create_filename(self, approved_or_received: str) -> str:
        template = TemplatedCustomNamer.DEFAULT_TEMPLATE
        if self._overrides_get_file_name():
            template = (
                "{test_source_directory}/{approvals_subdirectory}/"
                "{test_file_name}.{approved_or_received}.{file_extension}"
            )
        values = self._get_field_values().with_(
            approved_or_received, self.extension_with_dot[1:]
        )
        return TemplatedCustomNamer.create_filename(template, values)

    @override
    def get_basename(self) -> str:
        template = "{test_source_directory}/{approvals_subdirectory}/{test_file_name}"
        if not self._overrides_get_file_name():
            template += ".{test_case_name}"
        return TemplatedCustomNamer.create_filename(template, self._get_field_values())

    @override
    def get_approved_filename(self) -> str:
        return self._create_filename(self.APPROVED_WITHOUT_DOT)

    @override
    def get_received_filename(self) -> str:
        return self._create_filename(self.RECEIVED_WITHOUT_DOT)

    def get_extension_with_dot(self) -> str:
        return self.extension_with_dot

    def get_extension_without_dot(self) -> str:
        return self.extension_with_dot[1:]

    @classmethod
    def get_test_frame(cls) -> FrameInfo:
        return stack_walker.get_test_frame()

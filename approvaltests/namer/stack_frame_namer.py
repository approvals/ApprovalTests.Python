import inspect
import os
from inspect import FrameInfo

from typing_extensions import override

from approval_utilities.utilities.stack_frame_utilities import get_class_name_for_frame
from approvaltests.core.namer import Namer
from approvaltests.namer import stack_walker
from approvaltests.namer.template_field_values import TemplateFieldValues
from approvaltests.namer.templated_custom_namer import TemplatedCustomNamer


class StackFrameNamer(Namer):
    directory = ""
    method_name = ""
    class_name = ""

    def __init__(self, additional_information: str = "") -> None:
        self.additional_information = additional_information
        self.set_for_stack(inspect.stack(1))
        self.config: dict[str, str] = {}
        self.config_loaded = False

    def set_for_stack(self, caller: list[FrameInfo]) -> None:
        frame = stack_walker.get_test_frame_index(caller)
        stacktrace = caller[frame]
        self.method_name = stacktrace[3]
        self.class_name = get_class_name_for_frame(stacktrace)
        self.directory = os.path.dirname(stacktrace[1])

    def get_class_name(self) -> str:
        return self.class_name

    def get_method_name(self) -> str:
        return self.method_name

    def get_directory(self) -> str:
        return self.directory

    def get_config(self) -> dict[str, str]:
        """lazy load config when we need it, then store it in the instance variable self.config"""
        if not self.config_loaded:
            self.config = stack_walker.load_config(self.get_directory())
            self.config_loaded = True
        return self.config

    def get_file_name(self) -> str:
        class_name = "" if (self.class_name is None) else (self.class_name + ".")
        return class_name + self.method_name

    def _overrides_get_file_name(self) -> bool:
        return type(self).get_file_name is not StackFrameNamer.get_file_name

    def get_template_field_values(self) -> TemplateFieldValues:
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
            additional_information=self.additional_information,
        )

    def get_template(self) -> str:
        if self._overrides_get_file_name():
            return (
                "{test_source_directory}/{approvals_subdirectory}/"
                "{test_file_name}{additional_information}.{approved_or_received}.{file_extension}"
            )
        return TemplatedCustomNamer.DEFAULT_TEMPLATE

    def _create_filename(
        self, approved_or_received: str, extension_with_dot: str
    ) -> str:
        template = self.get_template()
        values = self.get_template_field_values().with_(
            approved_or_received, extension_with_dot[1:]
        )
        return os.path.normpath(TemplatedCustomNamer.create_filename(template, values))

    def get_basename(self) -> str:
        template = "{test_source_directory}/{approvals_subdirectory}/{test_file_name}"
        if not self._overrides_get_file_name():
            template += ".{test_case_name}"
        return os.path.normpath(
            TemplatedCustomNamer.create_filename(
                template, self.get_template_field_values()
            )
        )

    @override
    def get_approved_file(self, extension_with_dot: str) -> str:
        return self._create_filename(self.APPROVED_WITHOUT_DOT, extension_with_dot)

    @override
    def get_received_file(self, extension_with_dot: str) -> str:
        return self._create_filename(self.RECEIVED_WITHOUT_DOT, extension_with_dot)

    @classmethod
    def get_test_frame(cls) -> FrameInfo:
        return stack_walker.get_test_frame()

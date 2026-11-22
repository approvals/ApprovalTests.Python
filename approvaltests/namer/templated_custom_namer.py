import os
from dataclasses import asdict, replace

from typing_extensions import override

from approval_utilities.utilities.stack_frame_utilities import get_class_name_for_frame
from approvaltests.core.namer import Namer
from approvaltests.namer import stack_walker
from approvaltests.namer.template_field_values import TemplateFieldValues
from approvaltests.namer.template_fields import TemplateFields  # noqa: F401


class TemplatedCustomNamer(Namer):
    DEFAULT_TEMPLATE = (
        "{test_source_directory}/{approvals_subdirectory}/"
        "{test_file_name}.{test_case_name}{additional_information}.{approved_or_received}.{file_extension}"
    )

    def __init__(self, template: str) -> None:
        self.template = template
        self._template_field_values = self.get_template_fields_from_stacktrace()
        self.approvals_subdirectory: str | None = None
        self.additional_information: str | None = None

    @override
    def get_approved_file(self, extension_with_dot: str) -> str:
        return self._format_with_extension(
            self.APPROVED_WITHOUT_DOT, extension_with_dot
        )

    @override
    def get_received_file(self, extension_with_dot: str) -> str:
        return self._format_with_extension(
            self.RECEIVED_WITHOUT_DOT, extension_with_dot
        )

    def _format_with_extension(
        self, approved_or_received: str, extension_with_dot: str
    ) -> str:
        fields = self.get_template_field_values().with_(
            approved_or_received, extension_with_dot[1:]
        )
        return TemplatedCustomNamer.create_filename(self.template, fields)

    def get_template_field_values(self) -> TemplateFieldValues:
        fields = self._template_field_values
        if self.approvals_subdirectory is not None:
            fields = replace(fields, approvals_subdirectory=self.approvals_subdirectory)
        if self.additional_information:
            fields = fields.add_additional_information(self.additional_information)
        return fields

    def get_template(self) -> str:
        return self.template

    @staticmethod
    def create_filename(template: str, values: TemplateFieldValues) -> str:
        return template.format_map(asdict(values)).replace("//", "/")

    @staticmethod
    def get_template_fields_from_stacktrace() -> TemplateFieldValues:
        frame = stack_walker.get_test_frame()
        directory = os.path.dirname(frame[1])
        return TemplateFieldValues(
            approved_or_received="",
            approvals_subdirectory=stack_walker.load_config(directory).get(
                "subdirectory", ""
            ),
            file_extension="",
            relative_test_source_directory=os.path.relpath(directory).replace(
                os.sep, "/"
            ),
            test_case_name=frame[3],
            test_file_name=get_class_name_for_frame(frame),
            test_source_directory=directory,
            additional_information="",
        )

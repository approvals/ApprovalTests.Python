import os

from typing_extensions import override

from approvaltests import Namer
from approvaltests.namer import stack_walker


class TemplateFields:
    approved_or_received = "approved_or_received"
    test_file_name = "test_file_name"
    test_case_name = "test_case_name"
    file_extension = "file_extension"
    test_source_directory = "test_source_directory"
    relative_test_source_directory = "relative_test_source_directory"
    approvals_subdirectory = "approvals_subdirectory"


class TemplatedCustomNamer(Namer):
    DEFAULT_TEMPLATE = (
        "{test_source_directory}/{approvals_subdirectory}/"
        "{test_file_name}.{test_case_name}.{approved_or_received}.{file_extension}"
    )

    def __init__(self, template: str) -> None:
        self.template = template
        self.extension_with_dot = ".txt"
        self.approvals_subdirectory: str | None = None

    def set_extension(self, extension_with_dot: str) -> None:
        self.extension_with_dot = extension_with_dot

    @override
    def get_received_filename(self) -> str:
        return self.format_filename(self.RECEIVED_WITHOUT_DOT)

    @override
    def get_approved_filename(self) -> str:
        return self.format_filename(self.APPROVED_WITHOUT_DOT)

    def format_filename(self, approved_or_received: str) -> str:
        fields = self.get_template_fields_from_stacktrace()
        fields[TemplateFields.approved_or_received] = approved_or_received
        if self.approvals_subdirectory is not None:
            fields[TemplateFields.approvals_subdirectory] = self.approvals_subdirectory
        fields[TemplateFields.file_extension] = self.extension_with_dot[1:]
        return TemplatedCustomNamer.create_filename(self.template, fields)

    @staticmethod
    def create_filename(template: str, fields: dict[str, str]) -> str:
        return template.format_map(fields).replace("//", "/")

    @staticmethod
    def get_template_fields_from_stacktrace() -> dict[str, str]:
        frame = stack_walker.get_test_frame()
        directory = os.path.dirname(frame[1])
        return {
            TemplateFields.test_file_name: stack_walker.get_class_name_of_frame(frame),
            TemplateFields.test_case_name: frame[3],
            TemplateFields.test_source_directory: directory,
            TemplateFields.relative_test_source_directory: os.path.relpath(
                directory
            ).replace(os.sep, "/"),
            TemplateFields.approvals_subdirectory: stack_walker.load_config(
                directory
            ).get("subdirectory", ""),
        }

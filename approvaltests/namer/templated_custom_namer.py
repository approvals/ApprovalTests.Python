import os

from typing_extensions import override

from approvaltests import Namer, StackFrameNamer


class TemplateFields:
    approved_or_received = "approved_or_received"
    test_file_name = "test_file_name"
    test_case_name = "test_case_name"
    file_extension = "file_extension"
    test_source_directory = "test_source_directory"
    relative_test_source_directory = "relative_test_source_directory"
    approvals_subdirectory = "approvals_subdirectory"


class TemplatedCustomNamer(Namer):
    def __init__(self, template: str) -> None:
        self.template = template
        self.namer_parts = StackFrameNamer()

    def set_extension(self, extension_with_dot: str) -> None:
        self.namer_parts.set_extension(extension_with_dot)

    @override
    def get_received_filename(self) -> str:
        return self.format_filename(self.RECEIVED_WITHOUT_DOT)

    @override
    def get_approved_filename(self) -> str:
        return self.format_filename(self.APPROVED_WITHOUT_DOT)

    def format_filename(self, approved_or_received: str) -> str:
        return self.template.format_map(
            {
                TemplateFields.approved_or_received: approved_or_received,
                TemplateFields.test_file_name: self.namer_parts.get_class_name(),
                TemplateFields.test_case_name: self.namer_parts.get_method_name(),
                TemplateFields.file_extension: self.namer_parts.get_extension_without_dot(),
                TemplateFields.test_source_directory: self.namer_parts.directory,
                TemplateFields.relative_test_source_directory: os.path.relpath(
                    self.namer_parts.directory
                ).replace(os.sep, "/"),
                TemplateFields.approvals_subdirectory: self.namer_parts.get_config().get(
                    "subdirectory", ""
                ),
            }
        )

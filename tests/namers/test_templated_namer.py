from typing import Optional

from approval_utilities.utilities.markdown_table import MarkdownTable
from approvaltests import Namer, StackFrameNamer, verify_as_json, Options, verify



class TemplateFields:
    approved_or_received = "approved_or_received"
    test_file_name = "test_file_name"
    test_case_name = "test_case_name"
    file_extension = "file_extension"
    test_source_directory = "test_source_directory"
    # TODO - the following are not supported yet
    relative_test_source_directory = "relative_test_source_directory"
    approvals_subdirectory = "approvals_subdirectory"


class TemplatedCustomNamer(Namer):
    def __init__(self, template: str) -> None:
        self.template = template
        self.namer_parts = StackFrameNamer()

    def set_extension(self, extension_with_dot: str) -> None:
        self.namer_parts.set_extension(extension_with_dot)

    def get_received_filename(self, base: Optional[str] = None) -> str:
        return self.format_filename(self.RECEIVED_WITHOUT_DOT)

    def get_approved_filename(self, base: Optional[str] = None) -> str:
        return self.format_filename(self.APPROVED_WITHOUT_DOT)

    def format_filename(self, approved_or_received):
        return self.template.format_map(
            {TemplateFields.approved_or_received: approved_or_received,
             TemplateFields.test_file_name: self.namer_parts.get_class_name(),
             TemplateFields.test_case_name: self.namer_parts.get_method_name(),
             TemplateFields.file_extension: self.namer_parts.get_extension_without_dot(),
             TemplateFields.test_source_directory: self.namer_parts.directory})


def test_template_fields():
    table = MarkdownTable().with_headers("template", "usage")
    for fields in dir(TemplateFields):
        if not fields.startswith("__"):
            table.add_rows(fields, f"{{{fields}}}")
    verify(table)


def test_get_received_filename():
    namer = TemplatedCustomNamer(
        "/my/source/directory/{approved_or_received}/{test_file_name}.{test_case_name}.{file_extension}"
    )
    assert (
        namer.get_received_filename() == "/my/source/directory/received/"
        "test_templated_namer.test_get_received_filename.txt"
    )


def test_approved_file_extension():
    namer = TemplatedCustomNamer(
        "{test_source_directory}/sub/{approved_or_received}/{test_file_name}.{test_case_name}.{file_extension}"
    )
    verify_as_json("This should be a .json file", options=Options().with_namer(namer))


def test_get_approved_filename():
    namer = TemplatedCustomNamer(
        "/my/source/directory/{approved_or_received}/{test_file_name}.{test_case_name}.{file_extension}"
    )
    assert (
        namer.get_approved_filename() == "/my/source/directory/approved/"
        "test_templated_namer.test_get_approved_filename.txt"
    )

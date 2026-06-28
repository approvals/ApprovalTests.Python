from approval_utilities.utilities.markdown_table import MarkdownTable
from approvaltests import Options, verify, verify_as_json
from approvaltests.namer.templated_custom_namer import (
    TemplatedCustomNamer,
    TemplateFields,
)


def test_template_fields() -> None:
    table = MarkdownTable().with_headers("template", "usage")
    for fields in dir(TemplateFields):
        if not fields.startswith("__"):
            table.add_rows(fields, f"{{{fields}}}")
    verify(table)


def test_get_received_filename() -> None:
    namer = TemplatedCustomNamer(
        "/my/source/directory/{approved_or_received}/{test_file_name}.{test_case_name}.{file_extension}"
    )
    assert (
        namer.get_received_filename() == "/my/source/directory/received/"
        "test_templated_namer.test_get_received_filename.txt"
    )


def test_approved_file_extension() -> None:
    namer = TemplatedCustomNamer(
        "{test_source_directory}/sub/{approved_or_received}/{test_file_name}.{test_case_name}.{file_extension}"
    )
    verify_as_json("This should be a .json file", options=Options().with_namer(namer))


def test_get_approved_filename() -> None:
    namer = TemplatedCustomNamer(
        "/my/source/directory/{approved_or_received}/{test_file_name}.{test_case_name}.{file_extension}"
    )
    assert (
        namer.get_approved_filename() == "/my/source/directory/approved/"
        "test_templated_namer.test_get_approved_filename.txt"
    )


def test_approvals_subdirectory_field() -> None:
    namer = TemplatedCustomNamer(
        "/root/{approvals_subdirectory}/{approved_or_received}/{test_file_name}.{test_case_name}.{file_extension}"
    )
    namer.namer_parts.config = {"subdirectory": "my_subdir"}
    namer.namer_parts.config_loaded = True
    assert (
        namer.get_approved_filename() == "/root/my_subdir/approved/"
        "test_templated_namer.test_approvals_subdirectory_field.txt"
    )

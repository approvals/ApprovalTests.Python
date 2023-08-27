from typing import Optional

from approvaltests import Namer, StackFrameNamer, verify_as_json, Options


# make the relative test work when running solo (not with all tests)
# extract duplication
# more test coverage
# support all 7 tags (4/7)
# renames

class TemplateFields:
    approved_or_received = "approved_or_received"
    test_file_name = "test_file_name"
    test_case_name = "test_case_name"
    file_extension = "file_extension"


class TemplatedCustomNamer(Namer):
    def __init__(self, template: str) -> None:
        self.template = template
        self.namer_parts = StackFrameNamer()

    def set_extension(self, extension_with_dot: str) -> None:
        self.namer_parts.set_extension(extension_with_dot)

    def get_received_filename(self, base: Optional[str] = None) -> str:
        return self.template.format_map(
            {TemplateFields.approved_or_received: self.RECEIVED_WITHOUT_DOT,
             TemplateFields.test_file_name: self.namer_parts.get_class_name(),
             TemplateFields.test_case_name: self.namer_parts.get_method_name(),
             TemplateFields.file_extension: self.namer_parts.get_extension_without_dot()})

    def get_approved_filename(self, base: Optional[str] = None) -> str:
        return self.template.format(
            approved_or_received=self.APPROVED_WITHOUT_DOT,
            test_file_name=self.namer_parts.get_class_name(),
            test_case_name=self.namer_parts.get_method_name(),
            file_extension=self.namer_parts.get_extension_without_dot())


def test_get_received_filename():
    namer = TemplatedCustomNamer(
        "/my/source/directory/{approved_or_received}/{test_file_name}.{test_case_name}.{file_extension}"
    )
    assert (namer.get_received_filename() == "/my/source/directory/received/"
                                             "test_templated_namer.test_get_received_filename.txt")


def test_approved_file_extension():
    namer = TemplatedCustomNamer(
        "sub/{approved_or_received}/{test_file_name}.{test_case_name}.{file_extension}"
    )
    # assert (namer.get_received_filename() == "/my/source/directory/received/"
    #                                         "test_templated_namer.test_get_received_filename.txt")
    verify_as_json("This should be a .json file", options=Options().with_namer(namer))


def test_get_approved_filename():
    namer = TemplatedCustomNamer(
        "/my/source/directory/{approved_or_received}/{test_file_name}.{test_case_name}.{file_extension}"
    )
    assert (namer.get_approved_filename() == "/my/source/directory/approved/"
                                             "test_templated_namer.test_get_approved_filename.txt")

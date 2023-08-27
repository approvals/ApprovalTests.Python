from typing import Optional

from approvaltests import Namer, StackFrameNamer, verify_as_json, Options

# make the relative test work when running solo (not with all tests)
# extract duplication
# more test coverage
# support all 7 tags (4/7)
# renames

class TemplatedCustomNamer(Namer):
    def __init__(self, template: str) -> None:
        self.template = template
        self.stacktracenamer = StackFrameNamer()


    def set_extension(self, extension_with_dot: str) -> None:
        self.stacktracenamer.set_extension(extension_with_dot)


    def get_received_filename(self, base: Optional[str] = None) -> str:
        return self.template.format(
            approved_or_received=self.RECEIVED_WITHOUT_DOT,
            test_file_name=self.stacktracenamer.get_class_name(),
            test_case_name=self.stacktracenamer.get_method_name(),
            file_extension=self.stacktracenamer.get_extension_without_dot())

    def get_approved_filename(self, base: Optional[str] = None) -> str:
        return self.template.format(
            approved_or_received=self.APPROVED_WITHOUT_DOT,
            test_file_name=self.stacktracenamer.get_class_name(),
            test_case_name=self.stacktracenamer.get_method_name(),
            file_extension=self.stacktracenamer.get_extension_without_dot())


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
    #assert (namer.get_received_filename() == "/my/source/directory/received/"
    #                                         "test_templated_namer.test_get_received_filename.txt")
    verify_as_json("This should be a .json file",options=Options().with_namer(namer))

def test_get_approved_filename():
    namer = TemplatedCustomNamer(
        "/my/source/directory/{approved_or_received}/{test_file_name}.{test_case_name}.{file_extension}"
    )
    assert (namer.get_approved_filename() == "/my/source/directory/approved/"
                                             "test_templated_namer.test_get_approved_filename.txt")


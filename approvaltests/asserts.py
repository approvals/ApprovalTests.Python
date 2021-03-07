from typing import Optional

from approvaltests import (
    get_default_namer,
    verify_with_namer,
    write_to_temporary_file,
    get_reporter,
    StackFrameNamer,
)
from approvaltests.reporters.testing_reporter import ReporterForTesting


class FilePathNamer(StackFrameNamer):
    def __init__(self, file_path: str, extension: None = None) -> None:
        StackFrameNamer.__init__(self, extension)
        self.file_path = file_path

    def get_approved_filename(self, basename: Optional[str] = None) -> str:
        return self.file_path


def assert_against_file(
    actual: str, file_path: str, reporter: Optional[ReporterForTesting] = None
) -> None:
    namer = FilePathNamer(file_path)
    verify_with_namer(actual, namer, reporter)


def assert_equal_with_reporter(expected, actual, reporter=None):
    if actual == expected:
        return

    name = get_default_namer().get_file_name()
    expected_file = write_to_temporary_file(expected, name + ".expected.")
    actual_file = write_to_temporary_file(actual, name + ".actual.")
    get_reporter(reporter).report(actual_file, expected_file)
    raise AssertionError(
        'expected != actual\n  actual: "{}"\nexpected: "{}"'.format(actual, expected)
    )

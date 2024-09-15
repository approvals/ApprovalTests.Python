import os
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

from approvaltests import get_default_namer, verify, Options, verify_file, approvals
from approvaltests.file_approver import FileApprover
from approvaltests.reporters.generic_diff_reporter_factory import (
    GenericDiffReporterFactory,
)
from approvaltests.reporters.testing_reporter import ReporterForTesting
from approvaltests.string_writer import StringWriter
from commandline_interface import list_approved_files_in_test_directory
from file_approver import APPROVED_FILE_LOG

# Future TODO: Push what we are working on to origin/main
# overall intention: prune abandoned approved files

# TODO:
# We broke things because we imported from build/lib. We need to write a test to check that we do not import from build/lib
# Started writing new test and adding English to tests/test_build.py

# TODO:
#  TO Learn: How the "build" directory is created, used, populated....
#  Confirm that we should be using `parse_arguments()` from `commandline_interface.py` in `build`

# TODO:  Say what we want to test.  Describe the test in English.  Create shared vision.  Then create the test.
# We "shold" not have to test the one that is in a library.  Assume that it works.
# We should test the one that we wrote, or how we are using it.


# TODO: Refactoring
# Jay's ideas: argument parser, simplification we could make
# given current design
#  you can write a test that overrides Sys ag v
#  or you can allow the parcer to ____
# Jay prefers to separate config from execution
#  and now the parse arg returns a TUPLE
# instead have parse arg return a data class
# the data clas could be:
# @dataclasses.dataclass(frozen=True)
# class userintent:
#      id:str
#      received:str

# TODO: list_approved_files_in_test_directory should have the following capabilities
#       - contain relative filepaths instead of just file names (that should handle dedup piece)
#       - think more about dedup piece
#       - handle multiple levels of directories (e.g. recurse the tree in the OS)

# TODO: communicate to user which approved files are stale
#       give the user option to delete stale files
#       example of stale file: FileApproverTests.test_dummy_test.approved.txt
# TODO: log file reveals bugs in os independent path handling
#       e.g. C:\Code\ApprovalTests.Python\tests\core/differenttest.approved.txt
# TODO: inline approvals show up as meaningless temp files in the log
#       e.g. C:\Users\IMAGEB~1\AppData\Local\Temp\2\tmppdnb2jxa.approved.txt
# TO Discuss: OS-independent, and project-relative paths (i.e. WinDOS C:\\\ or Unix  /.../...)

class FileApproverTests(unittest.TestCase):
    def test_list_approved_files_in_test_directory(self):
        # similar test to below but with two or three nested directories
        sandbox_folder = Path("sandbox")
        sandbox_folder.mkdir(exist_ok=True)

        approved_files = ["b.approved.txt", "a.approved.txt", "c.approved.txt"]
        for approved_file in approved_files:
            (sandbox_folder / approved_file).touch()

        approved_files_list = list_approved_files_in_test_directory(sandbox_folder)

        shutil.rmtree(sandbox_folder)

        verify(sorted(approved_files_list))

    def test_multiple_log_entries(self):
        approvals.settings().allow_multiple_verify_calls_for_this_method()

        # multiple verifies
        verify("verify something")
        verify("verify something")

        assert Path(APPROVED_FILE_LOG).exists()
        the_log_text = Path(APPROVED_FILE_LOG).read_text()
        approved_file_name = "FileApproverTests.test_multiple_log_entries.approved.txt"

        assert the_log_text.count(approved_file_name) == 2

    def test_inner_test(self):
        verify("this verify is for triggering the logging")

    def test_is_log_file_cleared(self):
        child_log = ".test_approved_file_log"
        Path(child_log).write_text("insert text to log")

        subprocess.run([sys.executable, "-m", "pytest", "-k", self.test_inner_test.__name__],
                       env={**os.environ, "APPROVED_FILE_LOG": child_log})

        child_log_text = Path(child_log).read_text()

        cleared = "insert text to log" not in child_log_text
        assert cleared
        assert self.test_inner_test.__name__ in child_log_text

        verify("outer test")

        approved_file_name = "FileApproverTests.test_is_log_file_cleared.approved.txt"
        assert approved_file_name in Path(APPROVED_FILE_LOG).read_text()

    def test_accessed_approved_files(self):
        log_text_before = Path(APPROVED_FILE_LOG).read_text()
        approved_file_name = "FileApproverTests.test_accessed_approved_files.approved.txt"

        assert approved_file_name not in log_text_before

        # ACT
        verify("this verify is for triggering the logging")

        # ASSERT
        assert Path(APPROVED_FILE_LOG).exists()
        the_log_text = Path(APPROVED_FILE_LOG).read_text()
        assert approved_file_name in the_log_text

    @staticmethod
    def test_compare_same_files():
        writer = StringWriter("a")
        writer.write_received_file("a.txt")
        shutil.copy("a.txt", "a_same.txt")
        FileApprover.verify_files("a.txt", "a_same.txt", None, Options().comparator)

    def test_compare_different_files(self):
        reporter = ReporterForTesting()
        FileApprover.verify_files("a.txt", "b.txt", reporter, Options().comparator)
        self.assertTrue(reporter.called)

    def test_scrubbed_files(self):
        verify_file("a.txt", options=Options().with_scrubber(lambda t: "<scrubbed>"))

    def test_full(self):
        namer = get_default_namer()
        writer = StringWriter("b")
        reporter = ReporterForTesting()
        FileApprover.verify(namer, writer, reporter, Options().comparator)
        self.assertTrue(reporter.called)

    def test_returns_error_when_files_are_different(self):
        approvals.settings().allow_multiple_verify_calls_for_this_method()
        namer = get_default_namer()
        writer = StringWriter("b")
        reporter = ReporterForTesting()
        error = FileApprover.verify(namer, writer, reporter, Options().comparator)
        import re

        replaced = re.sub("ved: .*approved_files.", "ved: <rootdir>/", error)

        verify(replaced)

    def test_returns_none_when_files_are_same_files(self):
        namer = get_default_namer()
        writer = StringWriter("b")
        reporter = GenericDiffReporterFactory().get_first_working()
        error = FileApprover.verify(namer, writer, reporter, Options().comparator)
        self.assertEqual(None, error)


if __name__ == "__main__":
    unittest.main()

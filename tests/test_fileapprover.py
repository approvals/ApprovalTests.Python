import shutil
import unittest

from approvaltests import get_default_namer, verify, Options, verify_file, approvals
from approvaltests.file_approver import FileApprover
from approvaltests.reporters.generic_diff_reporter_factory import (
    GenericDiffReporterFactory,
)
from approvaltests.reporters.testing_reporter import ReporterForTesting
from approvaltests.string_writer import StringWriter
from file_approver import get_approved_files_log


class FileApproverTests(unittest.TestCase):
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

    def test_approved_file_is_logged(self):
        # touch approved file
        verify("a", options=Options().for_file.with_extension(".txt1"))
        verify("a", options=Options().for_file.with_extension(".txt2"))
        # read the log
        log = get_approved_files_log()
        # assert that the approved file is logged
        name = approvals.get_default_namer().get_approved_filename()
        log_lines = log.read_text().split("\n")
        self.assertIn(name.replace(".txt", ".txt1"), log_lines)
        self.assertIn(name.replace(".txt", ".txt2"), log_lines)
        # verify there are no duplicates
        self.assertEqual(len(log_lines), len(set(log_lines)))




import shutil
import unittest

from approvaltests import get_default_namer, verify, Options, verify_file, approvals
from approvaltests.file_approver import FileApprover
from approvaltests.reporters.generic_diff_reporter_factory import (
    GenericDiffReporterFactory,
)
from approvaltests.reporters.testing_reporter import ReporterForTesting
from approvaltests.string_writer import StringWriter
from approvaltests.approved_file_log import ApprovedFilesLog


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
        name = approvals.get_default_namer().get_approved_filename()
        log = ApprovedFilesLog.get_approved_files_log()
        log_lines = log.read_text().split("\n")
        name1 = name.replace(".txt", ".txt1")
        name2 = name.replace(".txt", ".txt2")

        # check log is cleared
        self.assertNotIn(name1, log_lines)
        self.assertNotIn(name2, log_lines)

        # touch approved file
        verify("a", options=Options().for_file.with_extension(".txt1"))
        verify("a", options=Options().for_file.with_extension(".txt2"))

        # assert that the approved file is logged
        log_lines = log.read_text().split("\n")
        self.assertIn(name1, log_lines)
        self.assertIn(name2, log_lines)

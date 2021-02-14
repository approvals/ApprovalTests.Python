import shutil
import unittest

from approvaltests import get_default_namer
from approvaltests.core.namer import Namer
from approvaltests.file_approver import FileApprover
from approvaltests.reporters.generic_diff_reporter_factory import (
    GenericDiffReporterFactory,
)
from approvaltests.reporters.testing_reporter import ReporterForTesting
from approvaltests.string_writer import StringWriter


class FileApproverTests(unittest.TestCase):
    @staticmethod
    def test_compare_same_files():
        approver = FileApprover()
        writer = StringWriter("a")
        writer.write_received_file("a.txt")
        shutil.copy("a.txt", "a_same.txt")
        approver.verify_files("a.txt", "a_same.txt", None)

    def test_compare_different_files(self):
        approver = FileApprover()
        reporter = ReporterForTesting()
        approver.verify_files("a.txt", "b.txt", reporter)
        self.assertTrue(reporter.called)

    def test_full(self):
        namer = get_default_namer()
        writer = StringWriter("b")
        reporter = ReporterForTesting()
        approver = FileApprover()
        approver.verify(namer, writer, reporter)
        self.assertTrue(reporter.called)

    def test_returns_error_when_files_are_different(self):
        namer = get_default_namer()
        writer = StringWriter("b")
        reporter = ReporterForTesting()
        approver = FileApprover()
        error = approver.verify(namer, writer, reporter)
        self.assertEqual("Approval Mismatch", error)

    def test_returns_none_when_files_are_same_files(self):
        namer = get_default_namer()
        writer = StringWriter("b")
        reporter = GenericDiffReporterFactory().get_first_working()
        approver = FileApprover()
        error = approver.verify(namer, writer, reporter)
        self.assertEqual(None, error)


if __name__ == "__main__":
    unittest.main()

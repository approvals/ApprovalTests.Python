import shutil
import unittest

from approvaltests.FileApprover import FileApprover
from approvaltests.GenericDiffReporterFactory import GenericDiffReporterFactory
from approvaltests.Namer import Namer
from approvaltests.StringWriter import StringWriter
from approvaltests.TestingReporter import TestingReporter


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
        reporter = TestingReporter()
        approver.verify_files("a.txt", "b.txt", reporter)
        self.assertTrue(reporter.called)

    def test_full(self):
        namer = Namer()
        writer = StringWriter("b")
        reporter = TestingReporter()
        approver = FileApprover()
        approver.verify(namer, writer, reporter)
        self.assertTrue(reporter.called)

    def test_returns_error_when_files_are_different(self):
        namer = Namer()
        writer = StringWriter("b")
        reporter = TestingReporter()
        approver = FileApprover()
        error = approver.verify(namer, writer, reporter)
        self.assertEqual("Approval Mismatch", error)

    def test_returns_none_when_files_are_same_files(self):
        namer = Namer()
        writer = StringWriter("b")
        reporter = GenericDiffReporterFactory().get_first_working()
        approver = FileApprover()
        error = approver.verify(namer, writer, reporter)
        self.assertEqual(None, error)


if __name__ == '__main__':
    unittest.main()

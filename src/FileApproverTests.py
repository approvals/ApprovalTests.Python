import unittest
import shutil
from Namer import Namer
from StringWriter import StringWriter
from TestingReporter import TestingReporter
from FileApprover import FileApprover
from ReceivedFileLauncherReporter import ReceivedFileLauncherReporter


class FileApproverTests(unittest.TestCase):
    def test_compare_same_files(self):
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
        reporter = ReceivedFileLauncherReporter()
        approver = FileApprover()
        error = approver.verify(namer, writer, reporter)
        self.assertEqual(None, error)

if __name__ == '__main__':
    unittest.main()

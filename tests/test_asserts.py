import codecs
import unittest

from approvaltests.approval_exception import ApprovalException
from approvaltests import assert_against_file, assert_equal_with_reporter
from approvaltests.core import Reporter
from approvaltests.reporters.testing_reporter import ReporterForTesting
from approvaltests.utils import get_adjacent_file


class TestAssertEqualWithReporter(unittest.TestCase):
    def test_text_reporter_called_on_failure(self) -> None:
        class LocalReporter(Reporter):
            def __init__(self):
                self.received = None
                self.approved = None

            def report(self, received_path, approved_path):
                self.received = codecs.open(
                    received_path, "r", encoding="utf-8-sig"
                ).read()
                self.approved = codecs.open(
                    approved_path, "r", encoding="utf-8-sig"
                ).read()

        reporter = LocalReporter()
        try:
            assert_equal_with_reporter("expected", "actual", reporter)
        except AssertionError:
            pass
        self.assertEqual(reporter.received, "actual")
        self.assertEqual(reporter.approved, "expected")


class TestAsserts(unittest.TestCase):
    def test_assert_against_file_works(self) -> None:
        file_path = get_adjacent_file("manual_file.approved.txt")
        assert_against_file("This text is in a file", file_path)

    def test_assert_against_file_fails_with_reporter(self) -> None:
        reporter = ReporterForTesting()
        file_path = get_adjacent_file("manual_file.approved.txt")
        try:
            assert_against_file("This text is NOT in a file", file_path, reporter)
        except ApprovalException:
            pass
        self.assertTrue(reporter.called)

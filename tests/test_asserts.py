import unittest
from pathlib import Path

from approvaltests.approval_exception import ApprovalException
from approvaltests import assert_against_file, assert_equal_with_reporter, Options
from approvaltests.core import Reporter
from approvaltests.reporters.testing_reporter import ReporterForTesting
from approval_utilities.utils import get_adjacent_file
from approvaltests.scrubbers import scrub_all_guids


class TestAssertEqualWithReporter(unittest.TestCase):
    def test_assert_with_scrubbing_and_options(self):
        actuals = "2fd78d4a-ad49-447d-96a8-deda585a9aa5 and text"
        expected = "<guid_0> and text"
        assert_equal_with_reporter(
            expected,
            actuals,
            options=Options()
            .with_scrubber(scrub_all_guids)
            .for_file.with_extension(".md"),
        )

    def test_text_reporter_called_on_failure(self) -> None:
        class LocalReporter(Reporter):
            def __init__(self):
                self.received = None
                self.approved = None
                self.extention = None

            def report(self, received_path, approved_path):
                self.received = Path(received_path).read_text(encoding="utf-8-sig")
                self.approved = Path(approved_path).read_text(encoding="utf-8-sig")
                self.extention = Path(received_path).suffix

        reporter = LocalReporter()
        try:
            assert_equal_with_reporter(
                "expected",
                "actual",
                options=Options()
                .with_reporter(reporter)
                .for_file.with_extension(".md"),
            )
        except AssertionError:
            pass
        self.assertEqual(reporter.received, "actual")
        self.assertEqual(reporter.approved, "expected")
        self.assertEqual(reporter.extention, ".md")


class TestAsserts(unittest.TestCase):
    def test_assert_against_file_works(self) -> None:
        file_path = get_adjacent_file("manual_file.approved.txt")
        assert_against_file("This text is in a file\n", file_path)

    def test_assert_against_file_fails_with_reporter(self) -> None:
        reporter = ReporterForTesting()
        file_path = get_adjacent_file("manual_file.approved.txt")
        try:
            assert_against_file("This text is NOT in a file", file_path, reporter)
        except ApprovalException:
            pass
        self.assertTrue(reporter.called)

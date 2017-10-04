import codecs
import unittest

from approvaltests.approvals import assert_equal_with_reporter, assert_against_file
from approvaltests.core import Reporter
from approvaltests.utils import get_adjacent_file


class TestAssertEqualWithReporter(unittest.TestCase):
    def test_text_reporter_called_on_failure(self):
        class LocalReporter(Reporter):
            def __init__(self):
                self.received = None
                self.approved = None

            def report(self, received_path, approved_path):
                self.received = codecs.open(received_path, 'r', encoding='utf-8-sig').read()
                self.approved = codecs.open(approved_path, 'r', encoding='utf-8-sig').read()

        reporter = LocalReporter()
        try:
            assert_equal_with_reporter('expected', 'actual', reporter)
        except AssertionError:
            pass
        self.assertEqual(reporter.received, 'actual')
        self.assertEqual(reporter.approved, 'expected')


class TestAsserts(unittest.TestCase):
    def test_assert_against_file_works(self):
        file_path = get_adjacent_file("manual_file.approved.txt")
        assert_against_file("This text is in a file", file_path)

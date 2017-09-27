import codecs
import unittest

from approvaltests.approvals import assert_equal_with_reporter
from approvaltests.core import Reporter


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


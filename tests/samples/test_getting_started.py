import unittest

from approvaltests import verify
from approvaltests.reporters import GenericDiffReporterFactory
from approvaltests.reporters.report_with_beyond_compare import ReportWithBeyondCompare

# begin-snippet: select_reporter_from_factory
class TestSelectReporter(unittest.TestCase):
    def setUp(self):
        self.factory = GenericDiffReporterFactory()

    def test_simple(self):
        verify('Hello', self.factory.get('BeyondCompare4'))
# end-snippet

# begin-snippet: select_reporter_from_class
class TestSelectReporterFromClass(unittest.TestCase):
     def test_simple(self):
        verify('Hello', reporter=ReportWithBeyondCompare())
# end-snippet
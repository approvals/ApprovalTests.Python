import unittest

from approvaltests import verify
from approvaltests.reporters import GenericDiffReporterFactory

# begin-snippet: select_reporter_from_factory
class TestSelectReporter(unittest.TestCase):
    def setUp(self):
        self.factory = GenericDiffReporterFactory()

    def test_simple(self):
        verify('Hello', self.factory.get('BeyondCompare4'))
# end-snippet

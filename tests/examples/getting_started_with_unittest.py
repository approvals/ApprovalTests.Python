# begin-snippet: getting_started_with_unittest
import unittest

from approvaltests.approvals import verify
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory


class GettingStartedTest(unittest.TestCase):
    def setUp(self):
        self.reporter = GenericDiffReporterFactory().get_first_working()

    def test_simple(self):
        verify('Hello ApprovalTests', self.reporter)


if __name__ == "__main__":
    unittest.main()
# end-snippet
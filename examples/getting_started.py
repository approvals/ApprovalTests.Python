import unittest

from approvaltests.Approvals import verify
from approvaltests.GenericDiffReporterFactory import GenericDiffReporterFactory


class GettingStartedTest(unittest.TestCase):
    def setUp(self):
        self.reporter = GenericDiffReporterFactory().get_first_working()

    def test_simple(self):
        verify('Hello', self.reporter)

if __name__ == "__main__":
    unittest.main()

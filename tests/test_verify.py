import unittest

from approvaltests.ApprovalException import ApprovalException
from approvaltests.Approvals import verify
from approvaltests.GenericDiffReporterFactory import GenericDiffReporterFactory
from approvaltests.TestingReporter import TestingReporter


class VerifyTests(unittest.TestCase):
    def setUp(self):
        self.reporter = GenericDiffReporterFactory().get('BeyondCompare4')

    def test_verify(self):
        verify("Hello World.", self.reporter)

    def test_verify_fail(self):
        reporter = TestingReporter()
        try:
            verify("Hello World.", reporter)
            self.assertFalse(True, "expected exception")
        except ApprovalException as e:
            self.assertTrue("Approval Mismatch", e.value)

import unittest
from ApprovalException import ApprovalException
from TestingReporter import TestingReporter
from Approvals import verify


class VerifyTests(unittest.TestCase):
    def test_verify(self):
        verify("Hello World.")

    def test_verify_fail(self):
        reporter = TestingReporter()
        try:
            verify("Hello World.", reporter)
            self.assertFalse(True, "expected exception")
        except ApprovalException as e:
            self.assertTrue("Approval Mismatch", e.value)

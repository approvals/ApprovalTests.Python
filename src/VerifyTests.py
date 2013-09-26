import unittest
from approvaltests.ApprovalException import ApprovalException
from approvaltests.Approvals import verify
from approvaltests.TestingReporter import TestingReporter


class VerifyTests(unittest.TestCase):
    @staticmethod
    def test_verify():
        verify("Hello World.")

    def test_verify_fail(self):
        reporter = TestingReporter()
        try:
            verify("Hello World.", reporter)
            self.assertFalse(True, "expected exception")
        except ApprovalException as e:
            self.assertTrue("Approval Mismatch", e.value)

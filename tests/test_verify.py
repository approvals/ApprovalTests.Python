import unittest

from approvaltests.ApprovalException import ApprovalException
from approvaltests.Approvals import verify, verify_as_json
from approvaltests.GenericDiffReporterFactory import GenericDiffReporterFactory
from approvaltests.TestingReporter import TestingReporter


class VerifyTests(unittest.TestCase):
    def setUp(self):
        self.reporter = GenericDiffReporterFactory().get('BeyondCompare4Mac')

    def test_verify(self):
        verify("Hello World.", self.reporter)

    def test_verify_fail(self):
        reporter = TestingReporter()
        try:
            verify("Hello World.", reporter)
            self.assertFalse(True, "expected exception")
        except ApprovalException as e:
            self.assertTrue("Approval Mismatch", e.value)

    def test_verify_as_json(self):
        class Bag(object):
            def __init__(self):
                self.stuff = 1
                self.json = None

        o = Bag()
        o.json = {
            "a": 0,
            "z": 26
        }
        verify_as_json(o, self.reporter)

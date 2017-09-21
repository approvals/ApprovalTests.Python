import unittest

from approvaltests.approval_exception import ApprovalException
from approvaltests.approvals import verify, verify_as_json, verify_file
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
from approvaltests.reporters.testing_reporter import TestingReporter
from approvaltests.utils import get_adjacent_file


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

    def test_verify_file(self):
        name = "testFile.txt"
        filename = get_adjacent_file(name)
        verify_file(filename, self.reporter)

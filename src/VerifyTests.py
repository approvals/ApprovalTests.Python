import unittest
from FileApprover import FileApprover
from Namer import Namer
from StringWriter import StringWriter
from ReceivedFileLauncherReporter import ReceivedFileLauncherReporter
from TestingReporter import TestingReporter


class ApprovalException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def verify(data, reporter=ReceivedFileLauncherReporter()):
    approver = FileApprover()
    namer = Namer(2)
    writer = StringWriter(data)

    error = approver.verify(namer, writer, reporter)
    if(error is not None):
        raise ApprovalException(error)


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

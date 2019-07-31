import unittest

from approvaltests.core.reporter import Reporter
from approvaltests.reporters.first_working_reporter import FirstWorkingReporter


class ReporterForTesting(Reporter):
    def __init__(self, success, additional=None):
        if additional is None:
            additional = lambda : None
        self.additional = additional
        self.called = False
        self.success = success

    def report(self, received_path, approved_path):
        self.called = True
        self.additional()
        return self.success


class TestFirstWorkingReporter(unittest.TestCase):
    def test_first_one(self):
        r1 = ReporterForTesting(True)
        r2 = ReporterForTesting(False)
        first = FirstWorkingReporter(r1, r2)
        success = first.report('a.txt', 'b.txt')
        self.assertTrue(r1.called)
        self.assertTrue(success)
        self.assertFalse(r2.called)

    def test_second_one(self):
        r1 = ReporterForTesting(False)
        r2 = ReporterForTesting(False)
        first = FirstWorkingReporter(r1, r2)
        success = first.report('a.txt', 'b.txt')
        self.assertTrue(r1.called)
        self.assertTrue(r2.called)
        self.assertFalse(success)

    def test_exception(self):
        def exception():
            raise Exception()
        r1 = ReporterForTesting(False, exception)
        r2 = ReporterForTesting(False)
        first = FirstWorkingReporter(r1, r2)
        success = first.report('a.txt', 'b.txt')
        self.assertTrue(r1.called)
        self.assertTrue(r2.called)
        self.assertFalse(success)

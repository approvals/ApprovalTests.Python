import unittest

from approvaltests.core.reporter import Reporter
from approvaltests.reporters.first_working_reporter import FirstWorkingReporter
from typing import Callable, Optional


class ReporterForTesting(Reporter):
    def __init__(self, success: bool, additional: Optional[Callable] = None) -> None:
        if additional is None:
            additional = lambda: None
        self.additional = additional
        self.called = False
        self.success = success

    def __str__(self):
        return f"{self.__class__.__name__}({self.success})"

    __repr__ = __str__

    def report(self, received_path: str, approved_path: str) -> bool:
        self.called = True
        self.additional()
        return self.success


class TestFirstWorkingReporter(unittest.TestCase):
    def test_first_one(self) -> None:
        r1 = ReporterForTesting(True)
        r2 = ReporterForTesting(False)
        first = FirstWorkingReporter(r1, r2)
        success = first.report("a.txt", "b.txt")
        self.assertTrue(r1.called)
        self.assertTrue(success)
        self.assertFalse(r2.called)

    def test_string_representation(self) -> None:
        r1 = ReporterForTesting(True)
        r2 = ReporterForTesting(False)
        first = FirstWorkingReporter(r1, r2)
        expected = (
            "FirstWorkingReporter(ReporterForTesting(True), ReporterForTesting(False))"
        )
        self.assertEqual(expected, str(first))

    def test_second_one(self) -> None:
        r1 = ReporterForTesting(False)
        r2 = ReporterForTesting(False)
        first = FirstWorkingReporter(r1, r2)
        success = first.report("a.txt", "b.txt")
        self.assertTrue(r1.called)
        self.assertTrue(r2.called)
        self.assertFalse(success)

    def test_exception(self) -> None:
        def exception():
            raise Exception()

        r1 = ReporterForTesting(False, exception)
        r2 = ReporterForTesting(False)
        first = FirstWorkingReporter(r1, r2)
        success = first.report("a.txt", "b.txt")
        self.assertTrue(r1.called)
        self.assertTrue(r2.called)
        self.assertFalse(success)

import unittest

from approvaltests import Options, verify
from approvaltests.reporters.diff_tools import ReportWithBeyondCompare
from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter


# begin-snippet: select_reporter_from_class
class TestSelectReporterFromClass(unittest.TestCase):
    def test_simple(self):
        verify("Hello", options=Options().with_reporter(ReportWithBeyondCompare()))


# end-snippet


# begin-snippet: custom_generic_diff_reporter
class GettingStartedTest(unittest.TestCase):
    def test_simple(self):
        verify(
            "Hello",
            options=Options().with_reporter(
                GenericDiffReporter.create(r"C:\my\favorite\diff\utility.exe")
            ),
        )


# end-snippet

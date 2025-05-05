from typing_extensions import override
import unittest

from approvaltests import verify, Options
from approvaltests.reporters import GenericDiffReporterFactory
from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter
from approvaltests.reporters.report_with_beyond_compare import (
    report_with_beyond_compare,
)


# begin-snippet: select_reporter_from_factory
class TestSelectReporter(unittest.TestCase):
    @override
    def setUp(self):
        self.factory = GenericDiffReporterFactory()

    def test_simple(self):
        verify(
            "Hello", options=Options().with_reporter(self.factory.get("BeyondCompare"))
        )


# end-snippet


# begin-snippet: select_reporter_from_class
class TestSelectReporterFromClass(unittest.TestCase):
    def test_simple(self):
        verify("Hello", options=Options().with_reporter(report_with_beyond_compare()))


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

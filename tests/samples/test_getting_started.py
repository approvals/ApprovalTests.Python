import unittest

from typing_extensions import override

from approvaltests import Options, verify
from approvaltests.reporters import GenericDiffReporterFactory
from approvaltests.reporters.generated_diff_reporters import ReportWithBeyondCompare
from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter


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

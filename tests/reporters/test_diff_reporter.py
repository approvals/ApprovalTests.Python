from typing import List

from approvaltests.reporters import (
    DiffReporter,
    PythonNativeReporter,
    Reporter,
)
from approvaltests.reporters.report_by_creating_diff_file import ReportByCreatingDiffFile


class FakeFactory:
    def get_all_reporters(self) -> List[Reporter]:
        return []


def test_fallback_reporter() -> None:
    empty_reporter_factory = FakeFactory()
    reporter = DiffReporter(empty_reporter_factory)
    # Testing implementation detail, not great but good enough for now
    assert isinstance(reporter.reporters[-1], PythonNativeReporter)


def test_get_diff_file_name() -> None:
    diff_file = ReportByCreatingDiffFile.get_diff_file_name("VerifyTests.test_verify_html.received.html")
    assert diff_file == "VerifyTests.test_verify_html.diff"
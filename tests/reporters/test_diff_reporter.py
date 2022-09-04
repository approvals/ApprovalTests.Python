from typing import List

from approvaltests import verify
from approvaltests.core.reporter import Reporter
from approvaltests.reporters.diff_reporter import DiffReporter
from approvaltests.reporters.introduction_reporter import IntroductionReporter

from approvaltests.reporters.report_by_creating_diff_file import (
    ReportByCreatingDiffFile,
)
from approvaltests.core import Options


class FakeFactory:
    def get_all_reporters(self) -> List[Reporter]:
        return []


def test_fallback_reporter() -> None:
    empty_reporter_factory = FakeFactory()
    reporter = DiffReporter(empty_reporter_factory)
    # Testing implementation detail, not great but good enough for now
    assert isinstance(reporter.reporters[-1], IntroductionReporter)


def test_get_diff_file_name() -> None:
    diff_file = ReportByCreatingDiffFile.get_diff_file_name(
        "VerifyTests.test_verify_html.received.html"
    )
    assert diff_file == "VerifyTests.test_verify_html.diff"


def test_default_reporter_chain() -> None:
    # get default reporter
    reporter = Options().reporter
    printed_reporter = str(reporter)
    verify(printed_reporter)


# print the chain
# verify the chain

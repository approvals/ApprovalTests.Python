import os

from typing_extensions import override

from approvaltests.core.reporter import Reporter
from approvaltests.reporters.clipboard_reporter import (
    ClipboardReporter,
    CommandLineReporter,
)
from approvaltests.reporters.diff_reporter import DiffReporter
from approvaltests.reporters.diff_tools import (
    ReportWithAraxisMerge,
    ReportWithBeyondCompare,
    ReportWithCodeCompareWindows,
    ReportWithDiffMerge,
    ReportWithKaleidoscope,
    ReportWithKdiff3,
    ReportWithMeldMergeLinux,
    ReportWithP4mergeMac,
    ReportWithSublimeMerge,
    ReportWithTortoise,
    ReportWithVisualStudioCode,
    ReportWithWinMergeReporterWindows,
)
from approvaltests.reporters.file_capture_reporter import FileCaptureReporter
from approvaltests.reporters.multi_reporter import MultiReporter
from approvaltests.reporters.python_native_reporter import PythonNativeReporter
from approvaltests.reporters.report_quietly import ReportQuietly
from approvaltests.reporters.reporter_that_automatically_approves import (
    ReporterThatAutomaticallyApproves,
)

REPORTER_MAP: dict[str, type[Reporter]] = {
    "AraxisMergeReporter": ReportWithAraxisMerge,
    "AutoApproveReporter": ReporterThatAutomaticallyApproves,
    "BeyondCompareReporter": ReportWithBeyondCompare,
    "ClipboardReporter": ClipboardReporter,
    "CodeCompareReporter": ReportWithCodeCompareWindows,
    "CommandLineReporter": CommandLineReporter,
    "DiffMergeReporter": ReportWithDiffMerge,
    "DiffReporter": DiffReporter,
    "FileCaptureReporter": FileCaptureReporter,
    "KaleidoscopeDiffReporter": ReportWithKaleidoscope,
    "KDiff3Reporter": ReportWithKdiff3,
    "MeldMergeReporter": ReportWithMeldMergeLinux,
    "P4MergeReporter": ReportWithP4mergeMac,
    "PythonNativeReporter": PythonNativeReporter,
    "QuietReporter": ReportQuietly,
    "SublimeMergeReporter": ReportWithSublimeMerge,
    "TortoiseDiffReporter": ReportWithTortoise,
    "VisualStudioCodeReporter": ReportWithVisualStudioCode,
    "WinMergeReporter": ReportWithWinMergeReporterWindows,
}


class EnvironmentVariableReporter(Reporter):
    ENVIRONMENT_VARIABLE_NAME = "APPROVAL_TESTS_USE_REPORTER"

    def __init__(self) -> None:
        self._reporter: Reporter | None = None
        environment_value = os.environ.get(self.ENVIRONMENT_VARIABLE_NAME)
        if environment_value is None:
            return
        names = environment_value.split(",")
        reporters = [REPORTER_MAP[n]() for n in names if n in REPORTER_MAP]
        if len(reporters) == 1:
            self._reporter = reporters[0]
        elif len(reporters) > 1:
            self._reporter = MultiReporter(*reporters)

    @override
    def report(self, received_path: str, approved_path: str) -> bool:
        if self._reporter is None:
            return False
        return self._reporter.report(received_path, approved_path)

    def get_reporter(self) -> Reporter | None:
        return self._reporter

    def get_reporter_mapping(self) -> dict[str, type[Reporter]]:
        return dict(REPORTER_MAP)

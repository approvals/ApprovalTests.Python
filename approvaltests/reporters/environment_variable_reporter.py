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

class EnvironmentVariableReporter(Reporter):
    ENVIRONMENT_VARIABLE_NAME = "APPROVAL_TESTS_USE_REPORTER"

    @override
    def report(self, received_path: str, approved_path: str) -> bool:
        class_name = os.environ.get(self.ENVIRONMENT_VARIABLE_NAME)
        return _report_with(class_name, received_path, approved_path)
        
        
    @staticmethod
    def _report_with(class_name: str, received_path: str, approved_path: str) -> bool:
        if not class_name:
            return False
        reporter = EnvironmentVariableReporter._load_reporter(class_name)
        return reporter.report(received_path, approved_path)

    @staticmethod
    def _load_reporter(class_name: str) -> Reporter:
        module_name, _, attr = class_name.rpartition(".")
        import importlib
        module = importlib.import_module(module_name)
        cls = getattr(module, attr)
        return cls()


from approvaltests.reporters import MultiReporter, PythonNativeReporter
from approvaltests.reporters.report_by_creating_diff_file import ReportByCreatingDiffFile


class ReportOnCyberDojo(MultiReporter):
    def __init__(self) -> None:
        super().__init__(ReportByCreatingDiffFile(), PythonNativeReporter())
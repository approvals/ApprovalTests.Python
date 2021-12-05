import os
from difflib import unified_diff
from pathlib import Path

from approvaltests import ensure_file_exists
from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter, GenericDiffReporterConfig


class ReportByCreatingDiffFile(GenericDiffReporter):
    def __init__(self):
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__, path=r"C:\Windows\System32\fc.exe"
            )
        )

    def report(self, received_path: str, approved_path: str) -> bool:
        diff = self.calculate_diff(received_path,approved_path)
        suffix = Path(received_path).suffix
        diff_file_path = received_path.replace(f".received{suffix}", ".diff")
        print("diff file path text is ", diff_file_path)
        with open(diff_file_path, mode="w") as f1 :
            f1.write(diff)
        return True

    @staticmethod
    def calculate_diff(file1: str, file2: str):
        with open(file1) as f1:
            with open(file2) as f2:
                diff = unified_diff(
                    f2.readlines(),
                    f1.readlines(),
                    os.path.basename(file2),
                    os.path.basename(file1),
                )
                diff_string = "".join(diff)
                return diff_string


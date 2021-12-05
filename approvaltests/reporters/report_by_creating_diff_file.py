from pathlib import Path

from approvaltests import Reporter
from approvaltests.reporters.python_native_reporter import calculate_diff


class ReportByCreatingDiffFile(Reporter):

    def report(self, received_path: str, approved_path: str) -> bool:
        diff = calculate_diff(received_path, approved_path)
        suffix = Path(received_path).suffix
        diff_file_path = received_path.replace(f".received{suffix}", ".diff")
        print("diff file path text is ", diff_file_path)
        with open(diff_file_path, mode="w") as f1:
            f1.write(diff)
        return True

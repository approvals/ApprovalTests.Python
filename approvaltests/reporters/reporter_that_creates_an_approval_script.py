from pathlib import Path

from approvaltests import Reporter
from approved_file_log import APPROVAL_TESTS_TEMP_DIRECTORY
from reporters import get_command_text
from utils import append_to_file


class ReporterThatCreatesAnApprovalScript (Reporter):
    file = None
    def create_approval_script(self, script:str):
        if ReporterThatCreatesAnApprovalScript.file is None:
            dir = Path(APPROVAL_TESTS_TEMP_DIRECTORY)
            dir.mkdir(parents=True, exist_ok=True)
            ReporterThatCreatesAnApprovalScript.file =dir / "approval_script.bat"
            ReporterThatCreatesAnApprovalScript.file.write_text("")
        append_to_file(ReporterThatCreatesAnApprovalScript.file, f"{script}\n")
    def report(self, received_path: str, approved_path: str) -> bool:
        self.create_approval_script( get_command_text(received_path, approved_path))
        return True

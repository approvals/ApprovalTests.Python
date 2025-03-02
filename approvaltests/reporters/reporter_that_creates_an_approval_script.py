from pathlib import Path

from approval_utilities.utils import is_windows_os, append_to_file
from approvaltests import Reporter

from approvaltests.internals.logs.log_commons import APPROVAL_TESTS_TEMP_DIRECTORY
from approvaltests.reporters import get_command_text


class ReporterThatCreatesAnApprovalScript(Reporter):
    file = None

    def create_approval_script(self, script: str):
        if ReporterThatCreatesAnApprovalScript.file is None:
            if is_windows_os():
                self.create_script_windows()
            else:
                self.create_script_unix()
        append_to_file(ReporterThatCreatesAnApprovalScript.file, f"{script}\n")

    def create_script_unix(self):
        APPROVAL_TESTS_TEMP_DIRECTORY.mkdir(parents=True, exist_ok=True)
        ReporterThatCreatesAnApprovalScript.file = (
            APPROVAL_TESTS_TEMP_DIRECTORY / "approval_script.sh"
        )
        ReporterThatCreatesAnApprovalScript.file.write_text("#!/bin/bash\n")
        # make executable
        ReporterThatCreatesAnApprovalScript.file.chmod(0o755)

    def create_script_windows(self):
        APPROVAL_TESTS_TEMP_DIRECTORY.mkdir(parents=True, exist_ok=True)
        ReporterThatCreatesAnApprovalScript.file = (
            APPROVAL_TESTS_TEMP_DIRECTORY / "approval_script.bat"
        )
        ReporterThatCreatesAnApprovalScript.file.write_text("")

    def report(self, received_path: str, approved_path: str) -> bool:
        self.create_approval_script(get_command_text(received_path, approved_path))
        return True

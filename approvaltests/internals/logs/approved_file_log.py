from pathlib import Path

import requests

from approval_utilities.utils import is_windows_os

APPROVAL_TESTS_TEMP_DIRECTORY: str = ".approval_tests_temp"


class ApprovedFilesLog:
    @staticmethod
    def clear_log_file() -> None:
        ApprovedFilesLog.get_approved_files_log().write_text("")
        ApprovedFilesLog.download_script_if_needed("detect_and_remove_abandoned")


    @staticmethod
    def get_approved_files_log() -> Path:
        path = Path(APPROVAL_TESTS_TEMP_DIRECTORY) / ".approved_files.log"
        path.parent.mkdir(parents=True, exist_ok=True)

        return path

    @staticmethod
    def log(approved_file: str) -> None:
        with ApprovedFilesLog.get_approved_files_log().open(mode="a") as file:
            file.write(f"{approved_file}\n")

    @staticmethod
    def download_script_if_needed(script_basename: str) -> None:
        suffix = ".bat" if is_windows_os() else ".sh"
        script_name_with_suffix = f"{script_basename}{suffix}"
        script_path = Path(APPROVAL_TESTS_TEMP_DIRECTORY) / script_name_with_suffix
        if script_path.exists():
            return

        response = requests.get(f"https://raw.githubusercontent.com/approvals/ApprovalTests.Java/refs/heads/master/resources/{script_name_with_suffix}")
        if response.ok:
            script_path.write_text(response.text)



ApprovedFilesLog.clear_log_file()

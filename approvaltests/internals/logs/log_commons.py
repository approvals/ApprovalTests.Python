from pathlib import Path

import requests

from approval_utilities.utils import is_windows_os

APPROVAL_TESTS_TEMP_DIRECTORY: str = ".approval_tests_temp"
class LogCommons:
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


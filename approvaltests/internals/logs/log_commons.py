import os
from pathlib import Path

import requests

APPROVAL_TESTS_TEMP_DIRECTORY = Path(".approval_tests_temp")


class LogCommons:
    @staticmethod
    def download_script_from_common_repo_if_needed(
        script_name_with_suffix: str,
    ) -> bool:
        if os.getenv("APPROVALTESTS_DISABLE_SCRIPT_DOWNLOADS") == "1":
            return False

        try:
            script_path = APPROVAL_TESTS_TEMP_DIRECTORY / script_name_with_suffix
            if script_path.exists():
                return False

            response = requests.get(
                f"https://raw.githubusercontent.com/approvals/ApprovalTests.CommonScripts/refs/heads/main/{script_name_with_suffix}"
            )
            if response.ok:
                script_path.write_text(response.text)

                make_executable = 0o755
                script_path.chmod(make_executable)
                return True
        except:
            pass
        return False

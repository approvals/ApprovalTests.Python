from pathlib import Path

from approvaltests.internals.logs.approved_file_log import (
    APPROVAL_TESTS_TEMP_DIRECTORY,
    ApprovedFilesLog,
)
from approvaltests.internals.logs.log_commons import LogCommons


class FailedComparisonLog:
    @staticmethod
    def clear_log_file() -> None:
        FailedComparisonLog.get_failed_comparison_log().write_text("")
        LogCommons.download_script_if_needed("approve_all")

    @staticmethod
    def get_failed_comparison_log() -> Path:
        return ApprovedFilesLog.get_temp_directory() / ".failed_comparison.log"

    @staticmethod
    def log(received_file, approved_file):
        with FailedComparisonLog.get_failed_comparison_log().open(mode="a") as file:
            file.write(f"{received_file} -> {approved_file}\n")


FailedComparisonLog.clear_log_file()

from pathlib import Path

from approvaltests.internals.logs.log_commons import (
    LogCommons,
    APPROVAL_TESTS_TEMP_DIRECTORY,
)


class ApprovedFilesLog:
    @staticmethod
    def clear_log_file() -> None:
        ApprovedFilesLog.get_approved_files_log().write_text("")
        LogCommons.download_script_if_needed("detect_and_remove_abandoned")

    @staticmethod
    def get_approved_files_log() -> Path:
        path = Path(APPROVAL_TESTS_TEMP_DIRECTORY) / ".approved_files.log"
        path.parent.mkdir(parents=True, exist_ok=True)

        return path

    @staticmethod
    def log(approved_file: str) -> None:
        with ApprovedFilesLog.get_approved_files_log().open(mode="a") as file:
            file.write(f"{approved_file}\n")


ApprovedFilesLog.clear_log_file()

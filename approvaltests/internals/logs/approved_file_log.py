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
        path = APPROVAL_TESTS_TEMP_DIRECTORY / ".approved_files.log"
        ApprovedFilesLog.make_directory_with_gitignore_with_text()

        return path

    @staticmethod
    def make_directory_with_gitignore_with_text():
        APPROVAL_TESTS_TEMP_DIRECTORY.mkdir(parents=True, exist_ok=True)
        APPROVAL_TESTS_TEMP_DIRECTORY.joinpath(".gitignore").write_text("*")

    @staticmethod
    def log(approved_file: str) -> None:
        with ApprovedFilesLog.get_approved_files_log().open(mode="a") as file:
            file.write(f"{approved_file}\n")


ApprovedFilesLog.clear_log_file()

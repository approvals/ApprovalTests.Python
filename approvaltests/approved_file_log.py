from pathlib import Path

APPROVAL_TESTS_TEMP_DIRECTORY: str = ".approval_tests_temp"


class ApprovedFilesLog:
    @staticmethod
    def clear_log_file() -> None:
        ApprovedFilesLog.get_approved_files_log().write_text("")

    @staticmethod
    def get_approved_files_log() -> Path:
        path = Path("%s/.approved_files.log" % APPROVAL_TESTS_TEMP_DIRECTORY)
        path.parent.mkdir(parents=True, exist_ok=True)

        return path

    @staticmethod
    def log(approved_file):
        with ApprovedFilesLog.get_approved_files_log().open(mode="a") as file:
            file.write(f"{approved_file}\n")


ApprovedFilesLog.clear_log_file()

from pathlib import Path


class ApprovedFilesLog:
    @staticmethod
    def clear_log_file() -> None:
        ApprovedFilesLog.get_approved_files_log().unlink(missing_ok=True)

    @staticmethod
    def get_approved_files_log() -> Path:
        return Path(".approved_files.log")

    @staticmethod
    def log(approved_file):
        with ApprovedFilesLog.get_approved_files_log().open(mode="a") as file:
            file.write(f"{approved_file}\n")

ApprovedFilesLog.clear_log_file()

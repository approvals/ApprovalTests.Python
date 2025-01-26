from pathlib import Path

from approvaltests.approved_file_log import APPROVAL_TESTS_TEMP_DIRECTORY


class FailedComparisonLog:
    @staticmethod
    def clear_log_file() -> None:
        FailedComparisonLog.get_failed_comparison_log().write_text("")

    @staticmethod
    def get_failed_comparison_log() -> Path:
        path = Path("%s/.failed_comparison.log" % APPROVAL_TESTS_TEMP_DIRECTORY)
        path.parent.mkdir(parents=True, exist_ok=True)

        return path

    @staticmethod
    def log(received_file, approved_file):
        with FailedComparisonLog.get_failed_comparison_log().open(mode="a") as file:
            file.write(f"{received_file} -> {approved_file}\n")


FailedComparisonLog.clear_log_file()

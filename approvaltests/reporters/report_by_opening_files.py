import platform
import subprocess
from pathlib import Path
from typing import List

from typing_extensions import override

from approval_utilities.utilities.logger.simple_logger import SimpleLogger
from approvaltests.core.reporter import Reporter


class ReportByOpeningFiles(Reporter):
    @staticmethod
    def display_file(file_path: str) -> None:
        call = ReportByOpeningFiles.get_opening_command(file_path, platform.system())
        subprocess.call(call, shell=True)

    @staticmethod
    def get_opening_command(file_path: str, os: str) -> List[str]:
        command = {
            "Windows": "start",
            "Darwin": "open",
            "Linux": "xdg-open",
        }[os]
        call = [command, file_path]
        return call

    @staticmethod
    def is_non_empty_file(file_path: str) -> bool:
        path = Path(file_path)
        return path.is_file() and path.stat().st_size > 0

    @override
    def report(self, received_path: str, approved_path: str) -> bool:
        try:
            if self.is_non_empty_file(approved_path):
                self.display_file(approved_path)

            self.display_file(received_path)

            return True
        except Exception as e:
            SimpleLogger.warning("Failed to open files", exception=e)
            return False

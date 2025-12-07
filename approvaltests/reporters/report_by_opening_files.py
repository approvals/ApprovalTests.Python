import os
import platform
import subprocess
from pathlib import Path
from typing import List

from typing_extensions import override

from approvaltests.core.reporter import Reporter
from approval_utilities.utilities.logger.simple_logger import SimpleLogger


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
        """
        Check if a file exists and has content.

        Args:
            file_path: The path to check

        Returns:
            True if the file exists and has size > 0, False otherwise
        """
        path = Path(file_path)
        return path.is_file() and path.stat().st_size > 0

    @override
    def report(self, received_path: str, approved_path: str) -> bool:
        """
        Opens the received file and optionally the approved file.

        The approved file is only opened if it exists and is non-empty.
        Catches and logs any exceptions during the process.

        Args:
            received_path: The path to the received file
            approved_path: The path to the approved file

        Returns:
            True if the operation completes without exception, False otherwise
        """
        try:
            # Open approved file if it exists and is non-empty
            if self.is_non_empty_file(approved_path):
                self.display_file(approved_path)

            # Always open the received file
            self.display_file(received_path)

            return True
        except Exception as e:
            SimpleLogger.warning("Failed to open files", exception=e)
            return False

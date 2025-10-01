import platform
from subprocess import call
from typing import List

from typing_extensions import override

from approvaltests.core.reporter import Reporter


class ReportWithOpeningFile(Reporter):
    """
    A reporter that opens the received file using the
    system default file viewer.

    Uses platform-specific commands:
    - macOS: open
    - Windows: start
    - Linux/Unix: xdg-open

    Depending on the file viewer being launched,
    the test suite execution may halt until the
    user has closed the new process.
    """

    @staticmethod
    def get_command(received_path: str) -> List[str]:
        system = platform.system()
        if system == "Darwin":
            return ["open", received_path]
        if system == "Windows":
            return ["start", received_path]
        return ["xdg-open", received_path]

    @override
    def report(self, received_path: str, approved_path: str) -> bool:
        command_array = self.get_command(received_path)
        call(command_array)
        return True

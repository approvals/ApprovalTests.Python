import subprocess
from typing import List

from approvaltests.utils import ensure_file_exists
from approvaltests.command import Command
from approvaltests.core.reporter import Reporter
from approvaltests.reporters.generic_diff_reporter_config import (
    GenericDiffReporterConfig,
    create_config,
)
from approvaltests.utils import to_json

PROGRAM_FILES = "{ProgramFiles}"


class GenericDiffReporter(Reporter):
    """
    A reporter that launches
    an external diff tool given by config.
    """

    @staticmethod
    def create(diff_tool_path: str) -> "GenericDiffReporter":
        return GenericDiffReporter(create_config(["custom", diff_tool_path]))

    def __init__(self, config: GenericDiffReporterConfig) -> None:
        self.name = config.name
        self.path = self.expand_program_files(config.path)
        self.extra_args = config.extra_args

    def __str__(self) -> str:
        if self.extra_args:
            config = {
                "name": self.name,
                "path": self.path,
                "arguments": self.extra_args,
            }
        else:
            config = {"name": self.name, "path": self.path}

        return to_json(config)

    @staticmethod
    def run_command(command_array):
        with subprocess.Popen(command_array):
            pass

    def get_command(self, received: str, approved: str) -> List[str]:
        return [self.path] + self.extra_args + [received, approved]

    def report(self, received_path: str, approved_path: str) -> bool:
        if not self.is_working():
            return False
        ensure_file_exists(approved_path)
        command_array = self.get_command(received_path, approved_path)
        self.run_command(command_array)
        return True

    def is_working(self) -> bool:
        found = Command(self.path).locate()
        if found:
            self.path = found
        return found

    @staticmethod
    def expand_program_files(path: str) -> str:
        if PROGRAM_FILES not in path:
            return path

        for candidate in [
            r"C:/Program Files",
            r"C:/Program Files (x86)",
            r"C:/ProgramW6432",
        ]:
            possible = path.replace(PROGRAM_FILES, candidate)
            if Command.executable(possible):
                return possible
        return path.replace(PROGRAM_FILES, "C:/Program Files")

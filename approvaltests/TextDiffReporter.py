import os
import subprocess
from approvaltests.Reporter import Reporter


class TextDiffReporter(Reporter):
    DIFF_TOOL_ENVIRONMENT_VARIABLE_NAME = 'APPROVALS_TEXT_DIFF_TOOL'

    @staticmethod
    def run_command(command_array):
        subprocess.call(command_array)

    @classmethod
    def get_command(cls, approved_path, received_path):
        diff_tool = os.environ[cls.DIFF_TOOL_ENVIRONMENT_VARIABLE_NAME]
        return [diff_tool, approved_path, received_path]

    def report(self, approved_path, received_path):
        if not os.path.isfile(approved_path):
            with open(approved_path, 'w') as approved_file:
                pass
        command_array = self.get_command(approved_path, received_path)
        self.run_command(command_array)


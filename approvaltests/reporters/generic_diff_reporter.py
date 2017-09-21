import json
import os
import subprocess

from approvaltests.command import Command
from approvaltests.core.reporter import Reporter


class GenericDiffReporter(Reporter):
    @staticmethod
    def create(diff_tool_path):
        return GenericDiffReporter(['custom', diff_tool_path])

    def __init__(self, config):
        self.name = config[0]
        self.path = config[1]

    def __str__(self):
        return json.dumps(
            {
                'name': self.name,
                'path': self.path
            },
            sort_keys=True,
            indent=4,
            separators=(',', ': ')
        )

    @staticmethod
    def create_empty_file(file_path):
        open(file_path, 'w').close()

    @staticmethod
    def run_command(command_array):
        subprocess.call(command_array)

    def get_command(self, received, approved):
        return [
            self.path,
            received,
            approved
        ]

    def report(self, received_path, approved_path):
        if not self.is_working:
            return False
        if not os.path.isfile(approved_path):
            self.create_empty_file(approved_path)
        command_array = self.get_command(received_path, approved_path)
        self.run_command(command_array)
        return True

    def is_working(self):
        return Command(self.path).locate()

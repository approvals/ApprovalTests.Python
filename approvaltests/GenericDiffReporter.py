import json
import os
import subprocess

from approvaltests.Command import Command
from approvaltests.Reporter import Reporter


class GenericDiffReporter(Reporter):
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
        if not os.path.isfile(approved_path):
            self.create_empty_file(approved_path)
        command_array = self.get_command(received_path, approved_path)
        self.run_command(command_array)

    def is_working(self):
        return Command(self.path).locate()

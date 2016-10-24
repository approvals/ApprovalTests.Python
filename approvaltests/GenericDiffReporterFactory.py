import inspect
import json
import os
from approvaltests.GenericDiffReporter import GenericDiffReporter
from approvaltests.Namer import Namer


class GenericDiffReporterFactory(object):
    reporters = []

    def __init__(self):
        directory = os.path.dirname(inspect.stack(1)[0][1])
        path = os.path.join(directory, 'reporters.json')
        self.load(path)

    def list(self):
        return [r[0] for r in self.reporters]

    def get(self, reporter_name):
        config = next((r for r in self.reporters if r[0] == reporter_name), None)
        if not config:
            return None
        return GenericDiffReporter(config)

    def save(self, file_name):
        with open(file_name, 'w') as f:
            json.dump(
                self.reporters,
                f,
                sort_keys=True,
                indent=2,
                separators=(',', ': ')
            )
        return file_name

    def load(self, file_name):
        with open(file_name, 'r') as f:
            self.reporters = json.load(f)
        return self.reporters

    def get_first_working(self):
        instances = (GenericDiffReporter(r) for r in self.reporters)
        working = (i for i in instances if i.is_working())
        return next(working, None)

    def remove(self, reporter_name):
        self.reporters = [r for r in self.reporters if r[0] != reporter_name]

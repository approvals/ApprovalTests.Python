import json

from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter
from approvaltests.utils import get_adjacent_file


class GenericDiffReporterFactory(object):
    reporters = []

    def __init__(self):
        self.load(get_adjacent_file('reporters.json'))
        self.add_fallback_reporter_config(["PythonNative", "python", [get_adjacent_file("python_native_reporter.py")]])

    def add_default_reporter_config(self, config):
        self.reporters.insert(0, config)

    def add_fallback_reporter_config(self, config):
        self.reporters.append(config)

    def list(self):
        return [r[0] for r in self.reporters]

    def get(self, reporter_name):
        config = next((r for r in self.reporters if r[0] == reporter_name), None)
        return self._create_reporter(config)

    @staticmethod
    def _create_reporter(config):
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
        working = (i for i in self.get_all_reporters() if i.is_working())
        return next(working, None)
    
    def get_all_reporters(self):
        instances = (self._create_reporter(r) for r in self.reporters)
        return instances

    def remove(self, reporter_name):
        self.reporters = [r for r in self.reporters if r[0] != reporter_name]

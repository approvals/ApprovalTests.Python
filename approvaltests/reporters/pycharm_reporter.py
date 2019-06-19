import json

from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter


class PyCharmReporter(GenericDiffReporter):
    def __init__(self, path=None):
        config = ['PyCharm', path or "/Applications/PyCharm CE.app/Contents/MacOS/pycharm"]
        GenericDiffReporter.__init__(self, config)

    def get_command(self, received, approved):
        return [
            self.path,
            "diff",
            received,
            approved
        ]

    def __str__(self):
        return json.dumps(
            {
                'name': self.name,
                'path': self.path,
                'clazz': "PyCharmReporter"
            },
            indent=4,
            separators=(',', ': ')
        )

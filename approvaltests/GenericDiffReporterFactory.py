from approvaltests.GenericDiffReporter import GenericDiffReporter


class GenericDiffReporterFactory(object):
    reporters = [
        ('BeyondCompare4', 'C:/Program Files (x86)/Beyond Compare 4/BCompare.exe'),
        ('WinMerge', 'C:/Program Files (x86)/WinMerge/WinMergeU.exe')
    ]

    def list(self):
        return [r[0] for r in self.reporters]

    def get(self, reporter_name):
        config = next((r for r in self.reporters if r[0] == reporter_name), None)
        if not config:
            return None
        return GenericDiffReporter(config)

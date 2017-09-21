from approvaltests.core.reporter import Reporter


class MultiReporter(Reporter):
    def __init__(self, *reporters):
        self.reporters = reporters

    def report(self, received_path, approved_path):
        for r in self.reporters:
            r.report(received_path, approved_path)

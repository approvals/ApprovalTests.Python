from approvaltests.core.reporter import Reporter


class ReporterForTesting(Reporter):

    def __init__(self):
        self.called = False

    def report(self, approved_path, received_path):
        self.called = True

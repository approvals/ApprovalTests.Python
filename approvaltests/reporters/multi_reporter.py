from approvaltests.core.reporter import Reporter


class MultiReporter(Reporter):
    """
    A reporter that combines a list of
    reporters and calls each of them in
    turn.
    """

    def __init__(self, *reporters):
        self.reporters = reporters

    def report(self, received_path, approved_path):
        for r in self.reporters:
            r.report(received_path, approved_path)

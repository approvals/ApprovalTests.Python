from approvaltests.core.reporter import Reporter


class MultiReporter(Reporter):
    """
    A composite reporter that goes through a list
    of reporters, running all that are working on
    the current machine.

    See also FirstWorkingReporter.
    """

    def __init__(self, *reporters) -> None:
        self.reporters = reporters

    def report(self, received_path, approved_path):
        for r in self.reporters:
            r.report(received_path, approved_path)

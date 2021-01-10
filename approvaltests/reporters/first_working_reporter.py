from approvaltests.core.reporter import Reporter


class FirstWorkingReporter(Reporter):
    """
    A reporter that goes through a list
    of reporters and returns success
    as soon as any reporter returns
    a truish value.

    If no reporter does, this reporter
    returns False, meaning not successful.
    """

    def __init__(self, *reporters):
        self.reporters = reporters

    def report(self, received_path, approved_path):
        for r in self.reporters:
            try:
                success = r.report(received_path, approved_path)
                if success:
                    return True
            except:
                pass

        return False

from approvaltests.core.reporter import Reporter


class FirstWorkingReporter(Reporter):
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

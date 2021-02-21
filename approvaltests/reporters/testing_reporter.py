from approvaltests.core.reporter import Reporter


class ReporterForTesting(Reporter):
    def __init__(self) -> None:
        self.called = False

    def report(self, approved_path: str, received_path: str) -> None:
        self.called = True

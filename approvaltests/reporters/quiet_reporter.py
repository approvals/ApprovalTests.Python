from approvaltests.core import Reporter


class QuietReport(Reporter):
    def report(self, received_path: str, approved_path: str) -> bool:
        pass

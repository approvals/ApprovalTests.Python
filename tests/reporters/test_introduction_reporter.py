from approvaltests import approvals, Reporter
from approvaltests.reporters import PythonNativeReporter


class IntroductionReporter(Reporter):

    def report(self, received_path: str, approved_path: str) -> bool:
        print(self.get_text())
        return PythonNativeReporter().report(received_path, approved_path)

    def get_text(self):
        return '''
        Welcome to ApprovalTests!
        No DiffReporters have been detected on this system.
        To learn more, visit [Introduction to Reporters](https://github.com/approvals/ApprovalTests.Python/blob/main/docs/tutorial/intro-to-reporters.md)
        '''


def test_pycharm_diff_command() -> None:
    reporter = IntroductionReporter()
    approvals.verify(reporter.get_text())
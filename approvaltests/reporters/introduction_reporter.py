from approvaltests.core.reporter import Reporter
from approvaltests.reporters.python_native_reporter import PythonNativeReporter


class IntroductionReporter(Reporter):

    def report(self, received_path: str, approved_path: str) -> bool:
        print(self.get_text())
        return PythonNativeReporter().report(received_path, approved_path)

    @staticmethod
    def get_text():
        return '''
        Welcome to ApprovalTests!
        No DiffReporters have been detected on this system.
        To learn more, visit [Introduction to Reporters](https://github.com/approvals/ApprovalTests.Python/blob/main/docs/tutorial/intro-to-reporters.md)
        '''
    def __str__(self):
        return self.__class__.__name__

    __repr__ = __str__

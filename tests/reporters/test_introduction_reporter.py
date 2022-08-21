from approvaltests import approvals
from approvaltests.reporters.introduction_reporter import IntroductionReporter


def test_pycharm_diff_command() -> None:
    reporter = IntroductionReporter()
    approvals.verify(reporter.get_text())

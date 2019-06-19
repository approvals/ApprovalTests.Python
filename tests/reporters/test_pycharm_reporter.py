
from approvaltests import verify

from approvaltests.reporters.pycharm_reporter import PyCharmReporter


def test_pycharm_diff_command():
    reporter = PyCharmReporter()
    received_path = "received.txt"
    approved_path = "approved.txt"
    verify(str(reporter.get_command(received_path, approved_path)))


def test_override_path():
    reporter = PyCharmReporter(path="foobar")
    received_path = "received.txt"
    approved_path = "approved.txt"
    verify(str(reporter.get_command(received_path, approved_path)))

from approvaltests import verify
from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter, create_config


def test_pycharm_diff_command() -> None:
    reporter = GenericDiffReporter(create_config(
        ["PyCharm", "/Applications/PyCharm CE.app/Contents/MacOS/pycharm", ["diff"]]
    )
    )
    received_path = "received.txt"
    approved_path = "approved.txt"
    verify(str(reporter.get_command(received_path, approved_path)))

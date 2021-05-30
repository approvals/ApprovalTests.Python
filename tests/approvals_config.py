import pytest

from approvaltests import set_default_reporter
from approvaltests.reporters.report_all_to_clipboard import ReporterByCopyMoveCommandForEverythingToClipboard


@pytest.fixture(scope="session", autouse=True)
def set_reporter():
    set_default_reporter(ReporterByCopyMoveCommandForEverythingToClipboard())
    print("HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
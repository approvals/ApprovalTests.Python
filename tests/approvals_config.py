from approvaltests import set_default_reporter
from approvaltests.reporters.report_all_to_clipboard import ReporterByCopyMoveCommandForEverythingToClipboard


def configure_approvaltests():
    print("CONFIGURED _____________________________________________-")
    set_default_reporter(ReporterByCopyMoveCommandForEverythingToClipboard())
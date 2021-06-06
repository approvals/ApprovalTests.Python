from approvaltests import set_default_reporter, DiffReporter
from approvaltests.reporters.report_all_to_clipboard import ReporterByCopyMoveCommandForEverythingToClipboard

my_preferred_reporter = DiffReporter

# begin-snippet: configure_approvaltests
def configure_approvaltests():
    set_default_reporter(my_preferred_reporter)
    # end-snippet
    # begin-snippet: default_reporter
    set_default_reporter(ReporterByCopyMoveCommandForEverythingToClipboard())
    # end-snippet

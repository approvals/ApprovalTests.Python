from itertools import chain

from approvaltests.reporters.generic_diff_reporter_factory import (
    GenericDiffReporterFactory,
)
from .python_native_reporter import PythonNativeReporter
from .first_working_reporter import FirstWorkingReporter
from .report_with_diff_command_line import ReportWithDiffCommandLine
from .report_with_vscode import ReportWithVSCode


class DiffReporter(FirstWorkingReporter):
    """
    The DiffReporter class goes through a chain of possible diffing tools,
    to find the first option installed on your system.

    If none are found, it falls back to writing the diffs on
    the console.

    At present, the default Reporter is the DiffReporter.
    """

    def __init__(self, reporter_factory=None):
        factory = reporter_factory or GenericDiffReporterFactory()

        reporters = list(factory.get_all_reporters())
        reporters.extend([
            ReportWithVSCode(),
            ReportWithDiffCommandLine(),
            PythonNativeReporter(),
        ])
        super(__class__, self).__init__(*reporters)

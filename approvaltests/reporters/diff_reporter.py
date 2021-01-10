from .first_working_reporter import FirstWorkingReporter
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
from .python_native_reporter import PythonNativeReporter


class DiffReporter(FirstWorkingReporter):
    """
    A reporter that first goes through
    the given list of reporters, then,
    as a fallback uses the builtin
    PythonNative reporter, meaning
    this reporter *should* never fail.
    """

    def __init__(self, reporter_factory=None):
        factory = reporter_factory or GenericDiffReporterFactory()
        
        reporters = list(factory.get_all_reporters())
        reporters.append(PythonNativeReporter())
        super(DiffReporter, self).__init__(*reporters)

from .first_working_reporter import FirstWorkingReporter
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
from .python_native_reporter import PythonNativeReporter


class DiffReporter(FirstWorkingReporter):
    def __init__(self, reporter_factory=None):
        factory = reporter_factory or GenericDiffReporterFactory()
        
        reporters = list(factory.get_all_reporters())
        reporters.append(PythonNativeReporter())
        super(DiffReporter, self).__init__(*reporters)

from .first_working_reporter import FirstWorkingReporter
from .clipboard_reporter import CommandLineReporter
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory


class DiffReporter(FirstWorkingReporter):
    def __init__(self):
        factory = GenericDiffReporterFactory()
        
        reporters = list(factory.get_all_reporters())
        reporters.append(CommandLineReporter())
        super(DiffReporter, self).__init__(*reporters)

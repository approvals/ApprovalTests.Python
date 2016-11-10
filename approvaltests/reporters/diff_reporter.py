from .first_working_reporter import FirstWorkingReporter
from .clipboard_reporter import CommandLineReporter
from ..GenericDiffReporterFactory import GenericDiffReporterFactory


class DiffReporter(FirstWorkingReporter):
    def __init__(self):
        factory = GenericDiffReporterFactory()
        
        reporters = list(factory.get_all_reporters())
        reporters.append(CommandLineReporter())
        super(DiffReporter, self).__init__(*reporters)

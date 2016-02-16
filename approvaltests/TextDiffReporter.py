import os

from approvaltests.GenericDiffReporter import GenericDiffReporter
from approvaltests.ReporterMissingException import ReporterMissingException


class TextDiffReporter(GenericDiffReporter):
    DIFF_TOOL_ENVIRONMENT_VARIABLE_NAME = 'APPROVALS_TEXT_DIFF_TOOL'

    def __init__(self):
        if self.DIFF_TOOL_ENVIRONMENT_VARIABLE_NAME not in os.environ:
            raise ReporterMissingException(self.DIFF_TOOL_ENVIRONMENT_VARIABLE_NAME)
        diff_tool = os.environ[self.DIFF_TOOL_ENVIRONMENT_VARIABLE_NAME]
        super(TextDiffReporter, self).__init__(('Custom', diff_tool))

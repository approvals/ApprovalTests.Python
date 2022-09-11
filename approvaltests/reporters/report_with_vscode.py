from .generic_diff_reporter import GenericDiffReporter, create_config


class ReportWithVSCode(GenericDiffReporter):
    def __init__(self):
        super().__init__(config=create_config(["ReportWithVSCode", "code", ["-d"]]))

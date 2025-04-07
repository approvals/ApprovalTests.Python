from approvaltests.reporters import FirstWorkingReporter, ReportWithBeyondCompare


class ReportWithDiffToolOnWindows(FirstWorkingReporter):

    def __init__(self):
        super().__init__(ReportWithBeyondCompare())

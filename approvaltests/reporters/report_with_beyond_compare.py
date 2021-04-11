from approvaltests.reporters.first_working_reporter import FirstWorkingReporter
from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter, GenericDiffReporterConfig


class ReportWithBeyondCompareLinux(GenericDiffReporter):
    def __init__(self):
        super().__init__(
            config=GenericDiffReporterConfig(name= self.__class__.__name__,
            path= "/usr/bin/bcompare")
        )



class ReportWithBeyondCompareMac(GenericDiffReporter):
    def __init__(self):
        super().__init__(
            config=GenericDiffReporterConfig(name= self.__class__.__name__,
            path= "/usr/bin/bcompare")
        )



class ReportWithBeyondCompareWindows(GenericDiffReporter):
    def __init__(self):
        super().__init__(
            config=GenericDiffReporterConfig(name= self.__class__.__name__,
            path= "{ProgramFiles}/Beyond Compare 4/BCompare.exe")
        )



class ReportWithBeyondCompare(FirstWorkingReporter):
    def __init__(self):
        super().__init__(
            ReportWithBeyondCompareMac(),
            ReportWithBeyondCompareWindows(),
            ReportWithBeyondCompareLinux()
        )


def report_with_beyond_compare() -> ReportWithBeyondCompare:
    return ReportWithBeyondCompare()
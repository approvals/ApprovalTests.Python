import unittest

from approvaltests import verify_all
from approvaltests.reporters import GenericDiffReporterFactory, get_command_text
from approvaltests.reporters.default_reporter_factory import (
    get_default_reporter,
    set_default_reporter,
)
from approvaltests.reporters.received_file_launcher_reporter import (
    ReceivedFileLauncherReporter,
)
from approvaltests.reporters.report_with_beyond_compare import (
    ReportWithBeyondCompare,
    report_with_beyond_compare,
)


class ReporterTests(unittest.TestCase):
    def test_file_launcher(self):
        reporter = ReceivedFileLauncherReporter()
        command = reporter.get_command("b.txt")
        self.assertEqual(command, ["cmd", "/C", "start", "b.txt", "/B"])

    def test_different_ways_of_creating_reporter(self):
        reporter1 = GenericDiffReporterFactory().get("BeyondCompare")
        reporter2 = ReportWithBeyondCompare()
        reporter3 = report_with_beyond_compare()
        assert reporter1 == reporter2 == reporter3

    def test_move_command(self):
        verify_all("", [True, False], lambda b: get_command_text("a.text", "r.txt", b))

    def test_set_default_reporter(self):
        old = get_default_reporter()
        set_default_reporter(ReportWithBeyondCompare())

        new = get_default_reporter()

        assert "ReportWithBeyondCompare" == new.__class__.__name__
        assert old != new
        set_default_reporter(old)

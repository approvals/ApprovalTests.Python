import os
import unittest
from unittest.mock import patch

from approvaltests.reporters.diff_reporter import DiffReporter
from approvaltests.reporters.environment_variable_reporter import (
    EnvironmentVariableReporter,
)
from approvaltests.reporters.multi_reporter import MultiReporter
from approvaltests.reporters.report_quietly import ReportQuietly

ENV_VAR = EnvironmentVariableReporter.ENVIRONMENT_VARIABLE_NAME


class EnvironmentVariableReporterTests(unittest.TestCase):
    def test_no_env_var_set(self) -> None:
        with patch.dict(os.environ, {}):
            os.environ.pop(ENV_VAR, None)
            reporter = EnvironmentVariableReporter()
            self.assertIsNone(reporter.get_reporter())

    def test_report_returns_false_when_not_configured(self) -> None:
        with patch.dict(os.environ, {}):
            os.environ.pop(ENV_VAR, None)
            self.assertFalse(EnvironmentVariableReporter().report("r.txt", "a.txt"))

    def test_single_reporter_name(self) -> None:
        with patch.dict(os.environ, {ENV_VAR: "QuietReporter"}):
            reporter = EnvironmentVariableReporter()
            self.assertIsInstance(reporter.get_reporter(), ReportQuietly)

    def test_multiple_reporter_names_wraps_in_multi_reporter(self) -> None:
        with patch.dict(os.environ, {ENV_VAR: "QuietReporter,DiffReporter"}):
            reporter = EnvironmentVariableReporter()
            self.assertIsInstance(reporter.get_reporter(), MultiReporter)

    def test_unknown_reporter_name_is_skipped(self) -> None:
        with patch.dict(os.environ, {ENV_VAR: "UnknownReporter,QuietReporter"}):
            reporter = EnvironmentVariableReporter()
            self.assertIsInstance(reporter.get_reporter(), ReportQuietly)

    def test_all_unknown_names_gives_none(self) -> None:
        with patch.dict(os.environ, {ENV_VAR: "UnknownReporter"}):
            reporter = EnvironmentVariableReporter()
            self.assertIsNone(reporter.get_reporter())

    def test_get_reporter_mapping_contains_expected_keys(self) -> None:
        mapping = EnvironmentVariableReporter().get_reporter_mapping()
        self.assertIn("AutoApproveReporter", mapping)
        self.assertIn("DiffReporter", mapping)
        self.assertIn("QuietReporter", mapping)

    def test_get_reporter_mapping_returns_copy(self) -> None:
        reporter = EnvironmentVariableReporter()
        mapping = reporter.get_reporter_mapping()
        mapping["NewKey"] = DiffReporter
        self.assertNotIn("NewKey", reporter.get_reporter_mapping())

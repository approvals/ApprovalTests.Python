import os
import platform
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from typing_extensions import override

from approvaltests.reporters.report_by_opening_files import ReportByOpeningFiles


class TestReportByOpeningFiles(unittest.TestCase):
    @override
    def setUp(self) -> None:
        self.reporter = ReportByOpeningFiles()
        self.temp_dir = tempfile.mkdtemp()

    @override
    def tearDown(self) -> None:
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_is_non_empty_file_with_content(self) -> None:
        temp_file = os.path.join(self.temp_dir, "test.txt")
        Path(temp_file).write_text("content")

        self.assertTrue(self.reporter.is_non_empty_file(temp_file))

    def test_is_non_empty_file_with_empty_file(self) -> None:
        temp_file = os.path.join(self.temp_dir, "empty.txt")
        Path(temp_file).touch()

        self.assertFalse(self.reporter.is_non_empty_file(temp_file))

    def test_is_non_empty_file_with_nonexistent_file(self) -> None:
        nonexistent = os.path.join(self.temp_dir, "nonexistent.txt")

        self.assertFalse(self.reporter.is_non_empty_file(nonexistent))

    @patch("approvaltests.reporters.report_by_opening_files.ReportByOpeningFiles.display_file")
    def test_report_opens_both_files_when_approved_is_non_empty(
        self, mock_display: MagicMock
    ) -> None:
        received_file = os.path.join(self.temp_dir, "received.txt")
        approved_file = os.path.join(self.temp_dir, "approved.txt")
        Path(received_file).write_text("received content")
        Path(approved_file).write_text("approved content")

        result = self.reporter.report(received_file, approved_file)

        self.assertTrue(result)
        self.assertEqual(2, mock_display.call_count)
        mock_display.assert_any_call(approved_file)
        mock_display.assert_any_call(received_file)

    @patch("approvaltests.reporters.report_by_opening_files.ReportByOpeningFiles.display_file")
    def test_report_only_opens_received_when_approved_is_empty(
        self, mock_display: MagicMock
    ) -> None:
        received_file = os.path.join(self.temp_dir, "received.txt")
        approved_file = os.path.join(self.temp_dir, "approved.txt")
        Path(received_file).write_text("received content")
        Path(approved_file).touch()

        result = self.reporter.report(received_file, approved_file)

        self.assertTrue(result)
        self.assertEqual(1, mock_display.call_count)
        mock_display.assert_called_once_with(received_file)

    @patch("approvaltests.reporters.report_by_opening_files.ReportByOpeningFiles.display_file")
    def test_report_only_opens_received_when_approved_does_not_exist(
        self, mock_display: MagicMock
    ) -> None:
        received_file = os.path.join(self.temp_dir, "received.txt")
        approved_file = os.path.join(self.temp_dir, "nonexistent.txt")
        Path(received_file).write_text("received content")

        result = self.reporter.report(received_file, approved_file)

        self.assertTrue(result)
        self.assertEqual(1, mock_display.call_count)
        mock_display.assert_called_once_with(received_file)

    @patch("approvaltests.reporters.report_by_opening_files.ReportByOpeningFiles.display_file")
    @patch("approvaltests.reporters.report_by_opening_files.SimpleLogger.warning")
    def test_report_returns_false_and_logs_on_exception(
        self, mock_warning: MagicMock, mock_display: MagicMock
    ) -> None:
        mock_display.side_effect = Exception("Failed to open file")

        received_file = os.path.join(self.temp_dir, "received.txt")
        approved_file = os.path.join(self.temp_dir, "approved.txt")
        Path(received_file).write_text("content")
        Path(approved_file).write_text("content")

        result = self.reporter.report(received_file, approved_file)

        self.assertFalse(result)
        mock_warning.assert_called_once()
        call_args = mock_warning.call_args
        self.assertEqual("Failed to open files", call_args[0][0])
        self.assertIsInstance(call_args[1]["exception"], Exception)

def test_current_os_is_known():
    ReportByOpeningFiles.get_opening_command("text.txt", platform.system())

def test_unknown_os():
    with pytest.raises(KeyError):
        ReportByOpeningFiles.get_opening_command("text.txt", "unknown")

def test_get_opening_command():
    assert ["start", "text.txt"] == ReportByOpeningFiles.get_opening_command("text.txt", "Windows")
    assert ["open", "text.txt"] == ReportByOpeningFiles.get_opening_command("text.txt", "Darwin")
    assert ["xdg-open", "text.txt"] == ReportByOpeningFiles.get_opening_command("text.txt", "Linux")
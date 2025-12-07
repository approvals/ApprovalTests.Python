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



    def test_is_non_empty_file_with_empty_file(self) -> None:
        temp_file = os.path.join(self.temp_dir, "empty.txt")
        Path(temp_file).touch()

        self.assertFalse(self.reporter.is_non_empty_file(temp_file))

    def test_is_non_empty_file_with_nonexistent_file(self) -> None:
        nonexistent = os.path.join(self.temp_dir, "nonexistent.txt")

        self.assertFalse(self.reporter.is_non_empty_file(nonexistent))

def test_is_non_empty_file_with_content() -> None:
    assert ReportByOpeningFiles.is_non_empty_file(__file__)

def test_current_os_is_known():
    ReportByOpeningFiles.get_opening_command("text.txt", platform.system())

def test_unknown_os():
    with pytest.raises(KeyError):
        ReportByOpeningFiles.get_opening_command("text.txt", "unknown")

def test_get_opening_command():
    assert ["start", "text.txt"] == ReportByOpeningFiles.get_opening_command("text.txt", "Windows")
    assert ["open", "text.txt"] == ReportByOpeningFiles.get_opening_command("text.txt", "Darwin")
    assert ["xdg-open", "text.txt"] == ReportByOpeningFiles.get_opening_command("text.txt", "Linux")
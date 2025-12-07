import os
import platform
import shutil
import tempfile

import pytest

from approval_utilities import utils
from approvaltests.reporters.report_by_opening_files import ReportByOpeningFiles


def test_is_non_empty_file_with_empty_file() -> None:
    temp_dir = tempfile.mkdtemp()
    temp_file = os.path.join(temp_dir, "empty.txt")
    utils.create_empty_file(temp_file)
    assert not ReportByOpeningFiles.is_non_empty_file(temp_file)

    shutil.rmtree(temp_dir, ignore_errors=True)


def test_is_non_empty_file() -> None:
    assert ReportByOpeningFiles.is_non_empty_file(__file__)


def test_is_non_missing_file() -> None:
    assert not ReportByOpeningFiles.is_non_empty_file("non_existent.txt")


def test_current_os_is_known() -> None:
    ReportByOpeningFiles.get_opening_command("text.txt", platform.system())


def test_unknown_os() -> None:
    with pytest.raises(KeyError):
        ReportByOpeningFiles.get_opening_command("text.txt", "unknown")


def test_get_opening_command() -> None:
    assert ["start", "text.txt"] == ReportByOpeningFiles.get_opening_command(
        "text.txt", "Windows"
    )
    assert ["open", "text.txt"] == ReportByOpeningFiles.get_opening_command(
        "text.txt", "Darwin"
    )
    assert ["xdg-open", "text.txt"] == ReportByOpeningFiles.get_opening_command(
        "text.txt", "Linux"
    )

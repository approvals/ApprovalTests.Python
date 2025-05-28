from unittest.mock import MagicMock, patch

from approvaltests.reporters.report_with_opening_file import ReportWithOpeningFile


def test_get_command_darwin() -> None:
    with patch("platform.system", return_value="Darwin"):
        command = ReportWithOpeningFile.get_command("test.txt")
        assert command == ["open", "test.txt"]


def test_get_command_windows() -> None:
    with patch("platform.system", return_value="Windows"):
        command = ReportWithOpeningFile.get_command("test.txt")
        assert command == ["start", "test.txt"]


def test_get_command_linux() -> None:
    with patch("platform.system", return_value="Linux"):
        command = ReportWithOpeningFile.get_command("test.txt")
        assert command == ["xdg-open", "test.txt"]


def test_get_command_unknown_system() -> None:
    with patch("platform.system", return_value="UnknownOS"):
        command = ReportWithOpeningFile.get_command("test.txt")
        assert command == ["xdg-open", "test.txt"]


@patch("subprocess.call")
def test_report_calls_command(mock_call: MagicMock) -> None:
    reporter = ReportWithOpeningFile()
    with patch("platform.system", return_value="Darwin"):
        result = reporter.report("received.txt", "approved.txt")
        mock_call.assert_called_once_with(["open", "received.txt"])
        assert result is True
